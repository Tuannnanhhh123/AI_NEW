# exam_history.py
import os
import json
import hashlib
import threading
from typing import List, Dict, Set

# ================== CONFIG ==================
MAX_HISTORY = 500
LOCAL_FILE = "exam_history.json"

# ================== FIREBASE ==================
try:
    from firebase_config import get_firestore_db
    _db = get_firestore_db()
    _FIREBASE_OK = True
except Exception as e:
    print("[Firebase Init Error]:", e)
    _FIREBASE_OK = False

_lock = threading.Lock()


# =================================================
#  HASH QUESTION (Safe Version)
# =================================================
def _hash_question(question_text: str) -> str:
    if not question_text:
        return ""

    text = str(question_text).strip().lower().rstrip(".?!")
    text = " ".join(text.split())

    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:24]


# =================================================
#  LOCAL STORAGE
# =================================================
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


# =================================================
#  GET USED HASHES (Merge FS + Local)
# =================================================
def get_used_hashes(subject: str, grade: str) -> Set[str]:
    key = f"{subject}_{grade}"

    hashes = set()

    # ---- Firestore ----
    if _FIREBASE_OK:
        try:
            doc = _db.collection("exam_history").document(key).get()
            if doc.exists:
                fs_hashes = doc.to_dict().get("hashes", [])
                hashes.update(fs_hashes)
        except Exception as e:
            print("[Firestore Read Error]:", e)

    # ---- Local ----
    data = _local_load()
    hashes.update(data.get(key, {}).get("hashes", []))

    return hashes


# =================================================
#  SAVE EXAM
# =================================================
def save_exam(subject: str, grade: str, questions: List[Dict]):
    key = f"{subject}_{grade}"

    # --- Hash questions safely ---
    new_hashes = []
    for q in questions:
        q_text = q.get("question", "")
        h = _hash_question(q_text)
        if h:
            new_hashes.append(h)

    if not new_hashes:
        print("[Warning] No valid questions to save.")
        return

    # =================================================
    # FIRESTORE SAVE
    # =================================================
    if _FIREBASE_OK:
        try:
            doc_ref = _db.collection("exam_history").document(key)
            doc = doc_ref.get()

            existing = []
            if doc.exists:
                existing = doc.to_dict().get("hashes", [])

            combined = list(dict.fromkeys(existing + new_hashes))
            combined = combined[-MAX_HISTORY:]

            doc_ref.set({"hashes": combined})

            print(f"[Firestore] Saved {len(new_hashes)} hashes.")

        except Exception as e:
            print("[Firestore Save Error]:", e)

    # =================================================
    # LOCAL SAVE (Always backup)
    # =================================================
    with _lock:
        data = _local_load()

        existing_local = data.get(key, {}).get("hashes", [])
        combined_local = list(dict.fromkeys(existing_local + new_hashes))
        combined_local = combined_local[-MAX_HISTORY:]

        data[key] = {"hashes": combined_local}
        _local_save(data)

        print(f"[Local] Saved {len(new_hashes)} hashes.")


# =================================================
#  CLEAR HISTORY
# =================================================
def clear_history():
    # ---- Firestore ----
    if _FIREBASE_OK:
        try:
            docs = list(_db.collection("exam_history").stream())
            for doc in docs:
                doc.reference.delete()
            print("[Firestore] Cleared history.")
        except Exception as e:
            print("[Firestore Clear Error]:", e)

    # ---- Local ----
    with _lock:
        _local_save({})
        print("[Local] Cleared history.")


# =================================================
#  GET STATS
# =================================================
def get_history_stats():
    stats = {}

    # Firestore
    if _FIREBASE_OK:
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
