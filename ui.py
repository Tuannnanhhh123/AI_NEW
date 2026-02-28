<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Preview – Sidebar Stats Card</title>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: 'Be Vietnam Pro', sans-serif;
    background: #eef2fb;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: 2rem;
  }

  .scene {
    display: flex;
    gap: 2rem;
    align-items: flex-start;
    flex-wrap: wrap;
    justify-content: center;
  }

  /* ── Sidebar mock ── */
  .sidebar {
    width: 230px;
    background: #fff;
    border-radius: 16px;
    padding: 1.2rem 1rem;
    box-shadow: 0 4px 24px rgba(26,115,232,.10);
    display: flex;
    flex-direction: column;
    gap: .5rem;
  }

  .sidebar-title {
    font-size: 1rem;
    font-weight: 800;
    color: #1a73e8;
    margin-bottom: .3rem;
    display: flex; align-items: center; gap: .4rem;
  }

  .avatar-row {
    display: flex; align-items: center; gap: .6rem;
    padding: .4rem 0 .6rem;
    border-bottom: 1px solid #eef1fb;
    margin-bottom: .2rem;
  }
  .avatar {
    width: 36px; height: 36px; border-radius: 50%;
    background: linear-gradient(135deg,#1a73e8,#0d47a1);
    display: flex; align-items: center; justify-content: center;
    font-size: .85rem; font-weight: 700; color: white; flex-shrink: 0;
  }
  .avatar-info .name  { font-size: .85rem; font-weight: 700; color: #1a1a2e; }
  .avatar-info .email { font-size: .68rem; color: #94a3b8; }

  /* Nav buttons */
  .nav-btn {
    display: block; width: 100%;
    padding: .38rem .7rem;
    border-radius: 8px;
    font-size: .8rem; font-weight: 600;
    color: #555; background: transparent;
    border: 1px solid transparent;
    cursor: pointer; text-align: left;
    transition: all .15s;
  }
  .nav-btn:hover { background: #f0f4ff; color: #1a73e8; }
  .nav-btn.active {
    background: #e8f0fe; color: #1a73e8;
    border-color: #c5d8fc;
  }

  .divider { border: none; border-top: 1px solid #eef1fb; margin: .3rem 0; }

  /* ── Stats card (phần được sửa) ── */
  .stats-card {
    background: #fff;
    border-left: 4px solid #1a73e8;
    border-radius: 8px;
    padding: .65rem .85rem;
    box-shadow: 0 2px 10px rgba(26,115,232,.12);
    margin: .2rem 0;
    animation: fadeUp .4s ease both;
  }
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  .stats-card-title {
    font-weight: 700;
    font-size: .78rem;
    color: #1a73e8;
    margin-bottom: .4rem;
    display: flex; align-items: center; gap: .3rem;
    letter-spacing: .01em;
  }
  .stats-card-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: .28rem 0;
    font-size: .75rem;
    color: #555;
    border-bottom: 1px solid #f0f4ff;
  }
  .stats-card-row:last-child { border-bottom: none; }
  .stats-card-row .label { display: flex; align-items: center; gap: .3rem; }
  .stats-card-count {
    font-weight: 700;
    color: #1a73e8;
    background: #e8f0fe;
    padding: .1rem .45rem;
    border-radius: 99px;
    font-size: .7rem;
  }

  .delete-btn {
    width: 100%; padding: .35rem;
    border-radius: 7px; border: 1px solid #fce8e6;
    background: #fff5f5; color: #d93025;
    font-size: .75rem; font-weight: 600;
    cursor: pointer; margin-top: .3rem;
    transition: background .15s;
  }
  .delete-btn:hover { background: #fce8e6; }

  /* ── Callout bên phải ── */
  .callout {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    max-width: 340px;
    box-shadow: 0 4px 24px rgba(0,0,0,.08);
  }
  .callout h2 { font-size: 1.1rem; font-weight: 800; color: #1a1a2e; margin-bottom: 1rem; }
  .change-item {
    display: flex; gap: .7rem; align-items: flex-start;
    margin-bottom: .85rem;
  }
  .change-icon {
    width: 32px; height: 32px; border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem; flex-shrink: 0;
  }
  .change-icon.blue  { background: #e8f0fe; }
  .change-icon.green { background: #e8f5e9; }
  .change-icon.red   { background: #fce8e6; }
  .change-text .title { font-size: .82rem; font-weight: 700; color: #1a1a2e; }
  .change-text .desc  { font-size: .74rem; color: #888; margin-top: .1rem; }

  .badge {
    display: inline-block;
    background: #1a73e8; color: white;
    font-size: .65rem; font-weight: 700;
    padding: .1rem .45rem; border-radius: 99px;
    margin-left: .35rem; vertical-align: middle;
  }
</style>
</head>
<body>
<div class="scene">

  <!-- Sidebar mock -->
  <div class="sidebar">
    <div class="sidebar-title">🎓 AI Exam Generator</div>

    <div class="avatar-row">
      <div class="avatar">NV</div>
      <div class="avatar-info">
        <div class="name">Nguyễn Văn A</div>
        <div class="email">lop12@thpt.edu.vn</div>
      </div>
    </div>

    <button class="nav-btn">🏠 Trang chủ</button>
    <button class="nav-btn active">📋 Lịch sử</button>
    <button class="nav-btn">💬 Chat AI</button>
    <button class="nav-btn">⚙️ Cài đặt</button>

    <hr class="divider">

    <!-- Stats card — phần được đổi màu -->
    <div class="stats-card">
      <div class="stats-card-title">📊 Câu hỏi đã dùng</div>
      <div class="stats-card-row">
        <span class="label">📖 Toán / Lớp 12</span>
        <span class="stats-card-count">24 câu</span>
      </div>
      <div class="stats-card-row">
        <span class="label">📖 Vật Lý / Lớp 12</span>
        <span class="stats-card-count">18 câu</span>
      </div>
      <div class="stats-card-row">
        <span class="label">📖 Hóa Học / Lớp 11</span>
        <span class="stats-card-count">12 câu</span>
      </div>
      <div class="stats-card-row">
        <span class="label">📖 Tiếng Anh / Lớp 10</span>
        <span class="stats-card-count">9 câu</span>
      </div>
      <button class="delete-btn">🗑️ Xóa lịch sử câu hỏi</button>
    </div>

    <hr class="divider">
    <button class="nav-btn" style="color:#d93025">🚪 Đăng xuất</button>
  </div>

  <!-- Callout giải thích thay đổi -->
  <div class="callout">
    <h2>✨ Thay đổi trong bản cập nhật</h2>

    <div class="change-item">
      <div class="change-icon blue">🃏</div>
      <div class="change-text">
        <div class="title">Kiểu card với viền trái xanh <span class="badge">MỚI</span></div>
        <div class="desc">Nền trắng sạch, viền trái xanh #1a73e8 nổi bật, shadow nhẹ tạo chiều sâu.</div>
      </div>
    </div>

    <div class="change-item">
      <div class="change-icon blue">🔢</div>
      <div class="change-text">
        <div class="title">Số câu dạng badge pill</div>
        <div class="desc">Số câu đã dùng hiển thị dạng pill xanh — dễ đọc hơn so với text thuần.</div>
      </div>
    </div>

    <div class="change-item">
      <div class="change-icon green">📏</div>
      <div class="change-text">
        <div class="title">Phân cách hàng rõ ràng</div>
        <div class="desc">Mỗi môn một hàng, đường kẻ nhạt #f0f4ff chia tách gọn gàng.</div>
      </div>
    </div>

    <div class="change-item">
      <div class="change-icon red">🗑️</div>
      <div class="change-text">
        <div class="title">Nút xóa nằm trong card</div>
        <div class="desc">Nút xóa được đặt ngay trong card, màu đỏ nhẹ để không gây nhầm lẫn.</div>
      </div>
    </div>
  </div>

</div>
</body>
</html>
