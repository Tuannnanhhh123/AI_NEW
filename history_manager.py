# ============================================================
# history_manager.py — Stable Production Version
# Lưu lịch sử câu hỏi bằng:
# 1. Firestore (nếu có)
# 2. Local JSON (backup)
# ============================================================

import os
import json
import hashlib
import threading
from datetime import datetime
from typing import List, Dict, Set

# ================= CONFIG =================
MAX_HISTORY = 500
LOCAL_FILE = "exam_history.json"

_lock = threading.Lock()

# ================= FIRESTORE INIT =================
try:
    from firebase_manager import _db, _FIREBASE_OK
except Exception as e:
    print("[Firebase Import Error]:", e)
    _db = None
    _FIREBASE_OK = False


# ============================================================
# HASH QUESTION (An toàn tuyệt đối)
# ============================================================
def _hash_question(question_text: str) -> str:
    if not question_text:
        return ""

    text = str(question_text).strip().lower().rstrip(".?!")
    text = " ".join(text.split())

    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:24]


# ============================================================
# LOCAL STORAGE
# ============================================================
def _local_load() -> dict:
    if not os.path.exists(LOCAL_FILE):
        return {}

    try:
        with open(LOCAL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("[Local Load Error]:", e)
        return {}


def _local_save(data: dict):
    try:
        with open(LOCAL_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("[Local Save Error]:", e)


# ============================================================
# GET USED HASHES
# ============================================================
def get_used_hashes(subject: str, grade: str) -> Set[str]:
    key = f"{subject}_{grade}"
    hashes = set()

    # ----- Firestore -----
    if _FIREBASE_OK and _db:
        try:
            doc = _db.collection("exam_history").document(key).get()
            if doc.exists:
                hashes.update(doc.to_dict().get("hashes", []))
        except Exception as e:
            print("[Firestore Read Error]:", e)

    # ----- Local -----
    data = _local_load()
    hashes.update(data.get(key, {}).get("hashes", []))

    return hashes


# ============================================================
# SAVE EXAM
# ============================================================
def save_exam(subject: str, grade: str, questions: List[Dict]):
    key = f"{subject}_{grade}"

    # ---- Tạo hash mới ----
    new_hashes = []
    for q in questions:
        if not isinstance(q, dict):
            continue

        h = _hash_question(q.get("question", ""))
        if h:
            new_hashes.append(h)

    if not new_hashes:
        print("[Warning] No valid questions to save.")
        return

    # ============================================================
    # FIRESTORE SAVE
    # ============================================================
    if _FIREBASE_OK and _db:
        try:
            doc_ref = _db.collection("exam_history").document(key)
            doc = doc_ref.get()

            existing = []
            if doc.exists:
                existing = doc.to_dict().get("hashes", [])

            combined = list(dict.fromkeys(existing + new_hashes))
            combined = combined[-MAX_HISTORY:]

            doc_ref.set({
                "hashes": combined,
                "last_updated": datetime.now().isoformat()
            })

            print(f"[Firestore] Saved {len(new_hashes)} hashes.")

        except Exception as e:
            print("[Firestore Save Error]:", e)

    # ============================================================
    # LOCAL SAVE (Backup luôn luôn)
    # ============================================================
    with _lock:
        data = _local_load()

        existing_local = data.get(key, {}).get("hashes", [])
        combined_local = list(dict.fromkeys(existing_local + new_hashes))
        combined_local = combined_local[-MAX_HISTORY:]

        data[key] = {
            "hashes": combined_local,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        _local_save(data)

        print(f"[Local] Saved {len(new_hashes)} hashes.")


# ============================================================
# FILTER NEW QUESTIONS
# ============================================================
def filter_new_questions(questions: List[Dict], used_hashes: Set[str]) -> List[Dict]:
    if not questions:
        return []

    filtered = []

    for q in questions:
        if not isinstance(q, dict):
            continue

        h = _hash_question(q.get("question", ""))

        if h and h not in used_hashes:
            filtered.append(q)

    return filtered


# ============================================================
# CLEAR HISTORY
# ============================================================
def clear_history(subject: str = None, grade: str = None):
    # ---- Firestore ----
    if _FIREBASE_OK and _db:
        try:
            if subject and grade:
                key = f"{subject}_{grade}"
                _db.collection("exam_history").document(key).delete()
            else:
                docs = list(_db.collection("exam_history").stream())
                for doc in docs:
                    doc.reference.delete()

            print("[Firestore] History cleared.")
        except Exception as e:
            print("[Firestore Clear Error]:", e)

    # ---- Local ----
    with _lock:
        data = _local_load()

        if subject and grade:
            data.pop(f"{subject}_{grade}", None)
        else:
            data = {}

        _local_save(data)
        print("[Local] History cleared.")


# ============================================================
# GET HISTORY STATS
# ============================================================
def get_history_stats() -> dict:
    stats = {}

    # Firestore
    if _FIREBASE_OK and _db:
        try:
            docs = _db.collection("exam_history").stream()
            for doc in docs:
                count = len(doc.to_dict().get("hashes", []))
                stats[doc.id.replace("_", " ")] = count
        except Exception as e:
            print("[Firestore Stats Error]:", e)

    # Local fallback
    data = _local_load()
    for k, v in data.items():
        stats[k.replace("_", " ")] = len(v.get("hashes", []))

    return stats
