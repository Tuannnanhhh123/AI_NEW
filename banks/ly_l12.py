QUESTIONS = [

    {
        "question": "Một bình kín dung tích 20 lít chứa khí lý tưởng ở áp suất 10^5 Pa. Nếu 1/4 lượng khí thoát ra ngoài và nhiệt độ tuyệt đối tăng thêm 20% thì áp suất mới trong bình là:",
        "options": ["0,9.10^5 Pa", "1,2.10^5 Pa", "1,5.10^5 Pa", "0,8.10^5 Pa"],
        "answer": "0,9.10^5 Pa",
        "explanation": "Sử dụng pV = nRT. p2 = (n2/n1)*(T2/T1)*p1 = (3/4)*(1,2)*10^5 = 0,9.10^5 Pa."
    },
    {
        "question": "Cung cấp nhiệt lượng 1,5 J cho một khối khí trong xilanh đặt nằm ngang. Khí nở ra đẩy pittông đi một đoạn 5cm bằng một lực có độ lớn 20N. Độ biến thiên nội năng của khối khí là:",
        "options": ["0,5 J", "2,5 J", "-0,5 J", "3,5 J"],
        "answer": "0,5 J",
        "explanation": "A = -F.s = -20 * 0,05 = -1 J (khí sinh công). delta_U = Q + A = 1,5 - 1 = 0,5 J."
    },
    {
        "question": "Một lượng khí lí tưởng thực hiện chu trình biến đổi: (1) sang (2) đẳng tích, (2) sang (3) đẳng áp, (3) về (1) đẳng nhiệt. Biết T1 = 300K, p1 = 1 atm, p2 = 3 atm. Thể tích V3 bằng bao nhiêu lần V1?",
        "options": ["3 lần", "1/3 lần", "9 lần", "1,5 lần"],
        "answer": "3 lần",
        "explanation": "Quá trình 1-2 đẳng tích: T2 = T1*(p2/p1) = 900K. Quá trình 2-3 đẳng áp: V3/V2 = T3/T2. Mà T3 = T1 (đẳng nhiệt 3-1) nên V3/V1 = T2/T1 = 3."
    },
    {
        "question": "Tính nhiệt lượng cần cung cấp để làm 200g nước đá ở -10°C nóng chảy hoàn toàn thành nước ở 0°C. Biết c_đá = 2100 J/kg.K, L = 3,34.10^5 J/kg.",
        "options": ["71000 J", "4200 J", "66800 J", "75200 J"],
        "answer": "71000 J",
        "explanation": "Q = m.c.delta_t + m.L = 0,2*2100*10 + 0,2*3,34.10^5 = 4200 + 66800 = 71000 J."
    },
    {
        "question": "Một hạt alpha có động năng 5 MeV bắn vào hạt nhân 14-N đứng yên gây ra phản ứng: alpha + 14-N -> 17-O + p. Biết phản ứng thu năng lượng 1,21 MeV. Tổng động năng của các hạt sau phản ứng là:",
        "options": ["3,79 MeV", "6,21 MeV", "5 MeV", "2,58 MeV"],
        "answer": "3,79 MeV",
        "explanation": "Wđ_sau = Wđ_trước + delta_E = 5 + (-1,21) = 3,79 MeV."
    },
    {
        "question": "Từ thông qua một khung dây biến thiên theo thời gian Phi = 0,02.cos(100.pi.t) Wb. Suất điện động cảm ứng cực đại trong khung có giá trị:",
        "options": ["2.pi V", "0,02 V", "100.pi V", "2 V"],
        "answer": "2.pi V",
        "explanation": "e = -Phi' = 0,02 * 100.pi * sin(100.pi.t). E0 = 2.pi V."
    },
    {
        "question": "Một dây dẫn thẳng dài mang dòng điện I1 đặt trong không khí. Một dây dẫn thứ hai song song với dây thứ nhất cách 10cm mang dòng điện I2 = 2.I1 ngược chiều. Lực từ tác dụng lên mỗi mét chiều dài dây là 4.10^-5 N. Giá trị I1 là:",
        "options": ["sqrt(10) A", "10 A", "3,16 A", "5 A"],
        "answer": "3,16 A",
        "explanation": "F = 2.10^-7 * (I1*I2)/r = 2.10^-7 * 2*I1^2 / 0,1. => 4.10^-5 = 4.10^-6 * I1^2 => I1^2 = 10 => I1 = 3,16 A."
    },
    {
        "question": "Một mẫu phóng xạ sau 15 giờ có độ phóng xạ giảm đi 3 lần. Sau 30 giờ, độ phóng xạ giảm đi bao nhiêu lần so với ban đầu?",
        "options": ["6 lần", "9 lần", "4,5 lần", "12 lần"],
        "answer": "9 lần",
        "explanation": "H = H0 * (1/3)^(t/15). Với t = 30 = 2*15, H = H0 * (1/3)^2 = H0/9."
    },
    {
        "question": "Trong lò phản ứng hạt nhân, các thanh điều khiển chứa Boron (B) hoặc Cadmium (Cd) có tác dụng:",
        "options": ["Làm chậm neutron", "Hấp thụ neutron dư thừa", "Tăng tốc độ phản ứng", "Phát ra neutron"],
        "answer": "Hấp thụ neutron dư thừa",
        "explanation": "Thanh điều khiển dùng để điều chỉnh hệ số nhân neutron k bằng cách hấp thụ neutron để kiểm soát phản ứng dây chuyền."
    },
    {
        "question": "Một proton chuyển động theo quỹ đạo tròn bán kính 5cm trong từ trường đều B = 0,2T. Chu kỳ chuyển động của proton là (m_p = 1,67.10^-27 kg):",
        "options": ["3,28.10^-7 s", "1,64.10^-7 s", "6,56.10^-7 s", "2,15.10^-6 s"],
        "answer": "3,28.10^-7 s",
        "explanation": "T = 2.pi.m / (q.B) = (2 * 3,14 * 1,67.10^-27) / (1,6.10^-19 * 0,2) approx 3,28.10^-7 s."
    },
    {
        "question": "Nội năng của một khối khí lí tưởng đơn nguyên tử tăng thêm 300 J khi được nung nóng đẳng tích. Nhiệt lượng mà khối khí đã nhận là:",
        "options": ["300 J", "500 J", "200 J", "0 J"],
        "answer": "300 J",
        "explanation": "Đẳng tích => A = 0. delta_U = Q = 300 J."
    },
    {
        "question": "Hạt nhân 235-U hấp thụ một neutron chậm và phân hạch thành 95-Mo và 139-La. Phản ứng này phát ra bao nhiêu hạt neutron?",
        "options": ["2 hạt", "3 hạt", "1 hạt", "4 hạt"],
        "answer": "2 hạt",
        "explanation": "Bảo toàn số khối: 235 + 1 = 95 + 139 + k => k = 2."
    },
    {
        "question": "Công thức tính nhiệt lượng hóa hơi Q = L.m. Một bình đun nước ở 100°C có công suất 1000W. Thời gian để 100g nước hóa hơi hoàn toàn là (L = 2,26.10^6 J/kg):",
        "options": ["226 s", "22,6 s", "100 s", "2260 s"],
        "answer": "226 s",
        "explanation": "Q = L.m = 2,26.10^6 * 0,1 = 2,26.10^5 J. t = Q/P = 226 s."
    },
    {
        "question": "Góc lệch của tia sáng khi đi qua lăng kính có góc chiết quang A nhỏ (n=1,5). Nếu tăng góc tới i lên 2 lần thì góc lệch D:",
        "options": ["Tăng 2 lần", "Giảm 2 lần", "Không đổi", "Tăng 4 lần"],
        "answer": "Không đổi",
        "explanation": "Với A nhỏ và i nhỏ, D = (n-1)A. Góc lệch không phụ thuộc vào góc tới i."
    },
    {
        "question": "Để làm tăng độ bền vững của một hạt nhân, ta cần:",
        "options": ["Tăng năng lượng liên kết riêng", "Tăng số lượng proton", "Tăng số khối", "Tăng thể tích hạt nhân"],
        "answer": "Tăng năng lượng liên kết riêng",
        "explanation": "Năng lượng liên kết riêng là đại lượng đặc trưng cho mức độ bền vững của hạt nhân."
    },
    {
        "question": "Một electron bay vào từ trường đều B = 0,1T với vận tốc v = 2.10^6 m/s theo phương hợp với B góc 30 độ. Lực Lorentz có độ lớn:",
        "options": ["1,6.10^-14 N", "3,2.10^-14 N", "1,6.10^-13 N", "0,8.10^-14 N"],
        "answer": "1,6.10^-14 N",
        "explanation": "f = |q|vB.sin(30) = 1,6.10^-19 * 2.10^6 * 0,1 * 0,5 = 1,6.10^-14 N."
    },
    {
        "question": "Xét một khối khí lí tưởng thực hiện quá trình giãn nở đẳng áp. Nếu thể tích tăng 2 lần thì động năng trung bình của các phân tử khí:",
        "options": ["Tăng 2 lần", "Giảm 2 lần", "Không đổi", "Tăng 4 lần"],
        "answer": "Tăng 2 lần",
        "explanation": "Đẳng áp: V/T = hằng số. V tăng 2 => T tăng 2. Động năng trung bình tỉ lệ thuận với T."
    },
    {
        "question": "Trong hiện tượng cảm ứng điện từ, nếu từ thông qua mạch tăng theo quy luật Phi = 2.t (Wb) thì suất điện động cảm ứng trong mạch là:",
        "options": ["-2 V", "2 V", "1 V", "0 V"],
        "answer": "-2 V",
        "explanation": "e = -dPhi/dt = -2 V."
    },
    {
        "question": "Hạt nhân 210-Po phóng xạ alpha tạo thành hạt nhân X. Biết khối lượng m_Po = 209,937u; m_alpha = 4,0015u; m_X = 205,929u. Năng lượng tỏa ra là (1u = 931,5 MeV/c2):",
        "options": ["6,05 MeV", "5,42 MeV", "9,31 MeV", "4,12 MeV"],
        "answer": "6,05 MeV",
        "explanation": "delta_E = (m_trước - m_sau).c2 = (209,937 - 205,929 - 4,0015) * 931,5 approx 6,05 MeV."
    },
    {
        "question": "Một bình khí chứa 2g khí Hydro ở 27°C, áp suất 1 atm. Nếu giữ nguyên áp suất, để thể tích tăng gấp đôi thì nhiệt độ phải là:",
        "options": ["327°C", "54°C", "600°C", "300°C"],
        "answer": "327°C",
        "explanation": "V1/T1 = V2/T2. V2=2V1 => T2 = 2T1 = 2*(27+273) = 600K = 327°C."
    },
    {
        "question": "Hai bình khí lí tưởng cùng thể tích, cùng nhiệt độ. Bình 1 chứa khí Nito, bình 2 chứa khí Oxy. Nếu áp suất bình 1 bằng 2 lần áp suất bình 2 thì tỉ số khối lượng m1/m2 là:",
        "options": ["1,75", "2,0", "0,57", "1,14"],
        "answer": "1,75",
        "explanation": "p = (m/M)*(RT/V). p1/p2 = (m1/M1)/(m2/M2) = 2. => m1/m2 = 2 * (M1/M2) = 2 * (28/32) = 1,75."
    },
    {
        "question": "Độ hụt khối của hạt nhân 2-D (Deuterium) là 0,0024u. Năng lượng liên kết của hạt nhân này là:",
        "options": ["2,235 MeV", "1,117 MeV", "4,47 MeV", "9,31 MeV"],
        "answer": "2,235 MeV",
        "explanation": "Wlk = delta_m * 931,5 = 0,0024 * 931,5 = 2,235 MeV."
    },
    {
        "question": "Tính tốc độ căn quân phương của phân tử khí Oxy ở nhiệt độ 27°C. Biết M = 32 g/mol, R = 8,31 J/mol.K.",
        "options": ["483,4 m/s", "15,3 m/s", "234,5 m/s", "340,2 m/s"],
        "answer": "483,4 m/s",
        "explanation": "v = sqrt(3RT/M) = sqrt(3 * 8,31 * 300 / 0,032) approx 483,4 m/s."
    },
    {
        "question": "Một mạch dao động LC lí tưởng. Nếu tăng điện dung tụ điện lên 4 lần và giảm độ tự cảm ống dây đi 2 lần thì tần số dao động của mạch:",
        "options": ["Giảm sqrt(2) lần", "Tăng sqrt(2) lần", "Giảm 2 lần", "Tăng 2 lần"],
        "answer": "Giảm sqrt(2) lần",
        "explanation": "f = 1 / (2.pi.sqrt(LC)). f' = 1 / (2.pi.sqrt(2L*4C)) = f / sqrt(2)."
    },
    {
        "question": "Phản ứng nhiệt hạch: 2-D + 3-T -> 4-He + n + 17,6 MeV. Biết năng lượng liên kết riêng của D là 1,1 MeV/nucl, của T là 2,8 MeV/nucl. Năng lượng liên kết riêng của He là:",
        "options": ["7,075 MeV/nucl", "28,3 MeV/nucl", "4,4 MeV/nucl", "5,2 MeV/nucl"],
        "answer": "7,075 MeV/nucl",
        "explanation": "delta_E = Wlk(He) - [Wlk(D) + Wlk(T)] => 17,6 = Wlk(He) - [1,1*2 + 2,8*3] => Wlk(He) = 17,6 + 10,6 = 28,2 MeV. Wlkr = 28,2 / 4 = 7,05 MeV/nucl."
    },
    {
        "question": "Lực Lorentz đóng vai trò là lực hướng tâm, hạt điện tích chuyển động tròn đều. Nếu cảm ứng từ B tăng 2 lần và vận tốc v giảm 2 lần thì bán kính quỹ đạo R:",
        "options": ["Giảm 4 lần", "Không đổi", "Tăng 4 lần", "Giảm 2 lần"],
        "answer": "Giảm 4 lần",
        "explanation": "R = mv / (qB). v' = v/2, B' = 2B => R' = R/4."
    },
    {
        "question": "Hệ số công suất của đoạn mạch RLC nối tiếp đạt cực đại khi:",
        "options": ["ZL = ZC", "ZL = R", "ZC = R", "ZL = 2.ZC"],
        "answer": "ZL = ZC",
        "explanation": "Khi cộng hưởng điện ZL = ZC thì cos_phi = R/Z = R/R = 1 (cực đại)."
    },
    {
        "question": "Trong không khí, hằng số điện môi epsilon = 1. Nếu đưa hai điện tích vào trong dầu có epsilon = 2 và giảm khoảng cách đi 2 lần thì lực tương tác giữa chúng:",
        "options": ["Tăng 2 lần", "Giảm 2 lần", "Không đổi", "Tăng 4 lần"],
        "answer": "Tăng 2 lần",
        "explanation": "F = k.q1.q2 / (epsilon.r^2). F' = F * (1/2) * (2^2) = 2F."
    },
    {
        "question": "Máy biến áp lí tưởng có N1 = 1000 vòng, N2 = 200 vòng. Nếu đặt vào hai đầu cuộn sơ cấp điện áp xoay chiều có giá trị hiệu dụng 220V thì điện áp hiệu dụng ở cuộn thứ cấp để hở là:",
        "options": ["44 V", "1100 V", "22 V", "88 V"],
        "answer": "44 V",
        "explanation": "U2 = U1 * (N2/N1) = 220 * (200/1000) = 44 V."
    },
    {
        "question": "Sự phân rã của hạt nhân 238-U thành 206-Pb kèm theo sự phát ra bao nhiêu hạt alpha và beta trừ?",
        "options": ["8 alpha, 6 beta-", "6 alpha, 8 beta-", "4 alpha, 2 beta-", "8 alpha, 8 beta-"],
        "answer": "8 alpha, 6 beta-",
        "explanation": "238 = 206 + 4x => x = 8. 92 = 82 + 2*8 - 1y => y = 6."
    },
    {
        "question": "Một ống dây dài 50cm, có 1000 vòng dây. Dòng điện qua ống dây là 2A. Cảm ứng từ bên trong lòng ống dây là:",
        "options": ["5,03.10^-3 T", "2,51.10^-3 T", "1,25.10^-2 T", "4,00.10^-4 T"],
        "answer": "5,03.10^-3 T",
        "explanation": "B = 4.pi.10^-7 * (N/L) * I = 4 * 3,14.10^-7 * (1000/0,5) * 2 approx 5,03.10^-3 T."
    },
    {
        "question": "Tính nội năng của 1 mol khí Heli ở nhiệt độ 27°C (R = 8,31 J/mol.K, coi Heli là khí lí tưởng đơn nguyên tử):",
        "options": ["3739,5 J", "2493,0 J", "1246,5 J", "6232,5 J"],
        "answer": "3739,5 J",
        "explanation": "U = (3/2)nRT = 1,5 * 1 * 8,31 * 300 = 3739,5 J."
    },
    {
        "question": "Trong máy phát điện xoay chiều một pha, nếu roto có p cặp cực và quay với tốc độ n vòng/phút thì tần số dòng điện là:",
        "options": ["f = n.p / 60", "f = n.p", "f = 60.n / p", "f = 60.p / n"],
        "answer": "f = n.p / 60",
        "explanation": "Đây là công thức chuẩn cho máy phát điện xoay chiều một pha với n tính theo vòng/phút."
    },
    {
        "question": "Khoảng cách giữa hai khe Young là 1mm, khoảng cách từ hai khe đến màn là 2m. Chiếu ánh sáng đơn sắc bước sóng 0,5 micromet. Khoảng cách từ vân sáng bậc 2 đến vân tối thứ 3 ở cùng một phía là:",
        "options": ["0,5 mm", "1,5 mm", "2,5 mm", "1,0 mm"],
        "answer": "0,5 mm",
        "explanation": "i = lambda.D/a = 0,5*2/1 = 1mm. x_s2 = 2i = 2mm. x_t3 = 2,5i = 2,5mm. delta_x = 0,5mm."
    },
    {
        "question": "Giới hạn quang điện của một kim loại là 0,3 micromet. Công thoát electron của kim loại đó là (h = 6,625.10^-34 J.s, c = 3.10^8 m/s):",
        "options": ["4,14 eV", "2,12 eV", "1,24 eV", "6,62 eV"],
        "answer": "4,14 eV",
        "explanation": "A = hc / lambda_0 = (6,625.10^-34 * 3.10^8) / 0,3.10^-6 approx 6,625.10^-19 J = 4,14 eV."
    },
    {
        "question": "Tốc độ truyền sóng âm trong một môi trường phụ thuộc vào:",
        "options": ["Độ đàn hồi và mật độ của môi trường", "Cường độ âm", "Tần số âm", "Biên độ âm"],
        "answer": "Độ đàn hồi và mật độ của môi trường",
        "explanation": "Vận tốc âm phụ thuộc bản chất môi trường (nhiệt độ, độ đàn hồi, khối lượng riêng)."
    },
    {
        "question": "Cường độ dòng điện cực đại trong mạch dao động LC là I0. Khi cường độ dòng điện i = I0/2 thì năng lượng điện trường bằng bao nhiêu lần năng lượng từ trường?",
        "options": ["3 lần", "1/3 lần", "sqrt(3) lần", "4 lần"],
        "answer": "3 lần",
        "explanation": "Wt = (1/2)Li^2 = (1/2)L(I0/2)^2 = W/4. => Wđ = W - Wt = 3W/4. Vậy Wđ/Wt = 3."
    },
    {
        "question": "Một vật thực hiện đồng thời hai dao động điều hòa cùng phương: x1 = 3.cos(10t) cm và x2 = 4.sin(10t) cm. Biên độ dao động tổng hợp là:",
        "options": ["5 cm", "7 cm", "1 cm", "25 cm"],
        "answer": "5 cm",
        "explanation": "x2 = 4.cos(10t - pi/2). Hai dao động vuông pha nên A = sqrt(3^2 + 4^2) = 5 cm."
    },
    {
        "question": "Đặc trưng nào sau đây của sóng âm liên quan đến biên độ âm?",
        "options": ["Độ to", "Độ cao", "Âm sắc", "Tần số"],
        "answer": "Độ to",
        "explanation": "Độ to của âm phụ thuộc vào mức cường độ âm và tần số, trong đó mức cường độ âm liên quan đến biên độ sóng âm."
    },
    {
        "question": "Một dây đàn dài 60cm phát ra âm cơ bản có tần số 440 Hz. Tốc độ truyền sóng trên dây là:",
        "options": ["528 m/s", "264 m/s", "132 m/s", "880 m/s"],
        "answer": "528 m/s",
        "explanation": "L = lambda / 2 = v / (2f) => v = 2.L.f = 2 * 0,6 * 440 = 528 m/s."
    },
    {
        "question": "Bước sóng dài nhất trong dãy Balmer của quang phổ vạch phát xạ Hydro tương ứng với sự chuyển electron từ quỹ đạo:",
        "options": ["M về L", "L về K", "N về L", "O về L"],
        "answer": "M về L",
        "explanation": "Dãy Balmer về mức L (n=2). Bước sóng dài nhất (năng lượng nhỏ nhất) là từ mức kế tiếp n=3 (M) về n=2 (L)."
    },
    {
        "question": "Khi chiếu chùm tia tử ngoại vào một tấm kẽm tích điện âm thì:",
        "options": ["Tấm kẽm mất dần điện tích âm", "Tấm kẽm mất dần điện tích dương", "Tấm kẽm không thay đổi điện tích", "Tấm kẽm tích điện âm thêm"],
        "answer": "Tấm kẽm mất dần điện tích âm",
        "explanation": "Hiện tượng quang điện làm electron bật ra khỏi tấm kẽm, khiến nó bớt âm đi."
    },
    {
        "question": "Trong thí nghiệm giao thoa sóng nước, hai nguồn S1, S2 dao động cùng pha. Điểm M trên mặt nước cách hai nguồn lần lượt 12cm và 15cm dao động với biên độ cực đại. Giữa M và đường trung trực có 1 dãy cực đại khác. Bước sóng là:",
        "options": ["1,5 cm", "3,0 cm", "1,0 cm", "2,0 cm"],
        "answer": "1,5 cm",
        "explanation": "M là cực đại thứ 2 => d2 - d1 = 2.lambda => 15 - 12 = 2.lambda => lambda = 1,5 cm."
    },
    {
        "question": "Một vật nặng 100g treo vào lò xo có độ cứng k = 40 N/m. Tác dụng một ngoại lực cưỡng bức F = F0.cos(omega.t). Khi omega bằng bao nhiêu thì biên độ dao động đạt cực đại?",
        "options": ["20 rad/s", "10 rad/s", "40 rad/s", "5 rad/s"],
        "answer": "20 rad/s",
        "explanation": "Cộng hưởng khi omega = omega_0 = sqrt(k/m) = sqrt(40/0,1) = 20 rad/s."
    },
    {
        "question": "Tính năng lượng nghỉ của 1g vật chất (c = 3.10^8 m/s):",
        "options": ["9.10^13 J", "9.10^16 J", "3.10^8 J", "3.10^5 J"],
        "answer": "9.10^13 J",
        "explanation": "E = m.c2 = 0,001 * (3.10^8)^2 = 9.10^13 J."
    },
    {
        "question": "Hiệu suất lượng tử của một nguồn sáng là 1%. Biết công suất nguồn là 2W, bước sóng ánh sáng là 0,6 micromet. Số photon phát ra trong 1 giây là:",
        "options": ["6.10^18 hạt", "6.10^16 hạt", "3.10^17 hạt", "2.10^15 hạt"],
        "answer": "6.10^18 hạt",
        "explanation": "P = n.hc/lambda. n = P.lambda / (hc) = 2 * 0,6.10^-6 / (6,625.10^-34 * 3.10^8) approx 6.10^18 hạt."
    },
    {
        "question": "Công thức của định luật khúc xạ ánh sáng là:",
        "options": ["n1.sin_i = n2.sin_r", "n2.sin_i = n1.sin_r", "sin_i / sin_r = n1 / n2", "n1.cos_i = n2.cos_r"],
        "answer": "n1.sin_i = n2.sin_r",
        "explanation": "Đây là định luật Snell về khúc xạ ánh sáng."
    },
    {
        "question": "Năng lượng của một tụ điện đã tích điện được tính bởi công thức:",
        "options": ["W = 1/2 C.U^2", "W = 1/2 C.U", "W = C.U^2", "W = 1/2 Q.C^2"],
        "answer": "W = 1/2 C.U^2",
        "explanation": "Năng lượng điện trường trong tụ điện."
    },
    {
        "question": "Chỉ số chiết suất của nước là 4/3, của thủy tinh là 1,5. Chiết suất tương đối của thủy tinh đối với nước là:",
        "options": ["1,125", "0,888", "1,250", "1,500"],
        "answer": "1,125",
        "explanation": "n21 = n2/n1 = 1,5 / (4/3) = 1,125."
    },
    {
        "question": "Hệ thức Anh-xtanh về hiện tượng quang điện là:",
        "options": ["hf = A + Wđ_max", "hf = A - Wđ_max", "A = hf + Wđ_max", "Wđ_max = A + hf"],
        "answer": "hf = A + Wđ_max",
        "explanation": "Năng lượng photon dùng để thắng công thoát và cung cấp động năng ban đầu cho electron."
    }
,    {
        "question": "Nội năng của một vật là tổng của:",
        "options": ["Động năng và thế năng của vật", "Động năng và thế năng của các phân tử cấu tạo nên vật", "Nhiệt lượng và công", "Nhiệt năng và quang năng"],
        "answer": "Động năng và thế năng của các phân tử cấu tạo nên vật",
        "explanation": "Nội năng bao gồm tổng động năng chuyển động nhiệt và thế năng tương tác giữa các phân tử."
    },
    {
        "question": "Đơn vị đo nhiệt độ trong hệ SI là:",
        "options": ["Độ C", "Độ F", "Kelvin", "Độ bách phân"],
        "answer": "Kelvin",
        "explanation": "Trong hệ đo lường quốc tế SI, Kelvin (K) là đơn vị cơ bản của nhiệt độ."
    },
    {
        "question": "Nhiệt độ nóng chảy của một chất rắn kết tinh phụ thuộc vào:",
        "options": ["Áp suất bên ngoài", "Thể tích của chất", "Hình dạng của vật", "Tốc độ đun nóng"],
        "answer": "Áp suất bên ngoài",
        "explanation": "Nhiệt độ nóng chảy thay đổi tùy thuộc vào áp suất tác động lên bề mặt chất đó."
    },
    {
        "question": "Chất khí lí tưởng là chất khí trong đó các phân tử được coi là:",
        "options": ["Các chất điểm và chỉ tương tác khi va chạm", "Các quả cầu có kích thước lớn", "Các hạt đứng yên", "Các hạt không có khối lượng"],
        "answer": "Các chất điểm và chỉ tương tác khi va chạm",
        "explanation": "Đây là giả thuyết cơ bản trong mô hình động học phân tử khí lí tưởng."
    },
    {
        "question": "Định luật Boyle (Bôi-lơ-ma-ri-ốt) mô tả quá trình:",
        "options": ["Đẳng nhiệt", "Đẳng tích", "Đẳng áp", "Đoạn nhiệt"],
        "answer": "Đẳng nhiệt",
        "explanation": "Định luật Boyle phát biểu về mối quan hệ giữa áp suất và thể tích khi nhiệt độ không đổi."
    },
    {
        "question": "Trong quá trình đẳng tích, đại lượng nào sau đây không thay đổi?",
        "options": ["Nhiệt độ", "Áp suất", "Thể tích", "Mật độ phân tử"],
        "answer": "Thể tích",
        "explanation": "Đẳng tích nghĩa là thể tích của khối khí được giữ cố định (V = hằng số)."
    },
    {
        "question": "Đơn vị của áp suất trong hệ SI là:",
        "options": ["Pascal (Pa)", "Atmosphere (atm)", "mmHg", "Bar"],
        "answer": "Pascal (Pa)",
        "explanation": "Pascal (1 Pa = 1 N/m²) là đơn vị chuẩn của áp suất."
    },
    {
        "question": "Công thức tính nhiệt lượng vật thu vào để tăng nhiệt độ là:",
        "options": ["Q = m.c.delta_t", "Q = m.L", "Q = m.lambda", "Q = U.I.t"],
        "answer": "Q = m.c.delta_t",
        "explanation": "Trong đó c là nhiệt dung riêng, m là khối lượng và delta_t là độ biến thiên nhiệt độ."
    },
    {
        "question": "Độ không tuyệt đối (0 Kelvin) tương đương với:",
        "options": ["0 độ C", "273,15 độ C", "-273,15 độ C", "100 độ C"],
        "answer": "-273,15 độ C",
        "explanation": "Thang Kelvin bắt đầu từ -273,15 độ C, nơi chuyển động nhiệt của các phân tử đạt mức tối thiểu."
    },
    {
        "question": "Hạt nhân nguyên tử được cấu tạo từ các hạt nào?",
        "options": ["Electron và Proton", "Proton và Neutron", "Electron và Neutron", "Chỉ có Proton"],
        "answer": "Proton và Neutron",
        "explanation": "Hạt nhân gồm các nucleon là proton (mang điện dương) và neutron (không mang điện)."
    },
    {
        "question": "Số khối A của một hạt nhân là tổng số của:",
        "options": ["Số Proton và số Electron", "Số Proton và số Neutron", "Số Neutron và số Electron", "Số Proton và số hạt Alpha"],
        "answer": "Số Proton và số Neutron",
        "explanation": "Số khối A = Z (số proton) + N (số neutron)."
    },
    {
        "question": "Đồng vị là các nguyên tử có cùng số:",
        "options": ["Neutron", "Proton nhưng khác số Neutron", "Số khối", "Nucleon"],
        "answer": "Proton nhưng khác số Neutron",
        "explanation": "Đồng vị nằm cùng một ô trong bảng tuần hoàn nhưng có khối lượng khác nhau."
    },
    {
        "question": "Lực hạt nhân chỉ có tác dụng khi khoảng cách giữa hai nucleon khoảng:",
        "options": ["10^-10 m", "10^-15 m", "10^-8 m", "Vô hạn"],
        "answer": "10^-15 m",
        "explanation": "Lực hạt nhân là lực tương tác mạnh nhưng có tầm tác dụng rất ngắn, cỡ kích thước hạt nhân."
    },
    {
        "question": "Hiện tượng phóng xạ là hiện tượng hạt nhân tự động phát ra tia phóng xạ và:",
        "options": ["Biến đổi thành hạt nhân khác", "Vẫn giữ nguyên như cũ", "Bị nóng chảy", "Biến thành electron"],
        "answer": "Biến đổi thành hạt nhân khác",
        "explanation": "Phóng xạ dẫn đến sự thay đổi số proton hoặc neutron, tạo ra hạt nhân mới."
    },
    {
        "question": "Tia Alpha có bản chất là dòng các hạt:",
        "options": ["Hạt nhân Heli (4-He-2)", "Electron", "Sóng điện từ", "Proton"],
        "answer": "Hạt nhân Heli (4-He-2)",
        "explanation": "Tia alpha gồm các hạt mang 2 điện tích dương và có số khối bằng 4."
    },
    {
        "question": "Tia Gamma là:",
        "options": ["Dòng hạt mang điện dương", "Dòng hạt mang điện âm", "Sóng điện từ có bước sóng rất ngắn", "Dòng hạt neutron"],
        "answer": "Sóng điện từ có bước sóng rất ngắn",
        "explanation": "Tia gamma không mang điện và có khả năng đâm xuyên rất mạnh."
    },
    {
        "question": "Chu kỳ bán rã T là khoảng thời gian để:",
        "options": ["Tất cả hạt nhân bị phân rã", "Một nửa số hạt nhân ban đầu bị phân rã", "Số hạt nhân tăng gấp đôi", "Hạt nhân trở nên bền vững"],
        "answer": "Một nửa số hạt nhân ban đầu bị phân rã",
        "explanation": "Đây là đặc trưng cho tốc độ phân rã của một chất phóng xạ."
    },
    {
        "question": "Phản ứng phân hạch là phản ứng trong đó một hạt nhân nặng:",
        "options": ["Kết hợp với hạt nhân nhẹ", "Vỡ ra thành hai hạt nhân trung bình", "Phát ra một tia alpha", "Tự biến mất"],
        "answer": "Vỡ ra thành hai hạt nhân trung bình",
        "explanation": "Thường xảy ra khi hạt nhân nặng hấp thụ một neutron chậm."
    },
    {
        "question": "Phản ứng nhiệt hạch là phản ứng trong đó:",
        "options": ["Hạt nhân nặng vỡ ra", "Hai hạt nhân rất nhẹ kết hợp lại thành hạt nhân nặng hơn", "Hạt nhân phát ra tia gamma", "Electron bị bắn ra"],
        "answer": "Hai hạt nhân rất nhẹ kết hợp lại thành hạt nhân nặng hơn",
        "explanation": "Phản ứng này tỏa ra năng lượng cực lớn và cần nhiệt độ rất cao để xảy ra."
    },
    {
        "question": "Đơn vị của cảm ứng từ là:",
        "options": ["Tesla (T)", "Weber (Wb)", "Vôn (V)", "Ampe (A)"],
        "answer": "Tesla (T)",
        "explanation": "Kí hiệu đơn vị cảm ứng từ B là T."
    },
    {
        "question": "Lực Lorentz là lực từ tác dụng lên:",
        "options": ["Dòng điện thẳng", "Khung dây dẫn", "Hạt mang điện chuyển động trong từ trường", "Điện tích đứng yên"],
        "answer": "Hạt mang điện chuyển động trong từ trường",
        "explanation": "Công thức tính: f = |q|vB.sin(alpha)."
    },
    {
        "question": "Từ thông qua một khung dây kín có đơn vị là:",
        "options": ["Tesla (T)", "Weber (Wb)", "Henry (H)", "Farad (F)"],
        "answer": "Weber (Wb)",
        "explanation": "Weber (Wb) là đơn vị đo thông lượng từ trường qua một diện tích."
    },
    {
        "question": "Quy tắc bàn tay trái dùng để xác định:",
        "options": ["Chiều của cảm ứng từ", "Chiều của lực từ tác dụng lên đoạn dây dẫn", "Chiều của dòng điện cảm ứng", "Chiều của đường sức từ"],
        "answer": "Chiều của lực từ tác dụng lên đoạn dây dẫn",
        "explanation": "Lòng bàn tay hứng B, chiều từ cổ tay đến ngón giữa là I, ngón cái là F."
    },
    {
        "question": "Mối liên hệ giữa áp suất p và nhiệt độ tuyệt đối T trong quá trình đẳng tích là:",
        "options": ["p tỉ lệ thuận với T", "p tỉ lệ nghịch với T", "p không phụ thuộc T", "p tỉ lệ với căn bậc hai của T"],
        "answer": "p tỉ lệ thuận với T",
        "explanation": "Theo định luật Charles, khi thể tích không đổi, p/T = hằng số."
    },
    {
        "question": "Nguyên lí I nhiệt động lực học có công thức là:",
        "options": ["delta_U = Q + A", "delta_U = Q - A", "Q = delta_U + A", "A = Q + delta_U"],
        "answer": "delta_U = Q + A",
        "explanation": "Độ biến thiên nội năng bằng tổng công và nhiệt lượng mà hệ nhận được."
    },
    {
        "question": "Khi đun nóng một khối khí trong bình kín (thể tích không đổi), áp suất khí tăng là do:",
        "options": ["Phân tử khí to lên", "Phân tử khí chuyển động nhanh hơn và va chạm mạnh hơn", "Số lượng phân tử khí tăng", "Trọng lượng phân tử tăng"],
        "answer": "Phân tử khí chuyển động nhanh hơn và va chạm mạnh hơn",
        "explanation": "Nhiệt độ tăng làm tăng động năng phân tử, dẫn đến va chạm vào thành bình mạnh và dày đặc hơn."
    },
    {
        "question": "Sự hóa hơi xảy ra ở bề mặt chất lỏng gọi là:",
        "options": ["Sự sôi", "Sự bay hơi", "Sự ngưng tụ", "Sự đông đặc"],
        "answer": "Sự bay hơi",
        "explanation": "Sự bay hơi diễn ra ở mọi nhiệt độ, khác với sự sôi chỉ xảy ra ở nhiệt độ xác định."
    },
    {
        "question": "Nhiệt hóa hơi riêng của một chất là nhiệt lượng cần cung cấp để 1 kg chất đó:",
        "options": ["Tăng thêm 1 độ", "Hóa hơi hoàn toàn ở nhiệt độ sôi", "Nóng chảy hoàn toàn", "Đông đặc lại"],
        "answer": "Hóa hơi hoàn toàn ở nhiệt độ sôi",
        "explanation": "Đơn vị thường dùng là J/kg."
    },
    {
        "question": "Đặc điểm của lực hạt nhân là:",
        "options": ["Có bản chất là lực điện", "Không phụ thuộc vào điện tích của các nucleon", "Là lực hấp dẫn giữa các nucleon", "Có tầm tác dụng rất lớn"],
        "answer": "Không phụ thuộc vào điện tích của các nucleon",
        "explanation": "Lực hạt nhân giữa p-p, n-n hay p-n đều có cường độ như nhau."
    },
    {
        "question": "Hạt nhân bền vững nhất khi có năng lượng liên kết riêng:",
        "options": ["Càng lớn", "Càng nhỏ", "Bằng 0", "Không đổi"],
        "answer": "Càng lớn",
        "explanation": "Năng lượng liên kết riêng là năng lượng tính trung bình cho một nucleon."
    },
    {
        "question": "Một mol của bất kỳ chất nào cũng chứa số phân tử bằng:",
        "options": ["3,14.10^23", "6,022.10^23", "9,11.10^-31", "1,6.10^-19"],
        "answer": "6,022.10^23",
        "explanation": "Đây được gọi là hằng số Avogadro (NA)."
    },
    {
        "question": "Phương trình trạng thái khí lí tưởng (phương trình Clapeyron) là:",
        "options": ["pV = nRT", "p/V = nRT", "pT = nRV", "V/p = nRT"],
        "answer": "pV = nRT",
        "explanation": "Trong đó n là số mol, R là hằng số khí lí tưởng."
    },
    {
        "question": "Trong máy biến áp, cuộn dây nối với nguồn điện gọi là:",
        "options": ["Cuộn thứ cấp", "Cuộn sơ cấp", "Cuộn lõi", "Cuộn cảm"],
        "answer": "Cuộn sơ cấp",
        "explanation": "Cuộn sơ cấp nhận năng lượng vào, cuộn thứ cấp đưa năng lượng ra."
    },
    {
        "question": "Dòng điện cảm ứng xuất hiện trong mạch kín khi nào?",
        "options": ["Khi từ thông qua mạch biến thiên", "Khi mạch nằm yên trong từ trường đều", "Khi không có từ trường", "Khi cường độ dòng điện bằng 0"],
        "answer": "Khi từ thông qua mạch biến thiên",
        "explanation": "Đây là nội dung chính của định luật Faraday về cảm ứng điện từ."
    },
    {
        "question": "Nhiệt dung riêng của một chất có đơn vị là:",
        "options": ["J/kg", "J/K", "J/(kg.K)", "kg/J"],
        "answer": "J/(kg.K)",
        "explanation": "Nhiệt lượng cần để 1kg chất tăng thêm 1 Kelvin."
    },
    {
        "question": "Khi nhiệt độ của khối khí tăng lên, động năng trung bình của các phân tử khí sẽ:",
        "options": ["Tăng", "Giảm", "Không đổi", "Bằng 0"],
        "answer": "Tăng",
        "explanation": "Nhiệt độ là số đo động năng trung bình của các phân tử cấu tạo nên vật."
    },
    {
        "question": "Hạt nhân 6-C-14 có bao nhiêu proton?",
        "options": ["14", "6", "8", "20"],
        "answer": "6",
        "explanation": "Số dưới (Z) là số hiệu nguyên tử, cũng là số proton."
    },
    {
        "question": "Hạt nhân 6-C-14 có bao nhiêu neutron?",
        "options": ["6", "14", "8", "20"],
        "answer": "8",
        "explanation": "Số neutron = Số khối A - Số proton Z = 14 - 6 = 8."
    },
    {
        "question": "Hiện tượng tán sắc ánh sáng xảy ra khi cho ánh sáng trắng đi qua:",
        "options": ["Gương phẳng", "Lăng kính", "Mặt thủy tinh phẳng song song", "Thấu kính phân kì"],
        "answer": "Lăng kính",
        "explanation": "Ánh sáng trắng bị tách thành dải màu từ đỏ đến tím."
    },
    {
        "question": "Ứng dụng của đồng vị phóng xạ trong y tế là:",
        "options": ["Điều trị ung thư (xạ trị)", "Nấu chín thức ăn", "Sản xuất điện", "Lọc nước"],
        "answer": "Điều trị ung thư (xạ trị)",
        "explanation": "Dùng các tia bức xạ để tiêu diệt tế bào ác tính."
    },
    {
        "question": "Lực từ tác dụng lên đoạn dây dẫn có dòng điện đạt giá trị cực đại khi:",
        "options": ["Dây dẫn song song với B", "Dây dẫn vuông góc với B", "Dây dẫn hợp với B góc 45 độ", "Dòng điện bằng 0"],
        "answer": "Dây dẫn vuông góc với B",
        "explanation": "Khi đó sin(90) = 1, lực F = B.I.L đạt cực đại."
    },
    {
        "question": "Từ trường là dạng vật chất tồn tại xung quanh:",
        "options": ["Điện tích đứng yên", "Dòng điện hoặc nam châm", "Các vật không nhiễm điện", "Thước nhựa"],
        "answer": "Dòng điện hoặc nam châm",
        "explanation": "Từ trường tác dụng lực từ lên dòng điện hoặc nam châm khác đặt trong nó."
    },
    {
        "question": "Trong hệ tọa độ (V, T), đường đẳng áp là đường:",
        "options": ["Thẳng song song trục T", "Hyperbol", "Thẳng có kéo dài đi qua gốc tọa độ", "Thẳng song song trục V"],
        "answer": "Thẳng có kéo dài đi qua gốc tọa độ",
        "explanation": "Theo định luật Gay-Lussac, V tỉ lệ thuận với T."
    },
    {
        "question": "Chất rắn nào sau đây là chất rắn vô định hình?",
        "options": ["Muối ăn", "Kim cương", "Thủy tinh", "Sắt"],
        "answer": "Thủy tinh",
        "explanation": "Chất rắn vô định hình không có cấu trúc tinh thể và không có nhiệt độ nóng chảy xác định."
    },
    {
        "question": "Pin quang điện hoạt động dựa trên hiện tượng:",
        "options": ["Quang điện ngoài", "Quang điện trong", "Tán sắc", "Cảm ứng điện từ"],
        "answer": "Quang điện trong",
        "explanation": "Biến đổi trực tiếp quang năng thành điện năng."
    },
    {
        "question": "Ký hiệu u (đơn vị khối lượng nguyên tử) xấp xỉ bằng khối lượng của hạt nào?",
        "options": ["Electron", "Photon", "Nucleon (Proton hoặc Neutron)", "Hạt Alpha"],
        "answer": "Nucleon (Proton hoặc Neutron)",
        "explanation": "1 u xấp xỉ bằng khối lượng của 1 proton hoặc 1 neutron."
    },
    {
        "question": "Sự ngưng tụ là quá trình chất chuyển từ:",
        "options": ["Rắn sang lỏng", "Lỏng sang khí", "Khí sang lỏng", "Lỏng sang rắn"],
        "answer": "Khí sang lỏng",
        "explanation": "Ví dụ: Hơi nước ngưng tụ thành hạt nước trên lá cây."
    },
    {
        "question": "Thiết bị nào dùng để đo nhiệt độ?",
        "options": ["Lực kế", "Nhiệt kế", "Áp kế", "Tốc kế"],
        "answer": "Nhiệt kế",
        "explanation": "Dựa trên sự giãn nở vì nhiệt hoặc thay đổi điện trở để đo nhiệt độ."
    },
    {
        "question": "Đường sức từ có đặc điểm nào sau đây?",
        "options": ["Là những đường cong kín", "Có thể cắt nhau", "Bắt đầu từ điện tích dương", "Luôn là đường thẳng"],
        "answer": "Là những đường cong kín",
        "explanation": "Các đường sức từ bao quanh dòng điện và không có điểm đầu hay điểm kết thúc."
    },
    {
        "question": "Năng lượng tỏa ra trong phản ứng hạt nhân được tính theo công thức Einstein là:",
        "options": ["E = m.c^2", "E = 1/2 m.v^2", "E = m.g.h", "E = P.t"],
        "answer": "E = m.c^2",
        "explanation": "Năng lượng liên quan đến độ hụt khối m của hệ hạt nhân."
    }
,
    {
        "question": "Nội năng của một vật là gì?",
        "options": ["Tổng động năng và thế năng của vật", "Tổng động năng và thế năng của các phân tử cấu tạo nên vật", "Nhiệt lượng vật nhận được", "Công mà vật thực hiện được"],
        "answer": "Tổng động năng và thế năng của các phân tử cấu tạo nên vật",
        "explanation": "Nội năng là dạng năng lượng bên trong vật, bao gồm tổng động năng chuyển động nhiệt và thế năng tương tác của các phân tử."
    },
    {
        "question": "Đơn vị của nhiệt độ trong hệ SI là:",
        "options": ["Độ C (Celsius)", "Độ F (Fahrenheit)", "Kelvin (K)", "Độ R (Reaumur)"],
        "answer": "Kelvin (K)",
        "explanation": "Kelvin là đơn vị đo nhiệt độ cơ bản trong hệ đo lường quốc tế SI."
    },
    {
        "question": "Nhiệt nóng chảy riêng của một chất là nhiệt lượng cần thiết để làm cho 1 kg chất đó:",
        "options": ["Tăng thêm 1 độ C", "Nóng chảy hoàn toàn ở nhiệt độ nóng chảy", "Hóa hơi hoàn toàn", "Chuyển từ thể khí sang thể lỏng"],
        "answer": "Nóng chảy hoàn toàn ở nhiệt độ nóng chảy",
        "explanation": "Nhiệt nóng chảy riêng (L) tính cho 1kg chất chuyển từ thể rắn sang thể lỏng tại nhiệt độ nóng chảy."
    },
    {
        "question": "Công thức liên hệ giữa nhiệt độ Kelvin (T) và nhiệt độ Celsius (t) là:",
        "options": ["T = t + 273,15", "T = t - 273,15", "T = t / 273,15", "T = 273,15 - t"],
        "answer": "T = t + 273,15",
        "explanation": "Nhiệt độ tuyệt đối bằng nhiệt độ bách phân cộng thêm 273,15."
    },
    {
        "question": "Chất khí lí tưởng là chất khí trong đó các phân tử được coi là:",
        "options": ["Những hạt có kích thước lớn", "Các chất điểm và chỉ tương tác khi va chạm", "Các hạt đứng yên", "Các hạt không có khối lượng"],
        "answer": "Các chất điểm và chỉ tương tác khi va chạm",
        "explanation": "Mô hình khí lí tưởng coi phân tử là chất điểm và bỏ qua tương tác khi chúng không va chạm."
    },
    {
        "question": "Định luật Boyle (Bôi-lơ-ma-ri-ốt) áp dụng cho quá trình nào?",
        "options": ["Đẳng nhiệt", "Đẳng tích", "Đẳng áp", "Đoạn nhiệt"],
        "answer": "Đẳng nhiệt",
        "explanation": "Định luật Boyle mô tả mối quan hệ nghịch biến giữa áp suất và thể tích khi nhiệt độ không đổi."
    },
    {
        "question": "Trong quá trình đẳng tích, đại lượng nào sau đây không thay đổi?",
        "options": ["Áp suất", "Nhiệt độ", "Thể tích", "Nội năng"],
        "answer": "Thể tích",
        "explanation": "Quá trình đẳng tích là quá trình biến đổi trạng thái trong đó thể tích được giữ cố định."
    },
    {
        "question": "Phương trình trạng thái của khí lí tưởng là:",
        "options": ["PV/T = hằng số", "PT/V = hằng số", "VT/P = hằng số", "P.V.T = hằng số"],
        "answer": "PV/T = hằng số",
        "explanation": "Kết hợp các định luật thực nghiệm, ta có tỉ số PV/T luôn không đổi cho một khối lượng khí xác định."
    },
    {
        "question": "Đơn vị của áp suất trong hệ SI là:",
        "options": ["Pascal (Pa)", "Atmosphere (atm)", "mmHg", "Bar"],
        "answer": "Pascal (Pa)",
        "explanation": "Pascal (1 Pa = 1 N/m2) là đơn vị áp suất chuẩn trong hệ SI."
    },
    {
        "question": "Hiện tượng các phân tử khí chuyển động hỗn loạn không ngừng về mọi phía gọi là:",
        "options": ["Chuyển động tịnh tiến", "Chuyển động nhiệt", "Chuyển động rơi tự do", "Chuyển động thẳng đều"],
        "answer": "Chuyển động nhiệt",
        "explanation": "Các phân tử cấu tạo nên vật chuyển động hỗn loạn không ngừng, nhiệt độ càng cao chuyển động càng mạnh."
    },
    {
        "question": "Lực từ tác dụng lên một đoạn dây dẫn có dòng điện đặt trong từ trường đều có hướng:",
        "options": ["Luôn cùng hướng với dòng điện", "Luôn vuông góc với mặt phẳng chứa dòng điện và đường sức từ", "Luôn cùng hướng với đường sức từ", "Luôn nằm ngang"],
        "answer": "Luôn vuông góc với mặt phẳng chứa dòng điện và đường sức từ",
        "explanation": "Theo quy tắc bàn tay trái, lực từ vuông góc với cả vectơ L và vectơ B."
    },
    {
        "question": "Đơn vị của cảm ứng từ B là:",
        "options": ["Tesla (T)", "Weber (Wb)", "Henry (H)", "Farad (F)"],
        "answer": "Tesla (T)",
        "explanation": "Cảm ứng từ có đơn vị là Tesla, ký hiệu là T."
    },
    {
        "question": "Từ thông qua một khung dây kín phụ thuộc vào:",
        "options": ["Cảm ứng từ B", "Diện tích khung dây S", "Góc hợp bởi B và pháp tuyến mặt phẳng khung dây", "Cả 3 phương án trên"],
        "answer": "Cả 3 phương án trên",
        "explanation": "Công thức tính từ thông là Phi = B.S.cos(alpha)."
    },
    {
        "question": "Hạt nhân nguyên tử được cấu tạo từ các hạt:",
        "options": ["Electron và Proton", "Proton và Neutron", "Electron và Neutron", "Chỉ có Proton"],
        "answer": "Proton và Neutron",
        "explanation": "Hạt nhân gồm hai loại hạt (gọi chung là nucleon) là proton mang điện dương và neutron không mang điện."
    },
    {
        "question": "Số khối A của hạt nhân là:",
        "options": ["Số Proton", "Số Neutron", "Tổng số Proton và Neutron", "Số Electron"],
        "answer": "Tổng số Proton và Neutron",
        "explanation": "Số khối A đặc trưng cho tổng số nucleon có trong hạt nhân."
    },
    {
        "question": "Đồng vị là những nguyên tử có cùng số:",
        "options": ["Neutron", "Proton nhưng khác số Neutron", "Số khối", "Electron nhưng khác số Proton"],
        "answer": "Proton nhưng khác số Neutron",
        "explanation": "Đồng vị cùng vị trí trong bảng tuần hoàn (cùng Z) nhưng khác khối lượng (khác N)."
    },
    {
        "question": "Lực liên kết các nucleon trong hạt nhân gọi là:",
        "options": ["Lực điện", "Lực hấp dẫn", "Lực hạt nhân (tương tác mạnh)", "Lực từ"],
        "answer": "Lực hạt nhân (tương tác mạnh)",
        "explanation": "Lực hạt nhân là lực tương tác mạnh, có tầm tác dụng rất ngắn (cỡ kích thước hạt nhân)."
    },
    {
        "question": "Hiện tượng hạt nhân tự động phát ra các tia phóng xạ và biến đổi thành hạt nhân khác là:",
        "options": ["Phản ứng nhiệt hạch", "Phản ứng phân hạch", "Sự phóng xạ", "Sự ion hóa"],
        "answer": "Sự phóng xạ",
        "explanation": "Phóng xạ là quá trình phân rã tự phát của các hạt nhân không bền vững."
    },
    {
        "question": "Tia phóng xạ nào sau đây không mang điện?",
        "options": ["Tia Alpha", "Tia Beta cộng", "Tia Beta trừ", "Tia Gamma"],
        "answer": "Tia Gamma",
        "explanation": "Tia Gamma là sóng điện từ có bước sóng rất ngắn, không mang điện tích."
    },
    {
        "question": "Chu kỳ bán rã là khoảng thời gian để:",
        "options": ["Một nửa số hạt nhân bị phân rã", "Tất cả các hạt nhân bị phân rã", "Vật nóng chảy", "Hạt nhân bắt đầu phóng xạ"],
        "answer": "Một nửa số hạt nhân bị phân rã",
        "explanation": "Sau mỗi chu kỳ T, số lượng hạt nhân phóng xạ còn lại giảm đi 1/2 so với ban đầu."
    },
    {
        "question": "Phản ứng phân hạch thường xảy ra với các hạt nhân:",
        "options": ["Rất nhẹ như Hydro", "Trung bình như Sắt", "Nặng như Urani", "Bền vững"],
        "answer": "Nặng như Urani",
        "explanation": "Phân hạch là sự vỡ ra của một hạt nhân nặng thành các hạt nhân trung bình."
    },
    {
        "question": "Phản ứng nhiệt hạch là phản ứng:",
        "options": ["Kết hợp hai hạt nhân rất nhẹ thành hạt nhân nặng hơn", "Vỡ hạt nhân nặng", "Phát ra tia Beta", "Đốt cháy nhiên liệu hóa thạch"],
        "answer": "Kết hợp hai hạt nhân rất nhẹ thành hạt nhân nặng hơn",
        "explanation": "Nhiệt hạch là sự tổng hợp các hạt nhân nhẹ (như các đồng vị Hydro) ở nhiệt độ rất cao."
    },
    {
        "question": "Đơn vị đo khối lượng hạt nhân thường dùng là:",
        "options": ["kg", "g", "Đơn vị khối lượng nguyên tử (amu hoặc u)", "mg"],
        "answer": "Đơn vị khối lượng nguyên tử (amu hoặc u)",
        "explanation": "Do khối lượng hạt nhân rất nhỏ nên dùng đơn vị u (1u = 1/12 khối lượng nguyên tử C12)."
    },
    {
        "question": "Sự hóa hơi xảy ra trên bề mặt chất lỏng gọi là:",
        "options": ["Sự sôi", "Sự bay hơi", "Sự ngưng tụ", "Sự nóng chảy"],
        "answer": "Sự bay hơi",
        "explanation": "Bay hơi diễn ra ở mọi nhiệt độ và chỉ trên bề mặt; còn sôi diễn ra ở nhiệt độ xác định và trong cả lòng chất lỏng."
    },
    {
        "question": "Độ không tuyệt đối (0 K) tương ứng với bao nhiêu độ C?",
        "options": ["0 độ C", "100 độ C", "-273,15 độ C", "273,15 độ C"],
        "answer": "-273,15 độ C",
        "explanation": "Điểm 0 trên thang Kelvin tương ứng với giá trị thấp nhất có thể đạt được trong nhiệt động lực học."
    },
    {
        "question": "Nguyên lí I nhiệt động lực học được diễn đạt qua công thức delta_U = Q + A. Nếu vật nhận nhiệt lượng và sinh công thì:",
        "options": ["Q > 0, A < 0", "Q < 0, A > 0", "Q > 0, A > 0", "Q < 0, A < 0"],
        "answer": "Q > 0, A < 0",
        "explanation": "Quy ước: Nhận (dương), Sinh/Mất (âm). Nhận nhiệt Q>0, Sinh công A<0."
    },
    {
        "question": "Theo thuyết động học phân tử, áp suất khí lên thành bình gây ra do:",
        "options": ["Trọng lượng của các phân tử", "Sự va chạm của các phân tử lên thành bình", "Lực hút giữa các phân tử", "Nhiệt độ bên ngoài"],
        "answer": "Sự va chạm của các phân tử lên thành bình",
        "explanation": "Vô số va chạm của phân tử lên thành bình tạo ra áp lực tác dụng lên một đơn vị diện tích (áp suất)."
    },
    {
        "question": "Hằng số Avogadro có giá trị xấp xỉ là:",
        "options": ["6,022.10^23 mol-1", "9,1.10^-31 mol-1", "1,6.10^-19 mol-1", "8,31 mol-1"],
        "answer": "6,022.10^23 mol-1",
        "explanation": "Số Avogadro (NA) cho biết số phân tử có trong 1 mol chất."
    },
    {
        "question": "Đường đẳng nhiệt trong hệ tọa độ (p, V) có dạng là đường:",
        "options": ["Thẳng đi qua gốc tọa độ", "Thẳng song song trục p", "Hyperbol", "Parabol"],
        "answer": "Hyperbol",
        "explanation": "Vì p tỉ lệ nghịch với V (p = hằng số / V) nên đồ thị là đường Hyperbol."
    },
    {
        "question": "Đặc điểm của lực từ tác dụng lên dòng điện song song với đường sức từ là:",
        "options": ["Có giá trị lớn nhất", "Bằng không", "Hướng lên trên", "Hướng xuống dưới"],
        "answer": "Bằng không",
        "explanation": "F = B.I.L.sin(alpha). Khi song song thì alpha = 0 hoặc 180 độ, sin(alpha) = 0."
    },
    {
        "question": "Quy tắc nào giúp xác định chiều của lực từ tác dụng lên đoạn dây dẫn?",
        "options": ["Quy tắc nắm tay phải", "Quy tắc bàn tay trái", "Quy tắc vặn đinh ốc", "Quy tắc bàn tay phải"],
        "answer": "Quy tắc bàn tay trái",
        "explanation": "Đặt bàn tay trái sao cho B hướng vào lòng bàn tay, chiều từ cổ tay đến ngón giữa là I, ngón cái choãi ra 90 độ là F."
    },
    {
        "question": "Trong máy phát điện, năng lượng được chuyển hóa từ:",
        "options": ["Nhiệt năng thành điện năng", "Cơ năng thành điện năng", "Hóa năng thành điện năng", "Quang năng thành điện năng"],
        "answer": "Cơ năng thành điện năng",
        "explanation": "Máy phát điện dựa trên hiện tượng cảm ứng điện từ để biến cơ năng quay thành dòng điện."
    },
    {
        "question": "Hạt nhân X có ký hiệu 6-C-12. Số neutron của hạt nhân này là:",
        "options": ["6", "12", "18", "4"],
        "answer": "6",
        "explanation": "Số neutron N = A - Z = 12 - 6 = 6."
    },
    {
        "question": "Độ hụt khối của hạt nhân là hiệu số giữa:",
        "options": ["Tổng khối lượng các nucleon và khối lượng hạt nhân", "Khối lượng hạt nhân và khối lượng các nucleon", "Khối lượng Proton và Neutron", "Khối lượng Electron và Proton"],
        "answer": "Tổng khối lượng các nucleon và khối lượng hạt nhân",
        "explanation": "Khối lượng của hạt nhân luôn nhỏ hơn tổng khối lượng của các nucleon tạo thành nó."
    },
    {
        "question": "Năng lượng liên kết riêng của hạt nhân đặc trưng cho:",
        "options": ["Độ bền vững của hạt nhân", "Khối lượng hạt nhân", "Số lượng proton", "Tốc độ phóng xạ"],
        "answer": "Độ bền vững của hạt nhân",
        "explanation": "Hạt nhân có năng lượng liên kết riêng càng lớn thì càng bền vững."
    },
    {
        "question": "Hằng số phóng xạ lambda và chu kỳ bán rã T liên hệ qua công thức:",
        "options": ["lambda = T / ln2", "lambda = ln2 / T", "lambda = ln2 * T", "lambda = 1 / T"],
        "answer": "lambda = ln2 / T",
        "explanation": "Đây là mối liên hệ nghịch biến giữa tốc độ phân rã và thời gian bán rã."
    },
    {
        "question": "Thiết bị dùng để đo liều lượng phóng xạ mà một người tiếp nhận là:",
        "options": ["Nhiệt kế", "Liều kế", "Ampe kế", "Áp kế"],
        "answer": "Liều kế",
        "explanation": "Liều kế được sử dụng để kiểm soát an toàn phóng xạ cho nhân viên làm việc trong môi trường độc hại."
    },
    {
        "question": "Trong y học, tia phóng xạ được dùng để:",
        "options": ["Chẩn đoán hình ảnh và điều trị ung thư", "Làm sạch nước", "Nấu chín thức ăn", "Sản xuất pin"],
        "answer": "Chẩn đoán hình ảnh và điều trị ung thư",
        "explanation": "Đồng vị phóng xạ được dùng trong xạ trị và chụp PET/CT để phát hiện bệnh."
    },
    {
        "question": "Ứng dụng của hiện tượng nóng chảy là:",
        "options": ["Đúc tượng, chuông", "Làm đá lạnh trong tủ lạnh", "Đun nước sôi", "Sấy tóc"],
        "answer": "Đúc tượng, chuông",
        "explanation": "Người ta nung chảy kim loại rồi đổ vào khuôn để tạo ra các vật dụng khi nó đông đặc lại."
    },
    {
        "question": "Máy biến áp là thiết bị dùng để:",
        "options": ["Thay đổi tần số dòng điện", "Thay đổi điện áp xoay chiều", "Biến dòng xoay chiều thành một chiều", "Tạo ra dòng điện"],
        "answer": "Thay đổi điện áp xoay chiều",
        "explanation": "Dựa trên hiện tượng cảm ứng điện từ, máy biến áp tăng hoặc hạ áp suất điện mà không đổi tần số."
    },
    {
        "question": "Động năng trung bình của phân tử khí tỉ lệ thuận với:",
        "options": ["Nhiệt độ tuyệt đối", "Thể tích bình chứa", "Số lượng phân tử", "Áp suất khí"],
        "answer": "Nhiệt độ tuyệt đối",
        "explanation": "Nhiệt độ tuyệt đối là đại lượng đo lường trực tiếp động năng trung bình của các phân tử."
    },
    {
        "question": "Khi đun nóng một khối khí trong bình kín, nội năng của khối khí tăng chủ yếu do:",
        "options": ["Tăng động năng nhiệt của các phân tử", "Tăng thế năng của các phân tử", "Tăng khối lượng phân tử", "Giảm va chạm"],
        "answer": "Tăng động năng nhiệt của các phân tử",
        "explanation": "Đun nóng làm tăng nhiệt độ, dẫn đến các phân tử chuyển động nhanh hơn (tăng động năng)."
    },
    {
        "question": "Lực Lorentz tác dụng lên một hạt mang điện chuyển động trong từ trường không phụ thuộc vào:",
        "options": ["Điện tích của hạt", "Vận tốc của hạt", "Khối lượng của hạt", "Cảm ứng từ"],
        "answer": "Khối lượng của hạt",
        "explanation": "Công thức lực Lorentz là f = |q|vBsin(alpha), không chứa khối lượng m."
    },
    {
        "question": "Dòng điện cảm ứng xuất hiện trong mạch kín khi:",
        "options": ["Mạch nằm yên trong từ trường đều", "Từ thông qua mạch biến thiên", "Diện tích mạch không đổi", "Cường độ dòng điện không đổi"],
        "answer": "Từ thông qua mạch biến thiên",
        "explanation": "Theo định luật Faraday, sự biến thiên từ thông sinh ra suất điện động cảm ứng trong mạch."
    },
    {
        "question": "Các tia phóng xạ Alpha có bản chất là dòng các hạt:",
        "options": ["Hạt nhân Heli (4-He-2)", "Electron", "Photon", "Proton"],
        "answer": "Hạt nhân Heli (4-He-2)",
        "explanation": "Hạt Alpha gồm 2 proton và 2 neutron, giống hệt hạt nhân nguyên tử Heli."
    },
    {
        "question": "Quá trình một hạt nhân nặng hấp thụ một neutron chậm rồi vỡ ra gọi là:",
        "options": ["Phân hạch", "Nhiệt hạch", "Phóng xạ Alpha", "Ion hóa"],
        "answer": "Phân hạch",
        "explanation": "Đây là cơ chế hoạt động chính trong các lò phản ứng hạt nhân hiện nay."
    },
    {
        "question": "Vật liệu nào sau đây được dùng để làm chậm neutron trong lò phản ứng hạt nhân?",
        "options": ["Nước nặng hoặc Than chì", "Sắt", "Vàng", "Nhựa"],
        "answer": "Nước nặng hoặc Than chì",
        "explanation": "Chất làm chậm giúp giảm tốc độ neutron để duy trì phản ứng dây chuyền kiểm soát được."
    },
    {
        "question": "Đơn vị đo liều lượng hấp thụ phóng xạ là:",
        "options": ["Gray (Gy)", "Newton (N)", "Pascal (Pa)", "Joule (J)"],
        "answer": "Gray (Gy)",
        "explanation": "1 Gray tương ứng với việc hấp thụ 1 Joule năng lượng bức xạ trên 1 kg vật chất."
    },
    {
        "question": "Năng lượng mặt trời có nguồn gốc từ phản ứng:",
        "options": ["Nhiệt hạch", "Phân hạch", "Đốt cháy oxy", "Phóng xạ Alpha"],
        "answer": "Nhiệt hạch",
        "explanation": "Bên trong lòng Mặt Trời diễn ra quá trình tổng hợp hạt nhân Hydro thành Heli giải phóng năng lượng khổng lồ."
    },
    {
        "question": "Trong thang nhiệt độ Celsius, nhiệt độ của nước đá đang tan được quy ước là:",
        "options": ["0 độ C", "32 độ C", "100 độ C", "273 độ C"],
        "answer": "0 độ C",
        "explanation": "Thang Celsius lấy điểm đóng băng của nước tinh khiết làm mốc 0 độ."
    }

]