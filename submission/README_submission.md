# Lab 17 - Submission Report

## Phân tích benchmark

11/11 case pass (`memory_hit_rate=1.0`, `avg_latency_ms=1127.4`, `avg_token_reduction=0.2085`, theo `reports/benchmark.json`). Không case nào fail nên xét "yếu nhất" theo chi phí: layer **long_term** nặng nhất - Context Block trả về nguyên user summary + facts + entities + threads (E02=2334ms/916tok, E03=1093.5ms/920tok, E08=1768.5ms/918tok, E09=1159ms/611tok), thay vì vài dòng marker như episodic/semantic.

Query retrieve nhiều token nhất: **E03** ("Minh còn open loop hay deadline nào chưa hoàn thành?") = **920 tokens** (sát E08=918, E02=916) - cả ba thuộc long_term.

**E07** (mixed) cần kết hợp **long_term + semantic**: `budget_breakdown` cho thấy `long_term.used_tokens=324`, `semantic.used_tokens=148`, còn `short_term`/`episodic`=0. Hai evidence bắt buộc: **preference Python cá nhân của Minh** (long_term) và **PAYMENT-RULE-3** - Idempotency-Key, exponential-backoff, max-3-retries (semantic).

Token reduction trung bình **20.85%**; cao nhất ở episodic/semantic có marker ngắn (E11=74.2%, E06=67.8%, E05=42.5%) vì chỉ lấy đoạn chứa marker. Long_term reduction=0.0 vì Context Block cố ý giữ nguyên dữ liệu, đánh đổi token lấy độ chính xác recency/isolation. "No-memory" sẽ reduction rất cao nhưng hit rate thấp vì thiếu dữ liệu khớp `must_contain_all`.

## Reflection bắt buộc

**Layer quan trọng nhất: episodic**, vì là layer duy nhất trả lời "lần trước đã làm gì" với đầy đủ trajectory. Minh họa qua **E04/E05**: E04 lấy đúng `ASYNC-FIX-20` + `ClientSession` + `concurrency=20`; E05 phân biệt "tăng timeout" (thất bại) với "connection churn" (root cause).

**Trade-off Context Block vs Redis+Qdrant:** Context Block là managed - tự extract fact/edge, xử lý bi-temporal invalidation, nhưng latency cao (1-3s), ít kiểm soát token. Redis+Qdrant tự build - latency thấp, kiểm soát được schema/budget, nhưng phải tự viết dedupe/decay/temporal logic.

**Guardrail chống memory poisoning:** `heartbeat.py` chỉ dedupe note, đánh dấu stale task, tạo recap - **không tự thêm instruction/quyền mới**. Mọi durable write phải qua `require_memory_consent` + `can_write_type`, PII bị redact trước khi ingest (`minimize_pii`).

**E08/E09 - scope-specific conflict:** cùng Minh nhưng 2 project đòi Python ngược nhau (ORCHID-27 dùng Python, BLUEBIRD-42 cấm Python/bắt buộc NestJS) - Context Block giữ song song cả hai. **E10 - durable constraint qua compaction:** `REVIEW-DEADLINE-1600` nằm trong `DURABLE_NOTES`, sống sót qua 8 lần compaction/6 filler turn, cho thấy short-term phân biệt được constraint cần giữ với filler có thể bị nén.

## Ảnh minh chứng

- `long_term.png`: E02/E03/E08/E09 PASS.
- `episodic.png`: E04/E05 PASS.
- `semantic.png`: E06/E11 PASS.
- `privacy.png`: `src.forget` + `--verify-only` -> `Zep user absent: True`, `Redis user keys remaining: 0`, semantic KB dùng chung không bị xóa.
