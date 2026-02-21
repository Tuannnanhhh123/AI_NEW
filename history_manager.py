# ============================================================
# history_manager.py — Chống trùng câu hỏi toàn diện
# Lưu vào Firestore (persist qua reload) + fallback JSON local
# Hash câu GỐC từ bank trước khi Groq paraphrase
# ============================================================
import json, os, hashlib, threading
from datetime import datetime

HISTORY_FILE = "exam_history.json"
MAX_HISTORY  = 500

_file_lock = threading.Lock()   # chống race condition khi ghi file JSON


# ── Hash câu hỏi gốc ─────────────────────────────────────
def _hash_question(question_text: str) -> str:
    text = question_text.strip().lower().rstrip(".?!")
    text = " ".join(text.split())
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:16]


# ── Firestore backend ─────────────────────────────────────
def _firestore_get(subject: str, grade: str) -> set:
    try:
        from firebase_manager import _db, _FIREBASE_OK
        if not _FIREBASE_OK or not _db:
            return set()
        key = f"{subject}|{grade}"
        doc = _db.collection("exam_history").document(
            key.replace("/", "_").replace(" ", "_")
        ).get()
        if doc.exists:
            return set(doc.to_dict().get("hashes", []))
    except Exception:
        pass
    return set()


def _firestore_save(subject: str, grade: str, hashes: list):
    try:
        from firebase_manager import _db, _FIREBASE_OK
        if not _FIREBASE_OK or not _db:
            return
        key = f"{subject}|{grade}"
        _db.collection("exam_history").document(
            key.replace("/", "_").replace(" ", "_")
        ).set({
            "hashes":       hashes,
            "last_updated": datetime.now().isoformat(),
        })
    except Exception:
        pass


# ── Local JSON fallback (thread-safe) ────────────────────
def _local_load() -> dict:
    with _file_lock:
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
    return {}


def _local_save(data: dict):
    with _file_lock:
        try:
            with open(HISTORY_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[history_manager] Lỗi ghi file: {e}")


# ── API công khai ─────────────────────────────────────────
def get_used_hashes(subject: str, grade: str) -> set:
    fs_hashes = _firestore_get(subject, grade)
    if fs_hashes:
        return fs_hashes
    data = _local_load()
    key  = f"{subject}|{grade}"
    return set(data.get(key, {}).get("hashes", []))


def save_exam(subject: str, grade: str, questions: list):
    key        = f"{subject}|{grade}"
    new_hashes = [_hash_question(q["question"]) for q in questions]

    # Cập nhật Firestore
    existing_fs = list(_firestore_get(subject, grade))
    combined    = list(dict.fromkeys(existing_fs + new_hashes))
    combined    = combined[-MAX_HISTORY:]
    _firestore_save(subject, grade, combined)

    # Cập nhật local (backup) — thread-safe qua _local_save
    data = _local_load()
    if key not in data:
        data[key] = {"hashes": [], "last_updated": ""}
    existing_local = data[key]["hashes"]
    combined_local = list(dict.fromkeys(existing_local + new_hashes))
    data[key]["hashes"]       = combined_local[-MAX_HISTORY:]
    data[key]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    _local_save(data)


def filter_new_questions(questions: list, used_hashes: set) -> list:
    return [
        q for q in questions
        if _hash_question(q["question"]) not in used_hashes
    ]


def clear_history(subject: str = None, grade: str = None):
    try:
        from firebase_manager import _db, _FIREBASE_OK
        if _FIREBASE_OK and _db:
            if subject and grade:
                key = f"{subject}|{grade}".replace("/","_").replace(" ","_")
                _db.collection("exam_history").document(key).delete()
            else:
                docs = _db.collection("exam_history").stream()
                for doc in docs:
                    doc.reference.delete()
    except Exception:
        pass

    data = _local_load()
    if subject and grade:
        data.pop(f"{subject}|{grade}", None)
    else:
        data = {}
    _local_save(data)


def get_history_stats() -> dict:
    stats = {}
    try:
        from firebase_manager import _db, _FIREBASE_OK
        if _FIREBASE_OK and _db:
            docs = _db.collection("exam_history").stream()
            for doc in docs:
                d = doc.to_dict()
                stats[doc.id.replace("_", " ", 1)] = len(d.get("hashes", []))
            if stats:
                return stats
    except Exception:
        pass

    data = _local_load()
    return {
        key: len(val.get("hashes", []))
        for key, val in data.items()
    }
