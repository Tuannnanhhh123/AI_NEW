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
        "question": "Sự khác biệt bản chất giữa 'Thời gian thần thoại' và 'Thời gian sử thi' là gì?",
        "options": [
            "Thời gian thần thoại là thời gian khởi nguyên; Thời gian sử thi là thời gian quá khứ hào hùng của cộng đồng",
            "Thời gian thần thoại có ngày tháng cụ thể; Thời gian sử thi thì không",
            "Thời gian thần thoại là tương lai; Thời gian sử thi là hiện tại",
            "Cả hai đều là thời gian tuyến tính hiện đại"
        ],
        "answer": "Thời gian thần thoại là thời gian khởi nguyên; Thời gian sử thi là thời gian quá khứ hào hùng của cộng đồng",
        "explanation": "Thần thoại gắn với buổi đầu tạo lập thế giới, Sử thi gắn với những biến cố lớn của bộ tộc."
    },
    {
        "question": "Trong sử thi 'Đăm Săn', việc tác giả dân gian miêu tả Đăm Săn đi bắt Nữ thần Mặt Trời thể hiện khát vọng gì?",
        "options": [
            "Khát vọng chinh phục và làm chủ những sức mạnh thiên nhiên tuyệt đối",
            "Khát vọng tìm kiếm sự bất tử của cá nhân",
            "Khát vọng mở rộng lãnh thổ sang các đại lục khác",
            "Khát vọng thay thế thần linh để cai trị thế giới"
        ],
        "answer": "Khát vọng chinh phục và làm chủ những sức mạnh thiên nhiên tuyệt đối",
        "explanation": "Đó là đỉnh cao của tinh thần anh hùng ca: con người muốn vươn tới cái giới hạn cao nhất của vũ trụ."
    },
    {
        "question": "Tính 'Lịch sử hóa' trong truyền thuyết 'An Dương Vương và Mị Châu - Trọng Thủy' được thể hiện qua:",
        "options": [
            "Sự kết hợp giữa cốt lõi sự thật lịch sử và hư cấu kỳ ảo để rút ra bài học mất nước",
            "Việc ghi chép chính xác ngày tháng xảy ra cuộc xâm lược của Triệu Đà",
            "Việc liệt kê tên tuổi của toàn bộ tướng sĩ nhà Thục",
            "Việc miêu tả chi tiết kỹ thuật đúc đồng thời Cổ Loa"
        ],
        "answer": "Sự kết hợp giữa cốt lõi sự thật lịch sử và hư cấu kỳ ảo để rút ra bài học mất nước",
        "explanation": "Truyền thuyết dùng cái ảo để vĩnh cửu hóa bài học lịch sử xương máu."
    },
    {
        "question": "Hệ thống nhân vật trong Chèo cổ (Hề, Đào, Kép, Lão) mang tính chất nghệ thuật nào rõ rệt nhất?",
        "options": [
            "Tính loại hình (nhân vật đại diện cho một tầng lớp, phẩm chất nhất định)",
            "Tính cá thể hóa sâu sắc về tâm lý cá nhân",
            "Tính biến đổi linh hoạt, không có đặc điểm cố định",
            "Tính siêu thực, thoát ly hoàn toàn đời sống thực tế"
        ],
        "answer": "Tính loại hình (nhân vật đại diện cho một tầng lớp, phẩm chất nhất định)",
        "explanation": "Nhân vật Chèo thường được ước lệ hóa để người xem nhận diện ngay vai trò xã hội của họ."
    },
    {
        "question": "Trong 'Bình Ngô đại cáo', tư tưởng 'Nhân nghĩa' của Nguyễn Trãi đã có sự phát triển vượt bậc so với Nho giáo truyền thống ở điểm nào?",
        "options": [
            "Nhân nghĩa gắn liền với tinh thần yêu nước và độc lập dân tộc (Yên dân là trừ bạo)",
            "Nhân nghĩa chỉ là việc tu dưỡng đạo đức cá nhân",
            "Nhân nghĩa là sự trung thành tuyệt đối với một vị vua cụ thể",
            "Nhân nghĩa gắn liền với việc trừng phạt kẻ thù bằng mọi giá"
        ],
        "answer": "Nhân nghĩa gắn liền với tinh thần yêu nước và độc lập dân tộc (Yên dân là trừ bạo)",
        "explanation": "Với Nguyễn Trãi, nhân nghĩa không chỉ là lý thuyết đạo đức mà là hành động cứu dân, cứu nước."
    },
    {
        "question": "Bút pháp 'Vẽ mây nảy trăng' (tả gián tiếp) trong thơ Đường luật có tác dụng gì?",
        "options": [
            "Tạo ra độ nhòe về hình ảnh, khơi gợi sự liên tưởng và tính hàm súc 'ý tại ngôn ngoại'",
            "Làm cho hình ảnh trở nên rõ ràng, chi tiết nhất có thể",
            "Dùng để giải thích các hiện tượng thiên văn học",
            "Để bài thơ có thêm nhiều tính từ miêu tả màu sắc"
        ],
        "answer": "Tạo ra độ nhòe về hình ảnh, khơi gợi sự liên tưởng và tính hàm súc 'ý tại ngôn ngoại'",
        "explanation": "Tả cái này để thấy cái kia, tạo nên vẻ đẹp sâu kín, tinh tế của thơ cổ."
    },
    {
        "question": "Xung đột kịch trong vở Tuồng 'Nghêu, Sò, Ốc, Hến' mang tính chất trào phúng chủ yếu vì:",
        "options": [
            "Sự mâu thuẫn giữa vẻ ngoài đạo mạo của quan lại và bản chất tham lam, dâm ô bên trong",
            "Cuộc chiến đấu giữa cái thiện và cái ác mang tính sống còn",
            "Sự hiểu lầm giữa các nhân vật lao động nghèo khổ",
            "Sự can thiệp của các yếu tố thần linh vào công đường"
        ],
        "answer": "Sự mâu thuẫn giữa vẻ ngoài đạo mạo của quan lại và bản chất tham lam, dâm ô bên trong",
        "explanation": "Tiếng cười bật ra từ việc mặt nạ nhân cách bị bóc trần."
    },
    {
        "question": "Khái niệm 'Hào khí Đông A' trong văn học đời Trần (như bài Thuật Hoài) được hiểu là:",
        "options": [
            "Sự kết hợp giữa tinh thần tự cường dân tộc và khát vọng lập công danh cao cả",
            "Sự tôn thờ các vị thần phương Đông",
            "Lối sống ẩn dật, xa lánh bụi trần của các nho sĩ",
            "Sự bi quan trước vận mệnh ngắn ngủi của kiếp người"
        ],
        "answer": "Sự kết hợp giữa tinh thần tự cường dân tộc và khát vọng lập công danh cao cả",
        "explanation": "Đông A là chữ Trần (chữ Hán), biểu tượng cho sức mạnh quật khởi của quân dân nhà Trần."
    },
    {
        "question": "Tại sao trong Thần thoại, các vị thần thường có kích thước khổng lồ và hành động 'đào đất, lấp biển'?",
        "options": [
            "Để cụ thể hóa sức mạnh vô biên của con người thời sơ khai trong việc nhận thức và cải tạo vũ trụ",
            "Vì thời đó con người thực sự cao lớn như vậy",
            "Để tạo sự khiếp sợ cho người đọc",
            "Vì các vị thần này thực chất là các hành tinh"
        ],
        "answer": "Để cụ thể hóa sức mạnh vô biên của con người thời sơ khai trong việc nhận thức và cải tạo vũ trụ",
        "explanation": "Kích thước khổng lồ là cách biểu đạt tư duy về sự vĩ đại của tự nhiên mà con người muốn chinh phục."
    },
    {
        "question": "Yếu tố 'Đối' (Niêm luật) trong thơ thất ngôn bát cú Đường luật đóng vai trò gì về mặt mỹ học?",
        "options": [
            "Tạo ra sự cân xứng, hài hòa tuyệt đối và vẻ đẹp trang trọng cho bài thơ",
            "Làm cho bài thơ dài hơn",
            "Để tác giả dễ tìm vần điệu hơn",
            "Để bài thơ có cấu trúc giống văn xuôi"
        ],
        "answer": "Tạo ra sự cân xứng, hài hòa tuyệt đối và vẻ đẹp trang trọng cho bài thơ",
        "explanation": "Phép đối tạo nên nhạc điệu và sự đăng đối chỉnh chu, chuẩn mực của thẩm mỹ phong kiến."
    },
    {
        "question": "Mối quan hệ giữa 'Tình' và 'Cảnh' trong bài 'Cảnh ngày hè' (Nguyễn Trãi) là mối quan hệ:",
        "options": [
            "Cảnh vật rực rỡ nảy sinh từ tâm thế yêu đời và tấm lòng ưu ái dân tộc của nhà thơ",
            "Cảnh vật buồn bã tương ứng với nỗi sầu muộn của tác giả",
            "Cảnh và Tình hoàn toàn tách biệt, không liên quan đến nhau",
            "Cảnh vật chỉ là phông nền cho các sự kiện lịch sử"
        ],
        "answer": "Cảnh vật rực rỡ nảy sinh từ tâm thế yêu đời và tấm lòng ưu ái dân tộc của nhà thơ",
        "explanation": "Tâm hồn có an yên, yêu dân thì cảnh ngày hè mới hiện lên tràn đầy sức sống 'đùn đùn', 'phun thức đỏ'."
    },
    {
        "question": "Cái chết của nhân vật Mị Châu trong truyền thuyết mang ý nghĩa:",
        "options": [
            "Sự trả giá tất yếu cho việc để tình cảm cá nhân vượt trên lợi ích quốc gia",
            "Sự oan ức vô tội của một người phụ nữ nhẹ dạ",
            "Một tai nạn ngoài ý muốn trong chiến tranh",
            "Sự giải thoát khỏi cuộc hôn nhân bất hạnh"
        ],
        "answer": "Sự trả giá tất yếu cho việc để tình cảm cá nhân vượt trên lợi ích quốc gia",
        "explanation": "Hình phạt nghiêm khắc của lịch sử dành cho sự thiếu cảnh giác."
    },
    {
        "question": "Đặc trưng ngôn ngữ của Sử thi là gì?",
        "options": ["Ngôn ngữ trang trọng, giàu nhạc điệu, sử dụng nhiều điệp từ và so sánh trùng điệp", "Ngôn ngữ bình dân, đời thường, ngắn gọn", "Ngôn ngữ khô khan, đậm tính lý trí", "Ngôn ngữ chỉ gồm các câu hỏi tu từ"],
        "answer": "Ngôn ngữ trang trọng, giàu nhạc điệu, sử dụng nhiều điệp từ và so sánh trùng điệp",
        "explanation": "Tạo nên âm hưởng hùng tráng, phù hợp với việc kể về những chiến công vĩ đại."
    },
    {
        "question": "Tính chất 'Lục ngôn' (câu 6 chữ) trong thơ Nguyễn Trãi có ý nghĩa cách tân như thế nào?",
        "options": [
            "Khẳng định sự tự chủ của văn học dân tộc bằng việc xen kẽ nhịp điệu dân gian vào thể thơ ngoại nhập",
            "Thể hiện sự vụng về trong việc tuân thủ luật Đường",
            "Làm cho bài thơ có cấu trúc giống thơ tự do hiện đại",
            "Chỉ để thay đổi không khí cho bài thơ đỡ nhàm chán"
        ],
        "answer": "Khẳng định sự tự chủ của văn học dân tộc bằng việc xen kẽ nhịp điệu dân gian vào thể thơ ngoại nhập",
        "explanation": "Đây là bước đi sáng tạo giúp thơ Nôm thoát khỏi cái bóng quá lớn của thơ Hán."
    },
    {
        "question": "Vai trò của nhân vật Hề trong Chèo đối với cấu trúc vở diễn là gì?",
        "options": [
            "Vừa là người dẫn chuyện, vừa là người phản biện và bộc lộ tư tưởng dân gian về xã hội",
            "Chỉ là nhân vật gây cười vô thưởng vô phạt",
            "Làm cho các nhân vật chính trở nên nghiêm túc hơn",
            "Thay thế hoàn toàn cho nhân vật đào và kép"
        ],
        "answer": "Vừa là người dẫn chuyện, vừa là người phản biện và bộc lộ tư tưởng dân gian về xã hội",
        "explanation": "Hề Chèo mang tiếng cười của nhân dân để phê phán thói hư tật xấu và bất công xã hội."
    },


    {
        "question": "Sự khác biệt bản chất giữa 'Thời gian thần thoại' và 'Thời gian sử thi' là gì?",
        "options": [
            "Thời gian thần thoại là thời gian khởi nguyên; Thời gian sử thi là thời gian quá khứ hào hùng của cộng đồng",
            "Thời gian thần thoại có ngày tháng cụ thể; Thời gian sử thi thì không",
            "Thời gian thần thoại là tương lai; Thời gian sử thi là hiện tại",
            "Cả hai đều là thời gian tuyến tính hiện đại"
        ],
        "answer": "Thời gian thần thoại là thời gian khởi nguyên; Thời gian sử thi là thời gian quá khứ hào hùng của cộng đồng",
        "explanation": "Thần thoại gắn với buổi đầu tạo lập thế giới, Sử thi gắn với những biến cố lớn của bộ tộc."
    },
    {
        "question": "Trong sử thi 'Đăm Săn', việc tác giả dân gian miêu tả Đăm Săn đi bắt Nữ thần Mặt Trời thể hiện khát vọng gì?",
        "options": [
            "Khát vọng chinh phục và làm chủ những sức mạnh thiên nhiên tuyệt đối",
            "Khát vọng tìm kiếm sự bất tử của cá nhân",
            "Khát vọng mở rộng lãnh thổ sang các đại lục khác",
            "Khát vọng thay thế thần linh để cai trị thế giới"
        ],
        "answer": "Khát vọng chinh phục và làm chủ những sức mạnh thiên nhiên tuyệt đối",
        "explanation": "Đó là đỉnh cao của tinh thần anh hùng ca: con người muốn vươn tới cái giới hạn cao nhất của vũ trụ."
    },
    {
        "question": "Tính 'Lịch sử hóa' trong truyền thuyết 'An Dương Vương và Mị Châu - Trọng Thủy' được thể hiện qua:",
        "options": [
            "Sự kết hợp giữa cốt lõi sự thật lịch sử và hư cấu kỳ ảo để rút ra bài học mất nước",
            "Việc ghi chép chính xác ngày tháng xảy ra cuộc xâm lược của Triệu Đà",
            "Việc liệt kê tên tuổi của toàn bộ tướng sĩ nhà Thục",
            "Việc miêu tả chi tiết kỹ thuật đúc đồng thời Cổ Loa"
        ],
        "answer": "Sự kết hợp giữa cốt lõi sự thật lịch sử và hư cấu kỳ ảo để rút ra bài học mất nước",
        "explanation": "Truyền thuyết dùng cái ảo để vĩnh cửu hóa bài học lịch sử xương máu."
    },
    {
        "question": "Hệ thống nhân vật trong Chèo cổ (Hề, Đào, Kép, Lão) mang tính chất nghệ thuật nào rõ rệt nhất?",
        "options": [
            "Tính loại hình (nhân vật đại diện cho một tầng lớp, phẩm chất nhất định)",
            "Tính cá thể hóa sâu sắc về tâm lý cá nhân",
            "Tính biến đổi linh hoạt, không có đặc điểm cố định",
            "Tính siêu thực, thoát ly hoàn toàn đời sống thực tế"
        ],
        "answer": "Tính loại hình (nhân vật đại diện cho một tầng lớp, phẩm chất nhất định)",
        "explanation": "Nhân vật Chèo thường được ước lệ hóa để người xem nhận diện ngay vai trò xã hội của họ."
    },
    {
        "question": "Trong 'Bình Ngô đại cáo', tư tưởng 'Nhân nghĩa' của Nguyễn Trãi đã có sự phát triển vượt bậc so với Nho giáo truyền thống ở điểm nào?",
        "options": [
            "Nhân nghĩa gắn liền với tinh thần yêu nước và độc lập dân tộc (Yên dân là trừ bạo)",
            "Nhân nghĩa chỉ là việc tu dưỡng đạo đức cá nhân",
            "Nhân nghĩa là sự trung thành tuyệt đối với một vị vua cụ thể",
            "Nhân nghĩa gắn liền với việc trừng phạt kẻ thù bằng mọi giá"
        ],
        "answer": "Nhân nghĩa gắn liền với tinh thần yêu nước và độc lập dân tộc (Yên dân là trừ bạo)",
        "explanation": "Với Nguyễn Trãi, nhân nghĩa không chỉ là lý thuyết đạo đức mà là hành động cứu dân, cứu nước."
    },
    {
        "question": "Bút pháp 'Vẽ mây nảy trăng' (tả gián tiếp) trong thơ Đường luật có tác dụng gì?",
        "options": [
            "Tạo ra độ nhòe về hình ảnh, khơi gợi sự liên tưởng và tính hàm súc 'ý tại ngôn ngoại'",
            "Làm cho hình ảnh trở nên rõ ràng, chi tiết nhất có thể",
            "Dùng để giải thích các hiện tượng thiên văn học",
            "Để bài thơ có thêm nhiều tính từ miêu tả màu sắc"
        ],
        "answer": "Tạo ra độ nhòe về hình ảnh, khơi gợi sự liên tưởng và tính hàm súc 'ý tại ngôn ngoại'",
        "explanation": "Tả cái này để thấy cái kia, tạo nên vẻ đẹp sâu kín, tinh tế của thơ cổ."
    },
    {
        "question": "Xung đột kịch trong vở Tuồng 'Nghêu, Sò, Ốc, Hến' mang tính chất trào phúng chủ yếu vì:",
        "options": [
            "Sự mâu thuẫn giữa vẻ ngoài đạo mạo của quan lại và bản chất tham lam, dâm ô bên trong",
            "Cuộc chiến đấu giữa cái thiện và cái ác mang tính sống còn",
            "Sự hiểu lầm giữa các nhân vật lao động nghèo khổ",
            "Sự can thiệp của các yếu tố thần linh vào công đường"
        ],
        "answer": "Sự mâu thuẫn giữa vẻ ngoài đạo mạo của quan lại và bản chất tham lam, dâm ô bên trong",
        "explanation": "Tiếng cười bật ra từ việc mặt nạ nhân cách bị bóc trần."
    },
    {
        "question": "Khái niệm 'Hào khí Đông A' trong văn học đời Trần (như bài Thuật Hoài) được hiểu là:",
        "options": [
            "Sự kết hợp giữa tinh thần tự cường dân tộc và khát vọng lập công danh cao cả",
            "Sự tôn thờ các vị thần phương Đông",
            "Lối sống ẩn dật, xa lánh bụi trần của các nho sĩ",
            "Sự bi quan trước vận mệnh ngắn ngủi của kiếp người"
        ],
        "answer": "Sự kết hợp giữa tinh thần tự cường dân tộc và khát vọng lập công danh cao cả",
        "explanation": "Đông A là chữ Trần (chữ Hán), biểu tượng cho sức mạnh quật khởi của quân dân nhà Trần."
    },
    {
        "question": "Tại sao trong Thần thoại, các vị thần thường có kích thước khổng lồ và hành động 'đào đất, lấp biển'?",
        "options": [
            "Để cụ thể hóa sức mạnh vô biên của con người thời sơ khai trong việc nhận thức và cải tạo vũ trụ",
            "Vì thời đó con người thực sự cao lớn như vậy",
            "Để tạo sự khiếp sợ cho người đọc",
            "Vì các vị thần này thực chất là các hành tinh"
        ],
        "answer": "Để cụ thể hóa sức mạnh vô biên của con người thời sơ khai trong việc nhận thức và cải tạo vũ trụ",
        "explanation": "Kích thước khổng lồ là cách biểu đạt tư duy về sự vĩ đại của tự nhiên mà con người muốn chinh phục."
    },
    {
        "question": "Yếu tố 'Đối' (Niêm luật) trong thơ thất ngôn bát cú Đường luật đóng vai trò gì về mặt mỹ học?",
        "options": [
            "Tạo ra sự cân xứng, hài hòa tuyệt đối và vẻ đẹp trang trọng cho bài thơ",
            "Làm cho bài thơ dài hơn",
            "Để tác giả dễ tìm vần điệu hơn",
            "Để bài thơ có cấu trúc giống văn xuôi"
        ],
        "answer": "Tạo ra sự cân xứng, hài hòa tuyệt đối và vẻ đẹp trang trọng cho bài thơ",
        "explanation": "Phép đối tạo nên nhạc điệu và sự đăng đối chỉnh chu, chuẩn mực của thẩm mỹ phong kiến."
    },
    {
        "question": "Mối quan hệ giữa 'Tình' và 'Cảnh' trong bài 'Cảnh ngày hè' (Nguyễn Trãi) là mối quan hệ:",
        "options": [
            "Cảnh vật rực rỡ nảy sinh từ tâm thế yêu đời và tấm lòng ưu ái dân tộc của nhà thơ",
            "Cảnh vật buồn bã tương ứng với nỗi sầu muộn của tác giả",
            "Cảnh và Tình hoàn toàn tách biệt, không liên quan đến nhau",
            "Cảnh vật chỉ là phông nền cho các sự kiện lịch sử"
        ],
        "answer": "Cảnh vật rực rỡ nảy sinh từ tâm thế yêu đời và tấm lòng ưu ái dân tộc của nhà thơ",
        "explanation": "Tâm hồn có an yên, yêu dân thì cảnh ngày hè mới hiện lên tràn đầy sức sống 'đùn đùn', 'phun thức đỏ'."
    },
    {
        "question": "Cái chết của nhân vật Mị Châu trong truyền thuyết mang ý nghĩa:",
        "options": [
            "Sự trả giá tất yếu cho việc để tình cảm cá nhân vượt trên lợi ích quốc gia",
            "Sự oan ức vô tội của một người phụ nữ nhẹ dạ",
            "Một tai nạn ngoài ý muốn trong chiến tranh",
            "Sự giải thoát khỏi cuộc hôn nhân bất hạnh"
        ],
        "answer": "Sự trả giá tất yếu cho việc để tình cảm cá nhân vượt trên lợi ích quốc gia",
        "explanation": "Hình phạt nghiêm khắc của lịch sử dành cho sự thiếu cảnh giác."
    },
    {
        "question": "Đặc trưng ngôn ngữ của Sử thi là gì?",
        "options": ["Ngôn ngữ trang trọng, giàu nhạc điệu, sử dụng nhiều điệp từ và so sánh trùng điệp", "Ngôn ngữ bình dân, đời thường, ngắn gọn", "Ngôn ngữ khô khan, đậm tính lý trí", "Ngôn ngữ chỉ gồm các câu hỏi tu từ"],
        "answer": "Ngôn ngữ trang trọng, giàu nhạc điệu, sử dụng nhiều điệp từ và so sánh trùng điệp",
        "explanation": "Tạo nên âm hưởng hùng tráng, phù hợp với việc kể về những chiến công vĩ đại."
    },
    {
        "question": "Tính chất 'Lục ngôn' (câu 6 chữ) trong thơ Nguyễn Trãi có ý nghĩa cách tân như thế nào?",
        "options": [
            "Khẳng định sự tự chủ của văn học dân tộc bằng việc xen kẽ nhịp điệu dân gian vào thể thơ ngoại nhập",
            "Thể hiện sự vụng về trong việc tuân thủ luật Đường",
            "Làm cho bài thơ có cấu trúc giống thơ tự do hiện đại",
            "Chỉ để thay đổi không khí cho bài thơ đỡ nhàm chán"
        ],
        "answer": "Khẳng định sự tự chủ của văn học dân tộc bằng việc xen kẽ nhịp điệu dân gian vào thể thơ ngoại nhập",
        "explanation": "Đây là bước đi sáng tạo giúp thơ Nôm thoát khỏi cái bóng quá lớn của thơ Hán."
    },
    {
        "question": "Vai trò của nhân vật Hề trong Chèo đối với cấu trúc vở diễn là gì?",
        "options": [
            "Vừa là người dẫn chuyện, vừa là người phản biện và bộc lộ tư tưởng dân gian về xã hội",
            "Chỉ là nhân vật gây cười vô thưởng vô phạt",
            "Làm cho các nhân vật chính trở nên nghiêm túc hơn",
            "Thay thế hoàn toàn cho nhân vật đào và kép"
        ],
        "answer": "Vừa là người dẫn chuyện, vừa là người phản biện và bộc lộ tư tưởng dân gian về xã hội",
        "explanation": "Hề Chèo mang tiếng cười của nhân dân để phê phán thói hư tật xấu và bất công xã hội."
    },


    {
        "question": "Điểm khác biệt căn bản về thế giới quan giữa Thần thoại và Truyện cổ tích là gì?",
        "options": [
            "Thần thoại giải thích sự hình thành vũ trụ; Cổ tích giải quyết mâu thuẫn xã hội và đạo đức",
            "Thần thoại có yếu tố kỳ ảo còn Cổ tích thì không",
            "Thần thoại chỉ dành cho người lớn, Cổ tích dành cho trẻ em",
            "Thần thoại là văn thơ, Cổ tích là văn xuôi"
        ],
        "answer": "Thần thoại giải thích sự hình thành vũ trụ; Cổ tích giải quyết mâu thuẫn xã hội và đạo đức",
        "explanation": "Thần thoại thuộc giai đoạn nhận thức sơ khai về tự nhiên; Cổ tích thuộc giai đoạn đã phân chia giai cấp."
    },
    {
        "question": "Tính 'Lịch sử hóa' trong sử thi Đăm Săn thể hiện rõ nhất qua chi tiết nào?",
        "options": [
            "Sự phát triển của cộng đồng thị tộc gắn liền với việc mở mang bờ cõi và chinh phục thiên nhiên",
            "Việc Đăm Săn cưới hai chị em Hơ Nhị, Hơ Bhị",
            "Các cuộc đối thoại giữa Đăm Săn và ông Trời",
            "Cách miêu tả trang phục và vũ khí của tù trưởng"
        ],
        "answer": "Sự phát triển của cộng đồng thị tộc gắn liền với việc mở mang bờ cõi và chinh phục thiên nhiên",
        "explanation": "Người anh hùng sử thi là đại diện cho khát vọng và sức mạnh của cả một cộng đồng dân tộc."
    },
    {
        "question": "Bi kịch của nhân vật Héc-to trong 'I-li-át' phản ánh sự giằng xé giữa hai giá trị nào?",
        "options": [
            "Bổn phận với quốc gia và tình cảm gia đình cá nhân",
            "Sự sống và cái chết",
            "Lòng kiêu hãnh và sự hèn nhát",
            "Tình yêu dành cho vợ và tình yêu dành cho người tình"
        ],
        "answer": "Bổn phận với quốc gia và tình cảm gia đình cá nhân",
        "explanation": "Héc-to ra trận dù biết sẽ chết, đó là sự lựa chọn danh dự cộng đồng trên hạnh phúc cá nhân."
    },
    {
        "question": "Tại sao Nguyễn Trãi thường chèn các câu thơ lục ngôn (6 chữ) vào bài thơ thất ngôn (7 chữ) trong 'Quốc âm thi tập'?",
        "options": [
            "Để tạo nhịp điệu dồn nén, dứt khoát và thể hiện sự sáng tạo thoát ly quy phạm thơ Đường",
            "Vì ông không viết đủ số chữ theo quy định",
            "Do sự nhầm lẫn trong quá trình sao chép bản thảo",
            "Để làm cho bài thơ trở nên khó đọc hơn"
        ],
        "answer": "Để tạo nhịp điệu dồn nén, dứt khoát và thể hiện sự sáng tạo thoát ly quy phạm thơ Đường",
        "explanation": "Đây là sự Việt hóa thơ Đường, tạo nên bản sắc riêng của thơ Nôm Việt Nam."
    },
    {
        "question": "Yếu tố 'Nhân nghĩa' trong 'Bình Ngô đại cáo' của Nguyễn Trãi mang nội dung cốt lõi là gì?",
        "options": [
            "Lo cho dân, trừ bạo cho dân và khẳng định chủ quyền dân tộc",
            "Lòng thương hại kẻ thù khi chúng thất bại",
            "Sự tuân thủ tuyệt đối các quy tắc của Nho giáo",
            "Việc phân chia bổng lộc công bằng cho quân sĩ"
        ],
        "answer": "Lo cho dân, trừ bạo cho dân và khẳng định chủ quyền dân tộc",
        "explanation": "Với Nguyễn Trãi, nhân nghĩa không trừu tượng mà gắn liền với vận mệnh nhân dân: 'Yên dân báu ở trừ bạo'."
    },
    {
        "question": "Thủ pháp 'Đòn bẩy' (miêu tả kẻ thù mạnh để tôn vinh nhân vật chính) được sử dụng như thế nào trong các đoạn trích Sử thi?",
        "options": [
            "Miêu tả Mtao Mxây hung hãn, trang bị tận răng để làm bật lên sự ung dung, bản lĩnh của Đăm Săn",
            "Làm cho câu chuyện trở nên kịch tính hơn",
            "Để kéo dài thời gian kể chuyện",
            "Chứng minh rằng kẻ ác luôn có sức mạnh hơn người thiện"
        ],
        "answer": "Miêu tả Mtao Mxây hung hãn, trang bị tận răng để làm bật lên sự ung dung, bản lĩnh của Đăm Săn",
        "explanation": "Kẻ thù càng mạnh thì chiến thắng của người anh hùng càng vinh quang."
    },
    {
        "question": "Bút pháp 'Ước lệ tượng trưng' trong miêu tả Thúy Kiều và Thúy Vân của Nguyễn Du nhằm mục đích:",
        "options": [
            "Gợi ra số phận và tính cách nhân vật thông qua các hình ảnh thiên nhiên chuẩn mực",
            "Miêu tả chính xác ngoại hình thực tế của nhân vật",
            "Tiết kiệm từ ngữ miêu tả",
            "Làm cho nhân vật trở nên xa lạ với người đọc"
        ],
        "answer": "Gợi ra số phận và tính cách nhân vật thông qua các hình ảnh thiên nhiên chuẩn mực",
        "explanation": "Vân 'mây thua nước tóc', Kiều 'hoa ghen thua thắm' báo hiệu một cuộc đời bình yên cho Vân và sóng gió cho Kiều."
    },
    {
        "question": "Đặc điểm của 'Xung đột bi kịch' trong kịch bản văn học là gì?",
        "options": [
            "Mâu thuẫn giữa những khát vọng cao cả và thực tại nghiệt ngã không thể điều hòa",
            "Sự hiểu lầm giữa các nhân vật về tiền bạc",
            "Sự tranh giành quyền lực giữa cái thiện và cái ác",
            "Cuộc đấu tranh chống lại thiên tai"
        ],
        "answer": "Mâu thuẫn giữa những khát vọng cao cả và thực tại nghiệt ngã không thể điều hòa",
        "explanation": "Nhân vật bi kịch thường phải đối mặt với sự lựa chọn mà kết thúc thường là sự trả giá bằng cái chết."
    },
    {
        "question": "Trong 'Độc Tiểu Thanh ký', sự đồng cảm của Nguyễn Du với nàng Tiểu Thanh thể hiện tư tưởng nào?",
        "options": [
            "Tư tưởng 'Tài mệnh tương đố' (Tài năng và số phận luôn mâu thuẫn nhau)",
            "Sự phê phán lối sống xa hoa",
            "Lòng trung quân ái quốc",
            "Khát vọng thay đổi chế độ phong kiến"
        ],
        "answer": "Tư tưởng 'Tài mệnh tương đố' (Tài năng và số phận luôn mâu thuẫn nhau)",
        "explanation": "Nguyễn Du thương người cũng là thương mình, thương cho những kiếp tài hoa mà bạc mệnh."
    },
    {
        "question": "Sự xuất hiện của yếu tố 'Kỳ ảo' trong văn học trung đại (như chi tiết Mị Châu trở thành ngọc trai) có vai trò:",
        "options": [
            "Vừa để minh oan cho nhân vật, vừa thể hiện thái độ nghiêm khắc của nhân dân trước sai lầm",
            "Chỉ để làm cho câu chuyện thêm hấp dẫn",
            "Để giải quyết các bế tắc mà thực tế không làm được",
            "Để tôn thờ các vị thần linh"
        ],
        "answer": "Vừa để minh oan cho nhân vật, vừa thể hiện thái độ nghiêm khắc của nhân dân trước sai lầm",
        "explanation": "Yếu tố kỳ ảo mang tính phán xét đạo đức và lưu giữ ký ức lịch sử của cộng đồng."
    }
,
    {
        "question": "Trong văn bản 'Thần Trụ Trời', hành động nào của vị thần giúp phân chia trời đất?",
        "options": ["Đào đất, đá đắp thành một cái cột cao để chống trời", "Dùng kiếm chém đôi bầu trời", "Hét một tiếng thật lớn", "Nhờ các vị thần khác giúp sức"],
        "answer": "Đào đất, đá đắp thành một cái cột cao để chống trời",
        "explanation": "Đây là hành động kỳ vĩ giải thích sự hình thành trời đất trong thần thoại."
    },
    {
        "question": "Văn bản 'Lô-mê-ô và Giu-li-ét' của Shakespeare thuộc thể loại nào?",
        "options": ["Bi kịch", "Hài kịch", "Truyện ngắn", "Thơ lục bát"],
        "answer": "Bi kịch",
        "explanation": "Tác phẩm kết thúc bằng cái chết của cả hai nhân vật chính do mâu thuẫn dòng tộc."
    },
    {
        "question": "Biện pháp tu từ nào được sử dụng chính trong câu: 'Đời người như bóng câu qua cửa sổ'?",
        "options": ["So sánh", "Ẩn dụ", "Nhân hóa", "Điệp ngữ"],
        "answer": "So sánh",
        "explanation": "Sử dụng từ 'như' để đối chiếu sự ngắn ngủi của đời người."
    },
    {
        "question": "Trong bài thơ 'Cảnh ngày hè', từ 'hồng liên' có nghĩa là gì?",
        "options": ["Sen hồng", "Mây hồng", "Lửa hồng", "Gạo hồng"],
        "answer": "Sen hồng",
        "explanation": "Hồng liên trì (ao sen hồng) - một hình ảnh đẹp của thiên nhiên mùa hè."
    },
    {
        "question": "Lỗi 'Dùng từ không đúng nghĩa' thường xảy ra do đâu?",
        "options": ["Nhầm lẫn giữa các từ gần âm hoặc gần nghĩa", "Viết sai chính tả", "Câu quá dài", "Thiếu chủ ngữ"],
        "answer": "Nhầm lẫn giữa các từ gần âm hoặc gần nghĩa",
        "explanation": "Người viết không nắm vững nghĩa của từ dẫn đến dùng sai ngữ cảnh."
    },
    {
        "question": "Văn bản 'Hiền tài là nguyên khí của quốc gia' (Thân Nhân Trung) khẳng định vai trò của ai?",
        "options": ["Người có tài cao, đạo đức tốt", "Những người giàu có", "Quân đội", "Nông dân"],
        "answer": "Người có tài cao, đạo đức tốt",
        "explanation": "Hiền tài được coi là mạch sống, nguồn năng lượng cốt lõi của đất nước."
    },
    {
        "question": "Trong thơ Đường luật, hai câu 'Thực' (câu 3-4) và hai câu 'Luận' (câu 5-6) phải tuân thủ quy tắc nào?",
        "options": ["Phải đối nhau", "Phải gieo vần trắc", "Phải có 6 chữ", "Không cần quy tắc"],
        "answer": "Phải đối nhau",
        "explanation": "Phép đối là đặc trưng quan trọng tạo nên sự cân xứng trong thơ Đường luật."
    },
    {
        "question": "Tác phẩm 'Bình Ngô đại cáo' được viết bằng ngôn ngữ nào?",
        "options": ["Chữ Hán", "Chữ Nôm", "Chữ Quốc ngữ", "Chữ Pháp"],
        "answer": "Chữ Hán",
        "explanation": "Văn bản hành chính nhà nước thời bấy giờ thường dùng chữ Hán."
    },
    {
        "question": "Yếu tố nào sau đây là đặc trưng của văn bản thông tin tổng hợp?",
        "options": ["Sử dụng kết hợp phương tiện ngôn ngữ và phi ngôn ngữ (hình ảnh, biểu đồ)", "Chỉ dùng lời kể", "Tập trung miêu tả nội tâm nhân vật", "Xây dựng tình huống kịch tính"],
        "answer": "Sử dụng kết hợp phương tiện ngôn ngữ và phi ngôn ngữ (hình ảnh, biểu đồ)",
        "explanation": "Hình ảnh và biểu đồ giúp thông tin trở nên trực quan và dễ hiểu hơn."
    },
    {
        "question": "Mục đích của việc lập dàn ý trước khi viết bài văn là gì?",
        "options": ["Giúp bài viết mạch lạc, đủ ý và không bị lạc đề", "Để bài viết dài hơn", "Để không phải suy nghĩ khi viết", "Để trang trí văn bản"],
        "answer": "Giúp bài viết mạch lạc, đủ ý và không bị lạc đề",
        "explanation": "Dàn ý là khung xương giúp kiểm soát dung lượng và nội dung bài viết."
    },
    {
        "question": "Câu thơ 'Dưới trăng quyên đã gọi hè / Đầu tường lửa lựu lập lòe đơm bông' miêu tả cảnh mùa nào?",
        "options": ["Mùa hè", "Mùa xuân", "Mùa thu", "Mùa đông"],
        "answer": "Mùa hè",
        "explanation": "Hình ảnh chim quyên và hoa lựu nở đỏ là biểu tượng của mùa hè trong văn chương cũ."
    },
    {
        "question": "Trong 'Truyện Kiều', nhân vật nào đại diện cho công lý và sức mạnh anh hùng?",
        "options": ["Từ Hải", "Kim Trọng", "Thúc Sinh", "Mã Giám Sinh"],
        "answer": "Từ Hải",
        "explanation": "Từ Hải là hình tượng 'đội trời đạp đất', mang lại sự công bằng cho Thúy Kiều."
    },
    {
        "question": "Phong cách ngôn ngữ sinh hoạt có đặc trưng nào?",
        "options": ["Tính cụ thể, tính cảm xúc và tính cá thể", "Tính trừu tượng", "Tính khuôn mẫu", "Tính khách quan tuyệt đối"],
        "answer": "Tính cụ thể, tính cảm xúc và tính cá thể",
        "explanation": "Phản ánh đời sống hàng ngày với những sắc thái tình cảm riêng của người nói."
    },
    {
        "question": "Nghĩa của từ 'Ưu ái' trong câu 'Dân giàu đủ khắp phương xa / Trẻ con người già đều ca hát' (Nguyễn Trãi) là gì?",
        "options": ["Luôn lo lắng và yêu thương dân", "Sự thiên vị", "Sự vui vẻ", "Sự giàu sang"],
        "answer": "Luôn lo lắng và yêu thương dân",
        "explanation": "Tấm lòng luôn đau đáu vì cuộc sống của nhân dân."
    },
    {
        "question": "Trình tự của một bài viết nghị luận về một vấn đề đời sống thường là gì?",
        "options": ["Nêu vấn đề -> Giải thích -> Phân tích/Chứng minh -> Bình luận/Rút ra bài học", "Kể chuyện -> Tả cảnh -> Kết thúc", "Mở bài -> Thân bài -> Kết bài", "Giới thiệu nhân vật -> Tình huống -> Giải quyết"],
        "answer": "Nêu vấn đề -> Giải thích -> Phân tích/Chứng minh -> Bình luận/Rút ra bài học",
        "explanation": "Đây là cấu trúc logic để thuyết phục người đọc về một quan điểm xã hội."
    }
,
    {
        "question": "Văn bản 'Thần Trụ Trời' thuộc thể loại văn học dân gian nào?",
        "options": ["Thần thoại", "Truyện cổ tích", "Truyện ngụ ngôn", "Truyện cười"],
        "answer": "Thần thoại",
        "explanation": "Đây là truyện thần thoại suy nguyên nhằm giải thích sự hình thành thế giới."
    },
    {
        "question": "Nhân vật Đăm Săn trong sử thi 'Chiến thắng Mtao Mxây' là người anh hùng của dân tộc nào?",
        "options": ["Ê-đê", "M'nông", "Thái", "Tày"],
        "answer": "Ê-đê",
        "explanation": "Đăm Săn là bộ sử thi nổi tiếng nhất của người dân tộc Ê-đê ở Tây Nguyên."
    },
    {
        "question": "Trong văn bản 'Héc-to từ biệt Ăng-đrô-mác', Héc-to là anh hùng của thành bang nào?",
        "options": ["Thành Tơ-roa", "Thành Ty-rơ", "Thành Ten-né", "Thành At-ten"],
        "answer": "Thành Tơ-roa",
        "explanation": "Héc-to là hoàng tử, người anh hùng bảo vệ thành Tơ-roa trong sử thi I-li-át."
    },
    {
        "question": "Đặc điểm nổi bật của nhân vật trong thần thoại là gì?",
        "options": ["Có sức mạnh phi thường và khả năng biến hóa", "Là người bình thường", "Luôn gặp bất hạnh",
                    "Chỉ là các con vật biết nói"],
        "answer": "Có sức mạnh phi thường và khả năng biến hóa",
        "explanation": "Thần thoại thường xây dựng nhân vật là các vị thần có quyền năng vô hạn."
    },
    {
        "question": "Thể thơ của bài 'Cảnh ngày hè' (Nguyễn Trãi) là gì?",
        "options": ["Thất ngôn xen lục ngôn", "Lục bát", "Song thất lục bát", "Thơ tự do"],
        "answer": "Thất ngôn xen lục ngôn",
        "explanation": "Bài thơ thuộc tập 'Quốc âm thi tập', viết theo lối 7 chữ xen lẫn câu 6 chữ."
    },
    {
        "question": "Trong bài thơ 'Thuật hoài' (Phạm Ngũ Lão), 'Tam quân' được so sánh với khí thế của con vật nào?",
        "options": ["Tỳ hưu", "Hổ báo", "Sư tử", "Rồng"],
        "answer": "Hổ báo",
        "explanation": "Câu thơ: 'Tam quân tì hổ khí thôn Ngưu' (Ba quân khí mạnh nuốt trôi trâu/nuốt sao Ngưu)."
    },
    {
        "question": "Văn bản 'Huyện đường' trích từ vở tuồng nào?",
        "options": ["Nghêu, Sò, Ốc, Hến", "Sơn Hậu", "Tam nữ đồ vương", "Trương Ngáo"],
        "answer": "Nghêu, Sò, Ốc, Hến",
        "explanation": "Đoạn trích này phê phán thói tham nhũng, cửa quyền của bọn quan lại địa phương."
    },
    {
        "question": "Chèo là loại hình nghệ thuật dân gian phổ biến nhất ở vùng nào?",
        "options": ["Đồng bằng Bắc Bộ", "Tây Nguyên", "Nam Bộ", "Miền Trung"],
        "answer": "Đồng bằng Bắc Bộ",
        "explanation": "Chèo gắn liền với sinh hoạt văn hóa làng quê ở Bắc Bộ."
    },
    {
        "question": "Trong bài 'Hương Sơn phong cảnh ca', Chu Mạnh Trinh gọi nơi này là gì?",
        "options": ["Nam thiên đệ nhất động", "Thiên đường hạ giới", "Chốn bồng lai", "Đệ nhất kì quan"],
        "answer": "Nam thiên đệ nhất động",
        "explanation": "Động Hương Tích được mệnh danh là hang động đẹp nhất trời Nam."
    },
    {
        "question": "Ai là tác giả của văn bản 'Bình Ngô đại cáo'?",
        "options": ["Nguyễn Trãi", "Lê Lợi", "Trần Hưng Đạo", "Nguyễn Du"],
        "answer": "Nguyễn Trãi",
        "explanation": "Nguyễn Trãi thừa lệnh Lê Lợi viết bản cáo để tuyên bố kết thúc kháng chiến chống quân Minh."
    },
    {
        "question": "Mục đích chính của văn bản Nghị luận là gì?",
        "options": ["Thuyết phục người đọc về một ý kiến, quan điểm", "Kể lại một câu chuyện", "Miêu tả phong cảnh",
                    "Bộc lộ cảm xúc đơn thuần"],
        "answer": "Thuyết phục người đọc về một ý kiến, quan điểm",
        "explanation": "Nghị luận dùng lý lẽ và bằng chứng để làm sáng tỏ một vấn đề."
    },
    {
        "question": "Trong sử thi 'O-đi-xê', vợ của O-đi-xê tên là gì?",
        "options": ["Pê-nê-lốp", "Hê-len", "Ăng-đrô-mác", "Ca-líp-xô"],
        "answer": "Pê-nê-lốp",
        "explanation": "Pê-nê-lốp là biểu tượng của lòng thủy chung son sắt."
    },
    {
        "question": "Bài thơ 'Tỏ lòng' (Phạm Ngũ Lão) thể hiện nội dung gì nổi bật?",
        "options": ["Hào khí Đông A của đời Trần", "Nỗi buồn mất nước", "Tình yêu đôi lứa", "Vẻ đẹp thiên nhiên"],
        "answer": "Hào khí Đông A của đời Trần",
        "explanation": "Bài thơ thể hiện khát vọng lập công danh và khí thế của quân đội nhà Trần."
    },
    {
        "question": "Nhân vật Thị Kính trong vở chèo 'Quan Âm Thị Kính' chịu nỗi oan gì?",
        "options": ["Oan giết chồng", "Oan trộm cắp", "Oan phản bội", "Oan bất hiếu"],
        "answer": "Oan giết chồng",
        "explanation": "Thị Kính bị khép tội giết chồng khi đang cầm dao xén sợi râu mọc ngược cho Thiện Sĩ."
    },
    {
        "question": "Trong 'Bình Ngô đại cáo', Nguyễn Trãi khẳng định chân lý độc lập dựa trên yếu tố nào?",
        "options": ["Văn hiến, lãnh thổ, phong tục, triều đại", "Sức mạnh quân sự", "Sự giúp đỡ của nước ngoài",
                    "Sự giàu có"],
        "answer": "Văn hiến, lãnh thổ, phong tục, triều đại",
        "explanation": "Đây là các yếu tố cơ bản xác định chủ quyền dân tộc."
    },
    {
        "question": "Từ Hán Việt 'Văn hiến' có nghĩa là gì?",
        "options": ["Truyền thống văn hóa lâu đời và tốt đẹp", "Sách vở cũ", "Người học rộng tài cao",
                    "Các quy tắc ứng xử"],
        "answer": "Truyền thống văn hóa lâu đời và tốt đẹp",
        "explanation": "Văn là văn chương, chữ nghĩa; hiến là người hiền tài."
    },
    {
        "question": "Thể loại 'Tùy bút' khác 'Truyện ngắn' ở điểm nào nhất?",
        "options": ["Tự do về cấu trúc, đậm chất cái tôi của tác giả", "Có cốt truyện phức tạp", "Nhiều nhân vật",
                    "Kết thúc có hậu"],
        "answer": "Tự do về cấu trúc, đậm chất cái tôi của tác giả",
        "explanation": "Tùy bút ghi chép tùy hứng, bộc lộ trực tiếp cảm xúc của người viết."
    },
    {
        "question": "Bài thơ 'Bánh trôi nước' của Hồ Xuân Hương sử dụng ẩn dụ để nói về điều gì?",
        "options": ["Thân phận người phụ nữ xã hội cũ", "Cách làm bánh", "Vẻ đẹp thiên nhiên", "Tình yêu quê hương"],
        "answer": "Thân phận người phụ nữ xã hội cũ",
        "explanation": "Chiếc bánh trôi 'bảy nổi ba chìm' là ẩn dụ cho cuộc đời bấp bênh của phụ nữ xưa."
    },
    {
        "question": "Trong văn bản 'Đăm Săn đi bắt Nữ thần Mặt Trời', mục đích của Đăm Săn là gì?",
        "options": ["Muốn cưới Nữ thần về làm vợ lẽ", "Muốn thách đấu sức mạnh", "Muốn xin ánh sáng cho làng",
                    "Muốn chiếm lấy vàng bạc"],
        "answer": "Muốn cưới Nữ thần về làm vợ lẽ",
        "explanation": "Khát vọng chinh phục thiên nhiên của người anh hùng sử thi."
    },
    {
        "question": "Khái niệm 'Điểm tựa' trong văn bản nghị luận xã hội thường dùng để chỉ điều gì?",
        "options": ["Cơ sở về đạo đức, niềm tin trong cuộc sống", "Một vật để tựa vào", "Người giúp đỡ về tài chính",
                    "Vị trí địa lý"],
        "answer": "Cơ sở về đạo đức, niềm tin trong cuộc sống",
        "explanation": "Điểm tựa tinh thần giúp con người vượt qua nghịch cảnh."
    },
    {
        "question": "Trong nghệ thuật Chèo, nhân vật nào thường mang lại tiếng cười và sự phê phán?",
        "options": ["Nhân vật Hề", "Nhân vật Đào", "Nhân vật Kép", "Nhân vật Lão"],
        "answer": "Nhân vật Hề",
        "explanation": "Hề Chèo vừa gây cười vừa mang tính châm biếm sâu sắc."
    },
    {
        "question": "Phông nền của các câu chuyện Thần thoại thường là gì?",
        "options": ["Thời gian phiếm chỉ, không gian vũ trụ", "Năm 1945", "Thời hiện đại", "Địa danh cụ thể"],
        "answer": "Thời gian phiếm chỉ, không gian vũ trụ",
        "explanation": "Thần thoại diễn ra vào thuở sơ khai của thế giới."
    },
    {
        "question": "Bài thơ 'Tại lầu Hoàng Hạc tiễn Mạnh Hạo Nhiên đi Quảng Lăng' của Lý Bạch thuộc thể loại nào?",
        "options": ["Thơ Đường luật", "Thơ tự do", "Sử thi", "Kịch"],
        "answer": "Thơ Đường luật",
        "explanation": "Đây là bài thơ thất ngôn tứ tuyệt nổi tiếng của 'Thi tiên' Lý Bạch."
    },
    {
        "question": "Tác giả của 'Truyện Kiều' là ai?",
        "options": ["Nguyễn Du", "Nguyễn Trãi", "Nguyễn Khuyến", "Nguyễn Đình Chiểu"],
        "answer": "Nguyễn Du",
        "explanation": "Nguyễn Du là Đại thi hào dân tộc, Danh nhân văn hóa thế giới."
    },
    {
        "question": "Trong 'Truyện Kiều', Thúy Kiều đã bán mình để làm gì?",
        "options": ["Chuộc cha và em trai", "Lấy tiền giúp người nghèo", "Đi du ngoạn", "Để nổi tiếng"],
        "answer": "Chuộc cha và em trai",
        "explanation": "Hành động thể hiện chữ Hiếu của Thúy Kiều."
    }

]