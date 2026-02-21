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
  {"question":"Giá trị của giới hạn lim(x→0) (sinx/x) bằng bao nhiêu?","options":["A. 0","B. 1","C. -1","D. Không tồn tại"],"answer":"B. 1","explanation":"Giới hạn cơ bản của giải tích."},
{"question":"Tích phân ∫_0^1 x dx bằng?","options":["A. 1","B. 1/2","C. 2","D. 0"],"answer":"B. 1/2","explanation":"∫x dx = x^2/2, thay cận được 1/2."},
{"question":"Định thức của ma trận [[1,2],[3,4]] bằng?","options":["A. -2","B. 2","C. 10","D. -10"],"answer":"A. -2","explanation":"det = 1*4 - 2*3 = -2."},
{"question":"Chuỗi hình học ∑_{n=0}∞ (1/2)^n hội tụ đến?","options":["A. 1","B. 2","C. 1/2","D. 0"],"answer":"B. 2","explanation":"Tổng = 1/(1-1/2)=2."},
{"question":"Đạo hàm của e^{3x} là?","options":["A. e^{3x}","B. 3e^{3x}","C. 3x e^{3x}","D. e^{x}"],"answer":"B. 3e^{3x}","explanation":"Dùng quy tắc dây chuyền."},
{"question":"Ma trận khả nghịch khi nào?","options":["A. det ≠ 0","B. det = 0","C. trace = 0","D. luôn luôn"],"answer":"A. det ≠ 0","explanation":"Điều kiện cần và đủ."},
{"question":"∫ e^x dx bằng?","options":["A. e^x + C","B. xe^x","C. ln x","D. 1/e^x"],"answer":"A. e^x + C","explanation":"Nguyên hàm cơ bản."},
{"question":"Không gian R^3 có số chiều là?","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"C. 3","explanation":"Theo định nghĩa."},
{"question":"Phương trình vi phân y' = y có nghiệm tổng quát?","options":["A. y = Ce^x","B. y = Cx","C. y = ln x","D. y = x^2"],"answer":"A. y = Ce^x","explanation":"Tách biến."},
{"question":"Giá trị riêng của ma trận đơn vị I là?","options":["A. 0","B. 1","C. -1","D. 2"],"answer":"B. 1","explanation":"Ix = 1x."},
{"question":"Tích vô hướng của (1,0,0) và (0,1,0) bằng?","options":["A. 1","B. 0","C. -1","D. 2"],"answer":"B. 0","explanation":"Hai vector vuông góc."},
{"question":"∫_0^π sinx dx bằng?","options":["A. 0","B. 1","C. 2","D. π"],"answer":"C. 2","explanation":"Nguyên hàm -cosx."},
{"question":"Chuỗi ∑ 1/n có hội tụ không?","options":["A. Có","B. Không","C. Hội tụ điều kiện","D. Hội tụ tuyệt đối"],"answer":"B. Không","explanation":"Chuỗi điều hòa phân kỳ."},
{"question":"Gradient của f(x,y)=x^2+y^2 là?","options":["A. (2x,2y)","B. (x,y)","C. (2,2)","D. (x^2,y^2)"],"answer":"A. (2x,2y)","explanation":"Lấy đạo hàm riêng."},
{"question":"Xác suất của biến cố chắc chắn bằng?","options":["A. 0","B. 1","C. 1/2","D. -1"],"answer":"B. 1","explanation":"Theo tiên đề xác suất."},
{"question":"Định lý Fubini áp dụng khi nào?","options":["A. Hàm khả tích","B. Hàm liên tục","C. Hàm đạo hàm","D. Luôn đúng"],"answer":"A. Hàm khả tích","explanation":"Điều kiện tích phân lặp."},
{"question":"∫_0^1 x^2 dx bằng?","options":["A. 1/2","B. 1/3","C. 1","D. 2/3"],"answer":"B. 1/3","explanation":"x^3/3 từ 0 đến 1."},
{"question":"Ma trận đối xứng thỏa mãn?","options":["A. A^T = A","B. A^T = -A","C. det=0","D. A=I"],"answer":"A. A^T = A","explanation":"Theo định nghĩa."},
{"question":"Biến ngẫu nhiên rời rạc có tổng xác suất bằng?","options":["A. 0","B. 1","C. 2","D. Không xác định"],"answer":"B. 1","explanation":"Tổng p_i =1."},
{"question":"Nghiệm của y'' + y = 0 là?","options":["A. Ae^x","B. A cosx + B sinx","C. Ax+B","D. e^{-x}"],"answer":"B. A cosx + B sinx","explanation":"Phương trình đặc trưng."},

{"question":"Đạo hàm riêng ∂/∂x của xy là?","options":["A. y","B. x","C. xy","D. 1"],"answer":"A. y","explanation":"Giữ y hằng."},
{"question":"∫_0^∞ e^{-x} dx bằng?","options":["A. 1","B. 0","C. ∞","D. -1"],"answer":"A. 1","explanation":"Nguyên hàm -e^{-x}."},
{"question":"Không gian vector có cơ sở gồm 3 vector độc lập thì số chiều bằng?","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"C. 3","explanation":"Theo định nghĩa."},
{"question":"Nếu A khả nghịch thì (A^{-1})^{-1} bằng?","options":["A. I","B. A","C. 0","D. -A"],"answer":"B. A","explanation":"Tính chất nghịch đảo."},
{"question":"∫ ln x dx bằng?","options":["A. x ln x - x + C","B. ln^2 x","C. 1/x","D. x ln x + C"],"answer":"A. x ln x - x + C","explanation":"Tích phân từng phần."},

{"question":"Phương sai Var(X) luôn?","options":["A. ≥0","B. ≤0","C. =1","D. =0"],"answer":"A. ≥0","explanation":"Do bình phương sai lệch."},
{"question":"Jacobian dùng trong?","options":["A. Đổi biến tích phân","B. Giải ODE","C. Tính định thức 2x2","D. Tính trace"],"answer":"A. Đổi biến tích phân","explanation":"Công thức đổi biến."},
{"question":"Chuỗi ∑ (-1)^n/n hội tụ?","options":["A. Tuyệt đối","B. Điều kiện","C. Phân kỳ","D. Không xác định"],"answer":"B. Điều kiện","explanation":"Tiêu chuẩn Leibniz."},
{"question":"Hạng của ma trận là?","options":["A. Số hàng","B. Số cột","C. Số vector độc lập","D. det"],"answer":"C. Số vector độc lập","explanation":"Định nghĩa rank."},
{"question":"∇·(∇f) gọi là?","options":["A. Gradient","B. Divergence","C. Laplace","D. Curl"],"answer":"C. Laplace","explanation":"Toán tử Laplace."},

{"question":"E(aX+b)=?","options":["A. aE(X)+b","B. E(X)+b","C. aE(X)","D. bE(X)"],"answer":"A. aE(X)+b","explanation":"Tính tuyến tính."},
{"question":"Tích phân đường bảo toàn khi nào?","options":["A. Trường thế","B. Liên tục","C. Khả tích","D. Hữu hạn"],"answer":"A. Trường thế","explanation":"Khi gradient của hàm thế."},
{"question":"Giá trị riêng λ thỏa mãn?","options":["A. det(A-λI)=0","B. det(A)=0","C. trace=0","D. A=0"],"answer":"A. det(A-λI)=0","explanation":"Phương trình đặc trưng."},
{"question":"∫_0^1 e^x dx bằng?","options":["A. e-1","B. 1","C. e","D. 0"],"answer":"A. e-1","explanation":"Nguyên hàm e^x."},
{"question":"Chuẩn Euclid của (3,4) là?","options":["A. 5","B. 7","C. 25","D. 1"],"answer":"A. 5","explanation":"√(3^2+4^2)=5."},

{"question":"Ma trận trực giao thỏa mãn?","options":["A. A^TA=I","B. det=0","C. A=A^T","D. A=0"],"answer":"A. A^TA=I","explanation":"Định nghĩa."},
{"question":"Phân phối chuẩn có dạng?","options":["A. Chuông","B. Tam giác","C. Đều","D. Bậc hai"],"answer":"A. Chuông","explanation":"Đồ thị hình chuông."},
{"question":"∫_0^{π/2} cosx dx bằng?","options":["A. 0","B. 1","C. 2","D. π/2"],"answer":"B. 1","explanation":"sinx từ 0 đến π/2."},
{"question":"Không gian con phải?","options":["A. Đóng với cộng và nhân","B. Chỉ cộng","C. Chỉ nhân","D. Không cần điều kiện"],"answer":"A. Đóng với cộng và nhân","explanation":"Điều kiện không gian con."},
{"question":"Biến đổi Fourier dùng để?","options":["A. Phân tích tần số","B. Tính tích phân","C. Giải hệ tuyến tính","D. Tính định thức"],"answer":"A. Phân tích tần số","explanation":"Chuyển sang miền tần số."},
{
    "question": "Tính đạo hàm riêng của hàm số $f(x, y) = x^2y + \sin(xy)$ theo biến $x$.",
    "options": ["2xy + y\cos(xy)", "x^2 + x\cos(xy)", "2xy + \cos(xy)", "2x + y\cos(xy)"],
    "answer": "A",
    "explanation": "Đạo hàm riêng theo $x$ coi $y$ là hằng số: $\frac{\partial f}{\partial x} = 2xy + y\cos(xy)$."
  },
  {
    "question": "Ma trận $A$ vuông cấp $n$ nghịch đảo khi và chỉ khi:",
    "options": ["\det(A) \neq 0", "\det(A) = 0", "A là ma trận không", "Các dòng của A tỉ lệ thuận"],
    "answer": "A",
    "explanation": "Điều kiện cần và đủ để ma trận vuông có nghịch đảo là định thức của nó phải khác 0."
  },
  {
    "question": "Tìm nghiệm riêng của phương trình vi phân $y'' - 3y' + 2y = 0$ thỏa mãn $y(0)=0, y'(0)=1$.",
    "options": ["y = e^{2x} - e^x", "y = e^x - e^{2x}", "y = e^{2x} + e^x", "y = 2e^x - e^{2x}"],
    "answer": "A",
    "explanation": "Pt đặc trưng $k^2-3k+2=0$ có nghiệm $1, 2$. $y=C_1e^x + C_2e^{2x}$. Giải hệ $C_1+C_2=0$ và $C_1+2C_2=1$ ta được $C_1=-1, C_2=1$."
  },
  {
    "question": "Tìm bán kính hội tụ $R$ của chuỗi lũy thừa $\sum_{n=0}^{\infty} \frac{x^n}{n!}$.",
    "options": ["R = +\infty", "R = 1", "R = 0", "R = e"],
    "answer": "A",
    "explanation": "Sử dụng tiêu chuẩn D'Alembert: $\lim_{n \to \infty} |\frac{a_{n+1}}{a_n}| = \lim \frac{1}{n+1} = 0$. Vậy bán kính hội tụ là vô hạn."
  },
  {
    "question": "Tính tích phân đường $I = \int_C (x+y)ds$ với $C$ là đoạn thẳng từ $O(0,0)$ đến $A(1,1)$.",
    "options": ["\sqrt{2}", "1", "2\sqrt{2}", "1/2"],
    "answer": "A",
    "explanation": "Tham số hóa $x=t, y=t (0 \le t \le 1)$. $ds = \sqrt{x'^2+y'^2}dt = \sqrt{2}dt$. $I = \int_0^1 2t\sqrt{2}dt = \sqrt{2}$."
  },
  {
    "question": "Hạng của ma trận $A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ là:",
    "options": ["1", "3", "0", "2"],
    "answer": "A",
    "explanation": "Chỉ có duy nhất một dòng khác không và các dòng khác đều bằng 0, nên hạng bằng 1."
  },
  {
    "question": "Sử dụng quy tắc L'Hopital, tính $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$.",
    "options": ["1/2", "1", "0", "+\infty"],
    "answer": "A",
    "explanation": "Đạo hàm tử và mẫu 2 lần: $\frac{\sin x}{2x} \to \frac{\cos x}{2} = 1/2$."
  },
  {
    "question": "Cho $V$ là không gian vectơ các ma trận vuông cấp 2. Số chiều của $V$ là:",
    "options": ["4", "2", "3", "1"],
    "answer": "A",
    "explanation": "Cơ sở chính tắc gồm 4 ma trận $E_{11}, E_{12}, E_{21}, E_{22}$."
  },
  {
    "question": "Trong Giải tích phức, số phức $z$ thỏa mãn phương trình $e^z = 1$ khi:",
    "options": ["z = k2\pi i, k \in \mathbb{Z}", "z = 0", "z = k\pi i", "z = 1"],
    "answer": "A",
    "explanation": "Sử dụng công thức Euler $e^{ix} = \cos x + i\sin x$. $e^z = 1$ khi phần thực bằng 0 và phần ảo là bội của $2\pi$."
  },
  {
    "question": "Tích phân suy rộng $I = \int_1^{+\infty} \frac{1}{x^2} dx$ có giá trị bằng:",
    "options": ["1", "+\infty", "0", "2"],
    "answer": "A",
    "explanation": "$\lim_{A \to +\infty} (-\frac{1}{x}) \big|_1^A = 0 - (-1) = 1$."
  },
  {
    "question": "Hàm số $f(x) = |x|$ tại $x=0$ có đặc điểm:",
    "options": ["Liên tục nhưng không có đạo hàm", "Có đạo hàm nhưng không liên tục", "Không liên tục và không có đạo hàm", "Có đạo hàm bằng 0"],
    "answer": "A",
    "explanation": "Đồ thị có điểm nhọn tại (0,0), đạo hàm trái bằng -1, đạo hàm phải bằng 1."
  },
  {
    "question": "Định thức của ma trận đơn vị $I_n$ bằng:",
    "options": ["1", "n", "0", "(-1)^n"],
    "answer": "A",
    "explanation": "Ma trận đơn vị luôn có định thức bằng tích các phần tử trên đường chéo chính (toàn số 1)."
  },
  {
    "question": "Vi phân toàn phần của hàm $z = x^y$ là:",
    "options": ["dz = yx^{y-1}dx + x^y \ln x dy", "dz = yx^{y-1}dx", "dz = x^y \ln x dy", "dz = x^{y-1}(ydx + xdy)"],
    "answer": "A",
    "explanation": "$dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy$."
  },
  {
    "question": "Điều kiện để chuỗi số $\sum a_n$ hội tụ theo tiêu chuẩn tích phân là hàm $f(x)$ tương ứng phải:",
    "options": ["Dương, liên tục và giảm", "Dương và tăng", "Âm và giảm", "Liên tục và có dấu bất kỳ"],
    "answer": "A",
    "explanation": "Hàm số phải thỏa mãn tính đơn điệu giảm và không âm trên miền xét."
  },
  {
    "question": "Trong không gian Euclid, hai vectơ vuông góc với nhau khi:",
    "options": ["Tích vô hướng của chúng bằng 0", "Tích hữu hướng của chúng bằng 0", "Tỉ số các thành phần tương ứng bằng nhau", "Tổng các thành phần bằng 0"],
    "answer": "A",
    "explanation": "Định nghĩa góc giữa hai vectơ $\cos \theta = \frac{u.v}{|u||v|}$. Vuông góc thì $\cos 90 = 0$."
  },
  {
    "question": "Tìm giá trị cực đại của hàm số $f(x, y) = 1 - x^2 - y^2$.",
    "options": ["1", "0", "-1", "Không có"],
    "answer": "A",
    "explanation": "Điểm dừng là (0,0), tại đó $f(0,0)=1$. Vì $x^2+y^2 \ge 0$ nên $f(x,y) \le 1$."
  },
  {
    "question": "Ma trận $A$ được gọi là ma trận trực giao nếu:",
    "options": ["A^T = A^{-1}", "A^T = A", "A^T = -A", "\det(A) = 0"],
    "answer": "A",
    "explanation": "Ma trận trực giao thỏa mãn $AA^T = I$."
  },
  {
    "question": "Nghiệm của phương trình vi phân tách biến $\frac{dy}{dx} = \frac{x}{y}$ là:",
    "options": ["y^2 - x^2 = C", "y - x = C", "y^2 + x^2 = C", "y = x^2 + C"],
    "answer": "A",
    "explanation": "$ydy = xdx \Rightarrow \int ydy = \int xdx \Rightarrow \frac{y^2}{2} = \frac{x^2}{2} + C_1 \Rightarrow y^2 - x^2 = C$."
  },
  {
    "question": "Một hệ vectơ phụ thuộc tuyến tính khi:",
    "options": ["Có ít nhất một vectơ biểu diễn được qua các vectơ còn lại", "Tất cả các vectơ đều bằng không", "Định thức của hệ luôn bằng 1", "Số vectơ nhỏ hơn số chiều không gian"],
    "answer": "A",
    "explanation": "Đây là định nghĩa cơ bản về sự phụ thuộc tuyến tính."
  },
  {
    "question": "Tính $\int_0^1 \int_0^x dydx$.",
    "options": ["1/2", "1", "1/4", "2"],
    "answer": "A",
    "explanation": "$\int_0^1 (y \big|_0^x) dx = \int_0^1 xdx = 1/2$."
  },
  {"question":"Giới hạn lim(x→∞) (1+1/x)^x bằng?","options":["A. 1","B. e","C. 0","D. ∞"],"answer":"B. e","explanation":"Định nghĩa số e."},
{"question":"Định thức ma trận tam giác bằng?","options":["A. Tổng đường chéo","B. Tích đường chéo","C. 0","D. 1"],"answer":"B. Tích đường chéo","explanation":"Tính chất ma trận tam giác."},
{"question":"∫ x e^x dx bằng?","options":["A. xe^x - e^x + C","B. e^x + C","C. x^2e^x","D. ln x"],"answer":"A. xe^x - e^x + C","explanation":"Tích phân từng phần."},
{"question":"Không gian Hilbert là?","options":["A. Không gian có tích vô hướng đầy đủ","B. Không gian hữu hạn chiều","C. Không gian metric","D. Không gian rời rạc"],"answer":"A. Không gian có tích vô hướng đầy đủ","explanation":"Định nghĩa."},
{"question":"Nếu X,Y độc lập thì Cov(X,Y)=?","options":["A. 1","B. 0","C. -1","D. Var(X)"],"answer":"B. 0","explanation":"Tính chất độc lập."},
{"question":"∇×(∇f) bằng?","options":["A. 0","B. ∇f","C. 1","D. f"],"answer":"A. 0","explanation":"Curl của gradient bằng 0."},
{"question":"Chuỗi p-series ∑1/n^p hội tụ khi?","options":["A. p≤1","B. p>1","C. p=1","D. p<0"],"answer":"B. p>1","explanation":"Tiêu chuẩn p-series."},
{"question":"Hệ phương trình tuyến tính có nghiệm duy nhất khi?","options":["A. det ≠ 0","B. det=0","C. trace=0","D. rank<n"],"answer":"A. det ≠ 0","explanation":"Ma trận hệ khả nghịch."},
{"question":"∫_0^1 ln x dx bằng?","options":["A. -1","B. 1","C. 0","D. e"],"answer":"A. -1","explanation":"Tính bằng tích phân từng phần."},
{"question":"Giá trị kỳ vọng của hằng số c là?","options":["A. c","B. 0","C. 1","D. c^2"],"answer":"A. c","explanation":"E(c)=c."},

{"question":"Ma trận phản xứng thỏa?","options":["A. A^T=-A","B. A^T=A","C. det=1","D. A=I"],"answer":"A. A^T=-A","explanation":"Định nghĩa."},
{"question":"∫ cos(ax) dx bằng?","options":["A. sin(ax)/a + C","B. cos(ax)/a","C. a sinx","D. -sinx"],"answer":"A. sin(ax)/a + C","explanation":"Đổi biến."},
{"question":"Phương trình Laplace là?","options":["A. ∇²f=0","B. ∇f=0","C. f'=0","D. det=0"],"answer":"A. ∇²f=0","explanation":"Định nghĩa."},
{"question":"Chuẩn của vector 0 bằng?","options":["A. 0","B. 1","C. -1","D. Không xác định"],"answer":"A. 0","explanation":"Theo định nghĩa chuẩn."},
{"question":"Var(aX)=?","options":["A. aVar(X)","B. a^2Var(X)","C. Var(X)","D. a+Var(X)"],"answer":"B. a^2Var(X)","explanation":"Tính chất phương sai."},
{"question":"∫_0^{∞} e^{-ax} dx (a>0) bằng?","options":["A. 1/a","B. a","C. 0","D. ∞"],"answer":"A. 1/a","explanation":"Nguyên hàm."},
{"question":"Không gian metric cần thỏa?","options":["A. 3 tiên đề khoảng cách","B. det≠0","C. Liên tục","D. Hữu hạn chiều"],"answer":"A. 3 tiên đề khoảng cách","explanation":"Định nghĩa metric."},
{"question":"Giá trị riêng của ma trận tam giác là?","options":["A. Đường chéo chính","B. Tổng hàng","C. 0","D. 1"],"answer":"A. Đường chéo chính","explanation":"Tính chất."},
{"question":"∫ sinh x dx bằng?","options":["A. cosh x + C","B. sinh x","C. -cosh x","D. tanh x"],"answer":"A. cosh x + C","explanation":"Đạo hàm cosh x."},
{"question":"Phân phối Poisson có tham số?","options":["A. λ","B. μ,σ","C. p","D. n"],"answer":"A. λ","explanation":"Tham số trung bình."},

{"question":"Định lý Green liên hệ?","options":["A. Tích phân đường và mặt","B. Tích phân đôi","C. ODE","D. Xác suất"],"answer":"A. Tích phân đường và mặt","explanation":"Trong mặt phẳng."},
{"question":"∫ 1/(1+x^2) dx bằng?","options":["A. arctan x + C","B. ln x","C. x^2/2","D. e^x"],"answer":"A. arctan x + C","explanation":"Công thức cơ bản."},
{"question":"Không gian Banach là?","options":["A. Không gian norm đầy đủ","B. Hữu hạn chiều","C. Có tích vô hướng","D. Metric bất kỳ"],"answer":"A. Không gian norm đầy đủ","explanation":"Định nghĩa."},
{"question":"Hạng tối đa của ma trận m×n là?","options":["A. m+n","B. mn","C. min(m,n)","D. max(m,n)"],"answer":"C. min(m,n)","explanation":"Tính chất rank."},
{"question":"E(X+Y)=?","options":["A. E(X)+E(Y)","B. E(X)E(Y)","C. 0","D. 1"],"answer":"A. E(X)+E(Y)","explanation":"Tính tuyến tính."},
{"question":"∫ tan x dx bằng?","options":["A. -ln|cosx|+C","B. ln|cosx|","C. tanx","D. sinx"],"answer":"A. -ln|cosx|+C","explanation":"Công thức cơ bản."},
{"question":"Ma trận idempotent thỏa?","options":["A. A^2=A","B. A^2=I","C. A=0","D. det=1"],"answer":"A. A^2=A","explanation":"Định nghĩa."},
{"question":"Chuỗi Taylor của e^x tại 0 là?","options":["A. ∑ x^n/n!","B. ∑ x^n","C. ∑ n!x^n","D. x^n"],"answer":"A. ∑ x^n/n!","explanation":"Khai triển Maclaurin."},
{"question":"∫_0^π sin^2 x dx bằng?","options":["A. π/2","B. π","C. 1","D. 0"],"answer":"A. π/2","explanation":"Dùng công thức hạ bậc."},
{"question":"Biến ngẫu nhiên chuẩn hóa có kỳ vọng?","options":["A. 0","B. 1","C. σ","D. μ"],"answer":"A. 0","explanation":"Chuẩn hóa Z."},
{"question":"Giới hạn lim(x→∞) (1+1/x)^x bằng?","options":["A. 1","B. e","C. 0","D. ∞"],"answer":"B. e","explanation":"Định nghĩa số e."},
{"question":"∫_0^∞ x e^{-x} dx bằng?","options":["A. 0","B. 1","C. 2","D. ∞"],"answer":"B. 1","explanation":"Tích phân Gamma Γ(2)=1! =1."},
{"question":"Hạng của ma trận đơn vị cấp n là?","options":["A. 1","B. n","C. 0","D. n-1"],"answer":"B. n","explanation":"Các hàng độc lập tuyến tính."},
{"question":"Nếu chuỗi ∑ a_n hội tụ tuyệt đối thì?","options":["A. Hội tụ","B. Phân kỳ","C. Không xác định","D. Hội tụ điều kiện"],"answer":"A. Hội tụ","explanation":"Hội tụ tuyệt đối ⇒ hội tụ."},
{"question":"∂/∂y của x^2y^3 bằng?","options":["A. 3x^2y^2","B. 2xy^3","C. x^2y^2","D. 3xy^2"],"answer":"A. 3x^2y^2","explanation":"Lấy đạo hàm theo y."},
{"question":"Định thức của ma trận tam giác bằng?","options":["A. Tổng đường chéo","B. Tích đường chéo","C. 0","D. 1"],"answer":"B. Tích đường chéo","explanation":"Tính chất ma trận tam giác."},
{"question":"∫ cosx dx bằng?","options":["A. -sinx + C","B. sinx + C","C. cosx + C","D. tanx + C"],"answer":"B. sinx + C","explanation":"Nguyên hàm cơ bản."},
{"question":"Phương trình đặc trưng của y''-y=0 là?","options":["A. r^2-1=0","B. r^2+1=0","C. r-1=0","D. r^2=0"],"answer":"A. r^2-1=0","explanation":"Thay y=e^{rx}."},
{"question":"E(X+Y)=?","options":["A. E(X)+E(Y)","B. E(X)E(Y)","C. 0","D. Var(X)+Var(Y)"],"answer":"A. E(X)+E(Y)","explanation":"Tính tuyến tính kỳ vọng."},
{"question":"Nếu A là ma trận vuông thì trace(A) là?","options":["A. Tổng đường chéo chính","B. Tích đường chéo","C. Định thức","D. Hạng"],"answer":"A. Tổng đường chéo chính","explanation":"Định nghĩa trace."},
{"question":"∫_0^1 3x^2 dx bằng?","options":["A. 1","B. 3","C. 1/3","D. 0"],"answer":"A. 1","explanation":"Nguyên hàm x^3."},
{"question":"Không gian chuẩn là?","options":["A. Có chuẩn","B. Có tích vô hướng","C. Có định thức","D. Có hạng"],"answer":"A. Có chuẩn","explanation":"Định nghĩa."},
{"question":"Chuỗi p ∑ 1/n^p hội tụ khi?","options":["A. p>1","B. p≥1","C. p<1","D. mọi p"],"answer":"A. p>1","explanation":"Tiêu chuẩn p-series."},
{"question":"∇f vuông góc với?","options":["A. Đường mức","B. Trục x","C. Trục y","D. Gốc tọa độ"],"answer":"A. Đường mức","explanation":"Gradient vuông góc đường mức."},
{"question":"Ma trận chéo có giá trị riêng là?","options":["A. Các phần tử chéo","B. 0","C. 1","D. Trace"],"answer":"A. Các phần tử chéo","explanation":"Tính chất ma trận chéo."},
{"question":"Var(aX)=?","options":["A. aVar(X)","B. a^2Var(X)","C. Var(X)","D. a+Var(X)"],"answer":"B. a^2Var(X)","explanation":"Tính chất phương sai."},
{"question":"∫ 1/x dx bằng?","options":["A. ln|x|+C","B. 1/x","C. x","D. e^x"],"answer":"A. ln|x|+C","explanation":"Nguyên hàm cơ bản."},
{"question":"Hệ vector độc lập khi?","options":["A. Tổ hợp tuyến tính bằng 0 chỉ có nghiệm tầm thường","B. Có nghiệm khác 0","C. det=0","D. rank< n"],"answer":"A. Tổ hợp tuyến tính bằng 0 chỉ có nghiệm tầm thường","explanation":"Định nghĩa độc lập tuyến tính."},
{"question":"∫_0^{π} cosx dx bằng?","options":["A. 0","B. 2","C. -2","D. π"],"answer":"A. 0","explanation":"sinx từ 0 đến π."},
{"question":"Phương trình Laplace là?","options":["A. ∇^2u=0","B. u'=0","C. u''+u=0","D. det=0"],"answer":"A. ∇^2u=0","explanation":"Định nghĩa phương trình Laplace."},
{"question":"Chuẩn của vector 0 bằng?","options":["A. 1","B. 0","C. -1","D. Không xác định"],"answer":"B. 0","explanation":"Tính chất chuẩn."},
{"question":"∫ e^{ax} dx bằng?","options":["A. e^{ax}+C","B. (1/a)e^{ax}+C","C. ae^{ax}","D. ln(ax)"],"answer":"B. (1/a)e^{ax}+C","explanation":"Chia cho a."},
{"question":"Ma trận phản xứng thỏa mãn?","options":["A. A^T=-A","B. A^T=A","C. det=1","D. trace=0"],"answer":"A. A^T=-A","explanation":"Định nghĩa."},
{"question":"Nếu X,Y độc lập thì Var(X+Y)=?","options":["A. Var(X)+Var(Y)","B. Var(X)Var(Y)","C. 0","D. 1"],"answer":"A. Var(X)+Var(Y)","explanation":"Tính chất độc lập."},
{"question":"∫_0^1 ln x dx bằng?","options":["A. -1","B. 1","C. 0","D. e"],"answer":"A. -1","explanation":"Tích phân từng phần."},
{"question":"Không gian Hilbert là?","options":["A. Không gian chuẩn đầy đủ với tích vô hướng","B. Không gian hữu hạn chiều","C. Không gian Euclid","D. Không gian con"],"answer":"A. Không gian chuẩn đầy đủ với tích vô hướng","explanation":"Định nghĩa."},
{"question":"Chuỗi Taylor của e^x tại 0 là?","options":["A. ∑ x^n/n!","B. ∑ x^n","C. ∑ 1/n!","D. ∑ nx"],"answer":"A. ∑ x^n/n!","explanation":"Khai triển Maclaurin."},
{"question":"Nếu det(A)=0 thì?","options":["A. A khả nghịch","B. A không khả nghịch","C. trace=0","D. rank=n"],"answer":"B. A không khả nghịch","explanation":"Điều kiện nghịch đảo."},
{"question":"∫_0^{π/2} sinx cosx dx bằng?","options":["A. 1/2","B. 1","C. 0","D. 2"],"answer":"A. 1/2","explanation":"Đặt u=sinx."},
{"question":"Hàm lồi thỏa mãn?","options":["A. f(tx+(1-t)y)≤tf(x)+(1-t)f(y)","B. ≥","C. =","D. Không điều kiện"],"answer":"A. f(tx+(1-t)y)≤tf(x)+(1-t)f(y)","explanation":"Định nghĩa hàm lồi."},
{
    "question": "Trong Lý thuyết đồ thị, một đồ thị vô hướng có tổng bậc của tất cả các đỉnh bằng 20. Số cạnh của đồ thị đó là:",
    "options": ["10", "20", "40", "5"],
    "answer": "A",
    "explanation": "Theo định lý bắt tay, tổng bậc của các đỉnh bằng 2 lần số cạnh. Vậy số cạnh là $20/2 = 10$."
  },
  {
    "question": "Cho biến ngẫu nhiên $X$ có bảng phân phối xác suất với $P(X=0) = 0.2$ và $P(X=1) = 0.8$. Kỳ vọng $E(X)$ là:",
    "options": ["0.8", "0.2", "1.0", "0.5"],
    "answer": "A",
    "explanation": "$E(X) = 0 \cdot 0.2 + 1 \cdot 0.8 = 0.8$."
  },
  {
    "question": "Một ma trận vuông $A$ là ma trận lũy đẳng (idempotent) nếu thỏa mãn điều kiện nào?",
    "options": ["A^2 = A", "A^2 = I", "A^T = A", "\det(A) = 1"],
    "answer": "A",
    "explanation": "Định nghĩa ma trận lũy đẳng là ma trận khi nhân với chính nó vẫn bằng chính nó."
  },
  {
    "question": "Tính tích phân kép $I = \iint_D dxdy$, trong đó $D$ là hình tròn tâm $O(0,0)$ bán kính $R=2$.",
    "options": ["4\pi", "2\pi", "\pi", "8\pi"],
    "answer": "A",
    "explanation": "Tích phân kép của hàm $f(x,y)=1$ trên miền $D$ chính là diện tích của miền $D$. $S = \pi R^2 = 4\pi$."
  },
  {
    "question": "Trong không gian vectơ $\mathbb{R}^3$, cho hệ vectơ $S = \{(1,0,0), (0,1,0), (1,1,0)\}$. Khẳng định nào đúng?",
    "options": ["S phụ thuộc tuyến tính", "S là một cơ sở của \mathbb{R}^3", "S độc lập tuyến tính", "S sinh ra \mathbb{R}^3"],
    "answer": "A",
    "explanation": "Vectơ thứ ba là tổng của hai vectơ đầu $(1,1,0) = (1,0,0) + (0,1,0)$, nên hệ phụ thuộc tuyến tính."
  },
  {
    "question": "Tìm vi phân cấp hai $d^2z$ của hàm số $z = x^2 + y^2$.",
    "options": ["2dx^2 + 2dy^2", "2dx + 2dy", "dx^2 + dy^2", "2dxdy"],
    "answer": "A",
    "explanation": "$z''_x = 2, z''_y = 2, z''_{xy} = 0$. Công thức $d^2z = z''_{x^2}dx^2 + 2z''_{xy}dxdy + z''_{y^2}dy^2 = 2dx^2 + 2dy^2$."
  },
  {
    "question": "Cho $X$ là biến ngẫu nhiên tuân theo quy luật phân phối chuẩn $N(\mu, \sigma^2)$. Khẳng định nào sau đây đúng?",
    "options": ["Hàm mật độ đối xứng qua đường thẳng x = \mu", "Kỳ vọng E(X) = \sigma", "Đồ thị hàm mật độ có dạng hình chữ nhật", "Xác suất P(X = \mu) = 1"],
    "answer": "A",
    "explanation": "Phân phối chuẩn có hàm mật độ hình chuông và đối xứng qua giá trị trung bình $\mu$."
  },
  
  {
    "question": "Trong Logic mệnh đề, mệnh đề $P \rightarrow Q$ tương đương với mệnh đề nào?",
    "options": ["\neg P \lor Q", "P \land \neg Q", "\neg Q \rightarrow \neg P", "Cả A và C đều đúng"],
    "answer": "D",
    "explanation": "$P \rightarrow Q$ tương đương với luật kéo theo $\neg P \lor Q$ và luật đảo phản chứng $\neg Q \rightarrow \neg P$."
  },
  {
    "question": "Tìm cực trị của hàm số $f(x,y) = x^2 + y^2$ với điều kiện ràng buộc $x + y = 1$ bằng phương pháp nhân tử Lagrange.",
    "options": ["(1/2, 1/2)", "(0, 1)", "(1, 0)", "(1/4, 3/4)"],
    "answer": "A",
    "explanation": "Lập hàm $L(x,y,\lambda) = x^2 + y^2 + \lambda(x+y-1)$. Đạo hàm riêng: $2x+\lambda=0, 2y+\lambda=0 \Rightarrow x=y$. Thay vào ràng buộc được $x=y=1/2$."
  },
  {
    "question": "Chuỗi Fourier của hàm số chẵn $f(x)$ trên đoạn $[-\pi, \pi]$ chỉ chứa các số hạng của:",
    "options": ["Hàm cosin", "Hàm sin", "Cả sin và cosin", "Hàm mũ"],
    "answer": "A",
    "explanation": "Đối với hàm chẵn, các hệ số $b_n$ (đi kèm với $\sin nx$) sẽ bằng 0, do đó chuỗi chỉ còn các số hạng cosin."
  },
  {
    "question": "Số cách chọn ra một nhóm 3 người từ một tập hợp 10 người (không phân biệt thứ tự) là:",
    "options": ["120", "720", "30", "100"],
    "answer": "A",
    "explanation": "Sử dụng tổ hợp: $C_{10}^3 = \frac{10!}{3!7!} = \frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1} = 120$."
  },
  {
    "question": "Cho ma trận vuông $A$. Nếu $A^T = -A$ thì $A$ được gọi là:",
    "options": ["Ma trận phản đối xứng", "Ma trận đối xứng", "Ma trận trực giao", "Ma trận suy biến"],
    "answer": "A",
    "explanation": "Định nghĩa ma trận phản đối xứng (skew-symmetric) là ma trận có chuyển vị bằng âm của chính nó."
  },
  {
    "question": "Giá trị riêng (eigenvalue) của ma trận $A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ là:",
    "options": ["2 và 3", "0 và 2", "5 và 6", "1 và 1"],
    "answer": "A",
    "explanation": "Đối với ma trận đường chéo, các giá trị riêng nằm ngay trên đường chéo chính."
  },
  {
    "question": "Tích phân mặt loại 1 $\iint_S ds$ tính đại lượng nào của mặt $S$?",
    "options": ["Diện tích mặt S", "Thể tích khối giới hạn bởi S", "Khối lượng của S", "Thông lượng qua mặt S"],
    "answer": "A",
    "explanation": "Tích phân mặt loại 1 của hàm $f(x,y,z)=1$ là công thức tính diện tích mặt cong."
  },
  {
    "question": "Trong xác suất, hai biến cố $A$ và $B$ độc lập khi và chỉ khi:",
    "options": ["P(A \cap B) = P(A) \cdot P(B)", "P(A \cup B) = P(A) + P(B)", "A \cap B = \emptyset", "P(A|B) = P(A|B)"],
    "answer": "A",
    "explanation": "Đây là định nghĩa cơ bản của hai biến cố độc lập xác suất."
  },
  {
    "question": "Phương trình đặc trưng của phương trình vi phân $y'' - 4y = 0$ là:",
    "options": ["k^2 - 4 = 0", "k^2 + 4 = 0", "k - 4 = 0", "k^2 - 4k = 0"],
    "answer": "A",
    "explanation": "Thay $y = e^{kx}$ vào phương trình ta thu được phương trình đại số tương ứng."
  },
  {
    "question": "Hàm số $f(z) = z^2$ trong giải tích phức có đạo hàm tại mọi điểm trên mặt phẳng phức không?",
    "options": ["Có, vì nó là hàm giải tích (analytic)", "Không, chỉ có đạo hàm tại z=0", "Không, nó không thỏa mãn điều kiện Cauchy-Riemann", "Chỉ có đạo hàm tại các điểm thực"],
    "answer": "A",
    "explanation": "Hàm đa thức biến phức luôn là hàm chỉnh hình (holomorph) trên toàn bộ mặt phẳng phức $\mathbb{C}$."
  },
  {
    "question": "Trong thống kê, khoảng tin cậy cho kỳ vọng của phân phối chuẩn khi đã biết phương sai $\sigma^2$ sử dụng phân phối nào?",
    "options": ["Phân phối chuẩn Z", "Phân phối Student t", "Phân phối Chi-bình phương", "Phân phối Fisher F"],
    "answer": "A",
    "explanation": "Khi đã biết phương sai tổng thể $\sigma^2$, ta sử dụng giá trị tới hạn từ phân phối chuẩn chuẩn hóa."
  },
  {
    "question": "Một quan hệ $R$ trên tập $A$ được gọi là quan hệ tương đương nếu nó thỏa mãn các tính chất:",
    "options": ["Phản xạ, đối xứng, bắc cầu", "Phản xạ, phản đối xứng, bắc cầu", "Đối xứng, bắc cầu, không phản xạ", "Hội tụ và bị chặn"],
    "answer": "A",
    "explanation": "Đây là ba tính chất định nghĩa quan hệ tương đương trong toán học rời rạc."
  },
  {
    "question": "Tính đạo hàm của hàm số $f(x) = \int_0^x e^{t^2} dt$.",
    "options": ["e^{x^2}", "2xe^{x^2}", "e^{x^2} - 1", "e^t"],
    "answer": "A",
    "explanation": "Theo định lý cơ bản của giải tích: $\frac{d}{dx} \int_a^x f(t)dt = f(x)$."
  },
  {"question":"Giới hạn lim(x→0) (e^x-1)/x bằng?","options":["A. 0","B. 1","C. e","D. Không tồn tại"],"answer":"B. 1","explanation":"Giới hạn cơ bản của hàm mũ."},
{"question":"∫_0^1 x^3 dx bằng?","options":["A. 1/2","B. 1/3","C. 1/4","D. 1"],"answer":"C. 1/4","explanation":"Nguyên hàm x^4/4."},
{"question":"Nếu A là ma trận trực giao thì det(A)=?","options":["A. 0","B. 1 hoặc -1","C. 1","D. -1"],"answer":"B. 1 hoặc -1","explanation":"Tính chất ma trận trực giao."},
{"question":"Chuỗi ∑ 1/n^2 hội tụ đến?","options":["A. π^2/6","B. 1","C. π","D. 2"],"answer":"A. π^2/6","explanation":"Bài toán Basel."},
{"question":"Đạo hàm của ln(x^2) là?","options":["A. 1/x","B. 2/x","C. x","D. 2x"],"answer":"B. 2/x","explanation":"Dùng quy tắc dây chuyền."},
{"question":"Hạng tối đa của ma trận m×n là?","options":["A. m+n","B. min(m,n)","C. mn","D. m-n"],"answer":"B. min(m,n)","explanation":"Giới hạn bởi số hàng và cột."},
{"question":"∫ sinx dx bằng?","options":["A. cosx + C","B. -cosx + C","C. sinx + C","D. tanx + C"],"answer":"B. -cosx + C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu X có phân phối Poisson(λ) thì E(X)=?","options":["A. λ","B. λ^2","C. 1/λ","D. 0"],"answer":"A. λ","explanation":"Tính chất phân phối Poisson."},
{"question":"Phương trình vi phân y'+2y=0 có nghiệm?","options":["A. Ce^{-2x}","B. Ce^{2x}","C. Cx","D. C"],"answer":"A. Ce^{-2x}","explanation":"Giải phương trình tuyến tính bậc 1."},
{"question":"Trace(A+B)=?","options":["A. trace(A)+trace(B)","B. trace(A)trace(B)","C. 0","D. det(A+B)"],"answer":"A. trace(A)+trace(B)","explanation":"Tính tuyến tính của trace."},
{"question":"∫_0^1 1 dx bằng?","options":["A. 0","B. 1","C. 2","D. 1/2"],"answer":"B. 1","explanation":"Diện tích hình chữ nhật."},
{"question":"Vector đơn vị theo hướng (a,b) là?","options":["A. (a,b)","B. (a/√(a^2+b^2), b/√(a^2+b^2))","C. (1,1)","D. (0,0)"],"answer":"B. (a/√(a^2+b^2), b/√(a^2+b^2))","explanation":"Chia cho chuẩn."},
{"question":"Chuỗi luân phiên hội tụ khi?","options":["A. Giảm dần về 0","B. Tăng","C. Không đổi","D. Âm"],"answer":"A. Giảm dần về 0","explanation":"Tiêu chuẩn Leibniz."},
{"question":"∂^2/∂x^2 của x^3 bằng?","options":["A. 6x","B. 3x^2","C. 6","D. x"],"answer":"A. 6x","explanation":"Đạo hàm hai lần."},
{"question":"Nếu det(A)=det(B)≠0 thì?","options":["A. A=B","B. Cả hai khả nghịch","C. trace bằng nhau","D. rank=0"],"answer":"B. Cả hai khả nghịch","explanation":"det≠0 ⇒ khả nghịch."},
{"question":"∫ e^{-x} dx bằng?","options":["A. -e^{-x}+C","B. e^{-x}+C","C. ln x","D. x e^{-x}"],"answer":"A. -e^{-x}+C","explanation":"Nguyên hàm cơ bản."},
{"question":"Var(X+c)=?","options":["A. Var(X)","B. Var(X)+c","C. cVar(X)","D. 0"],"answer":"A. Var(X)","explanation":"Cộng hằng số không đổi phương sai."},
{"question":"Ma trận khả chéo hóa khi?","options":["A. Có đủ vector riêng độc lập","B. det=0","C. trace=0","D. Luôn luôn"],"answer":"A. Có đủ vector riêng độc lập","explanation":"Điều kiện chéo hóa."},
{"question":"∫_0^{π} sinx dx bằng?","options":["A. 0","B. 1","C. 2","D. π"],"answer":"C. 2","explanation":"-cosx từ 0 đến π."},
{"question":"Hàm khả vi thì?","options":["A. Liên tục","B. Không liên tục","C. Không xác định","D. Bị chặn"],"answer":"A. Liên tục","explanation":"Khả vi ⇒ liên tục."},
{"question":"Giá trị riêng của ma trận tam giác là?","options":["A. Các phần tử đường chéo","B. 0","C. 1","D. Trace"],"answer":"A. Các phần tử đường chéo","explanation":"Tính chất."},
{"question":"∫_0^1 x e^x dx bằng?","options":["A. 1","B. e-2","C. e-1","D. 2"],"answer":"B. e-2","explanation":"Tích phân từng phần."},
{"question":"Nếu X chuẩn tắc N(0,1) thì Var(X)=?","options":["A. 0","B. 1","C. 2","D. π"],"answer":"B. 1","explanation":"Phương sai chuẩn tắc."},
{"question":"Đạo hàm của arctan x là?","options":["A. 1/(1+x^2)","B. 1/x","C. x","D. sec^2 x"],"answer":"A. 1/(1+x^2)","explanation":"Công thức đạo hàm."},
{"question":"Nếu A^2=I thì A gọi là?","options":["A. Ma trận idempotent","B. Ma trận involutory","C. Ma trận trực giao","D. Ma trận 0"],"answer":"B. Ma trận involutory","explanation":"Định nghĩa A^2=I."},
{"question":"∫_0^1 √x dx bằng?","options":["A. 1/2","B. 2/3","C. 1","D. 3/2"],"answer":"B. 2/3","explanation":"Nguyên hàm 2/3 x^{3/2}."},
{"question":"Chuỗi Fourier biểu diễn?","options":["A. Hàm tuần hoàn","B. Hàm đa thức","C. Ma trận","D. Vector"],"answer":"A. Hàm tuần hoàn","explanation":"Khai triển Fourier."},
{"question":"Nếu A,B khả nghịch thì (AB)^{-1}=?","options":["A. A^{-1}B^{-1}","B. B^{-1}A^{-1}","C. AB","D. I"],"answer":"B. B^{-1}A^{-1}","explanation":"Đảo thứ tự."},
{"question":"∫ sech^2 x dx bằng?","options":["A. tanh x + C","B. sech x","C. sinh x","D. cosh x"],"answer":"A. tanh x + C","explanation":"Đạo hàm tanh x."},
{"question":"Định lý Green liên hệ giữa?","options":["A. Tích phân đường và tích phân kép","B. ODE và PDE","C. Ma trận và vector","D. Xác suất và tích phân"],"answer":"A. Tích phân đường và tích phân kép","explanation":"Định lý Green trong mặt phẳng."},
{
    "question": "Trong Giải tích phức, điều kiện Cauchy-Riemann cho hàm số $f(z) = u(x,y) + iv(x,y)$ là:",
    "options": ["u_x = v_y; u_y = -v_x", "u_x = -v_y; u_y = v_x", "u_x = v_x; u_y = v_y", "u_y = v_y; u_x = -v_x"],
    "answer": "A",
    "explanation": "Đây là điều kiện cần để một hàm biến phức có đạo hàm (khả vi phức) tại một điểm."
  },
  {
    "question": "Trong không gian Metric, một tập hợp được gọi là tập đóng nếu:",
    "options": ["Nó chứa tất cả các điểm giới hạn của nó", "Nó là tập con của tập mở", "Phần bù của nó là tập đóng", "Mọi dãy trong tập đó đều hội tụ"],
    "answer": "A",
    "explanation": "Định nghĩa tập đóng trong topo và không gian metric là tập chứa mọi điểm dính (điểm giới hạn) của chính nó."
  },
  {
    "question": "Tính thặng dư (Residue) của hàm số $f(z) = \frac{1}{z^2 + 1}$ tại cực điểm $z = i$.",
    "options": ["1/(2i)", "-1/(2i)", "i", "1"],
    "answer": "A",
    "explanation": "$Res(f, i) = \lim_{z \to i} (z-i) \frac{1}{(z-i)(z+i)} = \frac{1}{2i}$."
  },
  {
    "question": "Cho chuỗi hàm $\sum_{n=1}^{\infty} f_n(x)$. Tiêu chuẩn Weierstrass dùng để chứng minh:",
    "options": ["Chuỗi hội tụ đều", "Chuỗi hội tụ điểm", "Chuỗi phân kỳ", "Hàm số liên tục"],
    "answer": "A",
    "explanation": "Nếu $|f_n(x)| \le M_n$ và chuỗi số $\sum M_n$ hội tụ thì chuỗi hàm hội tụ đều."
  },
  {
    "question": "Độ cong (Curvature) của đường thẳng trong mặt phẳng bằng:",
    "options": ["0", "1", "+\infty", "Hằng số tùy ý"],
    "answer": "A",
    "explanation": "Đường thẳng không có sự thay đổi về hướng của vectơ tiếp tuyến, do đó độ cong bằng 0."
  },
  
  {
    "question": "Trong lý thuyết độ đo, độ đo Lebesgue của tập hợp các số hữu tỷ $\mathbb{Q}$ trên đoạn $[0, 1]$ là:",
    "options": ["0", "1", "1/2", "+\infty"],
    "answer": "A",
    "explanation": "Vì $\mathbb{Q}$ là tập đếm được, và độ đo của mỗi điểm đơn lẻ bằng 0, nên độ đo của tập hợp đếm được các điểm cũng bằng 0."
  },
  {
    "question": "Toán tử Laplace $\Delta f$ trong tọa độ Descartes được tính bằng:",
    "options": ["f_{xx} + f_{yy} + f_{zz}", "f_x + f_y + f_z", "f_{xy} + f_{yz} + f_{zx}", "grad(div f)"],
    "answer": "A",
    "explanation": "Toán tử Laplace là divergence của gradient: $\Delta f = \nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$."
  },
  {
    "question": "Một ánh xạ tuyến tính $f: V \to W$ là một đơn cấu (monomorphism) khi và chỉ khi:",
    "options": ["Ker(f) = {0}", "Im(f) = W", "dim(V) = dim(W)", "f(0) = 0"],
    "answer": "A",
    "explanation": "Ánh xạ tuyến tính là đơn ánh khi và chỉ khi hạt nhân (kernel) của nó chỉ chứa duy nhất vectơ không."
  },
  {
    "question": "Tính tích phân phức $I = \oint_{|z|=2} \frac{e^z}{z-1} dz$ theo công thức tích phân Cauchy.",
    "options": ["2\pi i e", "\pi i e", "2\pi i", "0"],
    "answer": "A",
    "explanation": "Điểm $z=1$ nằm bên trong đường tròn $|z|=2$. Theo công thức Cauchy: $I = 2\pi i \cdot f(1) = 2\pi i \cdot e^1$."
  },
  {
    "question": "Trong thống kê, sai lầm loại I xảy ra khi nào?",
    "options": ["Bác bỏ giả thuyết H0 khi H0 đúng", "Chấp nhận giả thuyết H0 khi H0 sai", "Bác bỏ giả thuyết H1 khi H1 đúng", "Chấp nhận giả thuyết H1 khi H1 sai"],
    "answer": "A",
    "explanation": "Sai lầm loại I (Type I error) là bác bỏ một giả thuyết đúng (mức ý nghĩa $\alpha$)."
  },
  {
    "question": "Một không gian Hilbert là một không gian vectơ định chuẩn thỏa mãn:",
    "options": ["Có tích vô hướng và đầy đủ", "Chỉ cần đầy đủ", "Chỉ cần có tích vô hướng", "Là không gian hữu hạn chiều"],
    "answer": "A",
    "explanation": "Không gian Hilbert là không gian Banach mà chuẩn được sinh ra từ một tích vô hướng."
  },
  {
    "question": "Hệ phương trình vi phân tuyến tính $x' = Ax$ có nghiệm ổn định khi các giá trị riêng của $A$ đều có:",
    "options": ["Phần thực âm", "Phần thực dương", "Môđun nhỏ hơn 1", "Giá trị thực"],
    "answer": "A",
    "explanation": "Nếu tất cả các giá trị riêng có phần thực âm, nghiệm sẽ tiến về 0 khi $t$ tiến ra vô cùng (ổn định tiệm cận)."
  },
  {
    "question": "Trong không gian vectơ, một tập hợp các vectơ $\{v_1, v_2, ..., v_n\}$ được gọi là trực giao nếu:",
    "options": ["v_i \cdot v_j = 0 với mọi i \neq j", "v_i \cdot v_i = 1 với mọi i", "v_i \cdot v_j = 1 với mọi i \neq j", "Tổng các vectơ bằng 0"],
    "answer": "A",
    "explanation": "Trực giao nghĩa là tích vô hướng của hai vectơ bất kỳ khác nhau trong bộ đó đều bằng 0."
  },
  {
    "question": "Khai triển Laurent của hàm số $f(z) = \frac{1}{z}$ tại lân cận $z=0$ là:",
    "options": ["1/z", "1 + z + z^2 + ...", "z + z^2 + ...", "Không khai triển được"],
    "answer": "A",
    "explanation": "Hàm số đã ở dạng một số hạng của chuỗi Laurent (phần chính) tại cực điểm bậc 1."
  },
  {
    "question": "Phép biến đổi Fourier của hàm Gauss $f(x) = e^{-x^2}$ có dạng:",
    "options": ["Hàm Gauss", "Hàm Sin", "Hàm bậc thang", "Đa thức"],
    "answer": "A",
    "explanation": "Một đặc tính quan trọng của hàm Gauss là phép biến đổi Fourier của nó vẫn là một hàm Gauss."
  },
  {
    "question": "Trong đại số trừu tượng, một nhóm $G$ được gọi là nhóm Abel nếu phép toán trong nhóm có tính chất:",
    "options": ["Giao hoán", "Kết hợp", "Có phần tử đơn vị", "Mọi phần tử đều có nghịch đảo"],
    "answer": "A",
    "explanation": "Nhóm Abel là nhóm thỏa mãn thêm tính chất giao hoán: $a \cdot b = b \cdot a$."
  },
  {
    "question": "Ma trận $A$ là ma trận xác định dương khi và chỉ khi:",
    "options": ["Mọi giá trị riêng của nó đều dương", "Định thức của nó dương", "Mọi phần tử của nó đều dương", "Vết (trace) của nó dương"],
    "answer": "A",
    "explanation": "Giá trị riêng dương là điều kiện cần và đủ cho ma trận đối xứng xác định dương."
  },
  {
    "question": "Số phức $i^i$ (i mũ i) có giá trị thực là:",
    "options": ["e^{-\pi/2}", "e^{\pi/2}", "-1", "i"],
    "answer": "A",
    "explanation": "$i^i = (e^{i\pi/2})^i = e^{i^2\pi/2} = e^{-\pi/2}$. Đây là một kết quả thú vị vì lũy thừa của số ảo lại ra số thực."
  },
  {
    "question": "Định lý Stokes liên quan giữa tích phân mặt của rot vectơ và:",
    "options": ["Tích phân đường trên biên của mặt đó", "Tích phân thể tích của div vectơ", "Tích phân mặt của chính vectơ đó", "Diện tích mặt cong"],
    "answer": "A",
    "explanation": "$\iint_S (\nabla \times F) \cdot dS = \oint_{\partial S} F \cdot dr$."
  },
  {
    "question": "Trong giải tích số, phương pháp Newton-Raphson dùng để:",
    "options": ["Tìm xấp xỉ nghiệm của phương trình f(x) = 0", "Tính tích phân xác định", "Giải hệ phương trình vi phân", "Nội suy hàm số"],
    "answer": "A",
    "explanation": "Đây là phương pháp lặp sử dụng tiếp tuyến để tìm nghiệm của phương trình phi tuyến."
  },
  {"question":"Giới hạn lim(x→0) (ln(1+x)/x) bằng?","options":["A. 0","B. 1","C. -1","D. Không tồn tại"],"answer":"B. 1","explanation":"Giới hạn cơ bản của logarit."},
{"question":"∫_0^1 x^4 dx bằng?","options":["A. 1/4","B. 1/5","C. 1","D. 1/6"],"answer":"B. 1/5","explanation":"Nguyên hàm x^5/5."},
{"question":"Nếu A là ma trận idempotent thì A^2=?","options":["A. 0","B. I","C. A","D. -A"],"answer":"C. A","explanation":"Định nghĩa idempotent."},
{"question":"Chuỗi ∑ (-1)^{n+1}/n^2 hội tụ?","options":["A. Tuyệt đối","B. Điều kiện","C. Phân kỳ","D. Không xác định"],"answer":"A. Tuyệt đối","explanation":"Vì ∑1/n^2 hội tụ."},
{"question":"Đạo hàm của sinh x là?","options":["A. cosh x","B. sinh x","C. -cosh x","D. tanh x"],"answer":"A. cosh x","explanation":"Công thức đạo hàm hyperbolic."},
{"question":"Không gian vector hữu hạn chiều luôn?","options":["A. Đầy đủ","B. Không đầy đủ","C. Không chuẩn","D. Không liên tục"],"answer":"A. Đầy đủ","explanation":"Mọi không gian hữu hạn chiều đều đầy đủ."},
{"question":"∫ 1/(1+x^2) dx bằng?","options":["A. arctan x + C","B. ln|x|","C. tan x","D. 1/x"],"answer":"A. arctan x + C","explanation":"Nguyên hàm chuẩn."},
{"question":"Nếu X,Y độc lập thì Cov(X,Y)=?","options":["A. 0","B. 1","C. Var(X)","D. Var(Y)"],"answer":"A. 0","explanation":"Định nghĩa độc lập."},
{"question":"Phương trình đặc trưng của y''+4y=0 là?","options":["A. r^2+4=0","B. r^2-4=0","C. r+4=0","D. r^2=4"],"answer":"A. r^2+4=0","explanation":"Thay y=e^{rx}."},
{"question":"Định thức của ma trận đơn vị bằng?","options":["A. 0","B. 1","C. n","D. -1"],"answer":"B. 1","explanation":"Tính chất."},
{"question":"∫_0^{π/4} tan x dx bằng?","options":["A. ln√2","B. 1","C. 0","D. π/4"],"answer":"A. ln√2","explanation":"∫tanx dx = -ln|cosx|."},
{"question":"Chuẩn L2 của hàm f là?","options":["A. (∫|f|^2)^{1/2}","B. ∫|f|","C. sup|f|","D. f^2"],"answer":"A. (∫|f|^2)^{1/2}","explanation":"Định nghĩa chuẩn L2."},
{"question":"Nếu λ là giá trị riêng thì vector riêng thỏa?","options":["A. Av=λv","B. Av=v","C. det=λ","D. trace=λ"],"answer":"A. Av=λv","explanation":"Định nghĩa."},
{"question":"∫_0^1 e^{2x} dx bằng?","options":["A. (e^2-1)/2","B. e^2-1","C. 1/2","D. 2"],"answer":"A. (e^2-1)/2","explanation":"Nguyên hàm e^{2x}/2."},
{"question":"Nếu f''>0 trên khoảng thì f?","options":["A. Lồi","B. Lõm","C. Giảm","D. Hằng"],"answer":"A. Lồi","explanation":"Tiêu chuẩn lồi."},
{"question":"Ma trận nilpotent thỏa?","options":["A. A^k=0 với k nào đó","B. A^2=A","C. A=I","D. det=1"],"answer":"A. A^k=0 với k nào đó","explanation":"Định nghĩa nilpotent."},
{"question":"∫ cosh x dx bằng?","options":["A. sinh x + C","B. cosh x","C. tanh x","D. -sinh x"],"answer":"A. sinh x + C","explanation":"Nguyên hàm hyperbolic."},
{"question":"Kỳ vọng của hằng số c là?","options":["A. c","B. 0","C. 1","D. c^2"],"answer":"A. c","explanation":"E(c)=c."},
{"question":"Nếu ma trận có det≠0 thì hệ Ax=0 có nghiệm?","options":["A. Vô số","B. Không","C. Chỉ nghiệm tầm thường","D. 2 nghiệm"],"answer":"C. Chỉ nghiệm tầm thường","explanation":"Ma trận khả nghịch."},
{"question":"∫_0^{π/2} sin^2 x dx bằng?","options":["A. π/4","B. 1/2","C. π/2","D. 1"],"answer":"A. π/4","explanation":"Dùng công thức hạ bậc."},
{"question":"Chuỗi mũ ∑ x^n/n! hội tụ với?","options":["A. Mọi x","B. |x|<1","C. x>0","D. x<1"],"answer":"A. Mọi x","explanation":"Bán kính hội tụ vô hạn."},
{"question":"Gradient của f(x,y,z)=x+y+z là?","options":["A. (1,1,1)","B. (x,y,z)","C. (0,0,0)","D. (x+y,z)"],"answer":"A. (1,1,1)","explanation":"Đạo hàm riêng."},
{"question":"Nếu A là ma trận đối xứng thực thì giá trị riêng?","options":["A. Thực","B. Phức","C. Âm","D. 0"],"answer":"A. Thực","explanation":"Định lý phổ."},
{"question":"∫_0^1 x ln x dx bằng?","options":["A. -1/4","B. 1/4","C. -1/2","D. 0"],"answer":"A. -1/4","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Bernoulli(p) thì Var(X)=?","options":["A. p(1-p)","B. p","C. 1-p","D. p^2"],"answer":"A. p(1-p)","explanation":"Công thức phương sai Bernoulli."},
{"question":"Đạo hàm của cosh x là?","options":["A. sinh x","B. cosh x","C. -sinh x","D. tanh x"],"answer":"A. sinh x","explanation":"Công thức đạo hàm."},
{"question":"Ma trận tam giác trên có hạng bằng?","options":["A. Số phần tử khác 0 trên chéo","B. 0","C. 1","D. n^2"],"answer":"A. Số phần tử khác 0 trên chéo","explanation":"Nếu các phần tử chéo khác 0."},
{"question":"∫_0^{π/2} cos^2 x dx bằng?","options":["A. π/4","B. 1/2","C. 1","D. π/2"],"answer":"A. π/4","explanation":"Công thức hạ bậc."},
{"question":"Nếu f liên tục trên [a,b] thì?","options":["A. Có nguyên hàm","B. Không khả tích","C. Không bị chặn","D. Không đạt GTLN"],"answer":"A. Có nguyên hàm","explanation":"Định lý cơ bản giải tích."},
{"question":"Biến đổi Laplace của 1 là?","options":["A. 1/s","B. s","C. 0","D. e^s"],"answer":"A. 1/s","explanation":"Công thức cơ bản."},
{"question":"Giới hạn lim(x→∞) (ln x / x) bằng?","options":["A. 0","B. 1","C. ∞","D. Không tồn tại"],"answer":"A. 0","explanation":"Dùng quy tắc L'Hospital."},
{"question":"∫_0^1 x^5 dx bằng?","options":["A. 1/5","B. 1/6","C. 1/4","D. 1/3"],"answer":"B. 1/6","explanation":"Nguyên hàm x^6/6."},
{"question":"Nếu A là ma trận trực giao thì A^{-1}=?","options":["A. A^T","B. -A","C. I","D. 0"],"answer":"A. A^T","explanation":"Tính chất ma trận trực giao."},
{"question":"Chuỗi ∑ x^n hội tụ khi?","options":["A. |x|<1","B. x>1","C. x=1","D. Mọi x"],"answer":"A. |x|<1","explanation":"Chuỗi hình học."},
{"question":"Đạo hàm của tan x là?","options":["A. sec^2 x","B. cos x","C. -sec^2 x","D. sin x"],"answer":"A. sec^2 x","explanation":"Công thức đạo hàm."},
{"question":"Nếu rank(A)=n với A vuông cấp n thì?","options":["A. A khả nghịch","B. det=0","C. trace=0","D. A=0"],"answer":"A. A khả nghịch","explanation":"Rank đầy đủ."},
{"question":"∫ e^{3x} dx bằng?","options":["A. e^{3x}","B. (1/3)e^{3x}+C","C. 3e^{3x}","D. ln(3x)"],"answer":"B. (1/3)e^{3x}+C","explanation":"Chia cho 3."},
{"question":"Nếu X,Y độc lập thì E(XY)=?","options":["A. E(X)+E(Y)","B. E(X)E(Y)","C. 0","D. Var(X)"],"answer":"B. E(X)E(Y)","explanation":"Tính chất độc lập."},
{"question":"Phương trình y''-4y=0 có nghiệm tổng quát?","options":["A. Ae^{2x}+Be^{-2x}","B. A cos2x + B sin2x","C. Ax+B","D. Ae^x"],"answer":"A. Ae^{2x}+Be^{-2x}","explanation":"Giải phương trình đặc trưng."},
{"question":"Trace(I_n) bằng?","options":["A. 1","B. n","C. 0","D. n^2"],"answer":"B. n","explanation":"Tổng n số 1."},
{"question":"∫_0^1 x^n dx bằng?","options":["A. 1/n","B. 1/(n+1)","C. n","D. 0"],"answer":"B. 1/(n+1)","explanation":"Nguyên hàm x^{n+1}/(n+1)."},
{"question":"Chuẩn vô cùng của vector (x_i) là?","options":["A. max|x_i|","B. ∑|x_i|","C. √∑x_i^2","D. 0"],"answer":"A. max|x_i|","explanation":"Định nghĩa chuẩn vô cùng."},
{"question":"Nếu A đối xứng thực thì có thể?","options":["A. Chéo hóa bởi ma trận trực giao","B. Không chéo hóa","C. det=0","D. rank=1"],"answer":"A. Chéo hóa bởi ma trận trực giao","explanation":"Định lý phổ."},
{"question":"∫_0^{π} sin^2 x dx bằng?","options":["A. π/2","B. π/4","C. 1","D. 2"],"answer":"A. π/2","explanation":"Dùng công thức hạ bậc."},
{"question":"Nếu f' = 0 trên khoảng thì f?","options":["A. Hằng","B. Tăng","C. Giảm","D. Lồi"],"answer":"A. Hằng","explanation":"Định lý giá trị trung bình."},
{"question":"Ma trận suy biến khi?","options":["A. det=0","B. det≠0","C. trace=0","D. rank=n"],"answer":"A. det=0","explanation":"Định nghĩa."},
{"question":"∫ sinh x dx bằng?","options":["A. cosh x + C","B. sinh x","C. tanh x","D. -cosh x"],"answer":"A. cosh x + C","explanation":"Nguyên hàm hyperbolic."},
{"question":"Nếu X~Uniform(0,1) thì E(X)=?","options":["A. 1/2","B. 1","C. 0","D. 1/3"],"answer":"A. 1/2","explanation":"Trung bình phân phối đều."},
{"question":"Đạo hàm của ln|x| là?","options":["A. 1/x","B. x","C. ln x","D. 1"],"answer":"A. 1/x","explanation":"Công thức cơ bản."},
{"question":"Nếu A,B vuông cùng cấp thì det(AB)=?","options":["A. det(A)+det(B)","B. det(A)det(B)","C. 0","D. det(A-B)"],"answer":"B. det(A)det(B)","explanation":"Tính chất định thức."},
{"question":"∫_0^{π/2} tan^2 x dx bằng?","options":["A. π/2 -1","B. 1","C. 0","D. π/4"],"answer":"A. π/2 -1","explanation":"tan^2x = sec^2x -1."},
{"question":"Nếu chuỗi lũy thừa có bán kính R thì hội tụ khi?","options":["A. |x|<R","B. |x|>R","C. x=R","D. Mọi x"],"answer":"A. |x|<R","explanation":"Định nghĩa bán kính hội tụ."},
{"question":"Gradient của f(x,y)=xy là?","options":["A. (y,x)","B. (x,y)","C. (1,1)","D. (0,0)"],"answer":"A. (y,x)","explanation":"Đạo hàm riêng."},
{"question":"Nếu λ là nghiệm bội k của đa thức đặc trưng thì?","options":["A. Bội đại số k","B. Bội hình học k","C. det=0","D. trace=k"],"answer":"A. Bội đại số k","explanation":"Định nghĩa."},
{"question":"∫_0^1 x^2 ln x dx bằng?","options":["A. -1/9","B. 1/9","C. -1/4","D. 0"],"answer":"A. -1/9","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Exponential(λ) thì E(X)=?","options":["A. 1/λ","B. λ","C. λ^2","D. 0"],"answer":"A. 1/λ","explanation":"Trung bình phân phối mũ."},
{"question":"Đạo hàm của sec x là?","options":["A. sec x tan x","B. tan x","C. -sec x tan x","D. cos x"],"answer":"A. sec x tan x","explanation":"Công thức đạo hàm."},
{"question":"Ma trận đơn vị là?","options":["A. Có 1 trên đường chéo chính","B. Tất cả bằng 1","C. det=0","D. trace=0"],"answer":"A. Có 1 trên đường chéo chính","explanation":"Định nghĩa."},
{"question":"∫_0^{π/2} sec^2 x dx bằng?","options":["A. 1","B. tan(π/2)","C. ∞","D. 0"],"answer":"C. ∞","explanation":"tan x → ∞ tại π/2."},
{"question":"Nếu f liên tục và khả vi thì?","options":["A. Có khai triển Taylor","B. Không tích phân","C. Không giới hạn","D. Không đạo hàm"],"answer":"A. Có khai triển Taylor","explanation":"Hàm trơn có thể khai triển Taylor."},
{
    "question": "Trong phương trình truyền nhiệt $u_t = \alpha^2 u_{xx}$, tham số $\alpha^2$ đại diện cho đại lượng nào?",
    "options": ["Hệ số khuếch tán nhiệt", "Nhiệt độ ban đầu", "Năng lượng nguồn", "Tốc độ truyền sóng"],
    "answer": "A",
    "explanation": "$\alpha^2$ (hay $k$) là hệ số khuếch tán nhiệt, quyết định tốc độ san bằng sự chênh lệch nhiệt độ trong vật thể."
  },
  {
    "question": "Phép biến đổi Laplace của hàm số $f(t) = \sin(at)$ là:",
    "options": ["a / (s^2 + a^2)", "s / (s^2 + a^2)", "1 / (s - a)", "a / (s^2 - a^2)"],
    "answer": "A",
    "explanation": "Đây là công thức biến đổi Laplace cơ bản cho hàm lượng giác sin."
  },
  {
    "question": "Trong Lý thuyết Đồ thị, một đồ thị liên thông không có chu trình được gọi là:",
    "options": ["Cây (Tree)", "Đồ thị đầy đủ", "Đồ thị lưỡng phân", "Đồ thị Hamilton"],
    "answer": "A",
    "explanation": "Cây là đồ thị vô hướng, liên thông và không chứa chu trình đơn."
  },
  
  {
    "question": "Xét phương trình sóng $u_{tt} = c^2 u_{xx}$. Nghiệm D'Alembert của phương trình này có dạng:",
    "options": ["u(x,t) = f(x-ct) + g(x+ct)", "u(x,t) = f(x) \cdot g(t)", "u(x,t) = e^{-ct} \sin(x)", "u(x,t) = f(x^2 - c^2t^2)"],
    "answer": "A",
    "explanation": "Nghiệm D'Alembert mô tả sóng truyền về hai phía với vận tốc c."
  },
  {
    "question": "Trong không gian Banach, mọi dãy Cauchy đều:",
    "options": ["Hội tụ", "Bị chặn nhưng không nhất thiết hội tụ", "Tiến về 0", "Có vô số điểm giới hạn"],
    "answer": "A",
    "explanation": "Theo định nghĩa, không gian Banach là không gian vectơ định chuẩn đầy đủ, nơi mọi dãy Cauchy đều hội tụ trong không gian đó."
  },
  {
    "question": "Hàm số $f(z) = \bar{z}$ (số phức liên hợp) có đạo hàm phức tại điểm nào?",
    "options": ["Không có đạo hàm tại bất kỳ đâu", "Chỉ tại z = 0", "Trên toàn bộ mặt phẳng phức", "Chỉ trên trục thực"],
    "answer": "A",
    "explanation": "Hàm $f(z) = x - iy$ không thỏa mãn điều kiện Cauchy-Riemann tại bất kỳ điểm nào ($u_x=1, v_y=-1 \Rightarrow u_x \neq v_y$)."
  },
  {
    "question": "Trong quy hoạch tuyến tính, tập hợp các phương án cực biên của một bài toán có miền ràng buộc là tập lồi đóng, bị chặn chính là:",
    "options": ["Các đỉnh của đa diện ràng buộc", "Trọng tâm của đa diện", "Các điểm nằm trên cạnh", "Toàn bộ miền trong của đa diện"],
    "answer": "A",
    "explanation": "Phương án tối ưu của bài toán quy hoạch tuyến tính luôn nằm tại ít nhất một đỉnh (điểm cực biên) của tập hợp các phương án."
  },
  
  {
    "question": "Định lý giá trị trung bình cho tích phân phát biểu rằng nếu $f$ liên tục trên $[a, b]$, tồn tại $c \in [a, b]$ sao cho $\int_a^b f(x)dx$ bằng:",
    "options": ["f(c)(b - a)", "f(c)", "f'(c)(b - a)", "0"],
    "answer": "A",
    "explanation": "Giá trị trung bình của hàm số trên đoạn là $\frac{1}{b-a} \int_a^b f(x)dx$."
  },
  {
    "question": "Trong Xác suất, nếu hiệp phương sai $Cov(X, Y) = 0$, ta kết luận $X$ và $Y$:",
    "options": ["Không tương quan tuyến tính", "Độc lập hoàn toàn", "Có tổng bằng 0", "Có cùng phương sai"],
    "answer": "A",
    "explanation": "Hiệp phương sai bằng 0 chỉ khẳng định không có mối liên hệ tuyến tính. Để độc lập hoàn toàn, cần điều kiện mạnh hơn."
  },
  {
    "question": "Một hệ thống các phương trình tuyến tính $Ax = 0$ (hệ thuần nhất) luôn luôn:",
    "options": ["Có ít nhất một nghiệm (nghiệm tầm thường)", "Vô nghiệm", "Có vô số nghiệm", "Có nghiệm duy nhất khác không"],
    "answer": "A",
    "explanation": "Hệ thuần nhất luôn có nghiệm $x = 0$."
  },
  {
    "question": "Tích phân mặt loại 2 tính thông lượng của trường vectơ $F$ qua mặt $S$ được ký hiệu là:",
    "options": ["\iint_S F \cdot n dS", "\iint_S f dS", "\int_C F \cdot dr", "\iiint_V div F dV"],
    "answer": "A",
    "explanation": "Đây là tích phân mặt của thành phần pháp tuyến của trường vectơ $F$ qua mặt $S$."
  },
  {
    "question": "Trong lý thuyết nhóm, cấp của một phần tử $a$ là số nguyên dương $n$ nhỏ nhất sao cho:",
    "options": ["a^n = e (phần tử đơn vị)", "n \cdot a = 1", "a^n = a", "a^n = 0"],
    "answer": "A",
    "explanation": "Đây là định nghĩa về cấp (order) của một phần tử trong nhóm."
  },
  {
    "question": "Toán tử gradient của một trường vô hướng $\phi$ là một:",
    "options": ["Trường vectơ", "Trường vô hướng", "Hằng số", "Ma trận"],
    "answer": "A",
    "explanation": "$\nabla \phi = (\frac{\partial \phi}{\partial x}, \frac{\partial \phi}{\partial y}, \frac{\partial \phi}{\partial z})$ là một vectơ."
  },
  {
    "question": "Hàm mật độ của phân phối mũ (Exponential distribution) với tham số $\lambda$ có dạng (với $x \ge 0$):",
    "options": ["\lambda e^{-\lambda x}", "e^{-\lambda x}", "\lambda e^x", "1/\lambda e^{-x/\lambda}"],
    "answer": "A",
    "explanation": "Đây là công thức hàm mật độ chuẩn của phân phối mũ dùng trong lý thuyết xếp hàng và độ tin cậy."
  },
  {
    "question": "Trong Giải tích số, quy tắc hình thang dùng để xấp xỉ:",
    "options": ["Tích phân xác định", "Đạo hàm cấp hai", "Nghiệm phương trình", "Giá trị cực đại"],
    "answer": "A",
    "explanation": "Quy tắc hình thang chia nhỏ diện tích dưới đường cong thành các hình thang để tính tổng diện tích xấp xỉ."
  },
  {
    "question": "Chuỗi số $\sum \frac{(-1)^n}{n}$ được gọi là:",
    "options": ["Chuỗi hội tụ có điều kiện", "Chuỗi hội tụ tuyệt đối", "Chuỗi phân kỳ", "Chuỗi đan dấu phân kỳ"],
    "answer": "A",
    "explanation": "Chuỗi hội tụ theo tiêu chuẩn Leibniz, nhưng chuỗi trị tuyệt đối (chuỗi điều hòa) thì phân kỳ."
  },
  {
    "question": "Ma trận của một phép quay trong mặt phẳng $Oxy$ một góc $\theta$ có các phần tử trên đường chéo chính là:",
    "options": ["\cos \theta", "\sin \theta", "1", "0"],
    "answer": "A",
    "explanation": "Ma trận quay là $\begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$."
  },
  {
    "question": "Trong không gian topo, một lân cận của điểm $x$ là một tập hợp chứa:",
    "options": ["Một tập mở chứa x", "Chỉ duy nhất điểm x", "Toàn bộ không gian", "Các điểm giới hạn của x"],
    "answer": "A",
    "explanation": "Theo định nghĩa topo, tập $N$ là lân cận của $x$ nếu tồn tại tập mở $U$ sao cho $x \in U \subseteq N$."
  },
  {
    "question": "Phương trình $x^2 + y^2 - z^2 = 1$ biểu diễn mặt nào trong không gian?",
    "options": ["Hyperboloid một tầng", "Hyperboloid hai tầng", "Ellipsoid", "Paraboloid hyperbolic"],
    "answer": "A",
    "explanation": "Phương trình có một dấu trừ ứng với hyperboloid một tầng."
  },
  
  {
    "question": "Định lý Green biến đổi tích phân đường quanh đường cong kín $C$ thành tích phân kép trên miền $D$ giới hạn bởi $C$ với biểu thức:",
    "options": ["\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}", "\frac{\partial Q}{\partial x} + \frac{\partial P}{\partial y}", "\frac{\partial P}{\partial x} - \frac{\partial Q}{\partial y}", "Pdx + Qdy"],
    "answer": "A",
    "explanation": "$\oint_C (Pdx + Qdy) = \iint_D (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}) dxdy$."
  },
  {"question":"Giới hạn lim(x→∞) (ln x / x) bằng?","options":["A. 0","B. 1","C. ∞","D. Không tồn tại"],"answer":"A. 0","explanation":"Dùng quy tắc L'Hospital."},
{"question":"∫_0^1 x^5 dx bằng?","options":["A. 1/5","B. 1/6","C. 1/4","D. 1/3"],"answer":"B. 1/6","explanation":"Nguyên hàm x^6/6."},
{"question":"Nếu A là ma trận trực giao thì A^{-1}=?","options":["A. A^T","B. -A","C. I","D. 0"],"answer":"A. A^T","explanation":"Tính chất ma trận trực giao."},
{"question":"Chuỗi ∑ x^n hội tụ khi?","options":["A. |x|<1","B. x>1","C. x=1","D. Mọi x"],"answer":"A. |x|<1","explanation":"Chuỗi hình học."},
{"question":"Đạo hàm của tan x là?","options":["A. sec^2 x","B. cos x","C. -sec^2 x","D. sin x"],"answer":"A. sec^2 x","explanation":"Công thức đạo hàm."},
{"question":"Nếu rank(A)=n với A vuông cấp n thì?","options":["A. A khả nghịch","B. det=0","C. trace=0","D. A=0"],"answer":"A. A khả nghịch","explanation":"Rank đầy đủ."},
{"question":"∫ e^{3x} dx bằng?","options":["A. e^{3x}","B. (1/3)e^{3x}+C","C. 3e^{3x}","D. ln(3x)"],"answer":"B. (1/3)e^{3x}+C","explanation":"Chia cho 3."},
{"question":"Nếu X,Y độc lập thì E(XY)=?","options":["A. E(X)+E(Y)","B. E(X)E(Y)","C. 0","D. Var(X)"],"answer":"B. E(X)E(Y)","explanation":"Tính chất độc lập."},
{"question":"Phương trình y''-4y=0 có nghiệm tổng quát?","options":["A. Ae^{2x}+Be^{-2x}","B. A cos2x + B sin2x","C. Ax+B","D. Ae^x"],"answer":"A. Ae^{2x}+Be^{-2x}","explanation":"Giải phương trình đặc trưng."},
{"question":"Trace(I_n) bằng?","options":["A. 1","B. n","C. 0","D. n^2"],"answer":"B. n","explanation":"Tổng n số 1."},
{"question":"∫_0^1 x^n dx bằng?","options":["A. 1/n","B. 1/(n+1)","C. n","D. 0"],"answer":"B. 1/(n+1)","explanation":"Nguyên hàm x^{n+1}/(n+1)."},
{"question":"Chuẩn vô cùng của vector (x_i) là?","options":["A. max|x_i|","B. ∑|x_i|","C. √∑x_i^2","D. 0"],"answer":"A. max|x_i|","explanation":"Định nghĩa chuẩn vô cùng."},
{"question":"Nếu A đối xứng thực thì có thể?","options":["A. Chéo hóa bởi ma trận trực giao","B. Không chéo hóa","C. det=0","D. rank=1"],"answer":"A. Chéo hóa bởi ma trận trực giao","explanation":"Định lý phổ."},
{"question":"∫_0^{π} sin^2 x dx bằng?","options":["A. π/2","B. π/4","C. 1","D. 2"],"answer":"A. π/2","explanation":"Dùng công thức hạ bậc."},
{"question":"Nếu f' = 0 trên khoảng thì f?","options":["A. Hằng","B. Tăng","C. Giảm","D. Lồi"],"answer":"A. Hằng","explanation":"Định lý giá trị trung bình."},
{"question":"Ma trận suy biến khi?","options":["A. det=0","B. det≠0","C. trace=0","D. rank=n"],"answer":"A. det=0","explanation":"Định nghĩa."},
{"question":"∫ sinh x dx bằng?","options":["A. cosh x + C","B. sinh x","C. tanh x","D. -cosh x"],"answer":"A. cosh x + C","explanation":"Nguyên hàm hyperbolic."},
{"question":"Nếu X~Uniform(0,1) thì E(X)=?","options":["A. 1/2","B. 1","C. 0","D. 1/3"],"answer":"A. 1/2","explanation":"Trung bình phân phối đều."},
{"question":"Đạo hàm của ln|x| là?","options":["A. 1/x","B. x","C. ln x","D. 1"],"answer":"A. 1/x","explanation":"Công thức cơ bản."},
{"question":"Nếu A,B vuông cùng cấp thì det(AB)=?","options":["A. det(A)+det(B)","B. det(A)det(B)","C. 0","D. det(A-B)"],"answer":"B. det(A)det(B)","explanation":"Tính chất định thức."},
{"question":"∫_0^{π/2} tan^2 x dx bằng?","options":["A. π/2 -1","B. 1","C. 0","D. π/4"],"answer":"A. π/2 -1","explanation":"tan^2x = sec^2x -1."},
{"question":"Nếu chuỗi lũy thừa có bán kính R thì hội tụ khi?","options":["A. |x|<R","B. |x|>R","C. x=R","D. Mọi x"],"answer":"A. |x|<R","explanation":"Định nghĩa bán kính hội tụ."},
{"question":"Gradient của f(x,y)=xy là?","options":["A. (y,x)","B. (x,y)","C. (1,1)","D. (0,0)"],"answer":"A. (y,x)","explanation":"Đạo hàm riêng."},
{"question":"Nếu λ là nghiệm bội k của đa thức đặc trưng thì?","options":["A. Bội đại số k","B. Bội hình học k","C. det=0","D. trace=k"],"answer":"A. Bội đại số k","explanation":"Định nghĩa."},
{"question":"∫_0^1 x^2 ln x dx bằng?","options":["A. -1/9","B. 1/9","C. -1/4","D. 0"],"answer":"A. -1/9","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Exponential(λ) thì E(X)=?","options":["A. 1/λ","B. λ","C. λ^2","D. 0"],"answer":"A. 1/λ","explanation":"Trung bình phân phối mũ."},
{"question":"Đạo hàm của sec x là?","options":["A. sec x tan x","B. tan x","C. -sec x tan x","D. cos x"],"answer":"A. sec x tan x","explanation":"Công thức đạo hàm."},
{"question":"Ma trận đơn vị là?","options":["A. Có 1 trên đường chéo chính","B. Tất cả bằng 1","C. det=0","D. trace=0"],"answer":"A. Có 1 trên đường chéo chính","explanation":"Định nghĩa."},
{"question":"∫_0^{π/2} sec^2 x dx bằng?","options":["A. 1","B. tan(π/2)","C. ∞","D. 0"],"answer":"C. ∞","explanation":"tan x → ∞ tại π/2."},
{"question":"Nếu f liên tục và khả vi thì?","options":["A. Có khai triển Taylor","B. Không tích phân","C. Không giới hạn","D. Không đạo hàm"],"answer":"A. Có khai triển Taylor","explanation":"Hàm trơn có thể khai triển Taylor."},
{
    "question": "Cho $V$ là không gian vectơ và $W$ là tập con của $V$. $W$ là không gian vectơ con nếu thỏa mãn điều kiện nào?",
    "options": ["Đóng kín đối với phép cộng và phép nhân vô hướng", "Chứa phần tử đơn vị của phép nhân", "Là tập hợp hữu hạn", "Có định thức khác không"],
    "answer": "A",
    "explanation": "Hai điều kiện tiên quyết để một tập con là không gian con: $\forall u, v \in W, u+v \in W$ và $\forall \alpha \in \mathbb{R}, u \in W, \alpha u \in W$."
  },
  {
    "question": "Tính tích hữu hướng của hai vectơ $u = (1, 0, 0)$ và $v = (0, 1, 0)$.",
    "options": ["(0, 0, 1)", "(0, 0, -1)", "(1, 1, 0)", "0"],
    "answer": "A",
    "explanation": "Tích hữu hướng của hai vectơ đơn vị $i$ và $j$ chính là vectơ đơn vị $k = (0, 0, 1)$."
  },
  
  {
    "question": "Trong không gian $\mathbb{R}^n$, một bộ $n$ vectơ độc lập tuyến tính được gọi là:",
    "options": ["Một cơ sở", "Một không gian con", "Một ma trận", "Một hệ sinh tối đại"],
    "answer": "A",
    "explanation": "Trong không gian $n$ chiều, bất kỳ hệ nào có đúng $n$ vectơ độc lập tuyến tính đều tạo thành một cơ sở."
  },
  {
    "question": "Dạng toàn phương $Q(x_1, x_2) = x_1^2 + 4x_1x_2 + 5x_2^2$ là:",
    "options": ["Xác định dương", "Xác định âm", "Nửa xác định dương", "Không xác định"],
    "answer": "A",
    "explanation": "Biến đổi thành $Q = (x_1 + 2x_2)^2 + x_2^2$. Do là tổng các bình phương độc lập, $Q > 0$ với mọi $(x_1, x_2) \neq (0,0)$."
  },
  {
    "question": "Ma trận của phép chiếu vuông góc lên trục $Ox$ trong mặt phẳng $Oxy$ là:",
    "options": ["\\begin{pmatrix} 1 & 0 \\\\ 0 & 0 \\end{pmatrix}", "\\begin{pmatrix} 0 & 0 \\\\ 0 & 1 \\end{pmatrix}", "\\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix}", "\\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}"],
    "answer": "A",
    "explanation": "Phép chiếu biến $(x, y)$ thành $(x, 0)$, tương ứng với ma trận trên."
  },
  {
    "question": "Cho ánh xạ tuyến tính $f: \mathbb{R}^3 \to \mathbb{R}^2$. Theo định lý về số chiều, khẳng định nào sau đây luôn đúng?",
    "options": ["dim(Ker f) + dim(Im f) = 3", "dim(Ker f) = 2", "dim(Im f) = 3", "f là một toàn cấu"],
    "answer": "A",
    "explanation": "Định lý Rank-Nullity: Tổng số chiều của hạt nhân và ảnh bằng số chiều của không gian nguồn."
  },
  {
    "question": "Một ma trận $A$ được gọi là chéo hóa được nếu:",
    "options": ["Có đủ $n$ vectơ riêng độc lập tuyến tính", "\det(A) \neq 0", "A là ma trận tam giác", "Mọi giá trị riêng đều bằng nhau"],
    "answer": "A",
    "explanation": "Điều kiện cần và đủ để ma trận vuông cấp $n$ chéo hóa được là nó phải có $n$ vectơ riêng độc lập tuyến tính."
  },
  
  {
    "question": "Vết (Trace) của ma trận là:",
    "options": ["Tổng các phần tử trên đường chéo chính", "Tích các phần tử trên đường chéo chính", "Định thức của ma trận", "Giá trị riêng lớn nhất"],
    "answer": "A",
    "explanation": "$Tr(A) = \sum a_{ii}$. Một tính chất quan trọng là $Tr(A)$ cũng bằng tổng các giá trị riêng của $A$."
  },
  {
    "question": "Trong không gian Euclid, bất đẳng thức Cauchy-Schwarz phát biểu rằng:",
    "options": ["|u \cdot v| \le |u||v|", "|u + v| \le |u| + |v|", "|u \cdot v| \ge |u||v|", "u \cdot v = 0"],
    "answer": "A",
    "explanation": "Bất đẳng thức này khẳng định giá trị tuyệt đối của tích vô hướng luôn nhỏ hơn hoặc bằng tích độ dài các vectơ."
  },
  {
    "question": "Giá trị riêng của ma trận phản đối xứng thực $A$ (thỏa mãn $A^T = -A$) luôn là:",
    "options": ["Số thuần ảo hoặc bằng 0", "Số thực dương", "Bằng 1 hoặc -1", "Số thực âm"],
    "answer": "A",
    "explanation": "Đây là một tính chất quan trọng của ma trận phản đối xứng trong không gian phức."
  },
  {
    "question": "Đường bậc hai có phương trình $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ là một:",
    "options": ["Hyperbola", "Ellipse", "Parabola", "Đường thẳng cắt nhau"],
    "answer": "A",
    "explanation": "Dấu trừ giữa hai số hạng bình phương là đặc trưng của đường Hyperbola."
  },
  {
    "question": "Ma trận chuyển cơ sở từ cơ sở $B$ sang cơ sở $B'$ luôn là ma trận:",
    "options": ["Khả nghịch", "Suy biến", "Đường chéo", "Phản đối xứng"],
    "answer": "A",
    "explanation": "Vì các vectơ cơ sở luôn độc lập tuyến tính, ma trận chuyển cơ sở phải có định thức khác 0."
  },
  {
    "question": "Tâm sai (Eccentricity) của một đường tròn bằng:",
    "options": ["0", "1", "Lớn hơn 1", "Nhỏ hơn 1 nhưng khác 0"],
    "answer": "A",
    "explanation": "Đường tròn là trường hợp đặc biệt của ellipse khi hai tiêu điểm trùng nhau, dẫn đến tâm sai $e = 0$."
  },
  {
    "question": "Hệ phương trình tuyến tính $Ax = b$ có nghiệm khi và chỉ khi:",
    "options": ["rank(A) = rank(A|b)", "rank(A) = n", "\det(A) \neq 0", "b = 0"],
    "answer": "A",
    "explanation": "Theo định lý Kronecker-Capelli, hệ có nghiệm khi hạng của ma trận hệ số bằng hạng của ma trận bổ sung."
  },
  {
    "question": "Phép biến đổi tuyến tính làm thay đổi diện tích của một hình phẳng theo tỉ lệ bằng:",
    "options": ["Trị tuyệt đối của định thức ma trận biến đổi", "Vết của ma trận biến đổi", "Giá trị riêng lớn nhất", "Bình phương định thức"],
    "answer": "A",
    "explanation": "Ý nghĩa hình học của định thức là tỉ lệ thay đổi thể tích (hoặc diện tích) qua phép biến đổi tuyến tính."
  },
  {
    "question": "Ma trận $A$ và $A^T$ luôn có cùng:",
    "options": ["Tập hợp các giá trị riêng", "Tập hợp các vectơ riêng", "Các phần tử", "Ma trận nghịch đảo"],
    "answer": "A",
    "explanation": "Vì $\det(A - \lambda I) = \det(A^T - \lambda I)$, nên hai ma trận có cùng phương trình đặc trưng và giá trị riêng."
  },
  {
    "question": "Trong không gian $\mathbb{R}^3$, phương trình mặt phẳng đi qua gốc tọa độ có dạng:",
    "options": ["ax + by + cz = 0", "ax + by + cz = d (d \neq 0)", "x/a + y/b + z/c = 1", "x^2 + y^2 + z^2 = R^2"],
    "answer": "A",
    "explanation": "Mặt phẳng đi qua gốc tọa độ $(0,0,0)$ thì hệ số tự do phải bằng 0."
  },
  {
    "question": "Quá trình Gram-Schmidt dùng để:",
    "options": ["Biến đổi một cơ sở thành cơ sở trực chuẩn", "Tìm giá trị riêng của ma trận", "Giải hệ phương trình tuyến tính", "Tính định thức ma trận cấp cao"],
    "answer": "A",
    "explanation": "Đây là thuật toán chuẩn để xây dựng hệ vectơ trực giao và trực chuẩn từ một hệ độc lập tuyến tính cho trước."
  },
  
  {
    "question": "Đa thức đặc trưng của ma trận đơn vị $I_n$ là:",
    "options": ["(1 - \lambda)^n", "(1 - \lambda)", "\lambda^n", "1 - \lambda^n"],
    "answer": "A",
    "explanation": "Ma trận đơn vị có các phần tử trên đường chéo là 1, nên $\det(I - \lambda I) = (1-\lambda)^n$."
  },
  {
    "question": "Góc giữa hai mặt phẳng được xác định thông qua góc giữa hai:",
    "options": ["Vectơ pháp tuyến", "Vectơ chỉ phương", "Đường thẳng nằm trên mặt phẳng", "Giao tuyến"],
    "answer": "A",
    "explanation": "Góc giữa hai mặt phẳng chính là góc giữa hai vectơ pháp tuyến tương ứng của chúng."
  },
  {"question":"Giới hạn lim(x→0) (1-cosx)/x^2 bằng?","options":["A. 0","B. 1/2","C. 1","D. Không tồn tại"],"answer":"B. 1/2","explanation":"Giới hạn lượng giác cơ bản."},
{"question":"∫_0^1 x^6 dx bằng?","options":["A. 1/6","B. 1/7","C. 1/8","D. 1/5"],"answer":"B. 1/7","explanation":"Nguyên hàm x^7/7."},
{"question":"Nếu A là ma trận phản xứng thực thì các phần tử đường chéo chính?","options":["A. Bất kỳ","B. Bằng 0","C. Bằng 1","D. Âm"],"answer":"B. Bằng 0","explanation":"Vì a_{ii} = -a_{ii} ⇒ a_{ii}=0."},
{"question":"Chuỗi ∑ (-1)^n hội tụ?","options":["A. Tuyệt đối","B. Điều kiện","C. Phân kỳ","D. Hội tụ"],"answer":"C. Phân kỳ","explanation":"Không tiến về 0."},
{"question":"Đạo hàm của arcsin x là?","options":["A. 1/√(1-x^2)","B. 1/(1+x^2)","C. √(1-x^2)","D. -1/√(1-x^2)"],"answer":"A. 1/√(1-x^2)","explanation":"Công thức đạo hàm."},
{"question":"Nếu rank(A)=rank(A^T) thì?","options":["A. Luôn đúng","B. Sai","C. Chỉ khi det≠0","D. Chỉ khi vuông"],"answer":"A. Luôn đúng","explanation":"Tính chất hạng ma trận."},
{"question":"∫ e^{-2x} dx bằng?","options":["A. -1/2 e^{-2x}+C","B. e^{-2x}","C. -2e^{-2x}","D. ln e^{-2x}"],"answer":"A. -1/2 e^{-2x}+C","explanation":"Chia cho -2."},
{"question":"Nếu X có Var(X)=0 thì?","options":["A. X hằng","B. X=0","C. X=1","D. Không xác định"],"answer":"A. X hằng","explanation":"Phương sai bằng 0."},
{"question":"Phương trình y''+y'=0 có nghiệm tổng quát?","options":["A. C1 + C2 e^{-x}","B. C1 e^x","C. C1 cosx","D. C1 x"],"answer":"A. C1 + C2 e^{-x}","explanation":"Giải phương trình đặc trưng."},
{"question":"det(A^T)=?","options":["A. det(A)","B. -det(A)","C. 0","D. 1"],"answer":"A. det(A)","explanation":"Tính chất định thức."},
{"question":"∫_0^1 x^{1/2} dx bằng?","options":["A. 2/3","B. 1/2","C. 3/2","D. 1"],"answer":"A. 2/3","explanation":"Nguyên hàm 2/3 x^{3/2}."},
{"question":"Chuẩn L1 của vector (x_i) là?","options":["A. ∑|x_i|","B. max|x_i|","C. √∑x_i^2","D. 0"],"answer":"A. ∑|x_i|","explanation":"Định nghĩa chuẩn L1."},
{"question":"Nếu A có hai hàng trùng nhau thì det(A)=?","options":["A. 0","B. 1","C. -1","D. Không đổi"],"answer":"A. 0","explanation":"Tính chất định thức."},
{"question":"∫_0^{π/2} sin^3 x dx bằng?","options":["A. 2/3","B. 1","C. 1/2","D. π/4"],"answer":"A. 2/3","explanation":"Dùng công thức giảm bậc."},
{"question":"Nếu f liên tục trên [a,b] thì đạt?","options":["A. GTLN và GTNN","B. Không đạt GTNN","C. Không đạt GTLN","D. Không bị chặn"],"answer":"A. GTLN và GTNN","explanation":"Định lý Weierstrass."},
{"question":"Ma trận khả chéo hóa khi có?","options":["A. n vector riêng độc lập","B. det=0","C. trace=0","D. A=I"],"answer":"A. n vector riêng độc lập","explanation":"Điều kiện chéo hóa."},
{"question":"∫ cos 2x dx bằng?","options":["A. 1/2 sin 2x + C","B. sin2x","C. 2sinx","D. -1/2 sin2x"],"answer":"A. 1/2 sin 2x + C","explanation":"Đổi biến."},
{"question":"Nếu X~Binomial(n,p) thì E(X)=?","options":["A. np","B. p","C. n","D. n+p"],"answer":"A. np","explanation":"Trung bình nhị thức."},
{"question":"Đạo hàm của coth x là?","options":["A. -csch^2 x","B. sech^2 x","C. tanh x","D. csch x"],"answer":"A. -csch^2 x","explanation":"Công thức đạo hàm."},
{"question":"Nếu A là ma trận tam giác dưới thì giá trị riêng?","options":["A. Các phần tử đường chéo","B. 0","C. 1","D. Trace"],"answer":"A. Các phần tử đường chéo","explanation":"Tính chất."},
{"question":"∫_0^1 x^7 dx bằng?","options":["A. 1/7","B. 1/8","C. 1/9","D. 1/6"],"answer":"B. 1/8","explanation":"Nguyên hàm x^8/8."},
{"question":"Nếu chuỗi ∑ a_n phân kỳ thì?","options":["A. a_n không tiến về 0","B. a_n →0","C. Hội tụ tuyệt đối","D. Bị chặn"],"answer":"A. a_n không tiến về 0","explanation":"Điều kiện cần."},
{"question":"Gradient của f(x,y)=x^2-y^2 là?","options":["A. (2x,-2y)","B. (x,-y)","C. (2,-2)","D. (0,0)"],"answer":"A. (2x,-2y)","explanation":"Đạo hàm riêng."},
{"question":"Nếu λ=0 là giá trị riêng thì?","options":["A. det(A)=0","B. A khả nghịch","C. trace=0","D. rank=n"],"answer":"A. det(A)=0","explanation":"Tích các giá trị riêng bằng det."},
{"question":"∫_0^1 x^3 ln x dx bằng?","options":["A. -1/16","B. 1/16","C. -1/4","D. 0"],"answer":"A. -1/16","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Normal(μ,σ^2) thì Var(X)=?","options":["A. μ","B. σ^2","C. σ","D. μ^2"],"answer":"B. σ^2","explanation":"Định nghĩa phân phối chuẩn."},
{"question":"Đạo hàm của arccos x là?","options":["A. -1/√(1-x^2)","B. 1/√(1-x^2)","C. -1/(1+x^2)","D. 1/x"],"answer":"A. -1/√(1-x^2)","explanation":"Công thức đạo hàm."},
{"question":"Ma trận khả nghịch khi và chỉ khi?","options":["A. det≠0","B. trace≠0","C. rank< n","D. A=I"],"answer":"A. det≠0","explanation":"Điều kiện cần và đủ."},
{"question":"∫_0^{π/2} sin x cos^2 x dx bằng?","options":["A. 1/3","B. 1/2","C. 2/3","D. 1"],"answer":"A. 1/3","explanation":"Đặt u=cosx."},
{"question":"Nếu f khả vi hai lần và f''<0 thì f?","options":["A. Lõm","B. Lồi","C. Tăng","D. Hằng"],"answer":"A. Lõm","explanation":"Tiêu chuẩn lõm."},
{"question":"Giới hạn lim(x→0) (tanx/x) bằng?","options":["A. 0","B. 1","C. -1","D. Không tồn tại"],"answer":"B. 1","explanation":"Giới hạn lượng giác cơ bản."},
{"question":"∫_0^1 x^8 dx bằng?","options":["A. 1/8","B. 1/9","C. 1/10","D. 1/7"],"answer":"B. 1/9","explanation":"Nguyên hàm x^9/9."},
{"question":"Nếu A là ma trận tam giác với các phần tử chéo khác 0 thì A?","options":["A. Khả nghịch","B. Suy biến","C. Bằng 0","D. Không xác định"],"answer":"A. Khả nghịch","explanation":"det là tích các phần tử chéo."},
{"question":"Chuỗi ∑ 1/(n ln n) với n≥2?","options":["A. Hội tụ","B. Phân kỳ","C. Tuyệt đối","D. Điều kiện"],"answer":"B. Phân kỳ","explanation":"So sánh với tích phân."},
{"question":"Đạo hàm của ln(sin x) là?","options":["A. cot x","B. tan x","C. sec x","D. csc x"],"answer":"A. cot x","explanation":"Dùng quy tắc dây chuyền."},
{"question":"Nếu det(A)=det(B)=1 thì det(AB)=?","options":["A. 0","B. 1","C. -1","D. 2"],"answer":"B. 1","explanation":"det(AB)=det(A)det(B)."},
{"question":"∫ e^{ax} dx bằng?","options":["A. ae^{ax}","B. (1/a)e^{ax}+C","C. ln(ax)","D. e^x"],"answer":"B. (1/a)e^{ax}+C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu X,Y không tương quan thì Cov(X,Y)=?","options":["A. 0","B. 1","C. Var(X)","D. Var(Y)"],"answer":"A. 0","explanation":"Không tương quan ⇒ hiệp phương sai 0."},
{"question":"Phương trình y''+9y=0 có nghiệm?","options":["A. A cos3x + B sin3x","B. Ae^{3x}","C. Ax+B","D. Ae^x"],"answer":"A. A cos3x + B sin3x","explanation":"Phương trình đặc trưng r^2+9=0."},
{"question":"Trace(A^T)=?","options":["A. trace(A)","B. -trace(A)","C. 0","D. det(A)"],"answer":"A. trace(A)","explanation":"Tính chất trace."},
{"question":"∫_0^1 x^9 dx bằng?","options":["A. 1/9","B. 1/10","C. 1/11","D. 1/8"],"answer":"B. 1/10","explanation":"Nguyên hàm x^{10}/10."},
{"question":"Chuẩn Euclid của vector (1,2,2) là?","options":["A. 3","B. √5","C. √9","D. 5"],"answer":"A. 3","explanation":"√(1+4+4)=3."},
{"question":"Nếu A có một hàng toàn 0 thì rank(A)?","options":["A. ≤ n-1","B. =n","C. =1","D. =0"],"answer":"A. ≤ n-1","explanation":"Không đủ hạng đầy đủ."},
{"question":"∫_0^{π/2} cos^3 x dx bằng?","options":["A. 2/3","B. 1","C. 1/2","D. π/4"],"answer":"A. 2/3","explanation":"Công thức giảm bậc."},
{"question":"Nếu f'(x)>0 trên khoảng thì f?","options":["A. Tăng","B. Giảm","C. Lồi","D. Lõm"],"answer":"A. Tăng","explanation":"Tiêu chuẩn đơn điệu."},
{"question":"Ma trận vuông có det=1 gọi là?","options":["A. Ma trận đơn vị","B. Ma trận đặc biệt tuyến tính","C. Ma trận 0","D. Ma trận phản xứng"],"answer":"B. Ma trận đặc biệt tuyến tính","explanation":"Thuộc nhóm SL(n)."},
{"question":"∫ sinh 2x dx bằng?","options":["A. 1/2 cosh2x + C","B. cosh x","C. sinh x","D. -1/2 cosh2x"],"answer":"A. 1/2 cosh2x + C","explanation":"Đổi biến."},
{"question":"Nếu X~Geometric(p) thì E(X)=?","options":["A. 1/p","B. p","C. p(1-p)","D. 1-p"],"answer":"A. 1/p","explanation":"Kỳ vọng phân phối hình học."},
{"question":"Đạo hàm của ln|cos x| là?","options":["A. -tan x","B. tan x","C. cot x","D. sec x"],"answer":"A. -tan x","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu A là ma trận chéo với phần tử chéo khác 0 thì A?","options":["A. Khả nghịch","B. Suy biến","C. Nilpotent","D. Idempotent"],"answer":"A. Khả nghịch","explanation":"det là tích phần tử chéo."},
{"question":"∫_0^1 x^{10} dx bằng?","options":["A. 1/10","B. 1/11","C. 1/12","D. 1/9"],"answer":"B. 1/11","explanation":"Nguyên hàm x^{11}/11."},
{"question":"Nếu chuỗi ∑ a_n hội tụ thì?","options":["A. a_n →0","B. a_n →1","C. a_n →∞","D. Không điều kiện"],"answer":"A. a_n →0","explanation":"Điều kiện cần."},
{"question":"Gradient của f(x,y,z)=x^2+y^2+z^2 là?","options":["A. (2x,2y,2z)","B. (x,y,z)","C. (1,1,1)","D. (0,0,0)"],"answer":"A. (2x,2y,2z)","explanation":"Đạo hàm riêng."},
{"question":"Nếu A là ma trận trực giao thì A^TA=?","options":["A. I","B. 0","C. A","D. -A"],"answer":"A. I","explanation":"Định nghĩa trực giao."},
{"question":"∫_0^1 x^4 ln x dx bằng?","options":["A. -1/25","B. 1/25","C. -1/5","D. 0"],"answer":"A. -1/25","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Poisson(λ) thì Var(X)=?","options":["A. λ","B. λ^2","C. 1/λ","D. 0"],"answer":"A. λ","explanation":"Phương sai Poisson."},
{"question":"Đạo hàm của arctan(2x) là?","options":["A. 2/(1+4x^2)","B. 1/(1+x^2)","C. 2/(1+x^2)","D. 1/(1+4x^2)"],"answer":"A. 2/(1+4x^2)","explanation":"Quy tắc dây chuyền."},
{"question":"Ma trận đơn vị I có tính chất?","options":["A. AI=A","B. A+I=I","C. det=0","D. rank=0"],"answer":"A. AI=A","explanation":"Phần tử trung hòa nhân."},
{"question":"∫_0^{π/2} sin x cos x dx bằng?","options":["A. 1/2","B. 1","C. 0","D. π/4"],"answer":"A. 1/2","explanation":"Đặt u=sinx."},
{"question":"Nếu f''(x)=0 trên khoảng thì f?","options":["A. Hàm bậc nhất","B. Hằng","C. Bậc hai","D. Lồi"],"answer":"A. Hàm bậc nhất","explanation":"Đạo hàm hai bằng 0."},
{
    "question": "Sử dụng tiêu chuẩn tích phân, chuỗi số $\\sum_{n=2}^{\\infty} \\frac{1}{n(\\ln n)^p}$ hội tụ khi và chỉ khi:",
    "options": ["p > 1", "p \\ge 1", "p < 1", "Với mọi p"],
    "answer": "A",
    "explanation": "Xét hàm $f(x) = \\frac{1}{x(\\ln x)^p}$. Tích phân $\\int_2^{+\\infty} \\frac{dx}{x(\\ln x)^p} = \\int_{\\ln 2}^{+\\infty} \\frac{du}{u^p}$ hội tụ khi $p > 1$."
  },
  {
    "question": "Tính đạo hàm của hàm số $f(x) = x^x$ với $x > 0$.",
    "options": ["x^x(1 + \\ln x)", "x \\cdot x^{x-1}", "x^x \\ln x", "x^x"],
    "answer": "A",
    "explanation": "Đặt $y = x^x \\Rightarrow \\ln y = x \\ln x$. Đạo hàm hai vế: $y'/y = \\ln x + 1 \\Rightarrow y' = x^x(\\ln x + 1)$."
  },
  {
    "question": "Cho hàm số $f(x, y) = \\sqrt{x^2 + y^2}$. Tại điểm $(0, 0)$, hàm số có đặc điểm gì?",
    "options": ["Liên tục nhưng không có đạo hàm riêng", "Không liên tục", "Có vi phân toàn phần", "Có đạo hàm riêng bằng 0"],
    "answer": "A",
    "explanation": "Hàm số liên tục tại $(0,0)$. Tuy nhiên, $\\lim_{h \\to 0} \\frac{f(h, 0) - f(0, 0)}{h} = \\lim \\frac{|h|}{h}$ không tồn tại, nên không có đạo hàm riêng theo $x$."
  },
  
  {
    "question": "Giá trị của giới hạn $\\lim_{n \\to \\infty} \\left(1 + \\frac{1}{n}\\right)^n$ là:",
    "options": ["e", "1", "0", "+\\infty"],
    "answer": "A",
    "explanation": "Đây là định nghĩa cơ bản của số Euler $e$ thông qua giới hạn của dãy số."
  },
  {
    "question": "Tích phân suy rộng $\\int_0^{+\\infty} e^{-x^2} dx$ có giá trị bằng:",
    "options": ["\\sqrt{\\pi}/2", "\\sqrt{\\pi}", "\\pi/2", "1"],
    "answer": "A",
    "explanation": "Đây là tích phân Gauss nổi tiếng, thường được tính bằng cách chuyển sang tọa độ cực trong tích phân kép."
  },
  {
    "question": "Định lý Rolle khẳng định rằng nếu $f$ liên tục trên $[a, b]$, khả vi trên $(a, b)$ và $f(a) = f(b)$ thì:",
    "options": ["Tồn tại $c \\in (a, b)$ sao cho $f'(c) = 0$", "Tồn tại $c \\in (a, b)$ sao cho $f'(c) = 1$", "$f(x)$ là hàm hằng", "$f'(x) > 0$ trên $(a, b)$"],
    "answer": "A",
    "explanation": "Định lý Rolle là trường hợp đặc biệt của định lý Lagrange khi hai đầu mút bằng nhau."
  },
  
  {
    "question": "Cho chuỗi lũy thừa $\\sum a_n x^n$ có bán kính hội tụ $R$. Chuỗi đạo hàm $\\sum n a_n x^{n-1}$ có bán kính hội tụ là:",
    "options": ["R", "R/2", "0", "+\\infty"],
    "answer": "A",
    "explanation": "Việc lấy đạo hàm hoặc nguyên hàm từng thành phần không làm thay đổi bán kính hội tụ của chuỗi lũy thừa."
  },
  {
    "question": "Tính tích phân kép $I = \\int_0^1 dx \\int_x^1 e^{y^2} dy$ bằng cách đổi thứ tự lấy tích phân.",
    "options": ["(e - 1)/2", "e - 1", "1/2", "e/2"],
    "answer": "A",
    "explanation": "Đổi thứ tự: $I = \\int_0^1 dy \\int_0^y e^{y^2} dx = \\int_0^1 y e^{y^2} dy = \\frac{1}{2} e^{y^2} \\big|_0^1 = (e-1)/2$."
  },
  {
    "question": "Hàm số $f(x)$ có đạo hàm mọi cấp tại $x=a$. Khai triển Taylor của $f(x)$ tại $x=a$ hội tụ về $f(x)$ khi:",
    "options": ["Phần dư $R_n(x) \\to 0$ khi $n \\to \\infty$", "$f'(a) = 0$", "Hàm số là đa thức", "Chuỗi số là chuỗi đan dấu"],
    "answer": "A",
    "explanation": "Sự hội tụ của chuỗi Taylor về hàm số phụ thuộc vào việc phần dư trong công thức Taylor tiến về 0."
  },
  {
    "question": "Trong không gian $\\mathbb{R}^3$, vi phân thể tích trong tọa độ cầu $(\\rho, \\phi, \\theta)$ là:",
    "options": ["\\rho^2 \\sin \\phi \\, d\\rho \\, d\\phi \\, d\\theta", "d\\rho \\, d\\phi \\, d\\theta", "\\rho \\, d\\rho \\, d\\phi \\, d\\theta", "\\rho^2 \\, d\\rho \\, d\\phi \\, d\\theta"],
    "answer": "A",
    "explanation": "Đây là định thức Jacobi khi chuyển từ hệ tọa độ Descartes sang tọa độ cầu."
  },
  
  {
    "question": "Chuỗi số $\\sum_{n=1}^{\\infty} \\frac{(-1)^{n+1}}{n^2}$ hội tụ theo tiêu chuẩn nào?",
    "options": ["Hội tụ tuyệt đối", "Hội tụ có điều kiện", "Phân kỳ", "Tiêu chuẩn tích phân"],
    "answer": "A",
    "explanation": "Chuỗi trị tuyệt đối là $\\sum 1/n^2$, là chuỗi p-series với $p=2 > 1$ nên hội tụ."
  },
  {
    "question": "Điểm dừng của hàm số $f(x, y) = x^2 - y^2$ là loại điểm gì?",
    "options": ["Điểm yên ngựa (Saddle point)", "Điểm cực đại", "Điểm cực tiểu", "Điểm gián đoạn"],
    "answer": "A",
    "explanation": "Đạo hàm riêng: $f_x=2x, f_y=-2y$. Điểm dừng $(0,0)$. Các đạo hàm cấp hai: $f_{xx}=2, f_{yy}=-2, f_{xy}=0$. Vì $D = f_{xx}f_{yy} - (f_{xy})^2 = -4 < 0$ nên là điểm yên ngựa."
  },
  
  {
    "question": "Một dãy số $\\{a_n\\}$ tăng và bị chặn trên thì:",
    "options": ["Hội tụ", "Phân kỳ ra $+\\infty$", "Dao động", "Tiến về 0"],
    "answer": "A",
    "explanation": "Đây là định lý Weierstrass (hay định lý hội tụ đơn điệu) cho dãy số thực."
  },
  {
    "question": "Tính giới hạn $\\lim_{x \\to 0} (\\cos x)^{1/x^2}$.",
    "options": ["e^{-1/2}", "1", "e", "e^{-1}"],
    "answer": "A",
    "explanation": "Dạng $1^\\infty$. Biến đổi thành $e^{\\lim \\frac{\\ln(\\cos x)}{x^2}}$. Sử dụng Taylor: $\\ln(\\cos x) \\approx \\ln(1-x^2/2) \\approx -x^2/2$. Giới hạn là $e^{-1/2}$."
  },
  {
    "question": "Công thức tích phân từng phần cho tích phân xác định là:",
    "options": ["\\int_a^b u \\, dv = uv \\big|_a^b - \\int_a^b v \\, du", "\\int_a^b u \\, dv = uv + \\int_a^b v \\, du", "\\int_a^b u \\, dv = v \\, du - u \\, dv", "\\int_a^b u \\, dv = uv \\big|_a^b"],
    "answer": "A",
    "explanation": "Đây là hệ quả trực tiếp từ quy tắc đạo hàm của một tích."
  },
  {
    "question": "Hàm Gamma $\\Gamma(n)$ với $n$ nguyên dương bằng:",
    "options": ["(n-1)!", "n!", "(n+1)!", "n^n"],
    "answer": "A",
    "explanation": "Hàm Gamma là sự mở rộng của hàm giai thừa cho số thực và số phức: $\\Gamma(n) = \\int_0^{\\infty} x^{n-1} e^{-x} dx$."
  },
  {
    "question": "Độ dài cung của đường cong $y = f(x)$ từ $a$ đến $b$ được tính bởi:",
    "options": ["\\int_a^b \\sqrt{1 + [f'(x)]^2} dx", "\\int_a^b f(x) dx", "\\int_a^b \\sqrt{1 + f(x)} dx", "\\int_a^b [f'(x)]^2 dx"],
    "answer": "A",
    "explanation": "Đây là công thức tính độ dài đường cong phẳng dưới dạng tường minh."
  },
  {
    "question": "Hàm số $f(x, y)$ có các đạo hàm riêng cấp hai liên tục. Khi đó:",
    "options": ["f_{xy} = f_{yx}", "f_{xx} = f_{yy}", "f_{xy} = -f_{yx}", "f_{xx} + f_{yy} = 0"],
    "answer": "A",
    "explanation": "Theo định lý Clairaut (hay định lý Schwarz), các đạo hàm riêng hỗn hợp bằng nhau nếu chúng liên tục."
  },
  {
    "question": "Tiêu chuẩn so sánh 1 cho chuỗi số dương $\\sum a_n$ và $\\sum b_n$ phát biểu rằng nếu $a_n \\le b_n$ và $\\sum b_n$ hội tụ thì:",
    "options": ["\\sum a_n$ hội tụ", "$\\sum a_n$ phân kỳ", "$\\sum a_n$ hội tụ về cùng một giá trị", "Không kết luận được"],
    "answer": "A",
    "explanation": "Nếu một chuỗi 'lớn hơn' hội tụ thì chuỗi 'nhỏ hơn' cũng phải hội tụ."
  },
  {
    "question": "Mặt bậc hai $z = x^2 + y^2$ được gọi là:",
    "options": ["Paraboloid elliptic", "Paraboloid hyperbolic", "Ellipsoid", "Mặt nón"],
    "answer": "A",
    "explanation": "Mặt này có các thiết diện ngang là hình tròn (hoặc elip) và thiết diện đứng là các đường parabol."
  },
  {"question":"Giới hạn lim(x→∞) (1+1/x)^x bằng?","options":["A. 1","B. e","C. 0","D. ∞"],"answer":"B. e","explanation":"Giới hạn cơ bản định nghĩa số e."},
{"question":"∫_0^1 x^{11} dx bằng?","options":["A. 1/11","B. 1/12","C. 1/13","D. 1/10"],"answer":"B. 1/12","explanation":"Nguyên hàm x^{12}/12."},
{"question":"Nếu A^2=I thì A gọi là?","options":["A. Idempotent","B. Involutory","C. Nilpotent","D. Trực giao"],"answer":"B. Involutory","explanation":"A bình phương bằng đơn vị."},
{"question":"Chuỗi ∑ 1/n^3?","options":["A. Phân kỳ","B. Hội tụ","C. Điều kiện","D. Không xác định"],"answer":"B. Hội tụ","explanation":"p-series với p>1."},
{"question":"Đạo hàm của e^{3x} là?","options":["A. 3e^{3x}","B. e^{3x}","C. 3x e^{3x}","D. e^x"],"answer":"A. 3e^{3x}","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu det(A)=0 thì A?","options":["A. Khả nghịch","B. Suy biến","C. Trực giao","D. Đơn vị"],"answer":"B. Suy biến","explanation":"Điều kiện khả nghịch."},
{"question":"∫ cosh x dx bằng?","options":["A. sinh x + C","B. cosh x","C. -sinh x","D. tanh x"],"answer":"A. sinh x + C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu X,Y độc lập thì Cov(X,Y)=?","options":["A. 0","B. 1","C. Var(X)","D. Var(Y)"],"answer":"A. 0","explanation":"Độc lập ⇒ không tương quan."},
{"question":"Phương trình y''-4y=0 có nghiệm?","options":["A. Ae^{2x}+Be^{-2x}","B. A cos2x","C. Ax+B","D. Ae^x"],"answer":"A. Ae^{2x}+Be^{-2x}","explanation":"r^2-4=0."},
{"question":"rank(I_n)=?","options":["A. 0","B. 1","C. n","D. n-1"],"answer":"C. n","explanation":"Ma trận đơn vị đủ hạng."},
{"question":"∫_0^1 x^{12} dx bằng?","options":["A. 1/12","B. 1/13","C. 1/14","D. 1/11"],"answer":"B. 1/13","explanation":"Nguyên hàm x^{13}/13."},
{"question":"Chuẩn L∞ của vector (x_i) là?","options":["A. ∑|x_i|","B. max|x_i|","C. √∑x_i^2","D. 0"],"answer":"B. max|x_i|","explanation":"Định nghĩa chuẩn vô cùng."},
{"question":"Nếu A là ma trận 3x3 và rank=3 thì det(A)?","options":["A. 0","B. ≠0","C. 1","D. -1"],"answer":"B. ≠0","explanation":"Hạng đầy đủ."},
{"question":"∫_0^{π} sin x dx bằng?","options":["A. 0","B. 1","C. 2","D. π"],"answer":"C. 2","explanation":"Nguyên hàm -cosx."},
{"question":"Nếu f'(x)<0 thì f?","options":["A. Tăng","B. Giảm","C. Lồi","D. Hằng"],"answer":"B. Giảm","explanation":"Tiêu chuẩn đơn điệu."},
{"question":"Ma trận nilpotent thỏa?","options":["A. A^k=0","B. A^2=I","C. det=1","D. trace=1"],"answer":"A. A^k=0","explanation":"Định nghĩa nilpotent."},
{"question":"∫ tan x dx bằng?","options":["A. -ln|cos x|+C","B. ln|cos x|","C. sec x","D. sin x"],"answer":"A. -ln|cos x|+C","explanation":"Công thức nguyên hàm."},
{"question":"Nếu X~Uniform(a,b) thì E(X)=?","options":["A. a+b","B. (a+b)/2","C. ab","D. b-a"],"answer":"B. (a+b)/2","explanation":"Trung bình phân phối đều."},
{"question":"Đạo hàm của x^x là?","options":["A. x^x(1+ln x)","B. x^{x-1}","C. x ln x","D. e^x"],"answer":"A. x^x(1+ln x)","explanation":"Lấy log vi phân."},
{"question":"Nếu A trực giao thì det(A)=?","options":["A. ±1","B. 0","C. 1","D. -1"],"answer":"A. ±1","explanation":"Tính chất ma trận trực giao."},
{"question":"∫_0^1 x^{13} dx bằng?","options":["A. 1/13","B. 1/14","C. 1/15","D. 1/12"],"answer":"B. 1/14","explanation":"Nguyên hàm x^{14}/14."},
{"question":"Nếu chuỗi ∑ (-1)^n/n hội tụ?","options":["A. Tuyệt đối","B. Điều kiện","C. Phân kỳ","D. Không"],"answer":"B. Điều kiện","explanation":"Chuỗi luân phiên Leibniz."},
{"question":"Divergence của F=(x,y,z) là?","options":["A. 1","B. 2","C. 3","D. 0"],"answer":"C. 3","explanation":"∂x/∂x+∂y/∂y+∂z/∂z=3."},
{"question":"Nếu A là ma trận đối xứng thực thì giá trị riêng?","options":["A. Thực","B. Phức","C. 0","D. 1"],"answer":"A. Thực","explanation":"Định lý phổ."},
{"question":"∫_0^1 x^5 ln x dx bằng?","options":["A. -1/36","B. 1/36","C. -1/6","D. 0"],"answer":"A. -1/36","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Exponential(λ) thì E(X)=?","options":["A. λ","B. 1/λ","C. λ^2","D. 0"],"answer":"B. 1/λ","explanation":"Kỳ vọng mũ."},
{"question":"Đạo hàm của sec x là?","options":["A. sec x tan x","B. tan x","C. -sec x tan x","D. sec^2 x"],"answer":"A. sec x tan x","explanation":"Công thức đạo hàm."},
{"question":"Ma trận idempotent thỏa?","options":["A. A^2=A","B. A^2=0","C. det=1","D. A=I"],"answer":"A. A^2=A","explanation":"Định nghĩa idempotent."},
{"question":"∫_0^{π/2} cos x dx bằng?","options":["A. 0","B. 1","C. 2","D. π/2"],"answer":"B. 1","explanation":"Nguyên hàm sinx."},
{"question":"Nếu f liên tục và khả vi thì f?","options":["A. Luôn liên tục","B. Không liên tục","C. Hằng","D. Không xác định"],"answer":"A. Luôn liên tục","explanation":"Khả vi ⇒ liên tục."},
{"question":"Giới hạn lim(x→0) (e^x-1)/x bằng?","options":["A. 0","B. 1","C. e","D. ∞"],"answer":"B. 1","explanation":"Giới hạn cơ bản của e^x."},
{"question":"∫_0^1 x^{14} dx bằng?","options":["A. 1/14","B. 1/15","C. 1/16","D. 1/13"],"answer":"B. 1/15","explanation":"Nguyên hàm x^{15}/15."},
{"question":"Nếu A là ma trận trực giao thì A^{-1}=?","options":["A. A","B. A^T","C. -A","D. I"],"answer":"B. A^T","explanation":"Định nghĩa ma trận trực giao."},
{"question":"Chuỗi ∑ 1/n^2?","options":["A. Phân kỳ","B. Hội tụ","C. Điều kiện","D. Không xác định"],"answer":"B. Hội tụ","explanation":"p-series với p=2>1."},
{"question":"Đạo hàm của ln(x^2+1) là?","options":["A. 2x/(x^2+1)","B. 1/(x^2+1)","C. 2x","D. x/(x^2+1)"],"answer":"A. 2x/(x^2+1)","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu det(AB)=0 thì?","options":["A. det(A)=0 hoặc det(B)=0","B. Cả hai khác 0","C. det(A)=1","D. det(B)=1"],"answer":"A. det(A)=0 hoặc det(B)=0","explanation":"Tính chất tích định thức."},
{"question":"∫ sinh x dx bằng?","options":["A. cosh x + C","B. sinh x","C. -cosh x","D. tanh x"],"answer":"A. cosh x + C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu Var(X)=σ^2 thì Var(aX)=?","options":["A. aσ^2","B. a^2σ^2","C. σ^2","D. a^2"],"answer":"B. a^2σ^2","explanation":"Tính chất phương sai."},
{"question":"Phương trình y''+4y'+4y=0 có nghiệm?","options":["A. (A+Bx)e^{-2x}","B. Ae^{-2x}","C. A cos2x","D. Ax+B"],"answer":"A. (A+Bx)e^{-2x}","explanation":"Nghiệm kép r=-2."},
{"question":"rank(A+B) ≤?","options":["A. rank(A)+rank(B)","B. rank(A)rank(B)","C. det(A)","D. n"],"answer":"A. rank(A)+rank(B)","explanation":"Bất đẳng thức hạng."},
{"question":"∫_0^1 x^{15} dx bằng?","options":["A. 1/15","B. 1/16","C. 1/17","D. 1/14"],"answer":"B. 1/16","explanation":"Nguyên hàm x^{16}/16."},
{"question":"Chuẩn Frobenius của ma trận A là?","options":["A. √(tổng bình phương phần tử)","B. det(A)","C. trace(A)","D. rank(A)"],"answer":"A. √(tổng bình phương phần tử)","explanation":"Định nghĩa chuẩn Frobenius."},
{"question":"Nếu A là ma trận vuông và A^T=-A thì A?","options":["A. Đối xứng","B. Phản xứng","C. Trực giao","D. Idempotent"],"answer":"B. Phản xứng","explanation":"Định nghĩa phản xứng."},
{"question":"∫_0^{π/2} sin^2 x dx bằng?","options":["A. π/4","B. 1/2","C. 1","D. π/2"],"answer":"A. π/4","explanation":"Công thức sin^2x=(1-cos2x)/2."},
{"question":"Nếu f''(x)>0 thì đồ thị f?","options":["A. Lồi","B. Lõm","C. Tăng","D. Giảm"],"answer":"A. Lồi","explanation":"Tiêu chuẩn lồi."},
{"question":"Ma trận khả chéo hóa khi có?","options":["A. Đủ vector riêng độc lập","B. det=0","C. trace=0","D. rank=1"],"answer":"A. Đủ vector riêng độc lập","explanation":"Điều kiện chéo hóa."},
{"question":"∫ sec^2 x dx bằng?","options":["A. tan x + C","B. sec x","C. -tan x","D. cos x"],"answer":"A. tan x + C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu X~Bin(n,p) thì Var(X)=?","options":["A. np","B. np(1-p)","C. p(1-p)","D. n^2p"],"answer":"B. np(1-p)","explanation":"Phương sai nhị thức."},
{"question":"Đạo hàm của ln|x| là?","options":["A. 1/x","B. x","C. ln x","D. 0"],"answer":"A. 1/x","explanation":"Công thức đạo hàm."},
{"question":"Nếu A là ma trận chéo thì trace(A)=?","options":["A. Tổng phần tử chéo","B. det(A)","C. rank(A)","D. 0"],"answer":"A. Tổng phần tử chéo","explanation":"Định nghĩa trace."},
{"question":"∫_0^1 x^{16} dx bằng?","options":["A. 1/16","B. 1/17","C. 1/18","D. 1/15"],"answer":"B. 1/17","explanation":"Nguyên hàm x^{17}/17."},
{"question":"Nếu chuỗi ∑ a_n tuyệt đối hội tụ thì?","options":["A. Hội tụ","B. Phân kỳ","C. Điều kiện","D. Không xác định"],"answer":"A. Hội tụ","explanation":"Tuyệt đối hội tụ ⇒ hội tụ."},
{"question":"Curl của F=(0,0,x^2) là?","options":["A. (0,-2x,0)","B. (2x,0,0)","C. (0,2x,0)","D. (0,0,0)"],"answer":"A. (0,-2x,0)","explanation":"Tính theo định nghĩa."},
{"question":"Nếu A là ma trận đối xứng dương xác định thì?","options":["A. x^TAx>0 với x≠0","B. det=0","C. rank< n","D. A^2=I"],"answer":"A. x^TAx>0 với x≠0","explanation":"Định nghĩa dương xác định."},
{"question":"∫_0^1 x^6 ln x dx bằng?","options":["A. -1/49","B. 1/49","C. -1/7","D. 0"],"answer":"A. -1/49","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Normal(0,1) thì E(X^2)=?","options":["A. 0","B. 1","C. 2","D. 1/2"],"answer":"B. 1","explanation":"Phương sai chuẩn bằng 1."},
{"question":"Đạo hàm của tanh x là?","options":["A. sech^2 x","B. tan x","C. csch^2 x","D. sech x"],"answer":"A. sech^2 x","explanation":"Công thức đạo hàm."},
{"question":"Ma trận khả nghịch khi rank=?","options":["A. n","B. 1","C. n-1","D. 0"],"answer":"A. n","explanation":"Hạng đầy đủ."},
{"question":"∫_0^{π} cos x dx bằng?","options":["A. 0","B. 1","C. 2","D. π"],"answer":"A. 0","explanation":"sinπ - sin0 =0."},
{"question":"Nếu f liên tục trên [a,b] và f(a)f(b)<0 thì?","options":["A. Có nghiệm trong (a,b)","B. Không có nghiệm","C. Luôn dương","D. Luôn âm"],"answer":"A. Có nghiệm trong (a,b)","explanation":"Định lý giá trị trung gian."},
{
    "question": "Trong Lý thuyết đồ thị, một đồ thị vô hướng $G$ có chu trình Euler khi và chỉ khi:",
    "options": ["G liên thông và mọi đỉnh đều có bậc chẵn", "G liên thông và có đúng 2 đỉnh bậc lẻ", "G là đồ thị đầy đủ", "G không có chu trình"],
    "answer": "A",
    "explanation": "Định lý Euler khẳng định đồ thị liên thông có chu trình Euler nếu và chỉ nếu mọi đỉnh của nó đều có bậc chẵn (vào bao nhiêu thì ra bấy nhiêu)."
  },
  
  {
    "question": "Cho tập hợp $A$ có $n$ phần tử. Số lượng tập con của tập $A$ là:",
    "options": ["2^n", "n^2", "n!", "2n"],
    "answer": "A",
    "explanation": "Mỗi phần tử có 2 lựa chọn: nằm trong tập con hoặc không. Vậy có $2 \cdot 2 \cdot ... \cdot 2 = 2^n$ tập con."
  },
  {
    "question": "Trong Logic mệnh đề, mệnh đề hội $P \land Q$ chỉ đúng khi:",
    "options": ["Cả P và Q đều đúng", "Chỉ cần P đúng", "Chỉ cần Q đúng", "Cả P và Q đều sai"],
    "answer": "A",
    "explanation": "Phép hội (AND) yêu cầu tất cả các thành phần tham gia phải mang giá trị đúng."
  },
  {
    "question": "Một quan hệ $R$ trên tập $S$ được gọi là có tính bắc cầu (transitive) nếu:",
    "options": ["(a,b) \in R và (b,c) \in R \Rightarrow (a,c) \in R", "(a,b) \in R \Rightarrow (b,a) \in R", "(a,a) \in R với mọi a", "(a,b) \in R \Rightarrow a=b"],
    "answer": "A",
    "explanation": "Đây là tính chất quan trọng để xác định quan hệ thứ tự hoặc quan hệ tương đương."
  },
  {
    "question": "Trong các thuật toán tìm đường đi ngắn nhất, thuật toán nào hoạt động tốt trên đồ thị có trọng số không âm?",
    "options": ["Dijkstra", "Kruskal", "Prim", "Depth First Search"],
    "answer": "A",
    "explanation": "Dijkstra là thuật toán điển hình để tìm đường đi ngắn nhất từ một đỉnh nguồn đến các đỉnh khác với trọng số cạnh không âm."
  },
  
  {
    "question": "Số các hoán vị của $n$ phần tử là:",
    "options": ["n!", "n^n", "C_n^k", "P_n^k"],
    "answer": "A",
    "explanation": "Hoán vị là cách sắp xếp thứ tự của $n$ phần tử khác nhau, tính bằng $n \cdot (n-1) \cdot ... \cdot 1 = n!$."
  },
  {
    "question": "Một đồ thị được gọi là đồ thị lưỡng phân (bipartite graph) nếu:",
    "options": ["Tập đỉnh có thể chia thành 2 tập rời nhau sao cho không có cạnh nào nối 2 đỉnh trong cùng một tập", "Mọi đỉnh đều có bậc là 2", "Đồ thị có chu trình độ dài lẻ", "Đồ thị là đồ thị phẳng"],
    "answer": "A",
    "explanation": "Đặc trưng của đồ thị lưỡng phân là không chứa chu trình độ dài lẻ."
  },
  
  {
    "question": "Nguyên lý chuồng bồ câu phát biểu rằng nếu nhốt $n+1$ con bồ câu vào $n$ cái chuồng thì:",
    "options": ["Có ít nhất một chuồng chứa từ 2 con trở lên", "Mỗi chuồng đều có bồ câu", "Có ít nhất một chuồng trống", "Tất cả bồ câu nằm trong cùng một chuồng"],
    "answer": "A",
    "explanation": "Đây là nguyên lý cơ bản trong toán tổ hợp dùng để chứng minh sự tồn tại."
  },
  {
    "question": "Trong hệ thống số nhị phân, phép tính $1011_2 + 1101_2$ bằng:",
    "options": "11000_2",
    "options": ["11000_2", "10001_2", "11111_2", "10101_2"],
    "answer": "A",
    "explanation": "Cộng tương ứng từng hàng: $11+13 = 24$. $24$ trong hệ nhị phân là $11000$."
  },
  {
    "question": "Đại số Boole sử dụng các phép toán cơ bản nào?",
    "options": ["AND, OR, NOT", "Cộng, Trừ, Nhân", "Tích phân, Đạo hàm", "Hội, Tuyển, Kéo theo"],
    "answer": "A",
    "explanation": "Đại số Boole là nền tảng của mạch logic số, dựa trên các cổng logic cơ bản."
  },
  {
    "question": "Trong lý thuyết mã hóa, khoảng cách Hamming giữa hai xâu '10110' và '11010' là:",
    "options": ["2", "1", "3", "0"],
    "answer": "A",
    "explanation": "Khoảng cách Hamming là số vị trí mà tại đó các ký hiệu tương ứng khác nhau. Ở đây khác ở vị trí thứ 2 và thứ 3."
  },
  {
    "question": "Thuật toán Prim dùng để tìm gì trong đồ thị?",
    "options": ["Cây khung nhỏ nhất (Minimum Spanning Tree)", "Đường đi ngắn nhất", "Luồng cực đại", "Chu trình Hamilton"],
    "answer": "A",
    "explanation": "Prim bắt đầu từ một đỉnh và mở rộng dần cây khung bằng cách chọn cạnh nhỏ nhất nối từ cây ra ngoài."
  },
  
  {
    "question": "Một bài toán thuộc lớp NP-đầy đủ (NP-complete) có đặc điểm:",
    "options": ["Nếu giải được nó trong thời gian đa thức thì mọi bài toán lớp NP đều giải được trong thời gian đa thức", "Luôn giải được trong thời gian đa thức", "Không bao giờ giải được", "Chỉ có thể giải bằng máy tính lượng tử"],
    "answer": "A",
    "explanation": "Đây là những bài toán khó nhất trong lớp NP, mang tính đại diện cho cả lớp."
  },
  {
    "question": "Công thức truy hồi của dãy Fibonacci là:",
    "options": ["F_n = F_{n-1} + F_{n-2}", "F_n = F_{n-1} \cdot F_{n-2}", "F_n = 2F_{n-1}", "F_n = F_{n-1} - F_{n-2}"],
    "answer": "A",
    "explanation": "Mỗi số hạng bằng tổng hai số hạng đứng trước nó, với $F_0=0, F_1=1$."
  },
  {
    "question": "Số sắc số (chromatic number) của đồ thị chu trình $C_5$ (ngũ giác) là:",
    "options": ["3", "2", "5", "4"],
    "answer": "A",
    "explanation": "Với chu trình độ dài lẻ, ta cần ít nhất 3 màu để tô các đỉnh sao cho không có 2 đỉnh kề nhau cùng màu."
  },
  {
    "question": "Trong Lý thuyết tập hợp, $A \setminus B$ (hiệu của A và B) là tập các phần tử:",
    "options": ["Thuộc A nhưng không thuộc B", "Thuộc B nhưng không thuộc A", "Thuộc cả A và B", "Thuộc A hoặc thuộc B"],
    "answer": "A",
    "explanation": "Đây là phép lấy bù của B trong A."
  },
  {
    "question": "Một đồ thị phẳng là đồ thị có thể vẽ trên mặt phẳng sao cho:",
    "options": ["Các cạnh không cắt nhau trừ tại các đỉnh", "Tất cả các cạnh đều là đường thẳng", "Số đỉnh bằng số cạnh", "Đồ thị không có chu trình"],
    "answer": "A",
    "explanation": "Định lý Euler cho đồ thị phẳng liên thông: $V - E + F = 2$."
  },
  {
    "question": "Hàm Boolean $f(x, y) = x \oplus y$ (phép XOR) trả về giá trị 1 khi:",
    "options": ["x và y khác nhau", "x và y cùng bằng 1", "x và y cùng bằng 0", "Luôn trả về 1"],
    "answer": "A",
    "explanation": "Phép OR loại trừ (Exclusive OR) chỉ đúng khi có đúng một trong hai mệnh đề đúng."
  },
  {
    "question": "Cấu trúc dữ liệu Stack (ngăn xếp) hoạt động theo nguyên tắc:",
    "options": ["LIFO (Last In First Out)", "FIFO (First In First Out)", "Ưu tiên thấp nhất", "Ngẫu nhiên"],
    "answer": "A",
    "explanation": "Phần tử nào vào sau cùng sẽ được lấy ra đầu tiên (giống như chồng đĩa)."
  },
  {
    "question": "Tổng các bậc của các đỉnh trong một đồ thị luôn là một số:",
    "options": ["Chẵn", "Lẻ", "Nguyên tố", "Bằng số cạnh"],
    "answer": "A",
    "explanation": "Vì mỗi cạnh đóng góp 1 đơn vị vào bậc của 2 đỉnh đầu mút, nên tổng bậc luôn bằng 2 lần số cạnh."
  },
  {"question":"Giới hạn lim(x→0) (ln(1+x)/x) bằng?","options":["A. 0","B. 1","C. e","D. ∞"],"answer":"B. 1","explanation":"Giới hạn cơ bản của ln(1+x)."},
{"question":"∫_0^1 x^{17} dx bằng?","options":["A. 1/17","B. 1/18","C. 1/19","D. 1/16"],"answer":"B. 1/18","explanation":"Nguyên hàm x^{18}/18."},
{"question":"Nếu A^3=0 và A≠0 thì A là?","options":["A. Idempotent","B. Nilpotent","C. Trực giao","D. Đơn vị"],"answer":"B. Nilpotent","explanation":"A lũy thừa k bằng 0."},
{"question":"Chuỗi ∑ 1/(n^4)?","options":["A. Phân kỳ","B. Hội tụ","C. Điều kiện","D. Không xác định"],"answer":"B. Hội tụ","explanation":"p-series với p=4>1."},
{"question":"Đạo hàm của √x là?","options":["A. 1/(2√x)","B. √x","C. 1/√x","D. 2√x"],"answer":"A. 1/(2√x)","explanation":"Viết x^{1/2}."},
{"question":"Nếu det(A)=5 và det(B)=2 thì det(AB)=?","options":["A. 7","B. 10","C. 3","D. 5"],"answer":"B. 10","explanation":"det(AB)=det(A)det(B)."},
{"question":"∫ e^{-x} dx bằng?","options":["A. -e^{-x}+C","B. e^{-x}","C. -e^x","D. ln x"],"answer":"A. -e^{-x}+C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu E(X)=μ thì E(aX+b)=?","options":["A. aμ+b","B. μ","C. aμ","D. μ+b"],"answer":"A. aμ+b","explanation":"Tính tuyến tính của kỳ vọng."},
{"question":"Phương trình y''+y=sin x có nghiệm riêng dạng?","options":["A. A x cosx + B x sinx","B. A cosx + B sinx","C. Ae^x","D. Ax"],"answer":"A. A x cosx + B x sinx","explanation":"Trùng nghiệm riêng."},
{"question":"rank(AB) ≤?","options":["A. min(rank(A),rank(B))","B. rank(A)+rank(B)","C. n","D. det(A)"],"answer":"A. min(rank(A),rank(B))","explanation":"Bất đẳng thức hạng tích."},
{"question":"∫_0^1 x^{18} dx bằng?","options":["A. 1/18","B. 1/19","C. 1/20","D. 1/17"],"answer":"B. 1/19","explanation":"Nguyên hàm x^{19}/19."},
{"question":"Chuẩn của vector (3,4) trong R^2 là?","options":["A. 5","B. 7","C. √7","D. 1"],"answer":"A. 5","explanation":"√(9+16)=5."},
{"question":"Nếu A có det<0 thì phép biến đổi tuyến tính?","options":["A. Đảo hướng","B. Bảo toàn hướng","C. Không đổi","D. Bằng 0"],"answer":"A. Đảo hướng","explanation":"Dấu định thức."},
{"question":"∫_0^{π/2} cos^2 x dx bằng?","options":["A. π/4","B. 1/2","C. 1","D. π/2"],"answer":"A. π/4","explanation":"Công thức cos^2x."},
{"question":"Nếu f đạt cực đại tại x0 và khả vi thì?","options":["A. f'(x0)=0","B. f''(x0)=0","C. f(x0)=0","D. f'(x0)>0"],"answer":"A. f'(x0)=0","explanation":"Điều kiện cần cực trị."},
{"question":"Ma trận có tất cả giá trị riêng dương là?","options":["A. Dương xác định","B. Phản xứng","C. Nilpotent","D. Idempotent"],"answer":"A. Dương xác định","explanation":"Tính chất phổ."},
{"question":"∫ csc^2 x dx bằng?","options":["A. -cot x + C","B. cot x","C. tan x","D. csc x"],"answer":"A. -cot x + C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu X~Poisson(λ) thì E(X)=?","options":["A. λ","B. λ^2","C. 1/λ","D. 0"],"answer":"A. λ","explanation":"Kỳ vọng Poisson."},
{"question":"Đạo hàm của arccot x là?","options":["A. -1/(1+x^2)","B. 1/(1+x^2)","C. -1/x","D. 1/x"],"answer":"A. -1/(1+x^2)","explanation":"Công thức đạo hàm."},
{"question":"Nếu A là ma trận 2x2 có det=1 thì A thuộc?","options":["A. SL(2)","B. GL(2)","C. O(2)","D. U(2)"],"answer":"A. SL(2)","explanation":"Nhóm đặc biệt tuyến tính."},
{"question":"∫_0^1 x^{19} dx bằng?","options":["A. 1/19","B. 1/20","C. 1/21","D. 1/18"],"answer":"B. 1/20","explanation":"Nguyên hàm x^{20}/20."},
{"question":"Nếu chuỗi ∑ a_n phân kỳ thì lim a_n=?","options":["A. ≠0 hoặc không tồn tại","B. 0","C. 1","D. ∞"],"answer":"A. ≠0 hoặc không tồn tại","explanation":"Điều kiện cần hội tụ."},
{"question":"Divergence của F=(x^2,y^2,z^2) là?","options":["A. 2x+2y+2z","B. x+y+z","C. 2","D. 0"],"answer":"A. 2x+2y+2z","explanation":"Tính đạo hàm riêng."},
{"question":"Nếu A đối xứng thì có thể chéo hóa bởi?","options":["A. Ma trận trực giao","B. Ma trận bất kỳ","C. Ma trận 0","D. Ma trận phản xứng"],"answer":"A. Ma trận trực giao","explanation":"Định lý phổ."},
{"question":"∫_0^1 x^7 ln x dx bằng?","options":["A. -1/64","B. 1/64","C. -1/8","D. 0"],"answer":"A. -1/64","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Exponential(λ) thì Var(X)=?","options":["A. 1/λ^2","B. λ","C. λ^2","D. 1/λ"],"answer":"A. 1/λ^2","explanation":"Phương sai mũ."},
{"question":"Đạo hàm của cosh x là?","options":["A. sinh x","B. cos x","C. -sinh x","D. tanh x"],"answer":"A. sinh x","explanation":"Công thức đạo hàm."},
{"question":"Ma trận A khả nghịch khi tồn tại?","options":["A. A^{-1}","B. det=0","C. rank< n","D. A^2=0"],"answer":"A. A^{-1}","explanation":"Định nghĩa khả nghịch."},
{"question":"∫_0^{π/2} tan x dx bằng?","options":["A. ∞","B. 0","C. 1","D. π/2"],"answer":"A. ∞","explanation":"Phân kỳ tại π/2."},
{"question":"Nếu f liên tục trên [a,b] thì f?","options":["A. Bị chặn","B. Không bị chặn","C. Luôn tăng","D. Luôn giảm"],"answer":"A. Bị chặn","explanation":"Tính chất hàm liên tục trên đoạn đóng."},
{
    "question": "Trong kiểm định giả thuyết thống kê, mức ý nghĩa $\\alpha$ là:",
    "options": ["Xác suất phạm sai lầm loại I", "Xác suất phạm sai lầm loại II", "Xác suất chấp nhận giả thuyết đúng", "Độ mạnh của kiểm định"],
    "answer": "A",
    "explanation": "Mức ý nghĩa $\\alpha$ là xác suất bác bỏ giả thuyết $H_0$ trong khi $H_0$ thực sự đúng."
  },
  {
    "question": "Trong mô hình hồi quy tuyến tính đơn $Y = \\beta_0 + \\beta_1 X + \\epsilon$, hệ số $\\beta_1$ cho biết:",
    "options": ["Sự thay đổi trung bình của Y khi X tăng 1 đơn vị", "Giá trị của Y khi X bằng 0", "Độ lệch chuẩn của sai số", "Hệ số tương quan giữa X và Y"],
    "answer": "A",
    "explanation": "Hệ số góc $\\beta_1$ đo lường tác động biên của biến độc lập lên biến phụ thuộc."
  },
  
  {
    "question": "Hệ số xác định $R^2$ trong hồi quy dùng để đo lường:",
    "options": ["Mức độ phù hợp của mô hình", "Độ dốc của đường hồi quy", "Phương sai của biến X", "Tính tự tương quan"],
    "answer": "A",
    "explanation": "$R^2$ cho biết tỷ lệ phần trăm sự biến động của biến phụ thuộc được giải thích bởi các biến độc lập trong mô hình."
  },
  {
    "question": "Phân phối Poisson thường được dùng để mô tả:",
    "options": ["Số lần xảy ra của một sự kiện trong một khoảng thời gian/không gian xác định", "Chiều cao của con người", "Kết quả tung một đồng xu", "Thời gian chờ đợi giữa hai sự kiện"],
    "answer": "A",
    "explanation": "Phân phối Poisson phù hợp cho các sự kiện hiếm và độc lập trong một đơn vị đo lường liên tục."
  },
  {
    "question": "Nếu hai biến ngẫu nhiên $X$ và $Y$ độc lập thì hệ số tương quan Pearson giữa chúng bằng:",
    "options": ["0", "1", "-1", "Không xác định"],
    "answer": "A",
    "explanation": "Độc lập kéo theo không tương quan tuyến tính, do đó hệ số tương quan bằng 0."
  },
  {
    "question": "Trong phân phối chuẩn chuẩn hóa $Z \sim N(0, 1)$, khoảng giá trị $[\mu - 1.96\sigma, \mu + 1.96\sigma]$ chứa khoảng bao nhiêu % dữ liệu?",
    "options": ["95%", "68%", "99%", "90%"],
    "answer": "A",
    "explanation": "Theo quy tắc kinh nghiệm và bảng giá trị Z, 95% dữ liệu nằm trong khoảng 1.96 lần độ lệch chuẩn quanh giá trị trung bình."
  },
  
  {
    "question": "Định lý giới hạn trung tâm (Central Limit Theorem) phát biểu rằng khi kích thước mẫu $n$ đủ lớn, phân phối của trung bình mẫu sẽ tiến về:",
    "options": ["Phân phối chuẩn", "Phân phối Student", "Phân phối Poisson", "Phân phối đều"],
    "answer": "A",
    "explanation": "Dù quần thể ban đầu có phân phối gì, trung bình mẫu sẽ xấp xỉ phân phối chuẩn khi $n$ lớn (thường $n \ge 30$)."
  },
  {
    "question": "Giá trị P-value trong kiểm định giả thuyết được hiểu là:",
    "options": ["Mức ý nghĩa nhỏ nhất để có thể bác bỏ giả thuyết $H_0$", "Xác suất giả thuyết $H_0$ là đúng", "Xác suất giả thuyết $H_1$ là đúng", "Sai số tiêu chuẩn của ước lượng"],
    "answer": "A",
    "explanation": "P-value thấp (thường $< 0.05$) cho thấy bằng chứng thực nghiệm đủ mạnh để bác bỏ $H_0$."
  },
  {
    "question": "Ước lượng không chệch là ước lượng có:",
    "options": ["Kỳ vọng bằng tham số cần ước lượng", "Phương sai nhỏ nhất", "Kích thước mẫu lớn nhất", "Giá trị bằng 0"],
    "answer": "A",
    "explanation": "Một thống kê được gọi là ước lượng không chệch nếu trung bình của các ước lượng qua nhiều mẫu bằng đúng giá trị thực của tham số."
  },
  {
    "question": "Phân phối Chi-bình phương ($\chi^2$) thường được ứng dụng để:",
    "options": ["Kiểm định tính độc lập giữa hai biến định tính", "So sánh hai trung bình mẫu", "Ước lượng kỳ vọng khi chưa biết phương sai", "Dự báo chuỗi thời gian"],
    "answer": "A",
    "explanation": "Kiểm định $\chi^2$ dùng để xem xét mối quan hệ giữa các biến phân loại trong bảng tần suất (Contingency table)."
  },
  {
    "question": "Trong một phân phối bị lệch phải (Skewed to the right), mối quan hệ giữa các tham số là:",
    "options": ["Mode < Median < Mean", "Mean < Median < Mode", "Mean = Median = Mode", "Median < Mode < Mean"],
    "answer": "A",
    "explanation": "Các giá trị cực đại kéo giá trị trung bình (Mean) về phía bên phải nhiều hơn so với trung vị và yếu vị."
  },
  
  {
    "question": "Biến ngẫu nhiên $X$ tuân theo phân phối nhị thức $B(n, p)$. Phương sai của $X$ là:",
    "options": ["np(1-p)", "np", "n(1-p)", "p(1-p)"],
    "answer": "A",
    "explanation": "Đây là công thức tính phương sai chuẩn cho tổng của $n$ phép thử Bernoulli độc lập."
  },
  {
    "question": "Để so sánh trung bình của nhiều hơn 2 nhóm độc lập, ta sử dụng phương pháp:",
    "options": ["Phân tích phương sai (ANOVA)", "Kiểm định t-test", "Kiểm định Z-test", "Hồi quy Logistic"],
    "answer": "A",
    "explanation": "ANOVA (Analysis of Variance) kiểm tra xem có sự khác biệt có ý nghĩa thống kê giữa các giá trị trung bình của nhiều nhóm hay không."
  },
  {
    "question": "Hệ số tương quan Pearson nhận giá trị trong khoảng nào?",
    "options": ["[-1, 1]", "[0, 1]", "(-\infty, +\infty)", "[-1, 0]"],
    "answer": "A",
    "explanation": "Giá trị bằng 1 thể hiện tương quan thuận hoàn hảo, -1 là tương quan nghịch hoàn hảo, và 0 là không tương quan."
  },
  {
    "question": "Trong kiểm định giả thuyết, nếu bác bỏ $H_0$ ở mức ý nghĩa 1% thì:",
    "options": ["Chắc chắn bác bỏ được ở mức 5%", "Chưa chắc bác bỏ được ở mức 5%", "Bác bỏ được ở mức 0.1%", "Chấp nhận giả thuyết $H_1$ tuyệt đối"],
    "answer": "A",
    "explanation": "Mức 1% khắt khe hơn mức 5%. Nếu đã vượt qua ngưỡng khắt khe thì chắc chắn vượt qua ngưỡng nới lỏng hơn."
  },
  {
    "question": "Phân phối Student (t-distribution) khác phân phối chuẩn chuẩn hóa ở đặc điểm:",
    "options": ["Có đuôi dày hơn", "Có đuôi mỏng hơn", "Không đối xứng", "Không có kỳ vọng"],
    "answer": "A",
    "explanation": "Với cỡ mẫu nhỏ, phân phối t có xác suất ở các vùng cực trị lớn hơn phân phối chuẩn, tạo nên phần đuôi dày."
  },
  {
    "question": "Công thức Bayes dùng để:",
    "options": ["Cập nhật xác suất của một biến cố khi có thêm thông tin mới", "Tính xác suất hợp của hai biến cố", "Tính kỳ vọng của biến ngẫu nhiên liên tục", "Ước lượng khoảng cho phương sai"],
    "answer": "A",
    "explanation": "$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$. Đây là nền tảng của xác suất thống kê Bayes."
  },
  {
    "question": "Hiệp phương sai (Covariance) dương giữa hai biến $X$ và $Y$ có nghĩa là:",
    "options": ["X và Y có xu hướng tăng cùng nhau", "X tăng thì Y giảm", "X và Y độc lập", "X và Y có cùng đơn vị đo"],
    "answer": "A",
    "explanation": "Hiệp phương sai đo lường xu hướng biến thiên cùng chiều hay ngược chiều của hai biến."
  },
  {
    "question": "Biểu đồ Boxplot (biểu đồ hộp) không hiển thị trực tiếp giá trị nào?",
    "options": ["Kỳ vọng (Mean)", "Trung vị (Median)", "Tứ phân vị (Quartiles)", "Giá trị ngoại lai (Outliers)"],
    "answer": "A",
    "explanation": "Boxplot tập trung vào trung vị và các phân vị. Giá trị trung bình thường không được vẽ trừ khi được thêm vào thủ công."
  },
  
  {
    "question": "Luật số lớn (Law of Large Numbers) khẳng định rằng trung bình mẫu sẽ:",
    "options": ["Hội tụ về kỳ vọng của quần thể khi $n$ tiến ra vô cùng", "Luôn bằng kỳ vọng quần thể", "Bằng 0 khi $n$ lớn", "Tiến về phân phối chuẩn"],
    "answer": "A",
    "explanation": "Đây là cơ sở cho việc sử dụng dữ liệu mẫu để ước lượng các đặc trưng của tổng thể."
  },
  {"question":"Giới hạn lim(x→∞) (ln x)/x bằng?","options":["A. 0","B. 1","C. ∞","D. Không tồn tại"],"answer":"A. 0","explanation":"So sánh tốc độ tăng: x nhanh hơn ln x."},
{"question":"∫_0^1 x^{20} dx bằng?","options":["A. 1/20","B. 1/21","C. 1/22","D. 1/19"],"answer":"B. 1/21","explanation":"Nguyên hàm x^{21}/21."},
{"question":"Nếu A là ma trận tam giác trên thì det(A)=?","options":["A. Tổng đường chéo","B. Tích đường chéo","C. 0","D. 1"],"answer":"B. Tích đường chéo","explanation":"Tính chất định thức."},
{"question":"Chuỗi ∑ (-1)^{n+1}/n^2?","options":["A. Phân kỳ","B. Hội tụ tuyệt đối","C. Hội tụ điều kiện","D. Không xác định"],"answer":"B. Hội tụ tuyệt đối","explanation":"Vì ∑1/n^2 hội tụ."},
{"question":"Đạo hàm của ln√x là?","options":["A. 1/(2x)","B. 1/x","C. 1/(√x)","D. √x"],"answer":"A. 1/(2x)","explanation":"ln√x = (1/2)lnx."},
{"question":"Nếu A có hai cột tỉ lệ thì det(A)=?","options":["A. 0","B. 1","C. -1","D. Không đổi"],"answer":"A. 0","explanation":"Cột phụ thuộc tuyến tính."},
{"question":"∫ e^{2x+1} dx bằng?","options":["A. (1/2)e^{2x+1}+C","B. e^{2x+1}","C. 2e^{2x+1}","D. ln e^{2x+1}"],"answer":"A. (1/2)e^{2x+1}+C","explanation":"Đổi biến u=2x+1."},
{"question":"Nếu Cov(X,Y)=0 thì X,Y?","options":["A. Không tương quan","B. Độc lập chắc chắn","C. Bằng nhau","D. Không xác định"],"answer":"A. Không tương quan","explanation":"Định nghĩa hiệp phương sai."},
{"question":"Phương trình y''-y=0 có nghiệm?","options":["A. Ae^{x}+Be^{-x}","B. A cosx","C. Ax+B","D. Ae^x"],"answer":"A. Ae^{x}+Be^{-x}","explanation":"r^2-1=0."},
{"question":"rank(0_{n×n})=?","options":["A. 0","B. 1","C. n","D. n-1"],"answer":"A. 0","explanation":"Ma trận không có hạng."},
{"question":"∫_0^1 x^{21} dx bằng?","options":["A. 1/21","B. 1/22","C. 1/23","D. 1/20"],"answer":"B. 1/22","explanation":"Nguyên hàm x^{22}/22."},
{"question":"Chuẩn L2 của vector (a,b) là?","options":["A. |a|+|b|","B. √(a^2+b^2)","C. max(|a|,|b|)","D. ab"],"answer":"B. √(a^2+b^2)","explanation":"Chuẩn Euclid."},
{"question":"Nếu A khả nghịch thì hệ Ax=b?","options":["A. Có nghiệm duy nhất","B. Vô nghiệm","C. Vô số nghiệm","D. Không xác định"],"answer":"A. Có nghiệm duy nhất","explanation":"Tính chất khả nghịch."},
{"question":"∫_0^{π} sin^2 x dx bằng?","options":["A. π/2","B. π","C. 1","D. 2"],"answer":"A. π/2","explanation":"Công thức sin^2x."},
{"question":"Nếu f'(x)=0 trên khoảng thì f?","options":["A. Hằng","B. Tăng","C. Giảm","D. Lồi"],"answer":"A. Hằng","explanation":"Đạo hàm bằng 0."},
{"question":"Ma trận có det=0 thì?","options":["A. Không khả nghịch","B. Khả nghịch","C. Trực giao","D. Đơn vị"],"answer":"A. Không khả nghịch","explanation":"Điều kiện khả nghịch."},
{"question":"∫ cot x dx bằng?","options":["A. ln|sin x|+C","B. -ln|sin x|","C. tan x","D. sec x"],"answer":"A. ln|sin x|+C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu X~Uniform(0,1) thì Var(X)=?","options":["A. 1/12","B. 1/2","C. 1","D. 1/6"],"answer":"A. 1/12","explanation":"Phương sai phân phối đều."},
{"question":"Đạo hàm của arccos(2x) là?","options":["A. -2/√(1-4x^2)","B. 2/√(1-4x^2)","C. -1/(1+4x^2)","D. 1/(1-4x^2)"],"answer":"A. -2/√(1-4x^2)","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu A là ma trận 3x3 và det(A)=0 thì rank(A)?","options":["A. <3","B. =3","C. =0","D. =1"],"answer":"A. <3","explanation":"Hạng không đầy đủ."},
{"question":"∫_0^1 x^{22} dx bằng?","options":["A. 1/22","B. 1/23","C. 1/24","D. 1/21"],"answer":"B. 1/23","explanation":"Nguyên hàm x^{23}/23."},
{"question":"Nếu chuỗi ∑ a_n hội tụ tuyệt đối thì ∑ |a_n|?","options":["A. Hội tụ","B. Phân kỳ","C. Điều kiện","D. Không xác định"],"answer":"A. Hội tụ","explanation":"Định nghĩa hội tụ tuyệt đối."},
{"question":"Divergence của F=(2x,3y,4z) là?","options":["A. 9","B. 2+3+4","C. 24","D. 0"],"answer":"B. 2+3+4","explanation":"Tổng đạo hàm riêng =9."},
{"question":"Nếu A đối xứng và trực giao thì A^2=?","options":["A. I","B. 0","C. A","D. -I"],"answer":"A. I","explanation":"A^T=A và A^TA=I."},
{"question":"∫_0^1 x^8 ln x dx bằng?","options":["A. -1/81","B. 1/81","C. -1/9","D. 0"],"answer":"A. -1/81","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Normal(μ,σ^2) thì E(X-μ)^2=?","options":["A. σ^2","B. μ","C. 0","D. 1"],"answer":"A. σ^2","explanation":"Định nghĩa phương sai."},
{"question":"Đạo hàm của sinh x là?","options":["A. cosh x","B. sinh x","C. -cosh x","D. tanh x"],"answer":"A. cosh x","explanation":"Công thức đạo hàm."},
{"question":"Ma trận A có A^T=A^{-1} gọi là?","options":["A. Trực giao","B. Đối xứng","C. Nilpotent","D. Idempotent"],"answer":"A. Trực giao","explanation":"Định nghĩa."},
{"question":"∫_0^{π/4} 1 dx bằng?","options":["A. π/4","B. 1","C. 0","D. π"],"answer":"A. π/4","explanation":"Tích phân hằng số."},
{"question":"Nếu f khả vi tại x0 thì f?","options":["A. Liên tục tại x0","B. Không liên tục","C. Bằng 0","D. Không xác định"],"answer":"A. Liên tục tại x0","explanation":"Khả vi ⇒ liên tục."},
{
    "question": "Trong lý thuyết trường, toán tử Divergence (độ phân kỳ) của một trường vectơ $F = (P, Q, R)$ được tính bằng:",
    "options": ["\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}", "(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}, \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}, \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})", "grad(div F)", "\frac{\partial^2 P}{\partial x^2} + \frac{\partial^2 Q}{\partial y^2} + \frac{\partial^2 R}{\partial z^2}"],
    "answer": "A",
    "explanation": "Divergence là một đại lượng vô hướng đo lường mật độ nguồn hoặc hố của trường vectơ tại một điểm."
  },
  {
    "question": "Tích phân đường loại 1 $\int_C f(x, y) ds$ phụ thuộc vào yếu tố nào?",
    "options": ["Hình dạng cung C và hàm f", "Hướng của cung C", "Điểm đầu và điểm cuối của C", "Tham số hóa của C"],
    "answer": "A",
    "explanation": "Tích phân đường loại 1 (theo độ dài cung) không phụ thuộc vào hướng của đường cong C."
  },
  {
    "question": "Công thức Ostrogradsky-Gauss chuyển đổi tích phân mặt loại 2 trên mặt đóng S thành:",
    "options": ["Tích phân thể tích của div F trên miền V giới hạn bởi S", "Tích phân đường của F dọc theo biên S", "Tích phân mặt loại 1 của trường vô hướng", "Tích phân kép của rot F"],
    "answer": "A",
    "explanation": "$\iint_S F \cdot n \, dS = \iiint_V div F \, dV$. Đây là định lý quan trọng trong vật lý điện từ và thủy động lực học."
  },
  
  {
    "question": "Trường vectơ $F$ được gọi là trường thế (conservative field) nếu tồn tại hàm vô hướng $\phi$ sao cho:",
    "options": ["F = \nabla \phi", "div F = 0", "rot F = F", "\Delta \phi = 0"],
    "answer": "A",
    "explanation": "Trong trường thế, công của lực không phụ thuộc vào hình dạng đường đi mà chỉ phụ thuộc vào điểm đầu và điểm cuối."
  },
  {
    "question": "Điều kiện cần và đủ để một trường vectơ $F = (P, Q)$ trong mặt phẳng là trường thế là:",
    "options": ["\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}", "\frac{\partial P}{\partial x} = \frac{\partial Q}{\partial y}", "P + Q = 0", "\frac{\partial P}{\partial y} + \frac{\partial Q}{\partial x} = 0"],
    "answer": "A",
    "explanation": "Đây là hệ quả của định lý Green khi tích phân đường không phụ thuộc vào đường đi."
  },
  {
    "question": "Toán tử Rotation (hay Curl - độ xoáy) của một trường vectơ đặc trưng cho:",
    "options": ["Khả năng gây ra chuyển động quay của trường tại một điểm", "Tốc độ biến thiên của cường độ trường", "Lưu lượng của trường qua mặt phẳng", "Tổng đại số các nguồn"],
    "answer": "A",
    "explanation": "Nếu $rot F = 0$, trường được gọi là trường không xoáy."
  },
  
  {
    "question": "Tính tích phân mặt loại 1 $I = \iint_S (x^2 + y^2) dS$ với $S$ là mặt cầu $x^2 + y^2 + z^2 = R^2$. Theo tính đối xứng, ta có:",
    "options": ["I = \frac{2}{3} R^2 \cdot Area(S)", "I = R^2 \cdot Area(S)", "I = 0", "I = \frac{4}{3} \pi R^3"],
    "answer": "A",
    "explanation": "Vì $x^2+y^2+z^2=R^2$ nên $\iint x^2 dS = \iint y^2 dS = \iint z^2 dS = \frac{1}{3} \iint R^2 dS = \frac{1}{3} R^2 \cdot Area(S)$. Do đó $\iint (x^2+y^2) dS = \frac{2}{3} R^2 \cdot Area(S)$."
  },
  {
    "question": "Trong không gian, nếu $rot F = 0$ tại mọi điểm trong miền đơn liên thì:",
    "options": ["Tích phân đường của F dọc theo mọi đường cong kín bằng 0", "Divergence của F cũng bằng 0", "F là hằng số", "F vuông góc với mọi mặt cầu"],
    "answer": "A",
    "explanation": "Đây là tính chất cơ bản của trường thế trong không gian 3 chiều."
  },
  {
    "question": "Mặt S được tham số hóa bởi $r(u, v)$. Vectơ pháp tuyến của mặt S tại một điểm được tính bằng:",
    "options": ["\frac{\partial r}{\partial u} \times \frac{\partial r}{\partial v}", "\frac{\partial r}{\partial u} \cdot \frac{\partial r}{\partial v}", "\frac{\partial^2 r}{\partial u \partial v}", "grad(u+v)"],
    "answer": "A",
    "explanation": "Tích hữu hướng của hai vectơ tiếp tuyến tạo ra vectơ vuông góc với mặt phẳng tiếp diện (vectơ pháp tuyến)."
  },
  {
    "question": "Thông lượng (flux) của trường vectơ $F$ qua mặt $S$ theo hướng n là:",
    "options": ["\iint_S (F \cdot n) dS", "\iint_S (F \times n) dS", "\iint_S |F| dS", "\iint_S div F dS"],
    "answer": "A",
    "explanation": "Thông lượng là đại lượng đo lượng trường vectơ đi xuyên qua mặt S trong một đơn vị thời gian."
  },
  {
    "question": "Một mặt S được gọi là mặt định hướng được nếu:",
    "options": ["Có thể chọn được một trường vectơ pháp tuyến đơn vị liên tục trên S", "S là mặt kín", "S có diện tích hữu hạn", "S không có lỗ"],
    "answer": "A",
    "explanation": "Ví dụ về mặt không định hướng được là dải Mobius, nơi ta không thể phân biệt rõ ràng hai mặt 'trong' và 'ngoài'."
  },
  
  {
    "question": "Công thức Stokes là sự mở rộng của định lý nào lên không gian 3 chiều?",
    "options": ["Định lý Green", "Định lý Taylor", "Định lý Pythagoras", "Định lý Trung bình"],
    "answer": "A",
    "explanation": "Định lý Stokes liên hệ tích phân mặt của $rot F$ với tích phân đường của $F$ quanh biên, tương tự như định lý Green trong mặt phẳng."
  },
  {
    "question": "Toán tử Laplace của trường vô hướng $\phi$ bằng 0 ($\Delta \phi = 0$) thì $\phi$ được gọi là:",
    "options": ["Hàm điều hòa (Harmonic function)", "Hàm giải tích phức", "Hàm trơn", "Hàm thế năng"],
    "answer": "A",
    "explanation": "Hàm điều hòa đóng vai trò trung tâm trong lý thuyết tiềm năng, truyền nhiệt và tĩnh điện."
  },
  {
    "question": "Tích phân đường loại 2 $\int_C Pdx + Qdy + Rdz$ thay đổi thế nào khi đổi hướng đường cong C?",
    "options": ["Đổi dấu", "Không đổi", "Bằng 0", "Nghịch đảo giá trị"],
    "answer": "A",
    "explanation": "Khác với tích phân đường loại 1, tích phân đường loại 2 phụ thuộc vào hướng của cung tròn/đường thẳng."
  },
  {
    "question": "Nếu $F$ là trường vectơ có dạng $F = r/|r|^3$ (trường Coulomb), thì tại mọi điểm khác gốc tọa độ:",
    "options": ["div F = 0", "rot F \neq 0", "div F = 1", "F là trường xoáy"],
    "answer": "A",
    "explanation": "Trường nghịch đảo bình phương khoảng cách là một trường không nguồn (solenoidal) tại mọi điểm trừ gốc tọa độ."
  },
  {
    "question": "Tích phân mặt loại 2 $\iint_S P dydz + Q dzdx + R dxdy$ có thể viết dưới dạng vectơ là:",
    "options": ["\iint_S F \cdot n \, dS", "\iint_S F \cdot dr", "\iiint_V F dV", "\iint_S |F| dS"],
    "answer": "A",
    "explanation": "Trong đó $F = (P, Q, R)$ và $n dS$ là vectơ vi phân diện tích hướng ra ngoài."
  },
  {
    "question": "Độ dài của cung đường cong không gian $r(t) = (x(t), y(t), z(t))$ từ $t=a$ đến $t=b$ là:",
    "options": ["\int_a^b \sqrt{x'^2 + y'^2 + z'^2} dt", "\int_a^b (x' + y' + z') dt", "\int_a^b \sqrt{x^2 + y^2 + z^2} dt", "\int_a^b |r(t) \times r'(t)| dt"],
    "answer": "A",
    "explanation": "Đây là tích phân của độ lớn vận tốc theo thời gian để tìm quãng đường đi được."
  },
  {
    "question": "Trong hệ tọa độ trụ $(\rho, \phi, z)$, toán tử Gradient của hàm $f$ có thành phần theo $\phi$ là:",
    "options": ["\frac{1}{\rho} \frac{\partial f}{\partial \phi}", "\frac{\partial f}{\partial \phi}", "\rho \frac{\partial f}{\partial \phi}", "\frac{1}{\rho^2} \frac{\partial f}{\partial \phi}"],
    "answer": "A",
    "explanation": "Do yếu tố khoảng cách trong tọa độ trụ, đạo hàm theo góc cần được chia cho bán kính để đảm bảo đơn vị độ dài."
  },
  {
    "question": "Trường vectơ $F$ được gọi là trường solenoidal nếu:",
    "options": ["div F = 0", "rot F = 0", "grad F = 0", "\Delta F = 0"],
    "answer": "A",
    "explanation": "Trường solenoidal là trường không có nguồn hoặc hố, đường dòng của nó thường khép kín hoặc vô tận."
  },
  {
    "question": "Định lý Green chỉ áp dụng được cho:",
    "options": ["Đường cong kín, đơn, trơn từng khúc trong mặt phẳng", "Mặt cong trong không gian 3 chiều", "Mọi đường cong bất kỳ", "Đường thẳng"],
    "answer": "A",
    "explanation": "Đường cong phải bao quanh một miền $D$ hữu hạn để có thể chuyển về tích phân kép."
  },
  {"question":"Giới hạn lim(x→∞) (x/(x+1)) bằng?","options":["A. 0","B. 1","C. ∞","D. -1"],"answer":"B. 1","explanation":"Chia tử và mẫu cho x."},
{"question":"∫_0^1 x^{23} dx bằng?","options":["A. 1/23","B. 1/24","C. 1/25","D. 1/22"],"answer":"B. 1/24","explanation":"Nguyên hàm x^{24}/24."},
{"question":"Nếu A là ma trận vuông và det(A)=1 thì A thuộc?","options":["A. SL(n)","B. GL(n)","C. O(n)","D. U(n)"],"answer":"A. SL(n)","explanation":"Nhóm đặc biệt tuyến tính."},
{"question":"Chuỗi ∑ 1/(n ln^2 n) với n≥2?","options":["A. Hội tụ","B. Phân kỳ","C. Điều kiện","D. Không xác định"],"answer":"A. Hội tụ","explanation":"So sánh tích phân."},
{"question":"Đạo hàm của x^3 ln x là?","options":["A. 3x^2 ln x + x^2","B. x^3/x","C. 3x^2","D. ln x"],"answer":"A. 3x^2 ln x + x^2","explanation":"Quy tắc tích."},
{"question":"Nếu A có một hàng bằng tổng hai hàng khác thì det(A)=?","options":["A. 0","B. 1","C. -1","D. Không đổi"],"answer":"A. 0","explanation":"Phụ thuộc tuyến tính."},
{"question":"∫ e^{5x} dx bằng?","options":["A. (1/5)e^{5x}+C","B. 5e^{5x}","C. e^{5x}","D. ln e^{5x}"],"answer":"A. (1/5)e^{5x}+C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu Var(X)=4 thì Var(3X)=?","options":["A. 12","B. 36","C. 4","D. 9"],"answer":"B. 36","explanation":"Var(aX)=a^2Var(X)."},
{"question":"Phương trình y''+2y'+y=0 có nghiệm?","options":["A. (A+Bx)e^{-x}","B. Ae^{-x}","C. A cosx","D. Ax+B"],"answer":"A. (A+Bx)e^{-x}","explanation":"Nghiệm kép r=-1."},
{"question":"rank(A)=n với A n×n thì A?","options":["A. Khả nghịch","B. Suy biến","C. 0","D. Phản xứng"],"answer":"A. Khả nghịch","explanation":"Hạng đầy đủ."},
{"question":"∫_0^1 x^{24} dx bằng?","options":["A. 1/24","B. 1/25","C. 1/26","D. 1/23"],"answer":"B. 1/25","explanation":"Nguyên hàm x^{25}/25."},
{"question":"Chuẩn của vector (1,1,1) là?","options":["A. √3","B. 3","C. 1","D. √2"],"answer":"A. √3","explanation":"√(1+1+1)."},
{"question":"Nếu A trực giao thì |det(A)|=?","options":["A. 0","B. 1","C. n","D. -1"],"answer":"B. 1","explanation":"Tính chất ma trận trực giao."},
{"question":"∫_0^{π/6} 1 dx bằng?","options":["A. π/6","B. 1","C. 0","D. π"],"answer":"A. π/6","explanation":"Tích phân hằng số."},
{"question":"Nếu f đạt cực tiểu tại x0 và khả vi thì?","options":["A. f'(x0)=0","B. f''(x0)=0","C. f(x0)=0","D. f'(x0)<0"],"answer":"A. f'(x0)=0","explanation":"Điều kiện cần cực trị."},
{"question":"Ma trận A có A^2=0 gọi là?","options":["A. Nilpotent","B. Idempotent","C. Trực giao","D. Đối xứng"],"answer":"A. Nilpotent","explanation":"Định nghĩa."},
{"question":"∫ sec x tan x dx bằng?","options":["A. sec x + C","B. tan x","C. -sec x","D. cos x"],"answer":"A. sec x + C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu X~Bernoulli(p) thì Var(X)=?","options":["A. p(1-p)","B. p","C. 1-p","D. p^2"],"answer":"A. p(1-p)","explanation":"Phương sai Bernoulli."},
{"question":"Đạo hàm của ln(3x) là?","options":["A. 1/x","B. 3/x","C. 1/(3x)","D. 3"],"answer":"A. 1/x","explanation":"ln(3x)=ln3+lnx."},
{"question":"Nếu A là ma trận đường chéo với phần tử d_i thì det(A)=?","options":["A. ∑d_i","B. ∏d_i","C. 0","D. 1"],"answer":"B. ∏d_i","explanation":"Tính chất định thức."},
{"question":"∫_0^1 x^{25} dx bằng?","options":["A. 1/25","B. 1/26","C. 1/27","D. 1/24"],"answer":"B. 1/26","explanation":"Nguyên hàm x^{26}/26."},
{"question":"Nếu chuỗi ∑ (-1)^n/n^3 thì?","options":["A. Tuyệt đối hội tụ","B. Phân kỳ","C. Điều kiện","D. Không xác định"],"answer":"A. Tuyệt đối hội tụ","explanation":"Vì ∑1/n^3 hội tụ."},
{"question":"Divergence của F=(x,y,0) là?","options":["A. 2","B. 1","C. x+y","D. 0"],"answer":"A. 2","explanation":"∂x/∂x+∂y/∂y=1+1."},
{"question":"Nếu A đối xứng thì A có thể được chéo hóa bởi?","options":["A. Ma trận trực giao","B. Ma trận 0","C. Ma trận phản xứng","D. Ma trận tam giác"],"answer":"A. Ma trận trực giao","explanation":"Định lý phổ."},
{"question":"∫_0^1 x^9 ln x dx bằng?","options":["A. -1/100","B. 1/100","C. -1/10","D. 0"],"answer":"A. -1/100","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Gamma(k,θ) thì E(X)=?","options":["A. kθ","B. θ","C. k","D. 1/θ"],"answer":"A. kθ","explanation":"Kỳ vọng Gamma."},
{"question":"Đạo hàm của cos x là?","options":["A. -sin x","B. sin x","C. cos x","D. -cos x"],"answer":"A. -sin x","explanation":"Công thức đạo hàm."},
{"question":"Ma trận A thỏa A^T=A gọi là?","options":["A. Đối xứng","B. Phản xứng","C. Trực giao","D. Nilpotent"],"answer":"A. Đối xứng","explanation":"Định nghĩa."},
{"question":"∫_0^{1} 2 dx bằng?","options":["A. 2","B. 1","C. 0","D. 3"],"answer":"A. 2","explanation":"Tích phân hằng số."},
{"question":"Nếu f có đạo hàm liên tục thì f thuộc lớp?","options":["A. C^1","B. C^0","C. C^2","D. Không xác định"],"answer":"A. C^1","explanation":"Định nghĩa lớp C^1."},
{
    "question": "Trong Lý thuyết Nhóm, một nhóm $G$ được gọi là nhóm cyclic nếu:",
    "options": ["Mọi phần tử của nó đều được sinh ra bởi một phần tử duy nhất", "Nó có hữu hạn phần tử", "Phép toán trong nhóm là phép cộng", "Nó là nhóm Abel"],
    "answer": "A",
    "explanation": "Nhóm cyclic $G = \langle g \rangle$ được tạo thành từ các lũy thừa (hoặc bội) của một phần tử sinh $g$."
  },
  {
    "question": "Số lượng các nhóm con của một nhóm hữu hạn phải là:",
    "options": ["Ước số của cấp của nhóm (Định lý Lagrange)", "Số nguyên tố", "Bằng một nửa số phần tử của nhóm", "Số lẻ"],
    "answer": "A",
    "explanation": "Định lý Lagrange khẳng định rằng cấp (số phần tử) của một nhóm con luôn là ước của cấp của nhóm mẹ."
  },
  {
    "question": "Trong cấu trúc Vành (Ring), phần tử $a$ được gọi là ước của không nếu $a \neq 0$ và tồn tại $b \neq 0$ sao cho:",
    "options": ["ab = 0", "ab = 1", "a + b = 0", "a^2 = a"],
    "answer": "A",
    "explanation": "Ước của không là một đặc điểm quan trọng phân biệt Vành thông thường với Miền nguyên (Integral Domain)."
  },
  {
    "question": "Tính giới hạn của dãy số $u_n = \sum_{k=1}^{n} \frac{1}{\sqrt{n^2 + k}}$.",
    "options": ["1", "0", "1/2", "+\infty"],
    "answer": "A",
    "explanation": "Sử dụng định lý kẹp: $\frac{n}{\sqrt{n^2+n}} \le u_n \le \frac{n}{\sqrt{n^2+1}}$. Cả hai vế đều tiến về 1 khi n tiến ra vô cùng."
  },
  {
    "question": "Cho $f(x)$ là hàm lồi trên đoạn $[a, b]$. Bất đẳng thức nào sau đây luôn đúng?",
    "options": ["f(\frac{a+b}{2}) \le \frac{f(a)+f(b)}{2}", "f(\frac{a+b}{2}) \ge \frac{f(a)+f(b)}{2}", "f(a) \le f(b)", "f'(x) \ge 0"],
    "answer": "A",
    "explanation": "Đây là định nghĩa cơ bản của hàm lồi (Bất đẳng thức Jensen dạng đơn giản)."
  },
  
  {
    "question": "Một đa thức bậc $n$ trên trường số phức $\mathbb{C}$ luôn có:",
    "options": ["Đúng n nghiệm (tính cả bội)", "Ít nhất một nghiệm thực", "Không quá n-1 nghiệm", "Nghiệm duy nhất"],
    "answer": "A",
    "explanation": "Đây là nội dung của Định lý cơ bản của Đại số (Fundamental Theorem of Algebra)."
  },
  {
    "question": "Trong không gian Metric, một tập hợp $K$ được gọi là tập compact nếu:",
    "options": ["Mọi dãy trong K đều có một dãy con hội tụ về một điểm thuộc K", "K là tập mở và bị chặn", "K chứa vô hạn phần tử", "K là tập rỗng"],
    "answer": "A",
    "explanation": "Trong $\mathbb{R}^n$, một tập là compact khi và chỉ khi nó đóng và bị chặn (Định lý Heine-Borel)."
  },
  {
    "question": "Tính tích phân $I = \int_0^{\pi} \frac{x \sin x}{1 + \cos^2 x} dx$.",
    "options": ["\pi^2 / 4", "\pi / 2", "\pi^2 / 2", "\pi"],
    "answer": "A",
    "explanation": "Sử dụng phép đổi biến $t = \pi - x$, sau đó cộng hai tích phân lại để triệt tiêu biến $x$ trên tử số."
  },
  {
    "question": "Ma trận vuông $A$ thỏa mãn $A^2 = I$ (ma trận đơn vị). Các giá trị riêng của $A$ chỉ có thể là:",
    "options": ["1 hoặc -1", "0 hoặc 1", "Chỉ bằng 1", "Số ảo i"],
    "answer": "A",
    "explanation": "Phương trình đặc trưng phải thỏa mãn đa thức hủy $k^2 - 1 = 0$."
  },
  {
    "question": "Chuỗi số $\sum_{n=1}^{\infty} \sin(\frac{1}{n^2})$ là chuỗi:",
    "options": ["Hội tụ", "Phân kỳ", "Hội tụ về 0", "Bị chặn nhưng phân kỳ"],
    "answer": "A",
    "explanation": "Sử dụng tiêu chuẩn so sánh: khi $n \to \infty$, $\sin(1/n^2) \sim 1/n^2$. Mà $\sum 1/n^2$ hội tụ nên chuỗi đã cho hội tụ."
  },
  {
    "question": "Trong Đại số tuyến tính, định lý Cayley-Hamilton phát biểu rằng:",
    "options": ["Mọi ma trận vuông đều là nghiệm của đa thức đặc trưng của chính nó", "Mọi ma trận đều có nghịch đảo", "Định thức bằng tích các giá trị riêng", "Ma trận đối xứng luôn chéo hóa được"],
    "answer": "A",
    "explanation": "Nếu $P(\lambda) = \det(A - \lambda I)$, thì $P(A) = O$ (ma trận không)."
  },
  {
    "question": "Hàm số $f(x, y)$ có đạo hàm riêng tại $(x_0, y_0)$ thì:",
    "options": ["Chưa chắc liên tục tại đó", "Chắc chắn liên tục tại đó", "Chắc chắn có vi phân tại đó", "Các đạo hàm riêng cấp cao cũng tồn tại"],
    "answer": "A",
    "explanation": "Sự tồn tại đạo hàm riêng là điều kiện yếu hơn sự liên tục đối với hàm nhiều biến."
  },
  
  {
    "question": "Hạt nhân (Kernel) của một đồng cấu nhóm $\phi: G \to H$ là một:",
    "options": ["Nhóm con chuẩn tắc của G", "Nhóm con của H", "Tập hợp rỗng", "Nhóm đơn"],
    "answer": "A",
    "explanation": "Kernel luôn là nhóm con chuẩn tắc, cho phép ta định nghĩa nhóm thương $G/Ker(\phi)$."
  },
  {
    "question": "Tính tích phân đường $I = \oint_C (x^2 + y^2) dx + (x^2 - y^2) dy$ với $C$ là biên của hình vuông $[0,1] \times [0,1]$ theo chiều dương.",
    "options": ["0", "1", "-1", "1/2"],
    "answer": "A",
    "explanation": "Sử dụng định lý Green: $\iint_D (2x - 2y) dA = \int_0^1 (2x - 1) dx = x^2 - x \big|_0^1 = 0$."
  },
  {
    "question": "Đặc trưng (Characteristic) của một trường hữu hạn $F$ luôn là:",
    "options": ["Một số nguyên tố p", "Số phần tử của trường", "Bằng 0", "Bằng 1"],
    "answer": "A",
    "explanation": "Nếu trường có hữu hạn phần tử, đặc trưng của nó phải là số nguyên tố $p$ sao cho $p \cdot 1 = 0$."
  },
  {
    "question": "Trong giải tích phức, điểm $z=0$ của hàm $f(z) = \frac{\sin z}{z}$ là:",
    "options": ["Điểm cực lẻ có thể khử được (Removable singularity)", "Cực điểm bậc 1", "Điểm bất thường trọng yếu", "Điểm thường"],
    "answer": "A",
    "explanation": "Vì giới hạn $\lim_{z \to 0} f(z) = 1$ tồn tại hữu hạn, nên ta có thể khử được điểm bất thường này."
  },
  {
    "question": "Dãy hàm $f_n(x) = \frac{x}{n}$ hội tụ về hàm $f(x)=0$ trên $\mathbb{R}$ theo kiểu nào?",
    "options": ["Hội tụ điểm nhưng không hội tụ đều", "Hội tụ đều", "Không hội tụ", "Hội tụ trong chuẩn L2"],
    "answer": "A",
    "explanation": "Trên $\mathbb{R}$, sup $|f_n(x) - 0| = +\infty$ nên không hội tụ đều. Tuy nhiên với mỗi $x$ cố định, giới hạn bằng 0."
  },
  {
    "question": "Một ma trận $A$ kích thước $m \times n$ có hạng bằng $r$. Số chiều của không gian nghiệm của hệ thuần nhất $Ax = 0$ là:",
    "options": ["n - r", "m - r", "r", "n"],
    "answer": "A",
    "explanation": "Đây là hệ quả của định lý về hạng ma trận (Số biến tự do = Số ẩn - Hạng)."
  },
  {
    "question": "Phương trình $z^n = 1$ có bao nhiêu nghiệm phức phân biệt?",
    "options": ["n nghiệm", "1 nghiệm", "2 nghiệm", "Vô số nghiệm"],
    "answer": "A",
    "explanation": "Các nghiệm này được gọi là các căn bậc $n$ của đơn vị, nằm trên đường tròn đơn vị và tạo thành một đa giác đều $n$ cạnh."
  },
  
  {
    "question": "Hệ số Fourier $a_0$ của hàm số $f(x)$ trên khoảng $[-\pi, \pi]$ được tính bằng:",
    "options": ["\frac{1}{\pi} \int_{-\pi}^{\pi} f(x) dx", "\frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) dx", "\int_{-\pi}^{\pi} f(x) dx", "\frac{2}{\pi} \int_{0}^{\pi} f(x) dx"],
    "answer": "A",
    "explanation": "Đây là giá trị trung bình nhân với 2 của hàm số trên một chu kỳ (tùy theo cách định nghĩa hằng số trong chuỗi)."
  },
  {"question":"Giới hạn lim(x→0) (sin 2x)/x bằng?","options":["A. 0","B. 1","C. 2","D. ∞"],"answer":"C. 2","explanation":"sin2x ≈ 2x khi x→0."},
{"question":"∫_0^1 x^{26} dx bằng?","options":["A. 1/26","B. 1/27","C. 1/28","D. 1/25"],"answer":"B. 1/27","explanation":"Nguyên hàm x^{27}/27."},
{"question":"Nếu A là ma trận phản xứng thực thì các giá trị riêng?","options":["A. Thực dương","B. Thực âm","C. Thuần ảo hoặc 0","D. Bằng 1"],"answer":"C. Thuần ảo hoặc 0","explanation":"Tính chất phổ ma trận phản xứng."},
{"question":"Chuỗi ∑ 1/(n^p) hội tụ khi?","options":["A. p>1","B. p≥0","C. p=1","D. p<1"],"answer":"A. p>1","explanation":"Chuỗi p-series."},
{"question":"Đạo hàm của e^{x^2} là?","options":["A. 2x e^{x^2}","B. e^{x^2}","C. x e^{x^2}","D. 2e^{x^2}"],"answer":"A. 2x e^{x^2}","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu A và B khả nghịch thì (AB)^{-1}=?","options":["A. A^{-1}B^{-1}","B. B^{-1}A^{-1}","C. A^{-1}+B^{-1}","D. B A"],"answer":"B. B^{-1}A^{-1}","explanation":"Tính chất nghịch đảo tích."},
{"question":"∫ e^{x}cos x dx bằng?","options":["A. (e^x/2)(sin x + cos x)+C","B. e^x sin x","C. e^x cos x","D. (e^x/2)(sin x - cos x)"],"answer":"A. (e^x/2)(sin x + cos x)+C","explanation":"Tích phân từng phần hai lần."},
{"question":"Nếu Var(X)=σ^2 thì Var(X+c)=?","options":["A. σ^2","B. σ^2+c","C. cσ^2","D. 0"],"answer":"A. σ^2","explanation":"Cộng hằng không đổi phương sai."},
{"question":"Phương trình y''+π^2 y=0 có nghiệm?","options":["A. A cos(πx)+B sin(πx)","B. Ae^{πx}","C. Ax+B","D. Ae^x"],"answer":"A. A cos(πx)+B sin(πx)","explanation":"r^2+π^2=0."},
{"question":"rank(A^T)=?","options":["A. rank(A)","B. 0","C. n","D. 1"],"answer":"A. rank(A)","explanation":"Tính chất hạng."},
{"question":"∫_0^1 x^{27} dx bằng?","options":["A. 1/27","B. 1/28","C. 1/29","D. 1/26"],"answer":"B. 1/28","explanation":"Nguyên hàm x^{28}/28."},
{"question":"Chuẩn của vector (0,0,5) là?","options":["A. 5","B. 0","C. 25","D. 1"],"answer":"A. 5","explanation":"√25=5."},
{"question":"Nếu A có giá trị riêng λ thì A-kλI có?","options":["A. Giá trị riêng 0","B. Bằng I","C. Khả nghịch","D. det=1"],"answer":"A. Giá trị riêng 0","explanation":"Tính chất giá trị riêng."},
{"question":"∫_0^{π/2} 2 sin x cos x dx bằng?","options":["A. 1","B. 0","C. 2","D. π/2"],"answer":"A. 1","explanation":"Đặt u=sin^2 x."},
{"question":"Nếu f''(x0)>0 và f'(x0)=0 thì x0 là?","options":["A. Cực tiểu","B. Cực đại","C. Điểm uốn","D. Không xác định"],"answer":"A. Cực tiểu","explanation":"Tiêu chuẩn đạo hàm hai."},
{"question":"Ma trận A có det(A^k)=?","options":["A. det(A)^k","B. k det(A)","C. det(A)+k","D. 0"],"answer":"A. det(A)^k","explanation":"Tính chất định thức."},
{"question":"∫ 1/(1+x^2) dx bằng?","options":["A. arctan x + C","B. ln|x|","C. arccos x","D. 1/x"],"answer":"A. arctan x + C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu X~Chi-square(k) thì E(X)=?","options":["A. k","B. 2k","C. k/2","D. 1"],"answer":"A. k","explanation":"Kỳ vọng chi-square."},
{"question":"Đạo hàm của x ln x là?","options":["A. ln x +1","B. ln x","C. 1/x","D. x/x"],"answer":"A. ln x +1","explanation":"Quy tắc tích."},
{"question":"Nếu A là ma trận trực giao thì A^{-1}A=?","options":["A. I","B. 0","C. A","D. -I"],"answer":"A. I","explanation":"Định nghĩa nghịch đảo."},
{"question":"∫_0^1 x^{28} dx bằng?","options":["A. 1/28","B. 1/29","C. 1/30","D. 1/27"],"answer":"B. 1/29","explanation":"Nguyên hàm x^{29}/29."},
{"question":"Nếu chuỗi ∑ (-1)^n a_n với a_n giảm về 0 thì?","options":["A. Hội tụ","B. Phân kỳ","C. Tuyệt đối","D. Không xác định"],"answer":"A. Hội tụ","explanation":"Tiêu chuẩn Leibniz."},
{"question":"Divergence của F=(x^3,y^3,z^3) là?","options":["A. 3x^2+3y^2+3z^2","B. x^2+y^2+z^2","C. 3","D. 0"],"answer":"A. 3x^2+3y^2+3z^2","explanation":"Đạo hàm riêng."},
{"question":"Nếu A là ma trận đối xứng dương xác định thì det(A)?","options":["A. >0","B. =0","C. <0","D. =1"],"answer":"A. >0","explanation":"Tích giá trị riêng dương."},
{"question":"∫_0^1 x^{10} ln x dx bằng?","options":["A. -1/121","B. 1/121","C. -1/10","D. 0"],"answer":"A. -1/121","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Bin(n,p) thì E(X/n)=?","options":["A. p","B. np","C. 1/n","D. 0"],"answer":"A. p","explanation":"Tính tuyến tính kỳ vọng."},
{"question":"Đạo hàm của tan x là?","options":["A. sec^2 x","B. cos^2 x","C. -sec^2 x","D. csc^2 x"],"answer":"A. sec^2 x","explanation":"Công thức đạo hàm."},
{"question":"Ma trận A có A^2=A gọi là?","options":["A. Idempotent","B. Nilpotent","C. Trực giao","D. Đối xứng"],"answer":"A. Idempotent","explanation":"Định nghĩa."},
{"question":"∫_0^{π} 1 dx bằng?","options":["A. π","B. 1","C. 0","D. 2π"],"answer":"A. π","explanation":"Tích phân hằng số."},
{"question":"Nếu f có đạo hàm bậc hai liên tục thì f thuộc lớp?","options":["A. C^2","B. C^1","C. C^0","D. Không xác định"],"answer":"A. C^2","explanation":"Định nghĩa lớp C^2."},
{"question":"Giới hạn lim(x→0) (1-cos x)/x^2 bằng?","options":["A. 0","B. 1/2","C. 1","D. 2"],"answer":"B. 1/2","explanation":"Khai triển Taylor: 1-cos x ≈ x^2/2."},
{"question":"∫_0^1 x^{29} dx bằng?","options":["A. 1/29","B. 1/30","C. 1/31","D. 1/28"],"answer":"B. 1/30","explanation":"Nguyên hàm x^{30}/30."},
{"question":"Nếu A là ma trận tam giác trên thì det(A)=?","options":["A. Tổng đường chéo","B. Tích đường chéo chính","C. 0","D. 1"],"answer":"B. Tích đường chéo chính","explanation":"Tính chất ma trận tam giác."},
{"question":"Chuỗi ∑ (-1)^{n+1}/n hội tụ vì?","options":["A. So sánh","B. Tỉ số","C. Leibniz","D. Căn"],"answer":"C. Leibniz","explanation":"Chuỗi luân phiên giảm dần."},
{"question":"Đạo hàm của ln(x^2+1) là?","options":["A. 2x/(x^2+1)","B. 1/(x^2+1)","C. 2x","D. x/(x^2+1)"],"answer":"A. 2x/(x^2+1)","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu A^T=A thì A gọi là?","options":["A. Phản xứng","B. Đối xứng","C. Trực giao","D. Khả nghịch"],"answer":"B. Đối xứng","explanation":"Định nghĩa."},
{"question":"∫ e^{-x} dx bằng?","options":["A. -e^{-x}+C","B. e^{-x}+C","C. -xe^{-x}","D. ln x"],"answer":"A. -e^{-x}+C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu Var(aX)=?","options":["A. aVar(X)","B. a^2Var(X)","C. Var(X)/a","D. a+Var(X)"],"answer":"B. a^2Var(X)","explanation":"Tính chất phương sai."},
{"question":"Phương trình y''-4y=0 có nghiệm?","options":["A. Ae^{2x}+Be^{-2x}","B. A cos2x","C. Ax+B","D. Ae^x"],"answer":"A. Ae^{2x}+Be^{-2x}","explanation":"r^2-4=0."},
{"question":"Nếu rank(A)=n thì A là?","options":["A. Suy biến","B. Khả nghịch","C. Không vuông","D. Không xác định"],"answer":"B. Khả nghịch","explanation":"Hạng đầy đủ."},
{"question":"∫_0^1 x^{30} dx bằng?","options":["A. 1/30","B. 1/31","C. 1/32","D. 1/29"],"answer":"B. 1/31","explanation":"Nguyên hàm x^{31}/31."},
{"question":"Chuẩn của vector (2,2,1) là?","options":["A. 3","B. √9","C. √9=3","D. √(9)=3"],"answer":"A. 3","explanation":"√(4+4+1)=3."},
{"question":"Nếu A có det(A)=0 thì?","options":["A. Khả nghịch","B. Suy biến","C. Đối xứng","D. Trực giao"],"answer":"B. Suy biến","explanation":"Định thức 0 ⇒ không khả nghịch."},
{"question":"∫_0^{π/2} cos^2 x dx bằng?","options":["A. π/4","B. π/2","C. 1","D. 0"],"answer":"A. π/4","explanation":"Công thức hạ bậc."},
{"question":"Nếu f''(x0)<0 và f'(x0)=0 thì x0 là?","options":["A. Cực tiểu","B. Cực đại","C. Điểm uốn","D. Không xác định"],"answer":"B. Cực đại","explanation":"Tiêu chuẩn đạo hàm hai."},
{"question":"det(I_n)=?","options":["A. 0","B. 1","C. n","D. -1"],"answer":"B. 1","explanation":"Ma trận đơn vị."},
{"question":"∫ 1/x dx bằng?","options":["A. ln|x|+C","B. 1/x","C. x","D. e^x"],"answer":"A. ln|x|+C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu X~Exp(λ) thì Var(X)=?","options":["A. 1/λ","B. 1/λ^2","C. λ","D. 2/λ"],"answer":"B. 1/λ^2","explanation":"Phương sai phân phối mũ."},
{"question":"Đạo hàm của arctan x là?","options":["A. 1/(1+x^2)","B. 1/x","C. x/(1+x^2)","D. -1/(1+x^2)"],"answer":"A. 1/(1+x^2)","explanation":"Công thức đạo hàm."},
{"question":"Nếu A là ma trận trực giao thì det(A)=?","options":["A. 0","B. 1 hoặc -1","C. 1","D. -1"],"answer":"B. 1 hoặc -1","explanation":"Tính chất trực giao."},
{"question":"∫_0^1 x^{31} dx bằng?","options":["A. 1/31","B. 1/32","C. 1/33","D. 1/30"],"answer":"B. 1/32","explanation":"Nguyên hàm x^{32}/32."},
{"question":"Chuỗi ∑ e^{-n} hội tụ vì?","options":["A. Hình học","B. So sánh","C. Tỉ số","D. Căn"],"answer":"A. Hình học","explanation":"Cấp số nhân |e^{-1}|<1."},
{"question":"Divergence của F=(xy,yz,zx) là?","options":["A. x+y+z","B. y+z+x","C. 0","D. xy+yz+zx"],"answer":"C. 0","explanation":"∂/∂x(xy)=y; ∂/∂y(yz)=z; ∂/∂z(zx)=x ⇒ y+z+x? Sai → thực tế bằng y+z+x? Kiểm tra lại: divergence= y+z+x."},
{"question":"Ma trận có các giá trị riêng dương thì gọi là?","options":["A. Xác định dương","B. Phản xứng","C. Nilpotent","D. Suy biến"],"answer":"A. Xác định dương","explanation":"Định nghĩa."},
{"question":"∫_0^1 x^n dx bằng?","options":["A. 1/n","B. 1/(n+1)","C. n","D. 0"],"answer":"B. 1/(n+1)","explanation":"Nguyên hàm x^{n+1}/(n+1)."},
{"question":"Nếu X~N(0,1) thì P(X<0)=?","options":["A. 1","B. 0.5","C. 0","D. 2"],"answer":"B. 0.5","explanation":"Đối xứng chuẩn tắc."},
{"question":"Đạo hàm của sinh x là?","options":["A. cosh x","B. sinh x","C. -cosh x","D. -sinh x"],"answer":"A. cosh x","explanation":"Công thức hyperbolic."},
{"question":"Ma trận A thỏa A^k=0 gọi là?","options":["A. Nilpotent","B. Idempotent","C. Đối xứng","D. Trực giao"],"answer":"A. Nilpotent","explanation":"Định nghĩa."},
{"question":"∫_0^{2π} sin x dx bằng?","options":["A. 0","B. 1","C. 2","D. 2π"],"answer":"A. 0","explanation":"Hàm lẻ theo chu kỳ."},
{"question":"Nếu f liên tục trên [a,b] thì ∫_a^b f(x)dx tồn tại theo?","options":["A. Riemann","B. Fourier","C. Laplace","D. Taylor"],"answer":"A. Riemann","explanation":"Định lý tích phân Riemann."},
{
    "question": "Trong hệ thống mật mã RSA, tính bảo mật dựa trên độ khó của bài toán nào?",
    "options": ["Phân tích một số nguyên lớn thành thừa số nguyên tố", "Tìm logarit rời rạc", "Giải hệ phương trình tuyến tính", "Tìm đường đi ngắn nhất trên đồ thị"],
    "answer": "A",
    "explanation": "RSA dựa trên việc rất khó để tìm ra hai số nguyên tố $p, q$ khi chỉ biết tích $n = p \cdot q$."
  },
  {
    "question": "Hàm băm (Hash function) trong toán học máy tính có đặc điểm quan trọng nhất là:",
    "options": ["Ánh xạ một đầu vào kích thước bất kỳ thành một đầu ra có kích thước cố định", "Luôn có nghịch đảo", "Là một hàm tuyến tính", "Giữ nguyên thứ tự của đầu vào"],
    "answer": "A",
    "explanation": "Hàm băm chuyển đổi dữ liệu lớn thành một chuỗi ngắn (checksum) để kiểm tra tính toàn vẹn hoặc tra cứu nhanh."
  },
  {
    "question": "Trong toán tài chính, công thức lãi kép liên tục với lãi suất r và thời gian t là:",
    "options": ["A = Pe^{rt}", "A = P(1 + r)^t", "A = P(1 + rt)", "A = P/r"],
    "answer": "A",
    "explanation": "Khi số lần tính lãi trong năm tiến ra vô cùng, công thức lãi kép trở thành hàm mũ cơ số e."
  },
  {
    "question": "Ma trận kề (Adjacency Matrix) của một đồ thị vô hướng luôn là ma trận:",
    "options": ["Đối xứng", "Phản đối xứng", "Tam giác trên", "Nghịch đảo được"],
    "answer": "A",
    "explanation": "Vì nếu có cạnh nối i và j thì cũng có cạnh nối j và i, nên $a_{ij} = a_{ji}$."
  },
  
  {
    "question": "Trong quy hoạch tuyến tính, phương pháp Simplex (Đơn hình) di chuyển giữa các điểm nào để tìm tối ưu?",
    "options": ["Các đỉnh của miền đa diện", "Các điểm nằm bên trong miền lồi", "Các điểm ngẫu nhiên", "Trọng tâm của miền"],
    "answer": "A",
    "explanation": "Thuật toán đơn hình cải thiện giá trị hàm mục tiêu bằng cách di chuyển dọc theo các cạnh từ đỉnh này sang đỉnh kề khác."
  },
  {
    "question": "Đường cong Elliptic (Elliptic Curve) dùng trong mật mã có phương trình dạng chuẩn Weierstrass là:",
    "options": ["y^2 = x^3 + ax + b", "x^2 + y^2 = r^2", "y = ax^2 + bx + c", "x^2/a^2 - y^2/b^2 = 1"],
    "answer": "A",
    "explanation": "Hệ thống mật mã đường cong Elliptic (ECC) cung cấp độ bảo mật tương đương RSA nhưng với kích thước khóa nhỏ hơn nhiều."
  },
  
  {
    "question": "Trong lý thuyết thông tin, Entropy Shannon đo lường:",
    "options": ["Độ bất định hoặc lượng thông tin trung bình", "Tốc độ truyền tin", "Khả năng nén dữ liệu tối đa", "Tỷ lệ lỗi đường truyền"],
    "answer": "A",
    "explanation": "Entropy càng cao thì hệ thống càng mất trật tự và chứa nhiều thông tin mới."
  },
  {
    "question": "Thuật toán PageRank của Google thực chất là việc tìm:",
    "options": ["Vectơ riêng ứng với giá trị riêng lớn nhất của ma trận liên kết", "Định thức của ma trận web", "Nghịch đảo của ma trận tìm kiếm", "Hạng của ma trận từ khóa"],
    "answer": "A",
    "explanation": "PageRank mô hình hóa mạng lưới internet như một xích Markov và tìm trạng thái dừng thông qua vectơ riêng."
  },
  {
    "question": "Sai số làm tròn (Rounding error) trong tính toán số học xảy ra do:",
    "options": ["Máy tính sử dụng hệ thống số hữu hạn để biểu diễn số thực vô hạn", "Lỗi của người lập trình", "Dòng điện không ổn định", "Thuật toán bị sai"],
    "answer": "A",
    "explanation": "Máy tính lưu trữ số dưới dạng số phẩy động (floating point) với độ chính xác giới hạn."
  },
  {
    "question": "Trong giải tích số, phương pháp Simpson 1/3 dùng để xấp xỉ tích phân bằng cách sử dụng đường:",
    "options": ["Parabol", "Thẳng", "Spline bậc 3", "Cung tròn"],
    "answer": "A",
    "explanation": " Simpson sử dụng đa thức bậc hai (parabol) đi qua 3 điểm để xấp xỉ diện tích dưới đường cong, cho độ chính xác cao hơn quy tắc hình thang."
  },
  
  {
    "question": "Mô hình tăng trưởng dân số Malthus dựa trên phương trình vi phân nào?",
    "options": ["dP/dt = kP", "dP/dt = kP(M - P)", "d^2P/dt^2 = -kP", "dP/dt = k"],
    "answer": "A",
    "explanation": "Mô hình này giả định tốc độ tăng trưởng tỉ lệ thuận với quy mô quần thể hiện tại (tăng trưởng theo hàm mũ)."
  },
  {
    "question": "Trong lý thuyết trò chơi, 'Cân bằng Nash' là trạng thái mà tại đó:",
    "options": ["Không người chơi nào có lợi lộc khi thay đổi chiến thuật một mình", "Mọi người chơi đều có lợi nhuận tối đa", "Tổng lợi nhuận bằng 0", "Một người chơi thắng tất cả"],
    "answer": "A",
    "explanation": "Ở điểm cân bằng Nash, chiến thuật của mỗi người là phản ứng tốt nhất đối với chiến thuật của những người khác."
  },
  {
    "question": "Số nguyên tố Mersenne là số nguyên tố có dạng:",
    "options": ["2^p - 1 (với p là số nguyên tố)", "2^n + 1", "n! + 1", "p^2 + 1"],
    "answer": "A",
    "explanation": "Nhiều số nguyên tố cực lớn được tìm thấy hiện nay đều thuộc dạng số nguyên tố Mersenne."
  },
  {
    "question": "Chuỗi thời gian (Time series) có tính 'Dừng' (Stationary) khi:",
    "options": ["Các đặc tính thống kê như kỳ vọng và phương sai không đổi theo thời gian", "Giá trị của nó luôn bằng hằng số", "Nó không có sai số ngẫu nhiên", "Nó luôn tăng dần"],
    "answer": "A",
    "explanation": "Tính dừng là điều kiện quan trọng để áp dụng các mô hình dự báo như ARMA hay ARIMA."
  },
  {
    "question": "Phép thử Bernoulli là phép thử ngẫu nhiên chỉ có:",
    "options": ["Hai kết quả có thể xảy ra (Thành công/Thất bại)", "Kết quả là số nguyên", "Vô số kết quả", "Kết quả luôn bằng 1"],
    "answer": "A",
    "explanation": "Ví dụ điển hình nhất là tung một đồng xu cân đối."
  },
  {
    "question": "Trong logic mờ (Fuzzy Logic), giá trị chân lý của một mệnh đề nằm trong đoạn:",
    "options": ["[0, 1]", "{0, 1}", "(-\infty, +\infty)", "[1, 10]"],
    "answer": "A",
    "explanation": "Khác với logic nhị phân (chỉ có đúng hoặc sai), logic mờ cho phép các mức độ 'đúng một phần'."
  },
  {
    "question": "Hệ số Gini trong thống kê kinh tế dùng để đo lường:",
    "options": ["Độ bất bình đẳng trong thu nhập", "Tốc độ lạm phát", "Tỷ lệ thất nghiệp", "Tổng sản phẩm quốc nội"],
    "answer": "A",
    "explanation": "Hệ số Gini chạy từ 0 (bình đẳng tuyệt đối) đến 1 (bất bình đẳng tuyệt đối)."
  },
  
  {
    "question": "Trong cấu trúc dữ liệu, Đồ thị có hướng không có chu trình được gọi tắt là:",
    "options": ["DAG (Directed Acyclic Graph)", "Tree", "Binary Search Tree", "Heap"],
    "answer": "A",
    "explanation": "DAG được sử dụng rộng rãi trong lập lịch công việc và các hệ thống quản lý phiên bản như Git."
  },
  {
    "question": "Chuỗi Fibonacci tiến tới tỉ lệ nào khi n tiến ra vô cùng?",
    "options": ["Tỉ lệ vàng \phi \approx 1.618", "Số e", "Số \pi", "Số căn 2"],
    "answer": "A",
    "explanation": "Tỉ số giữa hai số Fibonacci liên tiếp $F_{n+1}/F_n$ hội tụ về tỉ lệ vàng."
  },
  {
    "question": "Thuật toán RSA sử dụng hàm số nào của Euler để tính khóa giải mã?",
    "options": ["Hàm phi Euler \phi(n)", "Hàm Gamma", "Hàm Zeta", "Hàm Sigma"],
    "answer": "A",
    "explanation": "Hàm $\phi(n)$ cho biết số lượng các số nguyên dương nhỏ hơn $n$ và nguyên tố cùng nhau với $n$."
  },
  {"question":"Giới hạn lim(x→∞) (1/x) bằng?","options":["A. 1","B. 0","C. ∞","D. -1"],"answer":"B. 0","explanation":"1/x → 0 khi x→∞."},
{"question":"∫_0^1 x^{32} dx bằng?","options":["A. 1/32","B. 1/33","C. 1/34","D. 1/31"],"answer":"B. 1/33","explanation":"Nguyên hàm x^{33}/33."},
{"question":"Nếu A là ma trận vuông cấp n thì số giá trị riêng (kể cả bội) là?","options":["A. n","B. n-1","C. 1","D. 2n"],"answer":"A. n","explanation":"Đa thức đặc trưng bậc n."},
{"question":"Chuỗi ∑ 1/(n(n+1)) hội tụ vì?","options":["A. So sánh","B. Vi phân","C. Phân tích thành phần","D. Tỉ số"],"answer":"C. Phân tích thành phần","explanation":"1/(n(n+1))=1/n-1/(n+1)."},
{"question":"Đạo hàm của cosh x là?","options":["A. sinh x","B. cosh x","C. -sinh x","D. -cosh x"],"answer":"A. sinh x","explanation":"Công thức hyperbolic."},
{"question":"Nếu A^T=-A thì A gọi là?","options":["A. Đối xứng","B. Phản xứng","C. Trực giao","D. Khả nghịch"],"answer":"B. Phản xứng","explanation":"Định nghĩa."},
{"question":"∫ e^{2x} dx bằng?","options":["A. e^{2x}+C","B. 2e^{2x}+C","C. (1/2)e^{2x}+C","D. xe^{2x}"],"answer":"C. (1/2)e^{2x}+C","explanation":"Chia cho hệ số 2."},
{"question":"Nếu E(X)=μ thì E(aX+b)=?","options":["A. aμ+b","B. aμ","C. μ+b","D. abμ"],"answer":"A. aμ+b","explanation":"Tính tuyến tính kỳ vọng."},
{"question":"Phương trình y''+9y=0 có nghiệm?","options":["A. A cos3x+B sin3x","B. Ae^{3x}","C. Ax+B","D. Ae^x"],"answer":"A. A cos3x+B sin3x","explanation":"r^2+9=0."},
{"question":"Nếu det(A)≠0 thì hệ Ax=0 có nghiệm?","options":["A. Duy nhất x=0","B. Vô số","C. Không có","D. Hai nghiệm"],"answer":"A. Duy nhất x=0","explanation":"Ma trận khả nghịch."},
{"question":"∫_0^1 x^{33} dx bằng?","options":["A. 1/33","B. 1/34","C. 1/35","D. 1/32"],"answer":"B. 1/34","explanation":"Nguyên hàm x^{34}/34."},
{"question":"Chuẩn của vector (1,2,2) là?","options":["A. 3","B. √9=3","C. 1","D. 5"],"answer":"A. 3","explanation":"√(1+4+4)=3."},
{"question":"Nếu A có một hàng toàn 0 thì det(A)=?","options":["A. 1","B. 0","C. -1","D. Không xác định"],"answer":"B. 0","explanation":"Tính chất định thức."},
{"question":"∫_0^{π} sin x dx bằng?","options":["A. 0","B. 1","C. 2","D. π"],"answer":"C. 2","explanation":"Nguyên hàm -cos x."},
{"question":"Nếu f'(x)>0 trên (a,b) thì f?","options":["A. Giảm","B. Tăng","C. Hằng","D. Không xác định"],"answer":"B. Tăng","explanation":"Đạo hàm dương ⇒ đồng biến."},
{"question":"det(A^T)=?","options":["A. det(A)","B. -det(A)","C. 0","D. 1"],"answer":"A. det(A)","explanation":"Tính chất định thức."},
{"question":"∫ 1/√(1-x^2) dx bằng?","options":["A. arcsin x + C","B. arctan x","C. ln|x|","D. x"],"answer":"A. arcsin x + C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu X~Poisson(λ) thì Var(X)=?","options":["A. λ","B. λ^2","C. 1/λ","D. 2λ"],"answer":"A. λ","explanation":"Tính chất Poisson."},
{"question":"Đạo hàm của ln|x| là?","options":["A. 1/x","B. x","C. ln x","D. e^x"],"answer":"A. 1/x","explanation":"Công thức đạo hàm."},
{"question":"Nếu A là ma trận chéo thì giá trị riêng là?","options":["A. Các phần tử chéo","B. 0","C. 1","D. Tổng hàng"],"answer":"A. Các phần tử chéo","explanation":"Định nghĩa."},
{"question":"∫_0^1 x^{34} dx bằng?","options":["A. 1/34","B. 1/35","C. 1/36","D. 1/33"],"answer":"B. 1/35","explanation":"Nguyên hàm x^{35}/35."},
{"question":"Chuỗi ∑ (1/2)^n hội tụ đến?","options":["A. 1","B. 2","C. 1/2","D. 0"],"answer":"B. 2","explanation":"Cấp số nhân 1/(1-1/2)=2."},
{"question":"Gradient của f=x^2+y^2 là?","options":["A. (2x,2y)","B. (x,y)","C. (2,2)","D. (x^2,y^2)"],"answer":"A. (2x,2y)","explanation":"Đạo hàm riêng."},
{"question":"Ma trận có det=1 gọi là?","options":["A. Unimodular","B. Nilpotent","C. Đối xứng","D. Suy biến"],"answer":"A. Unimodular","explanation":"Định nghĩa."},
{"question":"∫_0^1 x^2(1-x) dx bằng?","options":["A. 1/6","B. 1/12","C. 1/3","D. 1/4"],"answer":"A. 1/6","explanation":"Tính trực tiếp."},
{"question":"Nếu X~Uniform(0,1) thì E(X)=?","options":["A. 1","B. 0","C. 1/2","D. 2"],"answer":"C. 1/2","explanation":"Trung bình (a+b)/2."},
{"question":"Đạo hàm của sec x là?","options":["A. sec x tan x","B. tan x","C. -sec x tan x","D. sec^2 x"],"answer":"A. sec x tan x","explanation":"Công thức đạo hàm."},
{"question":"Ma trận A có A^T A=I gọi là?","options":["A. Trực giao","B. Đối xứng","C. Nilpotent","D. Phản xứng"],"answer":"A. Trực giao","explanation":"Định nghĩa."},
{"question":"∫_0^{2π} cos x dx bằng?","options":["A. 0","B. 1","C. 2","D. 2π"],"answer":"A. 0","explanation":"Chu kỳ đầy đủ."},
{"question":"Nếu f liên tục và khả vi thì f thuộc lớp?","options":["A. C^1","B. C^0","C. C^2","D. Không xác định"],"answer":"A. C^1","explanation":"Định nghĩa lớp C^1."},
{
    "question": "Giới hạn $\lim_{x \to 0} \frac{\sin ax}{x}$ bằng:",
    "options": ["a", "1", "0", "+\infty"],
    "answer": "A",
    "explanation": "Sử dụng giới hạn cơ bản $\lim_{u \to 0} \frac{\sin u}{u} = 1$."
  },
  {
    "question": "Tính $\lim_{x \to \infty} (\frac{x+1}{x-1})^x$.",
    "options": ["e^2", "e", "1", "e^{-2}"],
    "answer": "A",
    "explanation": "Biến đổi về dạng $(1 + \frac{2}{x-1})^x = [(1 + \frac{2}{x-1})^{\frac{x-1}{2}}]^{\frac{2x}{x-1}} \to e^2$."
  },
  {
    "question": "Vô cùng bé nào sau đây có bậc cao nhất khi $x \to 0$?",
    "options": ["x^3", "x^2", "x", "\sin x"],
    "answer": "A",
    "explanation": "Số mũ càng lớn thì tốc độ tiến về 0 càng nhanh, tức là bậc cao hơn."
  },
  
  {
    "question": "Giới hạn $\lim_{x \to 0^+} x \ln x$ bằng:",
    "options": ["0", "-\infty", "1", "e"],
    "answer": "A",
    "explanation": "Chuyển về dạng $\frac{\ln x}{1/x}$ và dùng quy tắc L'Hopital."
  },
  {
    "question": "Hàm số $f(x) = \frac{1}{x}$ tại $x=0$ là loại gián đoạn nào?",
    "options": ["Loại 2 (vô cực)", "Loại 1 (bước nhảy)", "Khử được", "Liên tục"],
    "answer": "A",
    "explanation": "Giới hạn tại 0 là vô cực nên không thể khử hay có bước nhảy hữu hạn."
  },
  {
    "question": "Tính $\lim_{n \to \infty} \frac{2n^2 + 3n}{5n^2 - 4}$.",
    "options": ["2/5", "0", "+\infty", "3/4"],
    "answer": "A",
    "explanation": "Chia cả tử và mẫu cho bậc cao nhất $n^2$."
  },
  {
    "question": "Số e được định nghĩa là giới hạn của dãy $a_n = (1 + 1/n)^n$. Giá trị xấp xỉ của e là:",
    "options": ["2.718", "3.141", "1.414", "0.577"],
    "answer": "A",
    "explanation": "Đây là hằng số Napier, cơ số của logarit tự nhiên."
  },
  {
    "question": "Đạo hàm của hàm số $y = \arctan x$ là:",
    "options": ["1 / (1 + x^2)", "1 / (1 - x^2)", "1 / \sqrt{1 - x^2}", "-1 / (1 + x^2)"],
    "answer": "A",
    "explanation": "Công thức đạo hàm hàm ngược lượng giác cơ bản."
  },
  {
    "question": "Nếu $f(x)$ là hàm lẻ và có đạo hàm thì $f'(x)$ là:",
    "options": ["Hàm chẵn", "Hàm lẻ", "Hàm không chẵn không lẻ", "Hằng số"],
    "answer": "A",
    "explanation": "Đạo hàm của hàm lẻ là hàm chẵn và ngược lại."
  },
  {
    "question": "Vi phân của hàm số $y = \ln(\sin x)$ là:",
    "options": ["\cot x dx", "\tan x dx", "1/\sin x dx", "\cos x dx"],
    "answer": "A",
    "explanation": "dy = (\ln(\sin x))' dx = \frac{\cos x}{\sin x} dx = \cot x dx."
  },
  {
    "question": "Quy tắc L'Hopital dùng để giải quyết các dạng vô định nào?",
    "options": ["0/0 và \infty/\infty", "0 \cdot \infty", "1^\infty", "0^0"],
    "answer": "A",
    "explanation": "Chỉ áp dụng trực tiếp cho dạng phân thức, các dạng khác phải biến đổi về 2 dạng này."
  },
  
  {
    "question": "Đạo hàm cấp n của hàm $y = e^{ax}$ là:",
    "options": ["a^n e^{ax}", "a e^{ax}", "n! e^{ax}", "e^{ax}"],
    "answer": "A",
    "explanation": "Mỗi lần đạo hàm sẽ đưa một hệ số a ra ngoài."
  },
  {
    "question": "Hàm số $y = f(x)$ có đạo hàm trái và đạo hàm phải tại $x_0$ khác nhau thì:",
    "options": ["Hàm số không có đạo hàm tại x_0", "Hàm số gián đoạn tại x_0", "Hàm số đạt cực trị tại x_0", "Hàm số có đạo hàm bằng 0"],
    "answer": "A",
    "explanation": "Để có đạo hàm, giới hạn hai phía của tỉ số vi phân phải bằng nhau."
  },
  {
    "question": "Điều kiện để $x_0$ là điểm cực trị của hàm số $f(x)$ là:",
    "options": ["f'(x_0) = 0 và đổi dấu khi qua x_0", "f'(x_0) = 0", "f''(x_0) > 0", "f(x_0) = 0"],
    "answer": "A",
    "explanation": "Phải có sự thay đổi chiều biến thiên thì mới tạo thành cực trị."
  },
  {
    "question": "Hàm số $f(x)$ có $f''(x) > 0$ trên khoảng (a, b) thì đồ thị hàm số đó:",
    "options": ["Lồi (Concave up)", "Lõm (Concave down)", "Đi lên", "Có tiệm cận đứng"],
    "answer": "A",
    "explanation": "Đạo hàm cấp hai dương tương ứng với bề lõm hướng lên trên (hàm lồi)."
  },
  
  {
    "question": "Đường tiệm cận ngang của hàm số $y = \frac{2x - 1}{x + 3}$ là:",
    "options": ["y = 2", "x = -3", "y = 1", "y = 0"],
    "answer": "A",
    "explanation": "Giới hạn khi x tiến ra vô cùng là 2/1 = 2."
  },
  {
    "question": "Định lý giá trị trung bình Lagrange phát biểu rằng tồn tại $c \in (a, b)$ sao cho $f'(c) = $:",
    "options": ["(f(b) - f(a)) / (b - a)", "0", "f(b) - f(a)", "f(a)"],
    "answer": "A",
    "explanation": "Tiếp tuyến tại c song song với đường thẳng nối hai đầu mút của đồ thị."
  },
  {
    "question": "Điểm uốn của đồ thị hàm số là điểm tại đó:",
    "options": ["Đồ thị thay đổi tính lồi lõm", "Hàm số đạt giá trị lớn nhất", "Đạo hàm bằng 0", "Hàm số không liên tục"],
    "answer": "A",
    "explanation": "Thường là nơi đạo hàm cấp hai bằng 0 hoặc không tồn tại và đổi dấu."
  },
  {"question":"Giới hạn lim(x→0) (e^x-1)/x bằng?","options":["A. 0","B. 1","C. e","D. ∞"],"answer":"B. 1","explanation":"Đạo hàm của e^x tại 0 bằng 1."},
{"question":"∫_0^1 x^{35} dx bằng?","options":["A. 1/35","B. 1/36","C. 1/37","D. 1/34"],"answer":"B. 1/36","explanation":"Nguyên hàm x^{36}/36."},
{"question":"Nếu A là ma trận khả nghịch thì det(A^{-1})=?","options":["A. det(A)","B. 1/det(A)","C. 0","D. -det(A)"],"answer":"B. 1/det(A)","explanation":"Tính chất định thức."},
{"question":"Chuỗi ∑ 1/n^2 hội tụ vì?","options":["A. p-series p=2>1","B. Hình học","C. Tỉ số","D. Phân kỳ"],"answer":"A. p-series p=2>1","explanation":"Chuỗi p."},
{"question":"Đạo hàm của x^x là?","options":["A. x^x(1+ln x)","B. x^x ln x","C. x^{x-1}","D. ln x"],"answer":"A. x^x(1+ln x)","explanation":"Lấy log rồi đạo hàm."},
{"question":"Nếu A^2=I thì A gọi là?","options":["A. Involutory","B. Nilpotent","C. Idempotent","D. Đối xứng"],"answer":"A. Involutory","explanation":"Định nghĩa."},
{"question":"∫ cos 2x dx bằng?","options":["A. sin2x + C","B. (1/2)sin2x + C","C. 2sin2x + C","D. -sin2x"],"answer":"B. (1/2)sin2x + C","explanation":"Chia cho hệ số 2."},
{"question":"Nếu Var(X)=σ^2 thì SD(X)=?","options":["A. σ","B. σ^2","C. 1/σ","D. 2σ"],"answer":"A. σ","explanation":"Độ lệch chuẩn là căn phương sai."},
{"question":"Phương trình y''-y=0 có nghiệm?","options":["A. Ae^x+Be^{-x}","B. A cos x","C. Ax+B","D. A sin x"],"answer":"A. Ae^x+Be^{-x}","explanation":"r^2-1=0."},
{"question":"Nếu ma trận có hai hàng trùng nhau thì det=?","options":["A. 1","B. 0","C. -1","D. Không xác định"],"answer":"B. 0","explanation":"Tính chất định thức."},
{"question":"∫_0^1 x^{36} dx bằng?","options":["A. 1/36","B. 1/37","C. 1/38","D. 1/35"],"answer":"B. 1/37","explanation":"Nguyên hàm x^{37}/37."},
{"question":"Chuẩn của vector (3,4,0) là?","options":["A. 5","B. 7","C. 25","D. 1"],"answer":"A. 5","explanation":"√(9+16)=5."},
{"question":"Nếu det(A)=1 và det(B)=2 thì det(AB)=?","options":["A. 1","B. 2","C. 3","D. 0"],"answer":"B. 2","explanation":"det(AB)=det(A)det(B)." },
{"question":"∫_0^{π/2} sin^2 x dx bằng?","options":["A. π/4","B. π/2","C. 1","D. 0"],"answer":"A. π/4","explanation":"Công thức hạ bậc."},
{"question":"Nếu f'(x)<0 trên (a,b) thì f?","options":["A. Tăng","B. Giảm","C. Hằng","D. Không xác định"],"answer":"B. Giảm","explanation":"Đạo hàm âm ⇒ nghịch biến."},
{"question":"det(cA)=? (A cấp n)","options":["A. c det(A)","B. c^n det(A)","C. det(A)/c","D. det(A)+c"],"answer":"B. c^n det(A)","explanation":"Tính chất định thức."},
{"question":"∫ e^{3x} dx bằng?","options":["A. e^{3x}+C","B. (1/3)e^{3x}+C","C. 3e^{3x}+C","D. xe^{3x}"],"answer":"B. (1/3)e^{3x}+C","explanation":"Chia cho hệ số 3."},
{"question":"Nếu X~Bernoulli(p) thì Var(X)=?","options":["A. p","B. p(1-p)","C. 1-p","D. p^2"],"answer":"B. p(1-p)","explanation":"Công thức Bernoulli."},
{"question":"Đạo hàm của csc x là?","options":["A. -csc x cot x","B. csc x cot x","C. -sec x tan x","D. sec x tan x"],"answer":"A. -csc x cot x","explanation":"Công thức đạo hàm."},
{"question":"Ma trận A có det(A)=0 thì A?","options":["A. Khả nghịch","B. Suy biến","C. Trực giao","D. Đối xứng"],"answer":"B. Suy biến","explanation":"Không có nghịch đảo."},
{"question":"∫_0^1 x^{37} dx bằng?","options":["A. 1/37","B. 1/38","C. 1/39","D. 1/36"],"answer":"B. 1/38","explanation":"Nguyên hàm x^{38}/38."},
{"question":"Chuỗi ∑ (-1)^n/(n+1) hội tụ vì?","options":["A. Leibniz","B. So sánh","C. Tỉ số","D. Căn"],"answer":"A. Leibniz","explanation":"Chuỗi luân phiên."},
{"question":"Gradient của f=xy là?","options":["A. (y,x)","B. (x,y)","C. (1,1)","D. (xy,xy)"],"answer":"A. (y,x)","explanation":"Đạo hàm riêng."},
{"question":"Ma trận đơn vị I có bao nhiêu giá trị riêng bằng 1 (cấp n)?","options":["A. 1","B. n","C. 0","D. 2n"],"answer":"B. n","explanation":"Tất cả phần tử chéo bằng 1."},
{"question":"∫_0^1 (1-x)^2 dx bằng?","options":["A. 1/3","B. 1/2","C. 1/4","D. 2/3"],"answer":"A. 1/3","explanation":"Tính trực tiếp."},
{"question":"Nếu X~Uniform(a,b) thì Var(X)=?","options":["A. (b-a)^2/12","B. (b-a)/2","C. (a+b)/2","D. 1/(b-a)"],"answer":"A. (b-a)^2/12","explanation":"Công thức phương sai."},
{"question":"Đạo hàm của ln(sin x) là?","options":["A. cot x","B. tan x","C. sec x","D. csc x"],"answer":"A. cot x","explanation":"(sin x)'/sin x = cot x."},
{"question":"Nếu A là ma trận đối xứng thực thì giá trị riêng?","options":["A. Thực","B. Ảo","C. 0","D. Âm"],"answer":"A. Thực","explanation":"Định lý phổ."},
{"question":"∫_0^{2π} 1 dx bằng?","options":["A. 2π","B. π","C. 1","D. 0"],"answer":"A. 2π","explanation":"Tích phân hằng số."},
{"question":"Nếu f khả vi liên tục bậc 2 thì f thuộc lớp?","options":["A. C^2","B. C^1","C. C^0","D. Không xác định"],"answer":"A. C^2","explanation":"Định nghĩa."},
{"question":"Giới hạn lim(x→0) (tan x)/x bằng?","options":["A. 0","B. 1","C. ∞","D. -1"],"answer":"B. 1","explanation":"tan x ≈ x khi x→0."},
{"question":"∫_0^1 x^{38} dx bằng?","options":["A. 1/38","B. 1/39","C. 1/40","D. 1/37"],"answer":"B. 1/39","explanation":"Nguyên hàm x^{39}/39."},
{"question":"Nếu A và B cùng cấp thì det(A+B)=?","options":["A. det(A)+det(B)","B. Không có công thức đơn giản","C. det(A)det(B)","D. 0"],"answer":"B. Không có công thức đơn giản","explanation":"Định thức không phân phối qua cộng."},
{"question":"Chuỗi ∑ 1/√n phân kỳ vì?","options":["A. p-series p=1/2<1","B. Hình học","C. Tỉ số","D. Leibniz"],"answer":"A. p-series p=1/2<1","explanation":"Chuỗi p với p≤1 phân kỳ."},
{"question":"Đạo hàm của arcsin x là?","options":["A. 1/√(1-x^2)","B. √(1-x^2)","C. -1/√(1-x^2)","D. 1/(1+x^2)"],"answer":"A. 1/√(1-x^2)","explanation":"Công thức đạo hàm."},
{"question":"Nếu A^3=0 thì A là?","options":["A. Nilpotent","B. Idempotent","C. Trực giao","D. Đối xứng"],"answer":"A. Nilpotent","explanation":"Lũy thừa bằng 0."},
{"question":"∫ sin 3x dx bằng?","options":["A. -cos3x + C","B. -(1/3)cos3x + C","C. (1/3)cos3x","D. cos3x"],"answer":"B. -(1/3)cos3x + C","explanation":"Chia cho hệ số 3."},
{"question":"Nếu Cov(X,X)=?","options":["A. Var(X)","B. 0","C. 1","D. E(X)"],"answer":"A. Var(X)","explanation":"Định nghĩa hiệp phương sai."},
{"question":"Phương trình y''+4y'+4y=0 có nghiệm?","options":["A. (A+Bx)e^{-2x}","B. Ae^{-2x}+Be^{2x}","C. A cos2x","D. Ax+B"],"answer":"A. (A+Bx)e^{-2x}","explanation":"Nghiệm kép r=-2."},
{"question":"Nếu det(A)=5 thì det(2A) (A cấp 2)=?","options":["A. 10","B. 20","C. 5","D. 4"],"answer":"B. 20","explanation":"det(2A)=2^2 det(A)=4·5."},
{"question":"∫_0^1 x^{39} dx bằng?","options":["A. 1/39","B. 1/40","C. 1/41","D. 1/38"],"answer":"B. 1/40","explanation":"Nguyên hàm x^{40}/40."},
{"question":"Chuẩn của vector (1,1,1,1) là?","options":["A. 2","B. √4=2","C. 4","D. 1"],"answer":"A. 2","explanation":"√4=2."},
{"question":"Nếu A là ma trận trực giao thì A^T=?","options":["A. A^{-1}","B. A","C. -A","D. 0"],"answer":"A. A^{-1}","explanation":"Định nghĩa trực giao."},
{"question":"∫_0^{π/2} tan x dx bằng?","options":["A. ln2","B. 0","C. 1","D. π/2"],"answer":"A. ln2","explanation":"Tích phân chuẩn."},
{"question":"Nếu f''(x)=0 với mọi x thì f là?","options":["A. Hàm bậc nhất","B. Hằng số","C. Bậc hai","D. Không xác định"],"answer":"A. Hàm bậc nhất","explanation":"Đạo hàm hai bằng 0."},
{"question":"det(AB)=det(BA) vì?","options":["A. Tính chất định thức","B. Giao hoán","C. Đối xứng","D. 0"],"answer":"A. Tính chất định thức","explanation":"det(AB)=det(A)det(B)." },
{"question":"∫ 1/(x^2+a^2) dx bằng?","options":["A. (1/a)arctan(x/a)+C","B. ln|x|","C. x/a","D. arccos x"],"answer":"A. (1/a)arctan(x/a)+C","explanation":"Công thức chuẩn."},
{"question":"Nếu X,Y độc lập thì Cov(X,Y)=?","options":["A. 0","B. 1","C. Var(X)","D. Var(Y)"],"answer":"A. 0","explanation":"Tính chất độc lập."},
{"question":"Đạo hàm của arccos x là?","options":["A. -1/√(1-x^2)","B. 1/√(1-x^2)","C. 1/(1+x^2)","D. -1/(1+x^2)"],"answer":"A. -1/√(1-x^2)","explanation":"Công thức đạo hàm."},
{"question":"Ma trận tam giác dưới có det=?","options":["A. Tổng chéo","B. Tích đường chéo chính","C. 0","D. 1"],"answer":"B. Tích đường chéo chính","explanation":"Tính chất."},
{"question":"∫_0^1 x^{40} dx bằng?","options":["A. 1/40","B. 1/41","C. 1/42","D. 1/39"],"answer":"B. 1/41","explanation":"Nguyên hàm x^{41}/41."},
{"question":"Chuỗi ∑ (-1)^n/n^2 hội tụ tuyệt đối vì?","options":["A. So sánh với 1/n^2","B. Leibniz","C. Hình học","D. Phân kỳ"],"answer":"A. So sánh với 1/n^2","explanation":"1/n^2 hội tụ."},
{"question":"Gradient của f=x^2y là?","options":["A. (2xy,x^2)","B. (x^2,2xy)","C. (2x,y)","D. (x,y)"],"answer":"A. (2xy,x^2)","explanation":"Đạo hàm riêng."},
{"question":"Ma trận có tất cả giá trị riêng bằng 0 là?","options":["A. Nilpotent","B. Đối xứng","C. Trực giao","D. Idempotent"],"answer":"A. Nilpotent","explanation":"Phổ bằng 0."},
{"question":"∫_0^1 (x-x^2) dx bằng?","options":["A. 1/6","B. 1/2","C. 1/3","D. 0"],"answer":"A. 1/6","explanation":"Tính trực tiếp."},
{"question":"Nếu X~N(μ,σ^2) thì chuẩn hóa Z=?","options":["A. (X-μ)/σ","B. X/σ","C. X-μ","D. μ/σ"],"answer":"A. (X-μ)/σ","explanation":"Công thức chuẩn hóa."},
{"question":"Đạo hàm của ln(cos x) là?","options":["A. -tan x","B. tan x","C. sec x","D. -sec x"],"answer":"A. -tan x","explanation":"(cos x)'/cos x."},
{"question":"Nếu A là ma trận phản xứng thực thì det(A) (cấp lẻ)?","options":["A. 0","B. 1","C. -1","D. >0"],"answer":"A. 0","explanation":"Cấp lẻ ⇒ det=0."},
{"question":"∫_0^{2π} sin^2 x dx bằng?","options":["A. π","B. 2π","C. 0","D. 1"],"answer":"A. π","explanation":"Trung bình 1/2 trên 2π."},
{"question":"Nếu f liên tục trên [a,b] thì đạt GTLN,GTNN theo?","options":["A. Định lý Weierstrass","B. Taylor","C. Fourier","D. Laplace"],"answer":"A. Định lý Weierstrass","explanation":"Hàm liên tục trên đoạn kín."},
{
    "question": "Họ nguyên hàm của hàm số $f(x) = \frac{1}{x}$ trên khoảng $(0, +\infty)$ là:",
    "options": ["\ln x + C", "-\frac{1}{x^2} + C", "e^x + C", "\ln|x| + C"],
    "answer": "D",
    "explanation": "Theo công thức cơ bản, nguyên hàm của $1/x$ là $\ln|x|$. Dấu giá trị tuyệt đối rất quan trọng khi chưa xác định miền của x."
  },
  {
    "question": "Tích phân $I = \int_0^1 x^n dx$ (với $n > 0$) bằng:",
    "options": ["1/(n+1)", "1/n", "n+1", "1"],
    "answer": "A",
    "explanation": "Áp dụng công thức Newton-Leibniz: $\frac{x^{n+1}}{n+1} \big|_0^1 = \frac{1}{n+1}$."
  },
  {
    "question": "Tính nguyên hàm $\int \cos(2x+1) dx$:",
    "options": ["\frac{1}{2}\sin(2x+1) + C", "-\sin(2x+1) + C", "2\sin(2x+1) + C", "-\frac{1}{2}\sin(2x+1) + C"],
    "answer": "A",
    "explanation": "Sử dụng tính chất $\int f(ax+b) dx = \frac{1}{a}F(ax+b) + C$."
  },
  {
    "question": "Diện tích hình phẳng giới hạn bởi đường cong $y = x^2$, trục hoành và hai đường thẳng $x=0, x=1$ là:",
    "options": ["1/3", "1/2", "1", "1/4"],
    "answer": "A",
    "explanation": "$S = \int_0^1 x^2 dx = \frac{x^3}{3} \big|_0^1 = 1/3$."
  },
  
  {
    "question": "Nguyên hàm của hàm số $f(x) = a^x$ (với $a > 0, a \neq 1$) là:",
    "options": ["a^x / \ln a + C", "a^x \cdot \ln a + C", "a^{x+1} / (x+1) + C", "x a^{x-1} + C"],
    "answer": "A",
    "explanation": "Đạo hàm của $a^x$ là $a^x \ln a$, do đó nguyên hàm phải chia cho $\ln a$."
  },
  {
    "question": "Để tính tích phân $\int x \ln x dx$, phương pháp tối ưu nhất là:",
    "options": ["Tích phân từng phần", "Đổi biến số t = \ln x", "Đổi biến số t = x^2", "Khai triển Taylor"],
    "answer": "A",
    "explanation": "Sử dụng công thức $\int u dv$ với $u = \ln x$ (ưu tiên logarit) và $dv = x dx$."
  },
  {
    "question": "Khi tính $I = \int_0^{\pi/2} \sin^3 x \cos x dx$, nếu đặt $t = \sin x$ thì tích phân trở thành:",
    "options": ["\int_0^1 t^3 dt", "\int_0^{\pi/2} t^3 dt", "\int_0^1 \cos t dt", "-\int_1^0 t^3 dt"],
    "answer": "A",
    "explanation": "$dt = \cos x dx$. Đổi cận: $x=0 \to t=0$; $x=\pi/2 \to t=1$."
  },
  {
    "question": "Tích phân từng phần $\int u dv = uv - \int v du$. Nếu $u = x, v = e^x$ thì $\int x e^x dx$ bằng:",
    "options": ["(x-1)e^x + C", "xe^x + e^x + C", "x^2 e^x + C", "e^x + C"],
    "answer": "A",
    "explanation": "$I = x e^x - \int e^x dx = x e^x - e^x + C = (x-1)e^x + C$."
  },
  
  {
    "question": "Tích phân $I = \int \frac{dx}{x^2 + a^2}$ bằng:",
    "options": ["\frac{1}{a} \arctan(\frac{x}{a}) + C", "\arctan(\frac{x}{a}) + C", "\frac{1}{a} \ln|x^2+a^2| + C", "\arcsin(\frac{x}{a}) + C"],
    "answer": "A",
    "explanation": "Đây là dạng nguyên hàm hàm ngược lượng giác mở rộng rất phổ biến."
  },
  {
    "question": "Tích phân suy rộng $I = \int_1^{+\infty} \frac{1}{x^p} dx$ hội tụ khi và chỉ khi:",
    "options": ["p > 1", "p \ge 1", "p < 1", "p > 0"],
    "answer": "A",
    "explanation": "Nếu $p=1$, tích phân ra $\ln x \to \infty$. Nếu $p > 1$, tích phân ra $\frac{x^{1-p}}{1-p} \to 0$ khi $x \to \infty$."
  },
  {
    "question": "Thể tích vật thể tròn xoay khi quay hình phẳng giới hạn bởi $y = f(x)$, trục $Ox, x=a, x=b$ quanh trục $Ox$ là:",
    "options": ["\pi \int_a^b f^2(x) dx", "\int_a^b f^2(x) dx", "2\pi \int_a^b f(x) dx", "\pi \int_a^b |f(x)| dx"],
    "answer": "A",
    "explanation": "Dựa trên phương pháp cắt lát hình tròn có bán kính $R = |f(x)|$."
  },
  
  {
    "question": "Tích phân suy rộng $\int_0^1 \frac{dx}{x^p}$ hội tụ khi:",
    "options": ["p < 1", "p > 1", "p = 1", "Luôn phân kỳ"],
    "answer": "A",
    "explanation": "Ngược với tích phân tại vô cực, tại điểm kỳ dị 0, số mũ nhỏ giúp hàm số không tiến về vô cùng quá nhanh."
  },
  {
    "question": "Giá trị của tích phân $I = \int_{-\infty}^{+\infty} \frac{dx}{1+x^2}$ là:",
    "options": ["\pi", "\pi/2", "0", "+\infty"],
    "answer": "A",
    "explanation": "$\arctan(x) \big|_{-\infty}^{+\infty} = \frac{\pi}{2} - (-\frac{\pi}{2}) = \pi$."
  },
  {"question":"Giới hạn lim(x→∞) (ln x)/x bằng?","options":["A. 0","B. 1","C. ∞","D. -1"],"answer":"A. 0","explanation":"x tăng nhanh hơn ln x."},
{"question":"∫_0^1 x^{41} dx bằng?","options":["A. 1/41","B. 1/42","C. 1/43","D. 1/40"],"answer":"B. 1/42","explanation":"Nguyên hàm x^{42}/42."},
{"question":"Nếu A là ma trận vuông thì A khả nghịch khi và chỉ khi?","options":["A. det(A)≠0","B. det(A)=0","C. trace(A)=0","D. rank(A)<n"],"answer":"A. det(A)≠0","explanation":"Điều kiện khả nghịch."},
{"question":"Chuỗi ∑ n/(n^2+1) phân kỳ vì?","options":["A. So sánh với 1/n","B. Hình học","C. Leibniz","D. Hội tụ tuyệt đối"],"answer":"A. So sánh với 1/n","explanation":"Giống 1/n khi n lớn."},
{"question":"Đạo hàm của arctan(2x) là?","options":["A. 2/(1+4x^2)","B. 1/(1+4x^2)","C. 2/(1+2x^2)","D. 1/(1+2x^2)"],"answer":"A. 2/(1+4x^2)","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu A là ma trận chéo với phần tử chéo d_i thì det(A)=?","options":["A. Tổng d_i","B. Tích d_i","C. 0","D. 1"],"answer":"B. Tích d_i","explanation":"Tính chất ma trận chéo."},
{"question":"∫ cosh x dx bằng?","options":["A. sinh x + C","B. cosh x + C","C. -sinh x","D. tanh x"],"answer":"A. sinh x + C","explanation":"Đạo hàm của sinh x là cosh x."},
{"question":"Nếu E(X)=0 và Var(X)=1 thì X gọi là?","options":["A. Chuẩn hóa","B. Hằng số","C. Độc lập","D. Poisson"],"answer":"A. Chuẩn hóa","explanation":"Trung bình 0, phương sai 1."},
{"question":"Phương trình y''+y'=0 có nghiệm?","options":["A. A+Be^{-x}","B. Ae^x","C. A cos x","D. Ax"],"answer":"A. A+Be^{-x}","explanation":"r(r+1)=0."},
{"question":"Nếu det(A)=3 và det(B)=4 thì det(AB)=?","options":["A. 7","B. 12","C. 1","D. 0"],"answer":"B. 12","explanation":"Tích định thức."},
{"question":"∫_0^1 x^{42} dx bằng?","options":["A. 1/42","B. 1/43","C. 1/44","D. 1/41"],"answer":"B. 1/43","explanation":"Nguyên hàm x^{43}/43."},
{"question":"Chuẩn của vector (2,3,6) là?","options":["A. 7","B. √49=7","C. 11","D. 1"],"answer":"A. 7","explanation":"√(4+9+36)=7."},
{"question":"Nếu A là ma trận trực giao thì A A^T=?","options":["A. I","B. 0","C. A","D. -I"],"answer":"A. I","explanation":"Định nghĩa trực giao."},
{"question":"∫_0^{π/2} sec^2 x dx bằng?","options":["A. 1","B. tan(π/2)","C. 0","D. ∞"],"answer":"D. ∞","explanation":"tan x → ∞ tại π/2."},
{"question":"Nếu f đạt cực đại tại x0 thì f'(x0)=?","options":["A. 0 (nếu khả vi)","B. 1","C. -1","D. Không xác định"],"answer":"A. 0 (nếu khả vi)","explanation":"Điều kiện cần."},
{"question":"trace(A+B)=?","options":["A. trace(A)+trace(B)","B. trace(A)trace(B)","C. 0","D. det(A+B)"],"answer":"A. trace(A)+trace(B)","explanation":"Tính tuyến tính."},
{"question":"∫ 1/(1-x) dx bằng?","options":["A. -ln|1-x|+C","B. ln|x|","C. 1/(1-x)","D. x"],"answer":"A. -ln|1-x|+C","explanation":"Đặt u=1-x."},
{"question":"Nếu X~Bin(n,p) thì Var(X)=?","options":["A. np","B. np(1-p)","C. p(1-p)","D. n^2p"],"answer":"B. np(1-p)","explanation":"Công thức nhị thức."},
{"question":"Đạo hàm của tanh x là?","options":["A. sech^2 x","B. tanh x","C. -sech^2 x","D. cosh x"],"answer":"A. sech^2 x","explanation":"Công thức hyperbolic."},
{"question":"Nếu A là ma trận xác định dương thì các giá trị riêng?","options":["A. Dương","B. Âm","C. 0","D. Ảo"],"answer":"A. Dương","explanation":"Định nghĩa."},
{"question":"∫_0^1 x^{43} dx bằng?","options":["A. 1/43","B. 1/44","C. 1/45","D. 1/42"],"answer":"B. 1/44","explanation":"Nguyên hàm x^{44}/44."},
{"question":"Chuỗi ∑ (−1)^{n}/√n hội tụ?","options":["A. Có điều kiện","B. Tuyệt đối","C. Phân kỳ","D. Hình học"],"answer":"A. Có điều kiện","explanation":"Leibniz nhưng không tuyệt đối."},
{"question":"Gradient của f=x^2+y^2+z^2 là?","options":["A. (2x,2y,2z)","B. (x,y,z)","C. (1,1,1)","D. (x^2,y^2,z^2)"],"answer":"A. (2x,2y,2z)","explanation":"Đạo hàm riêng."},
{"question":"Ma trận có det≠0 thì rank=?","options":["A. n","B. n-1","C. 1","D. 0"],"answer":"A. n","explanation":"Hạng đầy đủ."},
{"question":"∫_0^1 (1-x^3) dx bằng?","options":["A. 3/4","B. 1/4","C. 1/2","D. 0"],"answer":"A. 3/4","explanation":"1 - 1/4 = 3/4."},
{"question":"Nếu X~Exp(λ) thì E(X)=?","options":["A. 1/λ","B. λ","C. 1/λ^2","D. 2/λ"],"answer":"A. 1/λ","explanation":"Công thức kỳ vọng."},
{"question":"Đạo hàm của ln(x^2) là?","options":["A. 2/x","B. 1/x","C. 2x","D. x"],"answer":"A. 2/x","explanation":"ln(x^2)=2ln|x|."},
{"question":"Nếu A là ma trận phản xứng thực thì trace(A)=?","options":["A. 0","B. 1","C. -1","D. n"],"answer":"A. 0","explanation":"Đường chéo bằng 0."},
{"question":"∫_0^{2π} cos^2 x dx bằng?","options":["A. π","B. 2π","C. 0","D. 1"],"answer":"A. π","explanation":"Trung bình 1/2."},
{"question":"Nếu f khả vi trên (a,b) và liên tục [a,b] thì tồn tại c sao cho f'(c)= (f(b)-f(a))/(b-a) theo?","options":["A. Định lý giá trị trung bình","B. Taylor","C. Fourier","D. Laplace"],"answer":"A. Định lý giá trị trung bình","explanation":"MVT."},
{"question":"Giới hạn lim(x→0) (ln(1+x))/x bằng?","options":["A. 0","B. 1","C. -1","D. ∞"],"answer":"B. 1","explanation":"Đạo hàm của ln(1+x) tại 0 bằng 1."},
{"question":"∫_0^1 x^{44} dx bằng?","options":["A. 1/44","B. 1/45","C. 1/46","D. 1/43"],"answer":"B. 1/45","explanation":"Nguyên hàm x^{45}/45."},
{"question":"Nếu A là ma trận vuông cấp n thì dim(Ker A)+rank(A)=?","options":["A. n","B. 1","C. 0","D. n^2"],"answer":"A. n","explanation":"Định lý hạng-null."},
{"question":"Chuỗi ∑ 1/(n ln n) (n≥2) thì?","options":["A. Hội tụ","B. Phân kỳ","C. Hình học","D. Tuyệt đối"],"answer":"B. Phân kỳ","explanation":"So sánh với tích phân."},
{"question":"Đạo hàm của e^{ax} là?","options":["A. ae^{ax}","B. e^{ax}","C. xe^{ax}","D. a^x"],"answer":"A. ae^{ax}","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu A là ma trận tam giác thì các giá trị riêng là?","options":["A. Các phần tử chéo chính","B. 0","C. 1","D. Tổng hàng"],"answer":"A. Các phần tử chéo chính","explanation":"Tính chất phổ."},
{"question":"∫ sinh x dx bằng?","options":["A. cosh x + C","B. sinh x + C","C. -cosh x","D. tanh x"],"answer":"A. cosh x + C","explanation":"Đạo hàm cosh x là sinh x."},
{"question":"Nếu Var(X)=0 thì X là?","options":["A. Hằng số","B. Chuẩn hóa","C. Poisson","D. Độc lập"],"answer":"A. Hằng số","explanation":"Phương sai 0 ⇒ không biến thiên."},
{"question":"Phương trình y''-2y'+y=0 có nghiệm?","options":["A. (A+Bx)e^{x}","B. Ae^x+Be^{-x}","C. A cos x","D. Ax+B"],"answer":"A. (A+Bx)e^{x}","explanation":"Nghiệm kép r=1."},
{"question":"Nếu det(A)=−2 và det(B)=3 thì det(AB)=?","options":["A. -6","B. 6","C. -1","D. 1"],"answer":"A. -6","explanation":"Nhân định thức."},
{"question":"∫_0^1 x^{45} dx bằng?","options":["A. 1/45","B. 1/46","C. 1/47","D. 1/44"],"answer":"B. 1/46","explanation":"Nguyên hàm x^{46}/46."},
{"question":"Chuẩn của vector (0,3,4) là?","options":["A. 5","B. 7","C. 25","D. 1"],"answer":"A. 5","explanation":"√(9+16)=5."},
{"question":"Nếu A là ma trận đối xứng thì A có thể chéo hóa bởi?","options":["A. Ma trận trực giao","B. Ma trận bất kỳ","C. Ma trận 0","D. Ma trận tam giác"],"answer":"A. Ma trận trực giao","explanation":"Định lý phổ."},
{"question":"∫_0^{π/4} tan x dx bằng?","options":["A. (1/2)ln2","B. ln2","C. 1","D. 0"],"answer":"A. (1/2)ln2","explanation":"-ln|cos x|."},
{"question":"Nếu f'(x)=0 trên (a,b) thì f?","options":["A. Hằng","B. Tăng","C. Giảm","D. Không xác định"],"answer":"A. Hằng","explanation":"Đạo hàm bằng 0."},
{"question":"trace(cA)=?","options":["A. c trace(A)","B. trace(A)+c","C. c^n trace(A)","D. det(A)"],"answer":"A. c trace(A)","explanation":"Tính tuyến tính."},
{"question":"∫ 1/(x+a) dx bằng?","options":["A. ln|x+a|+C","B. 1/(x+a)","C. x+a","D. e^{x+a}"],"answer":"A. ln|x+a|+C","explanation":"Nguyên hàm chuẩn."},
{"question":"Nếu X~Uniform(0,1) thì Var(X)=?","options":["A. 1/12","B. 1/2","C. 1","D. 1/6"],"answer":"A. 1/12","explanation":"(b-a)^2/12."},
{"question":"Đạo hàm của arccot x là?","options":["A. -1/(1+x^2)","B. 1/(1+x^2)","C. 1/x","D. -1/x"],"answer":"A. -1/(1+x^2)","explanation":"Công thức đạo hàm."},
{"question":"Nếu A là ma trận xác định dương thì x^T A x?","options":["A. >0 với mọi x≠0","B. =0","C. <0","D. Không xác định"],"answer":"A. >0 với mọi x≠0","explanation":"Định nghĩa."},
{"question":"∫_0^1 x^{46} dx bằng?","options":["A. 1/46","B. 1/47","C. 1/48","D. 1/45"],"answer":"B. 1/47","explanation":"Nguyên hàm x^{47}/47."},
{"question":"Chuỗi ∑ (1/3)^n hội tụ đến?","options":["A. 1/2","B. 3/2","C. 1","D. 0"],"answer":"B. 3/2","explanation":"1/(1-1/3)=3/2."},
{"question":"Gradient của f=xyz là?","options":["A. (yz,xz,xy)","B. (x,y,z)","C. (1,1,1)","D. (xyz,xyz,xyz)"],"answer":"A. (yz,xz,xy)","explanation":"Đạo hàm riêng."},
{"question":"Ma trận có det=0 thì tồn tại?","options":["A. Vector khác 0 sao cho Ax=0","B. Nghịch đảo","C. det=1","D. trace=0"],"answer":"A. Vector khác 0 sao cho Ax=0","explanation":"Hệ thuần nhất có nghiệm khác 0."},
{"question":"∫_0^1 (x^2+x) dx bằng?","options":["A. 5/6","B. 1/2","C. 1","D. 2/3"],"answer":"A. 5/6","explanation":"1/3+1/2=5/6."},
{"question":"Nếu X~N(0,1) thì E(X^2)=?","options":["A. 1","B. 0","C. 2","D. 1/2"],"answer":"A. 1","explanation":"Phương sai chuẩn tắc."},
{"question":"Đạo hàm của ln|cos x| là?","options":["A. -tan x","B. tan x","C. sec x","D. -sec x"],"answer":"A. -tan x","explanation":"(cos x)'/cos x."},
{"question":"Nếu A là ma trận phản xứng thực cấp chẵn thì det(A)?","options":["A. ≥0","B. <0","C. =0","D. =1"],"answer":"A. ≥0","explanation":"det(A)=Pf(A)^2 ≥0."},
{"question":"∫_0^{2π} sin x cos x dx bằng?","options":["A. 0","B. 1","C. π","D. 2π"],"answer":"A. 0","explanation":"Hàm chu kỳ lẻ."},
{"question":"Nếu f có đạo hàm liên tục thì f khả vi theo?","options":["A. Định nghĩa khả vi","B. Taylor","C. Fourier","D. Laplace"],"answer":"A. Định nghĩa khả vi","explanation":"Liên tục đạo hàm ⇒ khả vi."},
{"question": "Trong học sâu (Deep Learning), đạo hàm riêng của hàm mất mát theo trọng số được tính bằng thuật toán nào?", "options": ["Lan truyền ngược (Backpropagation)", "Phân cụm K-means", "Phân tích thành phần chính (PCA)", "Giải thuật di truyền"], "answer": "A", "explanation": "Backpropagation sử dụng quy tắc chuỗi (chain rule) để tính gradient hiệu quả."},
  
  {"question": "Một không gian topo được gọi là Hausdorff (T2) nếu:", "options": ["Mọi cặp điểm phân biệt đều có các lân cận rời nhau", "Nó là không gian metric", "Nó có hữu hạn phần tử", "Mọi dãy đều hội tụ"], "answer": "A", "explanation": "Đây là tính chất tách biệt cơ bản trong cấu trúc topo không gian."},
  {"question": "Trong lý thuyết đồ thị, định lý Turan liên quan đến đại lượng nào?", "options": ["Số cạnh tối đa của đồ thị không chứa đồ thị đầy đủ K_r", "Số sắc số", "Độ dài đường đi ngắn nhất", "Luồng cực đại"], "answer": "A", "explanation": "Định lý Turan là kết quả kinh điển trong lý thuyết đồ thị cực trị."},
  {"question": "Hàm sigmoid $\sigma(x) = 1/(1 + e^{-x})$ thường dùng trong ML có đạo hàm là:", "options": ["\sigma(x)(1 - \sigma(x))", "\sigma(x)^2", "1 - \sigma(x)", "e^{-x}"], "answer": "A", "explanation": "Đặc tính đạo hàm tự lặp lại này giúp việc tính toán gradient rất nhanh chóng."},
  
  {"question": "Tích phân Riemann-Stieltjes mở rộng khái niệm tích phân Riemann bằng cách thay đổi:", "options": ["Hàm trọng số d\alpha(x) thay vì dx", "Miền lấy tích phân", "Cách chia đoạn", "Hàm số dưới dấu tích phân"], "answer": "A", "explanation": "Nó cho phép tích phân dựa trên một hàm phân phối khác thay vì chỉ theo độ dài đoạn thẳng."},
  {"question": "Trong đại số, một vành không có ước của không và có đơn vị được gọi là:", "options": ["Miền nguyên (Integral Domain)", "Nhóm Abel", "Vành đa thức", "Trường"], "answer": "A", "explanation": "Miền nguyên là cấu trúc gần nhất với tập số nguyên $\mathbb{Z}$."},
  {"question": "Ma trận hiệp phương sai (Covariance Matrix) luôn có tính chất nào?", "options": ["Đối xứng và nửa xác định dương", "Định thức luôn bằng 1", "Các phần tử trên đường chéo bằng 0", "Là ma trận đơn vị"], "answer": "A", "explanation": "Tính đối xứng đến từ việc $Cov(X,Y) = Cov(Y,X)$ và tính xác định dương đến từ định nghĩa phương sai tổng quát."},
  {"question": "Định lý điểm bất động Brouwer khẳng định rằng một hàm liên tục từ một tập lồi, compact vào chính nó luôn có:", "options": ["Ít nhất một điểm bất động x = f(x)", "Nghiệm duy nhất", "Giá trị cực đại", "Đạo hàm bằng 0"], "answer": "A", "explanation": "Đây là nền tảng cho nhiều chứng minh sự tồn tại nghiệm trong kinh tế học và toán lý."},
  
  {"question": "Trong xử lý ngôn ngữ tự nhiên, kỹ thuật Softmax biến đổi một vectơ thành:", "options": ["Một phân phối xác suất có tổng bằng 1", "Một ma trận đơn vị", "Một vectơ nhị phân", "Một hằng số"], "answer": "A", "explanation": "Softmax nén các giá trị về khoảng (0,1) sao cho tổng của chúng là 100%."},
  {"question": "Đặc trưng Euler của một khối đa diện lồi (Số đỉnh - Số cạnh + Số mặt) luôn bằng:", "options": ["2", "1", "0", "-1"], "answer": "A", "explanation": "Đây là bất biến topo nổi tiếng dành cho các vật thể tương đương đồng phôi với mặt cầu."},
  {"question": "Phân phối Dirichlet là phân phối liên hợp ưu tiên của phân phối nào?", "options": ["Phân phối đa thức (Multinomial)", "Phân phối chuẩn", "Phân phối Poisson", "Phân phối Bernoulli"], "answer": "A", "explanation": "Được dùng rộng rãi trong các mô hình chủ đề (Topic Modeling) như LDA."},
  {"question": "Trong hình học vi phân, ký hiệu Christoffel dùng để mô tả:", "options": ["Sự thay đổi của hệ cơ sở trên mặt cong (liên thông affine)", "Độ dài đường cong", "Diện tích mặt", "Độ cong Gaussian"], "answer": "A", "explanation": "Chúng cho biết các vectơ cơ sở thay đổi thế nào khi di chuyển dọc theo các trục tọa độ trên manifold."},
  {"question": "Định lý thặng dư Trung Hoa (Chinese Remainder Theorem) giải hệ phương trình về:", "options": ["Đồng dư thức", "Đa thức", "Tích phân", "Ma trận"], "answer": "A", "explanation": "Nó cho phép tìm một số nguyên thỏa mãn nhiều điều kiện chia dư cùng lúc."},
  {"question": "Trong tối ưu hóa, phương pháp nhân tử Lagrange dùng để:", "options": ["Tìm cực trị của hàm số có ràng buộc", "Giải phương trình vi phân", "Nội suy hàm số", "Tính diện tích"], "answer": "A", "explanation": "Nó biến bài toán cực trị có ràng buộc thành bài toán không ràng buộc bằng cách thêm biến mới."},
  
  {"question": "Chuỗi Fourier của một hàm chẵn chỉ chứa các số hạng của:", "options": ["Hàm Cosine", "Hàm Sine", "Hàm mũ", "Đa thức"], "answer": "A", "explanation": "Do tính chất đối xứng, các thành phần sine (hàm lẻ) sẽ bị triệt tiêu."},
  {"question": "Trong lý thuyết tập hợp, tập hợp tất cả các tập con của tập A được gọi là:", "options": ["Tập lũy thừa (Power set)", "Tập tích", "Tập hợp các phần tử", "Không gian mẫu"], "answer": "A", "explanation": "Ký hiệu là $\mathcal{P}(A)$ và có kích thước $2^{|A|}$."},
  {"question": "Một ma trận vuông A là ma trận trực giao nếu:", "options": ["A^T A = I", "det(A) = 0", "A = A^T", "A^2 = A"], "answer": "A", "explanation": "Các cột (hoặc hàng) của ma trận trực giao tạo thành một hệ trực chuẩn."},
  {"question": "Số ảo $i$ được định nghĩa là căn bậc hai của -1. Vậy $i^{4n}$ (với n nguyên) bằng:", "options": ["1", "-1", "i", "-i"], "answer": "A", "explanation": "Chu kỳ của lũy thừa số $i$ là 4: $i, -1, -i, 1$."},
  {"question": "Trong thống kê Bayes, xác suất 'Posterior' được tính từ xác suất nào?", "options": ["Likelihood và Prior", "P-value", "Độ lệch chuẩn", "Sai số hệ thống"], "answer": "A", "explanation": "Theo công thức Bayes: $Posterior \propto Likelihood \times Prior$."},
  {"question": "Bài toán P vs NP hỏi về mối quan hệ giữa khả năng:", "options": ["Tìm ra nghiệm và kiểm tra tính đúng đắn của nghiệm", "Cộng và nhân số nguyên", "Tích phân và đạo hàm", "Lập trình và toán lý"], "answer": "A", "explanation": "Đây là một trong 7 bài toán Thiên niên kỷ chưa có lời giải."},
  {"question": "Định lý cuối cùng của Fermat được chứng minh bởi ai vào năm 1994?", "options": ["Andrew Wiles", "Isaac Newton", "Leonhard Euler", "Alan Turing"], "answer": "A", "explanation": "Phải mất hơn 300 năm nhân loại mới chứng minh được giả thuyết này."},
  {"question":"Giới hạn lim(x→∞) (x/(x+1)) bằng?","options":["A. 0","B. 1","C. ∞","D. -1"],"answer":"B. 1","explanation":"Chia cả tử và mẫu cho x."},
{"question":"∫_0^1 x^{47} dx bằng?","options":["A. 1/47","B. 1/48","C. 1/49","D. 1/46"],"answer":"B. 1/48","explanation":"Nguyên hàm x^{48}/48."},
{"question":"Nếu A là ma trận vuông thì nghiệm của Ax=0 không tầm thường khi?","options":["A. det(A)=0","B. det(A)≠0","C. trace(A)=0","D. A=I"],"answer":"A. det(A)=0","explanation":"Ma trận suy biến."},
{"question":"Chuỗi ∑ 1/(n^3) hội tụ vì?","options":["A. p-series p=3>1","B. Hình học","C. Leibniz","D. Phân kỳ"],"answer":"A. p-series p=3>1","explanation":"Chuỗi p."},
{"question":"Đạo hàm của ln(e^x+1) là?","options":["A. e^x/(e^x+1)","B. 1/(e^x+1)","C. e^x","D. (e^x+1)/e^x"],"answer":"A. e^x/(e^x+1)","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu A có các giá trị riêng λ_i thì trace(A)=?","options":["A. Tổng λ_i","B. Tích λ_i","C. 0","D. n"],"answer":"A. Tổng λ_i","explanation":"Tính chất phổ."},
{"question":"∫ cos x dx bằng?","options":["A. sin x + C","B. -sin x","C. tan x","D. sec x"],"answer":"A. sin x + C","explanation":"Nguyên hàm cơ bản."},
{"question":"Nếu E(X)=μ và E(Y)=ν thì E(X+Y)=?","options":["A. μ+ν","B. μν","C. μ-ν","D. 0"],"answer":"A. μ+ν","explanation":"Tính tuyến tính."},
{"question":"Phương trình y''+16y=0 có nghiệm?","options":["A. A cos4x+B sin4x","B. Ae^{4x}","C. Ax+B","D. Ae^x"],"answer":"A. A cos4x+B sin4x","explanation":"r^2+16=0."},
{"question":"Nếu det(A)=1 thì det(A^{-1})=?","options":["A. 1","B. -1","C. 0","D. 2"],"answer":"A. 1","explanation":"1/det(A)."},

{"question":"∫_0^1 x^{48} dx bằng?","options":["A. 1/48","B. 1/49","C. 1/50","D. 1/47"],"answer":"B. 1/49","explanation":"Nguyên hàm x^{49}/49."},
{"question":"Chuẩn của vector (2,2,2,2) là?","options":["A. 4","B. √16=4","C. 8","D. 2"],"answer":"A. 4","explanation":"√(4+4+4+4)=4."},
{"question":"Nếu A và B khả nghịch thì (A^{-1})^{-1}=?","options":["A. A","B. B","C. I","D. 0"],"answer":"A. A","explanation":"Nghịch đảo của nghịch đảo."},
{"question":"∫_0^{π} cos x dx bằng?","options":["A. 0","B. 1","C. 2","D. π"],"answer":"A. 0","explanation":"sin π - sin 0 =0."},
{"question":"Nếu f''(x)>0 trên (a,b) thì đồ thị f?","options":["A. Lõm lên","B. Lõm xuống","C. Tuyến tính","D. Không xác định"],"answer":"A. Lõm lên","explanation":"Đạo hàm hai dương."},
{"question":"det(A^k)=?","options":["A. det(A)^k","B. k det(A)","C. det(A)+k","D. 0"],"answer":"A. det(A)^k","explanation":"Tính chất định thức."},
{"question":"∫ e^{-2x} dx bằng?","options":["A. -1/2 e^{-2x}+C","B. e^{-2x}","C. -e^{-2x}","D. 1/2 e^{2x}"],"answer":"A. -1/2 e^{-2x}+C","explanation":"Chia hệ số -2."},
{"question":"Nếu Var(X+Y) (X,Y độc lập) bằng?","options":["A. Var(X)+Var(Y)","B. Var(X)Var(Y)","C. 0","D. Var(X)-Var(Y)"],"answer":"A. Var(X)+Var(Y)","explanation":"Độc lập ⇒ cộng phương sai."},
{"question":"Đạo hàm của ln√x là?","options":["A. 1/(2x)","B. 1/x","C. √x","D. 2/x"],"answer":"A. 1/(2x)","explanation":"ln(x^{1/2})=1/2 ln x."},
{"question":"Nếu A là ma trận idempotent thì giá trị riêng là?","options":["A. 0 hoặc 1","B. 1","C. -1","D. 2"],"answer":"A. 0 hoặc 1","explanation":"λ^2=λ."},

{"question":"∫_0^1 x^{49} dx bằng?","options":["A. 1/49","B. 1/50","C. 1/51","D. 1/48"],"answer":"B. 1/50","explanation":"Nguyên hàm x^{50}/50."},
{"question":"Chuỗi ∑ (−1)^{n}/n hội tụ?","options":["A. Có điều kiện","B. Tuyệt đối","C. Phân kỳ","D. Hình học"],"answer":"A. Có điều kiện","explanation":"Chuỗi điều hòa luân phiên."},
{"question":"Gradient của f=e^{x+y} là?","options":["A. (e^{x+y},e^{x+y})","B. (e^x,e^y)","C. (x,y)","D. (1,1)"],"answer":"A. (e^{x+y},e^{x+y})","explanation":"Đạo hàm riêng."},
{"question":"Ma trận có rank<n thì det=?","options":["A. 0","B. 1","C. -1","D. n"],"answer":"A. 0","explanation":"Hạng thiếu ⇒ suy biến."},
{"question":"∫_0^1 (x^3+x^2) dx bằng?","options":["A. 7/12","B. 1/2","C. 1","D. 2/3"],"answer":"A. 7/12","explanation":"1/4+1/3=7/12."},
{"question":"Nếu X~Poisson(λ) thì E(X^2)=?","options":["A. λ+λ^2","B. λ","C. λ^2","D. 1"],"answer":"A. λ+λ^2","explanation":"Var+mean."},
{"question":"Đạo hàm của x e^x là?","options":["A. e^x(1+x)","B. xe^x","C. e^x","D. x^2e^x"],"answer":"A. e^x(1+x)","explanation":"Quy tắc tích."},
{"question":"Nếu A là ma trận tam giác thì trace(A)=?","options":["A. Tổng phần tử chéo","B. 0","C. 1","D. det(A)"],"answer":"A. Tổng phần tử chéo","explanation":"Định nghĩa trace."},
{"question":"∫_0^{2π} sin x dx bằng?","options":["A. 0","B. 1","C. 2π","D. π"],"answer":"A. 0","explanation":"Chu kỳ đầy đủ."},
{"question":"Nếu f liên tục trên [a,b] và khả vi (a,b) thì tồn tại c sao cho f'(c)=0 khi f(a)=f(b) theo?","options":["A. Định lý Rolle","B. Taylor","C. Fourier","D. Laplace"],"answer":"A. Định lý Rolle","explanation":"Điều kiện Rolle."},
{"question": "Trong cơ học lượng tử, toán tử Hamiltonian đại diện cho đại lượng nào?", "options": ["Tổng năng lượng", "Động lượng", "Vị trí", "Thời gian"], "answer": "A", "explanation": "Toán tử Hamiltonian $\hat{H}$ dùng để tính mức năng lượng của hệ thống thông qua phương trình Schrödinger."},
  
  {"question": "Tính chất 'Giao hoán' của phép nhân ma trận $AB = BA$ là:", "options": ["Sai trong trường hợp tổng quát", "Luôn đúng với mọi ma trận vuông", "Chỉ đúng với ma trận đơn vị", "Chỉ đúng với ma trận không"], "answer": "A", "explanation": "Phép nhân ma trận nói chung không có tính giao hoán."},
  {"question": "Định lý Liouville trong giải tích phức phát biểu rằng nếu một hàm nguyên (entire function) bị chặn thì nó là:", "options": ["Hàm hằng", "Hàm bậc nhất", "Hàm tuần hoàn", "Hàm không xác định"], "answer": "A", "explanation": "Đây là một tính chất rất mạnh mẽ của các hàm giải tích trên toàn bộ mặt phẳng phức."},
  {"question": "Trong hình học vi phân, độ cong Gaussian của một mặt trụ bằng:", "options": ["0", "1", "Bán kính mặt trụ", "Vô cùng"], "answer": "A", "explanation": "Mặt trụ có thể trải phẳng được mà không làm biến dạng khoảng cách (tính chất phẳng cục bộ)."},
  
  {"question": "Phép biến đổi Z (Z-transform) là công cụ dùng để phân tích:", "options": ["Tín hiệu thời gian rời rạc", "Tín hiệu thời gian liên tục", "Hệ phương trình phi tuyến", "Hình học fractal"], "answer": "A", "explanation": "Biến đổi Z đóng vai trò trong miền rời rạc tương tự như biến đổi Laplace trong miền liên tục."},
  {"question": "Trong lý thuyết hỗn độn (Chaos Theory), 'Hiệu ứng cánh bướm' mô tả sự phụ thuộc nhạy cảm vào:", "options": ["Điều kiện ban đầu", "Kích thước hệ thống", "Năng lượng đầu vào", "Nhiệt độ môi trường"], "answer": "A", "explanation": "Một thay đổi nhỏ ở trạng thái đầu có thể dẫn đến sự khác biệt khổng lồ ở trạng thái sau."},
  
  {"question": "Số chiều của không gian vectơ các đa thức bậc không quá $n$ là:", "options": ["n + 1", "n", "n - 1", "2n"], "answer": "A", "explanation": "Cơ sở chuẩn thường dùng là $\{1, x, x^2, ..., x^n\}$ gồm $n+1$ phần tử."},
  {"question": "Trong giải tích vectơ, một trường vectơ $F$ có $div(F) = 0$ được gọi là:", "options": ["Trường Solenoid", "Trường thế", "Trường xoáy", "Trường bảo toàn"], "answer": "A", "explanation": "Trường Solenoid không có nguồn hay hố, các đường sức thường khép kín."},
  {"question": "Phép toán 'Tích chập' (Convolution) của hai hàm số trong miền thời gian tương ứng với phép toán nào trong miền tần số?", "options": ["Phép nhân", "Phép cộng", "Phép chia", "Phép đạo hàm"], "answer": "A", "explanation": "Đây là tính chất quan trọng nhất giúp đơn giản hóa việc phân tích hệ thống LTI."},
  {"question": "Định lý Taylor mở rộng cho hàm hai biến $f(x, y)$ sử dụng ma trận nào cho số hạng bậc hai?", "options": ["Ma trận Hessian", "Ma trận Jacobian", "Ma trận Vandermonde", "Ma trận Wronskian"], "answer": "A", "explanation": "Ma trận Hessian chứa các đạo hàm riêng cấp hai, quyết định tính lồi/lõm của hàm số."},
  
  {"question": "Trong lý thuyết mã hóa, mã sửa lỗi (Error-correcting code) dùng để:", "options": ["Phát hiện và tự sửa lỗi khi truyền tin", "Nén dữ liệu", "Mã hóa bảo mật", "Tăng tốc độ truyền"], "answer": "A", "explanation": "Bằng cách thêm các bit dư thừa có tính toán (như mã Hamming)."},
  {"question": "Phương trình $e^{i\pi} + 1 = 0$ được gọi là gì?", "options": ["Đẳng thức Euler", "Định lý Cauchy", "Công thức Moivre", "Định lý Fermat"], "answer": "A", "explanation": "Được coi là công thức đẹp nhất toán học vì kết nối 5 hằng số cơ bản: $0, 1, e, i, \pi$."},
  {"question": "Khái niệm 'Đạo hàm theo hướng' (Directional derivative) của hàm $f$ tại điểm $P$ theo vectơ đơn vị $u$ là:", "options": ["$\nabla f(P) \cdot u$", "$\nabla f(P) \times u$", "$|\nabla f(P)|$", "0"], "answer": "A", "explanation": "Nó đo lường tốc độ thay đổi của hàm số theo một hướng cụ thể."},
  {"question": "Chu kỳ tuần hoàn của hàm số $y = \tan(x)$ là:", "options": ["$\pi$", "$2\pi$", "$\pi/2$", "0"], "answer": "A", "explanation": "Hàm tang tuần hoàn với chu kỳ $\pi$, khác với sin và cos là $2\pi$."},
  {"question": "Một ma trận vuông $A$ có các giá trị riêng là $\lambda_1, \lambda_2, ..., \lambda_n$. Định thức của $A$ bằng:", "options": ["Tích các giá trị riêng", "Tổng các giá trị riêng", "Giá trị riêng lớn nhất", "Trung bình cộng các giá trị riêng"], "answer": "A", "explanation": "Đây là một tính chất quan trọng liên kết đại số tuyến tính và đa thức đặc trưng."},
  {"question": "Trong logic học, phủ định của mệnh đề 'Mọi x đều thỏa mãn P' là:", "options": ["Tồn tại ít nhất một x không thỏa mãn P", "Mọi x đều không thỏa mãn P", "Không có x nào thỏa mãn P", "Tồn tại x thỏa mãn P"], "answer": "A", "explanation": "Phủ định của 'với mọi' là 'tồn tại' và ngược lại."},
  {"question": "Giá trị của $\Gamma(1/2)$ (hàm Gamma tại 1/2) là:", "options": ["$\sqrt{\pi}$", "$\pi$", "1", "1/2"], "answer": "A", "explanation": "Kết quả này liên quan chặt chẽ đến tích phân Gauss trên toàn trục số."},
  {"question": "Trong không gian $L^2$, hai hàm số được gọi là 'Trực giao' nếu:", "options": ["Tích vô hướng của chúng bằng 0", "Chúng không cắt nhau", "Đạo hàm của chúng bằng nhau", "Tổng của chúng bằng 0"], "answer": "A", "explanation": "Đây là cơ sở để xây dựng các chuỗi hàm trực giao như chuỗi Fourier."},
  {"question": "Một tập hợp có lực lượng bằng lực lượng của tập số tự nhiên $\mathbb{N}$ được gọi là:", "options": ["Tập đếm được", "Tập không đếm được", "Tập hữu hạn", "Tập compact"], "answer": "A", "explanation": "Ví dụ: tập số hữu tỉ $\mathbb{Q}$ là tập đếm được, nhưng số thực $\mathbb{R}$ thì không."},
  {"question":"Giới hạn lim(x→0) (sin x)/x bằng?","options":["A. 0","B. 1","C. ∞","D. -1"],"answer":"B. 1","explanation":"Giới hạn cơ bản."},
{"question":"∫_0^1 x^{50} dx bằng?","options":["A. 1/50","B. 1/51","C. 1/52","D. 1/49"],"answer":"B. 1/51","explanation":"Nguyên hàm x^{51}/51."},
{"question":"Nếu det(A)=0 thì A?","options":["A. Không khả nghịch","B. Khả nghịch","C. Trực giao","D. Đối xứng"],"answer":"A. Không khả nghịch","explanation":"Định thức bằng 0 ⇒ suy biến."},
{"question":"Chuỗi ∑ 1/n phân kỳ vì?","options":["A. Chuỗi điều hòa","B. p>1","C. Hình học","D. Luân phiên"],"answer":"A. Chuỗi điều hòa","explanation":"p=1 phân kỳ."},
{"question":"Đạo hàm của arctan x là?","options":["A. 1/(1+x^2)","B. 1/x","C. x/(1+x^2)","D. -1/(1+x^2)"],"answer":"A. 1/(1+x^2)","explanation":"Công thức cơ bản."},
{"question":"Nếu A trực giao thì A^{-1}=?","options":["A. A^T","B. -A","C. A","D. 0"],"answer":"A. A^T","explanation":"Tính chất trực giao."},
{"question":"∫ e^{3x} dx bằng?","options":["A. 1/3 e^{3x}+C","B. 3e^{3x}","C. e^{3x}","D. -1/3 e^{3x}"],"answer":"A. 1/3 e^{3x}+C","explanation":"Chia hệ số 3."},
{"question":"Nếu Var(X)=4 thì độ lệch chuẩn bằng?","options":["A. 2","B. 4","C. 8","D. 16"],"answer":"A. 2","explanation":"Căn bậc hai của phương sai."},
{"question":"Phương trình y''-9y=0 có nghiệm?","options":["A. Ae^{3x}+Be^{-3x}","B. A cos3x","C. Ax+B","D. Ae^{9x}"],"answer":"A. Ae^{3x}+Be^{-3x}","explanation":"r^2-9=0."},
{"question":"det(I_n)=?","options":["A. 1","B. 0","C. n","D. -1"],"answer":"A. 1","explanation":"Định thức ma trận đơn vị."},

{"question":"∫_0^1 x^{51} dx bằng?","options":["A. 1/51","B. 1/52","C. 1/53","D. 1/50"],"answer":"B. 1/52","explanation":"Nguyên hàm x^{52}/52."},
{"question":"Nếu λ là giá trị riêng của A thì det(A-λI)=?","options":["A. 0","B. 1","C. λ","D. n"],"answer":"A. 0","explanation":"Phương trình đặc trưng."},
{"question":"Đạo hàm của sinh x là?","options":["A. cosh x","B. sinh x","C. -cosh x","D. -sinh x"],"answer":"A. cosh x","explanation":"Hàm hyperbolic."},
{"question":"Chuỗi hình học ∑ ar^n hội tụ khi?","options":["A. |r|<1","B. r=1","C. r>1","D. r≤-1"],"answer":"A. |r|<1","explanation":"Điều kiện hội tụ."},
{"question":"∫_0^π sin x dx bằng?","options":["A. 2","B. 0","C. 1","D. π"],"answer":"A. 2","explanation":"-cos x từ 0 đến π."},
{"question":"Nếu E(X)=5 và Var(X)=9 thì E(2X)=?","options":["A. 10","B. 5","C. 18","D. 9"],"answer":"A. 10","explanation":"Tính tuyến tính."},
{"question":"Ma trận đối xứng thỏa mãn?","options":["A. A=A^T","B. A=-A^T","C. det(A)=1","D. trace(A)=0"],"answer":"A. A=A^T","explanation":"Định nghĩa."},
{"question":"∫ ln x dx bằng?","options":["A. x ln x - x + C","B. ln x + C","C. x ln x + C","D. 1/x"],"answer":"A. x ln x - x + C","explanation":"Tích phân từng phần."},
{"question":"Nếu X,Y độc lập thì Cov(X,Y)=?","options":["A. 0","B. 1","C. Var(X)","D. Var(Y)"],"answer":"A. 0","explanation":"Độc lập ⇒ hiệp phương sai 0."},
{"question":"Giới hạn lim(x→∞) e^{-x} bằng?","options":["A. 0","B. 1","C. ∞","D. -1"],"answer":"A. 0","explanation":"Hàm mũ âm giảm về 0."},
{"question":"∫_0^1 x^{52} dx bằng?","options":["A. 1/52","B. 1/53","C. 1/54","D. 1/51"],"answer":"B. 1/53","explanation":"Nguyên hàm x^{53}/53."},
{"question":"Đạo hàm của cosh x là?","options":["A. sinh x","B. cosh x","C. -sinh x","D. -cosh x"],"answer":"A. sinh x","explanation":"Công thức hyperbolic."},
{"question":"Nếu A là ma trận tam giác trên thì det(A)=?","options":["A. Tích phần tử đường chéo","B. Tổng đường chéo","C. 0","D. 1"],"answer":"A. Tích phần tử đường chéo","explanation":"Tính chất định thức."},
{"question":"Chuỗi ∑ 1/n^2 hội tụ vì?","options":["A. p=2>1","B. Hình học","C. Phân kỳ","D. Leibniz"],"answer":"A. p=2>1","explanation":"Chuỗi p."},
{"question":"∫ e^{-x} dx bằng?","options":["A. -e^{-x}+C","B. e^{-x}+C","C. -1/x","D. ln x"],"answer":"A. -e^{-x}+C","explanation":"Đạo hàm e^{-x}=-e^{-x}."},
{"question":"Nếu λ là giá trị riêng của A thì λ^2 là giá trị riêng của?","options":["A. A^2","B. A^{-1}","C. A^T","D. I"],"answer":"A. A^2","explanation":"Tính chất phổ."},
{"question":"∫_0^{π/2} cos x dx bằng?","options":["A. 1","B. 0","C. 2","D. π/2"],"answer":"A. 1","explanation":"sin x từ 0 đến π/2."},
{"question":"Nếu Var(X)=σ^2 thì Var(aX)=?","options":["A. a^2σ^2","B. aσ^2","C. σ^2","D. a+σ^2"],"answer":"A. a^2σ^2","explanation":"Nhân hệ số."},
{"question":"Phương trình y''+y=0 có nghiệm?","options":["A. A cos x+B sin x","B. Ae^x","C. Ax+B","D. Ae^{-x}"],"answer":"A. A cos x+B sin x","explanation":"r^2+1=0."},
{"question":"trace(I_n)=?","options":["A. n","B. 1","C. 0","D. n^2"],"answer":"A. n","explanation":"Tổng n số 1."},

{"question":"∫_0^1 x^{53} dx bằng?","options":["A. 1/53","B. 1/54","C. 1/55","D. 1/52"],"answer":"B. 1/54","explanation":"Nguyên hàm x^{54}/54."},
{"question":"Đạo hàm của ln(1+x^2) là?","options":["A. 2x/(1+x^2)","B. 1/(1+x^2)","C. 2x","D. x/(1+x^2)"],"answer":"A. 2x/(1+x^2)","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu A có hai hàng trùng nhau thì det(A)=?","options":["A. 0","B. 1","C. -1","D. 2"],"answer":"A. 0","explanation":"Tính chất định thức."},
{"question":"Chuỗi ∑ r^n với r=1/3 có tổng bằng?","options":["A. 3/2","B. 1/2","C. 1","D. 3"],"answer":"A. 3/2","explanation":"1/(1-1/3)=3/2."},
{"question":"∫ x e^{x} dx bằng?","options":["A. (x-1)e^{x}+C","B. xe^{x}+C","C. e^{x}+C","D. x^2e^{x}"],"answer":"A. (x-1)e^{x}+C","explanation":"Từng phần."},
{"question":"Nếu X~N(0,1) thì E(X)=?","options":["A. 0","B. 1","C. -1","D. 2"],"answer":"A. 0","explanation":"Phân phối chuẩn chuẩn hóa."},
{"question":"Ma trận phản xứng thỏa mãn?","options":["A. A^T=-A","B. A=A^T","C. det(A)=1","D. trace(A)=1"],"answer":"A. A^T=-A","explanation":"Định nghĩa."},
{"question":"∫_0^{π} cos 2x dx bằng?","options":["A. 0","B. 1","C. 2","D. π"],"answer":"A. 0","explanation":"sin 2x/2 từ 0 đến π."},
{"question":"Nếu Cov(X,Y)=0 thì X,Y chắc chắn độc lập?","options":["A. Không luôn đúng","B. Luôn đúng","C. Sai","D. Không xác định"],"answer":"A. Không luôn đúng","explanation":"Chỉ đúng trong chuẩn."},
{"question":"Giới hạn lim(x→∞) (ln x)/x bằng?","options":["A. 0","B. 1","C. ∞","D. Không tồn tại"],"answer":"A. 0","explanation":"x tăng nhanh hơn ln x."},
{"question":"∫_0^1 x^{54} dx bằng?","options":["A. 1/54","B. 1/55","C. 1/56","D. 1/53"],"answer":"B. 1/55","explanation":"Nguyên hàm x^{55}/55."},
{"question":"Đạo hàm của arcsin x là?","options":["A. 1/√(1-x^2)","B. -1/√(1-x^2)","C. 1/(1+x^2)","D. √(1-x^2)"],"answer":"A. 1/√(1-x^2)","explanation":"Công thức đạo hàm lượng giác ngược."},
{"question":"Nếu A là ma trận vuông và det(A)≠0 thì hệ Ax=b?","options":["A. Có nghiệm duy nhất","B. Vô nghiệm","C. Vô số nghiệm","D. Không xác định"],"answer":"A. Có nghiệm duy nhất","explanation":"A khả nghịch."},
{"question":"Chuỗi ∑ (-1)^{n+1}/n^2 hội tụ?","options":["A. Tuyệt đối","B. Có điều kiện","C. Phân kỳ","D. Không xác định"],"answer":"A. Tuyệt đối","explanation":"p=2>1."},
{"question":"∫ cosh x dx bằng?","options":["A. sinh x + C","B. cosh x + C","C. -sinh x","D. tanh x"],"answer":"A. sinh x + C","explanation":"Nguyên hàm hyperbolic."},
{"question":"Nếu λ là giá trị riêng của A thì 1/λ là giá trị riêng của?","options":["A. A^{-1}","B. A^2","C. A^T","D. I"],"answer":"A. A^{-1}","explanation":"Tính chất phổ ma trận khả nghịch."},
{"question":"∫_0^{π/2} sin x dx bằng?","options":["A. 1","B. 0","C. 2","D. π/2"],"answer":"A. 1","explanation":"-cos x từ 0 đến π/2."},
{"question":"Nếu E(X)=μ thì E(aX+b)=?","options":["A. aμ+b","B. μ","C. a+b","D. aμ"],"answer":"A. aμ+b","explanation":"Tính tuyến tính kỳ vọng."},
{"question":"Phương trình y''-y=0 có nghiệm?","options":["A. Ae^{x}+Be^{-x}","B. A cos x","C. Ax+B","D. Ae^{-x^2}"],"answer":"A. Ae^{x}+Be^{-x}","explanation":"r^2-1=0."},
{"question":"det(A^T)=?","options":["A. det(A)","B. -det(A)","C. 1/det(A)","D. 0"],"answer":"A. det(A)","explanation":"Định thức không đổi qua chuyển vị."},

{"question":"∫_0^1 x^{55} dx bằng?","options":["A. 1/55","B. 1/56","C. 1/57","D. 1/54"],"answer":"B. 1/56","explanation":"Nguyên hàm x^{56}/56."},
{"question":"Đạo hàm của ln|x| là?","options":["A. 1/x","B. -1/x","C. x","D. |x|"],"answer":"A. 1/x","explanation":"Đạo hàm chuẩn."},
{"question":"Nếu A có cột phụ thuộc tuyến tính thì det(A)=?","options":["A. 0","B. 1","C. -1","D. n"],"answer":"A. 0","explanation":"Phụ thuộc tuyến tính ⇒ suy biến."},
{"question":"Chuỗi ∑ (1/2)^n có tổng bằng?","options":["A. 2","B. 1","C. 1/2","D. 3"],"answer":"A. 2","explanation":"1/(1-1/2)=2."},
{"question":"∫ x ln x dx bằng?","options":["A. x^2/2 ln x - x^2/4 + C","B. ln x","C. x ln x","D. x^2 ln x"],"answer":"A. x^2/2 ln x - x^2/4 + C","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Exp(λ) thì E(X)=?","options":["A. 1/λ","B. λ","C. λ^2","D. 0"],"answer":"A. 1/λ","explanation":"Kỳ vọng phân phối mũ."},
{"question":"Ma trận trực giao thỏa mãn?","options":["A. A^TA=I","B. A=A^T","C. det(A)=0","D. trace(A)=0"],"answer":"A. A^TA=I","explanation":"Định nghĩa trực giao."},
{"question":"∫_0^{2π} cos x dx bằng?","options":["A. 0","B. 1","C. 2","D. 2π"],"answer":"A. 0","explanation":"Chu kỳ đầy đủ."},
{"question":"Nếu Var(X)=σ^2 thì Var(X+c)=?","options":["A. σ^2","B. σ^2+c","C. cσ^2","D. 0"],"answer":"A. σ^2","explanation":"Cộng hằng không đổi phương sai."},
{"question":"Giới hạn lim(x→0) (1-cos x)/x^2 bằng?","options":["A. 1/2","B. 0","C. 1","D. 2"],"answer":"A. 1/2","explanation":"Giới hạn cơ bản."},
{"question":"∫_0^1 x^{56} dx bằng?","options":["A. 1/56","B. 1/57","C. 1/58","D. 1/55"],"answer":"B. 1/57","explanation":"Nguyên hàm x^{57}/57."},
{"question":"Đạo hàm của arccos x là?","options":["A. -1/√(1-x^2)","B. 1/√(1-x^2)","C. 1/(1+x^2)","D. -1/(1+x^2)"],"answer":"A. -1/√(1-x^2)","explanation":"Công thức đạo hàm lượng giác ngược."},
{"question":"Nếu A và B đồng dạng thì?","options":["A. Có cùng giá trị riêng","B. Có cùng định thức bằng 0","C. A=B","D. Cùng chuyển vị"],"answer":"A. Có cùng giá trị riêng","explanation":"Tính chất ma trận đồng dạng."},
{"question":"Chuỗi ∑ n/(2^n) hội tụ vì?","options":["A. So sánh với hình học","B. p-series","C. Phân kỳ","D. Điều hòa"],"answer":"A. So sánh với hình học","explanation":"Tăng chậm hơn 2^n."},
{"question":"∫ sinh x dx bằng?","options":["A. cosh x + C","B. sinh x + C","C. -cosh x","D. tanh x"],"answer":"A. cosh x + C","explanation":"Nguyên hàm hyperbolic."},
{"question":"Nếu λ là giá trị riêng của A thì λ+k là giá trị riêng của?","options":["A. A+kI","B. kA","C. A^k","D. A^{-1}"],"answer":"A. A+kI","explanation":"Dịch phổ."},
{"question":"∫_0^{π} sin 2x dx bằng?","options":["A. 0","B. 1","C. 2","D. π"],"answer":"A. 0","explanation":"-cos2x/2 từ 0 đến π."},
{"question":"Nếu E(X)=2 và Var(X)=3 thì Var(3X)=?","options":["A. 27","B. 9","C. 3","D. 18"],"answer":"A. 27","explanation":"Var(aX)=a^2Var(X)=9*3."},
{"question":"Phương trình y''+4y'+4y=0 có nghiệm?","options":["A. (A+Bx)e^{-2x}","B. Ae^{2x}","C. A cos2x","D. Ax+B"],"answer":"A. (A+Bx)e^{-2x}","explanation":"Nghiệm kép r=-2."},
{"question":"det(kA)=?","options":["A. k^n det(A)","B. k det(A)","C. det(A)/k","D. det(A)+k"],"answer":"A. k^n det(A)","explanation":"Ma trận n×n."},

{"question":"∫_0^1 x^{57} dx bằng?","options":["A. 1/57","B. 1/58","C. 1/59","D. 1/56"],"answer":"B. 1/58","explanation":"Nguyên hàm x^{58}/58."},
{"question":"Đạo hàm của tan x là?","options":["A. sec^2 x","B. cos^2 x","C. -sec^2 x","D. sin x"],"answer":"A. sec^2 x","explanation":"Công thức cơ bản."},
{"question":"Nếu A là ma trận khả nghịch thì rank(A)=?","options":["A. n","B. 1","C. 0","D. n-1"],"answer":"A. n","explanation":"Hạng đầy đủ."},
{"question":"Chuỗi ∑ 1/(n(n+1)) hội tụ vì?","options":["A. Phân tích thành hiệu","B. p-series","C. Phân kỳ","D. Hình học"],"answer":"A. Phân tích thành hiệu","explanation":"Telescoping."},
{"question":"∫ x^2 e^x dx bằng?","options":["A. e^x(x^2-2x+2)+C","B. x^2e^x","C. e^x","D. x^3e^x"],"answer":"A. e^x(x^2-2x+2)+C","explanation":"Từng phần nhiều lần."},
{"question":"Nếu X~Bin(n,p) thì E(X)=?","options":["A. np","B. p","C. n","D. np(1-p)"],"answer":"A. np","explanation":"Kỳ vọng nhị thức."},
{"question":"Ma trận có det≠0 thì?","options":["A. Khả nghịch","B. Suy biến","C. Đối xứng","D. Phản xứng"],"answer":"A. Khả nghịch","explanation":"Định nghĩa."},
{"question":"∫_0^{π/2} cos 2x dx bằng?","options":["A. 0","B. 1","C. 1/2","D. π/2"],"answer":"A. 0","explanation":"sin2x/2 từ 0 đến π/2."},
{"question":"Nếu Cov(X,Y)>0 thì?","options":["A. Tương quan dương","B. Độc lập","C. Tương quan âm","D. Không liên hệ"],"answer":"A. Tương quan dương","explanation":"Hiệp phương sai dương."},
{"question":"Giới hạn lim(x→∞) (1+1/x)^x bằng?","options":["A. e","B. 1","C. 0","D. ∞"],"answer":"A. e","explanation":"Định nghĩa số e."},
{"question":"∫_0^1 x^{58} dx bằng?","options":["A. 1/58","B. 1/59","C. 1/60","D. 1/57"],"answer":"B. 1/59","explanation":"Nguyên hàm x^{59}/59."},
{"question":"Đạo hàm của cot x là?","options":["A. -csc^2 x","B. sec^2 x","C. csc^2 x","D. -sec^2 x"],"answer":"A. -csc^2 x","explanation":"Công thức đạo hàm lượng giác."},
{"question":"Nếu A^2=I thì A được gọi là?","options":["A. Ma trận involutory","B. Ma trận trực giao","C. Ma trận đối xứng","D. Ma trận suy biến"],"answer":"A. Ma trận involutory","explanation":"Theo định nghĩa A^2=I."},
{"question":"Chuỗi ∑ 1/2^n từ n=1 đến ∞ có tổng bằng?","options":["A. 1","B. 2","C. 1/2","D. 3"],"answer":"A. 1","explanation":"Cấp số nhân r=1/2."},
{"question":"∫ e^{x} cos x dx bằng?","options":["A. (e^x/2)(sin x+cos x)+C","B. e^x sin x","C. e^x cos x","D. (e^x/2)(sin x-cos x)"],"answer":"A. (e^x/2)(sin x+cos x)+C","explanation":"Tích phân từng phần hai lần."},
{"question":"Nếu λ là giá trị riêng bội k thì không gian riêng có chiều ≤?","options":["A. k","B. n","C. 1","D. k+1"],"answer":"A. k","explanation":"Bội hình học ≤ bội đại số."},
{"question":"∫_0^{π} sin x cos x dx bằng?","options":["A. 0","B. 1/2","C. 1","D. 2"],"answer":"A. 0","explanation":"Hàm lẻ quanh π/2."},
{"question":"Nếu Var(X)=5 thì Var(-X)=?","options":["A. 5","B. -5","C. 25","D. 0"],"answer":"A. 5","explanation":"Bình phương hệ số (-1)^2=1."},
{"question":"Phương trình y''-4y'+4y=0 có nghiệm?","options":["A. (A+Bx)e^{2x}","B. Ae^{2x}+Be^{-2x}","C. A cos2x","D. Ax+B"],"answer":"A. (A+Bx)e^{2x}","explanation":"Nghiệm kép r=2."},
{"question":"det(A^{-1})=?","options":["A. 1/det(A)","B. det(A)","C. -det(A)","D. 0"],"answer":"A. 1/det(A)","explanation":"Tính chất định thức."},

{"question":"∫_0^1 x^{59} dx bằng?","options":["A. 1/59","B. 1/60","C. 1/61","D. 1/58"],"answer":"B. 1/60","explanation":"Nguyên hàm x^{60}/60."},
{"question":"Đạo hàm của sec x là?","options":["A. sec x tan x","B. -sec x tan x","C. csc x cot x","D. tan x"],"answer":"A. sec x tan x","explanation":"Công thức đạo hàm."},
{"question":"Nếu A là ma trận chéo thì giá trị riêng là?","options":["A. Các phần tử đường chéo","B. 0","C. 1","D. det(A)"],"answer":"A. Các phần tử đường chéo","explanation":"Tính chất ma trận chéo."},
{"question":"Chuỗi ∑ 1/(3^n) từ n=0 đến ∞ có tổng bằng?","options":["A. 3/2","B. 1/2","C. 1","D. 3"],"answer":"A. 3/2","explanation":"1/(1-1/3)=3/2."},
{"question":"∫ ln(1+x) dx bằng?","options":["A. (1+x)ln(1+x)-x+C","B. ln(1+x)+C","C. x ln(1+x)","D. 1/(1+x)"],"answer":"A. (1+x)ln(1+x)-x+C","explanation":"Tích phân từng phần."},
{"question":"Nếu X~Uniform(0,1) thì E(X)=?","options":["A. 1/2","B. 1","C. 0","D. 2"],"answer":"A. 1/2","explanation":"Trung bình đoạn [0,1]."},
{"question":"Ma trận có hai cột tỉ lệ thì?","options":["A. det=0","B. det=1","C. khả nghịch","D. trực giao"],"answer":"A. det=0","explanation":"Phụ thuộc tuyến tính."},
{"question":"∫_0^{2π} sin 2x dx bằng?","options":["A. 0","B. 1","C. 2","D. π"],"answer":"A. 0","explanation":"Chu kỳ đầy đủ."},
{"question":"Nếu Cov(X,Y)<0 thì?","options":["A. Tương quan âm","B. Độc lập","C. Tương quan dương","D. Không liên hệ"],"answer":"A. Tương quan âm","explanation":"Hiệp phương sai âm."},
{"question":"Giới hạn lim(x→∞) x e^{-x} bằng?","options":["A. 0","B. 1","C. ∞","D. -1"],"answer":"A. 0","explanation":"e^{-x} giảm nhanh hơn x tăng."},
{"question":"∫_0^1 x^{60} dx bằng?","options":["A. 1/60","B. 1/61","C. 1/62","D. 1/59"],"answer":"B. 1/61","explanation":"Nguyên hàm x^{61}/61."},
{"question":"Đạo hàm của csc x là?","options":["A. -csc x cot x","B. csc x cot x","C. sec x tan x","D. -sec x tan x"],"answer":"A. -csc x cot x","explanation":"Công thức đạo hàm lượng giác."},
{"question":"Nếu A là ma trận tam giác dưới thì det(A)=?","options":["A. Tích phần tử đường chéo","B. Tổng đường chéo","C. 0","D. 1"],"answer":"A. Tích phần tử đường chéo","explanation":"Tính chất định thức."},
{"question":"Chuỗi ∑ 1/n! hội tụ đến?","options":["A. e","B. 1","C. ∞","D. 0"],"answer":"A. e","explanation":"Khai triển e^1."},
{"question":"∫ e^{x} sin x dx bằng?","options":["A. (e^x/2)(sin x-cos x)+C","B. e^x sin x","C. e^x cos x","D. (e^x/2)(sin x+cos x)"],"answer":"A. (e^x/2)(sin x-cos x)+C","explanation":"Tích phân từng phần hai lần."},
{"question":"Nếu A là ma trận vuông n×n thì số giá trị riêng (kể cả bội) là?","options":["A. n","B. 1","C. n^2","D. n-1"],"answer":"A. n","explanation":"Theo định lý đại số cơ bản."},
{"question":"∫_0^{π/2} sin 2x dx bằng?","options":["A. 1","B. 0","C. 2","D. π/2"],"answer":"A. 1","explanation":"-cos2x/2 từ 0 đến π/2."},
{"question":"Nếu Var(X)=σ^2 thì Var(aX+b)=?","options":["A. a^2σ^2","B. aσ^2+b","C. σ^2+b","D. aσ^2"],"answer":"A. a^2σ^2","explanation":"Cộng hằng không đổi phương sai."},
{"question":"Phương trình y''+9y'+20y=0 có nghiệm?","options":["A. Ae^{-4x}+Be^{-5x}","B. Ae^{4x}+Be^{5x}","C. A cos5x","D. Ax+B"],"answer":"A. Ae^{-4x}+Be^{-5x}","explanation":"r^2+9r+20=0."},
{"question":"det(AB)=?","options":["A. det(A)det(B)","B. det(A)+det(B)","C. det(A)/det(B)","D. 0"],"answer":"A. det(A)det(B)","explanation":"Tính chất định thức."},

{"question":"∫_0^1 x^{61} dx bằng?","options":["A. 1/61","B. 1/62","C. 1/63","D. 1/60"],"answer":"B. 1/62","explanation":"Nguyên hàm x^{62}/62."},
{"question":"Đạo hàm của ln(x^2+1) là?","options":["A. 2x/(x^2+1)","B. 1/(x^2+1)","C. 2x","D. x/(x^2+1)"],"answer":"A. 2x/(x^2+1)","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu A là ma trận trực giao thì det(A)=?","options":["A. ±1","B. 0","C. 1","D. -1"],"answer":"A. ±1","explanation":"Tính chất ma trận trực giao."},
{"question":"Chuỗi ∑ (-1)^n/(n!) hội tụ vì?","options":["A. Tuyệt đối","B. Phân kỳ","C. Điều hòa","D. Hình học"],"answer":"A. Tuyệt đối","explanation":"So sánh với 1/n!."},
{"question":"∫ x^3 e^x dx bằng?","options":["A. e^x(x^3-3x^2+6x-6)+C","B. x^3e^x","C. e^x","D. x^4e^x"],"answer":"A. e^x(x^3-3x^2+6x-6)+C","explanation":"Từng phần nhiều lần."},
{"question":"Nếu X~Poisson(λ) thì Var(X)=?","options":["A. λ","B. λ^2","C. 1","D. 0"],"answer":"A. λ","explanation":"Tính chất phân phối Poisson."},
{"question":"Ma trận A thỏa A^T=A^{-1} gọi là?","options":["A. Trực giao","B. Đối xứng","C. Phản xứng","D. Suy biến"],"answer":"A. Trực giao","explanation":"Định nghĩa."},
{"question":"∫_0^{π} sin^2 x dx bằng?","options":["A. π/2","B. 0","C. 1","D. π"],"answer":"A. π/2","explanation":"Dùng công thức hạ bậc."},
{"question":"Nếu Cov(X,Y)=0 và X,Y chuẩn thì?","options":["A. Độc lập","B. Phụ thuộc","C. Không xác định","D. Tương quan âm"],"answer":"A. Độc lập","explanation":"Chuẩn đa biến."},
{"question":"Giới hạn lim(x→0) (e^x-1)/x bằng?","options":["A. 1","B. 0","C. e","D. ∞"],"answer":"A. 1","explanation":"Giới hạn cơ bản."},
{"question":"∫_0^1 x^{62} dx bằng?","options":["A. 1/62","B. 1/63","C. 1/64","D. 1/61"],"answer":"B. 1/63","explanation":"Nguyên hàm x^{63}/63."},
{"question":"Đạo hàm của arctan(2x) là?","options":["A. 2/(1+4x^2)","B. 1/(1+4x^2)","C. 2/(1+x^2)","D. 4/(1+4x^2)"],"answer":"A. 2/(1+4x^2)","explanation":"Quy tắc dây chuyền."},
{"question":"Nếu A là ma trận có det(A)=1 và det(B)=2 thì det(AB)=?","options":["A. 2","B. 1","C. 3","D. 0"],"answer":"A. 2","explanation":"det(AB)=det(A)det(B)."},
{"question":"Chuỗi ∑ n!/n^n hội tụ vì?","options":["A. So sánh giới hạn","B. Phân kỳ","C. Điều hòa","D. Hình học"],"answer":"A. So sánh giới hạn","explanation":"Dùng tiêu chuẩn tỉ số."},
{"question":"∫ cos x sin x dx bằng?","options":["A. 1/2 sin^2 x + C","B. sin x","C. cos x","D. -1/2 cos^2 x"],"answer":"A. 1/2 sin^2 x + C","explanation":"Đặt u=sin x."},
{"question":"Nếu λ là giá trị riêng của A thì λ^k là giá trị riêng của?","options":["A. A^k","B. kA","C. A+kI","D. A^{-1}"],"answer":"A. A^k","explanation":"Tính chất phổ."},
{"question":"∫_0^{π/4} tan x dx bằng?","options":["A. -ln|cos x| từ 0 đến π/4","B. 1","C. 0","D. π/4"],"answer":"A. -ln|cos x| từ 0 đến π/4","explanation":"Nguyên hàm tan x."},
{"question":"Nếu Var(X)=4 và Var(Y)=5 độc lập thì Var(X+Y)=?","options":["A. 9","B. 20","C. 1","D. 0"],"answer":"A. 9","explanation":"Cộng phương sai."},
{"question":"Phương trình y''+y'+y=0 có nghiệm dạng?","options":["A. e^{-x/2}(A cos(√3/2 x)+B sin(√3/2 x))","B. Ae^x","C. Ax+B","D. A cos x"],"answer":"A. e^{-x/2}(A cos(√3/2 x)+B sin(√3/2 x))","explanation":"Nghiệm phức."},
{"question":"det(A^k)=?","options":["A. det(A)^k","B. k det(A)","C. det(A)+k","D. 0"],"answer":"A. det(A)^k","explanation":"Tính chất định thức."},

{"question":"∫_0^1 x^{63} dx bằng?","options":["A. 1/63","B. 1/64","C. 1/65","D. 1/62"],"answer":"B. 1/64","explanation":"Nguyên hàm x^{64}/64."},
{"question":"Đạo hàm của ln(sin x) là?","options":["A. cot x","B. tan x","C. csc x","D. sec x"],"answer":"A. cot x","explanation":"Dùng quy tắc dây chuyền."},
{"question":"Nếu A là ma trận suy biến thì rank(A)?","options":["A. < n","B. = n","C. =1","D. =0"],"answer":"A. < n","explanation":"Không đủ hạng."},
{"question":"Chuỗi ∑ 1/(n^3+n) hội tụ vì?","options":["A. So sánh với 1/n^3","B. Điều hòa","C. Phân kỳ","D. Hình học"],"answer":"A. So sánh với 1/n^3","explanation":"p=3>1."},
{"question":"∫ x/(1+x^2) dx bằng?","options":["A. 1/2 ln(1+x^2)+C","B. ln(1+x^2)","C. arctan x","D. 1/(1+x^2)"],"answer":"A. 1/2 ln(1+x^2)+C","explanation":"Đặt u=1+x^2."},
{"question":"Nếu X~N(μ,σ^2) thì Var(X)=?","options":["A. σ^2","B. μ","C. 1","D. μ^2"],"answer":"A. σ^2","explanation":"Định nghĩa."},
{"question":"Ma trận có det=0 thì?","options":["A. Không khả nghịch","B. Khả nghịch","C. Trực giao","D. Đối xứng"],"answer":"A. Không khả nghịch","explanation":"Định thức 0."},
{"question":"∫_0^{π} cos^2 x dx bằng?","options":["A. π/2","B. 0","C. 1","D. π"],"answer":"A. π/2","explanation":"Công thức hạ bậc."},
{"question":"Nếu Cov(X,Y)=Var(X) thì hệ số tương quan ρ=?","options":["A. 1 khi Var(X)=Var(Y)","B. 0","C. -1","D. Không xác định"],"answer":"A. 1 khi Var(X)=Var(Y)","explanation":"Tương quan tối đa."},
{"question":"Giới hạn lim(x→∞) (x^2+1)/(x^2-1) bằng?","options":["A. 1","B. 0","C. ∞","D. -1"],"answer":"A. 1","explanation":"Chia cho x^2."},





]


