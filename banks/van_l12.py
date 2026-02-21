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
    {
        "question": "Ai là tác giả của bản 'Tuyên ngôn Độc lập' (1945)?",
        "options": ["Hồ Chí Minh", "Phan Bội Châu", "Huỳnh Thúc Kháng", "Phạm Văn Đồng"],
        "answer": "Hồ Chí Minh",
        "explanation": "Bác Hồ soạn thảo và đọc bản Tuyên ngôn tại Quảng trường Ba Đình ngày 2/9/1945."
    },
    {
        "question": "Bài thơ 'Tây Tiến' của Quang Dũng gắn liền với đơn vị quân đội nào?",
        "options": ["Đoàn binh Tây Tiến", "Trung đoàn Thủ đô", "Sư đoàn 308", "Đoàn binh Nam Tiến"],
        "answer": "Đoàn binh Tây Tiến",
        "explanation": "Quang Dũng từng là đại đội trưởng của đoàn binh Tây Tiến."
    },
    {
        "question": "Địa danh nào sau đây xuất hiện trong bài thơ 'Tây Tiến'?",
        "options": ["Sài Khao, Mường Lát", "Đèo Ngang", "Sông Hương", "Núi Ngự"],
        "answer": "Sài Khao, Mường Lát",
        "explanation": "Câu thơ: 'Sài Khao sương lấp đoàn quân mỏi / Mường Lát hoa về trong đêm hơi'."
    },
    {
        "question": "Bài thơ 'Việt Bắc' của Tố Hữu được viết theo thể thơ nào?",
        "options": ["Lục bát", "Thơ 7 chữ", "Thơ 8 chữ", "Tự do"],
        "answer": "Lục bát",
        "explanation": "Đây là bài thơ lục bát dài, mang đậm tính dân tộc của Tố Hữu."
    },
    {
        "question": "Trong bài thơ 'Việt Bắc', cụm từ 'Mình - Ta' dùng để chỉ ai?",
        "options": [
            "Người cán bộ kháng chiến và người dân Việt Bắc",
            "Đôi lứa yêu nhau",
            "Tác giả và người bạn thân",
            "Quân đội và kẻ thù"
        ],
        "answer": "Người cán bộ kháng chiến và người dân Việt Bắc",
        "explanation": "Cách xưng hô 'mình - ta' dân dã thể hiện tình quân dân gắn bó."
    },
    {
        "question": "Đoạn trích 'Đất Nước' của Nguyễn Khoa Điềm nằm trong tác phẩm nào?",
        "options": ["Mặt đường khát vọng", "Gió Lào cát trắng", "Đất ngoại ô", "Ra trận"],
        "answer": "Mặt đường khát vọng",
        "explanation": "Đoạn trích thuộc chương V của trường ca 'Mặt đường khát vọng'."
    },
    {
        "question": "Nguyễn Khoa Điềm định nghĩa Đất Nước bắt đầu từ đâu?",
        "options": [
            "Từ những cái 'ngày xửa ngày xưa' mẹ thường hay kể",
            "Từ các cuộc chiến tranh",
            "Từ khi có vua Hùng",
            "Từ khi có bản đồ thế giới"
        ],
        "answer": "Từ những cái 'ngày xửa ngày xưa' mẹ thường hay kể",
        "explanation": "Tác giả nhìn nhận Đất Nước từ góc độ văn hóa, dân gian gần gũi."
    },
    {
        "question": "Bài thơ 'Sóng' của Xuân Quỳnh được sáng tác trong chuyến đi thực tế ở vùng biển nào?",
        "options": ["Diêm Điền (Thái Bình)", "Sầm Sơn (Thanh Hóa)", "Đồ Sơn (Hải Phòng)", "Nha Trang"],
        "answer": "Diêm Điền (Thái Bình)",
        "explanation": "Bài thơ ra đời năm 1967 tại vùng biển Diêm Điền."
    },
    {
        "question": "Hình tượng 'Sóng' trong bài thơ cùng tên là ẩn dụ cho nhân vật nào?",
        "options": ["Em (người phụ nữ đang yêu)", "Anh", "Thiên nhiên", "Thời gian"],
        "answer": "Em (người phụ nữ đang yêu)",
        "explanation": "Sóng và Em tuy hai mà một, cùng thể hiện khát vọng tình yêu."
    },
    {
        "question": "Ai là tác giả của tùy bút 'Người lái đò Sông Đà'?",
        "options": ["Nguyễn Tuân", "Hoàng Phủ Ngọc Tường", "Tô Hoài", "Kim Lân"],
        "answer": "Nguyễn Tuân",
        "explanation": "Tác phẩm thể hiện phong cách tài hoa, uyên bác của Nguyễn Tuân sau cách mạng."
    },
    {
        "question": "Con sông Đà được Nguyễn Tuân miêu tả với hai đặc điểm nổi bật nào?",
        "options": ["Hung bạo và Trữ tình", "Hiền hòa và Êm đềm", "Nhỏ bé và Giàu có", "Sâu và Rộng"],
        "answer": "Hung bạo và Trữ tình",
        "explanation": "Sông Đà vừa là 'kẻ thù số một' vừa là một tác phẩm nghệ thuật tuyệt mỹ."
    },
    {
        "question": "Tác phẩm 'Ai đã đặt tên cho dòng sông?' của Hoàng Phủ Ngọc Tường viết về dòng sông nào?",
        "options": ["Sông Hương", "Sông Đà", "Sông Hồng", "Sông Đuống"],
        "answer": "Sông Hương",
        "explanation": "Tác phẩm là lời ngợi ca vẻ đẹp của dòng sông gắn liền với cố đô Huế."
    },
    {
        "question": "Truyện ngắn 'Vợ chồng A Phủ' viết về cuộc sống của người dân ở vùng nào?",
        "options": ["Tây Bắc", "Việt Bắc", "Tây Nguyên", "Đồng bằng sông Cửu Long"],
        "answer": "Tây Bắc",
        "explanation": "Tô Hoài viết về số phận những người dân nghèo dưới ách thống trị của chúa đất miền núi Tây Bắc."
    },
    {
        "question": "Nhân vật Mị trong 'Vợ chồng A Phủ' có tài năng gì?",
        "options": ["Thổi lá giỏi như thổi sáo", "Hát hay", "Dệt vải nhanh", "Múa đẹp"],
        "answer": "Thổi lá giỏi như thổi sáo",
        "explanation": "Tiếng sáo/tiếng lá là chi tiết đánh thức tâm hồn yêu đời của Mị."
    },
    {
        "question": "Chi tiết 'Mị cắt dây trói cứu A Phủ' thể hiện điều gì?",
        "options": [
            "Sức sống tiềm tàng và sự tự giải phóng",
            "Sự sợ hãi quân lính",
            "Sự xúi giục của người khác",
            "Sự nhầm lẫn"
        ],
        "answer": "Sức sống tiềm tàng và sự tự giải phóng",
        "explanation": "Mị cứu người cũng chính là cứu lấy bản thân mình khỏi ách nô lệ."
    },
    {
        "question": "Ai là tác giả truyện ngắn 'Vợ nhặt'?",
        "options": ["Kim Lân", "Nam Cao", "Tô Hoài", "Bùi Hiển"],
        "answer": "Kim Lân",
        "explanation": "Kim Lân là nhà văn chuyên viết về nông thôn và người nông dân."
    },
    {
        "question": "Trong 'Vợ nhặt', Tràng đưa vợ về nhà bằng cách nào?",
        "options": ["Đi bộ, vợ theo sau", "Đi xe hoa", "Thuê kiệu", "Đi thuyền"],
        "answer": "Đi bộ, vợ theo sau",
        "explanation": "Một cảnh tượng vừa bi hài vừa xót xa trong ngày đói."
    },
    {
        "question": "Tác phẩm 'Chiếc thuyền ngoài xa' của Nguyễn Minh Châu thuộc giai đoạn nào?",
        "options": ["Văn học thời kỳ đổi mới (sau 1975)", "Văn học kháng chiến chống Pháp",
                    "Văn học kháng chiến chống Mỹ", "Văn học 1930-1945"],
        "answer": "Văn học thời kỳ đổi mới (sau 1975)",
        "explanation": "Tác phẩm ra đời năm 1983, mang tính tự vấn và chiêm nghiệm về cuộc đời."
    },
    {
        "question": "Nhân vật Phùng trong 'Chiếc thuyền ngoài xa' làm nghề gì?",
        "options": ["Nghệ sĩ nhiếp ảnh", "Họa sĩ", "Nhà văn", "Phóng viên báo chí"],
        "answer": "Nghệ sĩ nhiếp ảnh",
        "explanation": "Phùng đi thực tế để chụp một bức ảnh cho bộ lịch năm sau."
    },
    {
        "question": "Vở kịch 'Hồn Trương Ba, da hàng thịt' là của tác giả nào?",
        "options": ["Lưu Quang Vũ", "Nguyễn Huy Tưởng", "Học Phi", "Nguyễn Đình Thi"],
        "answer": "Lưu Quang Vũ",
        "explanation": "Lưu Quang Vũ là nhà soạn kịch tài hoa bậc nhất của văn học hiện đại."
    },
    {
        "question": "Bi kịch của Trương Ba trong 'Hồn Trương Ba, da hàng thịt' là gì?",
        "options": [
            "Phải sống nhờ thân xác kẻ khác, tâm hồn và thể xác không thống nhất",
            "Bị vợ bỏ rơi",
            "Bị Đế Thích lừa",
            "Không được đi đánh cờ"
        ],
        "answer": "Phải sống nhờ thân xác kẻ khác, tâm hồn và thể xác không thống nhất",
        "explanation": "Nỗi đau khổ khi phải sống trái với bản chất trong sạch của mình."
    },
    {
        "question": "Phong cách ngôn ngữ của bản 'Tuyên ngôn Độc lập' là gì?",
        "options": ["Chính luận", "Nghệ thuật", "Khoa học", "Sinh hoạt"],
        "answer": "Chính luận",
        "explanation": "Văn bản dùng để trình bày quan điểm chính trị, khẳng định quyền độc lập."
    },
    {
        "question": "Bài thơ 'Sóng' thuộc thể thơ nào?",
        "options": ["5 chữ", "7 chữ", "8 chữ", "Lục bát"],
        "answer": "5 chữ",
        "explanation": "Thể thơ 5 chữ gợi nhịp sóng biển và nhịp lòng trào dâng."
    },
    {
        "question": "Trong bài thơ 'Tây Tiến', tác giả dùng từ 'gục lên bao súng quên đời' để nói về điều gì?",
        "options": ["Sự hy sinh lẫm liệt của người lính", "Sự mệt mỏi", "Giấc ngủ trưa", "Sự hèn nhát"],
        "answer": "Sự hy sinh lẫm liệt của người lính",
        "explanation": "Cách nói giảm nói tránh về cái chết của người chiến sĩ."
    },
    {
        "question": "Tố Hữu được coi là lá cờ đầu của dòng văn học nào?",
        "options": ["Văn học cách mạng", "Văn học lãng mạn", "Văn học hiện thực", "Văn học phê phán"],
        "answer": "Văn học cách mạng",
        "explanation": "Thơ Tố Hữu luôn song hành với các chặng đường của cách mạng Việt Nam."
    },
    {
        "question": "Câu thơ 'Nhớ gì như nhớ người yêu' trong bài 'Việt Bắc' nói về điều gì?",
        "options": ["Nỗi nhớ cảnh và người Việt Bắc", "Nỗi nhớ người yêu cũ", "Nỗi nhớ Hà Nội", "Nỗi nhớ gia đình"],
        "answer": "Nỗi nhớ cảnh và người Việt Bắc",
        "explanation": "Sự gắn bó máu thịt giữa người cán bộ và chiến khu."
    },
    {
        "question": "Trong 'Người lái đò Sông Đà', Nguyễn Tuân ví sông Đà như một nhân vật có 'diện mạo và ...'?",
        "options": ["tâm địa", "sức mạnh", "vẻ đẹp", "hình thể"],
        "answer": "tâm địa",
        "explanation": "Nguyễn Tuân nhân hóa con sông như một sinh thể có tính cách hung bạo."
    },
    {
        "question": "Hoàng Phủ Ngọc Tường ví sông Hương như một 'người con gái ...'?",
        "options": ["Di-gan phóng khoáng và man dại", "Huế dịu dàng", "Kiêu kỳ", "Yếu đuối"],
        "answer": "Di-gan phóng khoáng và man dại",
        "explanation": "Đây là vẻ đẹp của sông Hương ở vùng thượng nguồn rừng già."
    },
    {
        "question": "Chi tiết 'bát cháo cám' trong 'Vợ nhặt' mang ý nghĩa gì?",
        "options": ["Sự khốn cùng của nạn đói và tình thân ấm áp", "Món ăn ngon nhất", "Sự giàu sang của nhà Tràng",
                    "Sự chê bai của người vợ"],
        "answer": "Sự khốn cùng của nạn đói và tình thân ấm áp",
        "explanation": "Trong cái đói, người ta vẫn dành cho nhau sự trân trọng qua 'chè khoán' (cháo cám)."
    },
    {
        "question": "Chủ đề chính của bài thơ 'Đất Nước' (Nguyễn Khoa Điềm) là gì?",
        "options": ["Đất Nước của Nhân dân", "Đất Nước của các vị vua", "Vẻ đẹp thiên nhiên", "Tình yêu lứa đôi"],
        "answer": "Đất Nước của Nhân dân",
        "explanation": "Tư tưởng cốt lõi: Nhân dân là người làm nên Đất Nước."
    },
    {
        "question": "Trong 'Vợ chồng A Phủ', Mị bị bắt làm 'con dâu gạt nợ' cho nhà ai?",
        "options": ["Thống lý Pá Tra", "Bá Kiến", "Học Phi", "Đội Tảo"],
        "answer": "Thống lý Pá Tra",
        "explanation": "Gia đình thống lý dùng cường quyền và thần quyền để áp bức Mị."
    },
    {
        "question": "Phân đoạn 'Sông Hương ở trong lòng thành phố Huế' mang vẻ đẹp gì?",
        "options": ["Yên tĩnh, điệu Slow tình tứ", "Dữ dội, ồn ào", "Hùng vĩ", "Khô cằn"],
        "answer": "Yên tĩnh, điệu Slow tình tứ",
        "explanation": "Khi về đến Huế, sông Hương chảy chậm như một điệu nhạc dành riêng cho thành phố."
    },
    {
        "question": "Từ 'mình' trong câu 'Mình về mình có nhớ ta' dùng để chỉ ai?",
        "options": ["Người ra đi (cán bộ)", "Người ở lại (dân bản)", "Tác giả", "Kẻ thù"],
        "answer": "Người ra đi (cán bộ)",
        "explanation": "Đây là câu hỏi của người dân Việt Bắc dành cho cán bộ về xuôi."
    },
    {
        "question": "Hình ảnh 'Súng ngửi trời' trong Tây Tiến thể hiện điều gì?",
        "options": ["Độ cao của núi và tính cách tinh nghịch của người lính", "Sự nguy hiểm", "Vẻ đẹp của vũ khí",
                    "Thời tiết lạnh"],
        "answer": "Độ cao của núi và tính cách tinh nghịch của người lính",
        "explanation": "Cách dùng từ 'ngửi trời' rất lãng mạn, lạc quan của Quang Dũng."
    },
    {
        "question": "Văn học Việt Nam từ 1945 - 1975 chủ yếu vận động theo hướng nào?",
        "options": ["Cách mạng hóa và hướng về đại chúng", "Cá nhân hóa", "Nghệ thuật vị nghệ thuật", "Tây phương hóa"],
        "answer": "Cách mạng hóa và hướng về đại chúng",
        "explanation": "Văn học giai đoạn này phục vụ nhiệm vụ chính trị và kháng chiến."
    },
    {
        "question": "Trong 'Chiếc thuyền ngoài xa', hành động của người đàn bà hàng chài ở tòa án huyện thể hiện điều gì?",
        "options": ["Sự cam chịu và đức hy sinh vì con", "Sự ngu ngốc", "Sự sợ hãi luật pháp", "Sự giàu có"],
        "answer": "Sự cam chịu và đức hy sinh vì con",
        "explanation": "Bà không bỏ chồng vì muốn có người cùng nuôi đàn con trên thuyền."
    },
    {
        "question": "Thể thơ 'Tây Tiến' là thể thơ gì?",
        "options": ["7 chữ", "8 chữ", "Lục bát", "Tự do"],
        "answer": "7 chữ",
        "explanation": "Thơ 7 chữ tạo âm hưởng trang trọng, hào hùng."
    },
    {
        "question": "Tác phẩm 'Ai đã đặt tên cho dòng sông?' thuộc thể loại gì?",
        "options": ["Bút ký", "Truyện ngắn", "Tiểu thuyết", "Kịch"],
        "answer": "Bút ký",
        "explanation": "Đây là một trong những bài bút ký hay nhất về sông Hương."
    },
    {
        "question": "Cụm từ 'Đám mây đi qua - Tình yêu ở lại' thường được gắn với tác giả nào?",
        "options": ["Lưu Quang Vũ", "Xuân Quỳnh", "Bằng Việt", "Thanh Thảo"],
        "answer": "Lưu Quang Vũ",
        "explanation": "Lưu Quang Vũ nổi tiếng với những vần thơ và kịch đầy tính nhân văn."
    },
    {
        "question": "Trong 'Người lái đò Sông Đà', Nguyễn Tuân miêu tả 'Thạch trận' sông Đà có mấy vòng vây?",
        "options": ["3 vòng", "2 vòng", "5 vòng", "1 vòng"],
        "answer": "3 vòng",
        "explanation": "Ông lái đò phải vượt qua 3 vòng trùng vi thạch trận đầy nguy hiểm."
    },
    {
        "question": "Ai được mệnh danh là 'Nhà thơ của tình yêu'?",
        "options": ["Xuân Quỳnh", "Tố Hữu", "Nguyễn Khoa Điềm", "Quang Dũng"],
        "answer": "Xuân Quỳnh",
        "explanation": "Xuân Quỳnh nổi tiếng với tiếng thơ nồng nàn, đôn hậu về tình yêu."
    },
    {
        "question": "Bản chất của phong cách nghệ thuật Hoàng Phủ Ngọc Tường là gì?",
        "options": ["Trí tuệ và chất thơ hòa quyện", "Góc cạnh, gồ ghề", "Châm biếm trào phúng", "Đơn giản, mộc mạc"],
        "answer": "Trí tuệ và chất thơ hòa quyện",
        "explanation": "Bút ký của ông giàu kiến thức văn hóa, lịch sử nhưng rất mượt mà."
    },
    {
        "question": "Trong 'Vợ nhặt', Tràng gặp vợ lần đầu ở đâu?",
        "options": ["Dốc tỉnh (khi đang đẩy xe thóc)", "Ở chợ", "Ở bến xe", "Ở cổng làng"],
        "answer": "Dốc tỉnh (khi đang đẩy xe thóc)",
        "explanation": "Tràng hò một câu cho đỡ mệt và Thị ra đẩy xe giúp."
    },
    {
        "question": "Sự kiện 'Bát xát ném vào sọt rác' trong 'Tây Tiến' chỉ điều gì?",
        "options": ["Sự khắc nghiệt của bệnh sốt rét rừng", "Sự lãng phí thức ăn", "Dọn dẹp chiến trường",
                    "Đánh rơi đồ dùng"],
        "answer": "Sự khắc nghiệt của bệnh sốt rét rừng",
        "explanation": "Gợi sự rụng rơi, hy sinh lặng lẽ vì bệnh tật nơi rừng thiêng nước độc."
    },
    {
        "question": "Chủ đề 'Nghệ thuật không thể tách rời cuộc đời' thể hiện rõ nhất trong tác phẩm nào?",
        "options": ["Chiếc thuyền ngoài xa", "Tây Tiến", "Sóng", "Việt Bắc"],
        "answer": "Chiếc thuyền ngoài xa",
        "explanation": "Người nghệ sĩ cần cái nhìn đa chiều, không chỉ nhìn vẻ đẹp bề ngoài mà phải thấu hiểu nỗi đau bên trong."
    },
    {
        "question": "Trong bài thơ 'Đất Nước', tác giả nhắc đến 'Gậy tre, chông tre' gợi nhớ đến ai?",
        "options": ["Thánh Gióng", "Lê Lợi", "Quang Trung", "Nguyễn Trãi"],
        "answer": "Thánh Gióng",
        "explanation": "Gợi nhắc truyền thống đánh giặc cứu nước từ ngàn đời."
    },
    {
        "question": "Từ 'Dữ dội và dịu dàng / Ồn ào và lặng lẽ' miêu tả đối tượng nào?",
        "options": ["Sóng", "Gió", "Nắng", "Mưa"],
        "answer": "Sóng",
        "explanation": "Những trạng thái đối lập của sóng cũng là tâm trạng của người phụ nữ khi yêu."
    },
    {
        "question": "Tác phẩm 'Hồn Trương Ba, da hàng thịt' được viết dựa trên cốt truyện gì?",
        "options": ["Truyện dân gian", "Truyện cổ tích phương Tây", "Sự việc có thật", "Tiểu thuyết nước ngoài"],
        "answer": "Truyện dân gian",
        "explanation": "Lưu Quang Vũ đã thổi vào cốt truyện dân gian những ý nghĩa triết học hiện đại."
    },
    {
        "question": "Hình ảnh 'Mai Châu mùa em thơm nếp xôi' gợi cảm giác gì?",
        "options": ["Sự ấm cúng, tình nghĩa quân dân", "Cái đói", "Sự xa lạ", "Thời tiết nóng nực"],
        "answer": "Sự ấm cúng, tình nghĩa quân dân",
        "explanation": "Kỷ niệm đẹp về sự đón tiếp nồng hậu của người dân địa phương."
    },
    {
        "question": "Nhà văn nào được coi là 'Người suốt đời đi tìm cái Đẹp'?",
        "options": ["Nguyễn Tuân", "Hoàng Phủ Ngọc Tường", "Tô Hoài", "Xuân Diệu"],
        "answer": "Nguyễn Tuân",
        "explanation": "Quan niệm nghệ thuật của Nguyễn Tuân luôn hướng tới sự toàn thiện, toàn mỹ."
    }
,
    {
        "question": "Bài thơ 'Đàn ghi ta của Lor-ca' là của tác giả nào?",
        "options": ["Thanh Thảo", "Nguyễn Khoa Điềm", "Hữu Thỉnh", "Nguyễn Duy"],
        "answer": "Thanh Thảo",
        "explanation": "Thanh Thảo là nhà thơ luôn nỗ lực cách tân hình thức thơ ca Việt Nam."
    },
    {
        "question": "Hình ảnh 'tiếng đàn bọt nước' trong bài thơ của Thanh Thảo gợi tính chất gì?",
        "options": ["Sự mong manh, ngắn ngủi và tan biến", "Sự vĩnh cửu", "Âm thanh chói tai", "Sự vui nhộn"],
        "answer": "Sự mong manh, ngắn ngủi và tan biến",
        "explanation": "Gợi số phận ngắn ngủi của người nghệ sĩ tài hoa Lor-ca."
    },
    {
        "question": "Trong bài thơ 'Bác ơi!', Tố Hữu đã ví sự ra đi của Bác Hồ với hình ảnh nào?",
        "options": ["Đời tuôn nước mắt, trời tuôn mưa", "Một vì sao rụng", "Mùa xuân lặng lẽ", "Dòng sông ngừng chảy"],
        "answer": "Đời tuôn nước mắt, trời tuôn mưa",
        "explanation": "Câu thơ diễn tả nỗi đau xót vô hạn của toàn dân tộc khi Bác qua đời."
    },
    {
        "question": "Tác phẩm 'Một người Hà Nội' của Nguyễn Khải xoay quanh nhân vật chính nào?",
        "options": ["Bà Hiền", "Ông Giáo", "Nhân vật tôi", "Cô Nguyệt"],
        "answer": "Bà Hiền",
        "explanation": "Bà Hiền là 'hạt bụi vàng' tiêu biểu cho cốt cách, bản lĩnh của người Hà Nội."
    },
    {
        "question": "Trong bài thơ 'Đò Lèn', Nguyễn Duy đã nhớ về người thân nào của mình?",
        "options": ["Bà ngoại", "Mẹ", "Cha", "Ông nội"],
        "answer": "Bà ngoại",
        "explanation": "Bài thơ là sự ân hận muộn màng và tình yêu thương dành cho bà."
    },
    {
        "question": "Phong cách ngôn ngữ nào dùng trong các văn bản pháp luật, nghị định, thông tư?",
        "options": ["Hành chính", "Chính luận", "Khoa học", "Báo chí"],
        "answer": "Hành chính",
        "explanation": "Dùng trong giao tiếp giữa các cơ quan nhà nước hoặc cá nhân với nhà nước."
    },
    {
        "question": "Biện pháp tu từ nào sử dụng tên bộ phận để chỉ toàn thể?",
        "options": ["Hoán dụ", "Ẩn dụ", "So sánh", "Điệp ngữ"],
        "answer": "Hoán dụ",
        "explanation": "Ví dụ: 'Mười đầu ngón tay' để chỉ bàn tay hoặc người thợ."
    },
    {
        "question": "Trong văn bản 'Tuyên ngôn Độc lập', Bác Hồ đã trích dẫn bản Tuyên ngôn của những nước nào?",
        "options": ["Mỹ và Pháp", "Anh và Nga", "Mỹ và Nhật", "Pháp và Đức"],
        "answer": "Mỹ và Pháp",
        "explanation": "Dùng lẽ phải của thế giới để khẳng định quyền độc lập của Việt Nam."
    },
    {
        "question": "Địa danh 'Hùng vĩ của sông Đà' được Nguyễn Tuân so sánh như cái gì?",
        "options": ["Một công trình vĩ đại của thạch trận", "Một con đường bằng phẳng", "Một dải lụa", "Một bức tranh thủy mặc"],
        "answer": "Một công trình vĩ đại của thạch trận",
        "explanation": "Sông Đà có những vách đá chẹt lòng sông và thác dữ gầm réo."
    },
    {
        "question": "Câu thơ 'Tây Tiến đoàn binh không mọc tóc' chỉ điều gì thực tế?",
        "options": ["Hậu quả của bệnh sốt rét rừng", "Quân đội tự cạo đầu", "Một kiểu thời trang", "Bị kẻ thù cắt tóc"],
        "answer": "Hậu quả của bệnh sốt rét rừng",
        "explanation": "Căn bệnh sốt rét làm rụng tóc, nhưng Quang Dũng viết rất hào hùng."
    },
    {
        "question": "Tiếng 'Lila lila lila' trong bài thơ của Thanh Thảo mô phỏng điều gì?",
        "options": ["Tiếng đàn ghi ta", "Tiếng chim hót", "Tiếng bước chân", "Tiếng gió thổi"],
        "answer": "Tiếng đàn ghi ta",
        "explanation": "Sử dụng kỹ thuật mô phỏng âm thanh để tạo nhạc tính cho thơ."
    },
    {
        "question": "Đặc điểm của thể loại 'Kịch' là gì?",
        "options": ["Xây dựng thông qua hành động và đối thoại", "Chủ yếu là miêu tả phong cảnh", "Chỉ có lời kể của người dẫn truyện", "Dùng vần điệu làm chính"],
        "answer": "Xây dựng thông qua hành động và đối thoại",
        "explanation": "Xung đột kịch được bộc lộ qua lời thoại và hành động nhân vật."
    },
    {
        "question": "Trong 'Vợ chồng A Phủ', Mị thường ngồi quay sợi bên cạnh cái gì?",
        "options": ["Tảng đá trước cửa", "Bếp lửa", "Cửa sổ", "Gốc cây"],
        "answer": "Tảng đá trước cửa",
        "explanation": "Hình ảnh Mị cúi mặt, mặt buồn rười rượi bên tảng đá gợi sự câm lặng, cam chịu."
    },
    {
        "question": "Từ 'mặn nồng' trong 'Đất Nước' của Nguyễn Khoa Điềm gắn với hình ảnh nào?",
        "options": ["Gừng cay muối mặn", "Đường kính", "Mật ong", "Phù sa"],
        "answer": "Gừng cay muối mặn",
        "explanation": "Câu thơ: 'Tay cầm tay nồng cháy / Gừng cay muối mặn xin đừng quên nhau'."
    },
    {
        "question": "Ai là tác giả của truyện ngắn 'Những đứa con trong gia đình'?",
        "options": ["Nguyễn Thi", "Nguyễn Trung Thành", "Phan Tứ", "Anh Đức"],
        "answer": "Nguyễn Thi",
        "explanation": "Nguyễn Thi là nhà văn của người nông dân Nam Bộ bộ thời đánh Mỹ."
    },
    {
        "question": "Nhân vật Việt và Chiến trong truyện của Nguyễn Thi có thói quen gì?",
        "options": ["Tranh nhau đi đánh giặc", "Tranh nhau làm việc nhà", "Hay cãi nhau", "Thích đi câu cá"],
        "answer": "Tranh nhau đi đánh giặc",
        "explanation": "Thể hiện tinh thần yêu nước quyết liệt của tuổi trẻ miền Nam."
    },
    {
        "question": "Tác phẩm 'Rừng xà nu' của Nguyễn Trung Thành lấy bối cảnh ở đâu?",
        "options": ["Tây Nguyên", "Tây Bắc", "Nam Bộ", "Miền Trung"],
        "answer": "Tây Nguyên",
        "explanation": "Câu chuyện về dân làng Xô Man kiên cường đánh giặc."
    },
    {
        "question": "Cây xà nu trong tác phẩm cùng tên là biểu tượng cho điều gì?",
        "options": ["Sức sống bất diệt và khát vọng tự do của dân làng", "Một loài cây gỗ quý", "Sự chết chóc", "Sự khô cằn"],
        "answer": "Sức sống bất diệt và khát vọng tự do của dân làng",
        "explanation": "Cây xà nu cũng như người dân Tây Nguyên, lớp này ngã xuống lớp khác mọc lên."
    },
    {
        "question": "Trong 'Chiếc thuyền ngoài xa', bức ảnh nghệ thuật được chọn là bức ảnh màu gì?",
        "options": ["Đen trắng", "Màu rực rỡ", "Màu xanh nước biển", "Màu đỏ rực"],
        "answer": "Đen trắng",
        "explanation": "Dù là đen trắng nhưng nghệ sĩ vẫn thấy hiện lên cái màu hồng hồng của ánh sương mai."
    },
    {
        "question": "Mục đích chính của thao tác lập luận 'Bác bỏ' là gì?",
        "options": ["Phủ nhận ý kiến sai để khẳng định ý kiến đúng", "Chứng minh sự việc", "Giải thích khái niệm", "So sánh hai đối tượng"],
        "answer": "Phủ nhận ý kiến sai để khẳng định ý kiến đúng",
        "explanation": "Dùng lý lẽ và dẫn chứng để chỉ ra chỗ sai của đối phương."
    },
    {
        "question": "Câu thơ 'Con sóng dưới lòng sâu / Con sóng trên mặt nước' sử dụng biện pháp tu từ nào?",
        "options": ["Đối lập và Điệp ngữ", "So sánh", "Liệt kê", "Nói quá"],
        "answer": "Đối lập và Điệp ngữ",
        "explanation": "Thể hiện các tầng sâu tâm trạng khác nhau của người phụ nữ khi yêu."
    },
    {
        "question": "Nhan đề 'Ai đã đặt tên cho dòng sông?' là một câu hỏi mang tính chất gì?",
        "options": ["Sự ngợi ca và tìm kiếm vẻ đẹp nguồn cội", "Sự thắc mắc về lịch sử", "Sự trách móc", "Yêu cầu cung cấp thông tin"],
        "answer": "Sự ngợi ca và tìm kiếm vẻ đẹp nguồn cội",
        "explanation": "Câu hỏi dẫn dắt người đọc vào hành trình khám phá vẻ đẹp dòng sông."
    },
    {
        "question": "Trong 'Vợ nhặt', tại sao người dân làng Vũ Đại lại ngạc nhiên khi thấy Tràng đi cùng một người đàn bà?",
        "options": ["Vì thời buổi đói khát, nuôi thân chẳng xong lại còn đèo bòng", "Vì Tràng rất giàu", "Vì người đàn bà đó quá đẹp", "Vì Tràng vốn ghét phụ nữ"],
        "answer": "Vì thời buổi đói khát, nuôi thân chẳng xong lại còn đèo bòng",
        "explanation": "Cái đói làm cho việc lấy vợ trở nên vừa kỳ lạ vừa xót xa."
    },
    {
        "question": "Hình ảnh 'Đầu súng trăng treo' gợi lên sự kết hợp giữa điều gì?",
        "options": ["Chiến tranh và Hòa bình", "Đêm và Ngày", "Đất và Trời", "Ta và Địch"],
        "answer": "Chiến tranh và Hòa bình",
        "explanation": "Một hình ảnh thơ mộng, mang đậm tinh thần lãng mạn cách mạng."
    },
    {
        "question": "Nghĩa của từ 'Sử thi' trong văn học là gì?",
        "options": ["Tác phẩm kể về những sự kiện trọng đại của cộng đồng", "Bài thơ tình ngắn", "Truyện cười", "Kịch nói"],
        "answer": "Tác phẩm kể về những sự kiện trọng đại của cộng đồng",
        "explanation": "Văn học 45-75 mang đậm tính sử thi vì nói về vận mệnh dân tộc."
    },
    {
        "question": "Từ 'Lũy tre', 'Con đê', 'Mái đình' là những hình ảnh quen thuộc của vùng nào?",
        "options": ["Nông thôn Đồng bằng Bắc Bộ", "Miền núi", "Thành thị", "Vùng biển"],
        "answer": "Nông thôn Đồng bằng Bắc Bộ",
        "explanation": "Đây là những biểu tượng văn hóa làng quê Việt Nam."
    },
    {
        "question": "Trong 'Hồn Trương Ba, da hàng thịt', Trương Ba đã quyết định điều gì cuối cùng?",
        "options": ["Chết hẳn để giải thoát cho mình và người thân", "Tiếp tục sống trong xác hàng thịt", "Nhập vào xác cu Tị", "Đi kiện trời"],
        "answer": "Chết hẳn để giải thoát cho mình và người thân",
        "explanation": "Sự lựa chọn bảo toàn nhân cách trong sáng của Trương Ba."
    },
    {
        "question": "Nhà văn nào được mệnh danh là 'Người thư ký của thời đại'?",
        "options": ["Balzac", "Nam Cao", "Thạch Lam", "Nguyễn Tuân"],
        "answer": "Balzac",
        "explanation": "Đây là nhận định về nhà văn hiện thực vĩ đại người Pháp."
    },
    {
        "question": "Phép liên kết nào dùng các từ như 'Tuy nhiên', 'Nhưng', 'Vả lại'?",
        "options": ["Phép nối", "Phép lặp", "Phép thế", "Phép đồng nghĩa"],
        "answer": "Phép nối",
        "explanation": "Dùng quan hệ từ để nối các câu, các đoạn văn."
    },
    {
        "question": "Trong bài thơ 'Đất Nước', Nguyễn Khoa Điềm nhắc đến 'Hòn Trống Mái' để nói về điều gì?",
        "options": ["Sự hóa thân của tình yêu lứa đôi vào hình hài đất nước", "Danh lam thắng cảnh đẹp", "Sự tích loài chim", "Một món ăn"],
        "answer": "Sự hóa thân của tình yêu lứa đôi vào hình hài đất nước",
        "explanation": "Đất nước hiện hình qua những trải nghiệm và tình cảm của nhân dân."
    },
    {
        "question": "Nhân vật Tnú trong 'Rừng xà nu' bị giặc đốt mấy đầu ngón tay?",
        "options": ["10 đầu ngón tay", "5 đầu ngón tay", "2 đầu ngón tay", "Không bị đốt"],
        "answer": "10 đầu ngón tay",
        "explanation": "Giặc đốt 10 đầu ngón tay Tnú bằng nhựa xà nu để uy hiếp tinh thần dân làng."
    },
    {
        "question": "Câu thơ 'Em ơi em Đất Nước là máu xương của mình' thể hiện thái độ gì?",
        "options": ["Sự trân trọng và ý thức trách nhiệm", "Sự sợ hãi", "Sự thờ ơ", "Sự kiêu ngạo"],
        "answer": "Sự trân trọng và ý thức trách nhiệm",
        "explanation": "Đất nước không ở đâu xa mà kết tinh trong mỗi con người."
    },
    {
        "question": "Phong cách ngôn ngữ nghệ thuật không có đặc điểm nào sau đây?",
        "options": ["Tính khuôn mẫu, máy móc", "Tính hình tượng", "Tính truyền cảm", "Tính cá thể hóa"],
        "answer": "Tính khuôn mẫu, máy móc",
        "explanation": "Nghệ thuật đòi hỏi sự sáng tạo và độc đáo, không được máy móc."
    },
    {
        "question": "Trong 'Người lái đò Sông Đà', Nguyễn Tuân gọi người lái đò là gì?",
        "options": ["Tay lái ra hoa", "Người lính già", "Thợ thuyền", "Kẻ lãng du"],
        "answer": "Tay lái ra hoa",
        "explanation": "Ngợi ca sự tài hoa, nghệ thuật trong công việc lao động nguy hiểm."
    },
    {
        "question": "Tác giả của bài thơ 'Sóng' thuộc thế hệ nhà thơ nào?",
        "options": ["Thời kỳ kháng chiến chống Mỹ", "Thời kỳ Thơ mới", "Thời kỳ đổi mới", "Thời kỳ kháng chiến chống Pháp"],
        "answer": "Thời kỳ kháng chiến chống Mỹ",
        "explanation": "Xuân Quỳnh là gương mặt tiêu biểu của thi ca thời đánh Mỹ."
    },
    {
        "question": "Nghĩa của từ 'Tài hoa' là gì?",
        "options": ["Người có tài năng nghệ thuật và cốt cách thanh cao", "Người chỉ có sức mạnh cơ bắp", "Người giàu có", "Người nói nhiều"],
        "answer": "Người có tài năng nghệ thuật và cốt cách thanh cao",
        "explanation": "Thường dùng để chỉ những người làm nghệ thuật có phong cách riêng."
    },
    {
        "question": "Đoạn trích 'Vĩnh biệt Cửu Trùng Đài' thuộc hồi thứ mấy của vở kịch 'Vũ Như Tô'?",
        "options": ["Hồi thứ V", "Hồi thứ I", "Hồi thứ III", "Hồi thứ IV"],
        "answer": "Hồi thứ V",
        "explanation": "Đây là hồi cuối, giải quyết toàn bộ xung đột của vở kịch."
    },
    {
        "question": "Trong 'Một người Hà Nội', bà Hiền quyết định không nuôi người giúp việc nữa khi nào?",
        "options": ["Khi chế độ bao cấp bắt đầu", "Khi bà hết tiền", "Khi con cái đã lớn", "Khi bà đi di cư"],
        "answer": "Khi chế độ bao cấp bắt đầu",
        "explanation": "Sự thích ứng khôn ngoan của một người phụ nữ sắc sảo để giữ gìn nếp nhà."
    },
    {
        "question": "Hình ảnh 'Bát cơm sẻ nửa, chăn lùi đắp chung' nói về điều gì?",
        "options": ["Tình đồng chí, đồng đội gắn bó", "Sự nghèo đói", "Sự tiết kiệm", "Lối sống tập thể"],
        "answer": "Tình đồng chí, đồng đội gắn bó",
        "explanation": "Sự chia ngọt sẻ bùi giữa những người lính cách mạng."
    },
    {
        "question": "Điểm nhìn trần thuật trong truyện 'Vợ nhặt' là của ai?",
        "options": ["Tác giả (người kể chuyện ngôi thứ ba)", "Nhân vật Tràng", "Nhân vật Thị", "Bà cụ Tứ"],
        "answer": "Tác giả (người kể chuyện ngôi thứ ba)",
        "explanation": "Người kể chuyện khách quan nhưng thấu hiểu tâm lý từng nhân vật."
    },
    {
        "question": "Từ ngữ nào dùng để kết thúc một bài văn nghị luận?",
        "options": ["Tóm lại / Thật vậy / Qua đó", "Ngày xửa ngày xưa", "Tôi nghĩ rằng", "Có lẽ là"],
        "answer": "Tóm lại / Thật vậy / Qua đó",
        "explanation": "Dùng để khẳng định lại luận điểm đã trình bày."
    },
    {
        "question": "Trong 'Sóng', nỗi nhớ của người phụ nữ được so sánh với điều gì?",
        "options": ["Sóng nhớ bờ không ngủ được", "Chim nhớ tổ", "Lá nhớ cành", "Nắng nhớ mưa"],
        "answer": "Sóng nhớ bờ không ngủ được",
        "explanation": "Nỗi nhớ thường trực cả trong tiềm thức (trong mơ)."
    },
    {
        "question": "Ai là người khẳng định: 'Hạnh phúc là một cái chăn hẹp'?",
        "options": ["Nam Cao", "Nguyễn Khải", "Nguyễn Minh Châu", "Lưu Quang Vũ"],
        "answer": "Nguyễn Khải",
        "explanation": "Một triết lý về sự lựa chọn và giới hạn của hạnh phúc trong đời sống."
    },
    {
        "question": "Tại sao 'Chiếc thuyền ngoài xa' lại được gọi là tác phẩm 'nghịch lý'?",
        "options": ["Vì vẻ đẹp bên ngoài che giấu sự thô bạo bên trong", "Vì thuyền không có người chèo", "Vì nghệ sĩ không biết chụp ảnh", "Vì tòa án không xử án"],
        "answer": "Vì vẻ đẹp bên ngoài che giấu sự thô bạo bên trong",
        "explanation": "Cảnh tượng đẹp như tranh vẽ lại chứa đựng tấn bi kịch gia đình."
    },
    {
        "question": "Câu thơ 'Dốc lên khúc khuỷu dốc thăm thẳm' sử dụng nhiều loại từ nào?",
        "options": ["Từ láy gợi hình", "Từ Hán Việt", "Từ tượng thanh", "Thuật ngữ khoa học"],
        "answer": "Từ láy gợi hình",
        "explanation": "Gợi sự hiểm trở, gập ghềnh của địa hình miền Tây."
    },
    {
        "question": "Thông điệp chính của 'Hồn Trương Ba, da hàng thịt' là gì?",
        "options": ["Con người cần sống thống nhất giữa linh hồn và thể xác", "Hãy biết cách đánh cờ giỏi", "Nên nghe lời tiên đế", "Sống sao cũng được miễn là còn sống"],
        "answer": "Con người cần sống thống nhất giữa linh hồn và thể xác",
        "explanation": "Sống thật với chính mình là hạnh phúc lớn nhất."
    },
    {
        "question": "Hình ảnh 'Máu và Hoa' trong thơ Tố Hữu tượng trưng cho điều gì?",
        "options": ["Sự hy sinh và chiến thắng", "Thiên nhiên tươi đẹp", "Mùa xuân", "Chiến tranh đau thương"],
        "answer": "Sự hy sinh và chiến thắng",
        "explanation": "Máu của sự mất mát và Hoa của ngày khải hoàn."
    },
    {
        "question": "Lý do chính khiến văn học giai đoạn 45-75 ít tập trung vào cái tôi cá nhân?",
        "options": ["Vì phải ưu tiên cho nhiệm vụ cứu nước của cộng đồng", "Vì không ai biết viết về cái tôi", "Vì cái tôi không quan trọng", "Vì bị cấm đoán"],
        "answer": "Vì phải ưu tiên cho nhiệm vụ cứu nước của cộng đồng",
        "explanation": "Lợi ích dân tộc lúc này đặt lên trên hết."
    },
    {
        "question": "Trong 'Tuyên ngôn Độc lập', đoạn cuối Bác Hồ khẳng định điều gì?",
        "options": ["Quyết tâm giữ vững quyền tự do, độc lập", "Yêu cầu các nước viện trợ", "Kêu gọi hòa bình thế giới", "Xóa bỏ các hiệp ước cũ"],
        "answer": "Quyết tâm giữ vững quyền tự do, độc lập",
        "explanation": "Lời thề bảo vệ nền độc lập bằng cả tính mạng và của cải."
    },
    {
        "question": "Tác phẩm nào sau đây không thuộc thể loại kí?",
        "options": ["Vợ nhặt", "Người lái đò Sông Đà", "Ai đã đặt tên cho dòng sông", "Một thời đại trong thi ca"],
        "answer": "Vợ nhặt",
        "explanation": "Vợ nhặt là truyện ngắn, các tác phẩm còn lại là tùy bút, bút ký hoặc tiểu luận."
    }
,
    {
        "question": "Tính chất 'Lãng mạn cách mạng' trong bài thơ 'Tây Tiến' của Quang Dũng chủ yếu được thể hiện qua:",
        "options": [
            "Cái nhìn lý tưởng hóa vẻ đẹp bi tráng của người lính và sự hùng vĩ, mĩ lệ của thiên nhiên",
            "Sự né tránh những mất mát, đau thương của chiến tranh",
            "Việc sử dụng quá nhiều các từ ngữ Hán Việt cổ kính",
            "Sự miêu tả chi tiết những cảnh sinh hoạt đời thường của bộ đội"
        ],
        "answer": "Cái nhìn lý tưởng hóa vẻ đẹp bi tráng của người lính và sự hùng vĩ, mĩ lệ của thiên nhiên",
        "explanation": "Quang Dũng không né tránh cái chết nhưng nhìn nó qua lăng kính của sự hy sinh cao cả và hào hùng."
    },
    {
        "question": "Vẻ đẹp 'Hung bạo' của sông Đà trong tùy bút của Nguyễn Tuân được ví như một 'loài thủy quái' nhằm mục đích:",
        "options": [
            "Làm nổi bật tư thế của con người là 'chất vàng mười' trong cuộc chiến chinh phục thiên nhiên",
            "Cảnh báo về sự nguy hiểm của việc đi lại trên sông",
            "Thể hiện sự căm ghét của tác giả đối với thiên nhiên miền Bắc",
            "Chứng minh kiến thức địa lý uyên bác của người viết"
        ],
        "answer": "Làm nổi bật tư thế của con người là 'chất vàng mười' trong cuộc chiến chinh phục thiên nhiên",
        "explanation": "Thiên nhiên càng dữ dội bao nhiêu thì tài năng và bản lĩnh của người lái đò càng được tôn vinh bấy nhiêu."
    },
    {
        "question": "Trong 'Vợ chồng A Phủ', sức sống tiềm tàng của nhân vật Mị bị kìm kẹp bởi hai thế lực nào?",
        "options": [
            "Cường quyền (nhà Thống lý) và Thần quyền (con ma mình nhận mặt)",
            "Sự nghèo đói và sự mù chữ",
            "Gia đình và những hủ tục lạc hậu",
            "Thiên nhiên khắc nghiệt và sự cô đơn"
        ],
        "answer": "Cường quyền (nhà Thống lý) và Thần quyền (con ma mình nhận mặt)",
        "explanation": "Mị không chỉ bị áp bức về thể xác bởi nhà Thống lý mà còn bị trói buộc về tâm linh bởi quan niệm 'đã trình ma nhà nó rồi'."
    },
    {
        "question": "Tư tưởng 'Đất Nước của Nhân dân' trong trường ca của Nguyễn Khoa Điềm có điểm gì mới mẻ về mặt chất liệu?",
        "options": [
            "Sử dụng đậm đặc chất liệu văn hóa dân gian (ca dao, truyền thuyết, phong tục) thay vì các sự kiện lịch sử triều đại",
            "Sử dụng nhiều từ ngữ chính trị hiện đại",
            "Tập trung vào các trận đánh lớn trong lịch sử",
            "Chỉ nhắc đến các anh hùng có tên tuổi trong sử sách"
        ],
        "answer": "Sử dụng đậm đặc chất liệu văn hóa dân gian (ca dao, truyền thuyết, phong tục) thay vì các sự kiện lịch sử triều đại",
        "explanation": "Tác giả khẳng định nhân dân vô danh mới là người giữ gìn và truyền lại các giá trị văn hóa cho Đất Nước."
    },
    {
        "question": "Tính 'Hiện đại' trong bài thơ 'Sóng' của Xuân Quỳnh thể hiện rõ nhất qua quan niệm nào về tình yêu?",
        "options": [
            "Sự chủ động bộc lộ khát vọng, dám từ bỏ nơi 'chật hẹp' để tìm đến cái 'cao rộng' của tâm hồn",
            "Sự cam chịu số phận và chờ đợi may mắn",
            "Việc tôn thờ tình yêu như một tôn giáo",
            "Sự phủ nhận hoàn toàn các giá trị tình cảm truyền thống"
        ],
        "answer": "Sự chủ động bộc lộ khát vọng, dám từ bỏ nơi 'chật hẹp' để tìm đến cái 'cao rộng' của tâm hồn",
        "explanation": "Câu 'Sông không hiểu nổi mình / Sóng tìm ra tận bể' thể hiện cái tôi cá nhân tự ý thức mạnh mẽ."
    },
    {
        "question": "Trong 'Chiếc thuyền ngoài xa', chi tiết 'tấm ảnh đen trắng' nhưng người nghệ sĩ thấy hiện lên 'màu hồng hồng của ánh sương mai' tượng trưng cho:",
        "options": [
            "Mối quan hệ giữa nghệ thuật và đời thực: nghệ thuật có thể lung linh nhưng đời thực thì nghiệt ngã",
            "Sự ảo tưởng của người nghệ sĩ nhiếp ảnh",
            "Chất lượng phim chụp ảnh thời bấy giờ",
            "Vẻ đẹp vĩnh cửu của thiên nhiên miền biển"
        ],
        "answer": "Mối quan hệ giữa nghệ thuật và đời thực: nghệ thuật có thể lung linh nhưng đời thực thì nghiệt ngã",
        "explanation": "Đó là khoảng cách giữa cái nhìn nghệ thuật thuần túy và cái nhìn đời sống đa diện."
    },
    {
        "question": "Nhận định nào đúng nhất về cấu trúc đối thoại trong vở kịch 'Hồn Trương Ba, da hàng thịt'?",
        "options": [
            "Là cuộc đấu tranh giữa khát vọng sống thanh cao và sự cám dỗ của các nhu cầu bản năng, tầm thường",
            "Chỉ là lời phàn nàn của Trương Ba về việc xác hàng thịt quá hôi",
            "Là cuộc tranh luận về quyền lực giữa Đế Thích và Nam Tào",
            "Là sự phê phán thói ham ăn lười làm của xác hàng thịt"
        ],
        "answer": "Là cuộc đấu tranh giữa khát vọng sống thanh cao và sự cám dỗ của các nhu cầu bản năng, tầm thường",
        "explanation": "Màn đối thoại giữa Hồn và Xác mang tính triết học về sự toàn vẹn của con người."
    },
    {
        "question": "Điểm chung về phong cách giữa tùy bút Nguyễn Tuân và bút ký Hoàng Phủ Ngọc Tường là gì?",
        "options": [
            "Cùng thể hiện sự tài hoa, uyên bác và cái tôi cá nhân đậm nét",
            "Cùng tập trung vào các sự kiện chiến đấu gay cấn",
            "Cùng sử dụng ngôn ngữ bình dân, mộc mạc",
            "Cùng có lối viết châm biếm, trào phúng"
        ],
        "answer": "Cùng thể hiện sự tài hoa, uyên bác và cái tôi cá nhân đậm nét",
        "explanation": "Cả hai đều huy động nhiều kiến thức lịch sử, địa lý, văn hóa để khám phá đối tượng thẩm mỹ."
    },
    {
        "question": "Tại sao hình tượng 'Tờ hoa' thường xuất hiện trong văn của Nguyễn Tuân sau Cách mạng?",
        "options": [
            "Để chỉ những sản phẩm lao động được tạo ra từ sự tận tụy và tài hoa của con người",
            "Để chỉ các loại giấy viết thư của tầng lớp quý tộc",
            "Để miêu tả vẻ đẹp của các loài hoa rừng",
            "Vì ông muốn trở thành một họa sĩ vẽ hoa"
        ],
        "answer": "Để chỉ những sản phẩm lao động được tạo ra từ sự tận tụy và tài hoa của con người",
        "explanation": "Sau 1945, cái Đẹp của Nguyễn Tuân nằm ngay trong cuộc sống lao động của nhân dân."
    },
    {
        "question": "Hệ thống lập luận trong 'Tuyên ngôn Độc lập' của Hồ Chí Minh được xây dựng dựa trên chiến thuật nào?",
        "options": [
            "Dùng 'gậy ông đập lưng ông': dùng chính chân lý của kẻ thù để phủ nhận tội ác của chúng",
            "Sử dụng nhiều từ ngữ gợi cảm để tranh thủ lòng thương hại",
            "Chỉ tập trung vào việc đe dọa quân sự đối với các nước thực dân",
            "Xây dựng một hệ thống pháp lý hoàn toàn mới chưa từng có"
        ],
        "answer": "Dùng 'gậy ông đập lưng ông': dùng chính chân lý của kẻ thù để phủ nhận tội ác của chúng",
        "explanation": "Bác trích dẫn Tuyên ngôn của Mỹ và Pháp để buộc chúng phải công nhận quyền độc lập của Việt Nam."
    },
    {
        "question": "Sự đổi mới của văn học Việt Nam sau năm 1975 (thể hiện qua Nguyễn Minh Châu) là sự chuyển dịch từ:",
        "options": [
            "Cảm hứng sử thi, lãng mạn sang cảm hứng thế sự và đời tư",
            "Văn học hiện thực sang văn học siêu thực",
            "Văn học chữ Nôm sang văn học chữ Quốc ngữ",
            "Đề tài chiến tranh sang đề tài khoa học viễn tưởng"
        ],
        "answer": "Cảm hứng sử thi, lãng mạn sang cảm hứng thế sự và đời tư",
        "explanation": "Văn học bắt đầu quan tâm đến số phận cá nhân và những góc khuất sau chiến tranh."
    }

]
