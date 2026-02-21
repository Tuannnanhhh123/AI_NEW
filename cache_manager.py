# ============================================================
# cache_manager.py — Cache toàn cục dùng st.cache_data
# Giảm tải Groq API + Firestore khi nhiều người dùng cùng lúc
# ============================================================
import time
import hashlib
import streamlit as st


# ══════════════════════════════════════════════════════════
# 1. CACHE NGÂN HÀNG CÂU HỎI
# Cache pool câu hỏi 1 giờ — toàn bộ user dùng chung
# Không cần đọc file bank mỗi lần tạo đề
# ══════════════════════════════════════════════════════════
@st.cache_data(ttl=3600, show_spinner=False)
def get_question_pool(subject: str, grade: str) -> list:
    """
    Cache pool câu hỏi theo môn+lớp trong 1 giờ.
    Tất cả user cùng dùng chung cache này.
    """
    from question_bank   import QUESTION_BANK
    from teacher_manager import get_approved_for_exam

    local = QUESTION_BANK.get(subject, {}).get(grade, [])
    if not local:
        from config import DIFFICULTY_MAP
        diff = DIFFICULTY_MAP.get(grade, "Khó")
        for g, d in DIFFICULTY_MAP.items():
            if d == diff and g in QUESTION_BANK.get(subject, {}):
                local = QUESTION_BANK[subject][g]
                break

    db_qs       = get_approved_for_exam(subject, grade)
    local_texts = {q["question"] for q in local}
    extra       = [q for q in db_qs if q["question"] not in local_texts]
    return local + extra


# ══════════════════════════════════════════════════════════
# 2. CACHE PROFILE FIREBASE
# Tránh gọi Firestore mỗi lần rerun
# ══════════════════════════════════════════════════════════
@st.cache_data(ttl=1800, show_spinner=False)
def get_user_profile_cached(uid: str, token: str) -> dict | None:
    """
    Cache profile user 30 phút.
    Key = uid (token chỉ dùng để xác thực lần đầu).
    """
    try:
        from firebase_manager import _fs_get
        return _fs_get(f"users/{uid}", token)
    except Exception:
        return None


# ══════════════════════════════════════════════════════════
# 3. RATE LIMITER — chống spam tạo đề
# Mỗi user chỉ được tạo đề 1 lần mỗi 30 giây
# ══════════════════════════════════════════════════════════
# Dùng st.session_state (per user) thay vì global dict
def check_rate_limit(action: str, limit_seconds: int = 30) -> tuple[bool, int]:
    """
    Kiểm tra rate limit cho 1 action.
    Trả về (allowed, seconds_remaining).
    """
    key      = f"_rl_{action}"
    now      = time.time()
    last     = st.session_state.get(key, 0)
    elapsed  = now - last
    remaining = max(0, int(limit_seconds - elapsed))

    if elapsed < limit_seconds:
        return False, remaining

    st.session_state[key] = now
    return True, 0


# ══════════════════════════════════════════════════════════
# 4. CACHE LỊCH SỬ BÀI THI
# Tránh gọi Firestore mỗi lần vào trang history
# ══════════════════════════════════════════════════════════
@st.cache_data(ttl=300, show_spinner=False)   # cache 5 phút
def get_exams_cached(uid: str, token: str) -> list:
    """Cache lịch sử bài thi 5 phút theo uid."""
    try:
        from firebase_manager import _fs_list
        docs = _fs_list(f"exam_results/{uid}/exams", token)
        docs.sort(key=lambda x: x.get("date", ""))
        return docs
    except Exception:
        return []


def invalidate_exam_cache(uid: str, token: str):
    """Xóa cache lịch sử sau khi nộp bài mới."""
    get_exams_cached.clear()


# ══════════════════════════════════════════════════════════
# 5. LAZY LOADING — chỉ load khi cần
# ══════════════════════════════════════════════════════════
def get_stats_cached(uid: str, token: str) -> dict:
    """Tính stats từ cache exams — không gọi thêm Firestore."""
    exams = get_exams_cached(uid, token)
    if not exams:
        return {}

    stats: dict = {}
    for e in exams:
        key = e.get("subject", "")
        if not key:
            continue
        if key not in stats:
            stats[key] = {"count": 0, "total_pct": 0, "best": 0}
        stats[key]["count"]     += 1
        stats[key]["total_pct"] += e.get("pct", 0)
        stats[key]["best"]       = max(stats[key]["best"], e.get("pct", 0))

    for k in stats:
        stats[k]["avg"] = round(stats[k]["total_pct"] / stats[k]["count"])
    return stats