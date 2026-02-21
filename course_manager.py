# ============================================================
# course_manager.py — CRUD khóa học + tiến độ học sinh
# ============================================================
import time
import streamlit as st

# ── Firebase helper ───────────────────────────────────────
def _db():
    try:
        from firebase_manager import _db as db, _FIREBASE_OK
        if _FIREBASE_OK and db:
            return db
    except Exception:
        pass
    return None


# ═══════════════════════════════════════════════════════════
# KHÓA HỌC (courses/)
# ═══════════════════════════════════════════════════════════

def get_all_courses() -> list:
    """Lấy tất cả khóa học."""
    db = _db()
    if not db:
        return _mock_courses()
    try:
        docs = db.collection("courses").order_by("created_at", direction="DESCENDING").stream()
        return [{"id": d.id, **d.to_dict()} for d in docs]
    except Exception:
        return _mock_courses()


def get_course(course_id: str) -> dict | None:
    db = _db()
    if not db:
        for c in _mock_courses():
            if c["id"] == course_id:
                return c
        return None
    try:
        doc = db.collection("courses").document(course_id).get()
        return {"id": doc.id, **doc.to_dict()} if doc.exists else None
    except Exception:
        return None


def create_course(data: dict) -> str:
    """Tạo khóa học mới. Trả về ID."""
    db = _db()
    data["created_at"] = time.time()
    data["chapters"]   = data.get("chapters", [])
    if not db:
        return "mock_id"
    try:
        ref = db.collection("courses").add(data)
        return ref[1].id
    except Exception as e:
        st.error(f"Lỗi tạo khóa học: {e}")
        return ""


def update_course(course_id: str, data: dict):
    db = _db()
    if not db:
        return
    try:
        db.collection("courses").document(course_id).update(data)
    except Exception as e:
        st.error(f"Lỗi cập nhật: {e}")


def delete_course(course_id: str):
    db = _db()
    if not db:
        return
    try:
        db.collection("courses").document(course_id).delete()
        # Xóa luôn toàn bộ tiến độ liên quan
        prog_docs = db.collection("course_progress") \
                      .where("course_id", "==", course_id).stream()
        for d in prog_docs:
            d.reference.delete()
    except Exception as e:
        st.error(f"Lỗi xóa: {e}")


# ═══════════════════════════════════════════════════════════
# CHƯƠNG & BÀI HỌC (lưu trong courses/{id}.chapters[])
# ═══════════════════════════════════════════════════════════

def add_chapter(course_id: str, title: str) -> list:
    """Thêm chương mới, trả về danh sách chapters mới."""
    course = get_course(course_id)
    if not course:
        return []
    chapters = course.get("chapters", [])
    chapters.append({
        "id":      f"ch_{int(time.time()*1000)}",
        "title":   title,
        "lessons": [],
    })
    update_course(course_id, {"chapters": chapters})
    return chapters


def update_chapter(course_id: str, ch_id: str, title: str):
    course = get_course(course_id)
    if not course:
        return
    chapters = course.get("chapters", [])
    for ch in chapters:
        if ch["id"] == ch_id:
            ch["title"] = title
            break
    update_course(course_id, {"chapters": chapters})


def delete_chapter(course_id: str, ch_id: str):
    course = get_course(course_id)
    if not course:
        return
    chapters = [c for c in course.get("chapters", []) if c["id"] != ch_id]
    update_course(course_id, {"chapters": chapters})


def add_lesson(course_id: str, ch_id: str, lesson: dict) -> bool:
    """
    lesson = {
        title, content, video_url, video_type (youtube|upload),
        duration_min, quiz: [{question, options, answer}]
    }
    """
    course = get_course(course_id)
    if not course:
        return False
    chapters = course.get("chapters", [])
    for ch in chapters:
        if ch["id"] == ch_id:
            lesson["id"]         = f"ls_{int(time.time()*1000)}"
            lesson["created_at"] = time.time()
            ch.setdefault("lessons", []).append(lesson)
            break
    update_course(course_id, {"chapters": chapters})
    return True


def update_lesson(course_id: str, ch_id: str, lesson_id: str, data: dict):
    course = get_course(course_id)
    if not course:
        return
    chapters = course.get("chapters", [])
    for ch in chapters:
        if ch["id"] == ch_id:
            for i, ls in enumerate(ch.get("lessons", [])):
                if ls["id"] == lesson_id:
                    ch["lessons"][i] = {**ls, **data}
                    break
    update_course(course_id, {"chapters": chapters})


def delete_lesson(course_id: str, ch_id: str, lesson_id: str):
    course = get_course(course_id)
    if not course:
        return
    chapters = course.get("chapters", [])
    for ch in chapters:
        if ch["id"] == ch_id:
            ch["lessons"] = [l for l in ch.get("lessons", [])
                             if l["id"] != lesson_id]
    update_course(course_id, {"chapters": chapters})


# ═══════════════════════════════════════════════════════════
# TIẾN ĐỘ HỌC SINH (course_progress/{uid}_{course_id})
# ═══════════════════════════════════════════════════════════

def _prog_id(uid: str, course_id: str) -> str:
    return f"{uid}_{course_id}"


def get_progress(uid: str, course_id: str) -> dict:
    """
    Trả về:
    {
        completed_lessons: [lesson_id, ...],
        quiz_scores: {lesson_id: score},
        started_at: float,
        completed_at: float | None,
        certificate_issued: bool,
    }
    """
    db = _db()
    default = {
        "completed_lessons": [],
        "quiz_scores":       {},
        "started_at":        None,
        "completed_at":      None,
        "certificate_issued": False,
    }
    if not db:
        return default
    try:
        doc = db.collection("course_progress").document(_prog_id(uid, course_id)).get()
        return {**default, **doc.to_dict()} if doc.exists else default
    except Exception:
        return default


def mark_lesson_done(uid: str, course_id: str, lesson_id: str,
                     quiz_score: int | None = None):
    """Đánh dấu bài học đã hoàn thành + lưu điểm quiz nếu có."""
    db = _db()
    if not db:
        return
    prog = get_progress(uid, course_id)
    if lesson_id not in prog["completed_lessons"]:
        prog["completed_lessons"].append(lesson_id)
    if prog["started_at"] is None:
        prog["started_at"] = time.time()
    if quiz_score is not None:
        prog["quiz_scores"][lesson_id] = quiz_score

    # Kiểm tra hoàn thành toàn bộ khóa
    course       = get_course(course_id)
    total_lessons = sum(len(ch.get("lessons", []))
                        for ch in course.get("chapters", [])) if course else 0
    if total_lessons > 0 and len(prog["completed_lessons"]) >= total_lessons:
        if not prog["completed_at"]:
            prog["completed_at"] = time.time()

    try:
        db.collection("course_progress").document(
            _prog_id(uid, course_id)
        ).set(prog, merge=True)
    except Exception as e:
        st.error(f"Lỗi lưu tiến độ: {e}")


def issue_certificate(uid: str, course_id: str):
    db = _db()
    if not db:
        return
    try:
        db.collection("course_progress").document(
            _prog_id(uid, course_id)
        ).update({"certificate_issued": True})
    except Exception:
        pass


def get_all_progress(uid: str) -> list:
    """Lấy tiến độ tất cả khóa học của 1 học sinh."""
    db = _db()
    if not db:
        return []
    try:
        docs = db.collection("course_progress") \
                 .where("uid", "==", uid).stream()
        return [d.to_dict() for d in docs]
    except Exception:
        return []


# ═══════════════════════════════════════════════════════════
# YOUTUBE SEARCH (dùng YouTube Data API v3)
# ═══════════════════════════════════════════════════════════

def search_youtube(query: str, max_results: int = 6) -> list:
    """
    Tìm video YouTube theo từ khóa.
    Trả về list: [{title, video_id, thumbnail, channel, duration}]
    Cần YOUTUBE_API_KEY trong st.secrets hoặc config.
    """
    try:
        api_key = st.secrets.get("YOUTUBE_API_KEY", "AIzaSyC_FN2bk2b4atsf-03xVANBOuTyQR9Tv9w")
        if not api_key:
            # Fallback: trả về kết quả search URL (không cần API key)
            return _youtube_fallback(query, max_results)

        import requests
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part":       "snippet",
            "q":          query + " bài giảng học sinh",
            "type":       "video",
            "maxResults": max_results,
            "key":        api_key,
            "relevanceLanguage": "vi",
        }
        r = requests.get(url, params=params, timeout=10)
        if r.status_code != 200:
            return _youtube_fallback(query, max_results)

        items = r.json().get("items", [])
        return [{
            "title":     i["snippet"]["title"],
            "video_id":  i["id"]["videoId"],
            "thumbnail": i["snippet"]["thumbnails"]["medium"]["url"],
            "channel":   i["snippet"]["channelTitle"],
        } for i in items]
    except Exception:
        return _youtube_fallback(query, max_results)


def _youtube_fallback(query: str, n: int) -> list:
    """Fallback khi không có API key — trả về link search."""
    import urllib.parse
    q = urllib.parse.quote(query + " bài giảng")
    return [{
        "title":     f"🔍 Tìm '{query}' trên YouTube",
        "video_id":  None,
        "search_url": f"https://www.youtube.com/results?search_query={q}",
        "thumbnail": "",
        "channel":   "YouTube Search",
    }]


def get_youtube_embed(video_id: str) -> str:
    """Trả về HTML embed YouTube."""
    return (
        f'<iframe width="100%" height="360" '
        f'src="https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1" '
        f'frameborder="0" allowfullscreen '
        f'style="border-radius:12px;display:block"></iframe>'
    )


# ═══════════════════════════════════════════════════════════
# HELPER: tính % tiến độ
# ═══════════════════════════════════════════════════════════

def calc_progress_pct(course: dict, progress: dict) -> int:
    total = sum(len(ch.get("lessons", [])) for ch in course.get("chapters", []))
    done  = len(progress.get("completed_lessons", []))
    return int(done / total * 100) if total else 0


def count_total_lessons(course: dict) -> int:
    return sum(len(ch.get("lessons", [])) for ch in course.get("chapters", []))


# ═══════════════════════════════════════════════════════════
# MOCK DATA (dùng khi Firebase chưa kết nối)
# ═══════════════════════════════════════════════════════════

def _mock_courses() -> list:
    return [
        {
            "id":          "mock_toan_10",
            "title":       "Toán lớp 10 — Đại số cơ bản",
            "subject":     "Toán",
            "grade":       "Lớp 10 (THPT)",
            "description": "Ôn tập toàn bộ đại số lớp 10: hàm số, phương trình, bất phương trình.",
            "teacher":     "Nguyễn Thị B",
            "thumbnail":   "🔢",
            "level":       "Cơ bản",
            "created_at":  time.time(),
            "chapters": [
                {
                    "id":    "ch_1",
                    "title": "Chương 1: Hàm số và đồ thị",
                    "lessons": [
                        {
                            "id":          "ls_1",
                            "title":       "Bài 1: Khái niệm hàm số",
                            "content":     "Hàm số là quy tắc tương ứng mỗi x thuộc tập D với đúng một y thuộc tập R.",
                            "video_url":   "dQw4w9WgXcQ",
                            "video_type":  "youtube",
                            "duration_min": 15,
                            "quiz": [
                                {"question": "Hàm số y = f(x) có bao nhiêu giá trị y ứng với mỗi x?",
                                 "options": ["Đúng một","Hai","Ba","Không xác định"],
                                 "answer":  "Đúng một"},
                            ]
                        },
                        {
                            "id":          "ls_2",
                            "title":       "Bài 2: Đồ thị hàm số bậc nhất",
                            "content":     "Hàm số bậc nhất y = ax + b có đồ thị là đường thẳng.",
                            "video_url":   "dQw4w9WgXcQ",
                            "video_type":  "youtube",
                            "duration_min": 20,
                            "quiz": []
                        },
                    ]
                },
                {
                    "id":    "ch_2",
                    "title": "Chương 2: Phương trình bậc hai",
                    "lessons": [
                        {
                            "id":          "ls_3",
                            "title":       "Bài 1: Giải phương trình bậc hai",
                            "content":     "ax² + bx + c = 0, a≠0. Dùng công thức nghiệm hoặc phân tích nhân tử.",
                            "video_url":   "dQw4w9WgXcQ",
                            "video_type":  "youtube",
                            "duration_min": 25,
                            "quiz": []
                        },
                    ]
                },
            ]
        },
        {
            "id":          "mock_van_10",
            "title":       "Ngữ Văn 10 — Văn học dân gian",
            "subject":     "Ngữ Văn",
            "grade":       "Lớp 10 (THPT)",
            "description": "Tìm hiểu các thể loại văn học dân gian Việt Nam.",
            "teacher":     "Trần Văn C",
            "thumbnail":   "📖",
            "level":       "Cơ bản",
            "created_at":  time.time(),
            "chapters": [
                {
                    "id":    "ch_1",
                    "title": "Chương 1: Truyện cổ tích",
                    "lessons": [
                        {
                            "id":          "ls_1",
                            "title":       "Bài 1: Đặc điểm truyện cổ tích",
                            "content":     "Truyện cổ tích là thể loại tự sự dân gian, kể về số phận con người.",
                            "video_url":   "dQw4w9WgXcQ",
                            "video_type":  "youtube",
                            "duration_min": 18,
                            "quiz": []
                        },
                    ]
                },
            ]
        },
    ]