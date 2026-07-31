# Phân tích hình ảnh - Why Ancient Humans Couldn't Afford to Lose Their Grandparents

Kênh **Before Civilization** (`https://www.youtube.com/@BeforeCivilization-01`). Số view chưa
xác định, không đọc được bằng script. Link:
`https://www.youtube.com/watch?v=MDa6ZFH9XIo`

Xác thực file: `youtube-verify.py` trả VERIFIED (exit 0), vì tên file chứa đúng video id
`MDa6ZFH9XIo`. Tiêu đề, tên kênh và slug trong tài liệu này lấy trực tiếp từ oEmbed, không
gõ lại bằng tay.

## Kết quả extract

| Thông số | Giá trị |
| --- | --- |
| Thời lượng | 25:31.75 (1531.75 giây) |
| Độ phân giải | 1920 x 1072 |
| fps | 30.0 |
| Coded frame (ước lượng) | 45.952 |
| Candidate ở threshold 0.02 | 1.252 (49.0 mỗi phút) |
| Frame giữ lại | **728** |
| Candidate bị loại | **524** |
| Contact sheet | 31 |
| Index | `frame-index.csv` (729 dòng, kể cả header) |
| Dung lượng | 170 MB frame + 22 MB sheet |

Phương pháp: scene detection ffmpeg ở threshold 0.02, xuất candidate, đọc **toàn bộ 209
review sheet** (6 frame mỗi sheet, 776 px mỗi ô), quyết định loại bằng tay, rồi `finalize`
đánh số lại liên tục. Không sample, không bỏ sheet nào.

### Vì sao video này sinh ra 1.252 candidate

Threshold 0.02 được calibrate cho doodle explainer cắt cứng, khoảng 30 candidate mỗi phút.
Video này ra 49 mỗi phút vì nó **animate liên tục**: 446 trong 1.251 khoảng cách giữa các
candidate ngắn hơn 0,10 giây (một tới ba frame ở 30 fps), và 747 candidate nằm trong 273
chùm frame gần như liền nhau. Detector đang lấy mẫu chuyển động, không phải trạng thái.

Nâng `--threshold` **không** giải được chuyện này, và đây là lý do cụ thể: hai từ caption
thật `DO` và `LIVE` ở 05:11 có diff 4.05 và 5.55, đúng dải với các frame trùng do icon
đồng hồ cát quay (1.79 tới 6.46). Threshold không phân biệt được, nâng lên là xoá mất cơ chế
đặc trưng nhất của video. Nên giữ 0.02 và loại bằng tay.

### Bốn nhóm bị loại, theo lý do

| Mã | Số frame | Lý do |
| --- | ---: | --- |
| D3 | 232 | trùng do camera drift: cùng caption, cùng nội dung, chỉ khác vài pixel zoom |
| D5 | 131 | bước phóng to của chữ caption (chữ vào nhỏ, vọt lớn, rồi ổn định) |
| D1 | 119 | frame đen tuyệt đối của fade và frame trung gian của nó |
| D2 | 25 | frame giữa cú wipe bụi ở 04:10.13 tới 04:11.30 |
| D4 | 17 | chỉ có icon đồng hồ cát quay, mọi thứ khác giữ nguyên |

Chi tiết theo timestamp của những cụm lớn nhất:

- **04:10.13 tới 04:11.30**, 24 candidate: một cú wipe bụi duy nhất dài 1,2 giây. Toàn bộ là
  frame giữa hai trạng thái, không có nội dung câu chuyện nào. Loại hết theo lý do 2.
- **05:09.80 tới 05:12.57**, 23 candidate cho 7 trạng thái thật. Plate là cảnh cháy rừng
  ([frame 153](extracted-frames/frame-153_05m08.83s.jpg)), câu chữ là
  `HOW / MANY / TRUE / CATASTROPHES / DO / LIVE / THROUGH`, phần dư là icon đồng hồ cát quay.
- **19:34.40 tới 19:38.73**, 30 candidate cho 14 trạng thái. Tỉ lệ dư tệ nhất cả video.
- **24:59.50 tới 24:59.77**, 9 candidate: chữ `TRANSMISSION` phóng to rồi thu lại.
- Mọi cú fade đều sinh đúng một frame đen (`sharp 0.0`) cộng một tới hai frame trung gian.
  Có 119 frame như vậy, tức khoảng 40 cú fade trong 25 phút.

Không loại một frame nào chỉ vì edge energy thấp. Tám frame thấp nhất đều là frame đen của
fade, đúng như dự đoán, và chúng bị loại theo lý do 2 chứ không vì điểm số.

## Kết luận quan trọng nhất

**Video này không kể chuyện bằng cách vẽ thêm. Nó giữ một tấm nền tĩnh rồi đổi từng chữ một
lên trên đó.** Đó là toàn bộ cơ chế: 728 beat trong 25 phút, nhưng số tấm nền thật ít hơn
nhiều, vì một plate duy nhất thường phải đỡ cả một câu dài 7 tới 11 từ.

Bằng chứng đo được: cảnh người kể chuyện trên bãi biển Australia
([frame 297](extracted-frames/frame-297_11m05.57s.jpg)) sinh 25 candidate cho 9 trạng thái
chữ, và hai cánh tay giơ lên của người già **không hề động** suốt cả đoạn. Cảnh khúc xương
đùi đã lành ([frame 554](extracted-frames/frame-554_20m18.97s.jpg)) đỡ trọn câu
`AND EVERY SINGLE ONE OF THOSE INJURIES SHOWS HEALING` trong 2,5 giây mà không đổi hình. Cảnh
người ngồi giữa vòng dữ liệu xanh ([frame 650](extracted-frames/frame-650_23m25.87s.jpg)) đỡ
`WE STORED FACTS BRILLIANTLY` bằng 13 candidate.

Hệ quả cho người viết prompt: **số ảnh cần vẽ nhỏ hơn số beat rất nhiều.** Đây là cách một
kênh một người dựng được video 25 phút mà vẫn dày. Không phải vẽ 728 ảnh, mà vẽ khoảng 320
tấm nền rồi để chữ làm phần còn lại.

## Nhịp hình ảnh

| Thông số | Giá trị |
| --- | ---: |
| Beat | 728 |
| Beat mỗi phút | 28.5 |
| Giây mỗi beat (duration / beats) | **2.10** |
| Khoảng cách trung vị | 1.77 |
| Khoảng cách dưới 1 giây | 256 |
| Khoảng cách dưới 2 giây | 394 trên 727 |
| Khoảng cách từ 4 giây trở lên | 106 |
| Beat trong 15 giây đầu | 18 |
| Hook 0 tới 45 giây | 34 beat, 1.34 giây mỗi beat, 45.3 mỗi phút |

Giữ duy nhất chỉ số `duration / beats` = **2.10** trong toàn bộ tài liệu này, giống cách
`the-rarest-human-possible` làm.

Hold dài nhất: 9.03 giây ở frame 691, 8.30 giây ở
[frame 486](extracted-frames/frame-486_17m44.53s.jpg), 8.00 giây ở
[frame 711](extracted-frames/frame-711_25m00.30s.jpg), 7.67 giây ở frame 230, 7.43 giây ở
[frame 371](extracted-frames/frame-371_13m42.17s.jpg).

### Nhịp theo chương

| Đoạn | Frame | Beat mỗi phút | Giây mỗi beat |
| --- | --- | ---: | ---: |
| Hook điện thoại chết | 001-021 | 62.5 | 0.96 |
| Điều người già giữ trong đầu | 022-126 | 28.1 | 2.14 |
| Công cụ và truyền dạy | 127-137 | 37.4 | 1.60 |
| Thảm hoạ và ký ức sống | 138-169 | 27.9 | 2.15 |
| Phép so sánh voi ma trưởng | 170-186 | 21.0 | 2.86 |
| Không phải tình cảm mà là sổ sách | 187-223 | 28.6 | 2.10 |
| Bằng chứng thực địa, các bà | 224-265 | 21.7 | 2.77 |
| Thứ không cân đong được | 266-296 | 23.0 | 2.61 |
| Bờ biển Australia và bản đồ kể | 297-349 | 30.9 | 1.94 |
| Kayak, công nghệ mất rồi quay lại | 350-385 | 28.3 | 2.12 |
| Địa hình, nhịp điệu, nghi lễ là bộ nhớ | 386-450 | 28.9 | 2.08 |
| Lần theo dấu và đọc sao | 451-501 | 22.8 | 2.63 |
| Mạng lưới, cưới xin, nơi trú, trao đổi | 502-527 | 25.0 | 2.40 |
| Vùng đất khắc nghiệt và xương đã lành | 528-602 | 38.4 | 1.56 |
| Cái hàm không còn răng | 603-635 | 25.5 | 2.35 |
| Lệch pha hiện đại | 636-691 | 30.2 | 1.98 |
| Kết, dòng nào đã dứt | 692-728 | 55.6 | 1.08 |

Đọc bảng này: video **không** front-load đơn điệu như `why-humans-eat-3-meals-a-day`, cũng
không tăng tốc đều như Ink Explainer. Nó là **hình chữ U**. Hook 62.5 beat mỗi phút, tụt
xuống đáy 21.0 ở chương voi, rồi bật lên 55.6 ở đoạn kết. Chương chậm nhất
([frame 170](extracted-frames/frame-170_05m39.90s.jpg) tới
[frame 186](extracted-frames/frame-186_06m25.63s.jpg)) là chương ẩn dụ, nơi khán giả phải tự
nối con voi với con người, và biên tập cho họ thời gian làm việc đó.

Hai đỉnh tốc độ nằm ở hai chỗ khác nhau về bản chất. Hook nhanh vì cắt cảnh liên tục.
Chương `Vùng đất khắc nghiệt` nhanh 38.4 beat mỗi phút vì **chữ chạy nhanh, không phải hình
đổi nhanh**: 30 candidate ở 19:34 chỉ nằm trên một plate băng duy nhất. Đây là điểm quan
trọng nhất của bảng: **beat mỗi phút ở kênh này đo tốc độ chữ, không đo tốc độ vẽ.**

## Các cơ chế, theo thứ tự xuất hiện

### 1. Hook là một vật hiện đại tan thành bụi (00:00 tới 00:19)

Câu đầu tiên là `YOUR PHONE DIES TONIGHT` dựng từng chữ trên đúng một plate: người ngồi
trên sofa tối, mặt buồn ([frame 1](extracted-frames/frame-001_00m00.00s.jpg)). Chữ `TONIGHT`
phóng to rồi ổn định ([frame 5](extracted-frames/frame-005_00m01.27s.jpg)). Ngay sau đó là
payoff vật thể: màn hình nứt, các khối màu tan thành khói đen
([frame 7](extracted-frames/frame-007_00m01.60s.jpg)), rồi cái điện thoại vụn thành bụi trong
một hố xoáy tối ([frame 17](extracted-frames/frame-017_00m13.60s.jpg), diff 109.5).

Hook chỉ chuyển sang thời tiền sử ở giây 15
([frame 18](extracted-frames/frame-018_00m14.93s.jpg)), sau khi đã bán xong cảm giác mất dữ
liệu. **18 beat trong 15 giây đầu.** Cấu trúc: một mất mát hiện đại, một vật tan rã, rồi mới
tới quá khứ.

### 2. Chữ nằm trên nền tranh, không nằm trên thẻ trắng

Không có một frame trắng nào trong 728 frame. Mọi caption là chữ **trắng đậm ALL CAPS có
viền đen dày**, đặt thẳng lên nền tranh, thường ở khoảng trống giữa hai nhân vật.

Đây là sự khác biệt lớn nhất so với Ink Explainer, vốn đẩy mọi chữ sang thẻ trắng riêng.
Before Civilization giải bài toán dễ đọc bằng **viền đen cộng vị trí**, không bằng nền
riêng. Ví dụ rõ nhất: trên plate lửa đêm
([frame 68](extracted-frames/frame-068_02m15.30s.jpg)), câu
`TWO THREE PEOPLE AROUND EACH FIRE` được xếp vào đúng khe giữa người già bên trái và đứa
trẻ ở giữa, chỗ nền tối và trống nhất.

### 3. Nhịp phóng chữ ba trạng thái

Mỗi từ vào theo ba bước: nhỏ, vọt to quá cỡ, rồi lùi về cỡ ổn định. Đo được rõ ở
17:22: chữ `FOOTPRINTS` nhỏ, rồi rất to, rồi ổn định ở
[frame 475](extracted-frames/frame-475_17m22.57s.jpg). Đây là nguồn của 131 frame D5 bị loại.

Một lần duy nhất video dùng bước "vọt to" làm hiệu ứng chính thức thay vì bước trung gian:
chữ `TRANSMISSION` ở [frame 708](extracted-frames/frame-708_24m59.60s.jpg) là chữ lớn nhất
trong cả video, chiếm gần hết chiều ngang khung, và nó rơi đúng vào câu kết luận.

### 4. Icon đồng hồ cát pixel, một motif quay liên tục (05:08.83)

Một icon đồng hồ cát pixel-art đen trắng xuất hiện ở góc trên trái
([frame 153](extracted-frames/frame-153_05m08.83s.jpg)) và **quay không ngừng**. Nó đánh dấu
những đoạn nói về thời gian dài. Về mặt kỹ thuật nó là thứ phá scene detection nặng nhất
trên các plate tĩnh. Về mặt thẩm mỹ nó là dị vật: pixel-art 8-bit nằm trên tranh vẽ tay.

### 5. Hai hệ chữ, không phải một

Ngoài caption sans-serif đậm, video còn có:

- **Thẻ số giấy xé**: một tấm giấy trắng nhỏ mang chữ số viết tay, ví dụ số `7` ở
  [frame 318](extracted-frames/frame-318_11m36.03s.jpg), đặt trên nền dải Ngân Hà và một
  hàng người dài hút tầm mắt.
- **Chữ viết tay mềm vẽ vào tranh**: `Gone forever` ở
  [frame 333](extracted-frames/frame-333_12m16.30s.jpg), viết bằng nét trắng mảnh có bông
  tuyết, hoà vào trời đêm. Dùng đúng một lần, cho beat cảm xúc.

Ba hệ chữ, ba việc khác nhau: tường thuật, đếm, và thở.

### 6. Base plate cộng progressive build hai lớp cùng lúc (19:35 tới 19:39)

Đây là cơ chế mạnh nhất tìm thấy. Trên một plate băng tĩnh
([frame 527](extracted-frames/frame-527_19m34.37s.jpg)), video vừa chạy caption từng từ, vừa
**vẽ dần một chữ X đỏ lớn theo từng nét**:

- [frame 530](extracted-frames/frame-530_19m35.27s.jpg) nét thứ nhất
- [frame 532](extracted-frames/frame-532_19m35.90s.jpg) nét thứ hai bắt đầu
- [frame 535](extracted-frames/frame-535_19m36.13s.jpg) chữ X hoàn chỉnh

Chữ X hoàn thành đúng lúc caption tới `MOST`, và cả câu là một phủ định:
`MOST MARGINAL HABITATS HUMANS EVER OCCUPIED`. Hai build song song trên một tấm hình tĩnh.

Đây là ANNOT duy nhất có animation. Còn lại video dùng dấu `!` đỏ tĩnh cộng một vòng tròn
đỏ, ví dụ ở [frame 93](extracted-frames/frame-093_03m07.40s.jpg) và
[frame 523](extracted-frames/frame-523_19m19.50s.jpg).

### 7. Cặp macro và wide để đổi thang bậc

Video liên tục ghép một cảnh rộng với một macro của cùng chủ đề:

- Hàm răng: [frame 94](extracted-frames/frame-094_03m08.83s.jpg) hai cái răng khổng lồ trên
  bệ, rồi [frame 96](extracted-frames/frame-096_03m12.90s.jpg) hai cái xương hàm so sánh.
- Sọ: [frame 570](extracted-frames/frame-570_20m42.97s.jpg) cái sọ trên đất hang, rồi
  [frame 571](extracted-frames/frame-571_20m45.97s.jpg) macro đúng cái hàm đã mòn.
- Hàm không răng: [frame 602](extracted-frames/frame-602_21m30.07s.jpg) rồi
  [frame 603](extracted-frames/frame-603_21m32.60s.jpg) đẩy sâu thêm.
- Nấu ăn: [frame 574](extracted-frames/frame-574_20m54.67s.jpg) bàn tay nghiền quả trên đá,
  ngay sau cảnh rộng của cùng động tác.

Khung macro luôn là **bàn tay hoặc vật thể, không có mặt**. Đó là cách video chèn nhịp mà
không cần thêm nhân vật.

### 8. Frame vắng người, dùng làm dấu chấm câu

82 trên 728 frame (11.3 phần trăm) không có người làm chủ thể. Chúng luôn rơi vào chỗ
chuyển ý:

- [frame 452](extracted-frames/frame-452_16m23.00s.jpg) cánh đồng muối trắng phẳng, một
  người bé xíu, đường chân trời trống.
- [frame 453](extracted-frames/frame-453_16m26.30s.jpg) tường tranh hang đã mờ đi một nửa.
- [frame 521](extracted-frames/frame-521_19m16.77s.jpg) một vòng đá bếp lạnh và vết chân,
  không còn ai.
- [frame 685](extracted-frames/frame-685_24m26.80s.jpg) tường bò rừng đầy ochre với đúng một
  cục ochre đỏ nằm trên sàn trống.
- [frame 370](extracted-frames/frame-370_13m35.53s.jpg) một cánh đồng đầy khung thuyền vỡ.

**Frame vắng người là cách video nói "mất" mà không cần chữ.**

### 9. Nhân vật hiện đại đầu trọc, nhân vật cổ có tóc

Phân biệt thời gian bằng đúng một dấu hiệu: người hiện đại là hình que **đầu trọc trơn**,
người cổ có **tóc dày và áo lông**. 48 frame hiện đại (6.6 phần trăm) so với 680 frame cổ.

Cách này cho phép video nhảy thời gian không cần transition: từ hang vẽ bò rừng
([frame 645](extracted-frames/frame-645_23m12.53s.jpg)) sang phòng server
([frame 644](extracted-frames/frame-644_23m11.57s.jpg)) sang máy in cổ
([frame 643](extracted-frames/frame-643_23m10.93s.jpg)) trong hai giây.

### 10. Ảnh luận đề: cái điện thoại trong tủ kính bảo tàng

[frame 636](extracted-frames/frame-636_22m54.23s.jpg) là ảnh mang toàn bộ luận đề của video
trong một khung: một chiếc smartphone nằm trong tủ kính bảo tàng, ngay cạnh một bức tường
tranh hang kiểu Lascaux, người hiện đại chìa tay về phía nó.

Video lặp lại ý này ở đoạn kết theo chiều ngược:
[frame 712](extracted-frames/frame-712_25m08.30s.jpg), người hiện đại **chụp ảnh** một cái
rìu đá trong tủ kính bằng điện thoại.

### 11. CTA giữa video, gắn vào một cảnh hiện đại (04:25 tới 04:28)

Ở phút thứ 4, tức 17 phần trăm thời lượng, video cắt sang phòng khách hiện đại
([frame 133](extracted-frames/frame-133_04m25.37s.jpg)), một nút `Subscribe` đỏ trượt vào từ
góc dưới phải ([frame 135](extracted-frames/frame-135_04m26.20s.jpg)), và caption đọc
`THAT LANDED FOR SUBSCRIBE NOW` ([frame 137](extracted-frames/frame-137_04m27.37s.jpg)).

Đáng chú ý: CTA **không** đặt trên nền tiền sử. Nó nhảy về hiện tại, xin, rồi fade đen quay
lại. Thời lượng chỉ 3 giây.

### 12. Cực tối dùng đúng vài lần

Video sáng và ấm phần lớn thời gian, và để dành đen cho vài chỗ:

- [frame 266](extracted-frames/frame-266_09m45.13s.jpg) gần như đen tuyệt đối, một người
  khum hai tay quanh một cục than hồng. Câu trên nó là
  `YOU CANNOT PUT THAT ON A SCALE`.
- [frame 546](extracted-frames/frame-546_19m48.20s.jpg) hai người được chiếu **đỏ** hoàn toàn
  bởi lửa, mặt phát sáng.
- [frame 340](extracted-frames/frame-340_12m28.40s.jpg) một người dưới cực quang xanh.

### 13. Đoạn kết dùng frame vắng người làm câu phủ định

Xem mục riêng bên dưới.

## Phân tích từng chương

| Thời gian | Frame | Hình làm gì | Đạt được gì |
| --- | --- | --- | --- |
| 00:00-00:26 | 001-021 | điện thoại chết, dữ liệu tan thành bụi, rồi nhảy về tiền sử | bán cảm giác mất mát bằng vật hiện đại trước khi nói tới quá khứ |
| 00:26-04:11 | 022-126 | người già chỉ chỗ nước, đọc dấu, dạy trên sườn đồi; xen bằng chứng răng và hàm | dựng luận đề: cái đầu người già là hạ tầng, và có dấu vết khảo cổ |
| 04:11-04:28 | 127-137 | tay xâu kim, lao xương, người già cầm tay đứa trẻ khắc gỗ; rồi CTA | chốt ý truyền dạy bằng cận cảnh bàn tay, xin sub ngay lúc cảm xúc cao |
| 04:28-05:38 | 138-169 | cháy rừng, hạn, bệnh; icon đồng hồ cát vào | đổi thang thời gian từ một đời sang nhiều đời |
| 05:38-06:27 | 170-186 | đàn voi và voi ma trưởng, không lời giải thích | để khán giả tự nối ẩn dụ, chương chậm nhất 21.0 beat mỗi phút |
| 06:27-07:47 | 187-223 | người già ăn, đi chậm, làm gánh nặng, rồi đống lưỡi đá đã làm xong | trả lời phản biện "giữ người già vì tình cảm" bằng hình sổ sách |
| 07:47-09:45 | 224-265 | nhà nghiên cứu hiện đại, ống nhòm, ba bà đào củ, đồng hồ bấm giây | chuyển từ kể sang đo, cấp uy tín cho luận đề |
| 09:45-11:05 | 266-296 | than hồng trong lòng tay, lưới cá, chia thịt, tường tranh | phần "không cân đong được", đối lập với chương đo đếm ngay trước |
| 11:05-12:47 | 297-349 | người kể chuyện trên bãi biển, đồng bằng đầy vỏ sò, băng tan, thẻ số 7 | ví dụ mạnh nhất: ký ức truyền miệng vượt hàng nghìn năm |
| 12:47-14:04 | 350-385 | thuyền rỉ nước, khung vỡ, rồi kayak hoàn chỉnh và cảnh trao cung | vòng mất rồi lấy lại công nghệ, dựng bằng cặp thất bại và thành công |
| 14:04-16:20 | 386-450 | vòm đá, dấu khắc trên cây, nhịp vỗ tay, nhảy, vạch đếm trên xương | mở rộng "bộ nhớ" ra ngoài lời nói: địa hình, nhịp, nghi lễ |
| 16:20-18:34 | 451-501 | cánh đồng muối trống, tường tranh mờ, dấu chân, thuyền dưới Ngân Hà | chương buồn nhất, nói về xoá; chậm 22.8 beat mỗi phút |
| 18:34-19:34 | 502-527 | cưới xin, hang trú mưa, trao vỏ sò, cung đá xếp thành vòng | người già là bộ nhớ của mạng lưới xã hội, không chỉ của kỹ thuật |
| 19:34-21:30 | 528-602 | plate băng với chữ X đỏ, rồi thung lũng xanh, rồi xương đùi đã lành | chương nhanh nhất giữa video, nhanh vì chữ chứ không vì hình |
| 21:30-22:54 | 603-635 | hàm không răng macro, người mớm ăn, sọ cạnh người vẽ tranh | bằng chứng chăm sóc: ai đó phải nghiền thức ăn cho người này |
| 22:54-24:52 | 636-691 | điện thoại trong tủ kính, máy in, phòng server, vòng dữ liệu, ngã ba đường | lệch pha hiện đại: lưu dữ kiện giỏi, mất cách truyền |
| 24:52-25:32 | 692-728 | bếp lạnh phủ tuyết, sọ trong sa mạc, xương truyền tay, rồi 13 cảnh hiện đại, rồi vòng lửa bốn thế hệ | đoạn kết, 55.6 beat mỗi phút |

## Vì sao phần kết hiệu quả

Đoạn kết dài 39 giây, 37 frame, 55.6 beat mỗi phút, nhanh gần bằng hook. Nó làm bốn việc
theo đúng thứ tự này.

**Một, nó phủ định bằng một frame vắng người.** Câu
`THE ONES WHO DIDN'T AREN'T YOUR ANCESTORS` không được đặt trên mặt ai. Nó đặt trên một
vòng đá bếp đã phủ tuyết với một cây lao rơi ngang
([frame 692](extracted-frames/frame-692_24m52.43s.jpg)), giữ suốt 6 trạng thái chữ tới
[frame 698](extracted-frames/frame-698_24m54.60s.jpg). Không có người vì đó chính là nội
dung: những người này đã hết.

**Hai, nó cắt sang cái sọ.** `THEIR LINES ENDED` rơi trên một cái sọ nửa vùi trong đá đỏ, có
một người đứng nhìn bên phải ([frame 699](extracted-frames/frame-699_24m55.20s.jpg) tới
[frame 702](extracted-frames/frame-702_24m56.03s.jpg)). Cặp bếp lạnh và cái sọ là hai ảnh
phủ định, không phải hai ảnh minh hoạ.

**Ba, nó đảo sang khẳng định bằng khung chặt nhất cả video.** Một two-shot cực cận, một khúc
xương được truyền từ tay này sang tay kia qua đống lửa
([frame 703](extracted-frames/frame-703_24m56.50s.jpg)), mang câu
`YOU OUTPUT OF UNBROKEN CHAIN OF TRANSMISSION`, kết bằng chữ lớn nhất trong phim ở
[frame 708](extracted-frames/frame-708_24m59.60s.jpg). Video đi từ khung rộng nhất, cánh đồng
băng trống, sang khung chặt nhất, hai bàn tay, trong 7 giây.

**Bốn, nó trả về hiện tại bằng 13 cảnh hàng ngày, rồi mới về lửa.** Từ
[frame 712](extracted-frames/frame-712_25m08.30s.jpg) tới
[frame 720](extracted-frames/frame-720_25m21.50s.jpg): chụp ảnh rìu đá trong bảo tàng, đi bộ
trong công viên với em bé trên ngực, ngồi một mình với album ảnh, ngồi cùng đứa trẻ xem điện
thoại, khuấy bột trong bếp, đặt tay lên cửa kính trước dải Ngân Hà, quỳ bên một bia mộ, viết
vào sổ tay. Tám hành động, không có chữ nào trên chúng.

Rồi mới về plate cuối: vòng lửa đêm bốn thế hệ
([frame 721](extracted-frames/frame-721_25m28.40s.jpg)) với câu
`BECAUSE THE FIRE WASN'T JUST FOR WARMTH`, đóng ở
[frame 728](extracted-frames/frame-728_25m31.30s.jpg).

Cấu trúc đóng vòng: mở bằng một người **một mình** với điện thoại trong phòng tối
([frame 1](extracted-frames/frame-001_00m00.00s.jpg)), đóng bằng một người **cùng đứa trẻ**
xem điện thoại trên sofa xanh ([frame 715](extracted-frames/frame-715_25m16.63s.jpg)). Cùng
đồ vật, cùng bố cục, khác một người. Đó là toàn bộ luận điểm nén vào một cặp hình.

## Những điểm không nên sao chép

### Lỗi thực tế tự kiểm tra được: frame `1.8 MILLION` vẽ sai thời đại

[frame 599](extracted-frames/frame-599_21m28.10s.jpg) mang caption `1.8 MILLION` và trình bày
như bằng chứng: một cái sọ thuộc về người cổ sống khoảng 1,8 triệu năm trước. Con số đó khớp
với sọ Dmanisi không răng ở Georgia, khoảng 1,77 tới 1,8 triệu năm.

Nhưng chính khung hình đó vẽ:

1. **Một cái rìu đá có cán** trong tay nhân vật. Kỹ thuật tra cán xuất hiện muộn hơn rất
   nhiều, chắc chắn nhất là trong vài trăm nghìn năm gần đây. Ở 1,8 triệu năm, công cụ là
   Oldowan cầm tay, không có cán.
2. **Ba con voi ma-mút** ở nền, cong ngà và gù vai, trên một savanna có cây keo. Voi ma-mút
   lông không sống ở savanna châu Phi và xuất hiện muộn hơn nhiều bậc.
3. **Nhân vật mặc áo lông và tóc dài y hệt** các nhân vật ở chương 30.000 năm trước. Không
   có một dấu hiệu hình nào phân biệt 1,8 triệu năm với 30.000 năm.

Đây không phải ý kiến thẩm mỹ. Ba chi tiết trong đúng một khung, và khung đó là khung mang
con số. Nếu TossExplains đặt một con số lên hình, **hình phải chịu được con số đó.**

### Lỗi thứ hai: 25 phút không nêu tên một nhà nghiên cứu nào trên hình

Video dựng nhà khoa học 14 lần, có kẹp giấy, ống nhòm, đồng hồ bấm giây, hố khai quật có
lưới dây và cờ vàng ([frame 228](extracted-frames/frame-228_08m02.93s.jpg),
[frame 233](extracted-frames/frame-233_08m19.77s.jpg),
[frame 393](extracted-frames/frame-393_14m27.17s.jpg)), nhưng **không một tên người, không
một tên địa điểm, không một năm công bố nào xuất hiện trên hình** trong toàn bộ 728 frame.

Nặng hơn: video ghép hai phát hiện thuộc hai tranh luận khác nhau thành một mạch liền. Mốc
"người già trở nên phổ biến khoảng 30.000 năm trước"
([frame 118](extracted-frames/frame-118_03m53.70s.jpg)) và cái sọ 1,8 triệu năm
([frame 599](extracted-frames/frame-599_21m28.10s.jpg)) không cùng loài và không cùng độ
chắc chắn. Trên hình không có gì báo cho khán giả biết điều đó.

`.agents/rules/channel-dna.md` buộc ít nhất 3 nhà nghiên cứu có tên trong script. Việc đó
phải **thấy được**, không chỉ nghe được.

### Lỗi thứ ba: ba bóng thoại chữ thường, sai hệ chữ

Ba khung mang bóng suy nghĩ với chữ **thường**, font UI trơn, hoàn toàn khác hệ caption ALL
CAPS có viền:

- [frame 491](extracted-frames/frame-491_18m02.63s.jpg) `Muscle vs map`
- [frame 656](extracted-frames/frame-656_23m27.77s.jpg) `Fact` (bóng còn đang phóng to)
- [frame 664](extracted-frames/frame-664_23m45.17s.jpg) `Running out of time`

Ba cái này đọc như ghi chú dựng phim bị bỏ lại trong bản final.

### Lỗi thứ tư: đầu người trống, không mặt

Nhiều khung có nhân vật nền là **hình bầu dục màu kem không mắt không miệng không tóc**,
trong khi nhân vật tiền cảnh vẽ đủ. Nặng nhất:

- [frame 667](extracted-frames/frame-667_23m50.17s.jpg), vòng lửa khoảng 18 người, phần lớn
  không mặt.
- [frame 682](extracted-frames/frame-682_24m19.13s.jpg), hàng thế hệ, ba hình bên trái trống
  hoàn toàn.
- [frame 433](extracted-frames/frame-433_15m36.33s.jpg) và
  [frame 406](extracted-frames/frame-406_15m05.00s.jpg).

Đây là lỗi sinh ảnh, hệ thống, không phải một lần. Nó xuất hiện đúng ở các khung đông người,
tức là khung tốn công nhất và cũng là khung video muốn dùng để nói "cả cộng đồng".

### Lỗi thứ năm: một icon vector lạc vào tranh

[frame 486](extracted-frames/frame-486_17m44.53s.jpg) có một **ghim bản đồ màu hồng cánh
sen**, vector phẳng kiểu UI, dán lên cảnh thuyền dưới dải Ngân Hà. Nó là khung hold lâu thứ
hai của cả video, 8.30 giây, nên không thể không thấy. Icon đồng hồ cát pixel ở
[frame 153](extracted-frames/frame-153_05m08.83s.jpg) cũng cùng loại vấn đề, nhẹ hơn vì đơn
sắc.

### Phần render không được phép sao chép

`.agents/rules/visual-style.md` cấm dứt khoát những thứ làm nên vẻ ngoài của video này:

| Video này có | TossExplains |
| --- | --- |
| tranh vẽ có chuyển sắc, khối sáng tối, chiều sâu khí quyển | `no gradients, no shadows, no textures` |
| bóng đổ dài trên đất, ánh lửa hắt lên mặt | cấm bóng, cấm texture |
| nền tối chiếm phần lớn thời lượng | trắng là mặc định, 55 tới 75 phần trăm |
| xanh cobalt dùng cho đêm, băng, biển | cobalt **chỉ** dùng khi khung đang ở trong đầu ai đó |
| camera zoom và drift liên tục | ảnh tĩnh, không có khái niệm camera |
| chữ viền đen đặt trên tranh | chữ ALL CAPS đặt ở **đỉnh** khung, đen hoặc đỏ |

Nói cụ thể: **không được** bắt chước [frame 485](extracted-frames/frame-485_17m44.13s.jpg)
hay [frame 546](extracted-frames/frame-546_19m48.20s.jpg). Chúng đẹp vì có gradient và ánh
sáng, đúng hai thứ style lock cấm. Bốn chuỗi verbatim trong `visual-style.md` thắng mọi thứ
đáng thích trong video này.

## Cách áp dụng cho TossExplains

### Register cho kênh này, và register tương ứng của ta

Từ vựng mode phải quyết định từ sheet, không thừa hưởng. Ink Explainer có
`FULL / WHITE / NARR / SPLIT`. Past Tense có `CARD / MAP / SEQ`. Before Civilization
**không có một frame trắng nào**, nên phân loại phải khác hẳn:

| Register | Frame | Phần trăm |
| --- | ---: | ---: |
| STORY, cảnh tranh có 1 tới 3 nhân vật | 416 | 57.1 |
| CLOSE, macro bàn tay hoặc mặt hoặc vật cầm tay | 62 | 8.5 |
| CAVE, trong hang, thường có tranh trên vách | 58 | 8.0 |
| MODERN, hiện tại: căn hộ, văn phòng, bảo tàng, phòng server | 48 | 6.6 |
| FIRE, vòng lửa đêm | 47 | 6.5 |
| OBJ, một vật đơn độc, không ai tác động | 38 | 5.2 |
| LAND, phong cảnh rộng, người bé xíu hoặc vắng | 32 | 4.4 |
| GROUP, từ 5 người trở lên | 15 | 2.1 |
| ANIMAL, con vật là chủ thể | 12 | 1.6 |

**326 lần đổi register, trung bình 2.23 frame một chuỗi.** Con số này gần y hệt Ink Explainer
(2.6) và Past Tense (2.26). Ba kênh, ba style vẽ khác nhau hoàn toàn, cùng một tần số đổi
register. Đây là phát hiện chuyển giao được rõ nhất của cả ba nghiên cứu:
**đổi register khoảng mỗi 2 tới 2,5 beat, bất kể vẽ kiểu gì.**

Bảng đổi sang từ vựng của ta, vẫn trong style lock:

| Của họ | Của ta | Nền |
| --- | --- | --- |
| STORY | cast reaction, then vs now split, status ladder | trắng |
| CLOSE | concept text frame với một vật lớn ở giữa | trắng |
| CAVE | frame bộ lạc, vòng quanh lửa | tan hoặc cam |
| MODERN | đời sống hiện đại, ít vật nhất có thể | trắng |
| FIRE | frame bộ lạc | cam `#F5820D` |
| OBJ | concept text frame | trắng |
| LAND | ngoài trời | xanh lá `#3A9E3A` cộng trời xanh |
| GROUP | frame bộ lạc | tan `#C4965A` |
| ANIMAL | evolution sequence hoặc villain personified | trắng |

Lưu ý: 93.4 phần trăm frame của họ là cảnh cổ. Của ta phải ngược lại, vì tone map buộc trắng
là mặc định và trắng thuộc về đời sống hiện đại. Lấy **cấu trúc** của họ, không lấy tỉ lệ.

### Beat target theo chương, nhịp hình chữ U

Nhịp 2.10 giây mỗi beat của họ hợp với video 25 phút. Video ta dài 10 tới 14 phút, nên bám
hình dạng chứ không bám con số tuyệt đối:

| Chương | Beat mỗi phút | Ghi chú |
| --- | ---: | --- |
| Hook | 45 tới 60 | cắt nhanh, một mất mát hiện đại cụ thể, không phải khái niệm |
| Reframe | 30 tới 35 | |
| Psychology deep dive | 25 tới 30 | |
| Ẩn dụ hoặc thí nghiệm | **20 tới 24** | chậm nhất, để khán giả tự nối |
| Nguồn gốc nhân học | 25 tới 30 | |
| Lệch pha hiện đại | 30 tới 35 | |
| Kết | **50 tới 56** | nhanh lại, gần bằng hook |

### Sáu kỹ thuật sống sót được với màu phẳng

1. **Base plate cộng progressive build.** Giữ nguyên một khung, thêm đúng một thứ mỗi beat:
   một mũi tên, một nhãn, một nhân vật. Đây là cơ chế chính của họ và nó không cần gradient.
   Mẫu: [frame 68](extracted-frames/frame-068_02m15.30s.jpg).
2. **Vẽ dần một dấu đỏ theo từng nét**, hoàn thành đúng lúc caption tới từ phủ định. Mẫu:
   [frame 530](extracted-frames/frame-530_19m35.27s.jpg) tới
   [frame 535](extracted-frames/frame-535_19m36.13s.jpg). Với ta là chữ X đỏ `#D94040` trên
   nền trắng, và nó phải rơi vào một từ đỏ trong danh sách được phép: nguy hiểm, thất bại,
   phủ định.
3. **Cặp wide và macro của cùng một vật.** Cảnh rộng rồi cận. Mẫu:
   [frame 570](extracted-frames/frame-570_20m42.97s.jpg) và
   [frame 571](extracted-frames/frame-571_20m45.97s.jpg). Macro luôn là bàn tay hoặc vật, không
   có mặt.
4. **Frame vắng người làm dấu chấm câu.** Một cái bếp lạnh, một cây gậy rơi, một cái ghế
   trống. Nhắm khoảng 10 phần trăm frame. Mẫu:
   [frame 692](extracted-frames/frame-692_24m52.43s.jpg).
5. **Đóng vòng bằng cặp hình đối xứng.** Cùng bố cục, cùng đồ vật, đổi đúng một biến. Mẫu:
   [frame 1](extracted-frames/frame-001_00m00.00s.jpg) và
   [frame 715](extracted-frames/frame-715_25m16.63s.jpg). Với ta là `@YOU` một mình rồi
   `@YOU` cùng một cast member khác, hai frame trắng giống nhau.
6. **Chốt bằng khung chặt nhất, không phải khung rộng nhất.** Họ đi từ cánh đồng băng trống
   sang hai bàn tay trong 7 giây
   ([frame 692](extracted-frames/frame-692_24m52.43s.jpg) tới
   [frame 703](extracted-frames/frame-703_24m56.50s.jpg)). Với ta là hai bàn tay doodle trên
   nền trắng.

### Thứ không lấy được, và thay bằng gì

Họ đặt chữ trên nền tranh, giải bài dễ đọc bằng viền đen. Ta **không** làm thế:
`visual-style.md` quy định chữ ALL CAPS ở **đỉnh khung**, màu đen hoặc đỏ, trên nền phẳng.
Nền trắng phẳng vốn đã dễ đọc, nên viền là dư thừa và trái style lock.

Điều lấy được từ hệ chữ của họ là **kỷ luật ba hệ, mỗi hệ một việc**:

| Việc | Của họ | Của ta |
| --- | --- | --- |
| tường thuật | caption trắng viền đen | ALL CAPS đen ở đỉnh khung |
| phủ định, nguy hiểm | chữ X đỏ vẽ dần | ALL CAPS đỏ `#D94040`, hoặc chữ X đỏ |
| đếm, con số | thẻ giấy xé có số viết tay | concept text frame, vật lớn cộng số ở đỉnh |
| beat cảm xúc | chữ viết tay vẽ vào tranh | **không có**, dùng bóng suy nghĩ thay |

Chữ viết tay mềm kiểu [frame 333](extracted-frames/frame-333_12m16.30s.jpg) không có chỗ
trong style lock. Thay bằng bóng suy nghĩ mây cổ điển với `HMMMM`, `?`, `WAIT...`.

## Checklist review cho mỗi video TossExplains tiếp theo

- [ ] Nền trắng chiếm 55 tới 75 phần trăm số prompt. Đếm, đừng đoán.
- [ ] Cobalt `#2D5FBF` chỉ dùng khi chủ thể là não, vòng suy nghĩ, hoặc vật thể ký ức. Không
      dùng cho đêm, buồn, hay nghiêm trọng.
- [ ] Không có gradient, bóng đổ, texture, chiều sâu khí quyển trong bất kỳ prompt nào.
- [ ] Chữ trên hình là ALL CAPS, đặt ở đỉnh khung, chỉ đen hoặc đỏ. Không vàng trên trắng.
- [ ] Đỏ chỉ dành cho nguy hiểm, thất bại, phủ định. Đếm tỉ lệ đen so với đỏ, mục tiêu quanh
      114 so với 44 như fixture đã nhận.
- [ ] Đổi register khoảng mỗi 2 tới 2,5 beat. Ba video đã nghiên cứu đều rơi vào 2.23 tới 2.6.
- [ ] Nhịp có hình chữ U: hook nhanh, chương ẩn dụ chậm nhất, kết nhanh lại gần bằng hook.
- [ ] Có ít nhất một chuỗi base plate cộng progressive build, thêm đúng một thứ mỗi beat.
- [ ] Có ít nhất một cặp wide cộng macro của cùng một vật.
- [ ] Khoảng 10 phần trăm frame vắng người, đặt ở chỗ chuyển ý.
- [ ] Frame đầu và frame cuối là một cặp đối xứng, đổi đúng một biến.
- [ ] Frame chốt là khung chặt nhất, không phải khung rộng nhất.
- [ ] Mọi con số trên hình phải được hình đỡ: đừng vẽ rìu có cán cạnh chữ `1.8 MILLION`.
- [ ] Tên nhà nghiên cứu và mốc thời gian **thấy được trên hình**, không chỉ có trong script.
- [ ] Mọi nhân vật trong mọi khung đều có mắt, miệng, và đường lông mày. Không có đầu trống.
- [ ] Không có icon vector, emoji, hay pixel-art lạc vào giữa doodle.
- [ ] Mọi caption đúng một hệ chữ. Không có chữ thường lọt vào bản final.
- [ ] Bốn chuỗi verbatim trong `visual-style.md` copy đúng từng ký tự. Chạy `/check`.

## Thứ tự xem bộ frame

| Sheet | Frame | Thời gian |
| --- | --- | --- |
| [01](contact-sheets/contact-sheet-01.jpg) | 001-024 | 00:00.00-00:27.00 |
| [02](contact-sheets/contact-sheet-02.jpg) | 025-048 | 00:27.30-01:28.23 |
| [03](contact-sheets/contact-sheet-03.jpg) | 049-072 | 01:30.07-02:16.77 |
| [04](contact-sheets/contact-sheet-04.jpg) | 073-096 | 02:17.07-03:12.90 |
| [05](contact-sheets/contact-sheet-05.jpg) | 097-120 | 03:15.97-03:58.63 |
| [06](contact-sheets/contact-sheet-06.jpg) | 121-144 | 04:02.63-04:49.27 |
| [07](contact-sheets/contact-sheet-07.jpg) | 145-168 | 04:50.57-05:34.07 |
| [08](contact-sheets/contact-sheet-08.jpg) | 169-192 | 05:35.53-06:29.63 |
| [09](contact-sheets/contact-sheet-09.jpg) | 193-216 | 06:30.03-07:25.00 |
| [10](contact-sheets/contact-sheet-10.jpg) | 217-240 | 07:27.07-08:40.83 |
| [11](contact-sheets/contact-sheet-11.jpg) | 241-264 | 08:46.07-09:37.33 |
| [12](contact-sheets/contact-sheet-12.jpg) | 265-288 | 09:41.43-10:41.20 |
| [13](contact-sheets/contact-sheet-13.jpg) | 289-312 | 10:42.83-11:18.60 |
| [14](contact-sheets/contact-sheet-14.jpg) | 313-336 | 11:22.97-12:22.27 |
| [15](contact-sheets/contact-sheet-15.jpg) | 337-360 | 12:22.47-13:08.60 |
| [16](contact-sheets/contact-sheet-16.jpg) | 361-384 | 13:11.30-14:01.47 |
| [17](contact-sheets/contact-sheet-17.jpg) | 385-408 | 14:01.80-15:10.73 |
| [18](contact-sheets/contact-sheet-18.jpg) | 409-432 | 15:13.23-15:35.57 |
| [19](contact-sheets/contact-sheet-19.jpg) | 433-456 | 15:36.33-16:34.43 |
| [20](contact-sheets/contact-sheet-20.jpg) | 457-480 | 16:36.23-17:25.03 |
| [21](contact-sheets/contact-sheet-21.jpg) | 481-504 | 17:29.60-18:35.03 |
| [22](contact-sheets/contact-sheet-22.jpg) | 505-528 | 18:35.60-19:34.40 |
| [23](contact-sheets/contact-sheet-23.jpg) | 529-552 | 19:34.87-20:10.63 |
| [24](contact-sheets/contact-sheet-24.jpg) | 553-576 | 20:14.03-20:56.60 |
| [25](contact-sheets/contact-sheet-25.jpg) | 577-600 | 20:57.87-21:29.03 |
| [26](contact-sheets/contact-sheet-26.jpg) | 601-624 | 21:29.47-22:28.43 |
| [27](contact-sheets/contact-sheet-27.jpg) | 625-648 | 22:28.67-23:21.30 |
| [28](contact-sheets/contact-sheet-28.jpg) | 649-672 | 23:23.03-24:05.03 |
| [29](contact-sheets/contact-sheet-29.jpg) | 673-696 | 24:07.67-24:53.67 |
| [30](contact-sheets/contact-sheet-30.jpg) | 697-720 | 24:54.07-25:21.50 |
| [31](contact-sheets/contact-sheet-31.jpg) | 721-728 | 25:28.40-25:31.30 |
