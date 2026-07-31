# Phân tích hình ảnh - What Did Ancient Humans Do When It Rained All Week?

Kênh: Ink Explainer (`https://www.youtube.com/@Inkexplainer96`). Video đạt khoảng 1 triệu
view theo thông tin chủ kênh cung cấp; số view không đọc được bằng script vì YouTube chặn
bot ở watch page. Link gốc: `https://www.youtube.com/watch?v=SD7XyG2wd1k`

## Kết quả extract

- Video nguồn: 11:36.44, 1920x1072, 30 FPS, khoảng 20.893 frame mã hóa.
- Bộ nghiên cứu: 355 trạng thái hình ảnh khác nhau, giữ nguyên độ phân giải 1920x1072.
- Contact sheet: 15 trang, mỗi frame có số thứ tự và timestamp.
- Index: `frame-index.csv`.
- Phương pháp: phát hiện thay đổi nội dung ở ngưỡng thấp (scene threshold 0.02) để bắt
  cả cut lớn và các bước build nhỏ. Từ 357 ứng viên, loại 2 frame không thêm thông tin:
  một frame giữa chu kỳ bước đi trong cơn mưa ở 00:13.20 và một frame chỉ khác ở độ mở
  của mí mắt ở 01:06.87. Không có frame chuyển tiếp bị blur, vì video này cut thẳng,
  gần như không dùng crossfade.

"355 frame" không phải 355 frame ngẫu nhiên. Đây là 355 visual beat: mỗi beat là một
trạng thái mà người xem nhận được thông tin mới, dù là một nhãn mở thêm, một icon xuất
hiện, một góc nhìn đổi, hay một bảng màu đổi.

## Kết luận quan trọng nhất

Video này không cuốn vì từng frame được vẽ đẹp. Nó cuốn vì **hệ thống ba chế độ hình ảnh
được luân phiên liên tục**.

Ba chế độ:

| Chế độ | Tỷ lệ | Chức năng |
| --- | ---: | --- |
| Cảnh vẽ đầy khung (nền màu, không khí, ánh sáng) | 51,5% | kể chuyện, tạo cảm xúc, định vị không gian |
| Thẻ trắng (diagram, số, bản đồ, object card, chữ lớn) | 40,3% | giải thích, dẫn chứng, đặt tên |
| Narrator stick figure trên nền trắng | 7,0% | dấu ngắt câu, chuyển ý, giọng tác giả |

Trong 355 frame có **138 lần đổi chế độ**, tức trung bình cứ 2,6 beat lại đổi chế độ một
lần, khoảng 5 giây một lần. Chuỗi dài nhất của cùng một chế độ là 15 frame, và đó là đoạn
liên tiếp các thẻ trắng khi video liệt kê bản đồ và con số.

Đây là cơ chế chống "thích nghi thị giác". Mắt người xem không bao giờ kịp quen một định
dạng. Đổi chế độ rẻ hơn đổi nội dung: không cần ý tưởng mới, chỉ cần đổi cách trình bày.

Công thức cốt lõi:

1. Cảnh màu chỉ làm việc kể chuyện. Chữ và nhãn gần như không bao giờ để lên cảnh màu.
2. Toàn bộ chữ, số, bản đồ, sơ đồ bị đẩy sang thẻ trắng. Vì vậy cảnh màu luôn sạch.
3. Narrator xuất hiện để ngắt nhịp trước mỗi luận điểm mới.
4. Một cảnh màu được tái sử dụng 3 đến 5 lần, mỗi lần thêm một delta.
5. Mỗi khẳng định có một "biên nhận" thị giác: bản đồ có pin, số lớn, hoặc artefact card.

## Nhịp hình ảnh

| Chỉ số | Kết quả |
| --- | ---: |
| Visual beat trong 11:36 | 355 |
| Visual beat mỗi phút | 30,6 |
| Thời gian trung bình mỗi beat | 1,96 giây |
| Trung vị khoảng cách hai beat | 1,80 giây |
| Lần thay đổi trong 1 giây hoặc nhanh hơn | 58 |
| Lần thay đổi trong 2 giây hoặc nhanh hơn | 214 trên 354 |
| Khoảng giữ hình từ 4 giây trở lên | 8 |
| Beat trong 15 giây đầu | 11 |
| Nhịp riêng phần hook (0 đến 45 giây) | 1,50 giây mỗi beat, 39,9 beat mỗi phút |

Nhịp không đều, và đó là có chủ ý:

| Đoạn | Frame | Beat mỗi phút | Giây mỗi beat |
| --- | --- | ---: | ---: |
| Hook | 001-030 | 39,9 | 1,50 |
| Luận đề và gương modern | 031-046 | 32,9 | 1,82 |
| Ba cách mưa giết người | 047-082 | 30,9 | 1,94 |
| Giữ lửa | 083-124 | 29,4 | 2,04 |
| Payoff của lửa | 125-139 | 43,5 | 1,38 |
| Chế tác đồ | 140-172 | 34,8 | 1,72 |
| Dây và rope | 173-197 | 31,1 | 1,93 |
| Bedding | 198-216 | 30,0 | 2,00 |
| Nghệ thuật hang động | 217-253 | 26,7 | 2,24 |
| Văn hóa và kể chuyện | 254-299 | 25,8 | 2,33 |
| Mưa có lợi | 300-329 | 27,6 | 2,17 |
| Kết | 330-355 | 30,0 | 2,00 |

Đọc bảng này theo một câu: **nhanh khi tạo cảm xúc, chậm khi giải thích, nhanh lại khi
trả payoff.** Đoạn nhanh nhất toàn video không phải hook mà là đoạn payoff của lửa
(1,38 giây mỗi beat), khi narration lật từ "lửa chỉ để sưởi" sang "lửa là tất cả". Đoạn
chậm nhất là chương văn hóa, vì đây là chương đòi người xem theo dõi một chuỗi suy luận.

Khoảng giữ hình dài nhất trong cả video là 5,7 giây ở [frame 254](extracted-frames/frame-254_07m52.53s.jpg),
cảnh 14 người ngồi quanh đống lửa. Đó là một cảnh đông người, nhiều chi tiết, và nó được
giữ lâu vì mắt người xem cần thời gian để quét.

## Mười hai cơ chế làm video cuốn

### 1. Hook là một cảnh phim, không phải một lời giới thiệu

Từ [frame 001](extracted-frames/frame-001_00m00.00s.jpg) đến
[frame 030](extracted-frames/frame-030_00m43.63s.jpg), video dùng 30 beat trong 44 giây,
nhanh gần gấp đôi phần thân bài.

Chuỗi hook không nói một câu luận đề nào. Nó diễn một ngày:

- Thợ săn ngồi đợi trên savanna khô ([frame 001](extracted-frames/frame-001_00m00.00s.jpg)).
- Nhìn thấy đàn bison ([frame 002](extracted-frames/frame-002_00m02.20s.jpg)).
- Cận gần dấu chân trên đất ([frame 004](extracted-frames/frame-004_00m05.37s.jpg)).
- Thought bubble kế hoạch: hang, con mồi, đường đi ([frame 005](extracted-frames/frame-005_00m06.63s.jpg)).
- Bước ra với trời xanh ([frame 006](extracted-frames/frame-006_00m08.27s.jpg)).
- Trời đổi màu xám, mưa bắt đầu, càng lần càng nặng, camera càng lại gần
  ([frame 009](extracted-frames/frame-009_00m12.17s.jpg) đến [frame 011](extracted-frames/frame-011_00m14.83s.jpg)).
- Cắt vào hang: 8 người quanh đống lửa ban ngày, rồi đêm, rồi hoàng hôn với đống lửa gần
  tàn ([frame 012](extracted-frames/frame-012_00m17.17s.jpg),
  [frame 013](extracted-frames/frame-013_00m18.03s.jpg),
  [frame 014](extracted-frames/frame-014_00m19.13s.jpg)).
- Macro mưa đập xuống bùn, không có nhân vật ([frame 017](extracted-frames/frame-017_00m23.77s.jpg)).
- Cận rất gần hai bàn chân trần trên đá ướt ([frame 019](extracted-frames/frame-019_00m27.67s.jpg)).
- Một bóng người nhỏ đi trong đồng nước, rồi chữ "Death" màu đỏ đổ lên chính khung đó
  ([frame 022](extracted-frames/frame-022_00m33.27s.jpg)).

Câu hỏi trí tuệ chỉ đến ở [frame 031](extracted-frames/frame-031_00m44.47s.jpg), sau khi
người xem đã xem một kế hoạch thất bại và một cái chết. Escalation: kế hoạch -> thời tiết
-> cơ thể -> cái chết -> luận đề.

### 2. Chữ bao giờ cũng nằm trên thẻ trắng, không nằm trên cảnh màu

Đây là quy tắc quan trọng nhất nếu mục tiêu là "scene bắt mắt".

Cảnh màu của video này hầu như không có chữ. Toàn bộ nhãn, mũi tên, con số, tên địa điểm
bị đẩy sang nền trắng: [frame 047](extracted-frames/frame-047_01m14.17s.jpg) (ba cách mưa
giết người), [frame 050](extracted-frames/frame-050_01m19.67s.jpg) (DRY 1x vs WET 25x),
[frame 054](extracted-frames/frame-054_01m25.43s.jpg) (nhiệt kế và vùng hạ nhiệt),
[frame 063](extracted-frames/frame-063_01m44.80s.jpg) (địa tầng khảo cổ),
[frame 122](extracted-frames/frame-122_03m41.43s.jpg) (banner birch bark),
[frame 142](extracted-frames/frame-142_04m15.13s.jpg) (bốn bước làm lưỡi đá).

Kết quả: cảnh màu giữ được độ sạch và không khí, còn thông tin vẫn được truyền đầy đủ.
Nếu trộn hai thứ vào một frame, cảnh sẽ rối và chữ sẽ khó đọc trên điện thoại.

### 3. Narrator cut-in là dấu ngắt câu rẻ nhất trong toàn bộ hệ thống

25 frame narrator, nền trắng, một nhân vật que, không có đạo cụ, chỉ thay tay và biểu cảm
([frame 016](extracted-frames/frame-016_00m22.60s.jpg),
[frame 020](extracted-frames/frame-020_00m30.47s.jpg),
[frame 080](extracted-frames/frame-080_02m19.17s.jpg),
[frame 299](extracted-frames/frame-299_09m37.17s.jpg)).

Vị trí của chúng không ngẫu nhiên. Gần như tất cả nằm ngay trước một khẳng định mới hoặc
một câu lật. Chúng làm ba việc cùng lúc: reset mắt người xem sau một cảnh nhiều chi tiết,
đánh dấu ranh giới ý, và cho narration một giọng "tôi đang nói với bạn".

Biến thể đáng chú ý: từ [frame 140](extracted-frames/frame-140_04m09.10s.jpg) trở đi
narrator đội mũ fedora khi video chuyển sang nói về khảo cổ học, và giữ mũ đó trong cả
chương ([frame 168](extracted-frames/frame-168_04m59.00s.jpg) khu vực,
[frame 176](extracted-frames/frame-176_05m10.53s.jpg)). Một đạo cụ duy nhất để đổi vai.

### 4. Một base plate, nhiều trạng thái

Đây là cơ chế giúp video có 355 beat mà không cần 355 bộ tranh độc lập. Cùng một cảnh hang
được dùng lại và mỗi lần thêm một delta:

- Hang 8 người: ban ngày, đêm có trăng, hoàng hôn lửa tàn
  ([frame 012](extracted-frames/frame-012_00m17.17s.jpg) đến [frame 014](extracted-frames/frame-014_00m19.13s.jpg)).
- Hang một người: sưởi tay, hai mắt xanh của thú ngoài trời, nướng thịt, lửa tàn
  ([frame 025](extracted-frames/frame-025_00m36.53s.jpg) đến [frame 028](extracted-frames/frame-028_00m40.90s.jpg)).
- Phòng khách modern: đọc sách, đặt sách xuống, mắt sụp, ngủ
  ([frame 040](extracted-frames/frame-040_01m02.83s.jpg) đến [frame 041](extracted-frames/frame-041_01m04.63s.jpg)).
- Hang làm rope: ngồi không, khắc dụng cụ, một cuộn dây, ba cuộn dây
  ([frame 185](extracted-frames/frame-185_05m29.53s.jpg) đến [frame 188](extracted-frames/frame-188_05m36.00s.jpg)).
- Cùng một cảnh hang, thêm một dải icon tuần trăng ở mép trên để nói "nhiều đêm đã qua"
  ([frame 125](extracted-frames/frame-125_03m49.10s.jpg),
  [frame 171](extracted-frames/frame-171_05m03.17s.jpg)).

Delta luôn là một trong năm thứ: thời gian, số lượng, ánh sáng, biểu cảm, hoặc một icon
overlay. Không bao giờ là "vẽ lại cảnh đó".

### 5. Rule of three rồi merge

Video xây một pattern bằng ba lần lặp cùng bố cục, rồi trả payoff bằng một frame gộp:

- Người núp dưới đá ([frame 076](extracted-frames/frame-076_02m13.50s.jpg)),
  báo núp dưới đá ([frame 077](extracted-frames/frame-077_02m14.17s.jpg)),
  hươu núp dưới đá ([frame 078](extracted-frames/frame-078_02m14.80s.jpg)),
  rồi cả ba núp chung một hốc đá ([frame 079](extracted-frames/frame-079_02m15.27s.jpg)).
  Ba beat này chỉ tốn 1,8 giây tổng cộng, và payoff là một cú cười.
- Bộ kit của Otzi hiện nguyên bảng ([frame 105](extracted-frames/frame-105_03m11.47s.jpg)),
  rồi tách ra từng item một ([frame 106](extracted-frames/frame-106_03m13.83s.jpg) đến
  [frame 109](extracted-frames/frame-109_03m17.13s.jpg)). Zoom vào từng phần tử của bảng
  đã có sẵn.
- SHELTER, SNARE, STONE AXE, STICKS quy về một trung tâm ROPE
  ([frame 193](extracted-frames/frame-193_05m44.67s.jpg)).
- TOOLS, CLOTHING, STORIES, ART, ROPE lần lượt xuất hiện rồi cùng trỏ vào DOWNTIME
  ([frame 344](extracted-frames/frame-344_11m13.73s.jpg) đến
  [frame 347](extracted-frames/frame-347_11m17.20s.jpg)).

### 6. Diagram vẽ thẳng vào trong cảnh màu khi lập luận cần cả hai

Khi một ý cần vừa bối cảnh vừa cơ chế, video không chọn một trong hai chế độ. Nó vẽ sơ đồ
ngay trên cảnh:

- Ba beat top-down sàn hang: đống lửa và vết đá vụn, nhãn "CONCENTRATED HERE", rồi thêm
  nhân vật và các vật liệu xung quanh, rồi ba mũi tên từ đống vụn ra tinder, xương, đá
  ([frame 145](extracted-frames/frame-145_04m21.67s.jpg) đến
  [frame 147](extracted-frames/frame-147_04m28.30s.jpg)). Đây là một argument về khảo cổ
  học được diễn bằng một bản đồ sàn nhà.
- Chuỗi bốn bước ochre vẽ trên sàn hang có ánh lửa
  ([frame 159](extracted-frames/frame-159_04m47.90s.jpg)).
- Nhãn "PRODUCTION" và dấu check đặt trong cảnh hang
  ([frame 155](extracted-frames/frame-155_04m41.83s.jpg)).
- Mũi tên từ đống lửa sang đống bedding cũ bị đốt, vẽ trong cảnh
  ([frame 210](extracted-frames/frame-210_06m17.00s.jpg)).

### 7. Mỗi khẳng định có một biên nhận thị giác

Video không bao giờ nói "các nhà khảo cổ tìm thấy" mà không cho xem một thứ. Bộ biên nhận
gồm bốn loại thẻ:

- **Bản đồ có pin**: QESEM CAVE, WONDERWERK CAVE, BLOMBOS CAVE, SIBUDU CAVE, CHAUVET,
  LASCAUX, ALTAMIRA, SULAWESI, ABRI DU MARAS, HOHLE FELS, KALAHARI. Ví dụ
  [frame 219](extracted-frames/frame-219_06m33.87s.jpg) khu vực,
  [frame 249](extracted-frames/frame-249_07m42.50s.jpg).
- **Thẻ con số lớn**: 50.000, 40.000, 400.000, 100.000, 61.000, 52.000, 35.000, 77.000,
  45.500, 36.000, 5.300, 5.000. Mỗi con số chiếm gần nguyên frame.
- **Object card có callout**: kim xương với nhãn "TINY DRILLED EYE"
  ([frame 167](extracted-frames/frame-167_04m57.70s.jpg)), dụng cụ ngà với "FOUR HOLES"
  và "SPIRAL GROOVES" ([frame 183](extracted-frames/frame-183_05m25.07s.jpg)), dây xoắn
  dưới kính lúp ([frame 177](extracted-frames/frame-177_05m11.73s.jpg)).
- **Thẻ trích dẫn nghiên cứu**: "2014 / Anthropologist Polly Wiessner published a study"
  ([frame 258](extracted-frames/frame-258_08m00.60s.jpg)).

Cảm giác "video này được đầu tư nghiên cứu" đến từ đây, không đến từ narration.

### 8. Chữ là hình ảnh, không phải phụ đề

Nhiều frame chỉ có chữ, và chữ được vẽ như một object: font marker tay, cỡ lớn chiếm 1/3
đến 1/2 khung, màu đỏ cho nguy hiểm, đen cho tuyên bố.

- "Death" đổ lên cảnh mưa ([frame 022](extracted-frames/frame-022_00m33.27s.jpg)).
- "IT WAS A CRISIS." đỏ đậm giữa những giọt nước
  ([frame 032](extracted-frames/frame-032_00m47.60s.jpg)).
- "EVERYTHING." với icon lửa phát sáng ([frame 129](extracted-frames/frame-129_03m53.80s.jpg)).
- "YOU MAKE THINGS." ([frame 139](extracted-frames/frame-139_04m08.40s.jpg)).
- "THE ART." ([frame 218](extracted-frames/frame-218_06m33.27s.jpg)).
- "NOT DEAD TIME." bị gạch đỏ, thay bằng "TRANSMISSION TIME."
  ([frame 296](extracted-frames/frame-296_09m26.60s.jpg)).
- "EVERYTHING THAT MATTERED." ([frame 331](extracted-frames/frame-331_10m46.17s.jpg)).
- "YOU GET CREATIVE" ([frame 354](extracted-frames/frame-354_11m32.93s.jpg)).

Các thẻ này làm hai việc: đánh dấu chương, và cho mắt một beat nghỉ giữa hai cảnh nhiều
chi tiết.

### 9. Ánh sáng là núm điều chỉnh cảm xúc

Video chỉ dùng bốn trạng thái ánh sáng, và dùng rất kỷ luật:

- **Vùng sáng cam quanh đống lửa** = an toàn, thuộc về nhóm. Mạnh nhất ở
  [frame 132](extracted-frames/frame-132_03m56.73s.jpg), cảnh nhìn từ ngoài vào miệng hang
  phát sáng cam giữa đêm, hai mắt xanh của thú trong tối.
- **Xám xanh lạnh** = nguy hiểm, ướt, mất nhiệt ([frame 135](extracted-frames/frame-135_04m00.67s.jpg)
  lửa tắt và dấu X đỏ, [frame 136](extracted-frames/frame-136_04m02.57s.jpg) cả nhóm run).
- **Gần như đen với một vùng đèn nhỏ** = bí ẩn, đi sâu vào hang
  ([frame 235](extracted-frames/frame-235_07m16.37s.jpg),
  [frame 236](extracted-frames/frame-236_07m17.73s.jpg)).
- **Xanh lá và bình minh** = giải tỏa, dùng ở frame cuối
  ([frame 355](extracted-frames/frame-355_11m33.87s.jpg)).

Cặp đối trực tiếp nhất: [frame 134](extracted-frames/frame-134_03m57.97s.jpg) sáu người
quanh lửa sáng, đối lại [frame 136](extracted-frames/frame-136_04m02.57s.jpg) năm người run
trong hang xanh lạnh. Cùng một bố cục, đổi ánh sáng, đảo ngược cảm xúc.

### 10. Âm thanh được vẽ thành chữ

Hai frame đối xứng nhau, cách nhau 7 giây:

- Phòng khách modern, mưa gõ cửa sổ, chữ "TAP TAP" rải quanh khung
  ([frame 040](extracted-frames/frame-040_01m02.83s.jpg)).
- Hang thời tiền sử, cùng bố cục "người ngủ trong khi mưa rơi ngoài kia", chữ
  "SHHHHHHH", "PATTER-PATTER", "RUMBLE", "DRIP DRIP", "PLINK"
  ([frame 046](extracted-frames/frame-046_01m11.83s.jpg)).

Đây là cách video nói "bạn và họ đang nghe cùng một thứ" mà không cần narration nói câu đó.

### 11. Gương modern đối ancient chạy xuyên cả video

Cấu trúc đối gương được mở ở phút đầu và đóng lại ở phút cuối:

- Mở: người hiện đại đóng cửa sổ, uống trà, cuộn chăn, ngủ trên sofa
  ([frame 034](extracted-frames/frame-034_00m53.03s.jpg) đến
  [frame 041](extracted-frames/frame-041_01m04.63s.jpg)).
- Thẻ chuyển cảnh "50.000 YEARS AGO" với thanh THEN-NOW
  ([frame 044](extracted-frames/frame-044_01m09.80s.jpg)).
- Lặp lại chính xác các beat đó trong hang ([frame 045](extracted-frames/frame-045_01m10.93s.jpg),
  [frame 046](extracted-frames/frame-046_01m11.83s.jpg)).
- Đóng lại ở [frame 350](extracted-frames/frame-350_11m23.03s.jpg): thẻ split "YOU"
  (nằm ôm điện thoại, zzz) đối "THEM" (làm dao, se dây, cạo da, giữ lửa).

Người xem được đưa vào vị trí so sánh với chính mình, không phải vị trí học lịch sử.

### 12. Chương nào cũng mở một curiosity loop mới

Video không sống bằng một câu hỏi duy nhất. Nó chia thành một chuỗi câu hỏi nhỏ, mỗi câu
có một thẻ tiêu đề riêng:

- Mưa giết người bằng cách nào? -> COLD, FLOODING, PREDATORS
  ([frame 047](extracted-frames/frame-047_01m14.17s.jpg),
  [frame 048](extracted-frames/frame-048_01m16.80s.jpg),
  [frame 058](extracted-frames/frame-058_01m36.90s.jpg)).
- Giữ lửa bằng gì khi tất cả đều ướt? -> tinder fungus, "BIOLOGICAL LIGHTER"
  ([frame 101](extracted-frames/frame-101_03m03.27s.jpg)).
- Họ làm gì trong những ngày đó? -> tools, needles, rope, bedding.
- Rồi một câu lật: "BUT THEN... something nobody expects" -> "THE ART."
  ([frame 212](extracted-frames/frame-212_06m23.60s.jpg) khu vực,
  [frame 218](extracted-frames/frame-218_06m33.27s.jpg)).
- Rồi lật lần hai: "RAIN DIDN'T JUST CREATE ART / IT MIGHT HAVE CREATED CULTURE ITSELF"
  ([frame 251](extracted-frames/frame-251_07m48.67s.jpg),
  [frame 252](extracted-frames/frame-252_07m50.10s.jpg)).
- Rồi lật lần ba: "RAIN WASN'T ALWAYS BAD" -> tracking, rock pools, mushrooms, termites
  ([frame 300](extracted-frames/frame-300_09m39.23s.jpg)).

Mỗi lần payoff được trả, một biến mới được mở ngay lập tức.

## Phân tích từng chương

| Thời gian | Frame | Cách hình ảnh hoạt động | Tác động |
| --- | --- | --- | --- |
| 00:00-00:44 | 001-030 | Kế hoạch đi săn, trời đổi, push-in ba bước, hang ba thời điểm, macro bàn chân và mưa, chữ "Death" | Tạo cảm xúc và stake trước khi nói luận đề |
| 00:44-01:12 | 031-046 | Hai thẻ chữ luận đề, chuỗi phòng khách modern, thẻ 50.000 năm, gương lại cảnh hang, chữ âm thanh | Bắt người xem tự so sánh với mình |
| 01:14-02:22 | 047-082 | Thẻ agenda ba icon, diagram 25x, nhiệt kế, cross-section hang và sông, địa tầng khảo cổ, rule of three núp mưa | Biến một mối đe dọa trừu tượng thành ba cơ chế cụ thể |
| 02:23-03:47 | 083-124 | Bản đồ Qesem và Wonderwerk, split SKILL 1 vs SKILL 2, object card tinder fungus, kit Otzi tách từng item, diagram cây ướt khô, birch bark | Chương nặng thông tin nhất, gần như toàn thẻ trắng, nhịp chậm nhất trong nửa đầu |
| 03:49-04:08 | 125-139 | Dải tuần trăng, biến thể ánh sáng của cùng một hang, cảnh đông người ấm đối cảnh nhóm run lạnh, thẻ "EVERYTHING." | Payoff cảm xúc, nhịp nhanh nhất toàn video |
| 04:09-05:04 | 140-172 | Narrator đội mũ fedora, chuỗi bốn bước làm lưỡi đá, ba beat top-down sàn hang, Blombos và ochre, kim xương với callout | Biến khảo cổ học thành một chuỗi suy luận nhìn thấy được |
| 05:06-05:52 | 173-197 | Bản đồ Abri du Maras và Hohle Fels, artefact card bốn lỗ và rãnh xoắn, diagram chức năng, base plate rope với số lượng tăng, hub ROPE | Cho thấy một phát minh nhỏ mở ra cả một cây công nghệ |
| 05:54-06:30 | 198-216 | Sibudu, thẻ 77.000 năm, cutaway lớp bedding, icon cape laurel, recap ba icon | Đóng chương "practical" lại bằng một recap gọn |
| 06:31-07:52 | 217-253 | Thẻ "THE ART.", bốn bản đồ di chỉ, tranh hang vẽ nguyên khung, cave plan có đường đỏ, cảnh gần như đen với đèn mỡ, split thời tiết | Chuyển từ kỹ năng sang ý nghĩa, nhịp chậm nhất để người xem thở |
| 07:52-09:37 | 254-299 | Cảnh đông người giữ 5,7 giây, speech bubble đổi chủ đề ngày và đêm, bản đồ thần thoại mưa toàn cầu, chuỗi truyền tri thức, thẻ "TRANSMISSION TIME." | Chương luận điểm trung tâm, nhịp chậm nhất, nhiều thẻ chữ nhất |
| 09:39-10:42 | 300-329 | Mudflat trống rồi vết chân xuất hiện trên cùng một plate, rock pool, mushroom, termite, cặp chimps-today đối early-humans | Đảo ngược luận đề một lần cuối trước kết |
| 10:44-11:34 | 330-355 | Thẻ câu hỏi echo tiêu đề, thẻ trả lời, montage sáu cảnh làm việc, năm icon quy về DOWNTIME, split YOU vs THEM, vista bình minh | Trả giá trị cảm xúc và đóng vòng lặp |

## Vì sao phần kết hiệu quả

Kết của video không phải một summary. Nó là một chuỗi sáu bước:

1. Lặp lại chính xác câu hỏi trong tiêu đề dưới dạng thẻ chữ
   ([frame 330](extracted-frames/frame-330_10m43.80s.jpg)).
2. Trả lời bằng một câu ba từ, cỡ lớn nhất trong cả video
   ([frame 331](extracted-frames/frame-331_10m46.17s.jpg)).
3. Montage sáu cảnh làm việc trong hang, mỗi cảnh một nghề: giữ lửa, chế lưỡi đá, cạo da,
   se dây, mài ochre, kể chuyện ([frame 332](extracted-frames/frame-332_10m47.23s.jpg) đến
   [frame 337](extracted-frames/frame-337_10m59.27s.jpg)).
4. Bước ra trời quang, đất ướt, cỏ xanh, mặt trời
   ([frame 338](extracted-frames/frame-338_11m02.90s.jpg) đến
   [frame 340](extracted-frames/frame-340_11m07.70s.jpg)).
5. Năm icon quy về một chữ DOWNTIME
   ([frame 347](extracted-frames/frame-347_11m17.20s.jpg)).
6. Chiếu trở lại người xem: split "YOU" đối "THEM"
   ([frame 350](extracted-frames/frame-350_11m23.03s.jpg)), rồi
   "YOU DON'T GET BORED." / "YOU GET CREATIVE"
   ([frame 353](extracted-frames/frame-353_11m32.03s.jpg),
   [frame 354](extracted-frames/frame-354_11m32.93s.jpg)), rồi một vista bình minh
   ([frame 355](extracted-frames/frame-355_11m33.87s.jpg)).

Kiến thức không dừng ở dạng thông tin. Nó biến thành một câu nói về người xem. Đây là lý do
video có khả năng được chia sẻ cao hơn một explainer chỉ kể sự kiện.

## Những điểm không nên sao chép

### 1. Luận điểm trung tâm là suy diễn, và frame bản đồ nói mạnh hơn bằng chứng

Video có tử tế đặt hai thẻ cảnh báo: "NOW WE CAN'T PROVE IT"
([frame 245](extracted-frames/frame-245_07m35.63s.jpg)) và "BUT THE LOGIC HOLDS TOGETHER"
([frame 247](extracted-frames/frame-247_07m38.60s.jpg)). Nhưng ngay trước đó,
[frame 249](extracted-frames/frame-249_07m42.50s.jpg) in câu
"ALL CAVE ART = PLACES WHERE PEOPLE GOT STUCK INSIDE" trên một bản đồ có hatching mưa phủ
châu Âu. Một thẻ trắng như vậy đọc như sự thật đã được xác lập.

Phân bố nghệ thuật hang động còn phụ thuộc rất nhiều vào địa chất karst đá vôi và vào điều
kiện bảo tồn, không chỉ vào lượng mưa. Nếu TossExplains dùng kỹ thuật "bản đồ kết luận"
này, kết luận trên bản đồ phải là kết luận đã có nguồn, không phải giả thuyết.

### 2. Con số 25x cần được kiểm tra trước khi tái sử dụng

[frame 050](extracted-frames/frame-050_01m19.67s.jpg) trình bày "DRY 1x" đối "WET 25x" như
tốc độ mất nhiệt của cơ thể. Con số 25 lần thường được dẫn cho **độ dẫn nhiệt của nước so
với không khí**, không phải cho tốc độ mất nhiệt thực tế của một cơ thể người mặc đồ ướt,
vì còn phụ thuộc gió, độ ẩm, diện tích tiếp xúc và lớp cách nhiệt.

Thẻ dạng này rất dễ nhớ và rất dễ sai. Trước khi làm một frame như vậy, phải xác định rõ
con số đó đo lường đại lượng nào.

### 3. Một vài mốc thời gian còn đang tranh luận

[frame 088](extracted-frames/frame-088_02m36.37s.jpg) ghi Wonderwerk Cave khoảng 1 triệu
năm. Video có thêm dấu "?" bên cạnh, và đó là cách xử lý đúng. Nhưng khi tái sử dụng mô
hình "bản đồ plus con số lớn", rủi ro là bỏ mất dấu hỏi đó và biến một mốc đang tranh luận
thành một mốc chắc chắn.

### 4. Không thể sao chép phần render

Đây là điểm quan trọng nhất về mặt kỹ thuật. Ink Explainer dùng nền vẽ đầy khung, vùng sáng
gradient từ đống lửa, độ sâu không khí, texture đá. TossExplains bị khóa ngược lại:
`no gradients, no shadows, no textures, no photorealism, no 3D`.

Nghĩa là: học **hệ thống quyết định** của video này, không học bề mặt mỹ thuật của nó.

## Cách áp dụng cho TossExplains mà vẫn giữ đúng style lock

### Định nghĩa ba chế độ trong phạm vi style lock

| Chế độ | Dạng trong TossExplains | Tỷ lệ đề xuất |
| --- | --- | --- |
| A. Cảnh kể chuyện | cảnh doodle trên nền màu phẳng một tone, không chữ | 50-55% |
| B. Thẻ trắng | nền trắng, diagram hoặc số hoặc bản đồ hoặc object card, chữ marker | 35-40% |
| C. Cut-in Toss | Toss một mình trên nền trắng, không đạo cụ, một biểu cảm rõ | 6-8% |

Ba chế độ này đạt được bằng flat color, không cần gradient. Vùng sáng cam quanh đống lửa
của video mẫu có thể thay bằng **đổi màu nền phẳng theo chương** và một vòng halo phẳng
nếu cần nhấn mạnh.

### Mục tiêu nhịp đề xuất

| Phần | Beat mỗi phút | Giây mỗi beat |
| --- | ---: | ---: |
| 45 giây đầu | 34-40 | 1,5-1,8 |
| Thân bài, phần giải thích | 25-30 | 2,0-2,4 |
| Payoff cảm xúc hoặc lật luận đề | 35-43 | 1,4-1,7 |
| Đoạn kết | 28-32 | 1,9-2,1 |

Với video 10 đến 14 phút, nhịp này ra khoảng 280 đến 400 visual beat. Không cần 400 ảnh
độc lập. Dùng ba cấp:

1. Hero scene mới cho mỗi ý lớn.
2. Biến thể build A/B/C/D trên cùng base plate, mỗi biến thể một delta duy nhất: thời
   gian, số lượng, biểu cảm, ánh sáng, hoặc một icon overlay.
3. Thẻ trắng chèn giữa để reset mắt.

Một base plate tốt cho 3 đến 5 beat.

### Quy tắc scene nên bổ sung vào quy trình

Trước khi viết prompt, gán mỗi câu narration vào một vai:

- Locate: chuyện này xảy ra ở đâu?
- Demonstrate: hành động gì đang diễn ra?
- Explain: cơ chế nào gây ra nó? (thường là thẻ trắng, không phải cảnh màu)
- Evidence: bằng chứng nào? (bản đồ có pin, thẻ con số, thẻ trích dẫn nghiên cứu)
- Compare: hai trạng thái khác nhau thế nào? (split card)
- Quantify: lớn hay nhỏ đến mức nào?
- Emotionalize: người xem cảm thấy gì?
- Punctuate: cần một cut-in Toss để ngắt ý không?

Nếu một frame không làm ít nhất một vai, nó chỉ là trang trí.

### Năm kỹ thuật có thể áp dụng ngay, không phá style lock

1. **Đẩy chữ ra khỏi cảnh màu.** Mọi nhãn, con số, tên nghiên cứu đi sang thẻ trắng riêng.
   Cảnh màu chỉ kể chuyện. Đây là thay đổi đơn giản nhất và có tác động lớn nhất đến cảm
   giác "scene bắt mắt".
2. **Cut-in Toss làm dấu ngắt câu.** Cứ 20 đến 40 giây một lần, đặt trước mỗi khẳng định
   mới. Chi phí sản xuất gần bằng không, giá trị nhịp rất cao.
3. **Base plate cộng delta.** Lập kế hoạch trước: cảnh nào là base plate, delta nào sẽ
   được thêm ở beat nào. Không vẽ lại cảnh.
4. **Rule of three rồi merge.** Ba lần lặp cùng bố cục, rồi một frame gộp lại. Rất hiệu
   quả cho các danh sách và các quan hệ "cái này giống cái kia".
5. **Biên nhận cho mọi khẳng định.** Mỗi nghiên cứu được nêu tên có một thẻ trích dẫn.
   Mỗi con số có một thẻ số. Mỗi địa điểm có một bản đồ có pin. Đoạn này chính là thứ tạo
   cảm giác video được nghiên cứu kỹ.

### Tỉ lệ đa dạng hình ảnh đề xuất cho TossExplains

Đây là tỉ lệ tham chiếu, không phải khóa cứng:

- 25-30% cảnh nhân vật và tình huống đời sống hiện đại.
- 15-20% cảnh tâm lý bên trong: thought object, memory, brain.
- 15-20% thẻ trắng giải thích cơ chế và thẻ trích dẫn nghiên cứu.
- 10-15% then-vs-now hoặc split comparison.
- 10-15% anthropology: tribe, ritual, ancestral environment.
- 5-10% thẻ con số và scale.
- 5-8% cut-in Toss.

Không để cùng một layout xuất hiện quá hai beat liên tiếp, trừ khi đang progressive build
có chủ ý. Không để quá 6 beat liên tiếp cùng một chế độ.

## Checklist review cho mỗi video TossExplains tiếp theo

- 15 giây đầu có ít nhất 9 đến 11 visual beat khác nhau.
- Hook diễn một tình huống trước khi nói luận đề, không giới thiệu chủ đề trong 10 giây đầu.
- Không có chữ nào nằm trên cảnh màu, trừ khi đó là sound lettering có chủ ý.
- Cứ 20 đến 40 giây có ít nhất một cut-in Toss hoặc một thẻ trắng để reset mắt.
- Mỗi nghiên cứu được nêu tên có một thẻ trích dẫn riêng.
- Mỗi con số lớn có thẻ số riêng và một phép so sánh cụ thể.
- Mỗi địa điểm anthropology có một bản đồ hoặc một bối cảnh chức năng, không phải phong
  cảnh chung chung.
- Mỗi chương mở bằng một thẻ tiêu đề và đóng bằng một payoff nhìn thấy được.
- Progressive build chỉ giữ các trạng thái thêm thông tin thực sự.
- Nhịp của chương payoff nhanh hơn nhịp của chương giải thích.
- Chữ và nhãn vẫn đọc được khi thu frame còn 25% kích thước.
- Màu nền đổi theo chương và vẫn tôn trọng background budget của TossExplains.
- Toss và `@YOU` giữ đúng reference sheet.
- Mọi con số, mốc thời gian và quan hệ nhân quả được kiểm tra độc lập trước khi render.
- Phần kết chiếu cơ chế khoa học trở lại một cảm xúc hoặc hành động của người xem, và echo
  lại câu hỏi mở đầu.

## Thứ tự xem bộ frame

| Contact sheet | Frame | Timeline |
| --- | --- | --- |
| [01](contact-sheets/contact-sheet-01.jpg) | 001-024 | 00:00.00-00:35.60 |
| [02](contact-sheets/contact-sheet-02.jpg) | 025-048 | 00:36.53-01:16.80 |
| [03](contact-sheets/contact-sheet-03.jpg) | 049-072 | 01:17.90-02:03.13 |
| [04](contact-sheets/contact-sheet-04.jpg) | 073-096 | 02:06.27-02:51.60 |
| [05](contact-sheets/contact-sheet-05.jpg) | 097-120 | 02:53.37-03:34.60 |
| [06](contact-sheets/contact-sheet-06.jpg) | 121-144 | 03:38.53-04:18.67 |
| [07](contact-sheets/contact-sheet-07.jpg) | 145-168 | 04:21.67-04:59.00 |
| [08](contact-sheets/contact-sheet-08.jpg) | 169-192 | 04:59.97-05:43.17 |
| [09](contact-sheets/contact-sheet-09.jpg) | 193-216 | 05:44.67-06:29.73 |
| [10](contact-sheets/contact-sheet-10.jpg) | 217-240 | 06:31.20-07:24.40 |
| [11](contact-sheets/contact-sheet-11.jpg) | 241-264 | 07:27.07-08:14.40 |
| [12](contact-sheets/contact-sheet-12.jpg) | 265-288 | 08:15.27-09:00.50 |
| [13](contact-sheets/contact-sheet-13.jpg) | 289-312 | 09:04.27-10:06.07 |
| [14](contact-sheets/contact-sheet-14.jpg) | 313-336 | 10:08.90-10:55.33 |
| [15](contact-sheets/contact-sheet-15.jpg) | 337-355 | 10:59.27-11:33.87 |
