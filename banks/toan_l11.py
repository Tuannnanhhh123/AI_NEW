QUESTIONS = [
    {
        "question": "Đổi số đo của góc $\\alpha = 150^\\circ$ sang đơn vị radian.",
        "options": ["5π/6", "π/6", "3π/4", "2π/3"],
        "answer": "5π/6",
        "explanation": "Công thức đổi: $\\alpha(rad) = \\alpha(deg) \\times \\frac{\\pi}{180}$. Vậy $150 \\times \\frac{\\pi}{180} = \\frac{5\\pi}{6}$."
    },
    {
        "question": "Hàm số nào sau đây là hàm số chẵn?",
        "options": ["y = \\sin x", "y = \\cos x", "y = \\tan x", "y = \\cot x"],
        "answer": "y = \\cos x",
        "explanation": "Hàm số $y = \\cos x$ thỏa mãn $\\cos(-x) = \\cos x$ nên là hàm số chẵn."
    },
    {
        "question": "Tìm tập giá trị T của hàm số $y = 3\\sin(2x) - 1$.",
        "options": ["T = [-1; 1]", "T = [-4; 2]", "T = [-3; 3]", "T = [-2; 4]"],
        "answer": "T = [-4; 2]",
        "explanation": "Vì $-1 \\le \\sin(2x) \\le 1 \\Rightarrow -3 \\le 3\\sin(2x) \\le 3 \\Rightarrow -4 \\le 3\\sin(2x) - 1 \\le 2$."
    },
    {
        "question": "Giải phương trình $\\cos x = \\cos(\\pi/3)$.",
        "options": ["x = ±π/3 + k2π", "x = π/3 + k2π", "x = ±π/3 + kπ", "x = π/3 + kπ"],
        "answer": "x = ±π/3 + k2π",
        "explanation": "Phương trình lượng giác cơ bản: $\\cos x = \\cos \\alpha \\Leftrightarrow x = \\pm \\alpha + k2\\pi$."
    },
    {
        "question": "Cho dãy số $(u_n)$ với $u_n = 2n - 1$. Số hạng $u_{10}$ là:",
        "options": ["10", "19", "21", "20"],
        "answer": "19",
        "explanation": "Thay $n = 10$ vào công thức: $u_{10} = 2(10) - 1 = 19$."
    },
    {
        "question": "Trong các dãy số sau, dãy số nào là cấp số cộng?",
        "options": ["1, 2, 4, 8", "1, 3, 5, 7", "1, 1, 2, 3", "0, 1, 0, 1"],
        "answer": "1, 3, 5, 7",
        "explanation": "Dãy 1, 3, 5, 7 có hiệu giữa hai số liên tiếp không đổi $d = 2$."
    },
    {
        "question": "Tìm công sai $d$ của cấp số cộng $(u_n)$ biết $u_1 = 3$ và $u_2 = 10$.",
        "options": ["d = 7", "d = -7", "d = 13", "d = 3.3"],
        "answer": "d = 7",
        "explanation": "$d = u_2 - u_1 = 10 - 3 = 7$."
    },
    {
        "question": "Tính tổng 10 số hạng đầu của cấp số cộng có $u_1 = 1, d = 2$.",
        "options": ["100", "110", "90", "120"],
        "answer": "100",
        "explanation": "$S_{10} = \\frac{10}{2}[2(1) + (10-1)2] = 5[2 + 18] = 100$."
    },
    {
        "question": "Cho cấp số nhân có $u_1 = -2$ và công bội $q = -3$. Số hạng thứ hai là:",
        "options": ["6", "-6", "-5", "1"],
        "answer": "6",
        "explanation": "$u_2 = u_1 \\cdot q = (-2) \\cdot (-3) = 6$."
    },
    {
        "question": "Giới hạn của dãy số $u_n = 1/n$ khi $n \\to +\\infty$ là:",
        "options": ["1", "0", "+\\infty", "Không tồn tại"],
        "answer": "0",
        "explanation": "Giới hạn cơ bản $\\lim \\frac{1}{n^k} = 0$ với $k > 0$."
    },
    {
        "question": "Tính $L = \\lim \\frac{3n^2 + n}{n^2 - 2}$.",
        "options": ["L = 0", "L = 3", "L = 1", "L = -1/2"],
        "answer": "L = 3",
        "explanation": "Chia cả tử và mẫu cho $n^2$, giới hạn bằng hệ số bậc cao nhất: $3/1 = 3$."
    },
    {
        "question": "Giá trị của $\\lim_{x \\to 2} (x^2 - 4)$ là:",
        "options": ["0", "4", "2", "8"],
        "answer": "0",
        "explanation": "Thay trực tiếp $x = 2$: $2^2 - 4 = 0$."
    },
    {
        "question": "Đạo hàm của hàm số $y = 5x^4$ là:",
        "options": ["20x^3", "5x^3", "20x^4", "x^5"],
        "answer": "20x^3",
        "explanation": "$y' = 5 \\cdot 4x^{4-1} = 20x^3$."
    },
    {
        "question": "Đạo hàm của hàm số $y = \\cos x$ là:",
        "options": ["\\sin x", "-\\sin x", "\\cos x", "1/\\cos x"],
        "answer": "-\\sin x",
        "explanation": "Công thức đạo hàm lượng giác cơ bản."
    },
    {
        "question": "Trong không gian, hai đường thẳng không có điểm chung và nằm trên cùng một mặt phẳng gọi là:",
        "options": ["Song song", "Chéo nhau", "Cắt nhau", "Trùng nhau"],
        "answer": "Song song",
        "explanation": "Định nghĩa hai đường thẳng song song trong không gian."
    },
    {
        "question": "Hình chóp tam giác có bao nhiêu mặt?",
        "options": ["3", "4", "5", "6"],
        "answer": "4",
        "explanation": "Gồm 1 mặt đáy và 3 mặt bên."
    },
    {
        "question": "Cho hàm số $f(x)$ có đạo hàm tại $x_0$. Hệ số góc của tiếp tuyến tại điểm $M(x_0; f(x_0))$ là:",
        "options": ["f(x_0)", "f'(x_0)", "-f'(x_0)", "1/f'(x_0)"],
        "answer": "f'(x_0)",
        "explanation": "Ý nghĩa hình học của đạo hàm: $k = f'(x_0)$."
    },
    {
        "question": "Tính đạo hàm của $y = \\sqrt{x}$ tại $x = 4$.",
        "options": ["1/2", "1/4", "2", "4"],
        "answer": "1/4",
        "explanation": "$y' = \\frac{1}{2\\sqrt{x}}$. Tại $x=4$, $y'(4) = \\frac{1}{2\\sqrt{4}} = \\frac{1}{4}$."
    },
    {
        "question": "Một đường thẳng d vuông góc với mặt phẳng (P) thì d vuông góc với:",
        "options": ["Mọi đường thẳng trong (P)", "Duy nhất 1 đường thẳng trong (P)", "Đường thẳng song song với d", "Không vuông góc với đường nào"],
        "answer": "Mọi đường thẳng trong (P)",
        "explanation": "Định nghĩa đường thẳng vuông góc với mặt phẳng."
    },
    {
        "question": "Số cách chọn 2 học sinh từ 10 học sinh là:",
        "options": ["C(10,2)", "A(10,2)", "10^2", "20"],
        "answer": "C(10,2)",
        "explanation": "Chọn không tính thứ tự dùng tổ hợp $C_n^k$."
    },
    {
        "question": "Phương trình $\\tan x = 1$ có nghiệm là:",
        "options": ["x = π/4 + kπ", "x = π/4 + k2π", "x = π/2 + kπ", "x = kπ"],
        "answer": "x = π/4 + kπ",
        "explanation": "$\\tan x = \\tan(\\pi/4) \\Leftrightarrow x = \\pi/4 + k\\pi$."
    },
    {
        "question": "Hàm số $y = \\frac{x+1}{x-1}$ gián đoạn tại điểm nào?",
        "options": ["x = 0", "x = -1", "x = 1", "x = 2"],
        "answer": "x = 1",
        "explanation": "Hàm số không xác định tại mẫu số bằng 0 $\\Rightarrow x-1=0 \\Leftrightarrow x=1$."
    },
    {
        "question": "Tính đạo hàm của hàm số $y = x^2 - 3x + 2$.",
        "options": ["2x - 3", "x - 3", "2x + 2", "2x"],
        "answer": "2x - 3",
        "explanation": "$(x^2)' - (3x)' + (2)' = 2x - 3$."
    },
    {
        "question": "Trong không gian, hai đường thẳng chéo nhau khi:",
        "options": ["Chúng không có điểm chung và không đồng phẳng", "Chúng không có điểm chung và đồng phẳng", "Chúng cắt nhau", "Chúng song song"],
        "answer": "Chúng không có điểm chung và không đồng phẳng",
        "explanation": "Định nghĩa hai đường thẳng chéo nhau."
    },
    {
        "question": "Cho hình chóp S.ABCD có đáy là hình vuông. Đường thẳng nào vuông góc với mặt đáy?",
        "options": ["AB", "BC", "Nếu SA vuông góc đáy thì là SA", "AC"],
        "answer": "Nếu SA vuông góc đáy thì là SA",
        "explanation": "Trong các bài toán hình chóp điển hình, cạnh bên SA thường được cho vuông góc với đáy."
    },
    {
        "question": "$\\lim_{x \\to +\\infty} \\frac{1-x^2}{x^2+1}$ bằng:",
        "options": ["1", "-1", "0", "+\\infty"],
        "answer": "-1",
        "explanation": "Tỉ số hệ số bậc cao nhất là $-1/1 = -1$."
    },
    {
        "question": "Chu kỳ tuần hoàn của hàm số $y = \\sin x$ là:",
        "options": ["π", "2π", "π/2", "k2π"],
        "answer": "2π",
        "explanation": "Hàm số $\\sin$ và $\\cos$ tuần hoàn với chu kỳ $2\\pi$."
    },
    {
        "question": "Đạo hàm của hàm số $y = x \\cdot \\sin x$ là:",
        "options": ["\\cos x", "\\sin x + x\\cos x", "\\sin x - x\\cos x", "x\\cos x"],
        "answer": "\\sin x + x\\cos x",
        "explanation": "Sử dụng quy tắc $(uv)' = u'v + uv'$."
    },
    {
        "question": "Góc giữa hai đường thẳng song song bằng:",
        "options": ["0°", "90°", "180°", "45°"],
        "answer": "0°",
        "explanation": "Theo quy ước góc giữa hai đường thẳng song song hoặc trùng nhau bằng $0^\\circ$."
    },
    {
        "question": "Công thức tính số hạng tổng quát của cấp số cộng là:",
        "options": ["u_n = u_1 + (n-1)d", "u_n = u_1 + nd", "u_n = u_1 \\cdot d^{n-1}", "u_n = u_1 - (n-1)d"],
        "answer": "u_n = u_1 + (n-1)d",
        "explanation": "Đây là công thức chuẩn trong SGK."
    },
    {
        "question": "Giá trị của $\\lim_{x \\to 1^+} \\frac{1}{x-1}$ là:",
        "options": ["0", "+\\infty", "-\\infty", "1"],
        "answer": "+\\infty",
        "explanation": "Khi $x \\to 1^+$, $x-1 > 0$ và tiến về $0$, nên phân thức tiến về $+\\infty$."
    },
    {
        "question": "Đạo hàm của hàm số $y = 1/x$ là:",
        "options": ["1/x^2", "-1/x^2", "\\ln x", "-1/x"],
        "answer": "-1/x^2",
        "explanation": "Công thức đạo hàm $(1/x)' = -1/x^2$."
    },
    {
        "question": "Trong các mệnh đề sau, mệnh đề nào sai?",
        "options": [
            "Hình lăng trụ đứng có các cạnh bên vuông góc với đáy",
            "Hình lăng trụ có các mặt bên là hình bình hành",
            "Hình chóp đều có đáy là đa giác đều",
            "Hình lăng trụ có tất cả các cạnh bằng nhau"
        ],
        "answer": "Hình lăng trụ có tất cả các cạnh bằng nhau",
        "explanation": "Lăng trụ chỉ yêu cầu các cạnh bên bằng nhau và các mặt bên là hình bình hành, không bắt buộc cạnh đáy bằng cạnh bên."
    },
    {
        "question": "Cho $\\sin \\alpha = 3/5$ với $\\pi/2 < \\alpha < \\pi$. Tính $\\cos \\alpha$.",
        "options": ["4/5", "-4/5", "16/25", "-16/25"],
        "answer": "-4/5",
        "explanation": "$\\cos^2 \\alpha = 1 - (3/5)^2 = 16/25$. Vì $\\alpha$ ở góc phần tư thứ II nên $\\cos \\alpha < 0 \\Rightarrow -4/5$."
    },
    {
        "question": "Tính đạo hàm của $y = \\tan x$.",
        "options": ["1/\\cos^2 x", "1/\\sin^2 x", "-\\tan x", "1 + \\sin^2 x"],
        "answer": "1/\\cos^2 x",
        "explanation": "Đạo hàm cơ bản $(\\tan x)' = \\frac{1}{\\cos^2 x} = 1 + \\tan^2 x$."
    },
    {
        "question": "Góc giữa hai mặt phẳng vuông góc với nhau bằng:",
        "options": ["0°", "45°", "90°", "180°"],
        "answer": "90°",
        "explanation": "Định nghĩa hai mặt phẳng vuông góc."
    },
    {
        "question": "Tính $\\lim (\\sqrt{n^2+1} - n)$.",
        "options": ["0", "1", "+\\infty", "1/2"],
        "answer": "0",
        "explanation": "Nhân liên hợp: $\\frac{1}{\\sqrt{n^2+1} + n} \\to 0$ khi $n \\to \\infty$."
    },
    {
        "question": "Hàm số $y = \\sin x$ đồng biến trên khoảng nào?",
        "options": ["(0; π)", "(-π/2; π/2)", "(π/2; 3π/2)", "(0; 2π)"],
        "answer": "(-π/2; π/2)",
        "explanation": "Trên nửa đường tròn bên phải, giá trị $\\sin$ tăng dần từ $-1$ đến $1$."
    },
    {
        "question": "Số hạng tổng quát của cấp số nhân là:",
        "options": ["u_n = u_1 \\cdot q^{n-1}", "u_n = u_1 + (n-1)q", "u_n = u_1 \\cdot q^n", "u_n = u_1 / q^{n-1}"],
        "answer": "u_n = u_1 \\cdot q^{n-1}",
        "explanation": "Công thức chuẩn SGK cho cấp số nhân."
    },
    {
        "question": "Đạo hàm của $y = e^x$ là:",
        "options": ["e^x", "x \\cdot e^{x-1}", "1/e^x", "e^x \\ln e"],
        "answer": "e^x",
        "explanation": "Hàm số mũ cơ số $e$ có đạo hàm là chính nó."
    },
    {
        "question": "Khoảng cách giữa hai đường thẳng song song là:",
        "options": [
            "Khoảng cách từ một điểm bất kỳ trên đường này tới đường kia",
            "Độ dài một đoạn thẳng nối hai đường",
            "Bằng 0",
            "Vô số"
        ],
        "answer": "Khoảng cách từ một điểm bất kỳ trên đường này tới đường kia",
        "explanation": "Định nghĩa khoảng cách giữa hai thực thể song song."
    },
    {
        "question": "$\\lim_{x \\to 0} \\frac{\\sin x}{x}$ bằng:",
        "options": ["0", "1", "+\\infty", "Không tồn tại"],
        "answer": "1",
        "explanation": "Đây là giới hạn đặc biệt quan trọng trong giải tích."
    },
    {
        "question": "Cho tứ diện ABCD. Có bao nhiêu cặp đường thẳng chéo nhau?",
        "options": ["2", "3", "4", "6"],
        "answer": "3",
        "explanation": "Các cặp cạnh đối: (AB, CD), (AC, BD), (AD, BC)."
    },
    {
        "question": "Hàm số $y = x^2$ đạt giá trị nhỏ nhất tại:",
        "options": ["x = 0", "x = 1", "x = -1", "Không có"],
        "answer": "x = 0",
        "explanation": "Vì $x^2 \\ge 0$ với mọi $x$, dấu '=' xảy ra khi $x = 0$."
    },
    {
        "question": "Đạo hàm của hàm số $y = \\ln x$ là:",
        "options": ["1/x", "e^x", "1/x^2", "x"],
        "answer": "1/x",
        "explanation": "Công thức đạo hàm hàm logarit tự nhiên."
    },
    {
        "question": "Trong một cấp số cộng, nếu biết $u_1$ và $u_3$, công sai $d$ được tính bởi:",
        "options": ["d = u_3 - u_1", "d = (u_3 - u_1)/2", "d = u_3 + u_1", "d = \\sqrt{u_1 u_3}"],
        "answer": "d = (u_3 - u_1)/2",
        "explanation": "$u_3 = u_1 + 2d \\Rightarrow 2d = u_3 - u_1$."
    },
    {
        "question": "Phép chiếu song song biến hai đường thẳng song song thành:",
        "options": ["Hai đường thẳng song song hoặc trùng nhau", "Hai đường thẳng cắt nhau", "Hai đường thẳng chéo nhau", "Một điểm"],
        "answer": "Hai đường thẳng song song hoặc trùng nhau",
        "explanation": "Tính chất của phép chiếu song song."
    },
    {
        "question": "Vi phân của hàm số $y = f(x)$ là:",
        "options": ["dy = f'(x)dx", "dy = f'(x)", "dy = dx", "dy = f(x)dx"],
        "answer": "dy = f'(x)dx",
        "explanation": "Định nghĩa vi phân trong toán học lớp 11."
    },
    {
        "question": "Nghiệm của phương trình $\\sin x = 0$ là:",
        "options": ["x = kπ", "x = π/2 + kπ", "x = k2π", "x = π + k2π"],
        "answer": "x = kπ",
        "explanation": "Các điểm nằm trên trục hoành của đường tròn lượng giác."
    },
    {
        "question": "Một mặt phẳng hoàn toàn được xác định khi biết:",
        "options": [
            "Một điểm và một đường thẳng",
            "Ba điểm không thẳng hàng",
            "Hai đường thẳng chéo nhau",
            "Ba điểm bất kỳ"
        ],
        "answer": "Ba điểm không thẳng hàng",
        "explanation": "Cách cơ bản nhất để xác định mặt phẳng."
    },
    {
            "question": "Giá trị của sin(π/6) bằng:",
            "options": ["1/2", "√2/2", "√3/2", "1"],
            "answer": "1/2",
            "explanation": "sin(30°) = sin(π/6) = 1/2 là giá trị đặc biệt cần nhớ."
        },
        {
            "question": "Giá trị của cos(π/3) bằng:",
            "options": ["1/2", "√2/2", "√3/2", "1"],
            "answer": "1/2",
            "explanation": "cos(60°) = cos(π/3) = 1/2."
        },
        {
            "question": "Giá trị của tan(π/4) bằng:",
            "options": ["1", "√2", "√3", "1/2"],
            "answer": "1",
            "explanation": "tan(45°) = tan(π/4) = 1."
        },
        {
            "question": "Giá trị của sin(π/2) bằng:",
            "options": ["0", "1/2", "√3/2", "1"],
            "answer": "1",
            "explanation": "sin(90°) = sin(π/2) = 1."
        },
        {
            "question": "Công thức sin²x + cos²x bằng:",
            "options": ["0", "1", "2", "sin(2x)"],
            "answer": "1",
            "explanation": "Đây là đẳng thức lượng giác cơ bản nhất: sin²x + cos²x = 1 với mọi x."
        },
        {
            "question": "Công thức 1 + tan²x bằng:",
            "options": ["1/cos²x", "sin²x", "cos²x", "tan²x"],
            "answer": "1/cos²x",
            "explanation": "1 + tan²x = 1/cos²x (với cos x ≠ 0)."
        },
        {
            "question": "Công thức 1 + cot²x bằng:",
            "options": ["1/sin²x", "cos²x", "sin²x", "cot²x"],
            "answer": "1/sin²x",
            "explanation": "1 + cot²x = 1/sin²x (với sin x ≠ 0)."
        },
        {
            "question": "Công thức sin(2x) bằng:",
            "options": ["2sin(x)cos(x)", "sin²x - cos²x", "2sin(x)", "2cos(x)"],
            "answer": "2sin(x)cos(x)",
            "explanation": "Công thức nhân đôi: sin(2x) = 2sin(x)cos(x)."
        },
        {
            "question": "Công thức cos(2x) bằng:",
            "options": ["cos²x - sin²x", "2cos(x)", "sin²x + cos²x", "2sin(x)cos(x)"],
            "answer": "cos²x - sin²x",
            "explanation": "cos(2x) = cos²x - sin²x = 2cos²x - 1 = 1 - 2sin²x."
        },
        {
            "question": "Công thức tan(2x) bằng:",
            "options": ["2tan(x)/(1 - tan²x)", "2tan(x)", "tan²x - 1", "1/tan(x)"],
            "answer": "2tan(x)/(1 - tan²x)",
            "explanation": "Công thức nhân đôi tan: tan(2x) = 2tan(x)/(1 - tan²x)."
        },
        {
            "question": "Phương trình sin(x) = 0 có nghiệm là:",
            "options": ["x = kπ (k ∈ ℤ)", "x = π/2 + kπ (k ∈ ℤ)", "x = π/4 + kπ (k ∈ ℤ)", "x = 2kπ (k ∈ ℤ)"],
            "answer": "x = kπ (k ∈ ℤ)",
            "explanation": "sin(x) = 0 ⟺ x = kπ với k nguyên."
        },
        {
            "question": "Phương trình cos(x) = 0 có nghiệm là:",
            "options": ["x = π/2 + kπ (k ∈ ℤ)", "x = kπ (k ∈ ℤ)", "x = 2kπ (k ∈ ℤ)", "x = π/4 + kπ (k ∈ ℤ)"],
            "answer": "x = π/2 + kπ (k ∈ ℤ)",
            "explanation": "cos(x) = 0 ⟺ x = π/2 + kπ với k nguyên."
        },
        {
            "question": "Phương trình sin(x) = 1 có nghiệm là:",
            "options": ["x = π/2 + k2π (k ∈ ℤ)", "x = kπ (k ∈ ℤ)", "x = 2kπ (k ∈ ℤ)", "x = π + k2π (k ∈ ℤ)"],
            "answer": "x = π/2 + k2π (k ∈ ℤ)",
            "explanation": "sin(x) = 1 ⟺ x = π/2 + k2π."
        },
        {
            "question": "Phương trình cos(x) = 1 có nghiệm là:",
            "options": ["x = k2π (k ∈ ℤ)", "x = π/2 + k2π (k ∈ ℤ)", "x = π + k2π (k ∈ ℤ)", "x = kπ (k ∈ ℤ)"],
            "answer": "x = k2π (k ∈ ℤ)",
            "explanation": "cos(x) = 1 ⟺ x = k2π."
        },
        {
            "question": "Phương trình sin(x) = 1/2 có nghiệm là:",
            "options": ["x = π/6 + k2π hoặc x = 5π/6 + k2π", "x = π/3 + k2π", "x = π/4 + k2π", "x = π/2 + k2π"],
            "answer": "x = π/6 + k2π hoặc x = 5π/6 + k2π",
            "explanation": "sin(x) = 1/2 ⟺ x = π/6 + k2π hoặc x = π - π/6 + k2π = 5π/6 + k2π."
        },
        {
            "question": "Phương trình cos(x) = √3/2 có nghiệm là:",
            "options": ["x = ±π/6 + k2π (k ∈ ℤ)", "x = π/3 + k2π", "x = π/4 + k2π", "x = π/2 + k2π"],
            "answer": "x = ±π/6 + k2π (k ∈ ℤ)",
            "explanation": "cos(x) = √3/2 ⟺ x = ±π/6 + k2π."
        },
        {
            "question": "Phương trình tan(x) = 1 có nghiệm là:",
            "options": ["x = π/4 + kπ (k ∈ ℤ)", "x = π/3 + kπ", "x = π/6 + kπ", "x = π/2 + kπ"],
            "answer": "x = π/4 + kπ (k ∈ ℤ)",
            "explanation": "tan(x) = 1 ⟺ x = π/4 + kπ."
        },
        {
            "question": "Phương trình cot(x) = √3 có nghiệm là:",
            "options": ["x = π/6 + kπ (k ∈ ℤ)", "x = π/3 + kπ", "x = π/4 + kπ", "x = π/2 + kπ"],
            "answer": "x = π/6 + kπ (k ∈ ℤ)",
            "explanation": "cot(x) = √3 ⟺ tan(x) = 1/√3 ⟺ x = π/6 + kπ."
        },
        {
            "question": "Điều kiện để phương trình sin(x) = m có nghiệm là:",
            "options": ["-1 ≤ m ≤ 1", "m > 0", "m < 1", "Mọi m"],
            "answer": "-1 ≤ m ≤ 1",
            "explanation": "Vì -1 ≤ sin(x) ≤ 1 với mọi x nên cần -1 ≤ m ≤ 1."
        },
        {
            "question": "Phương trình sin(2x) = 0 có nghiệm là:",
            "options": ["x = kπ/2 (k ∈ ℤ)", "x = kπ (k ∈ ℤ)", "x = k2π (k ∈ ℤ)", "x = π/2 + kπ"],
            "answer": "x = kπ/2 (k ∈ ℤ)",
            "explanation": "sin(2x) = 0 ⟺ 2x = kπ ⟺ x = kπ/2."
        },
        {
            "question": "Tập xác định của hàm số y = sin(x) là:",
            "options": ["ℝ", "ℝ \\ {π/2 + kπ}", "ℝ \\ {kπ}", "(-1, 1)"],
            "answer": "ℝ",
            "explanation": "Hàm sin xác định với mọi số thực."
        },
        {
            "question": "Tập giá trị của hàm số y = cos(x) là:",
            "options": ["[-1, 1]", "ℝ", "(0, 1)", "[-∞, +∞]"],
            "answer": "[-1, 1]",
            "explanation": "Với mọi x: -1 ≤ cos(x) ≤ 1."
        },
        {
            "question": "Chu kỳ của hàm số y = sin(x) là:",
            "options": ["2π", "π", "π/2", "4π"],
            "answer": "2π",
            "explanation": "sin(x + 2π) = sin(x) với mọi x, và 2π là chu kỳ nhỏ nhất."
        },
        {
            "question": "Chu kỳ của hàm số y = tan(x) là:",
            "options": ["π", "2π", "π/2", "4π"],
            "answer": "π",
            "explanation": "tan(x + π) = tan(x) với mọi x thuộc TXĐ."
        },
        {
            "question": "Tập xác định của hàm số y = tan(x) là:",
            "options": ["ℝ \\ {π/2 + kπ, k ∈ ℤ}", "ℝ", "ℝ \\ {kπ}", "(-π/2, π/2)"],
            "answer": "ℝ \\ {π/2 + kπ, k ∈ ℤ}",
            "explanation": "tan(x) = sin(x)/cos(x) không xác định khi cos(x) = 0."
        },
        {
            "question": "Hàm số y = sin(x) đồng biến trên khoảng:",
            "options": ["(-π/2 + k2π, π/2 + k2π)", "(kπ, π + kπ)", "(0, π)", "(-π, 0)"],
            "answer": "(-π/2 + k2π, π/2 + k2π)",
            "explanation": "Hàm sin đồng biến trên [-π/2, π/2] và các khoảng tuần hoàn."
        },
        {
            "question": "Hàm số y = cos(x) nghịch biến trên khoảng:",
            "options": ["(k2π, π + k2π)", "(-π/2 + k2π, π/2 + k2π)", "(0, 2π)", "(-π, π)"],
            "answer": "(k2π, π + k2π)",
            "explanation": "Hàm cos nghịch biến trên [0, π] và các khoảng tuần hoàn."
        },
        {
            "question": "Chu kỳ của hàm số y = sin(2x) là:",
            "options": ["π", "2π", "π/2", "4π"],
            "answer": "π",
            "explanation": "Chu kỳ của sin(ax) là 2π/|a|. Với a = 2 thì T = 2π/2 = π."
        },
        {
            "question": "Tập giá trị của hàm số y = 3sin(x) + 2 là:",
            "options": ["[-1, 5]", "[-3, 3]", "[0, 4]", "[-5, 1]"],
            "answer": "[-1, 5]",
            "explanation": "Vì -1 ≤ sin(x) ≤ 1 nên -3 ≤ 3sin(x) ≤ 3, suy ra -1 ≤ 3sin(x) + 2 ≤ 5."
        },
        {
            "question": "Đồ thị hàm số y = sin(x) đối xứng qua:",
            "options": ["Gốc tọa độ O", "Trục Ox", "Trục Oy", "Đường y = x"],
            "answer": "Gốc tọa độ O",
            "explanation": "sin(-x) = -sin(x) nên hàm sin là hàm lẻ, đồ thị đối xứng qua O."
        },
    {
            "question": "Cho dãy số (un) với un = 2n + 1. Số hạng u5 bằng:",
            "options": ["11", "9", "13", "15"],
            "answer": "11",
            "explanation": "u5 = 2×5 + 1 = 11."
        },
        {
            "question": "Dãy số (un) được gọi là dãy tăng nếu:",
            "options": ["un+1 > un với mọi n", "un+1 < un với mọi n", "un+1 = un với mọi n", "un+1 ≥ un với mọi n"],
            "answer": "un+1 > un với mọi n",
            "explanation": "Dãy tăng (tăng ngặt) khi mỗi số hạng sau lớn hơn số hạng trước."
        },
        {
            "question": "Dãy số (un) với un = (-1)^n là:",
            "options": ["Dãy bị chặn", "Dãy tăng", "Dãy giảm", "Dãy không bị chặn"],
            "answer": "Dãy bị chặn",
            "explanation": "un chỉ nhận 2 giá trị: 1 và -1, nên -1 ≤ un ≤ 1 (bị chặn)."
        },
        {
            "question": "Cho dãy số (un) với u1 = 1, un+1 = un + 3. Công thức tổng quát của un là:",
            "options": ["un = 3n - 2", "un = 3n + 1", "un = 2n + 1", "un = n + 2"],
            "answer": "un = 3n - 2",
            "explanation": "Dãy số có dạng un = u1 + (n-1)d = 1 + (n-1)×3 = 3n - 2."
        },
        {
            "question": "Dãy số (un) = (1/n) có giới hạn khi n → +∞ là:",
            "options": ["0", "1", "+∞", "Không tồn tại"],
            "answer": "0",
            "explanation": "lim(n→+∞) 1/n = 0."
        },
        {
            "question": "Cho cấp số cộng (un) có u1 = 3, công sai d = 2. Số hạng u10 bằng:",
            "options": ["21", "19", "23", "25"],
            "answer": "21",
            "explanation": "un = u1 + (n-1)d → u10 = 3 + 9×2 = 21."
        },
        {
            "question": "Trong cấp số cộng (un), nếu un+1 - un = d thì d được gọi là:",
            "options": ["Công sai", "Công bội", "Số hạng đầu", "Số hạng tổng quát"],
            "answer": "Công sai",
            "explanation": "Công sai d là hiệu số giữa hai số hạng liên tiếp."
        },
        {
            "question": "Công thức tổng n số hạng đầu của cấp số cộng là:",
            "options": ["Sn = n(u1 + un)/2", "Sn = u1(1 - q^n)/(1 - q)", "Sn = n×u1", "Sn = un - u1"],
            "answer": "Sn = n(u1 + un)/2",
            "explanation": "Sn = n(u1 + un)/2 hoặc Sn = n×[2u1 + (n-1)d]/2."
        },
        {
            "question": "Cho cấp số cộng có u1 = 5, u5 = 17. Công sai d bằng:",
            "options": ["3", "2", "4", "5"],
            "answer": "3",
            "explanation": "u5 = u1 + 4d → 17 = 5 + 4d → d = 3."
        },
        {
            "question": "Ba số x, y, z lập thành cấp số cộng khi:",
            "options": ["y = (x + z)/2", "y = xz", "y = x + z", "y² = xz"],
            "answer": "y = (x + z)/2",
            "explanation": "Số hạng giữa bằng trung bình cộng của hai số hạng hai bên."
        },
        {
            "question": "Cho cấp số nhân (un) có u1 = 2, công bội q = 3. Số hạng u5 bằng:",
            "options": ["162", "81", "243", "54"],
            "answer": "162",
            "explanation": "un = u1 × q^(n-1) → u5 = 2 × 3^4 = 2 × 81 = 162."
        },
        {
            "question": "Trong cấp số nhân (un), nếu un+1/un = q (un ≠ 0) thì q được gọi là:",
            "options": ["Công bội", "Công sai", "Số hạng đầu", "Tỉ số"],
            "answer": "Công bội",
            "explanation": "Công bội q là tỉ số giữa hai số hạng liên tiếp."
        },
        {
            "question": "Công thức tổng n số hạng đầu của cấp số nhân (q ≠ 1) là:",
            "options": ["Sn = u1(1 - q^n)/(1 - q)", "Sn = n(u1 + un)/2", "Sn = n×u1", "Sn = u1 + q^n"],
            "answer": "Sn = u1(1 - q^n)/(1 - q)",
            "explanation": "Với q ≠ 1: Sn = u1(1 - q^n)/(1 - q) = u1(q^n - 1)/(q - 1)."
        },
        {
            "question": "Ba số x, y, z (khác 0) lập thành cấp số nhân khi:",
            "options": ["y² = xz", "y = (x + z)/2", "y = x + z", "y = x/z"],
            "answer": "y² = xz",
            "explanation": "Bình phương số hạng giữa bằng tích hai số hạng hai bên."
        },
        {
            "question": "Cho cấp số nhân có u1 = 3, u4 = 81. Công bội q bằng:",
            "options": ["3", "2", "4", "27"],
            "answer": "3",
            "explanation": "u4 = u1 × q³ → 81 = 3 × q³ → q³ = 27 → q = 3."
        },
        {
            "question": "lim(n→+∞) (1/n) bằng:",
            "options": ["0", "1", "+∞", "Không tồn tại"],
            "answer": "0",
            "explanation": "Khi n → +∞ thì 1/n → 0."
        },
        {
            "question": "lim(n→+∞) n bằng:",
            "options": ["+∞", "0", "1", "Không tồn tại"],
            "answer": "+∞",
            "explanation": "Khi n → +∞ thì n → +∞."
        },
        {
            "question": "lim(n→+∞) q^n với |q| < 1 bằng:",
            "options": ["0", "1", "+∞", "q"],
            "answer": "0",
            "explanation": "Nếu |q| < 1 thì lim q^n = 0."
        },
        {
            "question": "lim(n→+∞) (2n + 1)/(n + 3) bằng:",
            "options": ["2", "1", "0", "+∞"],
            "answer": "2",
            "explanation": "Chia cả tử và mẫu cho n: lim (2 + 1/n)/(1 + 3/n) = 2/1 = 2."
        },
        {
            "question": "lim(n→+∞) (n² + n)/(2n² - 1) bằng:",
            "options": ["1/2", "1", "2", "0"],
            "answer": "1/2",
            "explanation": "Chia cả tử và mẫu cho n²: lim (1 + 1/n)/(2 - 1/n²) = 1/2."
        },
        {
            "question": "lim(n→+∞) (√(n² + 1) - n) bằng:",
            "options": ["0", "1/2", "1", "+∞"],
            "answer": "0",
            "explanation": "Nhân liên hợp: (√(n² + 1) - n)(√(n² + 1) + n)/(√(n² + 1) + n) = 1/(√(n² + 1) + n) → 0."
        },
        {
            "question": "Nếu lim(n→+∞) un = L và lim(n→+∞) vn = M thì lim(n→+∞) (un + vn) bằng:",
            "options": ["L + M", "L - M", "L × M", "L/M"],
            "answer": "L + M",
            "explanation": "Định lý về giới hạn của tổng."
        },
        {
            "question": "Nếu lim(n→+∞) un = L và c là hằng số thì lim(n→+∞) (c×un) bằng:",
            "options": ["c×L", "L + c", "L - c", "L/c"],
            "answer": "c×L",
            "explanation": "Định lý về giới hạn của tích với hằng số."
        },
        {
            "question": "lim(n→+∞) (3n - 1)/(2n + 5) bằng:",
            "options": ["3/2", "1", "0", "-1/5"],
            "answer": "3/2",
            "explanation": "Chia tử và mẫu cho n: lim (3 - 1/n)/(2 + 5/n) = 3/2."
        },
        {
            "question": "lim(n→+∞) (n³ - 2n²)/(n³ + 1) bằng:",
            "options": ["1", "0", "-2", "+∞"],
            "answer": "1",
            "explanation": "Chia tử và mẫu cho n³: lim (1 - 2/n)/(1 + 1/n³) = 1."
        },
        {
            "question": "lim(x→2) (x² - 4)/(x - 2) bằng:",
            "options": ["4", "2", "0", "Không tồn tại"],
            "answer": "4",
            "explanation": "(x² - 4)/(x - 2) = (x - 2)(x + 2)/(x - 2) = x + 2 → lim = 4."
        },
        {
            "question": "lim(x→+∞) (2x + 1)/(x - 3) bằng:",
            "options": ["2", "1", "0", "+∞"],
            "answer": "2",
            "explanation": "Chia tử và mẫu cho x: lim (2 + 1/x)/(1 - 3/x) = 2."
        },
        {
            "question": "lim(x→0) (sin x)/x bằng:",
            "options": ["1", "0", "+∞", "Không tồn tại"],
            "answer": "1",
            "explanation": "Đây là giới hạn đặc biệt quan trọng: lim(x→0) (sin x)/x = 1."
        },
        {
            "question": "lim(x→0) (1 - cos x)/x² bằng:",
            "options": ["1/2", "0", "1", "Không tồn tại"],
            "answer": "1/2",
            "explanation": "Giới hạn đặc biệt: lim(x→0) (1 - cos x)/x² = 1/2."
        },
        {
            "question": "lim(x→+∞) (√(x² + x) - x) bằng:",
            "options": ["1/2", "0", "1", "+∞"],
            "answer": "1/2",
            "explanation": "Nhân liên hợp: lim x/(√(x² + x) + x) = lim 1/(√(1 + 1/x) + 1) = 1/2."
        },
        {
            "question": "Hàm số f(x) liên tục tại x₀ khi:",
            "options": ["lim(x→x₀) f(x) = f(x₀)", "f(x₀) xác định", "lim(x→x₀) f(x) tồn tại", "Tất cả đều đúng"],
            "answer": "lim(x→x₀) f(x) = f(x₀)",
            "explanation": "f liên tục tại x₀ ⟺ lim(x→x₀) f(x) = f(x₀) (cần cả 3 điều kiện: f(x₀) xác định, giới hạn tồn tại và bằng f(x₀))."
        },
        {
            "question": "lim(x→1) (x³ - 1)/(x - 1) bằng:",
            "options": ["3", "1", "0", "Không tồn tại"],
            "answer": "3",
            "explanation": "(x³ - 1)/(x - 1) = (x - 1)(x² + x + 1)/(x - 1) = x² + x + 1 → lim = 3."
        },
        {
            "question": "lim(x→0) (tan x)/x bằng:",
            "options": ["1", "0", "+∞", "Không tồn tại"],
            "answer": "1",
            "explanation": "tan x/x = (sin x)/(x cos x) → lim = 1/1 = 1."
        },
        {
            "question": "lim(x→+∞) (x² + 1)/(x³ - 2) bằng:",
            "options": ["0", "1", "+∞", "Không tồn tại"],
            "answer": "0",
            "explanation": "Bậc tử < bậc mẫu nên giới hạn = 0."
        },
        {
            "question": "lim(x→2⁺) 1/(x - 2) bằng:",
            "options": ["+∞", "-∞", "0", "1"],
            "answer": "+∞",
            "explanation": "Khi x → 2⁺ thì x - 2 → 0⁺ nên 1/(x - 2) → +∞."
        },
        {
            "question": "Đạo hàm của hàm số y = c (c là hằng số) là:",
            "options": ["0", "c", "1", "x"],
            "answer": "0",
            "explanation": "(c)' = 0 với mọi hằng số c."
        },
        {
            "question": "Đạo hàm của hàm số y = x là:",
            "options": ["1", "0", "x", "2x"],
            "answer": "1",
            "explanation": "(x)' = 1."
        },
        {
            "question": "Đạo hàm của hàm số y = x² là:",
            "options": ["2x", "x", "x²", "2"],
            "answer": "2x",
            "explanation": "(x²)' = 2x."
        },
        {
            "question": "Đạo hàm của hàm số y = x^n là:",
            "options": ["n×x^(n-1)", "x^n", "n×x^n", "x^(n-1)"],
            "answer": "n×x^(n-1)",
            "explanation": "(x^n)' = n×x^(n-1)."
        },
        {
            "question": "Đạo hàm của hàm số y = √x là:",
            "options": ["1/(2√x)", "√x", "2√x", "1/√x"],
            "answer": "1/(2√x)",
            "explanation": "(√x)' = (x^(1/2))' = (1/2)×x^(-1/2) = 1/(2√x)."
        },
        {
            "question": "Đạo hàm của hàm số y = 1/x là:",
            "options": ["-1/x²", "1/x²", "-1/x", "1/x"],
            "answer": "-1/x²",
            "explanation": "(1/x)' = (x^(-1))' = -x^(-2) = -1/x²."
        },
        {
            "question": "Nếu y = u + v thì y' bằng:",
            "options": ["u' + v'", "u' - v'", "u'×v'", "u'/v'"],
            "answer": "u' + v'",
            "explanation": "Quy tắc đạo hàm của tổng: (u + v)' = u' + v'."
        },
        {
            "question": "Nếu y = u×v thì y' bằng:",
            "options": ["u'v + uv'", "u' + v'", "u'×v'", "uv"],
            "answer": "u'v + uv'",
            "explanation": "Quy tắc đạo hàm của tích: (uv)' = u'v + uv'."
        },
        {
            "question": "Nếu y = u/v (v ≠ 0) thì y' bằng:",
            "options": ["(u'v - uv')/v²", "u'/v'", "(u' + v')/v", "uv'/(v²)"],
            "answer": "(u'v - uv')/v²",
            "explanation": "Quy tắc đạo hàm của thương: (u/v)' = (u'v - uv')/v²."
        },
        {
            "question": "Đạo hàm của hàm số y = (2x + 1)³ là:",
            "options": ["6(2x + 1)²", "3(2x + 1)²", "(2x + 1)²", "6(2x + 1)"],
            "answer": "6(2x + 1)²",
            "explanation": "Dùng công thức đạo hàm hàm hợp: y' = 3(2x + 1)² × 2 = 6(2x + 1)²."
        }
    ]