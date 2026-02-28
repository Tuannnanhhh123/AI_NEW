# ============================================================
# chatbox_page.py — Chatbox AI + UX cải thiện
# ============================================================
import requests, time
import streamlit as st
from config import GROQ_API_URL, GROQ_HEADERS, GROQ_MODEL

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

<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Preview – Chat AI</title>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Be Vietnam Pro', sans-serif; background: #dde6f5; padding: 1.5rem; }

.wrapper {
  max-width: 860px; margin: 0 auto;
  display: flex; gap: 1rem; height: 580px;
}

/* ── Sidebar ── */
.sidebar {
  width: 200px; flex-shrink: 0;
  background: #eef3fd;
  border: 1px solid #93c5fd;
  border-radius: 12px; padding: .75rem;
  display: flex; flex-direction: column; gap: .4rem;
}
.sidebar-label {
  font-size: .65rem; font-weight: 700; color: #1557b0;
  letter-spacing: .08em; text-transform: uppercase; margin-bottom: .3rem;
}
.conv-item {
  display: flex; align-items: center; gap: .3rem; margin-bottom: 3px;
}
.conv-btn {
  flex: 1; padding: .38rem .6rem; border-radius: 7px;
  font-size: .78rem; font-weight: 600; cursor: pointer;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  text-align: left; transition: all .15s; font-family: inherit;
}
.conv-btn.active {
  background: #1557b0; border: 1px solid #0d47a1; color: white;
}
.conv-btn.inactive {
  background: white; border: 1px solid #93c5fd; color: #1557b0;
}
.conv-btn.inactive:hover { background: #1557b0; color: white; border-color: #1557b0; }
.del-btn {
  width: 22px; height: 22px; border-radius: 5px;
  background: white; border: 1px solid #fca5a5;
  color: #d93025; font-size: .7rem; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.conv-time { font-size: .62rem; color: #7ba7d4; padding: 0 .2rem .3rem; }

/* ── Chat area ── */
.chat-area {
  flex: 1; display: flex; flex-direction: column;
  border: 1px solid #93c5fd; border-radius: 12px;
  overflow: hidden; background: #f4f8ff;
}

/* Header */
.chat-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: .65rem 1rem; border-bottom: 1px solid #dbeafe;
  background: #eef3fd; flex-shrink: 0;
}
.chat-title { font-weight: 700; font-size: .9rem; color: #0d47a1; }
.chat-meta  { font-size: .65rem; color: #1557b0; margin-top: 1px; }

/* Messages */
.messages {
  flex: 1; overflow-y: auto; padding: 1rem;
  display: flex; flex-direction: column; gap: .5rem;
  background: #f4f8ff;
}

/* Bubble user — xanh đậm */
.bubble-user-wrap { display: flex; justify-content: flex-end; }
.bubble-user {
  background: linear-gradient(135deg, #1557b0, #0d47a1);
  color: white; padding: .55rem .9rem;
  border-radius: 16px 16px 4px 16px;
  max-width: 68%; font-size: .82rem; line-height: 1.5;
  box-shadow: 0 3px 12px rgba(13,71,161,.35);
}

/* Bubble AI */
.bubble-ai-wrap { display: flex; align-items: flex-end; gap: .4rem; }
.ai-avatar {
  width: 26px; height: 26px; border-radius: 50%;
  background: linear-gradient(135deg, #1557b0, #7c3aed);
  display: flex; align-items: center; justify-content: center;
  font-size: .75rem; flex-shrink: 0;
}
.bubble-ai {
  background: white; color: #1a1a2e;
  padding: .45rem .8rem;
  border-radius: 16px 16px 16px 4px;
  max-width: 68%; font-size: .8rem; line-height: 1.55;
  border: 1px solid #dbeafe;
  box-shadow: 0 1px 4px rgba(13,71,161,.08);
}

/* Quick chips */
.chips-wrap {
  padding: .6rem 1rem; border-bottom: 1px solid #dbeafe;
  background: #f4f8ff;
}
.chips-label {
  font-size: .62rem; font-weight: 700; color: #1557b0;
  letter-spacing: .08em; text-transform: uppercase; margin-bottom: .4rem;
}
.chips { display: flex; flex-wrap: wrap; gap: .4rem; }
.chip {
  display: inline-flex; align-items: center; gap: .3rem;
  background: white; border: 2px solid #1557b0;
  border-radius: 20px; padding: .25rem .65rem;
  font-size: .72rem; color: #1557b0; cursor: pointer;
  font-weight: 600; white-space: nowrap; transition: all .15s;
  font-family: inherit;
}
.chip:hover {
  background: linear-gradient(135deg, #1557b0, #0d47a1);
  color: white; border-color: #0d47a1;
  box-shadow: 0 3px 8px rgba(13,71,161,.25);
}

/* Input */
.input-wrap {
  padding: .6rem 1rem; border-top: 1px solid #dbeafe;
  background: #eef3fd; display: flex; gap: .5rem; flex-shrink: 0;
}
.input-box {
  flex: 1; border: 1px solid #93c5fd; border-radius: 8px;
  padding: .4rem .75rem; font-size: .82rem;
  font-family: inherit; outline: none; background: white; color: #1a1a2e;
}
.input-box:focus { border-color: #1557b0; box-shadow: 0 0 0 3px rgba(13,71,161,.1); }
.send-btn {
  background: linear-gradient(135deg, #1557b0, #0d47a1);
  color: white; border: none; border-radius: 8px;
  padding: .4rem .9rem; font-size: .8rem; font-weight: 700;
  cursor: pointer; font-family: inherit; transition: all .2s;
  white-space: nowrap;
}
.send-btn:hover { background: linear-gradient(135deg, #0d47a1, #0a3880); transform: translateY(-1px); }

/* hint */
.hint { font-size: .62rem; color: #1557b0; text-align: right; padding: .2rem 1rem .4rem; background: #eef3fd; }

/* nav */
.nav-row {
  display: flex; gap: .5rem; padding: .5rem 1rem;
  border-top: 1px solid #dbeafe; background: #eef3fd; flex-shrink: 0;
}
.nav-btn {
  flex: 1; padding: .38rem; border-radius: 8px;
  font-size: .78rem; font-weight: 600; cursor: pointer;
  font-family: inherit; transition: all .2s;
}
.nav-btn.secondary {
  background: white; border: 2px solid #1557b0; color: #1557b0;
}
.nav-btn.secondary:hover {
  background: linear-gradient(135deg, #1557b0, #0d47a1);
  color: white; border-color: #0d47a1;
}
.nav-btn.primary {
  background: linear-gradient(135deg, #1557b0, #0d47a1);
  border: none; color: white;
  box-shadow: 0 3px 10px rgba(13,71,161,.3);
}
.nav-btn.primary:hover { background: linear-gradient(135deg, #0d47a1, #0a3880); }
</style>
</head>
<body>

<div class="wrapper">

  <!-- Sidebar -->
  <div class="sidebar">
    <div class="sidebar-label">💬 Hội thoại</div>

    <div class="conv-item">
      <button class="conv-btn active">▸ Giải đạo hàm lớp 12</button>
      <button class="del-btn">✕</button>
    </div>
    <div class="conv-time">14:32 · 01/03</div>

    <div class="conv-item">
      <button class="conv-btn inactive">Cách dùng web</button>
      <button class="del-btn">✕</button>
    </div>
    <div class="conv-time">09:15 · 28/02</div>

    <div class="conv-item">
      <button class="conv-btn inactive">Phân biệt axit bazơ</button>
      <button class="del-btn">✕</button>
    </div>
    <div class="conv-time">21:40 · 27/02</div>
  </div>

  <!-- Chat area -->
  <div class="chat-area">

    <!-- Header -->
    <div class="chat-header">
      <div>
        <div class="chat-title">Giải đạo hàm lớp 12</div>
        <div class="chat-meta">🤖 llama-3.3-70b-versatile &nbsp;· 2 lượt</div>
      </div>
    </div>

    <!-- Quick chips -->
    <div class="chips-wrap">
      <div class="chips-label">💡 Gợi ý</div>
      <div class="chips">
        <button class="chip">🌐 Cách sử dụng web này?</button>
        <button class="chip">📊 Xem lịch sử bài thi ở đâu?</button>
        <button class="chip">📐 Giải thích công thức đạo hàm</button>
        <button class="chip">⚗️ Phân biệt axit và bazơ</button>
        <button class="chip">🇬🇧 Thì hiện tại hoàn thành</button>
        <button class="chip">🎲 Cách tính xác suất lớp 12</button>
      </div>
    </div>

    <!-- Messages -->
    <div class="messages">
      <div class="bubble-ai-wrap">
        <div class="ai-avatar">🤖</div>
        <div class="bubble-ai">Xin chào! Tôi có thể giúp gì cho bạn hôm nay? 😊</div>
      </div>

      <div class="bubble-user-wrap">
        <div class="bubble-user">Giải thích công thức đạo hàm của hàm hợp cho mình với</div>
      </div>

      <div class="bubble-ai-wrap">
        <div class="ai-avatar">🤖</div>
        <div class="bubble-ai">
          Đạo hàm của hàm hợp <b>y = f(g(x))</b> được tính theo quy tắc:<br><br>
          <b>y' = f'(g(x)) · g'(x)</b><br><br>
          Nói đơn giản: đạo hàm ngoài × đạo hàm trong. Bạn muốn mình giải ví dụ cụ thể không?
        </div>
      </div>

      <div class="bubble-user-wrap">
        <div class="bubble-user">Ví dụ y = sin(x²) thì tính như thế nào?</div>
      </div>
    </div>

    <!-- Input -->
    <div class="input-wrap">
      <input class="input-box" type="text" placeholder="Nhập câu hỏi của bạn…">
      <button class="send-btn">Gửi ➤</button>
    </div>
    <div class="hint">Nhấn Enter hoặc Gửi ➤</div>

    <!-- Nav -->
    <div class="nav-row">
      <button class="nav-btn secondary">← Trang chủ</button>
      <button class="nav-btn primary">🚀 Làm bài ngay</button>
    </div>

  </div>
</div>

</body>
</html>
                         type="primary", key="chat_exam"):
                st.session_state.page = "select"; st.rerun()

