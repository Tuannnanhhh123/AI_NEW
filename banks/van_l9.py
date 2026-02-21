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
        "question": "Bản chất của tình huống truyện trong 'Làng' của Kim Lân là gì?",
        "options": ["Xung đột giữa tình yêu làng và lòng yêu nước trong tâm hồn người nông dân", "Xung đột giữa ông Hai và những người dân trong làng tản cư", "Xung đột giữa cá nhân ông Hai và chính quyền địa phương", "Xung đột giữa gia đình ông Hai và thực dân Pháp"],
        "answer": "Xung đột giữa tình yêu làng và lòng yêu nước trong tâm hồn người nông dân",
        "explanation": "Tình yêu làng vốn thống nhất với yêu nước, nhưng tin làng theo giặc buộc nhân vật phải lựa chọn quyết liệt."
    },
    {
        "question": "Trong 'Chuyện người con gái Nam Xương', lời thề của Vũ Nương trước khi trèo xuống bến Hoàng Giang thể hiện điều gì?",
        "options": ["Sự phản kháng cuối cùng nhằm bảo vệ danh dự và nhân phẩm", "Sự tuyệt vọng và buông xuôi trước định mệnh", "Lòng căm thù đối với Trương Sinh", "Khát vọng muốn được các vị thần giúp đỡ"],
        "answer": "Sự phản kháng cuối cùng nhằm bảo vệ danh dự và nhân phẩm",
        "explanation": "Lời thề chứng minh cho sự trong sạch, lấy cái chết để khẳng định giá trị con người."
    },
    {
        "question": "Ý nghĩa triết lý của hình ảnh 'Bãi bồi bên kia sông' trong truyện ngắn 'Bến quê' là gì?",
        "options": ["Vẻ đẹp bình dị, gần gũi của quê hương mà con người thường bỏ qua", "Một vùng đất xa xôi không thể chạm tới", "Ký ức tuổi thơ đau buồn của nhân vật Nhĩ", "Biểu tượng cho sự nghèo khó của vùng nông thôn"],
        "answer": "Vẻ đẹp bình dị, gần gũi của quê hương mà con người thường bỏ qua",
        "explanation": "Con người thường ham chuộng những thứ xa vời mà quên mất giá trị bền vững ngay bên cạnh."
    },
    {
        "question": "Bút pháp nghệ thuật nổi bật nhất trong đoạn trích 'Chị em Thúy Kiều' là gì?",
        "options": ["Ước lệ tượng trưng và đòn bẩy", "Tả cảnh ngụ tình và nhân hóa", "Hiện thực nghiêm khắc", "Phóng đại và so sánh trực tiếp"],
        "answer": "Ước lệ tượng trưng và đòn bẩy",
        "explanation": "Dùng vẻ đẹp của Vân để làm nền (đòn bẩy) tôn vinh vẻ đẹp tuyệt đỉnh về tài lẫn sắc của Kiều."
    },
    {
        "question": "Hàm ý của câu 'Cơm sôi rồi, chắt nước giùm cái!' của bé Thu trong 'Chiếc lược ngà' là gì?",
        "options": ["Lời cầu cứu gián tiếp vì bé Thu không thể tự làm", "Sự thừa nhận ông Sáu là người trong gia đình", "Lời thách thức đối với ông Sáu", "Thông báo đơn thuần về tình trạng nồi cơm"],
        "answer": "Lời cầu cứu gián tiếp vì bé Thu không thể tự làm",
        "explanation": "Vì không chịu gọi 'Ba', bé Thu rơi vào tình huống buộc phải nói trống không nhưng mang hàm ý nhờ vả."
    },
    {
        "question": "Hình ảnh 'Đầu súng trăng treo' trong bài thơ 'Đồng chí' mang tính chất nghệ thuật gì?",
        "options": ["Sự kết hợp giữa hiện thực khắc nghiệt và cảm hứng lãng mạn", "Sự đối lập giữa ánh sáng và bóng tối", "Biểu tượng của sự chết chóc trong chiến tranh", "Sự miêu tả khách quan về thiên nhiên chiến trường"],
        "answer": "Sự kết hợp giữa hiện thực khắc nghiệt và cảm hứng lãng mạn",
        "explanation": "Súng (chiến sĩ) và Trăng (thi sĩ) hòa quyện tạo nên vẻ đẹp của lý tưởng và tâm hồn người lính."
    },
    {
        "question": "Sự vận động của hình tượng 'Trăng' từ đầu đến cuối bài thơ 'Ánh trăng' của Nguyễn Duy thể hiện điều gì?",
        "options": ["Sự chuyển biến từ tri kỷ quá khứ sang người dưng hiện tại và cái giật mình thức tỉnh", "Sự thay đổi của thiên nhiên theo thời gian", "Sự già đi của con người", "Vẻ đẹp không bao giờ thay đổi của vũ trụ"],
        "answer": "Sự chuyển biến từ tri kỷ quá khứ sang người dưng hiện tại và cái giật mình thức tỉnh",
        "explanation": "Cái 'giật mình' ở cuối bài là giá trị nhân văn cao nhất, nhắc nhở về đạo lý sống thủy chung."
    },
    {
        "question": "Trong 'Lặng lẽ Sa Pa', nhân vật anh thanh niên từ chối vẽ mình vì lẽ gì?",
        "options": ["Anh thấy mình chỉ là một trong nhiều người đang cống hiến âm thầm", "Anh là người khiêm tốn đến mức nhút nhát", "Anh không tin vào tài năng của bác họa sĩ", "Anh sợ lộ bí mật công tác"],
        "answer": "Anh thấy mình chỉ là một trong nhiều người đang cống hiến âm thầm",
        "explanation": "Quan niệm về sự cống hiến thầm lặng của anh mang tính đại diện cho cả một thế hệ."
    },
    {
        "question": "Đặc trưng của thể loại 'Truyền kỳ' thể hiện như thế nào trong kết thúc của Vũ Nương?",
        "options": ["Dùng yếu tố kỳ ảo để an ủi người lương thiện nhưng vẫn giữ nguyên bi kịch thực tại", "Làm cho câu chuyện trở nên phi thực tế hoàn toàn", "Xóa bỏ mọi đau khổ của nhân vật chính", "Trừng phạt kẻ ác bằng phép thuật"],
        "answer": "Dùng yếu tố kỳ ảo để an ủi người lương thiện nhưng vẫn giữ nguyên bi kịch thực tại",
        "explanation": "Vũ Nương hiện về rồi biến mất, bi kịch gia đình tan vỡ vẫn là sự thật không thể cứu vãn."
    },
    {
        "question": "Phép liên kết văn bản nào được sử dụng chủ yếu trong đoạn thơ 'Nhóm bếp lửa... / Nhóm niềm yêu thương... / Nhóm dậy cả những tâm tình...'?",
        "options": ["Phép điệp và liên tưởng", "Phép thế", "Phép nối", "Phép đồng nghĩa"],
        "answer": "Phép điệp và liên tưởng",
        "explanation": "Từ 'Nhóm' được lặp lại nhiều lần với các lớp nghĩa chuyển hóa từ cụ thể đến trừu tượng."
    },
    {
        "question": "Cách sử dụng từ ngữ trong 'Bài thơ về tiểu đội xe không kính' mang đậm phong cách nào?",
        "options": ["Khẩu ngữ, tự nhiên và giàu tính nhạc", "Trang trọng, cổ điển", "Hàn lâm, bác học", "Bi lụy, đau thương"],
        "answer": "Khẩu ngữ, tự nhiên và giàu tính nhạc",
        "explanation": "Sử dụng các cấu trúc: 'không có... ừ thì... chưa cần...' tạo giọng điệu ngang tàng, trẻ trung."
    },
    {
        "question": "Trong bài thơ 'Sang thu', hình ảnh 'Hương ổi / Phả vào trong gió se' gợi cảm giác gì về không gian?",
        "options": ["Sự vận động nhẹ nhàng, tinh tế của thời khắc chuyển mùa", "Sự ngột ngạt của không gian làng quê", "Sự lạnh lẽo của mùa đông sắp tới", "Sự tươi mới của mùa xuân"],
        "answer": "Sự vận động nhẹ nhàng, tinh tế của thời khắc chuyển mùa",
        "explanation": "Từ 'phả' gợi sự đậm đặc, chủ động xâm chiếm không gian của hương vị quê hương."
    },
    {
        "question": "Nghệ thuật xây dựng nhân vật Quang Trung trong 'Hoàng Lê nhất thống chí' nổi bật ở điểm nào?",
        "options": ["Sự kết hợp giữa vẻ đẹp của một vị vua anh minh và một thiên tài quân sự", "Sự miêu tả tâm lý phức tạp, đầy mâu thuẫn", "Việc tôn thờ các yếu tố siêu nhiên giúp nhà vua chiến thắng", "Việc hạ thấp vai trò của các tướng sĩ để làm nổi bật nhà vua"],
        "answer": "Sự kết hợp giữa vẻ đẹp của một vị vua anh minh và một thiên tài quân sự",
        "explanation": "Vua Quang Trung hiện lên với trí tuệ sáng suốt, hành động quyết đoán và tài cầm quân thần tốc."
    },
    {
        "question": "Bi kịch của nhân vật ông Hai trong truyện ngắn 'Làng' đạt đến đỉnh điểm khi nào?",
        "options": ["Khi ông bị bà chủ nhà đuổi khéo vì tin đồn làng theo giặc", "Khi ông vừa nghe tin làng Chợ Dầu theo Tây", "Khi ông phải đi tản cư", "Khi làng của ông bị đốt sạch"],
        "answer": "Khi ông bị bà chủ nhà đuổi khéo vì tin đồn làng theo giặc",
        "explanation": "Lúc này xung đột 'đi đâu bây giờ' đẩy nhân vật vào thế tuyệt lộ, buộc phải khẳng định 'Làng thì yêu thật, nhưng làng theo Tây thì phải thù'."
    },
    {
        "question": "Điểm chung về tư tưởng giữa 'Mùa xuân nho nhỏ' và 'Viếng lăng Bác' là gì?",
        "options": ["Khát vọng cống hiến và sự gắn kết giữa cá nhân với cái chung", "Nỗi buồn trước sự ra đi của các bậc vĩ nhân", "Sự ca ngợi vẻ đẹp của thiên nhiên đất nước", "Lòng tự hào về sức mạnh của quân đội"],
        "answer": "Khát vọng cống hiến và sự gắn kết giữa cá nhân với cái chung",
        "explanation": "Cả hai bài thơ đều thể hiện ước nguyện được hòa nhập, dâng hiến phần nhỏ bé của mình cho cuộc đời chung."
    },
    {
        "question": "Trong 'Những ngôi sao xa xôi', tâm trạng của Phương Định sau mỗi lần phá bom thể hiện phẩm chất gì?",
        "options": ["Sự dũng cảm đến mức bình thản và tâm hồn nhạy cảm", "Sự hoảng loạn được che giấu", "Sự tự phụ về chiến công", "Sự vô cảm trước cái chết"],
        "answer": "Sự dũng cảm đến mức bình thản và tâm hồn nhạy cảm",
        "explanation": "Cô coi việc đối mặt với cái chết là 'định mức', nhưng vẫn giữ được nét nữ tính, yêu đời."
    },
    {
        "question": "Tính đa nghĩa của từ 'Lộc' trong 'Mùa xuân nho nhỏ' (Lộc giắt đầy trên lưng / Lộc trải dài nương mạ) là:",
        "options": ["Vừa là chồi non, vừa là sức sống cách mạng và thành quả lao động", "Chỉ là quà tặng của thiên nhiên", "Chỉ sự may mắn về tiền bạc", "Chỉ các loại lá ngụy trang của quân đội"],
        "answer": "Vừa là chồi non, vừa là sức sống cách mạng và thành quả lao động",
        "explanation": "Lộc tượng trưng cho sự sinh sôi, phát triển của đất nước trên hai mặt trận: chiến đấu và sản xuất."
    },
    {
        "question": "Sử dụng lời dẫn gián tiếp thay cho lời dẫn trực tiếp nhằm mục đích gì trong văn bản tự sự?",
        "options": ["Để người kể chuyện có thể tóm lược, điều chỉnh nội dung cho phù hợp với mạch kể", "Để làm cho lời nói của nhân vật sống động hơn", "Để đảm bảo tính khách quan tuyệt đối", "Để kéo dài dung lượng của văn bản"],
        "answer": "Để người kể chuyện có thể tóm lược, điều chỉnh nội dung cho phù hợp với mạch kể",
        "explanation": "Lời dẫn gián tiếp giúp người viết linh hoạt hơn trong việc truyền tải ý nghĩa lời nói mà không cần giữ nguyên văn."
    },
    {
        "question": "Trong 'Nói với con', việc dùng hình ảnh 'Đục đá kê cao quê hương' có ý nghĩa gì?",
        "options": ["Sự kiên cường xây dựng quê hương từ khó khăn, gian khổ", "Công việc nặng nhọc của người miền núi", "Lối sống lạc hậu, thô sơ", "Sự tàn phá thiên nhiên để sinh tồn"],
        "answer": "Sự kiên cường xây dựng quê hương từ khó khăn, gian khổ",
        "explanation": "Hình ảnh ẩn dụ cho ý chí bền bỉ, lấy khó khăn làm nền tảng để nâng tầm quê hương."
    },
    {
        "question": "Tại sao bài thơ 'Đoàn thuyền đánh cá' lại được coi là 'khúc ca về lao động'?",
        "options": ["Vì tác giả xây dựng hình ảnh người lao động với tầm vóc sánh ngang vũ trụ", "Vì bài thơ liệt kê đầy đủ các loài cá biển", "Vì bài thơ miêu tả kỹ thuật đánh cá đêm", "Vì bài thơ có nhịp điệu giống như tiếng sóng"],
        "answer": "Vì tác giả xây dựng hình ảnh người lao động với tầm vóc sánh ngang vũ trụ",
        "explanation": "Con người không còn nhỏ bé trước thiên nhiên mà làm chủ biển cả bằng niềm vui phấn khởi."
    },
    {
        "question": "Thành phần biệt lập 'Tình thái' trong câu văn thể hiện:",
        "options": ["Cách nhìn của người nói đối với độ tin cậy của sự việc được nói đến", "Thái độ kính trọng của người nói đối với người nghe", "Sự giải thích thêm cho một chi tiết nào đó", "Tiếng gọi để bắt đầu cuộc hội thoại"],
        "answer": "Cách nhìn của người nói đối với độ tin cậy của sự việc được nói đến",
        "explanation": "Ví dụ các từ: có lẽ, chắc là, hình như..."
    },
    {
        "question": "Bi kịch của Vũ Nương là bi kịch mang tính thời đại vì:",
        "options": ["Nó phản ánh sự bất công của chế độ nam quyền và chiến tranh phong kiến", "Nó chỉ là một sự hiểu lầm tình cờ trong gia đình", "Nó cho thấy sự mê tín dị đoan của con người thời bấy giờ", "Nó chứng minh phụ nữ không nên lấy chồng là lính"],
        "answer": "Nó phản ánh sự bất công của chế độ nam quyền và chiến tranh phong kiến",
        "explanation": "Vũ Nương là nạn nhân của tư tưởng 'trọng nam khinh nữ' và cuộc chiến phi nghĩa chia cắt gia đình."
    },
    {
        "question": "Trong bài thơ 'Con cò', hình ảnh con cò ở đoạn cuối bài thơ mang ý nghĩa gì?",
        "options": ["Sự hóa thân của lòng mẹ, luôn theo sát con trên mọi dặm đường", "Sự vất vả của người phụ nữ nông thôn", "Cái chết và sự tái sinh", "Biểu tượng của vẻ đẹp thanh cao"],
        "answer": "Sự hóa thân của lòng mẹ, luôn theo sát con trên mọi dặm đường",
        "explanation": "'Con dù lớn vẫn là con của mẹ / Đi hết đời lòng mẹ vẫn theo con'."
    },
    {
        "question": "Nghệ thuật 'Tả cảnh ngụ tình' trong khổ cuối bài 'Ánh trăng' tập trung vào hình ảnh nào?",
        "options": ["Trăng cứ tròn vành vạnh và cái giật mình", "Ánh điện cửa gương", "Bầu trời tối om", "Dòng sông và đồng ruộng"],
        "answer": "Trăng cứ tròn vành vạnh và cái giật mình",
        "explanation": "Trăng tròn là sự thủy chung, im phăng phắc là sự nghiêm khắc nhắc nhở con người."
    },
    {
        "question": "Điểm độc đáo trong việc chọn 'xe không kính' làm hình tượng trung tâm của Phạm Tiến Duật là:",
        "options": ["Lấy cái khiếm khuyết để làm nổi bật tinh thần bất khuất và sự hiên ngang", "Để miêu tả sự nghèo nàn của trang bị quân sự", "Để tạo ra tiếng cười giải trí cho người lính", "Để phê phán sự tàn khốc của bom đạn"],
        "answer": "Lấy cái khiếm khuyết để làm nổi bật tinh thần bất khuất và sự hiên ngang",
        "explanation": "Xe không kính không làm chậm bước tiến, trái lại càng làm rõ hơn ý chí 'vì miền Nam' của người lính."
    }
,

    {
        "question": "Trong bài thơ 'Đồng chí', các anh bộ đội vốn xuất thân từ đâu?",
        "options": ["Nông dân", "Công nhân", "Trí thức", "Thị dân"],
        "answer": "Nông dân",
        "explanation": "Câu thơ 'Quê hương anh nước mặn đồng chua / Làng tôi nghèo đất cày lên sỏi đá' khẳng định gốc gác nông dân."
    },
    {
        "question": "Hình ảnh 'Trăng' trong cuối bài thơ 'Đồng chí' biểu tượng cho điều gì?",
        "options": ["Hòa bình và vẻ đẹp tâm hồn", "Ánh sáng soi đường", "Sự lạnh lẽo của đêm tối", "Vũ khí của người lính"],
        "answer": "Hòa bình và vẻ đẹp tâm hồn",
        "explanation": "Trăng treo đầu súng gợi sự kết hợp giữa chất thép và chất tình, giữa chiến tranh và hòa bình."
    },
    {
        "question": "Từ 'Đoàn' trong 'Đoàn thuyền đánh cá' chỉ số lượng như thế nào?",
        "options": ["Nhiều chiếc thuyền cùng đi", "Chỉ một chiếc thuyền", "Hai chiếc thuyền", "Không xác định được số lượng"],
        "answer": "Nhiều chiếc thuyền cùng đi",
        "explanation": "Từ 'Đoàn' gợi không khí lao động tập thể nhộn nhịp, quy mô lớn."
    },
    {
        "question": "Trong bài 'Đoàn thuyền đánh cá', công việc của người dân chài kết thúc vào lúc nào?",
        "options": ["Khi bình minh", "Khi hoàng hôn", "Lúc nửa đêm", "Buổi chiều tà"],
        "answer": "Khi bình minh",
        "explanation": "Câu thơ: 'Sao mờ kéo lưới kịp trời sáng / Mặt trời đội biển nhô màu mới'."
    },
    {
        "question": "Đặc điểm của nhân vật anh thanh niên trong 'Lặng lẽ Sa Pa' là gì?",
        "options": ["Yêu nghề và hiếu khách", "Sợ cô đơn", "Thích khoe khoang", "Lười biếng"],
        "answer": "Yêu nghề và hiếu khách",
        "explanation": "Anh làm việc một mình trên đỉnh núi cao nhưng luôn nhiệt tình, mến khách."
    },
    {
        "question": "Thành phần phụ chú trong câu: 'Lan - bạn thân của tôi - học rất giỏi.' là gì?",
        "options": ["bạn thân của tôi", "Lan", "học rất giỏi", "Lan - bạn thân"],
        "answer": "bạn thân của tôi",
        "explanation": "Thành phần này bổ sung thông tin cho danh từ 'Lan'."
    },
    {
        "question": "Tác phẩm 'Bến quê' của Nguyễn Minh Châu thuộc thể loại nào?",
        "options": ["Truyện ngắn", "Thơ", "Kịch", "Tùy bút"],
        "answer": "Truyện ngắn",
        "explanation": "Đây là truyện ngắn mang tính triết lý sâu sắc về đời người."
    },
    {
        "question": "Chi tiết 'chiếc bóng' trong 'Chuyện người con gái Nam Xương' đóng vai trò gì?",
        "options": ["Thắt nút và mở nút câu chuyện", "Làm đẹp cho nhân vật", "Chỉ là chi tiết phụ", "Để hù dọa Trương Sinh"],
        "answer": "Thắt nút và mở nút câu chuyện",
        "explanation": "Chiếc bóng khiến Trương Sinh nghi ngờ (thắt nút) và cũng chính nó giúp giải oan cho Vũ Nương (mở nút)."
    },
    {
        "question": "Trong 'Truyện Kiều', Nguyễn Du miêu tả Thúy Vân 'Hoa cười ngọc thốt đoan trang' nhằm mục đích gì?",
        "options": ["Gợi vẻ đẹp phúc hậu, êm đềm", "Gợi vẻ đẹp sắc sảo, trí tuệ", "Gợi số phận đau khổ", "Để so sánh với hoa hồng"],
        "answer": "Gợi vẻ đẹp phúc hậu, êm đềm",
        "explanation": "Vẻ đẹp của Vân tạo sự hòa hợp với thiên nhiên, báo trước cuộc đời bình lặng."
    },
    {
        "question": "Thành phần biệt lập 'Phụ chú' thường ngăn cách với các thành phần khác bởi dấu gì?",
        "options": ["Dấu gạch ngang, ngoặc đơn hoặc phẩy", "Dấu chấm hỏi", "Dấu ngoặc kép", "Dấu chấm phẩy"],
        "answer": "Dấu gạch ngang, ngoặc đơn hoặc phẩy",
        "explanation": "Dấu hiệu nhận biết này giúp phân biệt phụ chú với nội dung chính."
    },
    {
        "question": "Bài thơ 'Con cò' của Chế Lan Viên viết theo thể thơ nào?",
        "options": ["Thơ tự do", "Thơ lục bát", "Thơ 7 chữ", "Thơ 8 chữ"],
        "answer": "Thơ tự do",
        "explanation": "Thể thơ tự do giúp tác giả diễn đạt linh hoạt các cung bậc cảm xúc."
    },
    {
        "question": "Hình ảnh 'Mặt trời' trong câu 'Ngày ngày mặt trời đi qua trên lăng' là mặt trời của:",
        "options": ["Thiên nhiên", "Bác Hồ", "Nhân dân", "Cách mạng"],
        "answer": "Thiên nhiên",
        "explanation": "Đây là mặt trời thực của vũ trụ, soi sáng thế gian."
    },
    {
        "question": "Trong 'Chiếc lược ngà', vì sao bé Thu không nhận cha lúc mới gặp?",
        "options": ["Vì vết sẹo trên mặt ông Sáu", "Vì bà ngoại bảo thế", "Vì bé Thu bị mất trí nhớ", "Vì ông Sáu đi lâu quá"],
        "answer": "Vì vết sẹo trên mặt ông Sáu",
        "explanation": "Vết sẹo làm ông Sáu không giống với bức ảnh chụp chung với má mà bé Thu biết."
    },
    {
        "question": "Từ 'vàng' trong 'Một trời hoa phượng vàng' và 'nhẫn vàng' là hiện tượng gì?",
        "options": ["Từ đồng âm", "Từ nhiều nghĩa", "Từ trái nghĩa", "Từ mượn"],
        "answer": "Từ đồng âm",
        "explanation": "Một từ chỉ màu sắc, một từ chỉ kim loại, chúng chỉ giống nhau về âm thanh."
    },
    {
        "question": "Từ 'xuân' trong 'Mùa xuân nho nhỏ' mang nghĩa ẩn dụ cho điều gì?",
        "options": ["Sức trẻ và sự cống hiến", "Mùa đầu tiên trong năm", "Tuổi già", "Sự kết thúc"],
        "answer": "Sức trẻ và sự cống hiến",
        "explanation": "Ước nguyện làm một mùa xuân nhỏ góp vào mùa xuân lớn của đất nước."
    },
    {
        "question": "Tác giả của truyện ngắn 'Những ngôi sao xa xôi' là ai?",
        "options": ["Lê Minh Khuê", "Kim Lân", "Nguyễn Quang Sáng", "Nguyễn Minh Châu"],
        "answer": "Lê Minh Khuê",
        "explanation": "Bà là nhà văn nữ chuyên viết về cuộc sống chiến đấu ở Trường Sơn."
    },
    {
        "question": "Câu thơ 'Sấm cũng bớt bất ngờ / Trên hàng cây đã đứng tuổi' sử dụng biện pháp gì?",
        "options": ["Ẩn dụ", "So sánh", "Hoán dụ", "Điệp ngữ"],
        "answer": "Ẩn dụ",
        "explanation": "Sấm chỉ những biến động cuộc đời, hàng cây đứng tuổi chỉ những người từng trải."
    },
    {
        "question": "Phương thức biểu đạt chính của văn bản 'Phong cách Hồ Chí Minh' là gì?",
        "options": ["Nghị luận", "Tự sự", "Miêu tả", "Biểu cảm"],
        "answer": "Nghị luận",
        "explanation": "Văn bản dùng lý lẽ thuyết phục về vẻ đẹp lối sống của Bác."
    },
    {
        "question": "Trong 'Nói với con', tác giả dùng cụm từ 'người đồng mình' để chỉ ai?",
        "options": ["Người vùng mình, người quê mình", "Người nước ngoài", "Người lạ", "Người thành phố"],
        "answer": "Người vùng mình, người quê mình",
        "explanation": "Cách gọi thân thương, mộc mạc của người miền núi."
    },
    {
        "question": "Chi tiết 'Lục Vân Tiên cứu Kiều Nguyệt Nga' thể hiện phẩm chất gì của nhân vật?",
        "options": ["Hào hiệp, chính nghĩa", "Nhát gan", "Ham giàu sang", "Thích thể hiện"],
        "answer": "Hào hiệp, chính nghĩa",
        "explanation": "Thấy việc nghĩa không làm không phải là anh hùng."
    },
    {
        "question": "Câu 'Học, học nữa, học mãi.' là câu gì?",
        "options": ["Câu rút gọn", "Câu ghép", "Câu cảm thán", "Câu hỏi"],
        "answer": "Câu rút gọn",
        "explanation": "Câu đã được lược bỏ thành phần chủ ngữ (Chúng ta)."
    },
    {
        "question": "Bài thơ 'Viếng lăng Bác' có giọng điệu như thế nào?",
        "options": ["Trang trọng, tha thiết, thành kính", "Hào hùng, mạnh mẽ", "Vui tươi, nhí nhảnh", "Mỉa mai, châm biếm"],
        "answer": "Trang trọng, tha thiết, thành kính",
        "explanation": "Phù hợp với không khí thiêng liêng khi vào lăng viếng Bác."
    },
    {
        "question": "Từ 'in' trong 'in ấn' và 'in hệt' có quan hệ gì?",
        "options": ["Từ đồng âm", "Từ nhiều nghĩa", "Từ trái nghĩa", "Từ mượn"],
        "answer": "Từ đồng âm",
        "explanation": "Một từ là động từ (in ấn), một từ là tính từ mức độ (in hệt)."
    },
    {
        "question": "Trong bài thơ 'Bếp lửa', hình ảnh 'Bếp lửa' gắn liền với hình ảnh nào?",
        "options": ["Người bà", "Người mẹ", "Người cha", "Người thầy"],
        "answer": "Người bà",
        "explanation": "Bếp lửa là biểu tượng của tình bà ấm áp, nuôi dưỡng cháu khôn lớn."
    },
    {
        "question": "Kiểu câu 'Ôi, quê hương đẹp quá!' dùng để làm gì?",
        "options": ["Bộc lộ cảm xúc", "Hỏi thông tin", "Kể sự việc", "Đưa ra mệnh lệnh"],
        "answer": "Bộc lộ cảm xúc",
        "explanation": "Dấu chấm cảm và từ 'Ôi' cho thấy mục đích bộc lộ tình cảm."
    }
,
    {
        "question": "Tác giả của tác phẩm 'Chuyện người con gái Nam Xương' là ai?",
        "options": ["Nguyễn Dữ", "Nguyễn Trãi", "Nguyễn Du", "Đoàn Thị Điểm"],
        "answer": "Nguyễn Dữ",
        "explanation": "Tác phẩm trích trong tập 'Truyền kỳ mạn lục' của Nguyễn Dữ."
    },
    {
        "question": "Trong bài thơ 'Đồng chí', chi tiết nào là biểu tượng đẹp nhất về tình đồng đội?",
        "options": ["Đầu súng trăng treo", "Áo anh rách vai", "Quần tôi có vài mảnh vá", "Chân không giày"],
        "answer": "Đầu súng trăng treo",
        "explanation": "Đây là hình ảnh kết hợp giữa thực tại chiến đấu và tâm hồn lãng mạn của người lính."
    },
    {
        "question": "Nhân vật Vũ Nương trong 'Chuyện người con gái Nam Xương' bị chồng nghi oan về điều gì?",
        "options": ["Hư hỏng, thiếu thủy chung", "Lấy trộm tiền bạc", "Bỏ bê con cái", "Không chăm sóc mẹ chồng"],
        "answer": "Hư hỏng, thiếu thủy chung",
        "explanation": "Trương Sinh nghe lời ngây thơ của con trẻ nên đã nghi oan cho vợ."
    },
    {
        "question": "Phương thức biểu đạt chính của bài thơ 'Đoàn thuyền đánh cá' là gì?",
        "options": ["Biểu cảm kết hợp miêu tả", "Tự sự", "Nghị luận", "Thuyết minh"],
        "answer": "Biểu cảm kết hợp miêu tả",
        "explanation": "Bài thơ bộc lộ cảm xúc hào hứng trước vẻ đẹp thiên nhiên và lao động."
    },
    {
        "question": "Trong 'Truyện Kiều', Thúy Kiều mang họ gì?",
        "options": ["Vương", "Nguyễn", "Trần", "Lê"],
        "answer": "Vương",
        "explanation": "Gia đình Kiều gồm Vương viên ngoại, Vương Quan, Thúy Vân và Thúy Kiều."
    },
    {
        "question": "Từ 'đầu' trong câu 'Đầu súng trăng treo' được dùng theo nghĩa nào?",
        "options": ["Nghĩa gốc", "Nghĩa chuyển (ẩn dụ)", "Nghĩa chuyển (hoán dụ)",
                    "Nghĩa chuyển (phương thức so sánh)"],
        "answer": "Nghĩa gốc",
        "explanation": "Chỉ bộ phận tận cùng phía trên của họng súng."
    },
    {
        "question": "Bài thơ 'Bếp lửa' của Bằng Việt gợi lại kỷ niệm về tình cảm giữa ai với ai?",
        "options": ["Bà và cháu", "Mẹ và con", "Anh và em", "Thầy và trò"],
        "answer": "Bà và cháu",
        "explanation": "Xuyên suốt bài thơ là nỗi nhớ về những năm tháng sống bên bà và bếp lửa."
    },
    {
        "question": "Nội dung chính của bài thơ 'Bài thơ về tiểu đội xe không kính' là gì?",
        "options": ["Vẻ đẹp hiên ngang, lạc quan của người lính lái xe", "Sự khốc liệt của chiến tranh",
                    "Tình yêu quê hương đất nước", "Vẻ đẹp của thiên nhiên Trường Sơn"],
        "answer": "Vẻ đẹp hiên ngang, lạc quan của người lính lái xe",
        "explanation": "Khắc họa tư thế ung dung, bất chấp hiểm nguy của những chiến sĩ lái xe."
    },
    {
        "question": "Câu thơ 'Làn thu thủy, nét xuân sơn' miêu tả vẻ đẹp bộ phận nào của Thúy Kiều?",
        "options": ["Mắt và lông mày", "Tóc và làn da", "Khuôn mặt và nụ cười", "Dáng đi và giọng nói"],
        "answer": "Mắt và lông mày",
        "explanation": "Thu thủy là mắt trong như nước mùa thu, xuân sơn là lông mày thanh tú như núi mùa xuân."
    },
    {
        "question": "Thành phần biệt lập 'Cảm thán' trong câu 'Chao ôi, hoa đại đẹp quá!' là từ nào?",
        "options": ["Chao ôi", "Hoa đại", "Đẹp", "Quá"],
        "answer": "Chao ôi",
        "explanation": "Từ dùng để bộc lộ trực tiếp thái độ, cảm xúc của người nói."
    },
    {
        "question": "Trong văn bản 'Làng' của Kim Lân, nhân vật ông Hai luôn tự hào về điều gì?",
        "options": ["Làng Chợ Dầu", "Sức khỏe của mình", "Các con của mình", "Sự giàu có của gia đình"],
        "answer": "Làng Chợ Dầu",
        "explanation": "Ông Hai có thói quen khoe làng, một biểu hiện của tình yêu làng quê gắn liền với yêu nước."
    },
    {
        "question": "Phép tu từ nào được dùng trong câu 'Mặt trời của bắp thì nằm trên đồi / Mặt trời của mẹ, em nằm trên lưng'?",
        "options": ["Ẩn dụ", "Hoán dụ", "So sánh", "Nhân hóa"],
        "answer": "Ẩn dụ",
        "explanation": "Đứa con được ví như 'mặt trời' mang lại nguồn sống và ánh sáng cho mẹ."
    },
    {
        "question": "Ai là tác giả của văn bản 'Lặng lẽ Sa Pa'?",
        "options": ["Nguyễn Thành Long", "Nguyễn Minh Châu", "Nguyễn Quang Sáng", "Kim Lân"],
        "answer": "Nguyễn Thành Long",
        "explanation": "Truyện ngắn ca ngợi những người lao động thầm lặng trên đỉnh Yên Sơn."
    },
    {
        "question": "Trong 'Chiếc lược ngà', vật kỷ niệm cuối cùng ông Sáu gửi cho con là gì?",
        "options": ["Cái lược bằng ngà voi", "Một bức ảnh", "Một chiếc nhẫn", "Một bộ quần áo"],
        "answer": "Cái lược bằng ngà voi",
        "explanation": "Chiếc lược là kết tinh tình phụ tử thiêng liêng trong chiến tranh."
    },
    {
        "question": "Từ 'Xuân' trong 'Mùa xuân nho nhỏ' được hiểu theo nghĩa nào?",
        "options": ["Cả nghĩa gốc và nghĩa ẩn dụ", "Chỉ nghĩa gốc (mùa xuân của đất trời)",
                    "Chỉ nghĩa ẩn dụ (sự cống hiến)", "Nghĩa hoán dụ"],
        "answer": "Cả nghĩa gốc và nghĩa ẩn dụ",
        "explanation": "Vừa là mùa xuân thiên nhiên, vừa là sức trẻ và tâm hồn con người đóng góp cho đời."
    },
    {
        "question": "Thành phần biệt lập 'Gọi - đáp' dùng để làm gì?",
        "options": ["Thiết lập hoặc duy trì quan hệ giao tiếp", "Bộc lộ cảm xúc", "Nêu ý kiến nhận định",
                    "Bổ sung thông tin"],
        "answer": "Thiết lập hoặc duy trì quan hệ giao tiếp",
        "explanation": "Ví dụ: Này, ơi, dạ, vâng..."
    },
    {
        "question": "Tác phẩm 'Truyện Kiều' được viết bằng chữ gì?",
        "options": ["Chữ Nôm", "Chữ Hán", "Chữ Quốc ngữ", "Chữ Pháp"],
        "answer": "Chữ Nôm",
        "explanation": "Nguyễn Du dùng chữ Nôm để sáng tác kiệt tác này theo thể lục bát."
    },
    {
        "question": "Tình huống truyện trong 'Làng' nảy sinh khi ông Hai nghe tin gì?",
        "options": ["Làng Chợ Dầu theo giặc", "Làng Chợ Dầu bị cháy", "Ông không được về làng",
                    "Gia đình ông phải đi tản cư"],
        "answer": "Làng Chợ Dầu theo giặc",
        "explanation": "Tin này khiến ông Hai rơi vào trạng thái đau khổ và bế tắc tột độ."
    },
    {
        "question": "Trong 'Viếng lăng Bác', hình ảnh 'Hàng tre' tượng trưng cho điều gì?",
        "options": ["Phẩm chất kiên cường của con người Việt Nam", "Vẻ đẹp của thiên nhiên miền Bắc",
                    "Sự che chở của Bác Hồ", "Nỗi buồn của nhân dân"],
        "answer": "Phẩm chất kiên cường của con người Việt Nam",
        "explanation": "Hàng tre xanh xanh Việt Nam, bão táp mưa sa đứng thẳng hàng."
    },
    {
        "question": "Chủ đề của văn bản 'Phong cách Hồ Chí Minh' là gì?",
        "options": ["Vẻ đẹp văn hóa trong lối sống của Bác", "Sự nghiệp cứu nước của Bác", "Cuộc đời gian khổ của Bác",
                    "Tình cảm của Bác dành cho thiếu nhi"],
        "answer": "Vẻ đẹp văn hóa trong lối sống của Bác",
        "explanation": "Khẳng định phong cách của Người là sự kết hợp giữa truyền thống và hiện đại."
    },
    {
        "question": "Câu 'Cánh hoa rơi rụng.' thuộc kiểu câu gì xét theo cấu tạo?",
        "options": ["Câu đơn", "Câu ghép", "Câu đặc biệt", "Câu rút gọn"],
        "answer": "Câu đơn",
        "explanation": "Câu có một cụm chủ - vị (C: Cánh hoa, V: rơi rụng)."
    },
    {
        "question": "Trong đoạn trích 'Cảnh ngày xuân', tác giả dùng hình ảnh 'Trắng điểm một vài bông hoa lê' nhằm nhấn mạnh điều gì?",
        "options": ["Sự thanh khiết, tinh khôi", "Sự héo úa", "Sự đông đúc của các loài hoa", "Sự u ám của thời tiết"],
        "answer": "Sự thanh khiết, tinh khôi",
        "explanation": "Màu trắng của hoa lê gợi vẻ đẹp nhẹ nhàng, trong trẻo của mùa xuân."
    },
    {
        "question": "Tác giả của bài thơ 'Ánh trăng' là ai?",
        "options": ["Nguyễn Duy", "Chính Hữu", "Phạm Tiến Duật", "Huy Cận"],
        "answer": "Nguyễn Duy",
        "explanation": "Bài thơ gợi nhắc con người về đạo lý 'Uống nước nhớ nguồn'."
    },
    {
        "question": "Trạng ngữ trong câu 'Sáng nay, em đi học sớm.' chỉ gì?",
        "options": ["Thời gian", "Nơi chốn", "Nguyên nhân", "Cách thức"],
        "answer": "Thời gian",
        "explanation": "'Sáng nay' là thành phần phụ chỉ thời gian diễn ra sự việc."
    },
    {
        "question": "Trong truyện 'Bến quê', nhân vật Nhĩ đã nhận ra điều gì vào những ngày cuối đời?",
        "options": ["Vẻ đẹp bình dị của quê hương mà bấy lâu anh bỏ lỡ", "Anh vẫn muốn đi du lịch nước ngoài",
                    "Vợ anh không yêu thương anh", "Công việc là quan trọng nhất"],
        "answer": "Vẻ đẹp bình dị của quê hương mà bấy lâu anh bỏ lỡ",
        "explanation": "Một sự thức tỉnh muộn màng về những giá trị đích thực gần gũi."
    },
    {
        "question": "Lời thoại 'Con nín đi, mợ sắp về với con rồi' của Vũ Nương thuộc kiểu lời dẫn nào?",
        "options": ["Trực tiếp", "Gián tiếp", "Không xác định", "Lời dẫn phụ"],
        "answer": "Trực tiếp",
        "explanation": "Lời nói được nhắc lại nguyên văn và để trong dấu ngoặc kép."
    },
    {
        "question": "Bài thơ 'Con cò' của Chế Lan Viên sử dụng hình tượng con cò để nói về điều gì?",
        "options": ["Lòng mẹ và sự che chở suốt đời cho con", "Vẻ đẹp của đồng quê Việt Nam",
                    "Sự chăm chỉ của người nông dân", "Sự vất vả của loài chim"],
        "answer": "Lòng mẹ và sự che chở suốt đời cho con",
        "explanation": "Con cò tượng trưng cho tấm lòng người mẹ luôn theo sát con."
    },
    {
        "question": "Thành phần phụ chú thường được đặt giữa dấu gì?",
        "options": ["Dấu gạch ngang hoặc dấu ngoặc đơn", "Dấu chấm phẩy", "Dấu chấm hỏi", "Dấu ngoặc kép"],
        "answer": "Dấu gạch ngang hoặc dấu ngoặc đơn",
        "explanation": "Dùng để bổ sung chi tiết cho nội dung chính của câu."
    },
    {
        "question": "Từ 'đồng chí' có nghĩa gốc là gì?",
        "options": ["Cùng chí hướng", "Cùng quê hương", "Cùng gia đình", "Cùng đơn vị"],
        "answer": "Cùng chí hướng",
        "explanation": "Đồng là cùng, chí là chí hướng."
    },
    {
        "question": "Câu thơ 'Ngửa mặt lên nhìn mặt' trong bài 'Ánh trăng' sử dụng phép tu từ nào?",
        "options": ["Hoán dụ và ẩn dụ", "So sánh", "Nói quá", "Liệt kê"],
        "answer": "Hoán dụ và ẩn dụ",
        "explanation": "Từ 'mặt' thứ hai chỉ vầng trăng, vừa là nghĩa gốc vừa mang ý nghĩa tâm tình."
    },
    {
        "question": "Văn bản 'Chuẩn bị hành trang vào thế kỷ mới' của Vũ Khoan thuộc thể loại nào?",
        "options": ["Nghị luận xã hội", "Truyện ngắn", "Tùy bút", "Tiểu thuyết"],
        "answer": "Nghị luận xã hội",
        "explanation": "Bàn về những điểm mạnh, điểm yếu của người Việt Nam trước thời đại mới."
    },
    {
        "question": "Trong 'Sang thu', hình ảnh 'Đám mây mùa hạ / Hè nửa mình sang thu' là phép tu từ gì?",
        "options": ["Nhân hóa", "Ẩn dụ", "So sánh", "Điệp từ"],
        "answer": "Nhân hóa",
        "explanation": "Đám mây được miêu tả như có tâm hồn, sự lưu luyến khi chuyển mùa."
    },
    {
        "question": "Cách xưng hô 'Anh - Tôi' trong bài 'Đồng chí' thể hiện điều gì?",
        "options": ["Sự gắn bó, tương đồng giữa những người lính", "Sự xa cách về cấp bậc", "Sự khác biệt về quê quán",
                    "Sự đối đầu"],
        "answer": "Sự gắn bó, tương đồng giữa những người lính",
        "explanation": "Họ từ những người xa lạ trở thành tri kỷ, đồng đội."
    },
    {
        "question": "Nghĩa của câu 'Cơm sôi rồi, chắt nước giùm cái!' trong 'Chiếc lược ngà' mang hàm ý gì?",
        "options": ["Nhờ ông Sáu chắt nước cơm", "Khoe cơm đã chín", "Mắng ông Sáu", "Đuổi ông Sáu đi"],
        "answer": "Nhờ ông Sáu chắt nước cơm",
        "explanation": "Bé Thu nói trống không vì chưa chịu nhận ba, nhưng thực chất là một lời nhờ vả."
    },
    {
        "question": "Trong bài thơ 'Quê hương' của Tế Hanh, hình ảnh con thuyền được so sánh với gì?",
        "options": ["Con tuấn mã", "Con chim hải âu", "Cánh buồm", "Mặt trời"],
        "answer": "Con tuấn mã",
        "explanation": "'Chiếc thuyền nhẹ hăng như con tuấn mã'."
    },
    {
        "question": "Tác phẩm nào sau đây không thuộc văn học trung đại Việt Nam?",
        "options": ["Lặng lẽ Sa Pa", "Truyện Kiều", "Chuyện người con gái Nam Xương", "Hoàng Lê nhất thống chí"],
        "answer": "Lặng lẽ Sa Pa",
        "explanation": "Lặng lẽ Sa Pa là văn học hiện đại (sáng tác năm 1970)."
    },
    {
        "question": "Câu thơ 'Không có kính không phải vì xe không có kính' sử dụng điệp từ nào?",
        "options": ["Không", "Có", "Kính", "Xe"],
        "answer": "Không",
        "explanation": "Điệp từ 'không' nhấn mạnh sự thiếu thốn về cơ sở vật chất nhưng đầy ắp tinh thần."
    },
    {
        "question": "Ai là tác giả bài thơ 'Viếng lăng Bác'?",
        "options": ["Viễn Phương", "Thanh Hải", "Hữu Thỉnh", "Y Phương"],
        "answer": "Viễn Phương",
        "explanation": "Nhà thơ miền Nam ra thăm lăng Bác với niềm xúc động sâu sắc."
    },
    {
        "question": "Trong 'Mùa xuân nho nhỏ', nhà thơ muốn làm 'con chim hót', 'một nhành hoa' để làm gì?",
        "options": ["Dâng hiến cho đời", "Để được nổi tiếng", "Để vui chơi", "Để làm đẹp cho mình"],
        "answer": "Dâng hiến cho đời",
        "explanation": "Khát vọng cống hiến thầm lặng, chân thành cho đất nước."
    },
    {
        "question": "Thành phần biệt lập 'Tình thái' trong câu 'Có lẽ ngày mai trời sẽ mưa.' là từ nào?",
        "options": ["Có lẽ", "Ngày mai", "Trời", "Mưa"],
        "answer": "Có lẽ",
        "explanation": "Thể hiện độ tin cậy thấp hoặc phỏng đoán của người nói."
    },
    {
        "question": "Truyện 'Những ngôi sao xa xôi' kể về công việc của ai?",
        "options": ["Ba cô gái thanh niên xung phong", "Những chiến sĩ lái xe", "Những người nông dân",
                    "Các bác sĩ quân y"],
        "answer": "Ba cô gái thanh niên xung phong",
        "explanation": "Họ làm nhiệm vụ phá bom trên cao điểm Trường Sơn."
    },
    {
        "question": "Trong 'Nói với con', người cha dặn con nhớ về 'người đồng mình' với phẩm chất gì?",
        "options": ["Mộc mạc nhưng giàu chí khí", "Giàu có và sang trọng", "Yếu đuối và tự ti",
                    "Sợ hãi trước gian khổ"],
        "answer": "Mộc mạc nhưng giàu chí khí",
        "explanation": "Nhắc nhở con về cội nguồn và niềm tự hào dân tộc."
    },
    {
        "question": "Từ 'mặt' trong 'Ánh trăng' (Ngửa mặt lên nhìn mặt) là hiện tượng gì?",
        "options": ["Từ nhiều nghĩa", "Từ đồng âm", "Từ trái nghĩa", "Từ gần nghĩa"],
        "answer": "Từ nhiều nghĩa",
        "explanation": "Cùng một từ nhưng chỉ hai đối tượng khác nhau dựa trên sự tương đồng."
    },
    {
        "question": "Tên nhân vật chính trong truyện 'Những ngôi sao xa xôi' là gì?",
        "options": ["Phương Định", "Thúy Kiều", "Vũ Nương", "Bé Thu"],
        "answer": "Phương Định",
        "explanation": "Cô là người kể chuyện đồng thời là nhân vật chính."
    },
    {
        "question": "Câu thơ 'Cá huy hoàng giang tay đêm lại' sử dụng biện pháp gì?",
        "options": ["Nhân hóa", "So sánh", "Nói quá", "Liệt kê"],
        "answer": "Nhân hóa",
        "explanation": "Biển và cá được miêu tả như những thực thể có hành động của con người."
    },
    {
        "question": "Tác phẩm nào ca ngợi vẻ đẹp của người anh hùng áo vải Quang Trung?",
        "options": ["Hoàng Lê nhất thống chí", "Truyện Kiều", "Lục Vân Tiên", "Bình Ngô đại cáo"],
        "answer": "Hoàng Lê nhất thống chí",
        "explanation": "Hồi thứ 14 miêu tả khí thế thần tốc của nghĩa quân Tây Sơn."
    },
    {
        "question": "Kiểu câu 'Anh đi đâu đấy?' dùng để thực hiện hành động nói nào?",
        "options": ["Hỏi", "Trình bày", "Điều khiển", "Bộc lộ cảm xúc"],
        "answer": "Hỏi",
        "explanation": "Dùng để tìm kiếm thông tin chưa biết."
    },
    {
        "question": "Trong 'Mùa xuân nho nhỏ', hình ảnh 'Lộc giắt đầy trên lưng' chỉ điều gì?",
        "options": ["Người ra đồng", "Người cầm súng", "Cành lá ngụy trang", "Hoa mùa xuân"],
        "answer": "Người cầm súng",
        "explanation": "Chỉ những chiến sĩ bảo vệ tổ quốc với cành lá ngụy trang."
    },
    {
        "question": "Phần kết bài của một bài văn nghị luận thường có nhiệm vụ gì?",
        "options": ["Khẳng định lại vấn đề và rút ra bài học", "Nêu dẫn chứng mới", "Giải thích khái niệm",
                    "Kể chuyện"],
        "answer": "Khẳng định lại vấn đề và rút ra bài học",
        "explanation": "Tổng kết lại quan điểm và để lại ấn tượng cho người đọc."
    },
    {
        "question": "Bài thơ 'Viếng lăng Bác' được sáng tác trong hoàn cảnh nào?",
        "options": ["Khi lăng Bác vừa khánh thành (1976)", "Khi Bác Hồ vừa mất (1969)",
                    "Trong thời kỳ kháng chiến chống Pháp", "Khi đất nước mới thống nhất (1975)"],
        "answer": "Khi lăng Bác vừa khánh thành (1976)",
        "explanation": "Viễn Phương từ miền Nam ra thăm lăng Bác ngay sau khi công trình hoàn thành."
    }

]