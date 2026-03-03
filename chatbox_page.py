# ============================================================
# chatbox_page.py — Chatbox AI + UX cải thiện
# ============================================================
import requests, time
import streamlit as st
from config import GROQ_API_URL, GROQ_MODEL, get_groq_headers

_SYSTEM_PROMPT = """Bạn là trợ lý AI thông minh hỗ trợ học sinh ôn thi tại web AI Exam Generator.
Bạn có thể:
1. HƯỚNG DẪN SỬ DỤNG WEB: Giải thích các tính năng (làm bài, xem lịch sử, cài đặt...)
2. GIẢI BÀI TẬP: Hướng dẫn giải Toán, Vật Lý, Hóa Học, Sinh Học, Ngữ Văn, Tiếng Anh cấp THPT
3. TRẢ LỜI CÂU HỎI CHUNG: Về học tập, thi cử, phương pháp học

Quy tắc:
- Trả lời bằng tiếng Việt (trừ khi hỏi tiếng Anh)
- Giải thích rõ ràng, từng bước, dễ hiểu
- Không làm bài thay hoàn toàn — hướng dẫn để học sinh tự hiểu

Thông tin web: 6 môn (Toán, Văn, Anh, Lý, Hóa, Sinh), Lớp 9→ĐH, 10 câu/đề, có đồng hồ đếm ngược.
"""

_QUICK_QUESTIONS = [
    ("🌐", "Cách sử dụng web này?"),
    ("📊", "Xem lịch sử bài thi ở đâu?"),
    ("📐", "Giải thích công thức đạo hàm"),
    ("⚗️", "Phân biệt axit và bazơ"),
    ("🇬🇧", "Cách làm bài thì hiện tại hoàn thành"),
    ("🎲", "Cách tính xác suất lớp 12"),
]

_CHAT_CSS = """
<style>
.chat-layout { display:flex; gap:1rem; height:calc(100vh - 140px); min-height:500px; }

/* Sidebar */
.conv-sidebar {
    width:230px; flex-shrink:0; display:flex; flex-direction:column;
    background:#eef3fd; border:1px solid #93c5fd; border-radius:12px;
    padding:.75rem; overflow:hidden;
}
.conv-sidebar-label {
    font-size:.68rem; font-weight:700; color:#1557b0;
    letter-spacing:.08em; text-transform:uppercase; margin:.5rem 0 .4rem;
}
.conv-list { flex:1; overflow-y:auto; }
.conv-row { display:flex; align-items:center; gap:.3rem; margin-bottom:3px; }
.conv-btn-active {
    flex:1; background:#1557b0; border:1px solid #0d47a1;
    border-radius:7px; padding:.4rem .6rem; cursor:pointer;
    font-size:.8rem; font-weight:600; color:white;
    white-space:nowrap; overflow:hidden; text-overflow:ellipsis; text-align:left;
}
.conv-btn {
    flex:1; background:white; border:1px solid #93c5fd;
    border-radius:7px; padding:.4rem .6rem; cursor:pointer;
    font-size:.8rem; color:#1557b0;
    white-space:nowrap; overflow:hidden; text-overflow:ellipsis; text-align:left;
    transition:all .15s;
}
.conv-btn:hover { background:#1557b0; color:white; border-color:#1557b0; }
.conv-time { font-size:.68rem; color:#7ba7d4; padding:0 .3rem .2rem; }

/* Chat area — nền xanh rất nhạt */
.chat-area {
    flex:1; display:flex; flex-direction:column;
    border:1px solid #93c5fd; border-radius:12px;
    overflow:hidden; background:#f4f8ff;
}
.chat-header {
    display:flex; align-items:center; justify-content:space-between;
    padding:.75rem 1rem; border-bottom:1px solid #dbeafe;
    background:#eef3fd; flex-shrink:0;
}
.chat-header-title {
    font-weight:700; font-size:.95rem; color:#0d47a1;
    white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:300px;
}
.chat-header-meta { font-size:.7rem; color:#1557b0; margin-top:1px; }

/* Messages */
.chat-messages {
    flex:1; overflow-y:auto; padding:1rem;
    display:flex; flex-direction:column; gap:.4rem;
    background:#f4f8ff;
}
.bubble-wrap-user { display:flex; justify-content:flex-end; }
.bubble-wrap-ai   { display:flex; justify-content:flex-start; align-items:flex-end; gap:.4rem; }

/* Bubble user — xanh đậm */
.bubble-user {
    background: linear-gradient(135deg,#1557b0,#0d47a1);
    color:white; padding:.55rem .9rem;
    border-radius:16px 16px 4px 16px;
    max-width:70%; font-size:.85rem; line-height:1.5;
    word-break:break-word;
    box-shadow:0 3px 12px rgba(13,71,161,.35);
}
.bubble-ai {
    background:#fff; color:#1a1a2e;
    padding:.45rem .8rem;
    border-radius:16px 16px 16px 4px;
    max-width:70%; font-size:.82rem; line-height:1.55;
    word-break:break-word;
    border:1px solid #dbeafe;
    box-shadow:0 1px 4px rgba(13,71,161,.08);
}
.ai-avatar {
    width:26px; height:26px; border-radius:50%;
    background:linear-gradient(135deg,#1557b0,#7c3aed);
    display:flex; align-items:center; justify-content:center;
    font-size:.75rem; flex-shrink:0;
}

/* Quick chips — trắng viền xanh đậm, hover xanh */
.chips-section { padding:.75rem 1rem; border-bottom:1px solid #dbeafe; }
.chips-label {
    font-size:.68rem; font-weight:700; color:#1557b0;
    letter-spacing:.08em; text-transform:uppercase; margin-bottom:.4rem;
}
.chip-grid { display:flex; flex-wrap:wrap; gap:.4rem; }
.chip {
    display:inline-flex; align-items:center; gap:.3rem;
    background:white; border:2px solid #1557b0;
    border-radius:20px; padding:.28rem .7rem;
    font-size:.75rem; color:#1557b0; cursor:pointer;
    font-weight:600; white-space:nowrap; transition:all .15s;
}
.chip:hover {
    background:linear-gradient(135deg,#1557b0,#0d47a1);
    color:white; border-color:#0d47a1;
    box-shadow:0 3px 8px rgba(13,71,161,.25);
}

/* Input area */
.chat-input-area {
    padding:.6rem 1rem; border-top:1px solid #dbeafe;
    background:#eef3fd; flex-shrink:0;
}
.input-hint { font-size:.68rem; color:#1557b0; text-align:right; margin-top:.2rem; }

/* Empty state */
.empty-state { text-align:center; padding:3rem 1rem; color:#1557b0; }
.empty-state .icon { font-size:2.5rem; margin-bottom:.5rem; }
.empty-state p { font-size:.85rem; line-height:1.6; }

/* FAB */
.fab-new-conv {
    position:fixed; bottom:2rem; right:2rem; z-index:9999;
    background:linear-gradient(135deg,#1557b0,#0d47a1);
    color:white; border:none; border-radius:50px;
    padding:.65rem 1.2rem; font-size:.85rem; font-weight:700;
    cursor:pointer; box-shadow:0 4px 16px rgba(13,71,161,.4);
    display:inline-flex; align-items:center; gap:.4rem;
    white-space:nowrap; transition:transform .15s,box-shadow .15s;
}
.fab-new-conv:hover { transform:translateY(-2px); box-shadow:0 6px 20px rgba(13,71,161,.5); }

/* Nav row */
.nav-row {
    display:flex; gap:.5rem; padding:.5rem 1rem;
    border-top:1px solid #dbeafe; background:#eef3fd; flex-shrink:0;
}

/* st.button gợi ý — trắng viền xanh, hover xanh */
div[data-testid="stButton"] > button[kind="secondary"] {
    background:white !important;
    border:2px solid #1557b0 !important;
    color:#1557b0 !important;
    font-weight:600 !important;
    transition:all .2s !important;
}
div[data-testid="stButton"] > button[kind="secondary"]:hover {
    background:linear-gradient(135deg,#1557b0,#0d47a1) !important;
    border-color:#0d47a1 !important;
    color:white !important;
    box-shadow:0 4px 12px rgba(13,71,161,.3) !important;
    transform:translateY(-1px) !important;
}
</style>
"""


# ── Helpers ───────────────────────────────────────────────
def _init_state():
    if "conversations" not in st.session_state:
        st.session_state["conversations"] = []
    if "current_conv_id" not in st.session_state:
        st.session_state["current_conv_id"] = None


def _new_conversation() -> str:
    conv_id = f"conv_{int(time.time()*1000)}"
    st.session_state["conversations"].append({
        "id":         conv_id,
        "title":      "Cuộc trò chuyện mới",
        "messages":   [],
        "created_at": time.strftime("%H:%M · %d/%m"),
    })
    st.session_state["current_conv_id"] = conv_id
    return conv_id


def _get_current_conv() -> dict | None:
    cid = st.session_state.get("current_conv_id")
    for c in st.session_state.get("conversations", []):
        if c["id"] == cid:
            return c
    return None


def _update_title(conv: dict, first_msg: str):
    title = first_msg.strip()[:38]
    if len(first_msg.strip()) > 38:
        title += "…"
    conv["title"] = title


def _delete_conversation(conv_id: str):
    convs = st.session_state.get("conversations", [])
    st.session_state["conversations"] = [c for c in convs if c["id"] != conv_id]
    if st.session_state.get("current_conv_id") == conv_id:
        remaining = st.session_state["conversations"]
        st.session_state["current_conv_id"] = remaining[0]["id"] if remaining else None


# ── Groq ─────────────────────────────────────────────────
def _call_groq(messages: list) -> str:
    context = ""
    if st.session_state.get("questions") and st.session_state.get("page") == "exam":
        qs = st.session_state.questions
        context = "\n\n[Học sinh đang làm bài thi]\n"
        for i, q in enumerate(qs[:3]):
            context += f"Câu {i+1}: {q['question']}\n"

    payload = {
        "model":       GROQ_MODEL,
        "messages":    [{"role": "system", "content": _SYSTEM_PROMPT + context}]
                       + messages[-10:],
        "max_tokens":  1000,
        "temperature": 0.7,
    }
    try:
        resp = requests.post(GROQ_API_URL, headers=get_groq_headers(),
                             json=payload, timeout=30)
        if resp.status_code == 429:
            return "⏳ Groq đang bận, vui lòng thử lại sau vài giây!"
        if resp.status_code != 200:
            return f"❌ Lỗi kết nối: HTTP {resp.status_code}"
        return resp.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ Lỗi: {e}"


def _send_message(conv: dict, text: str):
    text = text.strip()
    if not text:
        return
    if not conv["messages"]:
        _update_title(conv, text)
    conv["messages"].append({"role": "user", "content": text})
    with st.spinner("🤖 Đang trả lời…"):
        reply = _call_groq(conv["messages"])
    conv["messages"].append({"role": "assistant", "content": reply})


# ── Auto scroll ───────────────────────────────────────────
def _auto_scroll():
    st.markdown("""
    <script>
        (function() {
            const els = window.parent.document.querySelectorAll('.chat-messages');
            els.forEach(el => { el.scrollTop = el.scrollHeight; });
            const stContainers = window.parent.document.querySelectorAll('[data-testid="stVerticalBlockBorderWrapper"]');
            if (stContainers.length) {
                const last = stContainers[stContainers.length - 1];
                last.scrollTop = last.scrollHeight;
            }
        })();
    </script>
    """, unsafe_allow_html=True)


# ── Render messages ───────────────────────────────────────
def _render_messages(messages: list):
    if not messages:
        st.markdown("""
        <div class="empty-state">
            <div class="icon">💬</div>
            <p style="color:#1557b0">Xin chào! Tôi có thể giúp gì cho bạn?<br>
            <span style="font-size:.78rem;color:#1557b0">Chọn gợi ý hoặc gõ câu hỏi bên dưới.</span></p>
        </div>""", unsafe_allow_html=True)
        return

    html = ""
    for msg in messages:
        if msg["role"] == "user":
            html += (f'<div class="bubble-wrap-user">'
                     f'<div class="bubble-user">{msg["content"]}</div>'
                     f'</div>')
        else:
            content = msg["content"].replace("\n", "<br>")
            html += (f'<div class="bubble-wrap-ai">'
                     f'<div class="ai-avatar">🤖</div>'
                     f'<div class="bubble-ai">{content}</div>'
                     f'</div>')
    st.markdown(html, unsafe_allow_html=True)


# ── Entry point ───────────────────────────────────────────
def show_chatbox():
    st.markdown(_CHAT_CSS, unsafe_allow_html=True)
    _init_state()

    if not st.session_state["conversations"]:
        _new_conversation()
    if st.session_state["current_conv_id"] is None and st.session_state["conversations"]:
        st.session_state["current_conv_id"] = st.session_state["conversations"][0]["id"]

    conv  = _get_current_conv()
    convs = st.session_state.get("conversations", [])

    with st.sidebar:
        st.markdown("---")
        if st.button("✏️ Hội thoại mới", use_container_width=True,
                     type="primary", key="btn_new_sidebar"):
            _new_conversation(); st.rerun()
        st.caption(f"{len(convs)} hội thoại")

    col_side, col_chat = st.columns([1, 3], gap="small")

    with col_side:
        st.markdown('<div class="conv-sidebar-label" style="font-size:.78rem;color:#1557b0;font-weight:700;">💬 Hội thoại</div>',
                    unsafe_allow_html=True)
        if not convs:
            st.caption("Chưa có hội thoại nào.")
        else:
            for c in reversed(convs):
                is_active = c["id"] == st.session_state["current_conv_id"]
                c_col, d_col = st.columns([5, 1])
                with c_col:
                    label = f"{'▸ ' if is_active else ''}{c['title']}"
                    if st.button(label, key=f"sel_{c['id']}",
                                 use_container_width=True,
                                 type="primary" if is_active else "secondary"):
                        st.session_state["current_conv_id"] = c["id"]
                        st.rerun()
                with d_col:
                    if st.button("✕", key=f"del_{c['id']}", help="Xóa"):
                        _delete_conversation(c["id"]); st.rerun()
                st.caption(c["created_at"])

    with col_chat:
        if conv is None:
            st.info("Nhấn **✏️ Hội thoại mới** để bắt đầu.")
            return

        turns = len(conv["messages"]) // 2
        h_left, h_right = st.columns([3, 1])
        with h_left:
            st.markdown(
                f'<div style="padding:.25rem 0">'
                f'<div style="font-weight:700;font-size:.95rem;color:#0d47a1;'
                f'white-space:nowrap;overflow:hidden;text-overflow:ellipsis">'
                f'{conv["title"]}</div>'
                f'<div style="font-size:.7rem;color:#1557b0">🤖 {GROQ_MODEL}'
                f'{"  · " + str(turns) + " lượt" if turns else ""}</div>'
                f'</div>', unsafe_allow_html=True)
        with h_right:
            st.caption("✏️ Tạo mới\nở sidebar →")

        st.markdown('<hr style="border:none;border-top:1px solid #dbeafe;margin:.4rem 0">',
                    unsafe_allow_html=True)

        if not conv["messages"]:
            st.markdown('<div style="font-size:.68rem;font-weight:700;color:#1557b0;'
                        'letter-spacing:.08em;text-transform:uppercase;margin-bottom:.4rem">'
                        '💡 Gợi ý</div>', unsafe_allow_html=True)
            q_cols = st.columns(3)
            for i, (icon, q) in enumerate(_QUICK_QUESTIONS):
                with q_cols[i % 3]:
                    if st.button(f"{icon} {q}", key=f"quick_{i}_{conv['id']}",
                                 use_container_width=True):
                        _send_message(conv, q); st.rerun()
            st.markdown('<hr style="border:none;border-top:1px solid #dbeafe;margin:.5rem 0">',
                        unsafe_allow_html=True)

        _render_messages(conv["messages"])
        if conv["messages"]:
            _auto_scroll()

        st.markdown('<hr style="border:none;border-top:1px solid #dbeafe;margin:.4rem 0">',
                    unsafe_allow_html=True)
        with st.form(key=f"chat_form_{conv['id']}", clear_on_submit=True):
            f1, f2 = st.columns([6, 1])
            with f1:
                user_input = st.text_input(
                    "", placeholder="Nhập câu hỏi của bạn…",
                    label_visibility="collapsed",
                    key=f"inp_{conv['id']}")
            with f2:
                submitted = st.form_submit_button("Gửi ➤", use_container_width=True,
                                                  type="primary")
            if submitted and user_input.strip():
                _send_message(conv, user_input); st.rerun()

        st.markdown('<div style="font-size:.68rem;color:#1557b0;text-align:right">Nhấn Enter hoặc Gửi ➤</div>',
                    unsafe_allow_html=True)

        st.markdown('<hr style="border:none;border-top:1px solid #dbeafe;margin:.5rem 0">',
                    unsafe_allow_html=True)
        n1, n2 = st.columns(2)
        with n1:
            if st.button("← Trang chủ", use_container_width=True, key="chat_home"):
                st.session_state.page = "home"; st.rerun()
        with n2:
            if st.button("🚀 Làm bài ngay", use_container_width=True,
                         type="primary", key="chat_exam"):
                st.session_state.page = "select"; st.rerun()

