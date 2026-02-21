# ============================================================
# banks/toan_l9.py — Ngân hàng Toán Lớp 9
# Thêm câu hỏi vào list QUESTIONS bên dưới
# Cấu trúc mỗi câu:
# {
#   "question": "Nội dung câu hỏi?",
#   "options": ["A", "B", "C", "D"],   ← đúng 4 lựa chọn
#   "answer": "B",                      ← phải khớp 1 trong 4 options
#   "explanation": "Giải thích..."
# }
# ============================================================

QUESTIONS = [
  {"question":"Giải phương trình: 2x + 3 = 7","options":["A. x = 1","B. x = 2","C. x = 3","D. x = 4"],"answer":"B","explanation":"2x = 4 ⇒ x = 2."},
{"question":"Giải phương trình: x² = 9","options":["A. x = 3","B. x = -3","C. x = ±3","D. x = 9"],"answer":"C","explanation":"x² = 9 ⇒ x = ±3."},
{"question":"Giá trị của √16 là?","options":["A. 2","B. 4","C. -4","D. 8"],"answer":"B","explanation":"√16 = 4."},
{"question":"Hệ phương trình có nghiệm duy nhất khi?","options":["A. a/a' ≠ b/b'","B. a/a' = b/b'","C. b/b' = c/c'","D. a = 0"],"answer":"A","explanation":"Điều kiện có nghiệm duy nhất."},
{"question":"Đồ thị hàm số y = ax² (a ≠ 0) là?","options":["A. Đường thẳng","B. Parabol","C. Hyperbol","D. Đường tròn"],"answer":"B","explanation":"Hàm bậc hai có đồ thị là parabol."},

{"question":"Giải phương trình: x² - 5x + 6 = 0","options":["A. x = 2; 3","B. x = -2; -3","C. x = 1; 6","D. x = -1; -6"],"answer":"A","explanation":"(x-2)(x-3)=0."},
{"question":"Tổng hai nghiệm của phương trình x² - 3x + 2 = 0 là?","options":["A. 2","B. 3","C. -3","D. -2"],"answer":"B","explanation":"Theo Viète: S = 3."},
{"question":"Giải bất phương trình: x - 4 > 0","options":["A. x > 4","B. x < 4","C. x ≥ 4","D. x ≤ 4"],"answer":"A","explanation":"Chuyển vế."},
{"question":"Căn bậc hai số học của 25 là?","options":["A. -5","B. 5","C. ±5","D. 25"],"answer":"B","explanation":"Căn số học là số không âm."},
{"question":"Tam giác vuông có định lí nào?","options":["A. Ta-lét","B. Pitago","C. Viète","D. Ơ-clit"],"answer":"B","explanation":"Định lí Pitago."},

{"question":"Nếu a² = 7 thì a bằng?","options":["A. √7","B. -√7","C. ±√7","D. 7"],"answer":"C","explanation":"Hai nghiệm đối nhau."},
{"question":"Hàm số y = 2x + 1 có hệ số góc là?","options":["A. 1","B. 2","C. -1","D. -2"],"answer":"B","explanation":"Hệ số góc là hệ số của x."},
{"question":"Phương trình bậc hai có Δ < 0 thì?","options":["A. Có 2 nghiệm","B. Có nghiệm kép","C. Vô nghiệm","D. 1 nghiệm"],"answer":"C","explanation":"Δ < 0 vô nghiệm."},
{"question":"Giải hệ: x + y = 5; x - y = 1","options":["A. x=3,y=2","B. x=2,y=3","C. x=4,y=1","D. x=1,y=4"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Diện tích hình tròn bán kính r là?","options":["A. 2πr","B. πr²","C. πd","D. r²"],"answer":"B","explanation":"Công thức diện tích."},

{"question":"Giải phương trình: 3x - 9 = 0","options":["A. x=1","B. x=2","C. x=3","D. x=4"],"answer":"C","explanation":"3x=9."},
{"question":"Nếu Δ = 0 thì phương trình có?","options":["A. 2 nghiệm phân biệt","B. Nghiệm kép","C. Vô nghiệm","D. 3 nghiệm"],"answer":"B","explanation":"Δ=0 có nghiệm kép."},
{"question":"Chu vi hình tròn là?","options":["A. πr²","B. 2πr","C. r²","D. πd²"],"answer":"B","explanation":"Công thức chu vi."},
{"question":"Giá trị của 3² là?","options":["A. 6","B. 9","C. 3","D. 12"],"answer":"B","explanation":"3×3=9."},
{"question":"Giải: x² = 0","options":["A. x=0","B. x=1","C. x=-1","D. x=±1"],"answer":"A","explanation":"0 có căn là 0."},

{"question":"Hàm số y = -x² mở xuống khi?","options":["A. a>0","B. a<0","C. a=0","D. a=1"],"answer":"B","explanation":"a<0 parabol mở xuống."},
{"question":"Tích hai nghiệm của x² - 4 = 0 là?","options":["A. 4","B. -4","C. 0","D. 2"],"answer":"B","explanation":"Nghiệm ±2 ⇒ tích -4."},
{"question":"Giải bất phương trình: 2x ≤ 6","options":["A. x ≤ 3","B. x ≥ 3","C. x < 3","D. x > 3"],"answer":"A","explanation":"Chia 2."},
{"question":"Công thức nghiệm phương trình bậc hai dùng?","options":["A. Δ","B. S","C. P","D. m"],"answer":"A","explanation":"Dùng biệt thức Δ."},
{"question":"Trong tam giác vuông, cạnh huyền bình phương bằng?","options":["A. Tổng bình phương hai cạnh góc vuông","B. Hiệu bình phương","C. Tích","D. Chu vi"],"answer":"A","explanation":"Định lí Pitago."},
{"question":"Giải phương trình: 4x - 8 = 0","options":["A. x=1","B. x=2","C. x=3","D. x=4"],"answer":"B","explanation":"4x=8 ⇒ x=2."},
{"question":"Giải phương trình: x² - 1 = 0","options":["A. x=1","B. x=-1","C. x=±1","D. x=0"],"answer":"C","explanation":"x²=1 ⇒ x=±1."},
{"question":"Giá trị của √49 là?","options":["A. 6","B. 7","C. -7","D. 14"],"answer":"B","explanation":"√49=7."},
{"question":"Hàm số y = -3x + 2 có hệ số góc là?","options":["A. -3","B. 3","C. 2","D. -2"],"answer":"A","explanation":"Hệ số của x là -3."},
{"question":"Giải bất phương trình: x + 5 ≥ 0","options":["A. x ≥ -5","B. x ≤ -5","C. x > -5","D. x < -5"],"answer":"A","explanation":"Chuyển vế."},

{"question":"Giải phương trình: x² - 9 = 0","options":["A. x=3","B. x=-3","C. x=±3","D. x=9"],"answer":"C","explanation":"x²=9."},
{"question":"Tổng hai nghiệm của x² + 5x + 6 = 0 là?","options":["A. -5","B. 5","C. -6","D. 6"],"answer":"A","explanation":"S = -b/a = -5."},
{"question":"Tích hai nghiệm của x² + 5x + 6 = 0 là?","options":["A. 5","B. 6","C. -6","D. -5"],"answer":"B","explanation":"P = c/a = 6."},
{"question":"Giải hệ: x+y=7; x-y=3","options":["A. x=5,y=2","B. x=2,y=5","C. x=4,y=3","D. x=3,y=4"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Diện tích tam giác là?","options":["A. a+b+c","B. 1/2 ah","C. πr²","D. 2πr"],"answer":"B","explanation":"Công thức diện tích."},

{"question":"Giải phương trình: 5x=20","options":["A. x=2","B. x=3","C. x=4","D. x=5"],"answer":"C","explanation":"20/5=4."},
{"question":"Nếu Δ > 0 thì phương trình bậc hai có?","options":["A. 2 nghiệm phân biệt","B. Nghiệm kép","C. Vô nghiệm","D. 3 nghiệm"],"answer":"A","explanation":"Δ>0."},
{"question":"Chu vi hình chữ nhật là?","options":["A. a+b","B. 2(a+b)","C. ab","D. a²"],"answer":"B","explanation":"Công thức chu vi."},
{"question":"Giá trị của 2³ là?","options":["A. 6","B. 8","C. 4","D. 9"],"answer":"B","explanation":"2×2×2=8."},
{"question":"Giải: x² = 4","options":["A. x=2","B. x=-2","C. x=±2","D. x=4"],"answer":"C","explanation":"Hai nghiệm."},

{"question":"Hàm số y = x² có đồ thị?","options":["A. Đường thẳng","B. Parabol","C. Đường tròn","D. Hyperbol"],"answer":"B","explanation":"Hàm bậc hai."},
{"question":"Tổng hai nghiệm của x² - 6x + 9 = 0 là?","options":["A. 6","B. -6","C. 9","D. -9"],"answer":"A","explanation":"S=6."},
{"question":"Giải bất phương trình: 3x < 9","options":["A. x<3","B. x>3","C. x≤3","D. x≥3"],"answer":"A","explanation":"Chia 3."},
{"question":"Cạnh huyền tam giác vuông cạnh góc vuông 3 và 4 là?","options":["A. 5","B. 6","C. 7","D. 4"],"answer":"A","explanation":"3²+4²=5²."},
{"question":"Giá trị của √81 là?","options":["A. 8","B. 9","C. -9","D. 18"],"answer":"B","explanation":"√81=9."},

{"question":"Giải phương trình: x² + 4x = 0","options":["A. x=0; -4","B. x=4","C. x=-4","D. x=2"],"answer":"A","explanation":"x(x+4)=0."},
{"question":"Hệ số tự do của y = 2x + 5 là?","options":["A. 2","B. 5","C. -2","D. -5"],"answer":"B","explanation":"Số không nhân x."},
{"question":"Giải: 7x - 14 = 0","options":["A. x=1","B. x=2","C. x=3","D. x=4"],"answer":"B","explanation":"7x=14."},
{"question":"Diện tích hình vuông cạnh a là?","options":["A. 4a","B. a²","C. 2a","D. a³"],"answer":"B","explanation":"a×a."},
{"question":"Giá trị của 10² là?","options":["A. 20","B. 100","C. 10","D. 200"],"answer":"B","explanation":"10×10."},

{"question":"Giải phương trình: x² - 16 = 0","options":["A. x=4","B. x=-4","C. x=±4","D. x=16"],"answer":"C","explanation":"x²=16."},
{"question":"Tổng hai nghiệm của x² + 2x - 3 = 0 là?","options":["A. -2","B. 2","C. -3","D. 3"],"answer":"A","explanation":"S=-b/a=-2."},
{"question":"Tích hai nghiệm của x² + 2x - 3 = 0 là?","options":["A. -3","B. 3","C. -2","D. 2"],"answer":"A","explanation":"P=c/a=-3."},
{"question":"Giải bất phương trình: x/2 ≥ 3","options":["A. x≥6","B. x≤6","C. x>6","D. x<6"],"answer":"A","explanation":"Nhân 2."},
{"question":"Định lí Ta-lét áp dụng trong?","options":["A. Tam giác","B. Hình tròn","C. Hình vuông","D. Parabol"],"answer":"A","explanation":"Định lí trong tam giác."},

{"question":"Giải phương trình: 9x = 27","options":["A. x=2","B. x=3","C. x=4","D. x=5"],"answer":"B","explanation":"27/9=3."},
{"question":"Giá trị của √0 là?","options":["A. 0","B. 1","C. -1","D. Không xác định"],"answer":"A","explanation":"√0=0."},
{"question":"Hàm số y = ax² + bx + c (a≠0) là?","options":["A. Bậc nhất","B. Bậc hai","C. Bậc ba","D. Hằng số"],"answer":"B","explanation":"Định nghĩa."},
{"question":"Giải phương trình: x² - 2x = 0","options":["A. x=0;2","B. x=2","C. x=0","D. x=-2"],"answer":"A","explanation":"x(x-2)=0."},
{"question":"Giá trị của 4² là?","options":["A. 8","B. 12","C. 16","D. 20"],"answer":"C","explanation":"4×4=16."},
{"question":"Giải phương trình: 6x = 18","options":["A. x=2","B. x=3","C. x=4","D. x=6"],"answer":"B","explanation":"18/6=3."},
{"question":"Giá trị của √121 là?","options":["A. 10","B. 11","C. -11","D. 12"],"answer":"B","explanation":"√121=11."},
{"question":"Giải phương trình: x² - 25 = 0","options":["A. x=5","B. x=-5","C. x=±5","D. x=25"],"answer":"C","explanation":"x²=25."},
{"question":"Tổng hai nghiệm của x² - 4x + 3 = 0 là?","options":["A. 4","B. -4","C. 3","D. -3"],"answer":"A","explanation":"S=-b/a=4."},
{"question":"Tích hai nghiệm của x² - 4x + 3 = 0 là?","options":["A. 4","B. 3","C. -3","D. -4"],"answer":"B","explanation":"P=c/a=3."},

{"question":"Giải bất phương trình: 2x > 10","options":["A. x>5","B. x<5","C. x≥5","D. x≤5"],"answer":"A","explanation":"Chia 2."},
{"question":"Diện tích hình tròn bán kính r là?","options":["A. 2πr","B. πr²","C. πd","D. r²"],"answer":"B","explanation":"Công thức diện tích."},
{"question":"Chu vi hình tròn bán kính r là?","options":["A. πr²","B. 2πr","C. πd²","D. r²"],"answer":"B","explanation":"Công thức chu vi."},
{"question":"Giải phương trình: x² + 9 = 0","options":["A. 3","B. -3","C. ±3","D. Vô nghiệm (R)"],"answer":"D","explanation":"x²=-9 không có nghiệm thực."},
{"question":"Giá trị của 5² là?","options":["A. 10","B. 20","C. 25","D. 15"],"answer":"C","explanation":"5×5=25."},

{"question":"Giải hệ: x+y=10; x-y=2","options":["A. x=6,y=4","B. x=4,y=6","C. x=5,y=5","D. x=8,y=2"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải phương trình: 8x-16=0","options":["A. x=1","B. x=2","C. x=3","D. x=4"],"answer":"B","explanation":"8x=16."},
{"question":"Nếu Δ = 0 thì phương trình bậc hai có?","options":["A. 2 nghiệm","B. 1 nghiệm kép","C. Vô nghiệm","D. 3 nghiệm"],"answer":"B","explanation":"Δ=0 có nghiệm kép."},
{"question":"Giải: x² - 2 = 0","options":["A. x=2","B. x=-2","C. x=±√2","D. x=√2"],"answer":"C","explanation":"x=±√2."},
{"question":"Giá trị của √144 là?","options":["A. 11","B. 12","C. 13","D. 14"],"answer":"B","explanation":"√144=12."},

{"question":"Giải phương trình: 3x+6=0","options":["A. x=-2","B. x=2","C. x=-3","D. x=3"],"answer":"A","explanation":"3x=-6."},
{"question":"Diện tích hình chữ nhật 5 và 8 là?","options":["A. 13","B. 40","C. 26","D. 20"],"answer":"B","explanation":"5×8=40."},
{"question":"Giải phương trình: x²+1=0","options":["A. 1","B. -1","C. ±1","D. Vô nghiệm (R)"],"answer":"D","explanation":"Không có nghiệm thực."},
{"question":"Giá trị của 3³ là?","options":["A. 9","B. 18","C. 27","D. 81"],"answer":"C","explanation":"3×3×3=27."},
{"question":"Giải bất phương trình: -2x > 4","options":["A. x> -2","B. x< -2","C. x>2","D. x<2"],"answer":"B","explanation":"Chia số âm đổi chiều."},

{"question":"Giải phương trình: x² - 7x = 0","options":["A. x=0;7","B. x=7","C. x=0","D. x=-7"],"answer":"A","explanation":"x(x-7)=0."},
{"question":"Giá trị của √196 là?","options":["A. 12","B. 13","C. 14","D. 15"],"answer":"C","explanation":"√196=14."},
{"question":"Hệ số góc của y=5x-1 là?","options":["A. 5","B. -1","C. -5","D. 1"],"answer":"A","explanation":"Hệ số x."},
{"question":"Giải phương trình: 12x=36","options":["A. x=2","B. x=3","C. x=4","D. x=6"],"answer":"B","explanation":"36/12=3."},
{"question":"Diện tích tam giác vuông cạnh góc vuông 6 và 8 là?","options":["A. 24","B. 48","C. 14","D. 28"],"answer":"A","explanation":"1/2×6×8=24."},

{"question":"Giải phương trình: x²-36=0","options":["A. x=6","B. x=-6","C. x=±6","D. x=36"],"answer":"C","explanation":"x²=36."},
{"question":"Giá trị của 7² là?","options":["A. 14","B. 49","C. 21","D. 28"],"answer":"B","explanation":"7×7=49."},
{"question":"Giải bất phương trình: 5x≤20","options":["A. x≤4","B. x≥4","C. x<4","D. x>4"],"answer":"A","explanation":"Chia 5."},
{"question":"Giải phương trình: x²+6x+9=0","options":["A. x=-3 kép","B. x=3 kép","C. x=±3","D. 2 nghiệm"],"answer":"A","explanation":"(x+3)²=0."},
{"question":"Giá trị của √225 là?","options":["A. 13","B. 14","C. 15","D. 16"],"answer":"C","explanation":"√225=15."},
{"question":"Giải phương trình: 15x = 45","options":["A. x=2","B. x=3","C. x=4","D. x=5"],"answer":"B","explanation":"45/15=3."},
{"question":"Giá trị của √256 là?","options":["A. 14","B. 15","C. 16","D. 18"],"answer":"C","explanation":"√256=16."},
{"question":"Giải phương trình: x² - 49 = 0","options":["A. x=7","B. x=-7","C. x=±7","D. x=49"],"answer":"C","explanation":"x²=49."},
{"question":"Tổng hai nghiệm của x² - 8x + 12 = 0 là?","options":["A. 8","B. -8","C. 12","D. -12"],"answer":"A","explanation":"S=-b/a=8."},
{"question":"Tích hai nghiệm của x² - 8x + 12 = 0 là?","options":["A. 8","B. 12","C. -12","D. -8"],"answer":"B","explanation":"P=c/a=12."},

{"question":"Giải bất phương trình: 4x < 16","options":["A. x<4","B. x>4","C. x≤4","D. x≥4"],"answer":"A","explanation":"Chia 4."},
{"question":"Diện tích hình vuông cạnh 9 là?","options":["A. 18","B. 27","C. 81","D. 36"],"answer":"C","explanation":"9²=81."},
{"question":"Giải phương trình: x² + 16 = 0","options":["A. 4","B. -4","C. ±4","D. Vô nghiệm (R)"],"answer":"D","explanation":"x²=-16 vô nghiệm thực."},
{"question":"Giá trị của 6² là?","options":["A. 12","B. 18","C. 36","D. 30"],"answer":"C","explanation":"6×6=36."},
{"question":"Giải hệ: x+y=12; x-y=4","options":["A. x=8,y=4","B. x=6,y=6","C. x=4,y=8","D. x=10,y=2"],"answer":"A","explanation":"Cộng hai phương trình."},

{"question":"Giải phương trình: 10x - 30 = 0","options":["A. x=2","B. x=3","C. x=4","D. x=5"],"answer":"B","explanation":"10x=30."},
{"question":"Nếu Δ < 0 thì phương trình bậc hai có?","options":["A. 2 nghiệm","B. 1 nghiệm kép","C. Vô nghiệm (R)","D. 3 nghiệm"],"answer":"C","explanation":"Δ<0 vô nghiệm thực."},
{"question":"Giải: x² - 5 = 0","options":["A. x=±√5","B. x=5","C. x=-5","D. x=√5"],"answer":"A","explanation":"x=±√5."},
{"question":"Giá trị của √324 là?","options":["A. 16","B. 17","C. 18","D. 19"],"answer":"C","explanation":"√324=18."},
{"question":"Giải phương trình: 2x+8=0","options":["A. x=-4","B. x=4","C. x=-2","D. x=2"],"answer":"A","explanation":"2x=-8."},

{"question":"Diện tích hình chữ nhật 7 và 9 là?","options":["A. 16","B. 63","C. 32","D. 56"],"answer":"B","explanation":"7×9=63."},
{"question":"Giải phương trình: x²+4x+4=0","options":["A. x=-2 kép","B. x=2 kép","C. x=±2","D. 2 nghiệm"],"answer":"A","explanation":"(x+2)²=0."},
{"question":"Giá trị của 8² là?","options":["A. 16","B. 32","C. 48","D. 64"],"answer":"D","explanation":"8×8=64."},
{"question":"Giải bất phương trình: 6x ≥ 18","options":["A. x≥3","B. x≤3","C. x>3","D. x<3"],"answer":"A","explanation":"Chia 6."},
{"question":"Giải phương trình: x² - 10x = 0","options":["A. x=0;10","B. x=10","C. x=0","D. x=-10"],"answer":"A","explanation":"x(x-10)=0."},

{"question":"Giá trị của √400 là?","options":["A. 18","B. 19","C. 20","D. 25"],"answer":"C","explanation":"√400=20."},
{"question":"Hệ số tự do của y=-4x+7 là?","options":["A. -4","B. 4","C. 7","D. -7"],"answer":"C","explanation":"Số không nhân x."},
{"question":"Giải phương trình: 20x=100","options":["A. x=2","B. x=3","C. x=4","D. x=5"],"answer":"D","explanation":"100/20=5."},
{"question":"Diện tích tam giác có đáy 10 và cao 6 là?","options":["A. 60","B. 30","C. 16","D. 20"],"answer":"B","explanation":"1/2×10×6=30."},
{"question":"Giải phương trình: x² - 64 = 0","options":["A. x=8","B. x=-8","C. x=±8","D. x=64"],"answer":"C","explanation":"x²=64."},

{"question":"Giá trị của 9² là?","options":["A. 18","B. 27","C. 81","D. 90"],"answer":"C","explanation":"9×9=81."},
{"question":"Giải bất phương trình: 7x ≤ 21","options":["A. x≤3","B. x≥3","C. x<3","D. x>3"],"answer":"A","explanation":"Chia 7."},
{"question":"Giải phương trình: x²+12x+36=0","options":["A. x=-6 kép","B. x=6 kép","C. x=±6","D. 2 nghiệm"],"answer":"A","explanation":"(x+6)²=0."},
{"question":"Giá trị của √625 là?","options":["A. 20","B. 22","C. 25","D. 30"],"answer":"C","explanation":"√625=25."},
{"question":"Giải phương trình: 14x-28=0","options":["A. x=1","B. x=2","C. x=3","D. x=4"],"answer":"B","explanation":"14x=28."},
{"question":"Giải phương trình: 18x = 54","options":["A. x=2","B. x=3","C. x=4","D. x=6"],"answer":"B","explanation":"54/18=3."},
{"question":"Giá trị của √289 là?","options":["A. 15","B. 16","C. 17","D. 18"],"answer":"C","explanation":"√289=17."},
{"question":"Giải phương trình: x² - 81 = 0","options":["A. x=9","B. x=-9","C. x=±9","D. x=81"],"answer":"C","explanation":"x²=81."},
{"question":"Tổng hai nghiệm của x² - 9x + 20 = 0 là?","options":["A. 9","B. -9","C. 20","D. -20"],"answer":"A","explanation":"S=-b/a=9."},
{"question":"Tích hai nghiệm của x² - 9x + 20 = 0 là?","options":["A. 9","B. 20","C. -20","D. -9"],"answer":"B","explanation":"P=c/a=20."},

{"question":"Giải bất phương trình: 9x < 27","options":["A. x<3","B. x>3","C. x≤3","D. x≥3"],"answer":"A","explanation":"Chia 9."},
{"question":"Diện tích hình vuông cạnh 12 là?","options":["A. 24","B. 48","C. 144","D. 36"],"answer":"C","explanation":"12²=144."},
{"question":"Giải phương trình: x² + 25 = 0","options":["A. 5","B. -5","C. ±5","D. Vô nghiệm (R)"],"answer":"D","explanation":"x²=-25 vô nghiệm thực."},
{"question":"Giá trị của 11² là?","options":["A. 110","B. 121","C. 100","D. 111"],"answer":"B","explanation":"11×11=121."},
{"question":"Giải hệ: x+y=14; x-y=6","options":["A. x=10,y=4","B. x=8,y=6","C. x=7,y=7","D. x=12,y=2"],"answer":"A","explanation":"Cộng hai phương trình."},

{"question":"Giải phương trình: 25x - 50 = 0","options":["A. x=1","B. x=2","C. x=3","D. x=4"],"answer":"B","explanation":"25x=50."},
{"question":"Nếu Δ = 16 và a≠0 thì phương trình bậc hai có?","options":["A. 2 nghiệm phân biệt","B. 1 nghiệm kép","C. Vô nghiệm","D. 3 nghiệm"],"answer":"A","explanation":"Δ>0 có 2 nghiệm phân biệt."},
{"question":"Giải: x² - 12 = 0","options":["A. x=±√12","B. x=12","C. x=-12","D. x=√12"],"answer":"A","explanation":"x=±√12."},
{"question":"Giá trị của √361 là?","options":["A. 17","B. 18","C. 19","D. 20"],"answer":"C","explanation":"√361=19."},
{"question":"Giải phương trình: 4x+12=0","options":["A. x=-3","B. x=3","C. x=-4","D. x=4"],"answer":"A","explanation":"4x=-12."},

{"question":"Diện tích hình chữ nhật 11 và 5 là?","options":["A. 16","B. 55","C. 50","D. 45"],"answer":"B","explanation":"11×5=55."},
{"question":"Giải phương trình: x²+8x+16=0","options":["A. x=-4 kép","B. x=4 kép","C. x=±4","D. 2 nghiệm"],"answer":"A","explanation":"(x+4)²=0."},
{"question":"Giá trị của 12² là?","options":["A. 124","B. 144","C. 132","D. 142"],"answer":"B","explanation":"12×12=144."},
{"question":"Giải bất phương trình: 8x ≥ 32","options":["A. x≥4","B. x≤4","C. x>4","D. x<4"],"answer":"A","explanation":"Chia 8."},
{"question":"Giải phương trình: x² - 15x = 0","options":["A. x=0;15","B. x=15","C. x=0","D. x=-15"],"answer":"A","explanation":"x(x-15)=0."},

{"question":"Giá trị của √484 là?","options":["A. 20","B. 21","C. 22","D. 23"],"answer":"C","explanation":"√484=22."},
{"question":"Hệ số góc của y=-7x+9 là?","options":["A. -7","B. 7","C. 9","D. -9"],"answer":"A","explanation":"Hệ số của x."},
{"question":"Giải phương trình: 30x=150","options":["A. x=4","B. x=5","C. x=6","D. x=3"],"answer":"B","explanation":"150/30=5."},
{"question":"Diện tích tam giác có đáy 14 và cao 8 là?","options":["A. 56","B. 112","C. 44","D. 64"],"answer":"A","explanation":"1/2×14×8=56."},
{"question":"Giải phương trình: x² - 100 = 0","options":["A. x=10","B. x=-10","C. x=±10","D. x=100"],"answer":"C","explanation":"x²=100."},

{"question":"Giá trị của 13² là?","options":["A. 169","B. 139","C. 159","D. 179"],"answer":"A","explanation":"13×13=169."},
{"question":"Giải bất phương trình: 12x ≤ 48","options":["A. x≤4","B. x≥4","C. x<4","D. x>4"],"answer":"A","explanation":"Chia 12."},
{"question":"Giải phương trình: x²+14x+49=0","options":["A. x=-7 kép","B. x=7 kép","C. x=±7","D. 2 nghiệm"],"answer":"A","explanation":"(x+7)²=0."},
{"question":"Giá trị của √729 là?","options":["A. 25","B. 26","C. 27","D. 28"],"answer":"C","explanation":"√729=27."},
{"question":"Giải phương trình: 16x-64=0","options":["A. x=2","B. x=3","C. x=4","D. x=5"],"answer":"C","explanation":"16x=64."},
{"question":"Giải phương trình: 21x = 63","options":["A. x=2","B. x=3","C. x=4","D. x=5"],"answer":"B","explanation":"63/21=3."},
{"question":"Giá trị của √900 là?","options":["A. 20","B. 25","C. 30","D. 35"],"answer":"C","explanation":"√900=30."},
{"question":"Giải phương trình: x² - 121 = 0","options":["A. x=11","B. x=-11","C. x=±11","D. x=121"],"answer":"C","explanation":"x²=121."},
{"question":"Tổng hai nghiệm của x² - 11x + 24 = 0 là?","options":["A. 11","B. -11","C. 24","D. -24"],"answer":"A","explanation":"S=-b/a=11."},
{"question":"Tích hai nghiệm của x² - 11x + 24 = 0 là?","options":["A. 11","B. 24","C. -24","D. -11"],"answer":"B","explanation":"P=c/a=24."},

{"question":"Giải bất phương trình: 15x < 45","options":["A. x<3","B. x>3","C. x≤3","D. x≥3"],"answer":"A","explanation":"Chia 15."},
{"question":"Diện tích hình vuông cạnh 15 là?","options":["A. 225","B. 150","C. 200","D. 250"],"answer":"A","explanation":"15²=225."},
{"question":"Giải phương trình: x² + 36 = 0","options":["A. 6","B. -6","C. ±6","D. Vô nghiệm (R)"],"answer":"D","explanation":"x²=-36 vô nghiệm thực."},
{"question":"Giá trị của 14² là?","options":["A. 196","B. 186","C. 206","D. 176"],"answer":"A","explanation":"14×14=196."},
{"question":"Giải hệ: x+y=20; x-y=4","options":["A. x=12,y=8","B. x=10,y=10","C. x=14,y=6","D. x=8,y=12"],"answer":"A","explanation":"Cộng hai phương trình."},

{"question":"Giải phương trình: 40x-80=0","options":["A. x=1","B. x=2","C. x=3","D. x=4"],"answer":"B","explanation":"40x=80."},
{"question":"Giải phương trình: x² - 18x = 0","options":["A. x=0;18","B. x=18","C. x=0","D. x=-18"],"answer":"A","explanation":"x(x-18)=0."},
{"question":"Giá trị của √1024 là?","options":["A. 30","B. 31","C. 32","D. 33"],"answer":"C","explanation":"√1024=32."},
{"question":"Giải phương trình: 5x+25=0","options":["A. x=-5","B. x=5","C. x=-4","D. x=4"],"answer":"A","explanation":"5x=-25."},
{"question":"Diện tích tam giác đáy 20 cao 10 là?","options":["A. 200","B. 100","C. 150","D. 250"],"answer":"B","explanation":"1/2×20×10=100."},
{"question":"Giải phương trình: x² - 5x + 6 = 0","options":["A. x=2;3","B. x=1;6","C. x=-2;-3","D. x=3;6"],"answer":"A","explanation":"(x-2)(x-3)=0."},

{"question":"Giải hệ: 2x+y=5; x-y=1","options":["A. x=2,y=1","B. x=1,y=3","C. x=3,y=-1","D. x=2,y=3"],"answer":"A","explanation":"Cộng hai phương trình."},

{"question":"Cho tam giác vuông có cạnh góc vuông 6 và 8. Cạnh huyền bằng?","options":["A. 10","B. 12","C. 14","D. 9"],"answer":"A","explanation":"6²+8²=10²."},

{"question":"Giải bất phương trình: 3x - 7 ≥ 2","options":["A. x≥3","B. x≤3","C. x>3","D. x<3"],"answer":"A","explanation":"3x≥9."},

{"question":"Rút gọn: (x²-9)/(x-3) (x≠3)","options":["A. x-3","B. x+3","C. x²-3","D. 3"],"answer":"B","explanation":"x²-9=(x-3)(x+3)."},

{"question":"Cho Δ = 25. Phương trình bậc hai có bao nhiêu nghiệm?","options":["A. 2 phân biệt","B. 1 kép","C. 0","D. 3"],"answer":"A","explanation":"Δ>0."},

{"question":"Tính diện tích hình tròn bán kính 5","options":["A. 10π","B. 25π","C. 5π","D. 20π"],"answer":"B","explanation":"πr²."},

{"question":"Giải phương trình: x²+4x+4=0","options":["A. x=-2 kép","B. x=2 kép","C. ±2","D. 2 nghiệm"],"answer":"A","explanation":"(x+2)²=0."},

{"question":"Một hình chữ nhật có chu vi 40, chiều dài hơn chiều rộng 4. Chiều dài là?","options":["A. 12","B. 14","C. 10","D. 8"],"answer":"B","explanation":"Giải hệ lập từ P=40."},

{"question":"Giải phương trình: x² - 2x - 8 = 0","options":["A. x=4;-2","B. x=2;-4","C. x=8;-1","D. x=1;-8"],"answer":"A","explanation":"(x-4)(x+2)=0."},
{"question":"Giải phương trình: 24x = 72","options":["A. x=2","B. x=3","C. x=4","D. x=6"],"answer":"B","explanation":"72/24=3."},
{"question":"Giá trị của √441 là?","options":["A. 19","B. 20","C. 21","D. 22"],"answer":"C","explanation":"√441=21."},
{"question":"Giải phương trình: x² - 144 = 0","options":["A. x=12","B. x=-12","C. x=±12","D. x=144"],"answer":"C","explanation":"x²=144."},
{"question":"Tổng hai nghiệm của x² - 13x + 30 = 0 là?","options":["A. 13","B. -13","C. 30","D. -30"],"answer":"A","explanation":"S=-b/a=13."},
{"question":"Tích hai nghiệm của x² - 13x + 30 = 0 là?","options":["A. 13","B. 30","C. -30","D. -13"],"answer":"B","explanation":"P=c/a=30."},

{"question":"Giải bất phương trình: 18x < 54","options":["A. x<3","B. x>3","C. x≤3","D. x≥3"],"answer":"A","explanation":"Chia 18."},
{"question":"Diện tích hình vuông cạnh 18 là?","options":["A. 324","B. 288","C. 360","D. 300"],"answer":"A","explanation":"18²=324."},
{"question":"Giải phương trình: x² + 49 = 0","options":["A. 7","B. -7","C. ±7","D. Vô nghiệm (R)"],"answer":"D","explanation":"x²=-49 vô nghiệm thực."},
{"question":"Giá trị của 15² là?","options":["A. 215","B. 225","C. 235","D. 205"],"answer":"B","explanation":"15×15=225."},
{"question":"Giải hệ: x+y=30; x-y=10","options":["A. x=20,y=10","B. x=15,y=15","C. x=25,y=5","D. x=18,y=12"],"answer":"A","explanation":"Cộng hai phương trình."},

{"question":"Giải phương trình: 50x-100=0","options":["A. x=1","B. x=2","C. x=3","D. x=4"],"answer":"B","explanation":"50x=100."},
{"question":"Giải phương trình: x² - 21x = 0","options":["A. x=0;21","B. x=21","C. x=0","D. x=-21"],"answer":"A","explanation":"x(x-21)=0."},
{"question":"Giá trị của √1600 là?","options":["A. 35","B. 36","C. 40","D. 45"],"answer":"C","explanation":"√1600=40."},
{"question":"Giải phương trình: 9x+27=0","options":["A. x=-3","B. x=3","C. x=-4","D. x=4"],"answer":"A","explanation":"9x=-27."},
{"question":"Diện tích tam giác đáy 30 cao 12 là?","options":["A. 360","B. 180","C. 240","D. 300"],"answer":"B","explanation":"1/2×30×12=180."},

{"question":"Giải phương trình: x² - 169 = 0","options":["A. x=13","B. x=-13","C. x=±13","D. x=169"],"answer":"C","explanation":"x²=169."},
{"question":"Giá trị của 16² là?","options":["A. 246","B. 256","C. 266","D. 276"],"answer":"B","explanation":"16×16=256."},
{"question":"Giải bất phương trình: 25x ≥ 100","options":["A. x≥4","B. x≤4","C. x>4","D. x<4"],"answer":"A","explanation":"Chia 25."},
{"question":"Giải phương trình: x²+16x+64=0","options":["A. x=-8 kép","B. x=8 kép","C. x=±8","D. 2 nghiệm"],"answer":"A","explanation":"(x+8)²=0."},
{"question":"Giá trị của √2025 là?","options":["A. 40","B. 45","C. 50","D. 55"],"answer":"B","explanation":"√2025=45."},
{"question":"Giải phương trình: x² - 7x + 10 = 0","options":["A. x=2;5","B. x=1;10","C. x=-2;-5","D. x=7;3"],"answer":"A","explanation":"(x-2)(x-5)=0."},

{"question":"Giải hệ: 3x+y=7; x-y=1","options":["A. x=2,y=1","B. x=1,y=4","C. x=3,y=-2","D. x=2,y=3"],"answer":"A","explanation":"Cộng hai phương trình."},

{"question":"Cho tam giác vuông cạnh góc vuông 9 và 12. Cạnh huyền?","options":["A. 15","B. 18","C. 20","D. 21"],"answer":"A","explanation":"9²+12²=15²."},

{"question":"Giải bất phương trình: 4x-5>3","options":["A. x>2","B. x<2","C. x≥2","D. x≤2"],"answer":"A","explanation":"4x>8."},

{"question":"Rút gọn: (x²-16)/(x-4) (x≠4)","options":["A. x-4","B. x+4","C. x²-4","D. 4"],"answer":"B","explanation":"x²-16=(x-4)(x+4)."},

{"question":"Tính diện tích hình tròn bán kính 7","options":["A. 14π","B. 49π","C. 7π","D. 28π"],"answer":"B","explanation":"πr²."},

{"question":"Giải phương trình: x²+6x+9=0","options":["A. x=-3 kép","B. x=3 kép","C. x=±3","D. 2 nghiệm"],"answer":"A","explanation":"(x+3)²=0."},

{"question":"Một hình chữ nhật có chu vi 50, chiều dài hơn chiều rộng 5. Chiều dài?","options":["A. 15","B. 20","C. 18","D. 12"],"answer":"A","explanation":"Giải hệ từ 2(l+w)=50."},

{"question":"Giải phương trình: x² - 3x - 18 = 0","options":["A. x=6;-3","B. x=3;-6","C. x=18;-1","D. x=1;-18"],"answer":"A","explanation":"(x-6)(x+3)=0."},

{"question":"Cho Δ=0, phương trình bậc hai có?","options":["A. 2 nghiệm","B. 1 nghiệm kép","C. 0 nghiệm","D. 3 nghiệm"],"answer":"B","explanation":"Δ=0 nghiệm kép."},
{"question":"Giải phương trình: x² - 4x - 5 = 0","options":["A. x=5;-1","B. x=1;-5","C. x=4;-5","D. x=2;-3"],"answer":"A","explanation":"(x-5)(x+1)=0."},
{"question":"Giải phương trình: x² + x - 12 = 0","options":["A. x=3;-4","B. x=4;-3","C. x=2;-6","D. x=6;-2"],"answer":"A","explanation":"(x+4)(x-3)=0."},
{"question":"Giải hệ: 2x+3y=13; x+y=5","options":["A. x=2,y=3","B. x=3,y=2","C. x=4,y=1","D. x=1,y=4"],"answer":"A","explanation":"Thế x=5-y."},
{"question":"Giải bất phương trình: 5x - 2 ≤ 13","options":["A. x≤3","B. x≥3","C. x<3","D. x>3"],"answer":"A","explanation":"5x≤15."},
{"question":"Tìm m để phương trình x² - 2mx + 1 = 0 có nghiệm kép","options":["A. m=1","B. m=-1","C. m=±1","D. m=0"],"answer":"C","explanation":"Δ=0 ⇒4m²-4=0."},

{"question":"Cho tam giác vuông có cạnh góc vuông 5 và 12. Cạnh huyền?","options":["A. 13","B. 10","C. 15","D. 17"],"answer":"A","explanation":"5²+12²=13²."},
{"question":"Rút gọn: (x²-25)/(x-5) (x≠5)","options":["A. x-5","B. x+5","C. x²-5","D. 5"],"answer":"B","explanation":"x²-25=(x-5)(x+5)."},
{"question":"Giải phương trình: x² - 2x - 15 = 0","options":["A. x=5;-3","B. x=3;-5","C. x=15;-1","D. x=1;-15"],"answer":"A","explanation":"(x-5)(x+3)=0."},
{"question":"Tính diện tích hình tròn bán kính 10","options":["A. 20π","B. 100π","C. 10π","D. 50π"],"answer":"B","explanation":"πr²."},
{"question":"Giải phương trình: x² + 7x + 12 = 0","options":["A. x=-3;-4","B. x=3;4","C. x=-2;-6","D. x=2;6"],"answer":"A","explanation":"(x+3)(x+4)=0."},

{"question":"Giải hệ: 3x-y=5; x+y=7","options":["A. x=3,y=4","B. x=4,y=3","C. x=2,y=5","D. x=5,y=2"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: 2x+1>7","options":["A. x>3","B. x<3","C. x≥3","D. x≤3"],"answer":"A","explanation":"2x>6."},
{"question":"Tổng hai nghiệm của x² - 6x + 8 = 0","options":["A. 6","B. -6","C. 8","D. -8"],"answer":"A","explanation":"S=-b/a=6."},
{"question":"Tích hai nghiệm của x² - 6x + 8 = 0","options":["A. 6","B. 8","C. -8","D. -6"],"answer":"B","explanation":"P=c/a=8."},
{"question":"Giải phương trình: x² - 9x = 0","options":["A. x=0;9","B. x=9","C. x=0","D. x=-9"],"answer":"A","explanation":"x(x-9)=0."},

{"question":"Cho Δ = 36, phương trình bậc hai có?","options":["A. 2 nghiệm phân biệt","B. 1 nghiệm kép","C. Vô nghiệm","D. 3 nghiệm"],"answer":"A","explanation":"Δ>0."},
{"question":"Giải phương trình: x² + 2x - 24 = 0","options":["A. x=4;-6","B. x=6;-4","C. x=3;-8","D. x=8;-3"],"answer":"A","explanation":"(x+6)(x-4)=0."},
{"question":"Rút gọn: (x²-1)/(x-1) (x≠1)","options":["A. x-1","B. x+1","C. x²-1","D. 1"],"answer":"B","explanation":"x²-1=(x-1)(x+1)."},
{"question":"Giải hệ: x-y=2; 2x+y=7","options":["A. x=3,y=1","B. x=1,y=3","C. x=2,y=4","D. x=4,y=2"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: -3x < 9","options":["A. x>-3","B. x<-3","C. x>3","D. x<3"],"answer":"A","explanation":"Chia số âm đổi chiều."},

{"question":"Giải phương trình: x² - 16x + 64 = 0","options":["A. x=8 kép","B. x=-8 kép","C. x=±8","D. 2 nghiệm"],"answer":"A","explanation":"(x-8)²=0."},
{"question":"Cho tam giác vuông có cạnh góc vuông 7 và 24. Cạnh huyền?","options":["A. 25","B. 26","C. 27","D. 28"],"answer":"A","explanation":"7²+24²=25²."},
{"question":"Giải phương trình: x² - x - 6 = 0","options":["A. x=3;-2","B. x=2;-3","C. x=6;-1","D. x=1;-6"],"answer":"A","explanation":"(x-3)(x+2)=0."},
{"question":"Giải bất phương trình: 4x+3≥11","options":["A. x≥2","B. x≤2","C. x>2","D. x<2"],"answer":"A","explanation":"4x≥8."},
{"question":"Tính chu vi hình tròn bán kính 6","options":["A. 6π","B. 12π","C. 36π","D. 18π"],"answer":"B","explanation":"2πr."},

{"question":"Giải phương trình: x² + 5x - 14 = 0","options":["A. x=2;-7","B. x=7;-2","C. x=14;-1","D. x=1;-14"],"answer":"A","explanation":"(x+7)(x-2)=0."},
{"question":"Giải hệ: 4x+y=9; x-y=1","options":["A. x=2,y=1","B. x=1,y=2","C. x=3,y=-3","D. x=4,y=5"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải phương trình: x² - 3x = 10","options":["A. x=5;-2","B. x=2;-5","C. x=10;-1","D. x=1;-10"],"answer":"A","explanation":"x²-3x-10=0."},
{"question":"Rút gọn: (x²-9)/(x+3) (x≠-3)","options":["A. x-3","B. x+3","C. x²-3","D. 3"],"answer":"A","explanation":"x²-9=(x-3)(x+3)."},
{"question":"Giải bất phương trình: 7x-14>0","options":["A. x>2","B. x<2","C. x≥2","D. x≤2"],"answer":"A","explanation":"7x>14."},
{"question":"Giải phương trình: x² - 10x + 21 = 0","options":["A. x=3;7","B. x=1;21","C. x=10;11","D. x=-3;-7"],"answer":"A","explanation":"(x-3)(x-7)=0."},
{"question":"Giải phương trình: x² + 4x - 21 = 0","options":["A. x=3;-7","B. x=7;-3","C. x=21;-1","D. x=1;-21"],"answer":"A","explanation":"(x+7)(x-3)=0."},
{"question":"Giải hệ: 5x+y=11; x-y=1","options":["A. x=2,y=1","B. x=1,y=6","C. x=3,y=-4","D. x=4,y=-9"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: 6x-9≥3","options":["A. x≥2","B. x≤2","C. x>2","D. x<2"],"answer":"A","explanation":"6x≥12."},
{"question":"Tìm m để phương trình x² + mx + 4 = 0 có nghiệm kép","options":["A. m=4","B. m=-4","C. m=±4","D. m=0"],"answer":"C","explanation":"Δ=m²-16=0."},

{"question":"Cho tam giác vuông có cạnh góc vuông 8 và 15. Cạnh huyền?","options":["A. 16","B. 17","C. 18","D. 19"],"answer":"B","explanation":"8²+15²=17²."},
{"question":"Rút gọn: (x²-36)/(x-6) (x≠6)","options":["A. x-6","B. x+6","C. x²-6","D. 6"],"answer":"B","explanation":"x²-36=(x-6)(x+6)."},
{"question":"Giải phương trình: x² - x - 12 = 0","options":["A. x=4;-3","B. x=3;-4","C. x=12;-1","D. x=1;-12"],"answer":"A","explanation":"(x-4)(x+3)=0."},
{"question":"Tính diện tích hình tròn bán kính 12","options":["A. 24π","B. 144π","C. 12π","D. 72π"],"answer":"B","explanation":"πr²."},
{"question":"Giải phương trình: x² + 8x + 15 = 0","options":["A. x=-3;-5","B. x=3;5","C. x=-1;-15","D. x=1;15"],"answer":"A","explanation":"(x+3)(x+5)=0."},

{"question":"Giải hệ: 2x-y=4; x+y=5","options":["A. x=3,y=2","B. x=2,y=3","C. x=4,y=1","D. x=1,y=4"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: 3x+5>14","options":["A. x>3","B. x<3","C. x≥3","D. x≤3"],"answer":"A","explanation":"3x>9."},
{"question":"Tổng hai nghiệm của x² - 12x + 35 = 0","options":["A. 12","B. -12","C. 35","D. -35"],"answer":"A","explanation":"S=-b/a=12."},
{"question":"Tích hai nghiệm của x² - 12x + 35 = 0","options":["A. 12","B. 35","C. -35","D. -12"],"answer":"B","explanation":"P=c/a=35."},
{"question":"Giải phương trình: x² - 25x = 0","options":["A. x=0;25","B. x=25","C. x=0","D. x=-25"],"answer":"A","explanation":"x(x-25)=0."},

{"question":"Cho Δ = 49, phương trình bậc hai có?","options":["A. 2 nghiệm phân biệt","B. 1 nghiệm kép","C. Vô nghiệm","D. 3 nghiệm"],"answer":"A","explanation":"Δ>0."},
{"question":"Giải phương trình: x² + 9x - 10 = 0","options":["A. x=1;-10","B. x=10;-1","C. x=2;-5","D. x=5;-2"],"answer":"A","explanation":"(x+10)(x-1)=0."},
{"question":"Rút gọn: (x²-4)/(x-2) (x≠2)","options":["A. x-2","B. x+2","C. x²-2","D. 2"],"answer":"B","explanation":"x²-4=(x-2)(x+2)."},
{"question":"Giải hệ: x+y=9; 2x-y=3","options":["A. x=4,y=5","B. x=5,y=4","C. x=3,y=6","D. x=6,y=3"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: -4x ≤ 8","options":["A. x≥-2","B. x≤-2","C. x≥2","D. x≤2"],"answer":"A","explanation":"Chia số âm đổi chiều."},

{"question":"Giải phương trình: x² - 18x + 81 = 0","options":["A. x=9 kép","B. x=-9 kép","C. x=±9","D. 2 nghiệm"],"answer":"A","explanation":"(x-9)²=0."},
{"question":"Cho tam giác vuông có cạnh góc vuông 9 và 40. Cạnh huyền?","options":["A. 41","B. 42","C. 43","D. 44"],"answer":"A","explanation":"9²+40²=41²."},
{"question":"Giải phương trình: x² - 5x - 24 = 0","options":["A. x=8;-3","B. x=3;-8","C. x=6;-4","D. x=4;-6"],"answer":"A","explanation":"(x-8)(x+3)=0."},
{"question":"Giải bất phương trình: 9x+6≥24","options":["A. x≥2","B. x≤2","C. x>2","D. x<2"],"answer":"A","explanation":"9x≥18."},
{"question":"Tính chu vi hình tròn bán kính 9","options":["A. 9π","B. 18π","C. 27π","D. 36π"],"answer":"B","explanation":"2πr."},
{"question":"Giải phương trình: x² - 10x + 21 = 0","options":["A. x=3;7","B. x=1;21","C. x=10;11","D. x=-3;-7"],"answer":"A","explanation":"(x-3)(x-7)=0."},
{"question":"Giải phương trình: x² + 4x - 21 = 0","options":["A. x=3;-7","B. x=7;-3","C. x=21;-1","D. x=1;-21"],"answer":"A","explanation":"(x+7)(x-3)=0."},
{"question":"Giải hệ: 5x+y=11; x-y=1","options":["A. x=2,y=1","B. x=1,y=6","C. x=3,y=-4","D. x=4,y=-9"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: 6x-9≥3","options":["A. x≥2","B. x≤2","C. x>2","D. x<2"],"answer":"A","explanation":"6x≥12."},
{"question":"Tìm m để phương trình x² + mx + 4 = 0 có nghiệm kép","options":["A. m=4","B. m=-4","C. m=±4","D. m=0"],"answer":"C","explanation":"Δ=m²-16=0."},

{"question":"Cho tam giác vuông có cạnh góc vuông 8 và 15. Cạnh huyền?","options":["A. 16","B. 17","C. 18","D. 19"],"answer":"B","explanation":"8²+15²=17²."},
{"question":"Rút gọn: (x²-36)/(x-6) (x≠6)","options":["A. x-6","B. x+6","C. x²-6","D. 6"],"answer":"B","explanation":"x²-36=(x-6)(x+6)."},
{"question":"Giải phương trình: x² - x - 12 = 0","options":["A. x=4;-3","B. x=3;-4","C. x=12;-1","D. x=1;-12"],"answer":"A","explanation":"(x-4)(x+3)=0."},
{"question":"Tính diện tích hình tròn bán kính 12","options":["A. 24π","B. 144π","C. 12π","D. 72π"],"answer":"B","explanation":"πr²."},
{"question":"Giải phương trình: x² + 8x + 15 = 0","options":["A. x=-3;-5","B. x=3;5","C. x=-1;-15","D. x=1;15"],"answer":"A","explanation":"(x+3)(x+5)=0."},

{"question":"Giải hệ: 2x-y=4; x+y=5","options":["A. x=3,y=2","B. x=2,y=3","C. x=4,y=1","D. x=1,y=4"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: 3x+5>14","options":["A. x>3","B. x<3","C. x≥3","D. x≤3"],"answer":"A","explanation":"3x>9."},
{"question":"Tổng hai nghiệm của x² - 12x + 35 = 0","options":["A. 12","B. -12","C. 35","D. -35"],"answer":"A","explanation":"S=-b/a=12."},
{"question":"Tích hai nghiệm của x² - 12x + 35 = 0","options":["A. 12","B. 35","C. -35","D. -12"],"answer":"B","explanation":"P=c/a=35."},
{"question":"Giải phương trình: x² - 25x = 0","options":["A. x=0;25","B. x=25","C. x=0","D. x=-25"],"answer":"A","explanation":"x(x-25)=0."},

{"question":"Cho Δ = 49, phương trình bậc hai có?","options":["A. 2 nghiệm phân biệt","B. 1 nghiệm kép","C. Vô nghiệm","D. 3 nghiệm"],"answer":"A","explanation":"Δ>0."},
{"question":"Giải phương trình: x² + 9x - 10 = 0","options":["A. x=1;-10","B. x=10;-1","C. x=2;-5","D. x=5;-2"],"answer":"A","explanation":"(x+10)(x-1)=0."},
{"question":"Rút gọn: (x²-4)/(x-2) (x≠2)","options":["A. x-2","B. x+2","C. x²-2","D. 2"],"answer":"B","explanation":"x²-4=(x-2)(x+2)."},
{"question":"Giải hệ: x+y=9; 2x-y=3","options":["A. x=4,y=5","B. x=5,y=4","C. x=3,y=6","D. x=6,y=3"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: -4x ≤ 8","options":["A. x≥-2","B. x≤-2","C. x≥2","D. x≤2"],"answer":"A","explanation":"Chia số âm đổi chiều."},

{"question":"Giải phương trình: x² - 18x + 81 = 0","options":["A. x=9 kép","B. x=-9 kép","C. x=±9","D. 2 nghiệm"],"answer":"A","explanation":"(x-9)²=0."},
{"question":"Cho tam giác vuông có cạnh góc vuông 9 và 40. Cạnh huyền?","options":["A. 41","B. 42","C. 43","D. 44"],"answer":"A","explanation":"9²+40²=41²."},
{"question":"Giải phương trình: x² - 5x - 24 = 0","options":["A. x=8;-3","B. x=3;-8","C. x=6;-4","D. x=4;-6"],"answer":"A","explanation":"(x-8)(x+3)=0."},
{"question":"Giải bất phương trình: 9x+6≥24","options":["A. x≥2","B. x≤2","C. x>2","D. x<2"],"answer":"A","explanation":"9x≥18."},
{"question":"Tính chu vi hình tròn bán kính 9","options":["A. 9π","B. 18π","C. 27π","D. 36π"],"answer":"B","explanation":"2πr."},
{"question":"Giải phương trình: x² - 7x + 12 = 0","options":["A. x=3;4","B. x=2;6","C. x=1;12","D. x=-3;-4"],"answer":"A","explanation":"(x-3)(x-4)=0."},
{"question":"Giải hệ: x+y=5; 2x-y=1","options":["A. x=2,y=3","B. x=3,y=2","C. x=1,y=4","D. x=4,y=1"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: 3x-6≥0","options":["A. x≥2","B. x≤2","C. x>2","D. x<2"],"answer":"A","explanation":"3x≥6."},
{"question":"Tổng hai nghiệm của x² - 5x + 6 = 0","options":["A. 5","B. 6","C. -5","D. -6"],"answer":"A","explanation":"S=-b/a=5."},
{"question":"Tích hai nghiệm của x² - 5x + 6 = 0","options":["A. 5","B. 6","C. -6","D. -5"],"answer":"B","explanation":"P=c/a=6."},

{"question":"Giải phương trình: x² - 16 = 0","options":["A. x=4","B. x=-4","C. x=±4","D. x=0"],"answer":"C","explanation":"x²=16."},
{"question":"Rút gọn: (x²-9)/(x-3) (x≠3)","options":["A. x-3","B. x+3","C. x²-3","D. 3"],"answer":"B","explanation":"x²-9=(x-3)(x+3)."},
{"question":"Cho tam giác vuông có cạnh góc vuông 6 và 8. Cạnh huyền?","options":["A. 9","B. 10","C. 11","D. 12"],"answer":"B","explanation":"6²+8²=10²."},
{"question":"Tính diện tích hình tròn bán kính 5","options":["A. 10π","B. 25π","C. 5π","D. 50π"],"answer":"B","explanation":"πr²."},
{"question":"Giải phương trình: x² + 2x - 15 = 0","options":["A. x=3;-5","B. x=5;-3","C. x=1;-15","D. x=15;-1"],"answer":"A","explanation":"(x+5)(x-3)=0."},

{"question":"Giải hệ: 3x+y=7; x+y=3","options":["A. x=2,y=1","B. x=1,y=2","C. x=3,y=0","D. x=0,y=3"],"answer":"A","explanation":"Trừ hai phương trình."},
{"question":"Giải bất phương trình: 4x+8<0","options":["A. x<-2","B. x>-2","C. x≤-2","D. x≥-2"],"answer":"A","explanation":"4x<-8."},
{"question":"Cho Δ=0, phương trình bậc hai có","options":["A. 2 nghiệm phân biệt","B. 1 nghiệm kép","C. Vô nghiệm","D. 3 nghiệm"],"answer":"B","explanation":"Δ=0 ⇒ nghiệm kép."},
{"question":"Giải phương trình: x² - 9x = 0","options":["A. x=0;9","B. x=9","C. x=0","D. x=-9"],"answer":"A","explanation":"x(x-9)=0."},
{"question":"Chu vi hình tròn bán kính 7","options":["A. 7π","B. 14π","C. 49π","D. 21π"],"answer":"B","explanation":"2πr."},

{"question":"Giải phương trình: x² - 4x - 21 = 0","options":["A. x=7;-3","B. x=3;-7","C. x=1;-21","D. x=21;-1"],"answer":"A","explanation":"(x-7)(x+3)=0."},
{"question":"Giải hệ: 2x+y=9; x-y=1","options":["A. x=2,y=5","B. x=3,y=3","C. x=4,y=1","D. x=5,y=-1"],"answer":"B","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: -2x≤6","options":["A. x≥-3","B. x≤-3","C. x≥3","D. x≤3"],"answer":"A","explanation":"Chia số âm đổi chiều."},
{"question":"Tổng hai nghiệm của x² - 8x + 15 = 0","options":["A. 8","B. 15","C. -8","D. -15"],"answer":"A","explanation":"S=-b/a."},
{"question":"Tích hai nghiệm của x² - 8x + 15 = 0","options":["A. 8","B. 15","C. -15","D. -8"],"answer":"B","explanation":"P=c/a."},

{"question":"Cho tam giác vuông có cạnh góc vuông 9 và 12. Cạnh huyền?","options":["A. 13","B. 14","C. 15","D. 16"],"answer":"C","explanation":"9²+12²=15²."},
{"question":"Giải phương trình: x² + 7x + 10 = 0","options":["A. x=-5;-2","B. x=5;2","C. x=-1;-10","D. x=1;10"],"answer":"A","explanation":"(x+5)(x+2)=0."},
{"question":"Giải hệ: x+y=10; 3x-y=2","options":["A. x=3,y=7","B. x=4,y=6","C. x=2,y=8","D. x=5,y=5"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Diện tích hình tròn bán kính 10","options":["A. 20π","B. 100π","C. 10π","D. 50π"],"answer":"B","explanation":"πr²."},
{"question":"Giải phương trình: x² - 25 = 0","options":["A. x=5","B. x=-5","C. x=±5","D. x=0"],"answer":"C","explanation":"x²=25."},

{"question":"Giải bất phương trình: 5x-15>0","options":["A. x>3","B. x<3","C. x≥3","D. x≤3"],"answer":"A","explanation":"5x>15."},
{"question":"Giải phương trình: x² - 11x + 30 = 0","options":["A. x=5;6","B. x=3;10","C. x=2;15","D. x=-5;-6"],"answer":"A","explanation":"(x-5)(x-6)=0."},
{"question":"Cho Δ<0, phương trình bậc hai","options":["A. Có 2 nghiệm","B. Có 1 nghiệm","C. Vô nghiệm","D. 3 nghiệm"],"answer":"C","explanation":"Δ<0."},
{"question":"Giải hệ: 4x+y=13; x+y=4","options":["A. x=3,y=1","B. x=2,y=2","C. x=1,y=3","D. x=4,y=0"],"answer":"A","explanation":"Trừ hai phương trình."},
{"question":"Chu vi hình tròn bán kính 12","options":["A. 12π","B. 24π","C. 48π","D. 144π"],"answer":"B","explanation":"2πr."},

{"question":"Giải phương trình: x² - 6x + 9 = 0","options":["A. x=3 kép","B. x=-3 kép","C. x=±3","D. 2 nghiệm"],"answer":"A","explanation":"(x-3)²=0."},
{"question":"Giải hệ: 2x+3y=12; x+y=5","options":["A. x=3,y=2","B. x=2,y=3","C. x=4,y=1","D. x=1,y=4"],"answer":"A","explanation":"Thế x=5-y."},
{"question":"Giải bất phương trình: 6x+12≤0","options":["A. x≤-2","B. x≥-2","C. x<-2","D. x>-2"],"answer":"A","explanation":"6x≤-12."},
{"question":"Giải phương trình: x² + 9x + 20 = 0","options":["A. x=-4;-5","B. x=4;5","C. x=-2;-10","D. x=2;10"],"answer":"A","explanation":"(x+4)(x+5)=0."},
{"question":"Cho tam giác vuông có cạnh góc vuông 5 và 12. Cạnh huyền?","options":["A. 12","B. 13","C. 14","D. 15"],"answer":"B","explanation":"5²+12²=13²."},

{"question":"Tính diện tích hình tròn bán kính 8","options":["A. 16π","B. 32π","C. 64π","D. 8π"],"answer":"C","explanation":"πr²."},
{"question":"Giải phương trình: x² - 3x - 18 = 0","options":["A. x=6;-3","B. x=3;-6","C. x=9;-2","D. x=2;-9"],"answer":"A","explanation":"(x-6)(x+3)=0."},
{"question":"Giải hệ: x+y=6; 2x-y=3","options":["A. x=3,y=3","B. x=2,y=4","C. x=4,y=2","D. x=1,y=5"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: 7x-14≥0","options":["A. x≥2","B. x≤2","C. x>2","D. x<2"],"answer":"A","explanation":"7x≥14."},
{"question":"Chu vi hình tròn bán kính 4","options":["A. 4π","B. 8π","C. 16π","D. 2π"],"answer":"B","explanation":"2πr."},

{"question":"Giải phương trình: x² - 13x + 36 = 0","options":["A. x=4;9","B. x=6;6","C. x=3;12","D. x=-4;-9"],"answer":"A","explanation":"(x-4)(x-9)=0."},
{"question":"Giải hệ: 5x+y=16; x+y=6","options":["A. x=2,y=4","B. x=3,y=3","C. x=4,y=2","D. x=1,y=5"],"answer":"A","explanation":"Trừ hai phương trình."},
{"question":"Giải bất phương trình: -3x≥9","options":["A. x≤-3","B. x≥-3","C. x≤3","D. x≥3"],"answer":"A","explanation":"Chia số âm đổi chiều."},
{"question":"Giải phương trình: x² + 4x - 12 = 0","options":["A. x=2;-6","B. x=6;-2","C. x=3;-4","D. x=4;-3"],"answer":"A","explanation":"(x+6)(x-2)=0."},
{"question":"Cho tam giác vuông có cạnh góc vuông 7 và 24. Cạnh huyền?","options":["A. 24","B. 25","C. 26","D. 27"],"answer":"B","explanation":"7²+24²=25²."},
{"question":"Giải phương trình: x² - 12x + 35 = 0","options":["A. x=5;7","B. x=3;9","C. x=1;35","D. x=-5;-7"],"answer":"A","explanation":"(x-5)(x-7)=0."},
{"question":"Giải hệ: x+y=7; 2x-y=4","options":["A. x=3,y=4","B. x=4,y=3","C. x=2,y=5","D. x=5,y=2"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: 4x-8>0","options":["A. x>2","B. x<2","C. x≥2","D. x≤2"],"answer":"A","explanation":"4x>8."},
{"question":"Tổng hai nghiệm của x² - 9x + 20 = 0","options":["A. 9","B. 20","C. -9","D. -20"],"answer":"A","explanation":"S=-b/a=9."},
{"question":"Tích hai nghiệm của x² - 9x + 20 = 0","options":["A. 9","B. 20","C. -20","D. -9"],"answer":"B","explanation":"P=c/a=20."},

{"question":"Giải phương trình: x² - 36 = 0","options":["A. x=6","B. x=-6","C. x=±6","D. x=0"],"answer":"C","explanation":"x²=36."},
{"question":"Rút gọn: (x²-25)/(x-5) (x≠5)","options":["A. x-5","B. x+5","C. x²-5","D. 5"],"answer":"B","explanation":"x²-25=(x-5)(x+5)."},
{"question":"Cho tam giác vuông có cạnh góc vuông 15 và 20. Cạnh huyền?","options":["A. 24","B. 25","C. 26","D. 27"],"answer":"B","explanation":"15²+20²=25²."},
{"question":"Tính diện tích hình tròn bán kính 6","options":["A. 12π","B. 36π","C. 6π","D. 18π"],"answer":"B","explanation":"πr²."},
{"question":"Giải phương trình: x² + 3x - 28 = 0","options":["A. x=4;-7","B. x=7;-4","C. x=2;-14","D. x=14;-2"],"answer":"A","explanation":"(x+7)(x-4)=0."},

{"question":"Giải hệ: 3x+y=10; x+y=4","options":["A. x=3,y=1","B. x=2,y=2","C. x=1,y=3","D. x=4,y=0"],"answer":"A","explanation":"Trừ hai phương trình."},
{"question":"Giải bất phương trình: 5x+15≤0","options":["A. x≤-3","B. x≥-3","C. x<-3","D. x>-3"],"answer":"A","explanation":"5x≤-15."},
{"question":"Cho Δ=25, phương trình bậc hai có","options":["A. 2 nghiệm phân biệt","B. 1 nghiệm kép","C. Vô nghiệm","D. 3 nghiệm"],"answer":"A","explanation":"Δ>0."},
{"question":"Giải phương trình: x² - 20x = 0","options":["A. x=0;20","B. x=20","C. x=0","D. x=-20"],"answer":"A","explanation":"x(x-20)=0."},
{"question":"Chu vi hình tròn bán kính 9","options":["A. 9π","B. 18π","C. 81π","D. 27π"],"answer":"B","explanation":"2πr."},

{"question":"Giải phương trình: x² - 15x + 56 = 0","options":["A. x=7;8","B. x=6;9","C. x=5;11","D. x=-7;-8"],"answer":"A","explanation":"(x-7)(x-8)=0."},
{"question":"Giải hệ: 2x+y=11; x-y=1","options":["A. x=4,y=3","B. x=3,y=4","C. x=5,y=1","D. x=2,y=5"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Giải bất phương trình: -4x≥8","options":["A. x≤-2","B. x≥-2","C. x≤2","D. x≥2"],"answer":"A","explanation":"Chia số âm đổi chiều."},
{"question":"Tổng hai nghiệm của x² - 6x + 8 = 0","options":["A. 6","B. 8","C. -6","D. -8"],"answer":"A","explanation":"S=-b/a=6."},
{"question":"Tích hai nghiệm của x² - 6x + 8 = 0","options":["A. 6","B. 8","C. -8","D. -6"],"answer":"B","explanation":"P=c/a=8."},

{"question":"Cho tam giác vuông có cạnh góc vuông 8 và 15. Cạnh huyền?","options":["A. 16","B. 17","C. 18","D. 19"],"answer":"B","explanation":"8²+15²=17²."},
{"question":"Giải phương trình: x² + 10x + 21 = 0","options":["A. x=-3;-7","B. x=3;7","C. x=-1;-21","D. x=1;21"],"answer":"A","explanation":"(x+3)(x+7)=0."},
{"question":"Giải hệ: x+y=8; 3x-y=4","options":["A. x=3,y=5","B. x=2,y=6","C. x=4,y=4","D. x=5,y=3"],"answer":"A","explanation":"Cộng hai phương trình."},
{"question":"Diện tích hình tròn bán kính 12","options":["A. 24π","B. 144π","C. 12π","D. 72π"],"answer":"B","explanation":"πr²."},
{"question":"Giải phương trình: x² - 49 = 0","options":["A. x=7","B. x=-7","C. x=±7","D. x=0"],"answer":"C","explanation":"x²=49."},

{"question":"Giải bất phương trình: 6x-18>0","options":["A. x>3","B. x<3","C. x≥3","D. x≤3"],"answer":"A","explanation":"6x>18."},
{"question":"Giải phương trình: x² - 17x + 72 = 0","options":["A. x=8;9","B. x=6;12","C. x=7;10","D. x=-8;-9"],"answer":"A","explanation":"(x-8)(x-9)=0."},
{"question":"Cho Δ<0, phương trình bậc hai","options":["A. Có 2 nghiệm","B. Có 1 nghiệm","C. Vô nghiệm","D. 3 nghiệm"],"answer":"C","explanation":"Δ<0."},
{"question":"Giải hệ: 4x+y=17; x+y=5","options":["A. x=4,y=1","B. x=3,y=2","C. x=2,y=3","D. x=5,y=0"],"answer":"A","explanation":"Trừ hai phương trình."},
{"question":"Chu vi hình tròn bán kính 15","options":["A. 15π","B. 30π","C. 60π","D. 225π"],"answer":"B","explanation":"2πr."},

{"question":"Giải phương trình: x² - 18x + 81 = 0","options":["A. x=9 kép","B. x=-9 kép","C. x=±9","D. 2 nghiệm"],"answer":"A","explanation":"(x-9)²=0."},
{"question":"Giải hệ: 3x+2y=12; x+y=5","options":["A. x=2,y=3","B. x=3,y=2","C. x=4,y=1","D. x=1,y=4"],"answer":"A","explanation":"Thế x=5-y."},
{"question":"Giải bất phương trình: 7x+14≤0","options":["A. x≤-2","B. x≥-2","C. x<-2","D. x>-2"],"answer":"A","explanation":"7x≤-14."},
{"question":"Giải phương trình: x² + 5x - 24 = 0","options":["A. x=3;-8","B. x=8;-3","C. x=6;-4","D. x=4;-6"],"answer":"A","explanation":"(x+8)(x-3)=0."},
{"question":"Cho tam giác vuông có cạnh góc vuông 9 và 40. Cạnh huyền?","options":["A. 41","B. 42","C. 43","D. 44"],"answer":"A","explanation":"9²+40²=41²."},
{
    "question": "Giải bất phương trình: 7x + 17 ≥ 52",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+1y=0; 2x+1y=2",
    "options": [
      "A. x=-2,y=6",
      "B. x=6,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (4)x + (-140) = 0",
    "options": [
      "A. x=-14;10",
      "B. x=10;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+2y=-10; 5x+5y=-25",
    "options": [
      "A. x=-4,y=-1",
      "B. x=-1,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+5y=-41; 1x+3y=-23",
    "options": [
      "A. x=4,y=-9",
      "B. x=-9,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (14)x + (24) = 0",
    "options": [
      "A. x=-12;-2",
      "B. x=-2;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-240) = 0",
    "options": [
      "A. x=20;-12",
      "B. x=-12;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+4y=14; 2x+3y=8",
    "options": [
      "A. x=10,y=-4",
      "B. x=-4,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-65) = 0",
    "options": [
      "A. x=13;-5",
      "B. x=-5;13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + -4 ≥ -4",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+1y=3; 2x+4y=10",
    "options": [
      "A. x=1,y=2",
      "B. x=2,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + 7 ≥ -49",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 4x + -3 ≥ -39",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + 10 ≥ 19",
    "options": [
      "A. x ≥ 1",
      "B. x ≤ 1",
      "C. x > 1",
      "D. x < 1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-5)x + (-6) = 0",
    "options": [
      "A. x=-1;6",
      "B. x=6;-1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+4y=20; 4x+4y=20",
    "options": [
      "A. x=6,y=-1",
      "B. x=-1,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-2)x + (-80) = 0",
    "options": [
      "A. x=-8;10",
      "B. x=10;-8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-3)x + (-70) = 0",
    "options": [
      "A. x=-7;10",
      "B. x=10;-7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (1)x + (-210) = 0",
    "options": [
      "A. x=14;-15",
      "B. x=-15;14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + 11 ≥ 27",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + -7 ≥ 28",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + -14 ≥ 16",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+3y=23; 3x+1y=3",
    "options": [
      "A. x=-2,y=9",
      "B. x=9,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + 2 ≥ -19",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-18)x + (-19) = 0",
    "options": [
      "A. x=19;-1",
      "B. x=-1;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (2)x + (-35) = 0",
    "options": [
      "A. x=-7;5",
      "B. x=5;-7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (12)x + (20) = 0",
    "options": [
      "A. x=-10;-2",
      "B. x=-2;-10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 2x + -5 ≥ -11",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (3)x + (-270) = 0",
    "options": [
      "A. x=15;-18",
      "B. x=-18;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + -8 ≥ -28",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 2x + -13 ≥ 3",
    "options": [
      "A. x ≥ 8",
      "B. x ≤ 8",
      "C. x > 8",
      "D. x < 8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + 10 ≥ -30",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 8x + 18 ≥ 10",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 2x + 18 ≥ 34",
    "options": [
      "A. x ≥ 8",
      "B. x ≤ 8",
      "C. x > 8",
      "D. x < 8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 8x + -4 ≥ -60",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + 1 ≥ -44",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + -11 ≥ 7",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+5y=31; 3x+4y=27",
    "options": [
      "A. x=1,y=6",
      "B. x=6,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-55) = 0",
    "options": [
      "A. x=11;-5",
      "B. x=-5;11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 10x + -15 ≥ -95",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 4x + 8 ≥ 44",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+5y=-12; 4x+3y=6",
    "options": [
      "A. x=6,y=-6",
      "B. x=-6,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + -5 ≥ -68",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + 16 ≥ 41",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 6x + -14 ≥ -20",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (12)x + (-108) = 0",
    "options": [
      "A. x=6;-18",
      "B. x=-18;6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+1y=0; 1x+1y=4",
    "options": [
      "A. x=-1,y=5",
      "B. x=5,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+1y=7; 1x+2y=-10",
    "options": [
      "A. x=8,y=-9",
      "B. x=-9,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+3y=-18; 1x+5y=-16",
    "options": [
      "A. x=-6,y=-2",
      "B. x=-2,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+5y=28; 3x+2y=4",
    "options": [
      "A. x=-4,y=8",
      "B. x=8,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (19)x + (70) = 0",
    "options": [
      "A. x=-5;-14",
      "B. x=-14;-5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+1y=20; 4x+3y=30",
    "options": [
      "A. x=6,y=2",
      "B. x=2,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 4x + 17 ≥ 17",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (22)x + (40) = 0",
    "options": [
      "A. x=-2;-20",
      "B. x=-20;-2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-247) = 0",
    "options": [
      "A. x=19;-13",
      "B. x=-13;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + -19 ≥ 21",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (13)x + (-140) = 0",
    "options": [
      "A. x=7;-20",
      "B. x=-20;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + 16 ≥ 58",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=-9; 1x+1y=-3",
    "options": [
      "A. x=0,y=-3",
      "B. x=-3,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-29)x + (210) = 0",
    "options": [
      "A. x=15;14",
      "B. x=14;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + 19 ≥ 16",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-32)x + (240) = 0",
    "options": [
      "A. x=20;12",
      "B. x=12;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + -8 ≥ -13",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+3y=-39; 5x+2y=-38",
    "options": [
      "A. x=-4,y=-9",
      "B. x=-9,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-12)x + (-28) = 0",
    "options": [
      "A. x=-2;14",
      "B. x=14;-2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-48) = 0",
    "options": [
      "A. x=12;-4",
      "B. x=-4;12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 2x + -18 ≥ -38",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+2y=-3; 4x+3y=-27",
    "options": [
      "A. x=-9,y=3",
      "B. x=3,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-11)x + (-60) = 0",
    "options": [
      "A. x=-4;15",
      "B. x=15;-4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+3y=-28; 1x+3y=-20",
    "options": [
      "A. x=-8,y=-4",
      "B. x=-4,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+1y=-19; 1x+5y=-39",
    "options": [
      "A. x=-4,y=-7",
      "B. x=-7,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+4y=58; 1x+5y=41",
    "options": [
      "A. x=6,y=7",
      "B. x=7,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+4y=11; 1x+4y=11",
    "options": [
      "A. x=-5,y=4",
      "B. x=4,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+1y=-20; 4x+1y=-50",
    "options": [
      "A. x=-10,y=-10",
      "B. x=-10,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+3y=26; 2x+3y=28",
    "options": [
      "A. x=2,y=8",
      "B. x=8,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+1y=-8; 2x+4y=18",
    "options": [
      "A. x=-5,y=7",
      "B. x=7,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+4y=31; 3x+4y=31",
    "options": [
      "A. x=-3,y=10",
      "B. x=10,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-5)x + (0) = 0",
    "options": [
      "A. x=5;0",
      "B. x=0;5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-11)x + (-26) = 0",
    "options": [
      "A. x=13;-2",
      "B. x=-2;13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+4y=-26; 5x+4y=-29",
    "options": [
      "A. x=-1,y=-6",
      "B. x=-6,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-22)x + (112) = 0",
    "options": [
      "A. x=14;8",
      "B. x=8;14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (14)x + (-95) = 0",
    "options": [
      "A. x=5;-19",
      "B. x=-19;5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + -11 ≥ -39",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 7x + 18 ≥ -31",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+4y=-8; 3x+5y=10",
    "options": [
      "A. x=-10,y=8",
      "B. x=8,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+5y=-30; 2x+1y=-6",
    "options": [
      "A. x=0,y=-6",
      "B. x=-6,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+1y=35; 3x+5y=56",
    "options": [
      "A. x=7,y=7",
      "B. x=7,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 10x + 13 ≥ 43",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+2y=-28; 4x+4y=-76",
    "options": [
      "A. x=-10,y=-9",
      "B. x=-9,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (2)x + (-360) = 0",
    "options": [
      "A. x=18;-20",
      "B. x=-20;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+2y=16; 1x+3y=4",
    "options": [
      "A. x=10,y=-2",
      "B. x=-2,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+1y=31; 2x+5y=25",
    "options": [
      "A. x=10,y=1",
      "B. x=1,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+5y=55; 2x+1y=17",
    "options": [
      "A. x=5,y=7",
      "B. x=7,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (12)x + (32) = 0",
    "options": [
      "A. x=-8;-4",
      "B. x=-4;-8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + 16 ≥ -4",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-112) = 0",
    "options": [
      "A. x=-8;14",
      "B. x=14;-8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+4y=17; 2x+5y=22",
    "options": [
      "A. x=1,y=4",
      "B. x=4,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+1y=32; 1x+4y=38",
    "options": [
      "A. x=6,y=8",
      "B. x=8,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + 9 ≥ 21",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 2x + 14 ≥ 26",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-216) = 0",
    "options": [
      "A. x=18;-12",
      "B. x=-12;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+5y=-27; 1x+4y=-30",
    "options": [
      "A. x=6,y=-9",
      "B. x=-9,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-9)x + (-112) = 0",
    "options": [
      "A. x=-7;16",
      "B. x=16;-7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (26)x + (169) = 0",
    "options": [
      "A. x=-13;-13",
      "B. x=-13;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-7)x + (0) = 0",
    "options": [
      "A. x=0;7",
      "B. x=7;0",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (2)x + (-15) = 0",
    "options": [
      "A. x=-5;3",
      "B. x=3;-5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + -1 ≥ 11",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + -16 ≥ -11",
    "options": [
      "A. x ≥ 1",
      "B. x ≤ 1",
      "C. x > 1",
      "D. x < 1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-1)x + (-42) = 0",
    "options": [
      "A. x=7;-6",
      "B. x=-6;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 10x + 2 ≥ 2",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + 19 ≥ 18",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 8x + -6 ≥ 66",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + -2 ≥ -17",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 7x + -5 ≥ 51",
    "options": [
      "A. x ≥ 8",
      "B. x ≤ 8",
      "C. x > 8",
      "D. x < 8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 4x + 20 ≥ 16",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-15)x + (50) = 0",
    "options": [
      "A. x=10;5",
      "B. x=5;10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+3y=-38; 5x+5y=-80",
    "options": [
      "A. x=-10,y=-6",
      "B. x=-6,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (9)x + (8) = 0",
    "options": [
      "A. x=-1;-8",
      "B. x=-8;-1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+3y=36; 3x+3y=36",
    "options": [
      "A. x=7,y=5",
      "B. x=5,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + 12 ≥ -23",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+3y=-67; 4x+1y=-41",
    "options": [
      "A. x=-8,y=-9",
      "B. x=-9,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + 20 ≥ -7",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+3y=-27; 2x+4y=-22",
    "options": [
      "A. x=-3,y=-4",
      "B. x=-4,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (13)x + (-90) = 0",
    "options": [
      "A. x=5;-18",
      "B. x=-18;5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (24)x + (108) = 0",
    "options": [
      "A. x=-18;-6",
      "B. x=-6;-18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 10x + 12 ≥ 22",
    "options": [
      "A. x ≥ 1",
      "B. x ≤ 1",
      "C. x > 1",
      "D. x < 1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (2)x + (0) = 0",
    "options": [
      "A. x=-2;0",
      "B. x=0;-2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + 6 ≥ 26",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+4y=-18; 3x+1y=18",
    "options": [
      "A. x=9,y=-9",
      "B. x=-9,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + 19 ≥ 37",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-14)x + (-120) = 0",
    "options": [
      "A. x=20;-6",
      "B. x=-6;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+1y=-5; 5x+4y=1",
    "options": [
      "A. x=-3,y=4",
      "B. x=4,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + 8 ≥ 38",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (16)x + (-80) = 0",
    "options": [
      "A. x=-20;4",
      "B. x=4;-20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 8x + -15 ≥ 25",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (32)x + (247) = 0",
    "options": [
      "A. x=-13;-19",
      "B. x=-19;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+5y=24; 1x+1y=9",
    "options": [
      "A. x=7,y=2",
      "B. x=2,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+1y=1; 4x+1y=7",
    "options": [
      "A. x=2,y=-1",
      "B. x=-1,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (5)x + (-36) = 0",
    "options": [
      "A. x=4;-9",
      "B. x=-9;4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+5y=-17; 3x+5y=-17",
    "options": [
      "A. x=-9,y=2",
      "B. x=2,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+3y=12; 1x+2y=8",
    "options": [
      "A. x=0,y=4",
      "B. x=4,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+3y=36; 1x+1y=12",
    "options": [
      "A. x=10,y=2",
      "B. x=2,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (21)x + (98) = 0",
    "options": [
      "A. x=-14;-7",
      "B. x=-7;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (19)x + (84) = 0",
    "options": [
      "A. x=-12;-7",
      "B. x=-7;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + 4 ≥ 4",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 7x + 16 ≥ 65",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + 19 ≥ 19",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (0)x + (-81) = 0",
    "options": [
      "A. x=-9;9",
      "B. x=9;-9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+4y=60; 1x+4y=28",
    "options": [
      "A. x=8,y=5",
      "B. x=5,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-15)x + (-34) = 0",
    "options": [
      "A. x=17;-2",
      "B. x=-2;17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + 10 ≥ 52",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+2y=0; 1x+5y=-36",
    "options": [
      "A. x=4,y=-8",
      "B. x=-8,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+3y=-13; 1x+2y=3",
    "options": [
      "A. x=-7,y=5",
      "B. x=5,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 6x + -14 ≥ 4",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-18)x + (-19) = 0",
    "options": [
      "A. x=19;-1",
      "B. x=-1;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+3y=26; 4x+3y=28",
    "options": [
      "A. x=1,y=8",
      "B. x=8,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+5y=13; 4x+5y=19",
    "options": [
      "A. x=6,y=-1",
      "B. x=-1,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+3y=36; 3x+5y=27",
    "options": [
      "A. x=9,y=0",
      "B. x=0,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-17)x + (70) = 0",
    "options": [
      "A. x=7;10",
      "B. x=10;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 10x + -12 ≥ 38",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+2y=9; 2x+4y=-6",
    "options": [
      "A. x=3,y=-3",
      "B. x=-3,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-2)x + (-120) = 0",
    "options": [
      "A. x=12;-10",
      "B. x=-10;12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+2y=-8; 2x+2y=-18",
    "options": [
      "A. x=-10,y=1",
      "B. x=1,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + 20 ≥ -34",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (23)x + (130) = 0",
    "options": [
      "A. x=-10;-13",
      "B. x=-13;-10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 2x + 19 ≥ 27",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (4)x + (-117) = 0",
    "options": [
      "A. x=-13;9",
      "B. x=9;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+2y=14; 2x+4y=28",
    "options": [
      "A. x=-6,y=10",
      "B. x=10,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + 9 ≥ 72",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (8)x + (-209) = 0",
    "options": [
      "A. x=-19;11",
      "B. x=11;-19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-105) = 0",
    "options": [
      "A. x=15;-7",
      "B. x=-7;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+5y=21; 4x+3y=16",
    "options": [
      "A. x=1,y=4",
      "B. x=4,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-1)x + (-12) = 0",
    "options": [
      "A. x=4;-3",
      "B. x=-3;4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+2y=-6; 5x+4y=12",
    "options": [
      "A. x=8,y=-7",
      "B. x=-7,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-15)x + (56) = 0",
    "options": [
      "A. x=7;8",
      "B. x=8;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-5)x + (-150) = 0",
    "options": [
      "A. x=-10;15",
      "B. x=15;-10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-112) = 0",
    "options": [
      "A. x=-8;14",
      "B. x=14;-8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+1y=-2; 3x+4y=-34",
    "options": [
      "A. x=2,y=-10",
      "B. x=-10,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+4y=2; 3x+5y=7",
    "options": [
      "A. x=-6,y=5",
      "B. x=5,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-10)x + (-24) = 0",
    "options": [
      "A. x=12;-2",
      "B. x=-2;12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+2y=28; 1x+5y=34",
    "options": [
      "A. x=4,y=6",
      "B. x=6,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+3y=28; 1x+5y=42",
    "options": [
      "A. x=7,y=7",
      "B. x=7,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (0)x + (-256) = 0",
    "options": [
      "A. x=-16;16",
      "B. x=16;-16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+2y=5; 5x+3y=5",
    "options": [
      "A. x=-5,y=10",
      "B. x=10,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+3y=39; 5x+4y=49",
    "options": [
      "A. x=9,y=1",
      "B. x=1,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-112) = 0",
    "options": [
      "A. x=14;-8",
      "B. x=-8;14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + 7 ≥ -47",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 2x + -16 ≥ -36",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-4)x + (-45) = 0",
    "options": [
      "A. x=9;-5",
      "B. x=-5;9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+4y=-52; 5x+2y=-58",
    "options": [
      "A. x=-8,y=-9",
      "B. x=-9,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+2y=-50; 4x+2y=-44",
    "options": [
      "A. x=-6,y=-10",
      "B. x=-10,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (5)x + (-126) = 0",
    "options": [
      "A. x=9;-14",
      "B. x=-14;9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + -5 ≥ -30",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+1y=-3; 2x+1y=-3",
    "options": [
      "A. x=-2,y=1",
      "B. x=1,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-7)x + (12) = 0",
    "options": [
      "A. x=4;3",
      "B. x=3;4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-35)x + (304) = 0",
    "options": [
      "A. x=19;16",
      "B. x=16;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + -14 ≥ -39",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+1y=8; 5x+5y=0",
    "options": [
      "A. x=8,y=-8",
      "B. x=-8,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+1y=-24; 4x+3y=-40",
    "options": [
      "A. x=-4,y=-8",
      "B. x=-8,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-7)x + (-170) = 0",
    "options": [
      "A. x=-10;17",
      "B. x=17;-10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-35)x + (300) = 0",
    "options": [
      "A. x=15;20",
      "B. x=20;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-17)x + (-18) = 0",
    "options": [
      "A. x=-1;18",
      "B. x=18;-1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+4y=67; 5x+2y=51",
    "options": [
      "A. x=7,y=8",
      "B. x=8,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 10x + -9 ≥ 41",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+1y=9; 2x+2y=0",
    "options": [
      "A. x=9,y=-9",
      "B. x=-9,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + 14 ≥ -4",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+2y=-32; 5x+1y=-30",
    "options": [
      "A. x=-4,y=-10",
      "B. x=-10,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+4y=44; 3x+2y=28",
    "options": [
      "A. x=6,y=5",
      "B. x=5,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 5x + 14 ≥ 44",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (5)x + (0) = 0",
    "options": [
      "A. x=0;-5",
      "B. x=-5;0",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + 13 ≥ 25",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + 3 ≥ -22",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + 11 ≥ 16",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+5y=-1; 1x+5y=26",
    "options": [
      "A. x=-9,y=7",
      "B. x=7,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 4x + 3 ≥ -5",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+1y=34; 4x+2y=36",
    "options": [
      "A. x=8,y=2",
      "B. x=2,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-9)x + (-162) = 0",
    "options": [
      "A. x=18;-9",
      "B. x=-9;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (7)x + (0) = 0",
    "options": [
      "A. x=0;-7",
      "B. x=-7;0",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-28)x + (160) = 0",
    "options": [
      "A. x=20;8",
      "B. x=8;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+1y=-33; 2x+4y=-42",
    "options": [
      "A. x=-5,y=-8",
      "B. x=-8,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (2)x + (-120) = 0",
    "options": [
      "A. x=-12;10",
      "B. x=10;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+2y=4; 3x+4y=4",
    "options": [
      "A. x=4,y=-2",
      "B. x=-2,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+1y=-14; 2x+3y=-12",
    "options": [
      "A. x=-3,y=-2",
      "B. x=-2,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-24)x + (108) = 0",
    "options": [
      "A. x=18;6",
      "B. x=6;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 8x + 18 ≥ 98",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-14)x + (-51) = 0",
    "options": [
      "A. x=17;-3",
      "B. x=-3;17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-4)x + (-221) = 0",
    "options": [
      "A. x=17;-13",
      "B. x=-13;17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (5)x + (4) = 0",
    "options": [
      "A. x=-4;-1",
      "B. x=-1;-4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 6x + 18 ≥ 60",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+2y=-3; 4x+2y=18",
    "options": [
      "A. x=7,y=-5",
      "B. x=-5,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-16)x + (-36) = 0",
    "options": [
      "A. x=-2;18",
      "B. x=18;-2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+2y=-8; 4x+4y=0",
    "options": [
      "A. x=8,y=-8",
      "B. x=-8,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + 0 ≥ -15",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+4y=-23; 2x+5y=-28",
    "options": [
      "A. x=1,y=-6",
      "B. x=-6,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + 0 ≥ -1",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 8x + -7 ≥ 1",
    "options": [
      "A. x ≥ 1",
      "B. x ≤ 1",
      "C. x > 1",
      "D. x < 1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 4x + 11 ≥ 7",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+4y=-28; 3x+4y=-24",
    "options": [
      "A. x=-4,y=-3",
      "B. x=-3,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 10x + -4 ≥ -104",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=-48; 4x+5y=-64",
    "options": [
      "A. x=-6,y=-8",
      "B. x=-8,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (7)x + (10) = 0",
    "options": [
      "A. x=-2;-5",
      "B. x=-5;-2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + -13 ≥ -21",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+5y=37; 1x+1y=1",
    "options": [
      "A. x=-8,y=9",
      "B. x=9,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + -5 ≥ -59",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (9)x + (-136) = 0",
    "options": [
      "A. x=8;-17",
      "B. x=-17;8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + 10 ≥ -8",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-14)x + (33) = 0",
    "options": [
      "A. x=11;3",
      "B. x=3;11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + 12 ≥ -18",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 6x + -5 ≥ 13",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+5y=26; 3x+3y=12",
    "options": [
      "A. x=-6,y=10",
      "B. x=10,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+4y=-10; 3x+3y=-12",
    "options": [
      "A. x=6,y=-10",
      "B. x=-10,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + 20 ≥ 10",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+2y=11; 2x+3y=9",
    "options": [
      "A. x=3,y=1",
      "B. x=1,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + 1 ≥ 55",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-16)x + (28) = 0",
    "options": [
      "A. x=14;2",
      "B. x=2;14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-160) = 0",
    "options": [
      "A. x=16;-10",
      "B. x=-10;16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+2y=-15; 2x+3y=-10",
    "options": [
      "A. x=-5,y=0",
      "B. x=0,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (1)x + (-90) = 0",
    "options": [
      "A. x=9;-10",
      "B. x=-10;9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + 2 ≥ 2",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-36)x + (320) = 0",
    "options": [
      "A. x=16;20",
      "B. x=20;16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + -19 ≥ 21",
    "options": [
      "A. x ≥ 8",
      "B. x ≤ 8",
      "C. x > 8",
      "D. x < 8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-12)x + (11) = 0",
    "options": [
      "A. x=11;1",
      "B. x=1;11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + -5 ≥ 5",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (3)x + (-270) = 0",
    "options": [
      "A. x=-18;15",
      "B. x=15;-18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (4)x + (0) = 0",
    "options": [
      "A. x=-4;0",
      "B. x=0;-4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+2y=-26; 3x+3y=-39",
    "options": [
      "A. x=-7,y=-6",
      "B. x=-6,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+2y=14; 4x+1y=19",
    "options": [
      "A. x=4,y=3",
      "B. x=3,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (29)x + (190) = 0",
    "options": [
      "A. x=-19;-10",
      "B. x=-10;-19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-13)x + (40) = 0",
    "options": [
      "A. x=8;5",
      "B. x=5;8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 6x + 11 ≥ -37",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+4y=20; 1x+3y=15",
    "options": [
      "A. x=0,y=5",
      "B. x=5,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + -8 ≥ -24",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 11 ≥ -49",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+2y=-35; 2x+4y=-42",
    "options": [
      "A. x=-7,y=-7",
      "B. x=-7,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 6x + -15 ≥ -3",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 2x + 17 ≥ 29",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=-37; 2x+1y=-17",
    "options": [
      "A. x=-7,y=-3",
      "B. x=-3,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-4)x + (-60) = 0",
    "options": [
      "A. x=10;-6",
      "B. x=-6;10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (27)x + (170) = 0",
    "options": [
      "A. x=-10;-17",
      "B. x=-17;-10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + -6 ≥ -11",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-15)x + (-76) = 0",
    "options": [
      "A. x=19;-4",
      "B. x=-4;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+3y=25; 3x+4y=25",
    "options": [
      "A. x=-5,y=10",
      "B. x=10,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + -8 ≥ -62",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (2)x + (-224) = 0",
    "options": [
      "A. x=14;-16",
      "B. x=-16;14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + -13 ≥ 14",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 6x + 13 ≥ -35",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + -16 ≥ -106",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 4x + -5 ≥ -45",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+3y=-18; 4x+2y=-16",
    "options": [
      "A. x=-6,y=4",
      "B. x=4,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+2y=-3; 1x+1y=-1",
    "options": [
      "A. x=-1,y=0",
      "B. x=0,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + -18 ≥ -13",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+4y=32; 2x+4y=32",
    "options": [
      "A. x=8,y=4",
      "B. x=4,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+1y=-6; 5x+5y=0",
    "options": [
      "A. x=-2,y=2",
      "B. x=2,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + -1 ≥ -11",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 8 ≥ 98",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 7 ≥ -83",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + -16 ≥ -14",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + -14 ≥ -6",
    "options": [
      "A. x ≥ 8",
      "B. x ≤ 8",
      "C. x > 8",
      "D. x < 8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 8x + 13 ≥ 53",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+1y=-44; 4x+2y=-48",
    "options": [
      "A. x=-10,y=-4",
      "B. x=-4,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-33)x + (272) = 0",
    "options": [
      "A. x=17;16",
      "B. x=16;17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + 5 ≥ 75",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+2y=-4; 5x+5y=-25",
    "options": [
      "A. x=-6,y=1",
      "B. x=1,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+5y=9; 1x+1y=0",
    "options": [
      "A. x=-9,y=9",
      "B. x=9,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (12)x + (0) = 0",
    "options": [
      "A. x=-12;0",
      "B. x=0;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+2y=30; 2x+1y=13",
    "options": [
      "A. x=4,y=5",
      "B. x=5,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-4)x + (-5) = 0",
    "options": [
      "A. x=5;-1",
      "B. x=-1;5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+3y=-32; 5x+2y=-43",
    "options": [
      "A. x=-5,y=-9",
      "B. x=-9,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+1y=4; 5x+3y=19",
    "options": [
      "A. x=-1,y=8",
      "B. x=8,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + -18 ≥ -3",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (8)x + (-209) = 0",
    "options": [
      "A. x=11;-19",
      "B. x=-19;11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (7)x + (6) = 0",
    "options": [
      "A. x=-1;-6",
      "B. x=-6;-1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-3)x + (-28) = 0",
    "options": [
      "A. x=-4;7",
      "B. x=7;-4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + -19 ≥ -19",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-216) = 0",
    "options": [
      "A. x=-12;18",
      "B. x=18;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + 0 ≥ 0",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-33)x + (270) = 0",
    "options": [
      "A. x=18;15",
      "B. x=15;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + -20 ≥ -18",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (23)x + (76) = 0",
    "options": [
      "A. x=-4;-19",
      "B. x=-19;-4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (1)x + (-30) = 0",
    "options": [
      "A. x=-6;5",
      "B. x=5;-6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-3)x + (-238) = 0",
    "options": [
      "A. x=-14;17",
      "B. x=17;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (7)x + (0) = 0",
    "options": [
      "A. x=-7;0",
      "B. x=0;-7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 10x + 4 ≥ 34",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (21)x + (80) = 0",
    "options": [
      "A. x=-5;-16",
      "B. x=-16;-5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+4y=-44; 2x+2y=-22",
    "options": [
      "A. x=-8,y=-3",
      "B. x=-3,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (14)x + (13) = 0",
    "options": [
      "A. x=-13;-1",
      "B. x=-1;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+2y=28; 3x+1y=16",
    "options": [
      "A. x=4,y=4",
      "B. x=4,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (21)x + (68) = 0",
    "options": [
      "A. x=-17;-4",
      "B. x=-4;-17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+1y=-4; 5x+2y=-20",
    "options": [
      "A. x=-4,y=0",
      "B. x=0,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+1y=-13; 5x+3y=-32",
    "options": [
      "A. x=-1,y=-9",
      "B. x=-9,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 5x + -8 ≥ 12",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-23)x + (112) = 0",
    "options": [
      "A. x=7;16",
      "B. x=16;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + -18 ≥ -6",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + -3 ≥ 47",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + 18 ≥ -3",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + -12 ≥ -3",
    "options": [
      "A. x ≥ 1",
      "B. x ≤ 1",
      "C. x > 1",
      "D. x < 1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + 15 ≥ -25",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 7x + 15 ≥ 36",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (16)x + (48) = 0",
    "options": [
      "A. x=-4;-12",
      "B. x=-12;-4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+1y=6; 2x+4y=30",
    "options": [
      "A. x=-3,y=9",
      "B. x=9,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-32)x + (256) = 0",
    "options": [
      "A. x=16;16",
      "B. x=16;16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (5)x + (-24) = 0",
    "options": [
      "A. x=3;-8",
      "B. x=-8;3",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + 8 ≥ -27",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + 5 ≥ 1",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+2y=-4; 4x+2y=-10",
    "options": [
      "A. x=-6,y=7",
      "B. x=7,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (13)x + (12) = 0",
    "options": [
      "A. x=-12;-1",
      "B. x=-1;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (2)x + (-168) = 0",
    "options": [
      "A. x=-14;12",
      "B. x=12;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+1y=22; 3x+3y=18",
    "options": [
      "A. x=8,y=-2",
      "B. x=-2,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+2y=7; 3x+1y=11",
    "options": [
      "A. x=5,y=-4",
      "B. x=-4,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-9)x + (-22) = 0",
    "options": [
      "A. x=11;-2",
      "B. x=-2;11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + 12 ≥ 12",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + 9 ≥ 15",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 8x + -12 ≥ -44",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+3y=-65; 1x+1y=-15",
    "options": [
      "A. x=-10,y=-5",
      "B. x=-5,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + 13 ≥ 94",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (1)x + (-56) = 0",
    "options": [
      "A. x=7;-8",
      "B. x=-8;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+2y=8; 1x+3y=-8",
    "options": [
      "A. x=10,y=-6",
      "B. x=-6,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 4x + -12 ≥ -36",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+3y=-10; 3x+4y=0",
    "options": [
      "A. x=8,y=-6",
      "B. x=-6,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+5y=2; 4x+1y=10",
    "options": [
      "A. x=3,y=-2",
      "B. x=-2,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-31)x + (240) = 0",
    "options": [
      "A. x=15;16",
      "B. x=16;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + 16 ≥ 13",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 8x + 20 ≥ -60",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-29)x + (190) = 0",
    "options": [
      "A. x=19;10",
      "B. x=10;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + 6 ≥ 33",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+2y=-20; 4x+1y=-10",
    "options": [
      "A. x=0,y=-10",
      "B. x=-10,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-20)x + (96) = 0",
    "options": [
      "A. x=12;8",
      "B. x=8;12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 8x + 20 ≥ -20",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+3y=-6; 4x+3y=3",
    "options": [
      "A. x=3,y=-3",
      "B. x=-3,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-20)x + (99) = 0",
    "options": [
      "A. x=9;11",
      "B. x=11;9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+1y=-16; 5x+2y=-20",
    "options": [
      "A. x=-4,y=0",
      "B. x=0,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+4y=30; 3x+1y=4",
    "options": [
      "A. x=-2,y=10",
      "B. x=10,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + 5 ≥ -22",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (13)x + (-68) = 0",
    "options": [
      "A. x=-17;4",
      "B. x=4;-17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+5y=-9; 4x+2y=2",
    "options": [
      "A. x=2,y=-3",
      "B. x=-3,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-21)x + (90) = 0",
    "options": [
      "A. x=15;6",
      "B. x=6;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + -19 ≥ -25",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 8x + -17 ≥ -17",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+3y=-22; 1x+3y=-17",
    "options": [
      "A. x=-5,y=-4",
      "B. x=-4,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+1y=3; 2x+3y=1",
    "options": [
      "A. x=2,y=-1",
      "B. x=-1,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-25)x + (114) = 0",
    "options": [
      "A. x=6;19",
      "B. x=19;6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+2y=-46; 3x+5y=-20",
    "options": [
      "A. x=-10,y=2",
      "B. x=2,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-14)x + (45) = 0",
    "options": [
      "A. x=5;9",
      "B. x=9;5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-22)x + (85) = 0",
    "options": [
      "A. x=5;17",
      "B. x=17;5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+5y=-15; 1x+5y=5",
    "options": [
      "A. x=-10,y=3",
      "B. x=3,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + 14 ≥ 44",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+5y=45; 3x+4y=34",
    "options": [
      "A. x=10,y=1",
      "B. x=1,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + -15 ≥ -79",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + -18 ≥ -36",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (6)x + (-72) = 0",
    "options": [
      "A. x=6;-12",
      "B. x=-12;6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + 17 ≥ 37",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+3y=-21; 3x+1y=0",
    "options": [
      "A. x=3,y=-9",
      "B. x=-9,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + -3 ≥ 21",
    "options": [
      "A. x ≥ 8",
      "B. x ≤ 8",
      "C. x > 8",
      "D. x < 8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + -16 ≥ 34",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-27)x + (176) = 0",
    "options": [
      "A. x=11;16",
      "B. x=16;11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+5y=45; 1x+1y=9",
    "options": [
      "A. x=0,y=9",
      "B. x=9,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+2y=-22; 3x+3y=-3",
    "options": [
      "A. x=-10,y=9",
      "B. x=9,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + -6 ≥ -33",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=6; 3x+5y=10",
    "options": [
      "A. x=0,y=2",
      "B. x=2,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + 16 ≥ -2",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + 0 ≥ 2",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+3y=27; 1x+2y=10",
    "options": [
      "A. x=8,y=1",
      "B. x=1,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+4y=8; 4x+5y=2",
    "options": [
      "A. x=8,y=-6",
      "B. x=-6,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + -2 ≥ -8",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+5y=-4; 3x+2y=-16",
    "options": [
      "A. x=-8,y=4",
      "B. x=4,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 5x + 4 ≥ -41",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (33)x + (272) = 0",
    "options": [
      "A. x=-16;-17",
      "B. x=-17;-16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + -19 ≥ -55",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + -6 ≥ 4",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-209) = 0",
    "options": [
      "A. x=-11;19",
      "B. x=19;-11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (0) = 0",
    "options": [
      "A. x=0;8",
      "B. x=8;0",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+5y=2; 1x+5y=-16",
    "options": [
      "A. x=9,y=-5",
      "B. x=-5,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+5y=4; 1x+2y=1",
    "options": [
      "A. x=3,y=-1",
      "B. x=-1,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+2y=20; 4x+1y=12",
    "options": [
      "A. x=1,y=8",
      "B. x=8,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + -10 ≥ -25",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-22)x + (117) = 0",
    "options": [
      "A. x=9;13",
      "B. x=13;9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (27)x + (170) = 0",
    "options": [
      "A. x=-17;-10",
      "B. x=-10;-17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+4y=-10; 1x+5y=-7",
    "options": [
      "A. x=-2,y=-1",
      "B. x=-1,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-84) = 0",
    "options": [
      "A. x=14;-6",
      "B. x=-6;14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + -3 ≥ 42",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (3)x + (-108) = 0",
    "options": [
      "A. x=-12;9",
      "B. x=9;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+4y=-23; 5x+3y=-47",
    "options": [
      "A. x=-7,y=-4",
      "B. x=-4,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + 8 ≥ 12",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+3y=-13; 2x+4y=-8",
    "options": [
      "A. x=-2,y=-1",
      "B. x=-1,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-26)x + (120) = 0",
    "options": [
      "A. x=6;20",
      "B. x=20;6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-29)x + (198) = 0",
    "options": [
      "A. x=11;18",
      "B. x=18;11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + -8 ≥ 19",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+1y=15; 1x+5y=-21",
    "options": [
      "A. x=4,y=-5",
      "B. x=-5,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-9)x + (-52) = 0",
    "options": [
      "A. x=13;-4",
      "B. x=-4;13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+3y=3; 4x+4y=4",
    "options": [
      "A. x=-9,y=10",
      "B. x=10,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+4y=-42; 3x+5y=-45",
    "options": [
      "A. x=-10,y=-3",
      "B. x=-3,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+4y=-2; 1x+5y=-5",
    "options": [
      "A. x=10,y=-3",
      "B. x=-3,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (14)x + (33) = 0",
    "options": [
      "A. x=-11;-3",
      "B. x=-3;-11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + -6 ≥ 3",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+4y=1; 4x+5y=-7",
    "options": [
      "A. x=-3,y=1",
      "B. x=1,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+4y=29; 5x+3y=41",
    "options": [
      "A. x=7,y=2",
      "B. x=2,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+4y=55; 2x+2y=26",
    "options": [
      "A. x=3,y=10",
      "B. x=10,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-25)x + (136) = 0",
    "options": [
      "A. x=17;8",
      "B. x=8;17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+2y=8; 2x+4y=16",
    "options": [
      "A. x=4,y=2",
      "B. x=2,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (0) = 0",
    "options": [
      "A. x=6;0",
      "B. x=0;6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + 4 ≥ -5",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+2y=-8; 4x+1y=10",
    "options": [
      "A. x=4,y=-6",
      "B. x=-6,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+4y=-48; 1x+5y=-24",
    "options": [
      "A. x=-9,y=-3",
      "B. x=-3,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + 20 ≥ 12",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (0)x + (-196) = 0",
    "options": [
      "A. x=-14;14",
      "B. x=14;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-3)x + (-340) = 0",
    "options": [
      "A. x=-17;20",
      "B. x=20;-17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + 1 ≥ 5",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 4x + -6 ≥ -22",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (13)x + (22) = 0",
    "options": [
      "A. x=-2;-11",
      "B. x=-11;-2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+1y=7; 2x+3y=-5",
    "options": [
      "A. x=2,y=-3",
      "B. x=-3,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+3y=-24; 2x+4y=-2",
    "options": [
      "A. x=-9,y=4",
      "B. x=4,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + 6 ≥ -3",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + -11 ≥ -14",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+3y=4; 5x+3y=-4",
    "options": [
      "A. x=-2,y=2",
      "B. x=2,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (25)x + (144) = 0",
    "options": [
      "A. x=-16;-9",
      "B. x=-9;-16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+5y=-35; 3x+1y=-7",
    "options": [
      "A. x=0,y=-7",
      "B. x=-7,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + -1 ≥ -7",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 20 ≥ -40",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+5y=-28; 2x+3y=-18",
    "options": [
      "A. x=3,y=-8",
      "B. x=-8,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+3y=-4; 1x+2y=-6",
    "options": [
      "A. x=2,y=-4",
      "B. x=-4,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + -5 ≥ 16",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-9)x + (-136) = 0",
    "options": [
      "A. x=-8;17",
      "B. x=17;-8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 2x + 7 ≥ 11",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + -3 ≥ 77",
    "options": [
      "A. x ≥ 8",
      "B. x ≤ 8",
      "C. x > 8",
      "D. x < 8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + 5 ≥ 59",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (3)x + (-108) = 0",
    "options": [
      "A. x=-12;9",
      "B. x=9;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (12)x + (36) = 0",
    "options": [
      "A. x=-6;-6",
      "B. x=-6;-6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-11)x + (-60) = 0",
    "options": [
      "A. x=-4;15",
      "B. x=15;-4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (2)x + (-48) = 0",
    "options": [
      "A. x=6;-8",
      "B. x=-8;6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 2x + 19 ≥ 7",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 9 ≥ -41",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 7x + -10 ≥ -10",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-22)x + (105) = 0",
    "options": [
      "A. x=15;7",
      "B. x=7;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 6x + -16 ≥ -52",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+4y=6; 4x+5y=21",
    "options": [
      "A. x=-6,y=9",
      "B. x=9,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+1y=-4; 5x+3y=-8",
    "options": [
      "A. x=-1,y=-1",
      "B. x=-1,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+1y=12; 3x+1y=7",
    "options": [
      "A. x=5,y=-8",
      "B. x=-8,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+2y=34; 2x+1y=17",
    "options": [
      "A. x=10,y=-3",
      "B. x=-3,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (8)x + (-180) = 0",
    "options": [
      "A. x=-18;10",
      "B. x=10;-18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + -14 ≥ -24",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (21)x + (108) = 0",
    "options": [
      "A. x=-12;-9",
      "B. x=-9;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+4y=-5; 3x+2y=-1",
    "options": [
      "A. x=1,y=-2",
      "B. x=-2,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+5y=28; 5x+1y=1",
    "options": [
      "A. x=-1,y=6",
      "B. x=6,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+1y=-40; 5x+4y=-90",
    "options": [
      "A. x=-10,y=-10",
      "B. x=-10,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + -3 ≥ -75",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 6 ≥ -54",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + 20 ≥ 29",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-15)x + (36) = 0",
    "options": [
      "A. x=12;3",
      "B. x=3;12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + -8 ≥ 55",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+3y=1; 4x+4y=12",
    "options": [
      "A. x=-4,y=7",
      "B. x=7,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-14)x + (24) = 0",
    "options": [
      "A. x=2;12",
      "B. x=12;2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + -6 ≥ 9",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (29)x + (210) = 0",
    "options": [
      "A. x=-14;-15",
      "B. x=-15;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + 2 ≥ -47",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 1 ≥ 21",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+3y=30; 4x+2y=20",
    "options": [
      "A. x=0,y=10",
      "B. x=10,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+3y=-13; 1x+2y=10",
    "options": [
      "A. x=-8,y=9",
      "B. x=9,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+3y=-48; 5x+1y=-48",
    "options": [
      "A. x=-8,y=-8",
      "B. x=-8,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (6)x + (-160) = 0",
    "options": [
      "A. x=-16;10",
      "B. x=10;-16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + 1 ≥ -27",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 16 ≥ 66",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+2y=-6; 1x+5y=-3",
    "options": [
      "A. x=-8,y=1",
      "B. x=1,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (8)x + (-33) = 0",
    "options": [
      "A. x=3;-11",
      "B. x=-11;3",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + -8 ≥ -71",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-27)x + (170) = 0",
    "options": [
      "A. x=10;17",
      "B. x=17;10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + -2 ≥ 33",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (8)x + (-240) = 0",
    "options": [
      "A. x=-20;12",
      "B. x=12;-20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+1y=15; 3x+5y=-10",
    "options": [
      "A. x=5,y=-5",
      "B. x=-5,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+1y=17; 4x+1y=17",
    "options": [
      "A. x=2,y=9",
      "B. x=9,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (5)x + (-266) = 0",
    "options": [
      "A. x=-19;14",
      "B. x=14;-19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+5y=5; 2x+3y=11",
    "options": [
      "A. x=-8,y=9",
      "B. x=9,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+2y=-7; 2x+5y=-17",
    "options": [
      "A. x=-1,y=-3",
      "B. x=-3,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (7)x + (-198) = 0",
    "options": [
      "A. x=11;-18",
      "B. x=-18;11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (5)x + (-150) = 0",
    "options": [
      "A. x=10;-15",
      "B. x=-15;10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (37)x + (342) = 0",
    "options": [
      "A. x=-19;-18",
      "B. x=-18;-19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (10)x + (-119) = 0",
    "options": [
      "A. x=7;-17",
      "B. x=-17;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-7)x + (10) = 0",
    "options": [
      "A. x=5;2",
      "B. x=2;5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+2y=-43; 3x+2y=-29",
    "options": [
      "A. x=-7,y=-4",
      "B. x=-4,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + -18 ≥ -38",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+4y=32; 1x+3y=24",
    "options": [
      "A. x=0,y=8",
      "B. x=8,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-25)x + (126) = 0",
    "options": [
      "A. x=18;7",
      "B. x=7;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-7)x + (-170) = 0",
    "options": [
      "A. x=17;-10",
      "B. x=-10;17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+3y=-33; 3x+2y=-30",
    "options": [
      "A. x=-8,y=-3",
      "B. x=-3,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-29)x + (198) = 0",
    "options": [
      "A. x=11;18",
      "B. x=18;11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 6x + -3 ≥ 21",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+4y=-10; 1x+2y=-5",
    "options": [
      "A. x=-5,y=0",
      "B. x=0,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+4y=48; 5x+2y=51",
    "options": [
      "A. x=9,y=3",
      "B. x=3,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-3)x + (-40) = 0",
    "options": [
      "A. x=-5;8",
      "B. x=8;-5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+3y=-65; 1x+1y=-17",
    "options": [
      "A. x=-7,y=-10",
      "B. x=-10,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + -8 ≥ 22",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-4)x + (-96) = 0",
    "options": [
      "A. x=12;-8",
      "B. x=-8;12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-20) = 0",
    "options": [
      "A. x=-2;10",
      "B. x=10;-2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+4y=44; 5x+3y=67",
    "options": [
      "A. x=8,y=9",
      "B. x=9,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+1y=6; 2x+2y=-2",
    "options": [
      "A. x=7,y=-8",
      "B. x=-8,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-15)x + (-16) = 0",
    "options": [
      "A. x=16;-1",
      "B. x=-1;16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (6)x + (-7) = 0",
    "options": [
      "A. x=1;-7",
      "B. x=-7;1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 6x + 20 ≥ -34",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (3)x + (-238) = 0",
    "options": [
      "A. x=14;-17",
      "B. x=-17;14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+5y=8; 2x+4y=10",
    "options": [
      "A. x=-3,y=4",
      "B. x=4,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + 0 ≥ -6",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+3y=-33; 1x+2y=-1",
    "options": [
      "A. x=-9,y=4",
      "B. x=4,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-9)x + (8) = 0",
    "options": [
      "A. x=8;1",
      "B. x=1;8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+5y=24; 3x+1y=-12",
    "options": [
      "A. x=-7,y=9",
      "B. x=9,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 5x + 5 ≥ -45",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+3y=33; 1x+2y=1",
    "options": [
      "A. x=9,y=-4",
      "B. x=-4,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + 18 ≥ 18",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 8x + 8 ≥ -16",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+2y=-8; 3x+1y=-24",
    "options": [
      "A. x=-8,y=0",
      "B. x=0,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 5x + 1 ≥ -9",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + -12 ≥ 6",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=13; 1x+1y=4",
    "options": [
      "A. x=1,y=3",
      "B. x=3,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + 19 ≥ -9",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+2y=32; 1x+4y=1",
    "options": [
      "A. x=9,y=-2",
      "B. x=-2,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (13)x + (12) = 0",
    "options": [
      "A. x=-12;-1",
      "B. x=-1;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + -2 ≥ -2",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-187) = 0",
    "options": [
      "A. x=17;-11",
      "B. x=-11;17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + 17 ≥ -23",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (14)x + (-32) = 0",
    "options": [
      "A. x=-16;2",
      "B. x=2;-16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (1)x + (-210) = 0",
    "options": [
      "A. x=14;-15",
      "B. x=-15;14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+4y=7; 3x+5y=-14",
    "options": [
      "A. x=7,y=-7",
      "B. x=-7,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + 6 ≥ -15",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (25)x + (156) = 0",
    "options": [
      "A. x=-12;-13",
      "B. x=-13;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-32)x + (252) = 0",
    "options": [
      "A. x=18;14",
      "B. x=14;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (2)x + (-168) = 0",
    "options": [
      "A. x=-14;12",
      "B. x=12;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + 11 ≥ 17",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 6x + -13 ≥ 41",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 4x + -3 ≥ -27",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+1y=-26; 3x+4y=-36",
    "options": [
      "A. x=-4,y=-6",
      "B. x=-6,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + 15 ≥ 71",
    "options": [
      "A. x ≥ 8",
      "B. x ≤ 8",
      "C. x > 8",
      "D. x < 8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-21)x + (104) = 0",
    "options": [
      "A. x=8;13",
      "B. x=13;8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-18)x + (65) = 0",
    "options": [
      "A. x=13;5",
      "B. x=5;13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+5y=34; 3x+2y=-4",
    "options": [
      "A. x=-8,y=10",
      "B. x=10,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+2y=-3; 1x+4y=-3",
    "options": [
      "A. x=-3,y=0",
      "B. x=0,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + 4 ≥ -14",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-5)x + (-50) = 0",
    "options": [
      "A. x=-5;10",
      "B. x=10;-5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + 11 ≥ 11",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (35)x + (300) = 0",
    "options": [
      "A. x=-15;-20",
      "B. x=-20;-15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + 16 ≥ -4",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + -18 ≥ -68",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+2y=-30; 1x+2y=10",
    "options": [
      "A. x=-10,y=10",
      "B. x=10,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+2y=-7; 5x+1y=19",
    "options": [
      "A. x=5,y=-6",
      "B. x=-6,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + 7 ≥ 7",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (0)x + (-196) = 0",
    "options": [
      "A. x=-14;14",
      "B. x=14;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-29)x + (190) = 0",
    "options": [
      "A. x=19;10",
      "B. x=10;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 10x + -20 ≥ -10",
    "options": [
      "A. x ≥ 1",
      "B. x ≤ 1",
      "C. x > 1",
      "D. x < 1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+2y=-6; 2x+1y=-15",
    "options": [
      "A. x=-8,y=1",
      "B. x=1,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + 4 ≥ -1",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+1y=42; 2x+4y=56",
    "options": [
      "A. x=8,y=10",
      "B. x=10,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + -8 ≥ 32",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+1y=-34; 1x+1y=-6",
    "options": [
      "A. x=-7,y=1",
      "B. x=1,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (8)x + (-105) = 0",
    "options": [
      "A. x=-15;7",
      "B. x=7;-15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 10x + -7 ≥ 43",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+3y=34; 2x+5y=6",
    "options": [
      "A. x=8,y=-2",
      "B. x=-2,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + 4 ≥ -8",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-3)x + (-108) = 0",
    "options": [
      "A. x=12;-9",
      "B. x=-9;12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-14)x + (-51) = 0",
    "options": [
      "A. x=17;-3",
      "B. x=-3;17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+2y=-4; 3x+1y=-2",
    "options": [
      "A. x=0,y=-2",
      "B. x=-2,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (0)x + (-16) = 0",
    "options": [
      "A. x=4;-4",
      "B. x=-4;4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 8x + -19 ≥ -51",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 2x + 5 ≥ 5",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+1y=-16; 4x+4y=-32",
    "options": [
      "A. x=-8,y=0",
      "B. x=0,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + 16 ≥ 32",
    "options": [
      "A. x ≥ 8",
      "B. x ≤ 8",
      "C. x > 8",
      "D. x < 8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (17)x + (42) = 0",
    "options": [
      "A. x=-14;-3",
      "B. x=-3;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + -6 ≥ -8",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (10)x + (24) = 0",
    "options": [
      "A. x=-4;-6",
      "B. x=-6;-4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-180) = 0",
    "options": [
      "A. x=18;-10",
      "B. x=-10;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+4y=-24; 3x+3y=-18",
    "options": [
      "A. x=-8,y=2",
      "B. x=2,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-2)x + (-35) = 0",
    "options": [
      "A. x=7;-5",
      "B. x=-5;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+4y=17; 4x+1y=8",
    "options": [
      "A. x=1,y=4",
      "B. x=4,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+5y=-20; 1x+5y=-20",
    "options": [
      "A. x=10,y=-6",
      "B. x=-6,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+4y=16; 1x+3y=17",
    "options": [
      "A. x=-4,y=7",
      "B. x=7,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (4)x + (-320) = 0",
    "options": [
      "A. x=-20;16",
      "B. x=16;-20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-26)x + (133) = 0",
    "options": [
      "A. x=19;7",
      "B. x=7;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-7)x + (6) = 0",
    "options": [
      "A. x=6;1",
      "B. x=1;6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + 14 ≥ -6",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (25)x + (154) = 0",
    "options": [
      "A. x=-11;-14",
      "B. x=-14;-11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+5y=32; 2x+1y=5",
    "options": [
      "A. x=-1,y=7",
      "B. x=7,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-160) = 0",
    "options": [
      "A. x=-10;16",
      "B. x=16;-10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+3y=8; 1x+3y=4",
    "options": [
      "A. x=4,y=0",
      "B. x=0,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + 18 ≥ -46",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + -3 ≥ -93",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 8x + -19 ≥ 29",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + -8 ≥ -6",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=13; 2x+5y=17",
    "options": [
      "A. x=1,y=3",
      "B. x=3,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 5x + -9 ≥ -24",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-17)x + (16) = 0",
    "options": [
      "A. x=16;1",
      "B. x=1;16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (0)x + (-81) = 0",
    "options": [
      "A. x=-9;9",
      "B. x=9;-9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (0)x + (-169) = 0",
    "options": [
      "A. x=-13;13",
      "B. x=13;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-33)x + (272) = 0",
    "options": [
      "A. x=16;17",
      "B. x=17;16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 2x + -8 ≥ 4",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (33)x + (270) = 0",
    "options": [
      "A. x=-18;-15",
      "B. x=-15;-18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (31)x + (240) = 0",
    "options": [
      "A. x=-16;-15",
      "B. x=-15;-16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-1)x + (-342) = 0",
    "options": [
      "A. x=19;-18",
      "B. x=-18;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+3y=9; 5x+5y=15",
    "options": [
      "A. x=1,y=2",
      "B. x=2,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+3y=15; 1x+2y=9",
    "options": [
      "A. x=-3,y=6",
      "B. x=6,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (31)x + (240) = 0",
    "options": [
      "A. x=-15;-16",
      "B. x=-16;-15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (4)x + (-96) = 0",
    "options": [
      "A. x=-12;8",
      "B. x=8;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-31)x + (240) = 0",
    "options": [
      "A. x=15;16",
      "B. x=16;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+5y=11; 3x+4y=22",
    "options": [
      "A. x=6,y=1",
      "B. x=1,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+5y=55; 1x+2y=16",
    "options": [
      "A. x=10,y=3",
      "B. x=3,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + 8 ≥ 1",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 2x + -8 ≥ 0",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 2x + 12 ≥ -2",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-11)x + (-12) = 0",
    "options": [
      "A. x=-1;12",
      "B. x=12;-1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-4)x + (-320) = 0",
    "options": [
      "A. x=-16;20",
      "B. x=20;-16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (2)x + (-99) = 0",
    "options": [
      "A. x=9;-11",
      "B. x=-11;9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (18)x + (80) = 0",
    "options": [
      "A. x=-8;-10",
      "B. x=-10;-8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 2x + 13 ≥ -3",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (21)x + (38) = 0",
    "options": [
      "A. x=-19;-2",
      "B. x=-2;-19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + -12 ≥ -24",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+1y=-29; 3x+5y=-43",
    "options": [
      "A. x=-6,y=-5",
      "B. x=-5,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (14)x + (24) = 0",
    "options": [
      "A. x=-12;-2",
      "B. x=-2;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + 1 ≥ -31",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + 7 ≥ 61",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+1y=-4; 5x+1y=-2",
    "options": [
      "A. x=1,y=-7",
      "B. x=-7,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (10)x + (16) = 0",
    "options": [
      "A. x=-8;-2",
      "B. x=-2;-8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+1y=-5; 4x+5y=-16",
    "options": [
      "A. x=-9,y=4",
      "B. x=4,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (13)x + (-14) = 0",
    "options": [
      "A. x=1;-14",
      "B. x=-14;1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + 10 ≥ 5",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-29)x + (190) = 0",
    "options": [
      "A. x=10;19",
      "B. x=19;10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-20)x + (0) = 0",
    "options": [
      "A. x=20;0",
      "B. x=0;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+1y=26; 5x+3y=29",
    "options": [
      "A. x=7,y=-2",
      "B. x=-2,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+2y=11; 3x+3y=21",
    "options": [
      "A. x=3,y=4",
      "B. x=4,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + -13 ≥ -9",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+4y=75; 2x+1y=24",
    "options": [
      "A. x=7,y=10",
      "B. x=10,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+4y=30; 2x+4y=30",
    "options": [
      "A. x=3,y=6",
      "B. x=6,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + 17 ≥ -18",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-23)x + (90) = 0",
    "options": [
      "A. x=18;5",
      "B. x=5;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+4y=-82; 1x+5y=-50",
    "options": [
      "A. x=-10,y=-8",
      "B. x=-8,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + -19 ≥ -22",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-20)x + (91) = 0",
    "options": [
      "A. x=7;13",
      "B. x=13;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + 20 ≥ 0",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + -12 ≥ -27",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 6x + 16 ≥ 28",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + -17 ≥ -17",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-2)x + (-48) = 0",
    "options": [
      "A. x=-6;8",
      "B. x=8;-6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (4)x + (-21) = 0",
    "options": [
      "A. x=3;-7",
      "B. x=-7;3",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+3y=29; 2x+1y=12",
    "options": [
      "A. x=7,y=-2",
      "B. x=-2,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 6x + -3 ≥ 33",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (18)x + (80) = 0",
    "options": [
      "A. x=-8;-10",
      "B. x=-10;-8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+5y=0; 4x+2y=-14",
    "options": [
      "A. x=-7,y=7",
      "B. x=7,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+5y=-48; 1x+1y=-12",
    "options": [
      "A. x=-4,y=-8",
      "B. x=-8,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-32)x + (256) = 0",
    "options": [
      "A. x=16;16",
      "B. x=16;16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + 7 ≥ 61",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + 18 ≥ 72",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=42; 1x+2y=18",
    "options": [
      "A. x=6,y=6",
      "B. x=6,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (19)x + (78) = 0",
    "options": [
      "A. x=-13;-6",
      "B. x=-6;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 2x + 13 ≥ -5",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-27) = 0",
    "options": [
      "A. x=-3;9",
      "B. x=9;-3",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-12)x + (35) = 0",
    "options": [
      "A. x=7;5",
      "B. x=5;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + -3 ≥ -3",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+2y=-8; 1x+3y=-8",
    "options": [
      "A. x=-8,y=0",
      "B. x=0,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (20)x + (91) = 0",
    "options": [
      "A. x=-13;-7",
      "B. x=-7;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (5)x + (-126) = 0",
    "options": [
      "A. x=9;-14",
      "B. x=-14;9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (30)x + (216) = 0",
    "options": [
      "A. x=-12;-18",
      "B. x=-18;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (8)x + (-128) = 0",
    "options": [
      "A. x=8;-16",
      "B. x=-16;8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + 4 ≥ -52",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+3y=-24; 3x+3y=-24",
    "options": [
      "A. x=0,y=-8",
      "B. x=-8,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 6x + -4 ≥ 50",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+2y=-20; 5x+5y=-20",
    "options": [
      "A. x=-4,y=0",
      "B. x=0,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+4y=-13; 2x+3y=-11",
    "options": [
      "A. x=-1,y=-3",
      "B. x=-3,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (23)x + (130) = 0",
    "options": [
      "A. x=-13;-10",
      "B. x=-10;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + 16 ≥ -20",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (16)x + (-36) = 0",
    "options": [
      "A. x=-18;2",
      "B. x=2;-18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-23)x + (126) = 0",
    "options": [
      "A. x=14;9",
      "B. x=9;14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + -2 ≥ -18",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + 19 ≥ 4",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + -13 ≥ -67",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+5y=-26; 3x+3y=-30",
    "options": [
      "A. x=-6,y=-4",
      "B. x=-4,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (9)x + (-22) = 0",
    "options": [
      "A. x=2;-11",
      "B. x=-11;2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (16)x + (60) = 0",
    "options": [
      "A. x=-10;-6",
      "B. x=-6;-10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-9)x + (-70) = 0",
    "options": [
      "A. x=14;-5",
      "B. x=-5;14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 8x + 11 ≥ -61",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-3)x + (-4) = 0",
    "options": [
      "A. x=4;-1",
      "B. x=-1;4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+4y=24; 2x+3y=11",
    "options": [
      "A. x=4,y=1",
      "B. x=1,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+1y=15; 5x+5y=15",
    "options": [
      "A. x=3,y=0",
      "B. x=0,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+4y=40; 1x+2y=20",
    "options": [
      "A. x=0,y=10",
      "B. x=10,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 6x + 0 ≥ 36",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (15)x + (36) = 0",
    "options": [
      "A. x=-3;-12",
      "B. x=-12;-3",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-20) = 0",
    "options": [
      "A. x=-2;10",
      "B. x=10;-2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + 17 ≥ 32",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 4x + 16 ≥ 28",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (3)x + (-270) = 0",
    "options": [
      "A. x=15;-18",
      "B. x=-18;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + -17 ≥ -21",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + 9 ≥ 21",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-15)x + (-54) = 0",
    "options": [
      "A. x=-3;18",
      "B. x=18;-3",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 8x + -18 ≥ -26",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 14 ≥ 44",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + -3 ≥ 4",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (30)x + (224) = 0",
    "options": [
      "A. x=-14;-16",
      "B. x=-16;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+4y=1; 1x+3y=2",
    "options": [
      "A. x=5,y=-1",
      "B. x=-1,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+2y=8; 3x+3y=3",
    "options": [
      "A. x=2,y=-1",
      "B. x=-1,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-33)x + (260) = 0",
    "options": [
      "A. x=20;13",
      "B. x=13;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-14)x + (-120) = 0",
    "options": [
      "A. x=-6;20",
      "B. x=20;-6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (15)x + (44) = 0",
    "options": [
      "A. x=-4;-11",
      "B. x=-11;-4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + 9 ≥ -7",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+2y=-2; 1x+1y=-4",
    "options": [
      "A. x=6,y=-10",
      "B. x=-10,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 10x + 16 ≥ 66",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-14)x + (-120) = 0",
    "options": [
      "A. x=20;-6",
      "B. x=-6;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+2y=-24; 1x+3y=-10",
    "options": [
      "A. x=-4,y=-2",
      "B. x=-2,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+5y=-41; 1x+5y=-41",
    "options": [
      "A. x=9,y=-10",
      "B. x=-10,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + 13 ≥ 12",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+4y=-39; 2x+5y=-36",
    "options": [
      "A. x=-3,y=-6",
      "B. x=-6,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 4x + 16 ≥ 56",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 7x + 19 ≥ 61",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + 16 ≥ 22",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+2y=-4; 2x+4y=-8",
    "options": [
      "A. x=0,y=-2",
      "B. x=-2,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + 16 ≥ 80",
    "options": [
      "A. x ≥ 8",
      "B. x ≤ 8",
      "C. x > 8",
      "D. x < 8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + -3 ≥ -1",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-2)x + (-3) = 0",
    "options": [
      "A. x=3;-1",
      "B. x=-1;3",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+1y=-30; 4x+1y=-26",
    "options": [
      "A. x=-4,y=-10",
      "B. x=-10,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + -3 ≥ -13",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=9; 3x+2y=5",
    "options": [
      "A. x=-3,y=7",
      "B. x=7,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + -14 ≥ -41",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (2)x + (-360) = 0",
    "options": [
      "A. x=-20;18",
      "B. x=18;-20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + -11 ≥ -7",
    "options": [
      "A. x ≥ 1",
      "B. x ≤ 1",
      "C. x > 1",
      "D. x < 1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + -13 ≥ 7",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+4y=24; 1x+3y=18",
    "options": [
      "A. x=0,y=6",
      "B. x=6,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-2)x + (-288) = 0",
    "options": [
      "A. x=18;-16",
      "B. x=-16;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+3y=-65; 5x+3y=-65",
    "options": [
      "A. x=-10,y=-5",
      "B. x=-5,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+4y=26; 3x+3y=15",
    "options": [
      "A. x=-3,y=8",
      "B. x=8,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+3y=43; 4x+4y=52",
    "options": [
      "A. x=4,y=9",
      "B. x=9,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-15)x + (0) = 0",
    "options": [
      "A. x=15;0",
      "B. x=0;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + -20 ≥ -48",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + 5 ≥ -22",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-9)x + (-220) = 0",
    "options": [
      "A. x=20;-11",
      "B. x=-11;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+2y=32; 1x+4y=14",
    "options": [
      "A. x=10,y=1",
      "B. x=1,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-27) = 0",
    "options": [
      "A. x=9;-3",
      "B. x=-3;9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+2y=-18; 5x+5y=-45",
    "options": [
      "A. x=-4,y=-5",
      "B. x=-5,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-14)x + (48) = 0",
    "options": [
      "A. x=8;6",
      "B. x=6;8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + -14 ≥ 13",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+4y=23; 3x+2y=-11",
    "options": [
      "A. x=-9,y=8",
      "B. x=8,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + -7 ≥ 0",
    "options": [
      "A. x ≥ 1",
      "B. x ≤ 1",
      "C. x > 1",
      "D. x < 1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=-3; 4x+3y=-3",
    "options": [
      "A. x=-6,y=7",
      "B. x=7,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (1)x + (-380) = 0",
    "options": [
      "A. x=-20;19",
      "B. x=19;-20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (37)x + (340) = 0",
    "options": [
      "A. x=-17;-20",
      "B. x=-20;-17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+3y=1; 1x+4y=3",
    "options": [
      "A. x=-5,y=2",
      "B. x=2,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+4y=5; 4x+1y=-15",
    "options": [
      "A. x=-5,y=5",
      "B. x=5,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+1y=-8; 2x+2y=-16",
    "options": [
      "A. x=-9,y=1",
      "B. x=1,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 5x + 3 ≥ -22",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+4y=1; 3x+4y=-5",
    "options": [
      "A. x=-3,y=1",
      "B. x=1,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (23)x + (130) = 0",
    "options": [
      "A. x=-10;-13",
      "B. x=-13;-10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+1y=3; 5x+3y=5",
    "options": [
      "A. x=-2,y=5",
      "B. x=5,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (24)x + (95) = 0",
    "options": [
      "A. x=-19;-5",
      "B. x=-5;-19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+5y=52; 5x+2y=36",
    "options": [
      "A. x=4,y=8",
      "B. x=8,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 6x + 18 ≥ 66",
    "options": [
      "A. x ≥ 8",
      "B. x ≤ 8",
      "C. x > 8",
      "D. x < 8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-24)x + (135) = 0",
    "options": [
      "A. x=9;15",
      "B. x=15;9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+3y=33; 3x+1y=31",
    "options": [
      "A. x=10,y=1",
      "B. x=1,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+4y=42; 4x+1y=28",
    "options": [
      "A. x=5,y=8",
      "B. x=8,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+2y=13; 3x+5y=30",
    "options": [
      "A. x=-5,y=9",
      "B. x=9,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (0)x + (-324) = 0",
    "options": [
      "A. x=18;-18",
      "B. x=-18;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (30)x + (224) = 0",
    "options": [
      "A. x=-16;-14",
      "B. x=-14;-16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+4y=35; 1x+3y=20",
    "options": [
      "A. x=5,y=5",
      "B. x=5,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-37)x + (342) = 0",
    "options": [
      "A. x=18;19",
      "B. x=19;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+1y=-30; 3x+1y=-25",
    "options": [
      "A. x=-5,y=-10",
      "B. x=-10,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 6x + -17 ≥ 37",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+5y=9; 1x+4y=9",
    "options": [
      "A. x=-3,y=3",
      "B. x=3,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-7)x + (-170) = 0",
    "options": [
      "A. x=17;-10",
      "B. x=-10;17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-1)x + (-240) = 0",
    "options": [
      "A. x=16;-15",
      "B. x=-15;16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + -19 ≥ -40",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 7x + -20 ≥ 1",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 2x + 12 ≥ 6",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + -3 ≥ 15",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+5y=-60; 5x+1y=-40",
    "options": [
      "A. x=-7,y=-5",
      "B. x=-5,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-23)x + (130) = 0",
    "options": [
      "A. x=13;10",
      "B. x=10;13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+3y=-14; 3x+2y=-10",
    "options": [
      "A. x=2,y=-8",
      "B. x=-8,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+5y=68; 3x+3y=45",
    "options": [
      "A. x=7,y=8",
      "B. x=8,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+3y=47; 4x+5y=65",
    "options": [
      "A. x=5,y=9",
      "B. x=9,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (13)x + (40) = 0",
    "options": [
      "A. x=-8;-5",
      "B. x=-5;-8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 6x + -11 ≥ -17",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-1)x + (0) = 0",
    "options": [
      "A. x=1;0",
      "B. x=0;1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-17)x + (-18) = 0",
    "options": [
      "A. x=-1;18",
      "B. x=18;-1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (20)x + (75) = 0",
    "options": [
      "A. x=-15;-5",
      "B. x=-5;-15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+3y=-13; 5x+5y=-20",
    "options": [
      "A. x=-1,y=-3",
      "B. x=-3,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 6x + 18 ≥ -18",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+5y=-34; 5x+5y=-40",
    "options": [
      "A. x=-3,y=-5",
      "B. x=-5,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+1y=17; 2x+2y=16",
    "options": [
      "A. x=9,y=-1",
      "B. x=-1,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + 18 ≥ 108",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+3y=-7; 4x+4y=4",
    "options": [
      "A. x=-5,y=6",
      "B. x=6,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 10x + -2 ≥ -82",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (8) = 0",
    "options": [
      "A. x=4;2",
      "B. x=2;4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+1y=-26; 2x+1y=-11",
    "options": [
      "A. x=-5,y=-1",
      "B. x=-1,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+2y=-5; 5x+4y=-7",
    "options": [
      "A. x=-3,y=2",
      "B. x=2,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-36)x + (324) = 0",
    "options": [
      "A. x=18;18",
      "B. x=18;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (24)x + (80) = 0",
    "options": [
      "A. x=-20;-4",
      "B. x=-4;-20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+4y=40; 3x+3y=24",
    "options": [
      "A. x=8,y=0",
      "B. x=0,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + -20 ≥ -2",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (22)x + (121) = 0",
    "options": [
      "A. x=-11;-11",
      "B. x=-11;-11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+2y=10; 3x+3y=0",
    "options": [
      "A. x=5,y=-5",
      "B. x=-5,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+4y=22; 3x+5y=31",
    "options": [
      "A. x=7,y=2",
      "B. x=2,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+2y=12; 4x+3y=2",
    "options": [
      "A. x=8,y=-10",
      "B. x=-10,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+4y=-8; 2x+5y=-10",
    "options": [
      "A. x=0,y=-2",
      "B. x=-2,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+4y=-48; 3x+2y=-34",
    "options": [
      "A. x=-10,y=-2",
      "B. x=-2,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+2y=12; 5x+5y=30",
    "options": [
      "A. x=0,y=6",
      "B. x=6,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + -17 ≥ -38",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + -5 ≥ 31",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+1y=-9; 2x+3y=-21",
    "options": [
      "A. x=-6,y=-3",
      "B. x=-3,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (5)x + (-66) = 0",
    "options": [
      "A. x=-11;6",
      "B. x=6;-11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + 4 ≥ -20",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + -4 ≥ 17",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (14)x + (48) = 0",
    "options": [
      "A. x=-6;-8",
      "B. x=-8;-6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (8)x + (7) = 0",
    "options": [
      "A. x=-7;-1",
      "B. x=-1;-7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-12)x + (-13) = 0",
    "options": [
      "A. x=-1;13",
      "B. x=13;-1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+5y=-20; 4x+4y=-24",
    "options": [
      "A. x=-5,y=-1",
      "B. x=-1,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + -5 ≥ 27",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (20)x + (99) = 0",
    "options": [
      "A. x=-11;-9",
      "B. x=-9;-11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + -19 ≥ -91",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 5x + 12 ≥ 2",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-16)x + (-80) = 0",
    "options": [
      "A. x=20;-4",
      "B. x=-4;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-16)x + (15) = 0",
    "options": [
      "A. x=15;1",
      "B. x=1;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + 4 ≥ 31",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (9)x + (-70) = 0",
    "options": [
      "A. x=5;-14",
      "B. x=-14;5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+5y=44; 1x+4y=31",
    "options": [
      "A. x=3,y=7",
      "B. x=7,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-5)x + (-24) = 0",
    "options": [
      "A. x=8;-3",
      "B. x=-3;8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 8x + 16 ≥ 72",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 8x + 11 ≥ 83",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-4)x + (-32) = 0",
    "options": [
      "A. x=8;-4",
      "B. x=-4;8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+4y=-36; 5x+4y=-36",
    "options": [
      "A. x=0,y=-9",
      "B. x=-9,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+5y=-48; 4x+3y=-22",
    "options": [
      "A. x=2,y=-10",
      "B. x=-10,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+4y=-24; 5x+5y=-35",
    "options": [
      "A. x=-4,y=-3",
      "B. x=-3,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-6)x + (-55) = 0",
    "options": [
      "A. x=11;-5",
      "B. x=-5;11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-14)x + (-15) = 0",
    "options": [
      "A. x=-1;15",
      "B. x=15;-1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-23)x + (112) = 0",
    "options": [
      "A. x=16;7",
      "B. x=7;16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+4y=16; 2x+5y=15",
    "options": [
      "A. x=10,y=-1",
      "B. x=-1,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 6x + 14 ≥ 56",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-105) = 0",
    "options": [
      "A. x=-7;15",
      "B. x=15;-7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+4y=14; 1x+5y=10",
    "options": [
      "A. x=5,y=1",
      "B. x=1,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (10)x + (0) = 0",
    "options": [
      "A. x=0;-10",
      "B. x=-10;0",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 8x + -7 ≥ -87",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-22)x + (117) = 0",
    "options": [
      "A. x=13;9",
      "B. x=9;13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-31)x + (240) = 0",
    "options": [
      "A. x=15;16",
      "B. x=16;15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 4x + -3 ≥ 9",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+4y=31; 2x+1y=4",
    "options": [
      "A. x=-3,y=10",
      "B. x=10,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (7)x + (-44) = 0",
    "options": [
      "A. x=-11;4",
      "B. x=4;-11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + -1 ≥ -73",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+4y=-32; 2x+5y=-13",
    "options": [
      "A. x=-9,y=1",
      "B. x=1,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-11)x + (18) = 0",
    "options": [
      "A. x=2;9",
      "B. x=9;2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+5y=69; 5x+5y=75",
    "options": [
      "A. x=6,y=9",
      "B. x=9,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (9)x + (0) = 0",
    "options": [
      "A. x=0;-9",
      "B. x=-9;0",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (11)x + (28) = 0",
    "options": [
      "A. x=-4;-7",
      "B. x=-7;-4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 10x + -15 ≥ -95",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (23)x + (130) = 0",
    "options": [
      "A. x=-13;-10",
      "B. x=-10;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+3y=-29; 5x+4y=-41",
    "options": [
      "A. x=-1,y=-9",
      "B. x=-9,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + 18 ≥ -22",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 4x + 18 ≥ 54",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (1)x + (-72) = 0",
    "options": [
      "A. x=8;-9",
      "B. x=-9;8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+5y=50; 2x+1y=14",
    "options": [
      "A. x=4,y=6",
      "B. x=6,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-10)x + (0) = 0",
    "options": [
      "A. x=10;0",
      "B. x=0;10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-18)x + (45) = 0",
    "options": [
      "A. x=3;15",
      "B. x=15;3",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 10x + 7 ≥ -3",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+1y=16; 5x+5y=40",
    "options": [
      "A. x=2,y=6",
      "B. x=6,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+5y=-2; 5x+5y=0",
    "options": [
      "A. x=2,y=-2",
      "B. x=-2,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-26)x + (160) = 0",
    "options": [
      "A. x=10;16",
      "B. x=16;10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 6x + -9 ≥ -9",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+5y=-60; 1x+1y=-12",
    "options": [
      "A. x=-3,y=-9",
      "B. x=-9,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+1y=2; 1x+4y=-16",
    "options": [
      "A. x=8,y=-6",
      "B. x=-6,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+1y=35; 5x+5y=85",
    "options": [
      "A. x=9,y=8",
      "B. x=8,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+3y=-26; 2x+1y=-12",
    "options": [
      "A. x=-10,y=8",
      "B. x=8,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+5y=100; 1x+1y=20",
    "options": [
      "A. x=10,y=10",
      "B. x=10,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-33)x + (270) = 0",
    "options": [
      "A. x=18;15",
      "B. x=15;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (3)x + (-208) = 0",
    "options": [
      "A. x=-16;13",
      "B. x=13;-16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-17)x + (-38) = 0",
    "options": [
      "A. x=-2;19",
      "B. x=19;-2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-23)x + (126) = 0",
    "options": [
      "A. x=14;9",
      "B. x=9;14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + -18 ≥ -33",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+2y=17; 5x+3y=22",
    "options": [
      "A. x=-1,y=9",
      "B. x=9,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (10)x + (-144) = 0",
    "options": [
      "A. x=8;-18",
      "B. x=-18;8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+2y=30; 4x+3y=54",
    "options": [
      "A. x=9,y=6",
      "B. x=6,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-1)x + (-90) = 0",
    "options": [
      "A. x=-9;10",
      "B. x=10;-9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 2x + -15 ≥ -19",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-26)x + (153) = 0",
    "options": [
      "A. x=9;17",
      "B. x=17;9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+3y=6; 5x+2y=43",
    "options": [
      "A. x=9,y=-1",
      "B. x=-1,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (20)x + (84) = 0",
    "options": [
      "A. x=-6;-14",
      "B. x=-14;-6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + -7 ≥ 29",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 1x + -12 ≥ -9",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+4y=-28; 1x+4y=-16",
    "options": [
      "A. x=-4,y=-3",
      "B. x=-3,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (32)x + (247) = 0",
    "options": [
      "A. x=-19;-13",
      "B. x=-13;-19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 8x + 20 ≥ 4",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+2y=17; 2x+4y=30",
    "options": [
      "A. x=1,y=7",
      "B. x=7,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+1y=2; 1x+5y=-35",
    "options": [
      "A. x=5,y=-8",
      "B. x=-8,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+5y=73; 4x+5y=73",
    "options": [
      "A. x=7,y=9",
      "B. x=9,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (22)x + (85) = 0",
    "options": [
      "A. x=-5;-17",
      "B. x=-17;-5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + 2 ≥ -5",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (9)x + (-112) = 0",
    "options": [
      "A. x=-16;7",
      "B. x=7;-16",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + -17 ≥ -7",
    "options": [
      "A. x ≥ 10",
      "B. x ≤ 10",
      "C. x > 10",
      "D. x < 10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+5y=-25; 5x+2y=-31",
    "options": [
      "A. x=-7,y=2",
      "B. x=2,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + -5 ≥ -12",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+4y=20; 4x+4y=20",
    "options": [
      "A. x=10,y=-5",
      "B. x=-5,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 4x + -13 ≥ 11",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+1y=-26; 3x+2y=-7",
    "options": [
      "A. x=-9,y=10",
      "B. x=10,y=-9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-20)x + (51) = 0",
    "options": [
      "A. x=17;3",
      "B. x=3;17",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+5y=14; 5x+4y=22",
    "options": [
      "A. x=6,y=-2",
      "B. x=-2,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+5y=7; 3x+3y=9",
    "options": [
      "A. x=2,y=1",
      "B. x=1,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-5)x + (-14) = 0",
    "options": [
      "A. x=-2;7",
      "B. x=7;-2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+2y=-14; 2x+4y=20",
    "options": [
      "A. x=-6,y=8",
      "B. x=8,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (22)x + (40) = 0",
    "options": [
      "A. x=-2;-20",
      "B. x=-20;-2",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-2)x + (-15) = 0",
    "options": [
      "A. x=5;-3",
      "B. x=-3;5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+1y=-8; 5x+4y=-32",
    "options": [
      "A. x=0,y=-8",
      "B. x=-8,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+4y=-48; 5x+5y=-85",
    "options": [
      "A. x=-10,y=-7",
      "B. x=-7,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+5y=25; 3x+1y=-5",
    "options": [
      "A. x=-5,y=10",
      "B. x=10,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-7)x + (-120) = 0",
    "options": [
      "A. x=-8;15",
      "B. x=15;-8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+5y=46; 1x+4y=39",
    "options": [
      "A. x=-1,y=10",
      "B. x=10,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (11)x + (-12) = 0",
    "options": [
      "A. x=-12;1",
      "B. x=1;-12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + 7 ≥ 21",
    "options": [
      "A. x ≥ 2",
      "B. x ≤ 2",
      "C. x > 2",
      "D. x < 2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-7)x + (-78) = 0",
    "options": [
      "A. x=13;-6",
      "B. x=-6;13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+3y=5; 5x+3y=5",
    "options": [
      "A. x=7,y=-10",
      "B. x=-10,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+3y=35; 4x+4y=20",
    "options": [
      "A. x=10,y=-5",
      "B. x=-5,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 6x + 9 ≥ -15",
    "options": [
      "A. x ≥ -4",
      "B. x ≤ -4",
      "C. x > -4",
      "D. x < -4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+1y=19; 2x+5y=-13",
    "options": [
      "A. x=6,y=-5",
      "B. x=-5,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + -12 ≥ -6",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 6x + -9 ≥ -51",
    "options": [
      "A. x ≥ -7",
      "B. x ≤ -7",
      "C. x > -7",
      "D. x < -7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + 20 ≥ -4",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=-24; 4x+2y=-24",
    "options": [
      "A. x=-6,y=0",
      "B. x=0,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+3y=10; 2x+4y=16",
    "options": [
      "A. x=-4,y=6",
      "B. x=6,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + 10 ≥ -11",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-22)x + (96) = 0",
    "options": [
      "A. x=6;16",
      "B. x=16;6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+3y=35; 4x+4y=60",
    "options": [
      "A. x=5,y=10",
      "B. x=10,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+5y=15; 1x+1y=-5",
    "options": [
      "A. x=-10,y=5",
      "B. x=5,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 10x + 8 ≥ -92",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (0)x + (-100) = 0",
    "options": [
      "A. x=10;-10",
      "B. x=-10;10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (13)x + (36) = 0",
    "options": [
      "A. x=-4;-9",
      "B. x=-9;-4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 7x + 13 ≥ 62",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-31)x + (220) = 0",
    "options": [
      "A. x=20;11",
      "B. x=11;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 10x + 8 ≥ -22",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + -10 ≥ -60",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+1y=13; 5x+3y=45",
    "options": [
      "A. x=3,y=10",
      "B. x=10,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+2y=-8; 2x+2y=-8",
    "options": [
      "A. x=-2,y=-2",
      "B. x=-2,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (15)x + (50) = 0",
    "options": [
      "A. x=-5;-10",
      "B. x=-10;-5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-31)x + (228) = 0",
    "options": [
      "A. x=19;12",
      "B. x=12;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-209) = 0",
    "options": [
      "A. x=19;-11",
      "B. x=-11;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+4y=-26; 5x+4y=-5",
    "options": [
      "A. x=7,y=-10",
      "B. x=-10,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (5)x + (-14) = 0",
    "options": [
      "A. x=-7;2",
      "B. x=2;-7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+2y=3; 1x+5y=42",
    "options": [
      "A. x=-3,y=9",
      "B. x=9,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-5)x + (-14) = 0",
    "options": [
      "A. x=7;-2",
      "B. x=-2;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+1y=-24; 4x+4y=-48",
    "options": [
      "A. x=-6,y=-6",
      "B. x=-6,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-36)x + (320) = 0",
    "options": [
      "A. x=20;16",
      "B. x=16;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+1y=-9; 3x+5y=-1",
    "options": [
      "A. x=-2,y=1",
      "B. x=1,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+3y=52; 2x+4y=46",
    "options": [
      "A. x=7,y=8",
      "B. x=8,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+2y=-4; 3x+1y=2",
    "options": [
      "A. x=4,y=-10",
      "B. x=-10,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 10x + 3 ≥ -7",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+4y=20; 1x+1y=5",
    "options": [
      "A. x=-2,y=7",
      "B. x=7,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + -16 ≥ -32",
    "options": [
      "A. x ≥ -2",
      "B. x ≤ -2",
      "C. x > -2",
      "D. x < -2"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=-3; 3x+3y=3",
    "options": [
      "A. x=-6,y=7",
      "B. x=7,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+4y=-10; 1x+2y=-4",
    "options": [
      "A. x=-2,y=-1",
      "B. x=-1,y=-2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+4y=32; 1x+1y=8",
    "options": [
      "A. x=-1,y=9",
      "B. x=9,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (31)x + (220) = 0",
    "options": [
      "A. x=-11;-20",
      "B. x=-20;-11",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + -20 ≥ -101",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+4y=-12; 2x+1y=2",
    "options": [
      "A. x=4,y=-6",
      "B. x=-6,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (13)x + (-30) = 0",
    "options": [
      "A. x=-15;2",
      "B. x=2;-15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (-4)x + (-45) = 0",
    "options": [
      "A. x=9;-5",
      "B. x=-5;9",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+4y=-46; 5x+3y=-47",
    "options": [
      "A. x=-10,y=1",
      "B. x=1,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+3y=16; 2x+2y=4",
    "options": [
      "A. x=10,y=-8",
      "B. x=-8,y=10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 3x + 4 ≥ 16",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+2y=-24; 5x+4y=-36",
    "options": [
      "A. x=-4,y=-4",
      "B. x=-4,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+5y=0; 5x+1y=-40",
    "options": [
      "A. x=-10,y=10",
      "B. x=10,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+2y=-70; 5x+2y=-70",
    "options": [
      "A. x=-10,y=-10",
      "B. x=-10,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 1x+5y=4; 4x+3y=-1",
    "options": [
      "A. x=-1,y=1",
      "B. x=1,y=-1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-18)x + (72) = 0",
    "options": [
      "A. x=6;12",
      "B. x=12;6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (11)x + (24) = 0",
    "options": [
      "A. x=-8;-3",
      "B. x=-3;-8",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (7)x + (-228) = 0",
    "options": [
      "A. x=12;-19",
      "B. x=-19;12",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+1y=-22; 2x+2y=-4",
    "options": [
      "A. x=-10,y=8",
      "B. x=8,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+2y=31; 2x+1y=13",
    "options": [
      "A. x=5,y=3",
      "B. x=3,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + 7 ≥ 47",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-11)x + (-152) = 0",
    "options": [
      "A. x=19;-8",
      "B. x=-8;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+4y=-12; 3x+5y=-7",
    "options": [
      "A. x=-4,y=1",
      "B. x=1,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+3y=29; 4x+1y=12",
    "options": [
      "A. x=1,y=8",
      "B. x=8,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-4)x + (3) = 0",
    "options": [
      "A. x=3;1",
      "B. x=1;3",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+2y=33; 3x+4y=17",
    "options": [
      "A. x=7,y=-1",
      "B. x=-1,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (15)x + (50) = 0",
    "options": [
      "A. x=-10;-5",
      "B. x=-5;-10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (21)x + (104) = 0",
    "options": [
      "A. x=-13;-8",
      "B. x=-8;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+2y=12; 1x+3y=11",
    "options": [
      "A. x=2,y=3",
      "B. x=3,y=2",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+3y=-9; 3x+5y=7",
    "options": [
      "A. x=-6,y=5",
      "B. x=5,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+3y=0; 1x+3y=-16",
    "options": [
      "A. x=8,y=-8",
      "B. x=-8,y=8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 3x+2y=-16; 2x+3y=-4",
    "options": [
      "A. x=-8,y=4",
      "B. x=4,y=-8",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-33)x + (260) = 0",
    "options": [
      "A. x=13;20",
      "B. x=20;13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 3x+1y=-21; 3x+3y=-21",
    "options": [
      "A. x=-7,y=0",
      "B. x=0,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 4x+5y=25; 2x+3y=13",
    "options": [
      "A. x=5,y=1",
      "B. x=1,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+2y=6; 4x+4y=12",
    "options": [
      "A. x=-6,y=9",
      "B. x=9,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + -3 ≥ -8",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 12 ≥ 52",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+3y=-50; 2x+1y=-20",
    "options": [
      "A. x=-5,y=-10",
      "B. x=-10,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (0)x + (-324) = 0",
    "options": [
      "A. x=18;-18",
      "B. x=-18;18",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + -9 ≥ -5",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + -9 ≥ -63",
    "options": [
      "A. x ≥ -6",
      "B. x ≤ -6",
      "C. x > -6",
      "D. x < -6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + -16 ≥ -16",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (8)x + (-105) = 0",
    "options": [
      "A. x=-15;7",
      "B. x=7;-15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (11)x + (-80) = 0",
    "options": [
      "A. x=5;-16",
      "B. x=-16;5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 8x + 2 ≥ -22",
    "options": [
      "A. x ≥ -3",
      "B. x ≤ -3",
      "C. x > -3",
      "D. x < -3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+4y=-44; 1x+3y=-13",
    "options": [
      "A. x=-10,y=-1",
      "B. x=-1,y=-10",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 5x+4y=59; 1x+2y=19",
    "options": [
      "A. x=7,y=6",
      "B. x=6,y=7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 6x + -19 ≥ -67",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 15 ≥ 85",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+3y=-9; 3x+4y=-13",
    "options": [
      "A. x=1,y=-4",
      "B. x=-4,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-7)x + (6) = 0",
    "options": [
      "A. x=1;6",
      "B. x=6;1",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 1x+5y=10; 3x+5y=20",
    "options": [
      "A. x=5,y=1",
      "B. x=1,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + 12 ≥ -78",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+1y=39; 2x+5y=33",
    "options": [
      "A. x=9,y=3",
      "B. x=3,y=9",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + 13 ≥ 13",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-14)x + (40) = 0",
    "options": [
      "A. x=10;4",
      "B. x=4;10",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + 0 ≥ -30",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 9x + 5 ≥ -67",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 1x+4y=-36; 1x+1y=-6",
    "options": [
      "A. x=4,y=-10",
      "B. x=-10,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 7x + -8 ≥ 20",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-23)x + (130) = 0",
    "options": [
      "A. x=13;10",
      "B. x=10;13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (7)x + (-260) = 0",
    "options": [
      "A. x=13;-20",
      "B. x=-20;13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (8)x + (-84) = 0",
    "options": [
      "A. x=6;-14",
      "B. x=-14;6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+5y=-3; 1x+3y=-1",
    "options": [
      "A. x=-4,y=1",
      "B. x=1,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 10x + -6 ≥ 64",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 6x + -4 ≥ -52",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + -18 ≥ -48",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+5y=45; 4x+4y=48",
    "options": [
      "A. x=5,y=7",
      "B. x=7,y=5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (24)x + (80) = 0",
    "options": [
      "A. x=-20;-4",
      "B. x=-4;-20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 2x + 10 ≥ 18",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+4y=13; 4x+2y=8",
    "options": [
      "A. x=1,y=2",
      "B. x=2,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-17)x + (52) = 0",
    "options": [
      "A. x=4;13",
      "B. x=13;4",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (14)x + (0) = 0",
    "options": [
      "A. x=-14;0",
      "B. x=0;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 4x+1y=32; 4x+3y=48",
    "options": [
      "A. x=6,y=8",
      "B. x=8,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + -15 ≥ 39",
    "options": [
      "A. x ≥ 6",
      "B. x ≤ 6",
      "C. x > 6",
      "D. x < 6"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + 14 ≥ 84",
    "options": [
      "A. x ≥ 7",
      "B. x ≤ 7",
      "C. x > 7",
      "D. x < 7"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-19)x + (0) = 0",
    "options": [
      "A. x=19;0",
      "B. x=0;19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + -18 ≥ -18",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (-18)x + (0) = 0",
    "options": [
      "A. x=0;18",
      "B. x=18;0",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+2y=-36; 3x+2y=-24",
    "options": [
      "A. x=-6,y=-3",
      "B. x=-3,y=-6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + 20 ≥ 38",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+3y=15; 2x+3y=14",
    "options": [
      "A. x=1,y=4",
      "B. x=4,y=1",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-8)x + (-105) = 0",
    "options": [
      "A. x=-7;15",
      "B. x=15;-7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 9x + -16 ≥ 11",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+4y=-45; 2x+5y=-44",
    "options": [
      "A. x=-7,y=-6",
      "B. x=-6,y=-7",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 1x + -13 ≥ -21",
    "options": [
      "A. x ≥ -8",
      "B. x ≤ -8",
      "C. x > -8",
      "D. x < -8"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (0)x + (-25) = 0",
    "options": [
      "A. x=5;-5",
      "B. x=-5;5",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 2x+5y=3; 3x+3y=9",
    "options": [
      "A. x=4,y=-1",
      "B. x=-1,y=4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-25)x + (126) = 0",
    "options": [
      "A. x=7;18",
      "B. x=18;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + 16 ≥ 43",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+1y=-4; 4x+3y=8",
    "options": [
      "A. x=-4,y=8",
      "B. x=8,y=-4",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 9x + -19 ≥ 62",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 7x + -12 ≥ 23",
    "options": [
      "A. x ≥ 5",
      "B. x ≤ 5",
      "C. x > 5",
      "D. x < 5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 4x+5y=-2; 1x+5y=7",
    "options": [
      "A. x=-3,y=2",
      "B. x=2,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-7)x + (-78) = 0",
    "options": [
      "A. x=13;-6",
      "B. x=-6;13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 5x + 10 ≥ 15",
    "options": [
      "A. x ≥ 1",
      "B. x ≤ 1",
      "C. x > 1",
      "D. x < 1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (30)x + (221) = 0",
    "options": [
      "A. x=-13;-17",
      "B. x=-17;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+1y=22; 1x+5y=38",
    "options": [
      "A. x=3,y=7",
      "B. x=7,y=3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải hệ: 2x+2y=28; 4x+5y=64",
    "options": [
      "A. x=6,y=8",
      "B. x=8,y=6",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 2x + -5 ≥ 1",
    "options": [
      "A. x ≥ 3",
      "B. x ≤ 3",
      "C. x > 3",
      "D. x < 3"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 10x + -18 ≥ -68",
    "options": [
      "A. x ≥ -5",
      "B. x ≤ -5",
      "C. x > -5",
      "D. x < -5"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 2x+3y=-30; 4x+5y=-52",
    "options": [
      "A. x=-3,y=-8",
      "B. x=-8,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 8x + -10 ≥ -18",
    "options": [
      "A. x ≥ -1",
      "B. x ≤ -1",
      "C. x > -1",
      "D. x < -1"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải bất phương trình: 3x + 15 ≥ 27",
    "options": [
      "A. x ≥ 4",
      "B. x ≤ 4",
      "C. x > 4",
      "D. x < 4"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 5x+2y=-15; 2x+1y=-5",
    "options": [
      "A. x=-5,y=5",
      "B. x=5,y=-5",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-13)x + (42) = 0",
    "options": [
      "A. x=7;6",
      "B. x=6;7",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 3x + -10 ≥ -40",
    "options": [
      "A. x ≥ -10",
      "B. x ≤ -10",
      "C. x > -10",
      "D. x < -10"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (34)x + (285) = 0",
    "options": [
      "A. x=-19;-15",
      "B. x=-15;-19",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (31)x + (240) = 0",
    "options": [
      "A. x=-15;-16",
      "B. x=-16;-15",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + -9 ≥ 0",
    "options": [
      "A. x ≥ 9",
      "B. x ≤ 9",
      "C. x > 9",
      "D. x < 9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (9)x + (-90) = 0",
    "options": [
      "A. x=6;-15",
      "B. x=-15;6",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải bất phương trình: 1x + 13 ≥ 13",
    "options": [
      "A. x ≥ 0",
      "B. x ≤ 0",
      "C. x > 0",
      "D. x < 0"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải phương trình: x² + (5)x + (-126) = 0",
    "options": [
      "A. x=-14;9",
      "B. x=9;-14",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải phương trình: x² + (4)x + (-117) = 0",
    "options": [
      "A. x=-13;9",
      "B. x=9;-13",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  },
  {
    "question": "Giải hệ: 5x+1y=1; 3x+1y=1",
    "options": [
      "A. x=0,y=1",
      "B. x=1,y=0",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải bất phương trình: 10x + 17 ≥ -73",
    "options": [
      "A. x ≥ -9",
      "B. x ≤ -9",
      "C. x > -9",
      "D. x < -9"
    ],
    "answer": "A",
    "explanation": "Chuyển vế và chia hệ số dương."
  },
  {
    "question": "Giải hệ: 3x+4y=-49; 4x+5y=-62",
    "options": [
      "A. x=-3,y=-10",
      "B. x=-10,y=-3",
      "C. Vô nghiệm",
      "D. Vô số nghiệm"
    ],
    "answer": "A",
    "explanation": "Giải bằng phương pháp thế hoặc cộng đại số."
  },
  {
    "question": "Giải phương trình: x² + (-9)x + (-220) = 0",
    "options": [
      "A. x=20;-11",
      "B. x=-11;20",
      "C. Vô nghiệm",
      "D. Có nghiệm kép"
    ],
    "answer": "A",
    "explanation": "Áp dụng định lý Viète."
  }
]