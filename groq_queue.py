# ============================================================
# groq_queue.py — Rate limit Groq với hàng đợi + cache
# Dùng threading.Semaphore để giới hạn concurrent requests
# + cache kết quả xáo đề trong 5 phút để tránh gọi lặp
# ============================================================
import threading
import time
import hashlib
import json
import random
from typing import Callable

# ── Giới hạn tối đa N request Groq cùng lúc ─────────────
_MAX_CONCURRENT = 5
_semaphore  = threading.Semaphore(_MAX_CONCURRENT)

# ── Cache kết quả (in-memory, tự xóa sau TTL) ────────────
_cache: dict = {}
_cache_lock  = threading.Lock()
_CACHE_TTL   = 300   # 5 phút


def _cache_key(questions: list) -> str:
    raw = json.dumps([q["question"] for q in questions], ensure_ascii=False)
    return hashlib.md5(raw.encode()).hexdigest()[:12]


def _cache_get(key: str):
    with _cache_lock:
        if key in _cache:
            data, ts = _cache[key]
            if time.time() - ts < _CACHE_TTL:
                return data
            del _cache[key]
    return None


def _cache_set(key: str, data: list):
    with _cache_lock:
        if len(_cache) >= 200:
            oldest = min(_cache, key=lambda k: _cache[k][1])
            del _cache[oldest]
        _cache[key] = (data, time.time())


def call_groq_limited(groq_fn: Callable, questions: list,
                      timeout: float = 45.0) -> tuple:
    """
    Gọi Groq với:
    1. Cache hit  → trả về ngay, không gọi API
    2. Semaphore  → tối đa _MAX_CONCURRENT request cùng lúc
    3. Timeout    → nếu chờ quá lâu → fallback local shuffle
    """
    from ai_engine import _shuffle_local

    # 1. Kiểm tra cache
    key    = _cache_key(questions)
    cached = _cache_get(key)
    if cached:
        result = cached[:]
        random.shuffle(result)
        return result, "cache"

    # 2. Thử lấy semaphore
    acquired = _semaphore.acquire(timeout=timeout)
    if not acquired:
        return _shuffle_local(questions), "local"

    try:
        result, source = groq_fn(questions)
        if source == "ai":
            _cache_set(key, result)
        return result, source
    finally:
        _semaphore.release()


def get_queue_stats() -> dict:
    with _cache_lock:
        cache_count = len(_cache)
    return {
        "cache_entries":   cache_count,
        "max_concurrent":  _MAX_CONCURRENT,
        "semaphore_value": _semaphore._value,
    }