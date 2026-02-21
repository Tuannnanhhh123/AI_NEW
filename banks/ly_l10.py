
QUESTIONS= [

    {
        "question": "Một vật rơi tự do từ độ cao h. Trong giây cuối cùng, vật đi được quãng đường bằng 3/4 toàn bộ độ cao rơi. Lấy g = 10m/s2. Thời gian rơi của vật là:",
        "options": ["2 s", "1 s", "4 s", "3 s"],
        "answer": "2 s",
        "explanation": "Gọi t là thời gian rơi. h = 0.5gt^2. Quãng đường giây cuối: delta_h = h - 0.5g(t-1)^2 = 0.75h. Giải phương trình tìm được t = 2s."
    },
    {
        "question": "Một canô đi từ bến A đến bến B xuôi dòng hết 2 giờ, đi ngược dòng hết 3 giờ. Nếu canô tắt máy trôi theo dòng nước từ A đến B thì hết bao nhiêu thời gian?",
        "options": ["12 giờ", "5 giờ", "6 giờ", "10 giờ"],
        "answer": "12 giờ",
        "explanation": "v_xuoi = v_t + v_n = S/2; v_nguoc = v_t - v_n = S/3. Suy ra 2v_n = S/2 - S/3 = S/6 => v_n = S/12. Thời gian trôi t = S/v_n = 12h."
    },
    {
        "question": "Vật chuyển động chậm dần đều cho đến khi dừng lại. Trong giây cuối cùng vật đi được 0,5m. Quãng đường vật đi được trong giây sát trước giây cuối là:",
        "options": ["1,5 m", "1,0 m", "2,0 m", "2,5 m"],
        "answer": "1,5 m",
        "explanation": "Xét ngược lại là nhanh dần đều từ trạng thái nghỉ: s1 = 0.5a(1)^2 = 0.5 => a = 1m/s2. Quãng đường giây thứ 2 (ngược): s2 = 0.5*1*2^2 - 0.5 = 1.5m."
    },
    {
        "question": "Một vật được ném ngang từ độ cao h với vận tốc v0. Tầm xa của vật là L. Nếu tăng v0 lên gấp đôi và giảm h đi 4 lần thì tầm xa của vật sẽ là:",
        "options": ["L", "2L", "4L", "L/2"],
        "answer": "L",
        "explanation": "L = v0 * sqrt(2h/g). Khi v0' = 2v0 và h' = h/4 thì L' = 2v0 * sqrt(2(h/4)/g) = 2v0 * 0.5 * sqrt(2h/g) = L."
    },
    {
        "question": "Hai vật m1 = 1kg, m2 = 3kg nối bằng dây nhẹ qua ròng rọc cố định. Thả hệ tự do. Lực căng dây tác dụng lên ròng rọc (trục ròng rọc) có độ lớn là (g = 10m/s2):",
        "options": ["30 N", "15 N", "40 N", "20 N"],
        "answer": "30 N",
        "explanation": "a = (m2-m1)g/(m1+m2) = 5m/s2. T = m1(g+a) = 15N. Lực nén lên trục ròng rọc là F = 2T = 30N."
    },
    {
        "question": "Lực F truyền cho vật m1 gia tốc a1, truyền cho m2 gia tốc a2. Nếu lực F truyền cho vật có khối lượng M = m1 + m2 thì gia tốc a là:",
        "options": ["a1 + a2", "(a1*a2)/(a1+a2)", "sqrt(a1*a2)", "abs(a1-a2)"],
        "answer": "(a1*a2)/(a1+a2)",
        "explanation": "m1 = F/a1, m2 = F/a2. M = F/a = F/a1 + F/a2 => 1/a = 1/a1 + 1/a2 => a = (a1*a2)/(a1+a2)."
    },
    {
        "question": "Một vật 2kg trượt trên sàn có hệ số ma sát 0,2 dưới tác dụng lực kéo F = 10N hợp với phương ngang góc 30 độ. Gia tốc vật là (g = 10m/s2):",
        "options": ["2,83 m/s2", "3,12 m/s2", "2,33 m/s2", "1,55 m/s2"],
        "answer": "2,83 m/s2",
        "explanation": "N = mg - Fsin(30) = 15N. Fms = 0.2*15 = 3N. a = (Fcos30 - Fms)/m = (10*cos30 - 3)/2 approx 2.83m/s2."
    },
    {
        "question": "Một ô tô công suất P không đổi, leo dốc với vận tốc v1, xuống dốc với vận tốc v2. Biết độ dốc là như nhau và lực cản bằng nhau. Vận tốc trên đường bằng là:",
        "options": ["(v1+v2)/2", "2v1v2/(v1+v2)", "sqrt(v1v2)", "v2-v1"],
        "answer": "2v1v2/(v1+v2)",
        "explanation": "P = (Fc + Psin)v1 = (Fc - Psin)v2 = Fc*v. Giải hệ phương trình ta được v = 2v1v2/(v1+v2)."
    },
    {
        "question": "Một viên đạn 10g bay với vận tốc 400m/s xuyên qua tấm gỗ dày 10cm. Sau đó vận tốc còn 100m/s. Lực cản trung bình của tấm gỗ là:",
        "options": ["7500 N", "750 N", "1500 N", "3750 N"],
        "answer": "7500 N",
        "explanation": "Độ biến thiên động năng: 0.5m(v2^2 - v1^2) = -Fc*s. Fc = -0.01*(100^2 - 400^2) / (2 * 0.1) = 7500N."
    },
    {
        "question": "Quả cầu m = 100g treo vào dây l = 1m. Kéo dây lệch góc 60 độ rồi thả nhẹ. Lực căng dây khi quả cầu qua vị trí cân bằng là (g = 10m/s2):",
        "options": ["1 N", "2 N", "3 N", "1,5 N"],
        "answer": "2 N",
        "explanation": "T = mg(3 - 2cos(alpha_0)). Với alpha_0 = 60 độ, T = 0.1*10*(3 - 2*0.5) = 2N."
    },
    {
        "question": "Thả vật từ độ cao h. Tại vị trí nào thế năng bằng 1/3 động năng?",
        "options": ["h/4", "h/3", "2h/3", "3h/4"],
        "answer": "h/4",
        "explanation": "W = Wd + Wt = 3Wt + Wt = 4Wt. mgh = 4mgh' => h' = h/4."
    },
    {
        "question": "Một hệ gồm 2 vật m1 = 1kg, m2 = 4kg chuyển động với vận tốc v1 = 4m/s, v2 = 1m/s theo hai hướng vuông góc. Động lượng tổng cộng của hệ có độ lớn:",
        "options": ["8 kg.m/s", "5 kg.m/s", "4*sqrt(2) kg.m/s", "0 kg.m/s"],
        "answer": "4*sqrt(2) kg.m/s",
        "explanation": "p1 = m1v1 = 4; p2 = m2v2 = 4. Vì vuông góc nên p = sqrt(p1^2 + p2^2) = sqrt(16+16) = 4*sqrt(2)."
    },
    {
        "question": "Một khẩu súng 5kg bắn viên đạn 20g theo phương ngang với vận tốc 500m/s. Vận tốc giật lùi của súng là:",
        "options": ["2 m/s", "4 m/s", "10 m/s", "2,5 m/s"],
        "answer": "2 m/s",
        "explanation": "Bảo toàn động lượng: M*V + m*v = 0 => V = -mv/M = -(0.02 * 500) / 5 = -2m/s."
    },
    {
        "question": "Lực F tác dụng vào vật m trong khoảng thời gian 0,1s làm vận tốc thay đổi từ 2m/s lên 5m/s. Nếu m = 2kg thì F có độ lớn:",
        "options": ["60 N", "30 N", "10 N", "15 N"],
        "answer": "60 N",
        "explanation": "F*delta_t = m(v2 - v1) => F = 2*(5-2)/0.1 = 60N."
    },
    {
        "question": "Một vệ tinh bay quanh Trái Đất ở độ cao bằng bán kính Trái Đất (R). Gia tốc hướng tâm của vệ tinh là (g là gia tốc tại mặt đất):",
        "options": ["g/2", "g/4", "g", "g/9"],
        "answer": "g/4",
        "explanation": "g' = g * [R/(R+h)]^2. Với h = R, g' = g * (R/2R)^2 = g/4."
    },
    {
        "question": "Một đĩa tròn quay đều với tần số 5 vòng/s. Điểm A cách tâm 10cm, điểm B cách tâm 20cm. Tỉ số vận tốc dài vB/vA là:",
        "options": ["2", "4", "1", "0,5"],
        "answer": "2",
        "explanation": "v = omega*r. Cùng đĩa nên cùng omega. vB/vA = rB/rA = 20/10 = 2."
    },
    {
        "question": "Ngẫu lực tác dụng vào một vật có đặc điểm:",
        "options": ["Làm vật chuyển động tịnh tiến", "Hợp lực bằng 0 nhưng mômen khác 0", "Hợp lực khác 0", "Mômen bằng 0"],
        "answer": "Hợp lực bằng 0 nhưng mômen khác 0",
        "explanation": "Ngẫu lực gồm 2 lực song song ngược chiều cùng độ lớn nên hợp lực triệt tiêu, chỉ gây tác dụng quay."
    },
    {
        "question": "Một vật m = 5kg đứng yên trên mặt sàn nằm ngang. Hệ số ma sát nghỉ là 0,4. Tác dụng lực F = 15N song song với sàn. Lực ma sát khi đó là:",
        "options": ["20 N", "15 N", "10 N", "0 N"],
        "answer": "15 N",
        "explanation": "Fms_nghi_max = mu*m*g = 0.4*5*10 = 20N. Vì F_keo = 15N < 20N nên vật chưa chuyển động, Fms_nghi = F_keo = 15N."
    },
    {
        "question": "Động năng của vật thay đổi như thế nào nếu khối lượng giảm đi một nửa và vận tốc tăng gấp đôi?",
        "options": ["Không đổi", "Tăng 2 lần", "Tăng 4 lần", "Giảm 2 lần"],
        "answer": "Tăng 2 lần",
        "explanation": "Wd' = 0.5 * (m/2) * (2v)^2 = 0.5 * m/2 * 4v^2 = 2 * (0.5mv^2) = 2Wd."
    },
    {
        "question": "Công của lực thế (như trọng lực) có đặc điểm:",
        "options": ["Phụ thuộc hình dạng đường đi", "Chỉ phụ thuộc vị trí đầu và cuối", "Luôn bằng 0", "Luôn dương"],
        "answer": "Chỉ phụ thuộc vị trí đầu và cuối",
        "explanation": "Đây là định nghĩa về lực thế trong vật lí."
    },
    {
        "question": "Một lò xo có độ cứng k. Khi cắt lò xo thành 2 đoạn bằng nhau thì độ cứng của mỗi đoạn mới là:",
        "options": ["k/2", "k", "2k", "4k"],
        "answer": "2k",
        "explanation": "Độ cứng k tỉ lệ nghịch với chiều dài tự nhiên l. Chiều dài giảm nửa thì k tăng gấp đôi."
    },
    {
        "question": "Một vật rơi tự do, trong giây thứ n quãng đường đi được là sn. Quãng đường đi được trong giây thứ (n+1) là:",
        "options": ["sn + g/2", "sn + g", "sn + 2g", "sn + g^2"],
        "answer": "sn + g",
        "explanation": "delta_s_n = 0.5g(2n-1). delta_s_n+1 = 0.5g(2n+1). Hiệu là g."
    },
    {
        "question": "Mômen của một lực đối với một trục quay là đại lượng đo bằng:",
        "options": ["Tích lực và cánh tay đòn", "Thương số lực và cánh tay đòn", "Tích lực và quãng đường", "Tích lực và vận tốc"],
        "answer": "Tích lực và cánh tay đòn",
        "explanation": "M = F.d, trong đó d là khoảng cách từ trục quay đến giá của lực."
    },
    {
        "question": "Một ô tô đang chạy với vận tốc v thì tắt máy trượt trên sàn ngang. Quãng đường đi được đến khi dừng tỉ lệ với:",
        "options": ["v", "căn bậc hai của v", "v bình phương", "nghịch đảo của v"],
        "answer": "v bình phương",
        "explanation": "0 - v^2 = 2as => s = v^2 / (2*mu*g)."
    },
    {
        "question": "Để tăng hiệu suất của một máy, ta cần:",
        "options": ["Giảm công toàn phần", "Giảm công hao phí", "Tăng thời gian làm việc", "Tăng lực tác dụng"],
        "answer": "Giảm công hao phí",
        "explanation": "H = (Atp - Ahp) / Atp. Giảm Ahp giúp H tăng."
    },
    {
        "question": "Lực ném một vật theo phương ngang từ độ cao h. Thời gian rơi phụ thuộc vào:",
        "options": ["Vận tốc ném v0", "Độ cao h", "Khối lượng m", "Cả v0 và h"],
        "answer": "Độ cao h",
        "explanation": "t = sqrt(2h/g), không phụ thuộc vào vận tốc ném ngang."
    },
    {
        "question": "Hai vật m1 = m, m2 = 2m va chạm hoàn toàn đàn hồi. Trước va chạm m2 đứng yên, m1 chuyển động với vận tốc v. Sau va chạm v1 bằng:",
        "options": ["v/3", "-v/3", "v/2", "0"],
        "answer": "-v/3",
        "explanation": "v1' = [(m1-m2)v + 2m2v2] / (m1+m2) = (m-2m)v / (3m) = -v/3."
    },
    {
        "question": "Công suất tức thời của một lực F tác dụng lên vật đang chuyển động với vận tốc v là:",
        "options": ["F.v.cos(alpha)", "F.s", "F.v.sin(alpha)", "F/v"],
        "answer": "F.v.cos(alpha)",
        "explanation": "P = dA/dt = F.ds.cos(alpha)/dt = F.v.cos(alpha)."
    },
    {
        "question": "Một vật trượt từ đỉnh mặt phẳng nghiêng góc 30 độ, dài 10m. Hệ số ma sát là 0,1. Vận tốc ở chân dốc là (g=10):",
        "options": ["9,1 m/s", "8,5 m/s", "7,2 m/s", "10 m/s"],
        "answer": "9,1 m/s",
        "explanation": "a = g(sin30 - mu.cos30) = 4.13m/s2. v = sqrt(2as) approx 9.1m/s."
    },
    {
        "question": "Động năng của một vật chuyển động tròn đều là:",
        "options": ["Biến thiên điều hòa", "Không đổi", "Luôn bằng 0", "Tăng dần theo bán kính"],
        "answer": "Không đổi",
        "explanation": "Trong chuyển động tròn đều, độ lớn vận tốc không đổi nên động năng không đổi."
    },
    {
        "question": "Đơn vị của hằng số hấp dẫn G là:",
        "options": ["N.m2/kg2", "N.m/kg", "kg2/N.m2", "m/s2"],
        "answer": "N.m2/kg2",
        "explanation": "Từ F = G.m1.m2/r2 => G = F.r2 / (m1.m2)."
    },
    {
        "question": "Nếu khối lượng của cả hai vật tăng gấp đôi và khoảng cách giảm một nửa thì lực hấp dẫn giữa chúng:",
        "options": ["Tăng 4 lần", "Tăng 8 lần", "Tăng 16 lần", "Không đổi"],
        "answer": "Tăng 16 lần",
        "explanation": "F' = G(2m1)(2m2) / (r/2)^2 = 4*4*F = 16F."
    },
    {
        "question": "Độ lớn lực hướng tâm tỉ lệ với:",
        "options": ["Bình phương tốc độ góc", "Tốc độ góc", "Căn bậc hai tốc độ góc", "Nghịch đảo tốc độ góc"],
        "answer": "Bình phương tốc độ góc",
        "explanation": "Fht = m.omega^2.r."
    },
    {
        "question": "Trong va chạm đàn hồi giữa hai quả cầu, đại lượng nào sau đây KHÔNG bảo toàn?",
        "options": ["Động lượng", "Cơ năng", "Động năng", "Vận tốc của mỗi vật"],
        "answer": "Vận tốc của mỗi vật",
        "explanation": "Vận tốc của từng vật sẽ thay đổi sau va chạm, chỉ có tổng động lượng và tổng động năng được bảo toàn."
    },
    {
        "question": "Lực đàn hồi của lò xo có hướng:",
        "options": ["Luôn hướng vào tâm Trái Đất", "Ngược hướng với biến dạng", "Cùng hướng với biến dạng", "Luôn nằm ngang"],
        "answer": "Ngược hướng với biến dạng",
        "explanation": "Lực đàn hồi luôn có xu hướng đưa vật về vị trí chưa biến dạng."
    },
    {
        "question": "Một máy kéo có công suất 10kW kéo một vật chuyển động đều với vận tốc 2m/s. Lực kéo của máy là:",
        "options": ["20 kN", "5 kN", "2 kN", "500 N"],
        "answer": "5 kN",
        "explanation": "P = F.v => F = P/v = 10000 / 2 = 5000N = 5kN."
    },
    {
        "question": "Khi khoảng cách giữa hai chất điểm tăng lên 3 lần thì lực hấp dẫn giữa chúng sẽ:",
        "options": ["Giảm 3 lần", "Giảm 9 lần", "Tăng 3 lần", "Tăng 9 lần"],
        "answer": "Giảm 9 lần",
        "explanation": "Lực hấp dẫn tỉ lệ nghịch với bình phương khoảng cách."
    },
    {
        "question": "Một lò xo giãn ra 2cm khi treo vật 100g. Độ cứng của lò xo là (g=10):",
        "options": ["50 N/m", "5 N/m", "0,5 N/m", "500 N/m"],
        "answer": "50 N/m",
        "explanation": "k = F/delta_l = mg/delta_l = (0.1*10)/0.02 = 50N/m."
    },
    {
        "question": "Định luật bảo toàn cơ năng áp dụng khi vật chuyển động chỉ dưới tác dụng của:",
        "options": ["Lực ma sát", "Lực thế (như trọng lực, lực đàn hồi)", "Ngoại lực bất kì", "Lực cản"],
        "answer": "Lực thế (như trọng lực, lực đàn hồi)",
        "explanation": "Cơ năng chỉ bảo toàn khi không có lực không thế (như ma sát) làm việc."
    },
    {
        "question": "Gia tốc của một vật tỉ lệ thuận với lực tác dụng và tỉ lệ nghịch với khối lượng vật. Đây là định luật nào?",
        "options": ["Định luật I Newton", "Định luật II Newton", "Định luật III Newton", "Định luật Vạn vật hấp dẫn"],
        "answer": "Định luật II Newton",
        "explanation": "Nội dung định luật II Newton: a = F/m."
    },
    {
        "question": "Khi ném một vật lên cao, công của trọng lực trong quá trình đi lên là:",
        "options": ["Dương", "Âm", "Bằng 0", "Không xác định"],
        "answer": "Âm",
        "explanation": "Khi đi lên, lực trọng trường hướng xuống ngược chiều dịch chuyển nên công âm."
    },
    {
        "question": "Một vật khối lượng m đang chuyển động với động năng Wd. Động lượng của vật có độ lớn là:",
        "options": ["sqrt(2m*Wd)", "2m*Wd", "m*Wd", "sqrt(m*Wd)"],
        "answer": "sqrt(2m*Wd)",
        "explanation": "Wd = p^2 / 2m => p = sqrt(2m*Wd)."
    },
    {
        "question": "Đơn vị của công suất trong hệ SI là:",
        "options": ["Joule", "Newton", "Watt", "Pascal"],
        "answer": "Watt",
        "explanation": "1 Watt = 1 Joule / giây."
    },
    {
        "question": "Một người xách một túi gạo 10kg đi bộ trên quãng đường ngang 20m. Công của trọng lực là:",
        "options": ["2000 J", "200 J", "0 J", "1000 J"],
        "answer": "0 J",
        "explanation": "Trọng lực vuông góc với hướng dịch chuyển nên không sinh công."
    },
    {
        "question": "Hệ số ma sát giữa hai bề mặt phụ thuộc vào:",
        "options": ["Áp lực", "Diện tích tiếp xúc", "Bản chất bề mặt", "Vận tốc vật"],
        "answer": "Bản chất bề mặt",
        "explanation": "Hệ số ma sát chỉ phụ thuộc vật liệu và tình trạng của hai bề mặt tiếp xúc."
    },
    {
        "question": "Chuyển động thẳng biến đổi đều có đồ thị vận tốc - thời gian (v-t) là một đường:",
        "options": ["Thẳng", "Parabol", "Cong bất kì", "Tròn"],
        "answer": "Thẳng",
        "explanation": "v = v0 + at là hàm bậc nhất theo t, đồ thị là đường thẳng xiên."
    },
    {
        "question": "Điều kiện để một vật đứng yên trên mặt phẳng nghiêng là:",
        "options": ["Lực ma sát nghỉ lớn hơn hoặc bằng thành phần trọng lực song song mặt nghiêng", "Hệ số ma sát bằng 0", "Trọng tâm vật ở rất cao", "Vật phải có khối lượng rất nhỏ"],
        "answer": "Lực ma sát nghỉ lớn hơn hoặc bằng thành phần trọng lực song song mặt nghiêng",
        "explanation": "Điều kiện cân bằng lực dọc theo mặt nghiêng."
    },
    {
        "question": "Đơn vị của tần số góc omega là:",
        "options": ["vòng/giây", "rad/s", "giây/vòng", "Hz"],
        "answer": "rad/s",
        "explanation": "Tần số góc được đo bằng radian trên giây."
    },
    {
        "question": "Biểu thức của momen lực đối với trục quay là:",
        "options": ["M = F/d", "M = F.d", "M = d/F", "M = F.s"],
        "answer": "M = F.d",
        "explanation": "Trong đó d là cánh tay đòn của lực."
    },
    {
        "question": "Nếu một vật đang chuyển động tịnh tiến mà tổng các lực tác dụng lên nó bằng 0 thì vật sẽ:",
        "options": ["Dừng lại ngay", "Chuyển động thẳng đều", "Chuyển động nhanh dần", "Chuyển động chậm dần"],
        "answer": "Chuyển động thẳng đều",
        "explanation": "Theo định luật I Newton (quán tính)."
    }
,
    {
        "question": "Đại lượng nào sau đây là đại lượng vectơ?",
        "options": ["Quãng đường", "Thời gian", "Độ dịch chuyển", "Tốc độ"],
        "answer": "Độ dịch chuyển",
        "explanation": "Độ dịch chuyển xác định độ biến thiên vị trí của vật, có hướng và độ lớn nên là đại lượng vectơ."
    },
    {
        "question": "Đơn vị đo vận tốc trong hệ SI là:",
        "options": ["km/h", "m/s", "cm/s", "m/s^2"],
        "answer": "m/s",
        "explanation": "Mét trên giây (m/s) là đơn vị chuẩn của vận tốc trong hệ đo lường quốc tế."
    },
    {
        "question": "Tốc độ trung bình được tính bằng công thức nào?",
        "options": ["v = d/t", "v = s/t", "v = a.t", "v = s.t"],
        "answer": "v = s/t",
        "explanation": "Tốc độ trung bình bằng tổng quãng đường chia cho tổng thời gian chuyển động."
    },
    {
        "question": "Chuyển động thẳng biến đổi đều là chuyển động có:",
        "options": ["Gia tốc thay đổi", "Gia tốc không đổi", "Vận tốc không đổi", "Quỹ đạo là đường cong"],
        "answer": "Gia tốc không đổi",
        "explanation": "Đặc điểm của chuyển động biến đổi đều là gia tốc là một hằng số."
    },
    {
        "question": "Trong chuyển động thẳng nhanh dần đều, gia tốc và vận tốc luôn:",
        "options": ["Cùng chiều", "Ngược chiều", "Vuông góc", "Ngược dấu"],
        "answer": "Cùng chiều",
        "explanation": "Nhanh dần đều thì tích a.v > 0, nghĩa là a và v cùng chiều."
    },
    {
        "question": "Công thức tính gia tốc là:",
        "options": ["a = (v-v0)/t", "a = v/t", "a = s/t", "a = v.t"],
        "answer": "a = (v-v0)/t",
        "explanation": "Gia tốc đặc trưng cho sự biến thiên vận tốc theo thời gian."
    },
    {
        "question": "Rơi tự do là chuyển động của vật dưới tác dụng của lực nào?",
        "options": ["Lực ma sát", "Lực đẩy", "Trọng lực", "Lực đàn hồi"],
        "answer": "Trọng lực",
        "explanation": "Sự rơi tự do là sự rơi chỉ dưới tác dụng của trọng lực."
    },
    {
        "question": "Gia tốc rơi tự do g thường được lấy giá trị xấp xỉ là:",
        "options": ["9,8 m/s^2", "1,6 m/s^2", "0 m/s^2", "100 m/s^2"],
        "answer": "9,8 m/s^2",
        "explanation": "Ở gần mặt đất, g thường được lấy là 9,8 hoặc 10 m/s^2."
    },
    {
        "question": "Vật nào sau đây được coi là chất điểm?",
        "options": ["Ô tô trong gara", "Trái Đất quay quanh Mặt Trời", "Con kiến trên bàn tay", "Người đang tập thể dục"],
        "answer": "Trái Đất quay quanh Mặt Trời",
        "explanation": "Vật được coi là chất điểm khi kích thước rất nhỏ so với quãng đường di chuyển."
    },
    {
        "question": "Đồ thị độ dịch chuyển - thời gian của chuyển động thẳng đều là:",
        "options": ["Đường tròn", "Đường thẳng", "Đường parabol", "Đường gấp khúc"],
        "answer": "Đường thẳng",
        "explanation": "Trong chuyển động thẳng đều, độ dịch chuyển tỉ lệ thuận với thời gian nên đồ thị là đường thẳng."
    },
    {
        "question": "Đơn vị của lực trong hệ SI là:",
        "options": ["Kilôgam (kg)", "Newton (N)", "Joule (J)", "Watt (W)"],
        "answer": "Newton (N)",
        "explanation": "Đơn vị đo lực là Newton, ký hiệu là N."
    },
    {
        "question": "Định luật I Newton còn được gọi là định luật:",
        "options": ["Hấp dẫn", "Bảo toàn", "Quán tính", "Phản xạ"],
        "answer": "Quán tính",
        "explanation": "Định luật I khẳng định tính chất bảo toàn trạng thái chuyển động của vật, gọi là quán tính."
    },
    {
        "question": "Biểu thức của định luật II Newton là:",
        "options": ["F = m.a", "F = m/a", "a = m.F", "m = F.a"],
        "answer": "F = m.a",
        "explanation": "Lực tác dụng bằng tích khối lượng và gia tốc vật thu được."
    },
    {
        "question": "Theo định luật III Newton, cặp lực và phản lực:",
        "options": ["Cùng điểm đặt", "Cùng chiều", "Cùng giá, ngược chiều", "Độ lớn khác nhau"],
        "answer": "Cùng giá, ngược chiều",
        "explanation": "Lực và phản lực luôn cùng giá, cùng độ lớn nhưng ngược chiều và đặt vào 2 vật khác nhau."
    },
    {
        "question": "Trọng lượng của một vật được tính theo công thức:",
        "options": ["P = m.g", "P = m/g", "P = m+g", "P = g/m"],
        "answer": "P = m.g",
        "explanation": "Trọng lượng là độ lớn của trọng lực: P = mg."
    },
    {
        "question": "Lực ma sát trượt xuất hiện khi nào?",
        "options": ["Vật đứng yên", "Vật trượt trên bề mặt", "Vật rơi tự do", "Vật đang bay"],
        "answer": "Vật trượt trên bề mặt",
        "explanation": "Ma sát trượt sinh ra ở mặt tiếp xúc khi vật này trượt trên bề mặt vật khác."
    },
    {
        "question": "Hệ số ma sát trượt có đơn vị là:",
        "options": ["Newton", "m/s", "Không có đơn vị", "Joule"],
        "answer": "Không có đơn vị",
        "explanation": "Hệ số ma sát là tỉ lệ giữa hai lực nên là đại lượng không đơn vị."
    },
    {
        "question": "Lực đẩy Archimedes có chiều như thế nào?",
        "options": ["Hướng xuống dưới", "Hướng lên trên", "Nằm ngang", "Xiên góc"],
        "answer": "Hướng lên trên",
        "explanation": "Lực đẩy của chất lỏng tác dụng lên vật nhúng trong nó luôn hướng thẳng đứng lên trên."
    },
    {
        "question": "Định luật Hooke áp dụng cho lò xo trong giới hạn đàn hồi là:",
        "options": ["F = k.|dl|", "F = m.a", "F = k/|dl|", "F = p.S"],
        "answer": "F = k.|dl|",
        "explanation": "Trong giới hạn đàn hồi, lực đàn hồi tỉ lệ thuận với độ biến dạng."
    },
    {
        "question": "Mômen lực đặc trưng cho tác dụng nào của lực?",
        "options": ["Làm biến dạng vật", "Làm quay vật", "Làm vật rơi", "Làm vật dừng lại"],
        "answer": "Làm quay vật",
        "explanation": "Mômen lực là đại lượng đặc trưng cho tác dụng làm quay vật quanh một trục."
    },
    {
        "question": "Đơn vị của mômen lực là:",
        "options": ["N/m", "N.m", "kg.m", "J/s"],
        "answer": "N.m",
        "explanation": "M = F.d, đơn vị là Newton nhân mét."
    },
    {
        "question": "Công cơ học được tính bằng công thức nào (khi lực cùng chiều chuyển động)?",
        "options": ["A = F.s", "A = F/s", "A = m.g.h", "A = P.t"],
        "answer": "A = F.s",
        "explanation": "Công bằng tích lực tác dụng và quãng đường dịch chuyển."
    },
    {
        "question": "Đơn vị của công trong hệ SI là:",
        "options": ["Watt (W)", "Newton (N)", "Joule (J)", "Pascal (Pa)"],
        "answer": "Joule (J)",
        "explanation": "Đơn vị đo công và năng lượng là Joule (J)."
    },
    {
        "question": "Công suất là đại lượng đặc trưng cho:",
        "options": ["Độ lớn của lực", "Tốc độ thực hiện công", "Quãng đường đi được", "Năng lượng dư thừa"],
        "answer": "Tốc độ thực hiện công",
        "explanation": "Công suất bằng công thực hiện được trong một đơn vị thời gian."
    },
    {
        "question": "Đơn vị của công suất là:",
        "options": ["Joule (J)", "Watt (W)", "Newton (N)", "Hertz (Hz)"],
        "answer": "Watt (W)",
        "explanation": "1 Watt = 1 Joule / giây."
    },
    {
        "question": "Động năng của một vật được tính theo công thức:",
        "options": ["1/2 m.v^2", "m.v", "m.g.h", "1/2 k.x^2"],
        "answer": "1/2 m.v^2",
        "explanation": "Năng lượng do vật chuyển động mà có gọi là động năng."
    },
    {
        "question": "Thế năng trọng trường của một vật phụ thuộc vào:",
        "options": ["Vận tốc", "Độ cao", "Thời gian", "Nhiệt độ"],
        "answer": "Độ cao",
        "explanation": "Wt = mgh, phụ thuộc vào khối lượng và độ cao so với mốc."
    },
    {
        "question": "Cơ năng của một vật bằng:",
        "options": ["Tổng động năng và thế năng", "Hiệu động năng và thế năng", "Tích động năng và thế năng", "Động năng nhân 2"],
        "answer": "Tổng động năng và thế năng",
        "explanation": "Cơ năng là tổng các dạng năng lượng cơ học của vật."
    },
    {
        "question": "Động lượng của một vật khối lượng m đang chuyển động với vận tốc v là:",
        "options": ["p = m.v", "p = 1/2 m.v^2", "p = m.a", "p = F.t"],
        "answer": "p = m.v",
        "explanation": "Động lượng là đại lượng vectơ bằng tích khối lượng và vận tốc."
    },
    {
        "question": "Đơn vị của động lượng là:",
        "options": ["kg.m/s", "N.m", "J.s", "kg.m/s^2"],
        "answer": "kg.m/s",
        "explanation": "Dựa trên công thức p=mv, đơn vị khối lượng (kg) nhân đơn vị vận tốc (m/s)."
    },
    {
        "question": "Trong hệ cô lập, đại lượng nào sau đây được bảo toàn?",
        "options": ["Vận tốc", "Động lượng", "Gia tốc", "Lực"],
        "answer": "Động lượng",
        "explanation": "Theo định luật bảo toàn động lượng cho hệ kín."
    },
    {
        "question": "Va chạm mềm là va chạm mà sau đó hai vật:",
        "options": ["Dính vào nhau", "Nảy ra xa nhau", "Dừng lại", "Vỡ vụn"],
        "answer": "Dính vào nhau",
        "explanation": "Đặc điểm va chạm mềm là sau va chạm hai vật nhập làm một."
    },
    {
        "question": "Chu kỳ trong chuyển động tròn đều là:",
        "options": ["Số vòng đi được trong 1s", "Thời gian đi hết một vòng", "Quãng đường đi được", "Vận tốc góc"],
        "answer": "Thời gian đi hết một vòng",
        "explanation": "Chu kỳ T là khoảng thời gian để vật thực hiện một vòng quay."
    },
    {
        "question": "Tần số f của chuyển động tròn đều có đơn vị là:",
        "options": ["Giây (s)", "Hertz (Hz)", "m/s", "rad/s"],
        "answer": "Hertz (Hz)",
        "explanation": "Tần số là số vòng trong 1 giây, đơn vị là Hz."
    },
    {
        "question": "Gia tốc hướng tâm có hướng như thế nào?",
        "options": ["Cùng hướng vận tốc", "Ngược hướng vận tốc", "Hướng vào tâm quỹ đạo", "Hướng ra xa tâm"],
        "answer": "Hướng vào tâm quỹ đạo",
        "explanation": "Trong chuyển động tròn, gia tốc luôn hướng về tâm quỹ đạo."
    },
    {
        "question": "Tốc độ góc omega có đơn vị là:",
        "options": ["m/s", "rad/s", "vòng/s", "rad.s"],
        "answer": "rad/s",
        "explanation": "Radian trên giây là đơn vị chuẩn của tốc độ góc."
    },
    {
        "question": "Hiệu suất của một máy luôn có giá trị:",
        "options": ["H > 1", "H = 1", "H < 1", "H = 0"],
        "answer": "H < 1",
        "explanation": "Do hao phí năng lượng, công có ích luôn nhỏ hơn công toàn phần."
    },
    {
        "question": "Đại lượng vật lí nào đặc trưng cho mức độ quán tính của vật?",
        "options": ["Vận tốc", "Lực", "Khối lượng", "Thể tích"],
        "answer": "Khối lượng",
        "explanation": "Khối lượng càng lớn thì vật càng khó thay đổi trạng thái chuyển động."
    },
    {
        "question": "Khi ô tô đang chạy mà phanh gấp, hành khách có xu hướng:",
        "options": ["Ngả người ra sau", "Chúi người về phía trước", "Nghiêng sang trái", "Nghiêng sang phải"],
        "answer": "Chúi người về phía trước",
        "explanation": "Do quán tính, cơ thể hành khách muốn duy trì vận tốc cũ."
    },
    {
        "question": "Lực hấp dẫn giữa hai vật phụ thuộc vào:",
        "options": ["Khối lượng và khoảng cách", "Vận tốc và khối lượng", "Thời gian và vị trí", "Thể tích vật"],
        "answer": "Khối lượng và khoảng cách",
        "explanation": "F = G.m1.m2 / r^2."
    },
    {
        "question": "Năng lượng không tự sinh ra cũng không tự mất đi mà chỉ:",
        "options": ["Biến mất", "Đứng yên", "Chuyển hóa và truyền đi", "Tăng dần"],
        "answer": "Chuyển hóa và truyền đi",
        "explanation": "Đây là nội dung định luật bảo toàn năng lượng."
    },
    {
        "question": "Sai số hệ thống là sai số:",
        "options": ["Do người đo bất cẩn", "Do dụng cụ đo", "Do điều kiện môi trường", "Do lấy số lẻ"],
        "answer": "Do dụng cụ đo",
        "explanation": "Sai số do dụng cụ đo không chuẩn gọi là sai số hệ thống."
    },
    {
        "question": "Cánh tay đòn của lực là khoảng cách từ tâm quay đến:",
        "options": ["Điểm đặt lực", "Trọng tâm vật", "Giá của lực", "Mép vật"],
        "answer": "Giá của lực",
        "explanation": "Định nghĩa cánh tay đòn là khoảng cách vuông góc từ trục quay tới giá của lực."
    },
    {
        "question": "Vật ở trạng thái cân bằng bền là vật có trọng tâm:",
        "options": ["Ở vị trí cao nhất", "Ở vị trí thấp nhất", "Nằm ngoài vật", "Không thay đổi"],
        "answer": "Ở vị trí thấp nhất",
        "explanation": "Cân bằng bền khi lệch khỏi vị trí đó trọng tâm sẽ cao lên."
    },
    {
        "question": "Điều kiện cân bằng của một vật chịu tác dụng của 2 lực là 2 lực đó phải:",
        "options": ["Cùng chiều", "Cùng độ lớn, ngược chiều, cùng giá", "Vuông góc", "Cùng điểm đặt"],
        "answer": "Cùng độ lớn, ngược chiều, cùng giá",
        "explanation": "Hai lực trực đối sẽ triệt tiêu tác dụng của nhau."
    },
    {
        "question": "Chuyển động tịnh tiến là chuyển động mà mọi điểm của vật:",
        "options": ["Chuyển động giống hệt nhau", "Chuyển động tròn", "Đứng yên", "Quay quanh trục"],
        "answer": "Chuyển động giống hệt nhau",
        "explanation": "Trong chuyển động tịnh tiến, mọi đường thẳng nối 2 điểm bất kỳ của vật luôn song song với chính nó."
    },
    {
        "question": "Gia tốc hướng tâm được tính bởi công thức:",
        "options": ["v^2/r", "v.r", "v/r^2", "v^2.r"],
        "answer": "v^2/r",
        "explanation": "Công thức tính gia tốc trong chuyển động tròn."
    },
    {
        "question": "Lực ma sát nghỉ có độ lớn:",
        "options": ["Bằng lực tác dụng song song mặt tiếp xúc", "Luôn bằng mu.N", "Luôn bằng trọng lực", "Bằng 0"],
        "answer": "Bằng lực tác dụng song song mặt tiếp xúc",
        "explanation": "Ma sát nghỉ cân bằng với lực kéo khi vật chưa trượt."
    },
    {
        "question": "Một người kéo vật trên sàn bằng lực F. Nếu góc giữa F và hướng dịch chuyển là 90 độ thì công của lực F bằng:",
        "options": ["F.s", "0", "F.s.0.5", "-F.s"],
        "answer": "0",
        "explanation": "Lực vuông góc với hướng chuyển động thì không sinh công."
    },
    {
        "question": "Thế năng đàn hồi của lò xo được tính theo công thức:",
        "options": ["1/2 k.x^2", "k.x", "m.g.h", "1/2 m.v^2"],
        "answer": "1/2 k.x^2",
        "explanation": "Năng lượng lưu trữ trong vật bị biến dạng đàn hồi."
    }
,
    # --- CHƯƠNG 1: MỞ ĐẦU & ĐỘNG HỌC (15 CÂU) ---
    {
        "question": "Đại lượng nào sau đây là đại lượng vectơ?",
        "options": ["Độ dịch chuyển", "Quãng đường", "Thời gian", "Tốc độ"],
        "answer": "Độ dịch chuyển",
        "explanation": "Độ dịch chuyển xác định cả độ lớn và hướng, nên là đại lượng vectơ."
    },
    {
        "question": "Đơn vị đo vận tốc trong hệ SI là:",
        "options": ["m/s", "km/h", "cm/s", "m.s"],
        "answer": "m/s",
        "explanation": "Mét trên giây (m/s) là đơn vị chuẩn của vận tốc."
    },
    {
        "question": "Tốc độ trung bình được tính bằng công thức:",
        "options": ["v = s / t", "v = d / t", "v = a * t", "v = s * t"],
        "answer": "v = s / t",
        "explanation": "Tốc độ trung bình bằng quãng đường chia cho thời gian chuyển động."
    },
    {
        "question": "Chuyển động thẳng biến đổi đều là chuyển động có:",
        "options": ["Gia tốc không đổi", "Vận tốc không đổi", "Quỹ đạo là đường cong", "Tốc độ không đổi"],
        "answer": "Gia tốc không đổi",
        "explanation": "Đặc điểm của chuyển động thẳng biến đổi đều là gia tốc là hằng số."
    },
    {
        "question": "Công thức tính gia tốc là:",
        "options": ["a = (v - v0) / t", "a = v / t^2", "a = s / t", "a = v * t"],
        "answer": "a = (v - v0) / t",
        "explanation": "Gia tốc đặc trưng cho sự biến thiên của vận tốc theo thời gian."
    },
    {
        "question": "Trong chuyển động thẳng nhanh dần đều, vectơ gia tốc và vectơ vận tốc:",
        "options": ["Cùng chiều", "Ngược chiều", "Vuông góc", "Hợp với nhau góc 45 độ"],
        "answer": "Cùng chiều",
        "explanation": "Nhanh dần đều thì tích a.v > 0, nên a và v cùng chiều."
    },
    {
        "question": "Rơi tự do là chuyển động:",
        "options": ["Thẳng nhanh dần đều", "Thẳng chậm dần đều", "Thẳng đều", "Biến đổi phức tạp"],
        "answer": "Thẳng nhanh dần đều",
        "explanation": "Rơi tự do có gia tốc g không đổi và vận tốc tăng dần theo thời gian."
    },
    {
        "question": "Gia tốc rơi tự do (g) thường được lấy giá trị xấp xỉ là:",
        "options": ["9,8 m/s2", "0 m/s2", "1,0 m/s2", "100 m/s2"],
        "answer": "9,8 m/s2",
        "explanation": "Giá trị tiêu chuẩn của g gần mặt đất là khoảng 9,8 m/s2 hoặc 10 m/s2."
    },
    {
        "question": "Một người đi từ A đến B dài 10km rồi quay lại A. Độ dịch chuyển của người đó là:",
        "options": ["0 km", "10 km", "20 km", "5 km"],
        "answer": "0 km",
        "explanation": "Điểm đầu và điểm cuối trùng nhau nên độ dịch chuyển bằng 0."
    },
    {
        "question": "Công thức tính quãng đường trong chuyển động thẳng đều là:",
        "options": ["s = v * t", "s = v / t", "s = 0.5 * a * t^2", "s = v0*t + 0.5*a*t^2"],
        "answer": "s = v * t",
        "explanation": "Trong chuyển động đều, vận tốc không đổi nên s = v.t."
    },
    {
        "question": "Chuyển động của vật nào sau đây là chuyển động tròn đều?",
        "options": ["Đầu kim đồng hồ", "Chiếc lá rơi", "Quả bóng ném ngang", "Ô tô đang hãm phanh"],
        "answer": "Đầu kim đồng hồ",
        "explanation": "Đầu kim đồng hồ vạch ra đường tròn và quay đều đặn."
    },
    {
        "question": "Đại lượng đặc trưng cho mức độ nhanh chậm của chuyển động tại một thời điểm là:",
        "options": ["Vận tốc tức thời", "Vận tốc trung bình", "Gia tốc", "Quãng đường"],
        "answer": "Vận tốc tức thời",
        "explanation": "Vận tốc tức thời cho biết trạng thái chuyển động tại thời điểm đó."
    },
    {
        "question": "Đồ thị vận tốc - thời gian của chuyển động thẳng đều là một đường thẳng:",
        "options": ["Song song với trục thời gian", "Đi qua gốc tọa độ", "Dốc lên phía trên", "Dốc xuống phía dưới"],
        "answer": "Song song với trục thời gian",
        "explanation": "Vì vận tốc không đổi theo thời gian."
    },
    {
        "question": "Khi đo một đại lượng vật lí, sai số ngẫu nhiên có thể giảm bớt bằng cách:",
        "options": ["Đo nhiều lần", "Dùng dụng cụ đắt tiền", "Thay đổi người đo", "Cẩn thận hơn"],
        "answer": "Đo nhiều lần",
        "explanation": "Lấy trung bình cộng nhiều lần đo giúp giảm sai số ngẫu nhiên."
    },
    {
        "question": "Biển báo 'Cấm đi ngược chiều' thuộc loại biển báo nào?",
        "options": ["Biển báo cấm", "Biển báo nguy hiểm", "Biển chỉ dẫn", "Biển hiệu lệnh"],
        "answer": "Biển báo cấm",
        "explanation": "Đây là biển báo quy định các hành vi không được phép."
    },

    # --- CHƯƠNG 2: ĐỘNG LỰC HỌC (15 CÂU) ---
    {
        "question": "Theo định luật I Newton, một vật đang đứng yên mà không chịu tác dụng của lực nào thì:",
        "options": ["Tiếp tục đứng yên", "Chuyển động thẳng đều", "Chuyển động nhanh dần", "Chuyển động chậm dần"],
        "answer": "Tiếp tục đứng yên",
        "explanation": "Vật sẽ giữ nguyên trạng thái đứng yên nếu không có ngoại lực tác động."
    },
    {
        "question": "Đại lượng đặc trưng cho mức độ quán tính của vật là:",
        "options": ["Khối lượng", "Vận tốc", "Lực", "Gia tốc"],
        "answer": "Khối lượng",
        "explanation": "Khối lượng càng lớn thì vật càng khó thay đổi vận tốc, tức quán tính càng lớn."
    },
    {
        "question": "Công thức của định luật II Newton là:",
        "options": ["F = m * a", "F = m / a", "a = m * F", "m = F * a"],
        "answer": "F = m * a",
        "explanation": "Lực tác dụng lên vật bằng tích khối lượng và gia tốc."
    },
    {
        "question": "Đơn vị của lực trong hệ SI là:",
        "options": ["Newton (N)", "Kilogam (kg)", "Met (m)", "Joule (J)"],
        "answer": "Newton (N)",
        "explanation": "Lực được đo bằng đơn vị Newton."
    },
    {
        "question": "Cặp lực và phản lực trong định luật III Newton có đặc điểm:",
        "options": ["Cùng giá, ngược chiều", "Cùng giá, cùng chiều", "Khác giá, ngược chiều", "Cùng điểm đặt"],
        "answer": "Cùng giá, ngược chiều",
        "explanation": "Hai lực này trực đối, đặt vào hai vật khác nhau."
    },
    {
        "question": "Trọng lượng của một vật được tính bằng công thức:",
        "options": ["P = m * g", "P = m / g", "P = g / m", "P = m + g"],
        "answer": "P = m * g",
        "explanation": "Trọng lượng là độ lớn của trọng lực tác dụng lên vật."
    },
    {
        "question": "Lực ma sát trượt xuất hiện khi:",
        "options": ["Vật trượt trên bề mặt vật khác", "Vật đứng yên", "Vật lăn", "Vật rơi trong không khí"],
        "answer": "Vật trượt trên bề mặt vật khác",
        "explanation": "Lực này cản trở chuyển động trượt của vật."
    },
    {
        "question": "Hệ số ma sát trượt:",
        "options": ["Không có đơn vị", "Đơn vị là Newton", "Đơn vị là m/s", "Đơn vị là kg"],
        "answer": "Không có đơn vị",
        "explanation": "Hệ số ma sát là tỉ số giữa lực ma sát và áp lực nên không có đơn vị."
    },
    {
        "question": "Lực đẩy Archimedes tác dụng lên vật nhúng trong chất lỏng có chiều:",
        "options": ["Thẳng đứng hướng lên", "Thẳng đứng hướng xuống", "Nằm ngang", "Xiên góc"],
        "answer": "Thẳng đứng hướng lên",
        "explanation": "Chất lỏng đẩy vật từ dưới lên trên."
    },
    {
        "question": "Lực đàn hồi của lò xo xuất hiện khi lò xo bị:",
        "options": ["Biến dạng", "Giữ nguyên hình dạng", "Đứng yên", "Di chuyển"],
        "answer": "Biến dạng",
        "explanation": "Lực đàn hồi xuất hiện để chống lại nguyên nhân gây biến dạng."
    },
    {
        "question": "Định luật Hooke (Húc) áp dụng cho lò xo trong giới hạn đàn hồi là:",
        "options": ["F = k * |delta l|", "F = k / |delta l|", "F = m * g", "F = p * S"],
        "answer": "F = k * |delta l|",
        "explanation": "Lực đàn hồi tỉ lệ thuận với độ biến dạng của lò xo."
    },
    {
        "question": "Một vật có khối lượng 2kg, gia tốc 2m/s2 thì lực tác dụng là:",
        "options": ["4 N", "1 N", "0 N", "2 N"],
        "answer": "4 N",
        "explanation": "F = m.a = 2.2 = 4N."
    },
    {
        "question": "Lực tổng hợp của hai lực F1 và F2 cùng phương, cùng chiều là:",
        "options": ["F = F1 + F2", "F = F1 - F2", "F = sqrt(F1^2 + F2^2)", "F = 0"],
        "answer": "F = F1 + F2",
        "explanation": "Hai lực cùng chiều thì cộng độ lớn lại."
    },
    {
        "question": "Đại lượng vật lí đặc trưng cho tác dụng làm quay của lực là:",
        "options": ["Mômen lực", "Cánh tay đòn", "Lực", "Gia tốc góc"],
        "answer": "Mômen lực",
        "explanation": "Mômen lực M = F.d xác định khả năng làm quay."
    },
    {
        "question": "Điều kiện cân bằng của một vật có mặt chân đế là giá của trọng lực:",
        "options": ["Phải rơi vào mặt chân đế", "Nằm ngoài mặt chân đế", "Phải song song mặt chân đế", "Không quan trọng"],
        "answer": "Phải rơi vào mặt chân đế",
        "explanation": "Để vật đứng vững, đường thẳng đứng đi qua trọng tâm phải đi qua mặt chân đế."
    },

    # --- CHƯƠNG 3: NĂNG LƯỢNG - CÔNG - ĐỘNG LƯỢNG (20 CÂU) ---
    {
        "question": "Công của một lực được tính bằng công thức (khi lực song song hướng dịch chuyển):",
        "options": ["A = F * s", "A = F / s", "A = m * g", "A = 0.5 * m * v^2"],
        "answer": "A = F * s",
        "explanation": "Công bằng tích của lực và quãng đường dịch chuyển."
    },
    {
        "question": "Đơn vị của công và năng lượng là:",
        "options": ["Joule (J)", "Watt (W)", "Newton (N)", "Pascal (Pa)"],
        "answer": "Joule (J)",
        "explanation": "Joule là đơn vị chuẩn đo công và các dạng năng lượng."
    },
    {
        "question": "Công suất là đại lượng đặc trưng cho:",
        "options": ["Tốc độ thực hiện công", "Khả năng sinh lực", "Mức độ biến dạng", "Quãng đường đi được"],
        "answer": "Tốc độ thực hiện công",
        "explanation": "Công suất P = A / t cho biết công thực hiện trong một đơn vị thời gian."
    },
    {
        "question": "Đơn vị của công suất là:",
        "options": ["Watt (W)", "Joule (J)", "Newton (N)", "Hertz (Hz)"],
        "answer": "Watt (W)",
        "explanation": "Watt (W) tương đương với Joule trên giây (J/s)."
    },
    {
        "question": "Động năng của một vật khối lượng m đang chuyển động với vận tốc v là:",
        "options": ["Wd = 0.5 * m * v^2", "Wd = m * v", "Wd = m * g * h", "Wd = 0.5 * k * x^2"],
        "answer": "Wd = 0.5 * m * v^2",
        "explanation": "Công thức tính năng lượng do chuyển động mà có."
    },
    {
        "question": "Thế năng trọng trường của một vật ở độ cao h được tính theo công thức:",
        "options": ["Wt = m * g * h", "Wt = 0.5 * m * v^2", "Wt = F * s", "Wt = m * v"],
        "answer": "Wt = m * g * h",
        "explanation": "Năng lượng tương tác giữa vật và Trái Đất."
    },
    {
        "question": "Cơ năng của một vật bằng:",
        "options": ["Tổng động năng và thế năng", "Hiệu động năng và thế năng", "Tích động năng và thế năng", "Động năng trừ thế năng"],
        "answer": "Tổng động năng và thế năng",
        "explanation": "W = Wd + Wt."
    },
    {
        "question": "Trong hệ kín và không có ma sát, đại lượng nào sau đây được bảo toàn?",
        "options": ["Cơ năng", "Vận tốc", "Gia tốc", "Quãng đường"],
        "answer": "Cơ năng",
        "explanation": "Cơ năng được bảo toàn nếu chỉ có lực thế tác dụng."
    },
    {
        "question": "Động lượng của một vật được tính bằng công thức:",
        "options": ["p = m * v", "p = m * a", "p = 0.5 * m * v^2", "p = F * t"],
        "answer": "p = m * v",
        "explanation": "Động lượng đặc trưng cho trạng thái chuyển động về mặt động lực học."
    },
    {
        "question": "Đơn vị của động lượng là:",
        "options": ["kg.m/s", "N.m", "J.s", "kg.m/s2"],
        "answer": "kg.m/s",
        "explanation": "Khối lượng (kg) nhân vận tốc (m/s)."
    },
    {
        "question": "Hệ thức của định luật bảo toàn động lượng cho hệ kín hai vật là:",
        "options": ["m1.v1 + m2.v2 = m1.v1' + m2.v2'", "m1.v1 = m2.v2", "p1 + p2 = 0", "F.t = m.v"],
        "answer": "m1.v1 + m2.v2 = m1.v1' + m2.v2'",
        "explanation": "Tổng động lượng trước và sau va chạm của hệ kín là không đổi."
    },
    {
        "question": "Va chạm mềm là va chạm mà sau đó hai vật:",
        "options": ["Dính vào nhau và chuyển động cùng vận tốc", "Nảy ra xa nhau", "Dừng lại ngay lập tức", "Biến mất"],
        "answer": "Dính vào nhau và chuyển động cùng vận tốc",
        "explanation": "Đặc điểm của va chạm không đàn hồi hoàn toàn."
    },
    {
        "question": "Hiệu suất của một máy được tính bằng tỉ số giữa:",
        "options": ["Công có ích và công toàn phần", "Công toàn phần và công có ích", "Lực và quãng đường", "Năng lượng và thời gian"],
        "answer": "Công có ích và công toàn phần",
        "explanation": "H = (A_ich / A_tp) * 100%."
    },
    {
        "question": "Tốc độ góc trong chuyển động tròn đều có đơn vị là:",
        "options": ["rad/s", "m/s", "vòng/phút", "độ/s"],
        "answer": "rad/s",
        "explanation": "Radian trên giây là đơn vị chuẩn của tốc độ góc."
    },
    {
        "question": "Gia tốc hướng tâm trong chuyển động tròn đều có tác dụng:",
        "options": ["Làm thay đổi hướng của vận tốc", "Làm thay đổi độ lớn vận tốc", "Làm vật dừng lại", "Làm vật bay ra xa"],
        "answer": "Làm thay đổi hướng của vận tốc",
        "explanation": "Trong chuyển động tròn đều, v có độ lớn không đổi nhưng hướng luôn thay đổi."
    },
    {
        "question": "Lực hướng tâm là:",
        "options": ["Hợp lực tác dụng lên vật gây ra gia tốc hướng tâm", "Một loại lực mới", "Lực đẩy vật ra khỏi quỹ đạo", "Lực ma sát nghỉ"],
        "answer": "Hợp lực tác dụng lên vật gây ra gia tốc hướng tâm",
        "explanation": "Lực hướng tâm không phải loại lực mới, nó là tên gọi của hợp lực gây ra chuyển động tròn."
    },
    {
        "question": "Chu kỳ là:",
        "options": ["Thời gian vật đi hết một vòng", "Số vòng vật đi được trong 1 giây", "Quãng đường vật đi được trong 1 giây", "Góc vật quay được trong 1 giây"],
        "answer": "Thời gian vật đi hết một vòng",
        "explanation": "Định nghĩa chu kỳ T trong chuyển động tuần hoàn."
    },
    {
        "question": "Tần số là:",
        "options": ["Số vòng vật đi được trong 1 giây", "Thời gian vật đi được một vòng", "Tốc độ của vật", "Bán kính quỹ đạo"],
        "answer": "Số vòng vật đi được trong 1 giây",
        "explanation": "Tần số f = 1/T."
    },
    {
        "question": "Công thức liên hệ giữa tốc độ dài v và tốc độ góc omega là:",
        "options": ["v = omega * r", "v = omega / r", "omega = v * r", "v = omega^2 * r"],
        "answer": "v = omega * r",
        "explanation": "Mối quan hệ giữa các đại lượng trong chuyển động tròn."
    },
    {
        "question": "Một vật khối lượng 1kg có thế năng 10J tại độ cao h. Nếu lấy g = 10m/s2 thì h bằng:",
        "options": ["1 m", "10 m", "0,1 m", "2 m"],
        "answer": "1 m",
        "explanation": "h = Wt / (mg) = 10 / (1.10) = 1m."
    }
,
    {
        "question": "Một vật rơi tự do từ độ cao h. Trong giây cuối cùng, vật đi được quãng đường bằng 3/4 toàn bộ độ cao rơi. Lấy g = 10m/s2. Thời gian rơi của vật là:",
        "options": ["2 s", "1 s", "4 s", "3 s"],
        "answer": "2 s",
        "explanation": "Sử dụng công thức h = 0.5gt^2 và h - h(t-1) = 0.75h."
    },
    {
        "question": "Một canô đi từ bến A đến bến B xuôi dòng hết 2 giờ, đi ngược dòng hết 3 giờ. Nếu canô tắt máy trôi theo dòng nước từ A đến B thì hết bao nhiêu thời gian?",
        "options": ["12 giờ", "5 giờ", "6 giờ", "10 giờ"],
        "answer": "12 giờ",
        "explanation": "v_x = v_t + v_n; v_n = v_t - v_n. Giải hệ tìm v_n theo quãng đường AB."
    },
    {
        "question": "Vật chuyển động chậm dần đều, trong giây cuối cùng đi được 0,5m. Quãng đường vật đi được trong giây sát trước giây cuối là:",
        "options": ["1,5 m", "1,0 m", "2,0 m", "2,5 m"],
        "answer": "1,5 m",
        "explanation": "Sử dụng tính chất đối xứng của chuyển động chậm dần đều dừng lại và chuyển động nhanh dần đều."
    },
    {
        "question": "Một vật được ném ngang từ độ cao h với vận tốc v0. Tầm xa của vật là L. Nếu tăng v0 lên gấp đôi và giữ nguyên h thì tầm xa của vật sẽ là:",
        "options": ["2L", "4L", "L*sqrt(2)", "L/2"],
        "answer": "2L",
        "explanation": "Tầm xa L = v0 * sqrt(2h/g). L tỉ lệ thuận với v0."
    },
    {
        "question": "Từ một đỉnh tháp cao 80m, người ta ném một vật theo phương ngang với vận tốc 20m/s. Lấy g = 10m/s2. Vận tốc của vật khi chạm đất là:",
        "options": ["44,7 m/s", "40 m/s", "60 m/s", "20 m/s"],
        "answer": "44,7 m/s",
        "explanation": "v = sqrt(v0^2 + (gt)^2) với t = sqrt(2h/g) = 4s."
    },

    # --- ĐỘNG LỰC HỌC (ĐỊNH LUẬT NEWTON) ---
    {
        "question": "Một vật khối lượng 5kg được kéo lên sàn nghiêng góc 30 độ bằng lực F song song với mặt nghiêng. Hệ số ma sát là 0,1. Để vật chuyển động đều, F có độ lớn:",
        "options": ["29,33 N", "25 N", "4,33 N", "30,5 N"],
        "answer": "29,33 N",
        "explanation": "F = P*sin(alpha) + mu*P*cos(alpha)."
    },
    {
        "question": "Lực F truyền cho vật m1 gia tốc a1, truyền cho vật m2 gia tốc a2. Nếu lực F truyền cho vật có khối lượng M = m1 + m2 thì gia tốc là:",
        "options": ["(a1*a2)/(a1+a2)", "a1+a2", "sqrt(a1^2+a2^2)", "|a1-a2|"],
        "answer": "(a1*a2)/(a1+a2)",
        "explanation": "m1 = F/a1; m2 = F/a2. M = F/a -> 1/a = 1/a1 + 1/a2."
    },
    {
        "question": "Hai vật m1 = 1kg, m2 = 2kg nối bằng dây nhẹ qua ròng rọc cố định. Thả nhẹ cho hệ chuyển động. Gia tốc của hệ là (g = 10m/s2):",
        "options": ["3,33 m/s2", "5,0 m/s2", "1,5 m/s2", "10 m/s2"],
        "answer": "3,33 m/s2",
        "explanation": "a = (m2 - m1)g / (m1 + m2)."
    },
    {
        "question": "Một lò xo có độ cứng k, khi treo vật m thì giãn 4cm. Nếu cắt lò xo làm hai nửa bằng nhau rồi treo vật m vào một nửa đó thì lò xo giãn:",
        "options": ["2 cm", "4 cm", "8 cm", "1 cm"],
        "answer": "2 cm",
        "explanation": "Cắt đôi lò xo thì độ cứng tăng gấp đôi (k' = 2k). Delta l = mg/k."
    },
    {
        "question": "Lực hướng tâm tác dụng lên một vệ tinh nhân tạo đang bay quanh Trái Đất là:",
        "options": ["Lực hấp dẫn", "Lực đàn hồi", "Lực ma sát", "Lực đẩy Archimedes"],
        "answer": "Lực hấp dẫn",
        "explanation": "Lực hấp dẫn giữa Trái Đất và vệ tinh đóng vai trò lực hướng tâm."
    },

    # --- TỔNG HỢP CÔNG - NĂNG LƯỢNG ---
    {
        "question": "Một vật khối lượng 2kg rơi tự do từ độ cao 20m. Công của trọng lực thực hiện khi vật rơi chạm đất là:",
        "options": ["400 J", "200 J", "40 J", "800 J"],
        "answer": "400 J",
        "explanation": "A = mgh = 2 * 10 * 20 = 400 J."
    },
    {
        "question": "Ô tô công suất không đổi P, leo dốc với vận tốc v1, xuống dốc với vận tốc v2. Vận tốc ô tô trên đường bằng là:",
        "options": ["(2*v1*v2)/(v1+v2)", "sqrt(v1*v2)", "(v1+v2)/2", "v2-v1"],
        "answer": "(2*v1*v2)/(v1+v2)",
        "explanation": "Sử dụng điều kiện lực kéo và lực cản (giả thiết lực cản không đổi)."
    },
    {
        "question": "Một viên đạn khối lượng 10g bay với vận tốc 200m/s xuyên qua tấm gỗ dày 5cm. Sau khi xuyên qua, vận tốc còn 100m/s. Lực cản trung bình của gỗ là:",
        "options": ["3000 N", "1500 N", "300 N", "150 N"],
        "answer": "3000 N",
        "explanation": "Sử dụng định lý biến thiên động năng: 0.5m(v2^2 - v1^2) = -Fc * s."
    },
    {
        "question": "Thả một vật từ độ cao h. Tại đâu thì thế năng bằng 3 lần động năng?",
        "options": ["Ở độ cao 3h/4", "Ở độ cao h/4", "Ở độ cao h/2", "Ở độ cao 2h/3"],
        "answer": "Ở độ cao 3h/4",
        "explanation": "Wt = 3Wd -> W = Wt + Wd = 4/3 Wt. mgh_max = 4/3 mgh."
    },
    {
        "question": "Một con lắc đơn chiều dài l. Kéo lệch góc 60 độ rồi thả nhẹ. Vận tốc vật khi qua vị trí cân bằng là:",
        "options": ["sqrt(gl)", "sqrt(2gl)", "0,5*sqrt(gl)", "2*sqrt(gl)"],
        "answer": "sqrt(gl)",
        "explanation": "v = sqrt(2gl(1 - cos60))."
    },

    # --- ĐỘNG LƯỢNG - VA CHẠM ---
    {
        "question": "Vật m1 = 2kg chuyển động với v1 = 3m/s đến va chạm mềm với vật m2 = 1kg đang đứng yên. Vận tốc hệ sau va chạm là:",
        "options": ["2 m/s", "1,5 m/s", "1 m/s", "3 m/s"],
        "answer": "2 m/s",
        "explanation": "Bảo toàn động lượng: m1*v1 = (m1 + m2)V."
    },
    {
        "question": "Một khẩu súng khối lượng 4kg bắn ra viên đạn 20g với vận tốc 500m/s. Vận tốc giật lùi của súng là:",
        "options": ["2,5 m/s", "4 m/s", "5 m/s", "1,25 m/s"],
        "answer": "2,5 m/s",
        "explanation": "M*V + m*v = 0 (về độ lớn: V = mv/M)."
    },
    {
        "question": "Động lượng của một hệ cô lập là một đại lượng:",
        "options": ["Bảo toàn", "Biến thiên theo thời gian", "Luôn bằng 0", "Tỉ lệ thuận với bình phương vận tốc"],
        "answer": "Bảo toàn",
        "explanation": "Định luật bảo toàn động lượng cho hệ kín."
    },
    {
        "question": "Lực F tác dụng vào vật trong khoảng thời gian 0,2s làm động lượng biến thiên 4 kg.m/s. Độ lớn lực F là:",
        "options": ["20 N", "0,8 N", "40 N", "10 N"],
        "answer": "20 N",
        "explanation": "F * delta t = delta p."
    },
    {
        "question": "Một vật khối lượng 1kg có động năng 8J. Động lượng của vật có độ lớn:",
        "options": ["4 kg.m/s", "2 kg.m/s", "8 kg.m/s", "16 kg.m/s"],
        "answer": "4 kg.m/s",
        "explanation": "p = sqrt(2m*Wd) = sqrt(2*1*8) = 4."
    },

    # --- CHUYỂN ĐỘNG TRÒN - CÂN BẰNG ---
    {
        "question": "Một cánh quạt quay đều với tần số 300 vòng/phút. Tốc độ góc của cánh quạt là:",
        "options": ["10*pi rad/s", "5*pi rad/s", "300 rad/s", "50 rad/s"],
        "answer": "10*pi rad/s",
        "explanation": "omega = 2*pi*f = 2*pi*(300/60)."
    },
    {
        "question": "Điểm A nằm trên vành bánh xe, điểm B nằm trên trung điểm bán kính. Tỉ số tốc độ dài vA/vB là:",
        "options": ["2", "1", "0,5", "4"],
        "answer": "2",
        "explanation": "v = omega * r. Cùng bánh xe thì cùng omega, rA = 2*rB."
    },
    {
        "question": "Một vật nặng được buộc vào dây và quay tròn trong mặt phẳng đứng. Lực căng dây lớn nhất ở đâu?",
        "options": ["Vị trí thấp nhất", "Vị trí cao nhất", "Vị trí nằm ngang", "Mọi điểm như nhau"],
        "answer": "Vị trí thấp nhất",
        "explanation": "T = m*an + mg*cos(alpha). Tại điểm thấp nhất cos(alpha) lớn nhất."
    },
    {
        "question": "Một vật có khối lượng 10kg nằm yên trên sàn. Hệ số ma sát nghỉ là 0,4. Tác dụng lực nằm ngang 30N vào vật. Lực ma sát khi đó là:",
        "options": ["30 N", "40 N", "0 N", "10 N"],
        "answer": "30 N",
        "explanation": "F_kéo (30N) < F_ms_nghỉ_cực_đại (40N) nên vật đứng yên, F_ms = F_kéo."
    },
    {
        "question": "Ngẫu lực là hệ hai lực song song:",
        "options": ["Ngược chiều, cùng độ lớn, không cùng giá", "Cùng chiều, cùng độ lớn", "Ngược chiều, khác độ lớn", "Cùng giá, ngược chiều"],
        "answer": "Ngược chiều, cùng độ lớn, không cùng giá",
        "explanation": "Định nghĩa ngẫu lực."
    },

    # --- CÂU HỎI TỔNG HỢP VÀ THỰC TIỄN (25 CÂU CÒN LẠI) ---
    {
        "question": "Một vật khối lượng m trượt xuống mặt nghiêng chiều dài l, cao h. Công của lực ma sát trên cả đoạn đường là (hệ số ma sát mu):",
        "options": ["-mu*mg*l*cos(alpha)", "-mu*mg*h", "-mu*mg*l", "-mg*h"],
        "answer": "-mu*mg*l*cos(alpha)",
        "explanation": "A_ms = -F_ms * l = -mu*N*l = -mu*mg*cos(alpha)*l."
    },
    {
        "question": "Công suất của một lực được tính bằng biểu thức:",
        "options": ["P = F*v*cos(theta)", "P = F*s", "P = m*g*h", "P = 0,5*m*v^2"],
        "answer": "P = F*v*cos(theta)",
        "explanation": "P = A/t = (F*s*cos)/t = F*v*cos."
    },
    {
        "question": "Hai vệ tinh nhân tạo A và B bay quanh Trái Đất trên các quỹ đạo tròn bán kính rA = 2*rB. Tỉ số tốc độ dài vA/vB là:",
        "options": ["1/sqrt(2)", "1/2", "sqrt(2)", "2"],
        "answer": "1/sqrt(2)",
        "explanation": "v = sqrt(G*M/r). v tỉ lệ nghịch với căn r."
    },
    {
        "question": "Một người nhấc một vật 10kg lên cao 2m trong 2s. Công suất trung bình là:",
        "options": ["100 W", "200 W", "50 W", "20 W"],
        "answer": "100 W",
        "explanation": "P = mgh/t = 10*10*2/2 = 100."
    },
    {
        "question": "Trong các đại lượng sau, đại lượng nào là đại lượng vectơ?",
        "options": ["Động lượng", "Công", "Thế năng", "Động năng"],
        "answer": "Động lượng",
        "explanation": "p = m*v, v là vectơ nên p là vectơ."
    },
    {
        "question": "Một con lắc lò xo treo thẳng đứng. Tại vị trí cân bằng lò xo giãn 10cm. Kích thích vật dao động. Chu kỳ dao động là (g = pi^2 = 10):",
        "options": ["0,63 s", "0,2 s", "1 s", "2 s"],
        "answer": "0,63 s",
        "explanation": "T = 2*pi*sqrt(delta_l / g) = 2*pi*sqrt(0,1/10) = 0,2*pi."
    },
    {
        "question": "Nếu khối lượng của cả hai vật tăng gấp đôi và khoảng cách giữa chúng giảm một nửa thì lực hấp dẫn sẽ:",
        "options": ["Tăng 16 lần", "Tăng 8 lần", "Tăng 4 lần", "Không đổi"],
        "answer": "Tăng 16 lần",
        "explanation": "F = G*m1*m2/r^2. Tử tăng 4, mẫu giảm 4 -> Tăng 16."
    },
    {
        "question": "Hệ số ma sát giữa hai bề mặt phụ thuộc vào yếu tố nào?",
        "options": ["Bản chất và tình trạng bề mặt", "Diện tích tiếp xúc", "Vận tốc của vật", "Áp lực lên bề mặt"],
        "answer": "Bản chất và tình trạng bề mặt",
        "explanation": "Ma sát không phụ thuộc diện tích tiếp xúc (trong giới hạn bài học)."
    },
    {
        "question": "Một lò xo độ cứng 100 N/m bị nén 5cm. Thế năng đàn hồi của lò xo là:",
        "options": ["0,125 J", "1,25 J", "2,5 J", "0,25 J"],
        "answer": "0,125 J",
        "explanation": "Wt = 0,5 * k * x^2 = 0,5 * 100 * 0,05^2 = 0,125."
    },
    {
        "question": "Một ô tô đang chạy với vận tốc 10m/s thì tắt máy, hệ số ma sát lăn là 0,05. Quãng đường ô tô đi thêm được đến khi dừng là:",
        "options": ["100 m", "50 m", "200 m", "10 m"],
        "answer": "100 m",
        "explanation": "s = v0^2 / (2*mu*g) = 100 / (2*0,05*10) = 100."
    },
    {
        "question": "Chuyển động của vật nào dưới đây được coi là rơi tự do?",
        "options": ["Một viên bi chì rơi trong chân không", "Một chiếc lá rơi", "Một quả bóng tennis rơi", "Một vận động viên nhảy dù"],
        "answer": "Một viên bi chì rơi trong chân không",
        "explanation": "Rơi tự do là chuyển động chỉ dưới tác dụng của trọng lực."
    },
    {
        "question": "Đơn vị của mômen lực là:",
        "options": ["N.m", "N/m", "J.s", "kg.m/s"],
        "answer": "N.m",
        "explanation": "M = F * d (Lực * cánh tay đòn)."
    },
    {
        "question": "Một vật rơi từ độ cao 45m xuống đất. Lấy g = 10m/s2. Thời gian rơi là:",
        "options": ["3 s", "4,5 s", "9 s", "2 s"],
        "answer": "3 s",
        "explanation": "t = sqrt(2h/g) = sqrt(90/10) = 3."
    },
    {
        "question": "Vật m chuyển động tròn đều bán kính r, tốc độ dài v. Biểu thức lực hướng tâm là:",
        "options": ["F = m*v^2 / r", "F = m*v / r", "F = m*r / v^2", "F = m*v*r"],
        "answer": "F = m*v^2 / r",
        "explanation": "Công thức cơ bản của lực hướng tâm."
    },
    {
        "question": "Sai số hệ thống là sai số:",
        "options": ["Do đặc điểm cấu tạo dụng cụ", "Do người đo bất cẩn", "Do điều kiện môi trường thay đổi", "Có thể loại bỏ bằng cách đo nhiều lần"],
        "answer": "Do đặc điểm cấu tạo dụng cụ",
        "explanation": "Sai số hệ thống lặp lại như nhau ở mọi lần đo."
    },
    {
        "question": "Một vật trượt không vận tốc đầu từ đỉnh mặt phẳng nghiêng dài 5m, cao 3m. Bỏ qua ma sát. Vận tốc ở chân dốc là:",
        "options": ["7,75 m/s", "10 m/s", "6 m/s", "8 m/s"],
        "answer": "7,75 m/s",
        "explanation": "v = sqrt(2gh) = sqrt(2 * 9,8 * 3) approx 7,75 (Lấy g = 10 thì là 7,74)."
    },
    {
        "question": "Định luật I Newton xác định:",
        "options": ["Quán tính của vật", "Mối liên hệ lực và gia tốc", "Tương tác giữa hai vật", "Sự bảo toàn năng lượng"],
        "answer": "Quán tính của vật",
        "explanation": "Định luật I còn gọi là định luật quán tính."
    },
    {
        "question": "Một người kéo gàu nước 5kg từ giếng sâu 10m lên đều trong 20s. Công suất người đó là:",
        "options": ["25 W", "50 W", "10 W", "100 W"],
        "answer": "25 W",
        "explanation": "P = mgh/t = 5 * 10 * 10 / 20 = 25."
    },
    {
        "question": "Điều kiện cân bằng của một vật chịu tác dụng của ba lực không song song là:",
        "options": ["Ba lực đồng quy và hợp lực bằng 0", "Ba lực cùng độ lớn", "Ba lực song song nhau", "Ba lực vuông góc nhau"],
        "answer": "Ba lực đồng quy và hợp lực bằng 0",
        "explanation": "Quy tắc hợp lực và giá của lực."
    },
    {
        "question": "Gia tốc rơi tự do phụ thuộc vào:",
        "options": ["Vĩ độ địa lý và độ cao", "Khối lượng vật rơi", "Vận tốc vật rơi", "Hình dạng vật rơi"],
        "answer": "Vĩ độ địa lý và độ cao",
        "explanation": "g thay đổi theo vị trí trên Trái Đất."
    },
    {
        "question": "Chuyển động thẳng biến đổi đều có gia tốc:",
        "options": ["Không đổi theo thời gian", "Tăng dần theo thời gian", "Bằng 0", "Luôn dương"],
        "answer": "Không đổi theo thời gian",
        "explanation": "Định nghĩa chuyển động thẳng biến đổi đều."
    },
    {
        "question": "Công của lực ma sát nghỉ bằng:",
        "options": ["0", "Dương", "Âm", "Phụ thuộc vào quãng đường"],
        "answer": "0",
        "explanation": "Ma sát nghỉ không làm vật dịch chuyển đối với bề mặt nên công bằng 0."
    },
    {
        "question": "Một vật đang chuyển động với vận tốc v. Nếu khối lượng giảm một nửa và vận tốc tăng gấp đôi thì động năng sẽ:",
        "options": ["Tăng gấp đôi", "Không đổi", "Tăng 4 lần", "Giảm một nửa"],
        "answer": "Tăng gấp đôi",
        "explanation": "Wd = 0,5 * (m/2) * (2v)^2 = 0,5 * m/2 * 4v^2 = 2 * (0,5mv^2)."
    },
    {
        "question": "Khi một vật chuyển động từ độ cao h xuống mặt đất theo những con đường khác nhau thì công trọng lực:",
        "options": ["Như nhau trên mọi con đường", "Lớn nhất trên đường thẳng", "Phụ thuộc độ dài quãng đường", "Bằng 0"],
        "answer": "Như nhau trên mọi con đường",
        "explanation": "Trọng lực là lực thế, công chỉ phụ thuộc hiệu độ cao."
    },
    {
        "question": "Định luật III Newton nói lên tính chất gì của lực?",
        "options": ["Lực luôn xuất hiện thành từng cặp trực đối", "Lực là nguyên nhân gây gia tốc", "Lực làm vật biến dạng", "Lực tỉ lệ với khối lượng"],
        "answer": "Lực luôn xuất hiện thành từng cặp trực đối",
        "explanation": "Tương tác hai chiều: F_AB = -F_BA."
    }
]