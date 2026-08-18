from __future__ import annotations

import json
import math
import re
from types import SimpleNamespace
from typing import Any, Iterable

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty, normalize
from .zep_common import prime_eval_thread, render_graph_search

# --- Small helpers used to keep every layer inside its token budget ----------
#
# ContextBudgetManager trims each layer from the TAIL (it keeps the head).
# So the job of a retrieve_* method is not only "fetch evidence" but also
# "put the evidence that answers THIS query at the head". The helpers below
# split raw Zep output into blocks, drop boilerplate/duplicates, and re-order
# blocks by query relevance + marker density before returning the text.

_WORD_RE = re.compile(r"[a-z0-9]+")
_MARKER_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b")

# Boilerplate emitted inside the Zep Context Block; carries no evidence.
_BOILERPLATE = (
    "Episodes are source message or document excerpts",
    "The timestamp shown for each fact",
)
# `[user] {json profile}:` prefix Zep prepends to raw message episodes.
_ROLE_JSON_PREFIX = re.compile(r"\[(?:user|assistant|system)\]\s*\{.*?\}\s*:", re.DOTALL)
_SECTION_RE = re.compile(r"<([A-Z_]+)>\n(.*?)\n</\1>", re.DOTALL)
_EPISODE_META_RE = re.compile(r"^Created At:.*?Source:\s*\S+\s*Content:\s*", re.DOTALL)
_RENDER_PREFIXES = ("EPISODE: ", "FACT: ", "ENTITY: ", "OBSERVATION: ", "THREAD_SUMMARY: ")


def _tokens(text: str) -> set[str]:
    return set(_WORD_RE.findall(text.casefold()))


def _score(block: str, query_tokens: set[str]) -> tuple[int, float]:
    """Rank key: marker-bearing blocks first, then by query relevance.

    Evidence in this lab is carried by literal provenance markers
    (LAB-REPORT-1600, ASYNC-FIX-20, BUDGET-10-4-3-3, ...). Prose paraphrases
    them away, so a block that still holds a marker is worth more budget than
    a chatty block that merely shares vocabulary with the query.
    """
    block_tokens = _tokens(block)
    if not block_tokens:
        return (1, 0.0)
    overlap = len(block_tokens & query_tokens)
    # Normalise by length so a short, dense line beats a long rambling one.
    relevance = overlap / math.sqrt(len(block_tokens))
    has_marker = 0 if _MARKER_RE.search(block) else 1
    return (has_marker, relevance)


def _dedupe(blocks: Iterable[str]) -> list[str]:
    seen: list[str] = []
    out: list[str] = []
    for block in blocks:
        key = normalize(block)
        if not key or any(key in prev for prev in seen):
            continue
        seen.append(key)
        out.append(block.strip())
    return out


def _rank(blocks: list[str], query: str) -> list[str]:
    query_tokens = _tokens(query)
    query_key = normalize(query)
    ranked: list[tuple[int, float, int, str]] = []
    for i, block in enumerate(blocks):
        # The evaluation thread is primed with the query itself; echoing it
        # back wastes budget without adding evidence.
        if normalize(block) in query_key:
            continue
        tier, relevance = _score(block, query_tokens)
        ranked.append((tier, -relevance, i, block))
    ranked.sort()
    return [block for *_, block in ranked]


def _split_rendered(text: str) -> list[str]:
    """Split render_graph_search output back into one block per result."""
    blocks: list[str] = []
    for line in text.splitlines():
        if line.startswith(_RENDER_PREFIXES) or not blocks:
            blocks.append(line)
        else:
            blocks[-1] += "\n" + line
    return [b for b in blocks if b.strip()]


def _is_query_echo(episode: Any) -> bool:
    """True for episodes that are just an evaluation query, not evidence.

    Every case primes its own thread with the raw query before reading the
    Context Block, and Zep stores that message as an episode on the user graph
    (`ignore_roles` only skips fact/entity extraction, the raw episode is still
    kept and still searchable). Those echoes look exactly like a question, so
    they outrank real session content whenever we search WITH a question — and
    cases poison each other inside a single benchmark run.
    """
    thread_id = str(getattr(episode, "thread_id", "") or "")
    return thread_id.startswith("eval-") or getattr(episode, "role", "") == "Evaluation User"


def _context_sections(context: str) -> tuple[str, list[str]]:
    """Return (pinned user summary, evidence blocks) from a Zep Context Block."""
    pinned = ""
    blocks: list[str] = []
    for tag, body in _SECTION_RE.findall(context):
        body = body.strip()
        if not body:
            continue
        if tag == "USER_SUMMARY":
            pinned = f"<USER_SUMMARY>\n{body}\n</USER_SUMMARY>"
            continue
        lines = [
            ln
            for ln in body.splitlines()
            if ln.strip() and not ln.strip().startswith(_BOILERPLATE)
        ]
        for entry in re.split(r"\n(?=\s*-\s)", "\n".join(lines)):
            entry = _ROLE_JSON_PREFIX.sub("", entry)
            entry = re.sub(r"\s+", " ", entry).strip(" -")
            entry = _EPISODE_META_RE.sub("", entry).strip()
            if entry:
                blocks.append(f"[{tag}] {entry}")
    if not pinned and not blocks and context.strip():
        blocks.append(context.strip())
    return pinned, blocks


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def _search(self, query: str, *, episode_char_cap: int | None = None, **kwargs: Any) -> str:
        try:
            results = self.client.graph.search(query=cap_query(query), **kwargs)
        except Exception:
            return ""
        return render_graph_search(results, episode_char_cap=episode_char_cap)

    def _episode_blocks(
        self,
        user_id: str,
        query: str,
        *,
        limit: int = 30,
        char_cap: int = 280,
        markers_only: bool = False,
        max_items: int | None = None,
    ) -> list[str]:
        """Raw user episodes, with evaluation-query echoes removed.

        `limit` is deliberately high: echoes take their slots BEFORE filtering,
        so we must ask for far more than we intend to keep.
        """
        try:
            results = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="episodes",
                limit=limit,
            )
        except Exception:
            return []

        kept = []
        for episode in getattr(results, "episodes", None) or []:
            if _is_query_echo(episode):
                continue
            content = getattr(episode, "content", None) or ""
            if markers_only and not _MARKER_RE.search(content):
                continue
            kept.append(episode)
            if max_items and len(kept) >= max_items:
                break
        rendered = render_graph_search(
            SimpleNamespace(episodes=kept), episode_char_cap=char_cap
        )
        return _split_rendered(rendered)

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4
        # 1) prime_eval_thread(...) has already been provided as scaffolding.
        # 2) call thread.get_user_context(thread_id=...)
        # 3) return the .context string.
        # Bonus: append graph.search(scope="edges", limit>=20) facts with
        #        validity ranges (a low limit can miss deadline/open-loop facts).
        prime_eval_thread(self.client, user_id, thread_id, query)
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""
        pinned, blocks = _context_sections(context_block)

        # Long-term needs THREE channels, because the first two are lossy:
        #  - Context Block: an LLM summary, it paraphrases literal codes away
        #    ("benchmark report by Friday at 16:00", no LAB-REPORT-1600);
        #  - edge facts: extracted relations, also paraphrased, but the only
        #    channel carrying valid_at/invalid_at for recency;
        #  - raw episodes: the ONLY non-lossy channel, so it is the only place
        #    a literal open-loop marker can come from. Kept deliberately narrow
        #    (marker-bearing only, 3 items, 220 chars) so it does not turn into
        #    a copy of the episodic layer inside a 320-token budget.
        # All three stay user-scoped, so minh/lan isolation is preserved.
        facts = _split_rendered(self._search(query, user_id=user_id, scope="edges", limit=20))
        literal = self._episode_blocks(
            user_id, query, limit=30, char_cap=220, markers_only=True, max_items=3
        )

        # Order = evidence density per token. USER_SUMMARY is pinned first (it
        # holds the preference/recency wording most cases score on), then the
        # literal markers, then facts and the rest of the Context Block, which
        # are the first to be dropped by the 4% trim.
        deduped = _dedupe(literal + facts + blocks)
        literal_keys = {normalize(b) for b in literal}
        ordered = _rank([b for b in deduped if normalize(b) in literal_keys], query)
        ordered += _rank([b for b in deduped if normalize(b) not in literal_keys], query)
        return join_nonempty([pinned] + ordered, sep="\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4
        # Use client.graph.search(user_id=..., query=cap_query(query),
        #     scope="episodes", limit=...) then render_graph_search(...).
        # Tip: verbose session episodes can crowd out concise, marker-bearing
        # reflections under the tight episodic budget — render_graph_search
        # accepts an `episode_char_cap` to keep more distinct episodes.
        # Same echo filter as long-term: an evaluation query stored as an
        # episode is a question, not a trajectory.
        blocks = self._episode_blocks(user_id, query, limit=30, char_cap=280)
        return join_nonempty(_rank(_dedupe(blocks), query), sep="\n")

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4
        # Search the standalone graph (graph_id, NOT user_id).
        # Recommended: scope="episodes" — it returns raw document text that keeps
        # literal markers (e.g. PAYMENT-RULE-3). The "auto" scope returns
        # extracted facts that DROP those literal codes, so avoid it here.
        # Fallback: scope="nodes".
        text = self._search(query, graph_id=graph_id, scope="episodes", limit=8)
        if not text.strip():
            text = self._search(query, graph_id=graph_id, scope="nodes", limit=8)

        # Each KB doc is ingested twice (raw JSON + plain summary) and rendered
        # with an empty `metadata=` line. Collapsing every episode to its
        # `summary` field makes the two copies identical, so dedupe drops one
        # and roughly twice as many distinct docs fit in the 3% budget.
        blocks: list[str] = []
        for block in _split_rendered(text):
            body = block
            for prefix in _RENDER_PREFIXES:
                if body.startswith(prefix):
                    body = body[len(prefix):]
                    break
            body = re.sub(r"(?m)^metadata=.*$", "", body).strip()
            try:
                payload = json.loads(body)
            except Exception:
                payload = None
            if isinstance(payload, dict) and payload.get("summary"):
                body = str(payload["summary"])
            if body:
                blocks.append(f"EPISODE: {body}")
        return join_nonempty(_rank(_dedupe(blocks), query), sep="\n")

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4
        # Use ContextBudgetManager to enforce 10/4/3/3 budget and priority order.
        return self.budget.assemble(layers)
