from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Class được phép chỉnh sửa dành cho sinh viên."""

    def __init__(self, client: Any):
        self.client = client
        # Khởi tạo bộ quản lý ngân sách token dựa trên cấu hình hệ thống
        self.budget = ContextBudgetManager(settings.context_tokens)

    # LƯU Ý: Đồ thị Zep giới hạn độ dài truy vấn tối đa 400 ký tự.
    # Hàm cap_query() sẽ được dùng để cắt gọn query trước khi gọi API graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # 1. Kích hoạt thread với câu query hiện tại để Zep nhận diện được ngữ cảnh
        prime_eval_thread(self.client, user_id, thread_id, query)

        # 2. Lấy khối thông tin tóm tắt (Context Block) của người dùng trong thread
        ctx_obj = self.client.thread.get_user_context(thread_id=thread_id)
        summary_block = getattr(ctx_obj, "context", "") or ""

        # 3. Truy xuất thêm các sự kiện (facts) từ đồ thị để tránh lọt thông tin quan trọng
        safe_query = cap_query(query)
        try:
            graph_data = self.client.graph.search(
                user_id=user_id,
                query=safe_query,
                scope="edges",
                limit=20,
            )
            retrieved_facts = render_graph_search(graph_data)
        except Exception:
            # Nếu có lỗi trong quá trình lấy fact thì bỏ qua (trả về chuỗi rỗng)
            retrieved_facts = ""

        # 4. Gộp kết quả: Đặt tóm tắt (summary) lên trên facts để ưu tiên giữ lại khi bị cắt bớt
        return join_nonempty([summary_block, retrieved_facts], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # Tìm lại các đoạn tin nhắn gốc (episodes) trong đồ thị cá nhân của user
        search_res = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        # Ép độ dài mỗi episode xuống tối đa 180 ký tự để nhồi nhét được nhiều kết quả vào mức budget 3%
        return render_graph_search(search_res, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        capped_q = cap_query(query)
        
        try:
            # Tìm kiếm trên graph dùng chung (graph_id) để lấy văn bản tài liệu nguyên bản
            raw_results = self.client.graph.search(
                graph_id=graph_id,
                query=capped_q,
                scope="episodes",
                limit=8,
            )
        except Exception:
            # Phương án dự phòng: Nếu không lấy được episodes thì chuyển sang lấy thực thể (nodes)
            raw_results = self.client.graph.search(
                graph_id=graph_id,
                query=capped_q,
                scope="nodes",
                limit=8,
            )
            
        # Không cắt giảm số lượng ký tự ở bước này để tránh làm mất các marker quan trọng ở cuối văn bản
        return render_graph_search(raw_results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # Giao phó toàn bộ công việc phân bổ ngân sách (với tỷ lệ 10/4/3/3 và thứ tự ưu tiên) 
        # cho ContextBudgetManager xử lý.
        return self.budget.assemble(layers)