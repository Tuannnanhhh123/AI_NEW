# ============================================================
# ui_helpers.py — Logout logic & shared helpers
# KHÔNG import từ app.py hoặc ui.py để tránh circular import
# ============================================================
import streamlit as st


# ── Defaults dùng khi logout (mirror của _DEFAULTS trong app.py) ──
_SESSION_DEFAULTS = {
    "page":               "login",
    "username":           None,
    "uid":                None,
    "email":              None,
    "role":               None,
    "grade":              None,
    "favorite_subjects":  [],
    "subject":            None,
    "questions":          [],
    "answers":            {},
    "submitted":          False,
    "score":              0,
    "start_time":         None,
    "exam_source":        None,
    "ai_error":           None,
    "verify_summary":     None,
    "dup_filtered":       0,
    "exam_start_ts":      None,
    "current_assignment": None,
    "remind_assignments": [],
    "teacher_tab":        "dashboard",
    "_is_mobile":         False,
    "_sb_render_count":   0,
}


def do_logout():
    """Xóa session và quay về login. Không import app.py."""
    st.query_params.clear()
    for k, v in _SESSION_DEFAULTS.items():
        st.session_state[k] = v
    st.rerun()


def detect_mobile() -> bool:
    """Đọc query param _mobile để xác định thiết bị."""
    val = st.query_params.get("_mobile", "0")
    mobile = str(val) == "1"
    st.session_state["_is_mobile"] = mobile
    return mobile


def is_mobile() -> bool:
    return st.session_state.get("_is_mobile", False)