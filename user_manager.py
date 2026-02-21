# ============================================================
# user_manager.py — Quản lý người dùng & lưu bài làm
# Lưu lên Firestore REST API (không cần Admin SDK)
# Collection: exam_results/{uid}/exams/{exam_id}
# Collection: users/{uid}  (danh sách username)
# ============================================================
import json, requests
from datetime import datetime
import streamlit as st

from config import FIREBASE_CONFIG

_API_KEY    = FIREBASE_CONFIG["apiKey"]
_PROJECT_ID = FIREBASE_CONFIG["projectId"]
_FS_BASE    = (
    f"https://firestore.googleapis.com/v1/"
    f"projects/{_PROJECT_ID}/databases/(default)/documents"
)


# ══════════════════════════════════════════════════════════
# Firestore REST helpers (copy từ firebase_manager)
# ══════════════════════════════════════════════════════════

def _get_token() -> str:
    """Lấy idToken từ session_state."""
    return st.session_state.get("_id_token", "")


def _headers() -> dict:
    return {
        "Authorization": f"Bearer {_get_token()}",
        "Content-Type":  "application/json",
    }


def _fs_encode(data: dict) -> dict:
    """dict Python → Firestore field format."""
    fields = {}
    for k, v in data.items():
        if isinstance(v, str):
            fields[k] = {"stringValue": v}
        elif isinstance(v, bool):
            fields[k] = {"booleanValue": v}
        elif isinstance(v, int):
            fields[k] = {"integerValue": str(v)}
        elif isinstance(v, float):
            fields[k] = {"doubleValue": v}
        elif v is None:
            fields[k] = {"nullValue": None}
        elif isinstance(v, list):
            fields[k] = {"arrayValue": {"values": [
                _fs_encode_value(i) for i in v
            ]}}
        elif isinstance(v, dict):
            fields[k] = {"mapValue": {"fields": _fs_encode(v)}}
        else:
            fields[k] = {"stringValue": str(v)}
    return fields


def _fs_encode_value(v) -> dict:
    if isinstance(v, str):   return {"stringValue": v}
    if isinstance(v, bool):  return {"booleanValue": v}
    if isinstance(v, int):   return {"integerValue": str(v)}
    if isinstance(v, float): return {"doubleValue": v}
    if isinstance(v, dict):  return {"mapValue": {"fields": _fs_encode(v)}}
    if isinstance(v, list):  return {"arrayValue": {"values": [_fs_encode_value(i) for i in v]}}
    return {"stringValue": str(v)}


def _fs_parse_value(v: dict):
    if "stringValue"  in v: return v["stringValue"]
    if "booleanValue" in v: return v["booleanValue"]
    if "integerValue" in v: return int(v["integerValue"])
    if "doubleValue"  in v: return v["doubleValue"]
    if "nullValue"    in v: return None
    if "arrayValue"   in v:
        return [_fs_parse_value(i) for i in v["arrayValue"].get("values", [])]
    if "mapValue"     in v:
        return {k: _fs_parse_value(val)
                for k, val in v["mapValue"].get("fields", {}).items()}
    return None


def _fs_parse(doc: dict) -> dict:
    return {k: _fs_parse_value(v) for k, v in doc.get("fields", {}).items()}


def _fs_set(path: str, data: dict) -> bool:
    """PATCH (upsert) một document. path = 'collection/doc_id'."""
    url = f"{_FS_BASE}/{path}"
    try:
        r = requests.patch(
            url, headers=_headers(),
            json={"fields": _fs_encode(data)},
            timeout=10
        )
        return r.status_code in (200, 201)
    except Exception as e:
        print(f"[Firestore SET] {path}: {e}")
        return False


def _fs_get(path: str) -> dict | None:
    """GET một document. path = 'collection/doc_id'."""
    url = f"{_FS_BASE}/{path}"
    try:
        r = requests.get(url, headers=_headers(), timeout=10)
        if r.status_code == 200:
            return _fs_parse(r.json())
        if r.status_code == 404:
            return None
    except Exception as e:
        print(f"[Firestore GET] {path}: {e}")
    return None


def _fs_list(path: str) -> list[dict]:
    """
    LIST sub-collection documents.
    path = 'collection/doc_id/sub_collection'
    """
    url = f"{_FS_BASE}/{path}"
    try:
        r = requests.get(url, headers=_headers(), timeout=10)
        if r.status_code == 200:
            docs = r.json().get("documents", [])
            return [_fs_parse(d) for d in docs]
    except Exception as e:
        print(f"[Firestore LIST] {path}: {e}")
    return []


def _fs_query(collection: str, field: str, value: str) -> list[dict]:
    """
    Firestore structuredQuery — lọc theo 1 field bằng =.
    Dùng để list tất cả exam của 1 username (teacher view).
    """
    url = f"{_FS_BASE}:runQuery"
    body = {
        "structuredQuery": {
            "from": [{"collectionId": collection, "allDescendants": True}],
            "where": {
                "fieldFilter": {
                    "field":  {"fieldPath": field},
                    "op":     "EQUAL",
                    "value":  {"stringValue": value},
                }
            },
            "orderBy": [{"field": {"fieldPath": "date"}, "direction": "DESCENDING"}],
        }
    }
    try:
        r = requests.post(url, headers=_headers(), json=body, timeout=10)
        if r.status_code == 200:
            results = r.json()
            return [
                _fs_parse(item["document"])
                for item in results
                if "document" in item
            ]
    except Exception as e:
        print(f"[Firestore QUERY] {e}")
    return []


# ══════════════════════════════════════════════════════════
# Người dùng
# ══════════════════════════════════════════════════════════

def get_all_users() -> list[str]:
    """
    Lấy danh sách username từ Firestore.
    Dùng cho teacher stats tab.
    """
    uid = st.session_state.get("uid", "")
    if not uid:
        return []
    # Lấy từ sub-collection usernames (ghi khi tạo user)
    docs = _fs_list(f"user_index/index/names")
    return sorted([d.get("username", "") for d in docs if d.get("username")])


def user_exists(username: str) -> bool:
    doc = _fs_get(f"user_index/index/names/{_safe(username)}")
    return doc is not None


def create_user(username: str):
    """Ghi username vào index để teacher có thể list."""
    username = username.strip()
    if not username:
        return
    uid = st.session_state.get("uid", "")
    _fs_set(f"user_index/index/names/{_safe(username)}", {
        "username": username,
        "uid":      uid,
        "created_at": _now(),
    })


# ══════════════════════════════════════════════════════════
# Lưu bài làm
# ══════════════════════════════════════════════════════════

def save_exam_result(
    username: str, subject: str, grade: str,
    score: int, total: int,
    questions: list, answers: dict,
    elapsed_seconds: int, source: str,
) -> str:
    uid     = st.session_state.get("uid", "")
    exam_id = _make_id(username)

    record = {
        "id":       exam_id,
        "uid":      uid,
        "username": username,
        "date":     _now(),
        "subject":  subject,
        "grade":    grade,
        "score":    score,
        "total":    total,
        "pct":      round(score / total * 100) if total else 0,
        "time_sec": elapsed_seconds,
        "source":   source,
        "detail": [
            {
                "no":       i + 1,
                "question": q["question"],
                "correct":  q["answer"],
                "user_ans": answers.get(i, "—"),
                "is_right": answers.get(i) == q["answer"],
            }
            for i, q in enumerate(questions)
        ],
    }

    # Lưu vào: exam_results/{uid}/exams/{exam_id}
    path = f"exam_results/{uid}/exams/{exam_id}"
    ok   = _fs_set(path, record)
    if not ok:
        print(f"[user_manager] Lưu bài thi thất bại: {path}")

    return exam_id


# ══════════════════════════════════════════════════════════
# Truy vấn lịch sử
# ══════════════════════════════════════════════════════════

def get_user_exams(username: str) -> list:
    """
    Lấy toàn bộ bài thi của user hiện tại (dùng uid từ session).
    Nếu username khác với session (teacher xem HS) → dùng query.
    """
    session_user = st.session_state.get("username", "")
    uid          = st.session_state.get("uid", "")

    if username == session_user and uid:
        # Học sinh xem bài của chính mình
        docs = _fs_list(f"exam_results/{uid}/exams")
    else:
        # Giáo viên xem bài của học sinh khác → query theo username
        docs = _fs_query("exams", "username", username)

    # Sắp xếp theo ngày tăng dần
    docs.sort(key=lambda x: x.get("date", ""))
    return docs


def get_user_stats(username: str) -> dict:
    """Thống kê tổng hợp theo môn."""
    exams = get_user_exams(username)
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


def delete_user(username: str):
    """Xóa index user (không xóa exam_results để giữ lịch sử)."""
    _fs_set(f"user_index/index/names/{_safe(username)}", {"deleted": True})


# ══════════════════════════════════════════════════════════
# Helpers
# ══════════════════════════════════════════════════════════

def _now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def _make_id(username: str) -> str:
    ts = datetime.now().strftime("%Y%m%d%H%M%S%f")[:18]
    return f"{username[:4].upper()}_{ts}"


def _safe(name: str) -> str:
    """Chuyển username thành Firestore-safe document ID."""
    return name.strip().replace(" ", "_").replace("/", "_").replace(".", "_")