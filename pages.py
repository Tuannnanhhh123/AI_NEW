<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Preview – Chọn đề thi v2</title>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Be Vietnam Pro', sans-serif;
  background: #eef2fb;
  padding: 2rem;
  color: #1a1a2e;
}

.page {
  max-width: 720px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

h2 { font-size: 1.4rem; font-weight: 800; color: #1a1a2e; }

.sec-title {
  font-size: .68rem; font-weight: 700; color: #94a3b8;
  letter-spacing: .08em; text-transform: uppercase; margin-bottom: .6rem;
}

/* ── Grid layouts ── */
.subj-grid  { display: grid; grid-template-columns: repeat(3,1fr); gap: .6rem; }
.grade-grid { display: grid; grid-template-columns: repeat(5,1fr); gap: .6rem; }
.nq-grid    { display: grid; grid-template-columns: repeat(4,1fr); gap: .6rem; }
.bottom-row { display: grid; grid-template-columns: 1fr 1fr; gap: .75rem; }

/* ── PRIMARY button ── */
.btn {
  width: 100%; padding: .5rem .8rem;
  border-radius: 8px; font-size: .82rem; font-weight: 700;
  cursor: pointer; border: 2px solid transparent;
  transition: all .2s; font-family: 'Be Vietnam Pro', sans-serif;
}

.btn-primary {
  background: linear-gradient(135deg, #1557b0, #0d47a1);
  border-color: transparent;
  color: white;
  box-shadow: 0 3px 10px rgba(13,71,161,.3);
}
.btn-primary:hover {
  background: linear-gradient(135deg, #0d47a1, #0a3880);
  box-shadow: 0 5px 16px rgba(13,71,161,.4);
  transform: translateY(-1px);
}

/* ── SECONDARY button — trắng + viền xanh → hover xanh đậm ── */
.btn-secondary {
  background: white;
  border: 2px solid #1557b0;
  color: #1557b0;
}
.btn-secondary:hover {
  background: linear-gradient(135deg, #1557b0, #0d47a1);
  border-color: #0d47a1;
  color: white;
  box-shadow: 0 4px 12px rgba(13,71,161,.3);
  transform: translateY(-1px);
}

/* ── Grade card ── */
.grade-card {
  background: white; border-radius: 12px; padding: 1rem .75rem;
  border: 2px solid #c5d8fc; cursor: pointer;
  transition: all .2s; text-align: center;
  box-shadow: 0 2px 8px rgba(21,87,176,.08);
}
.grade-card:hover {
  border-color: #1557b0; transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(21,87,176,.18);
  background: #eef3fd;
}
.grade-card.active {
  border-color: #0d47a1;
  background: linear-gradient(135deg, #e8f0fe, #dbeafe);
  box-shadow: 0 4px 16px rgba(13,71,161,.2);
}
.grade-emoji { font-size: 1.6rem; margin-bottom: .3rem; }
.grade-name  { font-size: .78rem; font-weight: 700; color: #0d47a1; }
.grade-desc  { font-size: .68rem; color: #1557b0; margin-top: .2rem; font-weight: 600; }

.grade-btn-row { display: grid; grid-template-columns: repeat(5,1fr); gap: .6rem; margin-top: .5rem; }

/* ── Exam summary ── */
.exam-summary {
  background: linear-gradient(135deg, #eef3fd, #dbeafe);
  border: 1px solid #93c5fd; border-left: 4px solid #1557b0;
  border-radius: 10px; padding: .75rem 1rem;
  font-size: .85rem; color: #1e3a5f; font-weight: 500;
}

hr { border: none; border-top: 1px solid #dde4f5; }

.btn-lg { padding: .65rem 1rem; font-size: .88rem; border-radius: 10px; }

/* number input */
.num-input {
  border: 1px solid #1557b0; border-radius: 8px;
  padding: .45rem .75rem; font-size: .85rem;
  font-family: 'Be Vietnam Pro', sans-serif;
  color: #1a1a2e; width: 100%; margin-top: .4rem; outline: none;
}
.num-input:focus { border-color: #0d47a1; box-shadow: 0 0 0 3px rgba(13,71,161,.1); }
label.input-label { font-size: .8rem; font-weight: 600; color: #1a1a2e; }

/* hover label */
.hint {
  text-align: center; font-size: .7rem; color: #94a3b8;
  margin-top: -.5rem;
  font-style: italic;
}
</style>
</head>
<body>
<div class="page">

  <h2>📋 Chọn đề thi</h2>
  <p class="hint">👆 Hover vào các nút để xem hiệu ứng</p>

  <!-- Môn học -->
  <div>
    <div class="sec-title">📚 Chọn môn học</div>
    <div class="subj-grid">
      <button class="btn btn-primary">🔢 Toán</button>
      <button class="btn btn-secondary">📖 Ngữ Văn</button>
      <button class="btn btn-secondary">🇬🇧 Tiếng Anh</button>
      <button class="btn btn-secondary">⚡ Vật Lý</button>
      <button class="btn btn-secondary">⚗️ Hóa Học</button>
      <button class="btn btn-secondary">🧬 Sinh Học</button>
    </div>
  </div>

  <!-- Lớp -->
  <div>
    <div class="sec-title">🏫 Chọn lớp / cấp độ</div>
    <div class="grade-grid">
      <div class="grade-card">
        <div class="grade-emoji">🎯</div>
        <div class="grade-name">Lớp 9</div>
        <div class="grade-desc">20 phút</div>
      </div>
      <div class="grade-card active">
        <div class="grade-emoji">📊</div>
        <div class="grade-name">Lớp 10</div>
        <div class="grade-desc">25 phút</div>
      </div>
      <div class="grade-card">
        <div class="grade-emoji">📡</div>
        <div class="grade-name">Lớp 11</div>
        <div class="grade-desc">25 phút</div>
      </div>
      <div class="grade-card">
        <div class="grade-emoji">🏆</div>
        <div class="grade-name">Lớp 12</div>
        <div class="grade-desc">25 phút</div>
      </div>
      <div class="grade-card">
        <div class="grade-emoji">🎓</div>
        <div class="grade-name">Đại học</div>
        <div class="grade-desc">30 phút</div>
      </div>
    </div>
    <div class="grade-btn-row">
      <button class="btn btn-secondary" style="font-size:.75rem;padding:.35rem">Chọn</button>
      <button class="btn btn-primary"   style="font-size:.75rem;padding:.35rem">Chọn</button>
      <button class="btn btn-secondary" style="font-size:.75rem;padding:.35rem">Chọn</button>
      <button class="btn btn-secondary" style="font-size:.75rem;padding:.35rem">Chọn</button>
      <button class="btn btn-secondary" style="font-size:.75rem;padding:.35rem">Chọn</button>
    </div>
  </div>

  <!-- Số câu -->
  <div>
    <div class="sec-title">🔢 Số câu hỏi</div>
    <div class="nq-grid">
      <button class="btn btn-secondary">16 câu</button>
      <button class="btn btn-primary">20 câu</button>
      <button class="btn btn-secondary">25 câu</button>
      <button class="btn btn-secondary">30 câu</button>
    </div>
    <div style="margin-top:.75rem">
      <label class="input-label">Hoặc nhập số câu tuỳ ý:</label>
      <input class="num-input" type="number" value="20" min="16" max="100">
    </div>
  </div>

  <!-- Tóm tắt -->
  <div class="exam-summary">
    💡 <b>Toán</b> · Lớp 10 (THPT) · <b>20 câu</b> · ⏱️ 25 phút · Đầy đủ 6 môn, nền tảng THPT
  </div>

  <hr>

  <!-- Nút dưới -->
  <div class="bottom-row">
    <button class="btn btn-secondary btn-lg">← Quay lại</button>
    <button class="btn btn-primary btn-lg">✨ Tạo đề thi</button>
  </div>

</div>
</body>
</html>
