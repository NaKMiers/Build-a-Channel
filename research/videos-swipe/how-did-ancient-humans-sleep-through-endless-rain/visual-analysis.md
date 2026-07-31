# Phân tích hình ảnh - How Did Ancient Humans Sleep Through Endless Rain?

Kênh: Before Civilization (`https://www.youtube.com/@BeforeCivilization-01`). Link gốc:
`https://www.youtube.com/watch?v=iYub7rFKhE8`. Số view không đọc được bằng script vì YouTube
chặn bot ở watch page. Xác minh bằng `tools/youtube-verify.py`: **VERIFIED**, video id
`iYub7rFKhE8` nằm trong tên file; tiêu đề và tên kênh lấy trực tiếp từ oEmbed.

Tên thư mục đã được sửa. Bộ tải về cắt ngắn tiêu đề thành `...-sleep-through-end`, nhưng slug
thật từ oEmbed là `how-did-ancient-humans-sleep-through-endless-rain`.

## Kết quả extract

- Video nguồn: **26:19.51** (1579,51 giây), 1920x1072, 30 FPS, khoảng 47.385 frame mã hóa.
- Bộ nghiên cứu: **349 trạng thái hình ảnh**, giữ nguyên 1920x1072.
- Contact sheet: **15 trang**. Index: `frame-index.csv` (350 dòng, 1 dòng header).

### Phương pháp, và vì sao ngưỡng không phải 0.02

Đây là video đầu tiên trong bộ nghiên cứu **không dùng được ngưỡng mặc định 0.02**. Ở 0.02 nó
cho ra **973 ứng viên, 37,0 mỗi phút**, và con số đó vô nghĩa, vì ba lý do cùng lúc:

1. **Phụ đề karaoke từng chữ được nung vào khung hình.** Bộ phát hiện scene bắn một lần cho
   mỗi **từ được đọc**: "tonight" / "you'll" / "lie" / "down". Nếu giữ ngưỡng 0.02 thì "beat mỗi
   phút" đo tốc độ nói, không đo nhịp hình ảnh.
2. **Lớp mưa động phủ lên cảnh tĩnh.** 290 trên 972 khoảng cách nhỏ hơn 0,11 giây, và cụm lớn
   nhất là **24 ứng viên trong đúng 1,00 giây** của một cảnh lều duy nhất, chỉ có các vệt mưa
   ngang di chuyển.
3. **Mỗi lần chuyển cảnh đều fade qua đen tuyền hoặc trắng tuyền.**

So sánh ba ngưỡng trên chính file này:

| Ngưỡng | Ứng viên | Mỗi phút | Khoảng cách dưới 0,11s | Khoảng cách trung bình |
| --- | ---: | ---: | ---: | ---: |
| 0.02 (mặc định) | 973 | 37,0 | 290 (29,8 phần trăm) | 1,62s |
| **0.06 (đã dùng)** | **433** | **16,4** | **50 (11,6 phần trăm)** | **3,64s** |
| 0.12 | 366 | 13,9 | 24 (6,6 phần trăm) | 4,31s |

Chọn **0.06**: đây là ngưỡng thấp nhất triệt được hiện tượng bắn theo từng từ mà vẫn bắt được
thay đổi thật bên trong một cảnh đang giữ, kể cả khi thay đổi đó chỉ là một chữ caption xuất
hiện. Chủ kênh đã xác nhận lựa chọn này.

### Cảnh báo: bộ này đo "tấm nền", không đo "trạng thái caption"

Một nghiên cứu khác về **cùng kênh này**,
`research/videos-swipe/why-ancient-humans-coundnt-afford-to-lose-their-grandparents/`, đã giữ
ngưỡng **0.02** và loại 524 trên 1252 ứng viên **bằng tay** theo năm lớp, giữ lại 728 frame.
Cách đó bảo toàn được **một frame cho mỗi từ caption đã đứng yên**, tức chính cơ chế đặc trưng
của kênh: giữ một tấm nền tĩnh rồi đổi chữ trên đó.

Bộ nghiên cứu này thì không. Ở ngưỡng 0.06, nó chỉ giữ **45 frame có caption**, tức phần lớn
trạng thái caption đã bị bỏ. Hệ quả phải nói rõ:

| Bộ nghiên cứu | Ngưỡng | Giữ | Đơn vị thực sự được đo |
| --- | --- | ---: | --- |
| `...-lose-their-grandparents` | 0.02 cộng 524 drop tay | 728 | trạng thái caption, một cho mỗi từ |
| **bộ này** | 0.06 | 349 | **tấm nền và cú cắt**, caption chỉ được lấy mẫu |

**Con số 13,3 beat mỗi phút dưới đây là nhịp của tấm nền, không phải nhịp caption**, và **không
so sánh được** với con số của bộ grandparents. Mọi kết luận về nhịp trong tài liệu này chỉ đúng
ở cấp độ tấm nền và cú cắt.

### Đã loại 84 trên 433 ứng viên

**60 frame hoàn toàn đồng nhất.** Sau khi cắt bỏ vùng watermark, 60 frame có **phương sai
đúng bằng 0**: đen tuyền hoặc trắng tuyền. Frame có cấu trúc thấp thứ hai đạt điểm 25, và trung
vị là 61,6, nên đây là một ranh giới nhị phân sạch, không cần phán đoán. Video fade qua **cả
đen và trắng**: 24 frame trắng tuyền có chỉ số `sharp` giống nhau tới hai chữ số thập phân
(3,43) vì phần sai khác duy nhất còn lại là cái watermark ở góc.

**14 frame chuyển tiếp có nội dung nhưng không đọc được**, gồm 8 vệt nhòe do lia máy
(00:19.47, 00:20.60, 00:20.63, 00:20.67, 03:24.13, 03:24.17, 04:36.97, 04:37.00) và 6 frame
fade dở dang khi hình chưa hiện ra (00:56.00, 03:12.03, 04:52.80, 04:54.63, 05:19.03, 05:19.13).

**10 frame trùng lặp thật**, gồm bảy frame giữa của một chuỗi 1,00 giây trên **một** cảnh lều
(03:08.10 tới 03:08.83) mà thứ duy nhất thay đổi là lớp vệt mưa, cộng ba frame cách frame trước
đúng 0,03 giây và không thay đổi gì (06:47.13 với diff 0,07; 07:36.60; 13:21.83).

### Một lỗi phương pháp đáng ghi lại

Bộ lọc thống kê đầu tiên của tôi gắn cờ **89** frame là "gần như đồng nhất" dựa trên độ lệch
chuẩn thấp. Khi soi từng cái thì **phần lớn là cảnh thật**, chỉ là đang ở đáy của một cú fade
vào từ đen: bố cục đã vẽ xong đầy đủ, chỉ tối. Ví dụ
[frame 176](extracted-frames/frame-176_13m04.67s.jpg),
[frame 286](extracted-frames/frame-286_21m04.53s.jpg) và
[frame 132](extracted-frames/frame-132_09m57.63s.jpg) đều bị gắn cờ sai và đều là frame hoàn
chỉnh. **Độ tối không phải độ trống.** Phép thử đúng là chuẩn hóa tương phản rồi đo cấu trúc,
không phải đo độ sáng trung bình.

## Kết luận quan trọng nhất

Video này **không giữ người xem bằng nhịp**. Nó chạy **13,3 beat mỗi phút**, tức chậm hơn hai
video đã nghiên cứu trước **hai lần rưỡi** (32,3 và 30,6). Cơ chế trung tâm của nó là:
**một hình duy nhất được nêu ra ở giây thứ chín, rồi bị lấy đi, rồi được giành lại trong 26
phút, rồi lặp lại ở phút thứ 25.**

Hình đó là **một tấm da căng trên đầu để che mưa**:

| Frame | Thời điểm | Trạng thái |
| --- | --- | --- |
| [frame 2](extracted-frames/frame-002_00m09.57s.jpg) | 00:09.57 | tấm da căng trên đầu, giữa đồng mưa. **Câu trả lời được đưa ra ở giây thứ 9.** |
| [frame 58](extracted-frames/frame-058_03m39.87s.jpg) | 03:39.87 | cận cảnh, hai tay giơ tấm da lên, nước bắn ra hai bên. Lần này nó được **phát minh**. |
| [frame 343](extracted-frames/frame-343_25m38.03s.jpg) | 25:38.03 | một phiến vỏ cây giơ lên trong hẻm núi mưa, 24 phút sau. |

Đó là toàn bộ cấu trúc của phim: **cho xem đáp án, rồi bắt người xem ngồi 25 phút để hiểu tại
sao đáp án đó khó.** Không có build trên thẻ, không có chữ đè, không có diagram nào ở đoạn hook.
Chỉ có một hành động, ba lần.

Và cơ chế thứ hai, cái làm nên chất riêng: **caption một chữ màu đỏ có viền sáng trắng, chạy
theo từng từ được đọc, nằm đè lên cảnh chứ không nằm trên thẻ.** Bộ nghiên cứu giữ 45 frame có
caption, và chúng cho thấy một thủ pháp mà hai video trước không có:
**caption giữ nguyên trong khi hình lật sang mặt đối lập.**

- [frame 52](extracted-frames/frame-052_03m14.30s.jpg) 03:14.30: lều mái vòm sáng lửa trong
  đêm mưa, caption "important".
- [frame 53](extracted-frames/frame-053_03m14.87s.jpg) 03:14.87: cắt thẳng sang đồng trống xám,
  người co ro ướt sũng, **vẫn caption "important"**.

Cùng thủ pháp ở [frame 186](extracted-frames/frame-186_13m38.43s.jpg) và
[frame 187](extracted-frames/frame-187_13m39.07s.jpg), cả hai caption "ash". Một từ, hai hình
ngược nhau, và người xem tự nối.

## Nhịp hình ảnh

Số của tool, không làm tròn lại:

- beat: **349**
- beat mỗi phút: **13,3**
- khoảng cách trung bình giữa các beat: **4,52 giây**
- khoảng cách trung vị: **3,44 giây**
- khoảng cách dưới 1 giây: 47
- khoảng cách dưới 2 giây: 115 trên 348
- khoảng cách **từ 4 giây trở lên: 148**, tức 42,5 phần trăm
- beat trong 15 giây đầu: **2**
- hook (0 tới 45 giây): 12 beat, **3,94 giây mỗi beat**, tức 16,0 mỗi phút
- hold dài nhất: **27,10 giây** ở frame 331, rồi 21,37 ở frame 96, 17,27 ở frame 64,
  16,93 ở frame 346, 15,36 ở frame 78

Ở toàn bộ tài liệu này, "giây mỗi beat" là **khoảng cách trung bình giữa các beat**.

| Đoạn | Frame | Beat mỗi phút | Giây mỗi beat |
| --- | --- | ---: | ---: |
| Hook | 001-011 | 17,3 | 3,46 |
| Kiệt sức trong mưa | 012-022 | 17,6 | 3,40 |
| Chỗ trú đầu tiên | 023-038 | 16,6 | 3,61 |
| Vòng đá và bằng chứng | 039-051 | 14,8 | 4,05 |
| Lều dệt và lửa | 052-072 | 12,5 | 4,80 |
| Khảo cổ hiện đại | 073-093 | 10,8 | 5,57 |
| Giường lá và tro | 094-149 | 13,3 | 4,51 |
| Truyền lại | 150-205 | 15,1 | 3,96 |
| Thất bại và nước | 206-220 | 14,5 | 4,14 |
| Vòng ngủ và người thức | 221-260 | 11,5 | 5,24 |
| Băng hà và lều xương | 261-298 | 15,3 | 3,92 |
| Nhà đá và giường đá | 299-322 | 12,2 | 4,91 |
| Kết | 323-349 | 11,3 | 5,29 |

Hình dạng ở đây **khác cả hai video trước**. Video 3-meals dồn hết vào hook rồi chậm dần đơn
điệu. Video ancient-humans tăng tốc ở các payoff cảm xúc. Video này gần như **phẳng**: biên độ
chỉ từ 10,8 tới 17,6 beat mỗi phút, tức nhanh nhất chưa gấp đôi chậm nhất. Không có đoạn nào
được phép chạy.

Hai điều đáng học từ bảng này:

1. **Hook không nhanh.** 17,3 beat mỗi phút, và **chỉ 2 beat trong 15 giây đầu**. Frame đầu
   được giữ **9,57 giây** trước khi có cắt. Đây là chiến lược ngược hoàn toàn với 3-meals
   (14 beat trong 15 giây đầu). Nó hoạt động vì frame đầu là một hình quen tới mức không cần
   giải thích: [frame 1](extracted-frames/frame-001_00m00.00s.jpg), một người đang ngủ, đèn ấm,
   mưa trên cửa sổ.
2. **Đoạn chậm nhất là "Khảo cổ hiện đại", 10,8 beat mỗi phút.** Đó là đoạn đưa bằng chứng:
   hố cột, lớp đất, than. Phim giữ lâu ở chỗ người xem phải **đọc một hình phức tạp**, giống
   quy tắc đã thấy ở video 3-meals. Frame chi tiết nhất của đoạn đó,
   [frame 87](extracted-frames/frame-087_06m29.20s.jpg), có sharpness 38,26.

Chỉ 47 trên 348 khoảng cách dưới 1 giây, và gần một nửa số khoảng cách vượt 4 giây. Phim này
cho người xem thời gian, và đó là một lựa chọn, không phải sự thiếu sót.

## Mười cơ chế làm video này hoạt động

### 1. Chỉ có hai register, và tỉ lệ giữa chúng là 8 trên 1

Không có thẻ, không có bản đồ, không có mũi tên, không có split-screen, không có nền trắng.
Toàn bộ 349 frame chia làm:

| Register | Số frame | Tỉ lệ |
| --- | ---: | ---: |
| `ANC` cảnh tiền sử vẽ tay full-bleed | 295 | 85,8 phần trăm |
| `MOD` cảnh hiện đại | 39 | 11,3 phần trăm |
| `CAPONLY` chỉ còn chữ caption trên nền trơn | 6 | 1,7 phần trăm |
| `PAPER` nền giấy da trống | 3 | 0,9 phần trăm |
| `FX` frame hiệu ứng | 1 | 0,3 phần trăm |

Tám mươi sáu phần trăm là một register duy nhất. Phim không luân phiên chế độ để chống nhàm, nó
**dùng một chế độ và thay đổi thời tiết bên trong chế độ đó**. Ba cảnh mưa liên tiếp ở
[frame 13](extracted-frames/frame-013_00m47.27s.jpg),
[frame 15](extracted-frames/frame-015_00m50.13s.jpg) và
[frame 17](extracted-frames/frame-017_00m57.57s.jpg) là cùng một hành động trong ba nhiệt độ
màu: xanh lạnh, xám xanh, rồi băng giá với **vệt nhiệt màu cam bốc ra khỏi tay** người.

Đây là điểm TossExplains **không** nên bắt chước trực tiếp, vì `visual-style.md` đòi 55 tới 75
phần trăm nền trắng phẳng. Nhưng nguyên tắc bên dưới thì chuyển được: **đổi thời tiết và ánh
sáng thay vì đổi loại khung.**

### 2. Cảnh hiện đại là một tấm gương, và nó xuất hiện đúng lúc

39 frame `MOD` không rải đều. Chúng luôn đứng ngay cạnh một frame cổ đại tương ứng, làm thành
cặp gương:

| Cổ đại | Hiện đại | Nội dung cặp |
| --- | --- | --- |
| [frame 254](extracted-frames/frame-254_18m49.43s.jpg) | [frame 255](extracted-frames/frame-255_18m54.97s.jpg) | **ba mươi người ngủ thành vòng tròn quanh một đống lửa** trong hang, so với **một người trên giường, mặt xanh vì ánh điện thoại** |
| [frame 229](extracted-frames/frame-229_16m35.57s.jpg) | [frame 230](extracted-frames/frame-230_16m47.50s.jpg) | người thức canh bên lửa, so với người đứng áp tay vào cửa kính ban đêm |
| [frame 258](extracted-frames/frame-258_19m01.27s.jpg) | [frame 259](extracted-frames/frame-259_19m13.40s.jpg) | người cầm giáo đứng canh hai đứa trẻ đang ngủ, so với người nằm thao thức cạnh **đồng hồ báo thức phát sáng hồng** |

Cặp đầu là frame mạnh nhất phim. [Frame 254](extracted-frames/frame-254_18m49.43s.jpg) có
khoảng ba mươi người nằm thành một vòng kín, đầu hướng vào tâm, quanh một đống lửa duy nhất,
và **một hàng dấu bàn tay đỏ bằng đất son trên vách hang phía trên**. Frame ngay sau nó là một
người, một cái điện thoại, không có vòng nào. Phim không nói gì. Nó chỉ đặt hai hình cạnh nhau.

### 3. Fade qua đen là dấu chấm câu, và nó dùng 60 lần

Không có cut cứng giữa các chương. Mọi chuyển cảnh lớn đi qua **một frame đen tuyền hoặc trắng
tuyền**, và trong bộ 433 ứng viên có 60 frame như vậy. Chúng đã bị loại khỏi bộ nghiên cứu vì
không mang thông tin, nhưng **sự tồn tại của chúng chính là cơ chế**: phim thở giữa các ý bằng
cách tắt hình hoàn toàn.

Hệ quả đo được: cú thay đổi lớn nhất toàn phim là **diff 253,81** ở 14:19.40, và nó xảy ra vì
phim cắt **từ trắng tuyền sang đen tuyền** trong hai frame liền nhau. Không có nội dung nào ở
đó cả.

TossExplains không có nền đen trong tone map, nên bản chuyển được là: **một beat nền trắng
trống hoàn toàn, không vật thể nào, giữa hai chương.**

### 4. Ba lớp scale trên cùng một chủ thể: chân, macro, rồi toàn cảnh

Phim dạy một kỹ thuật bằng cách quay nó ở ba khoảng cách liên tiếp. Ví dụ rõ nhất là vòng đá:

1. [frame 44](extracted-frames/frame-044_02m44.17s.jpg) 02:44.17: chỉ thấy **hai cái chân** ở
   góc trên trái, tảng đá lớn chiếm hết khung. Mặt bị giữ lại.
2. [frame 45](extracted-frames/frame-045_02m45.17s.jpg) 02:45.17: cận cảnh **một bàn tay đẩy
   viên đá vào chỗ**, chỉ còn thấy bàn chân và vạt áo lông.
3. [frame 46](extracted-frames/frame-046_02m46.37s.jpg) 02:46.37: lùi ra, người đứng giữa
   **vòng đá đã hoàn thành** trên mỏm núi, thung lũng xanh phía sau.

Cùng ngữ pháp cho lều xương voi ma mút:
[frame 280](extracted-frames/frame-280_20m38.57s.jpg) cận cảnh xương hàm xếp lớp,
[frame 282](extracted-frames/frame-282_20m48.77s.jpg) macro **lưới xương đan** với một bàn tay
nhồi rêu vào kẽ, rồi [frame 281](extracted-frames/frame-281_20m40.87s.jpg) toàn cảnh khung mái
vòm hoàn thiện. Và cho tường phên: [frame 87](extracted-frames/frame-087_06m29.20s.jpg).

Đây là cơ chế **chuyển được nguyên vẹn** sang TossExplains, vì nó không cần gradient hay
texture, chỉ cần ba prompt ở ba khoảng cách.

### 5. Cặp trước-sau trên cùng một bố cục, và nó dùng ít nhất tám lần

Phim gần như không bao giờ nói "cách này tốt hơn". Nó vẽ cùng một khung hai lần:

| Trước | Sau | Nội dung |
| --- | --- | --- |
| [frame 103](extracted-frames/frame-103_07m36.57s.jpg) | [frame 104](extracted-frames/frame-104_07m39.07s.jpg) | lửa lụi và khói trắng dày, so với lửa cháy tốt dưới mái lá |
| [frame 213](extracted-frames/frame-213_15m19.60s.jpg) | [frame 212](extracted-frames/frame-212_15m12.43s.jpg) | giường sập nát trong vũng nước, so với giường hoàn chỉnh trên vành tro trắng |
| [frame 320](extracted-frames/frame-320_23m36.13s.jpg) | [frame 321](extracted-frames/frame-321_23m44.90s.jpg) | **nước dội thành tấm khỏi mái tranh** với người lo lắng, so với người tươi cười trong ô cửa sáng khi mái đã ăn khớp |
| [frame 310](extracted-frames/frame-310_22m52.10s.jpg) | [frame 311](extracted-frames/frame-311_22m56.93s.jpg) | giường đá trống, so với giường đá đã lót thạch thảo, dương xỉ và da lông |
| [frame 133](extracted-frames/frame-133_10m06.20s.jpg) | [frame 134](extracted-frames/frame-134_10m07.23s.jpg) | vệt tro trắng trên sàn hang, so với lá xanh đã rải lên trên lớp tro đó |

Cặp cuối là một **build hai bước trên một bố cục**, thứ gần nhất với cơ chế base-plate của
video 3-meals mà phim này có.

### 6. Diagram chỉ xuất hiện ba lần, và cả ba lần đều làm hết việc của cả chương

Trong 349 frame chỉ có ba khung thật sự là diagram, và chúng gánh toàn bộ phần lập luận:

- [frame 112](extracted-frames/frame-112_08m12.93s.jpg) 08:12.93: **mặt cắt đất**, người đứng
  trên mặt cỏ và phần đất bên dưới bị cắt ra để thấy rễ và đá.
- [frame 165](extracted-frames/frame-165_12m26.47s.jpg) 12:26.47: **khối giường bị cắt mở** cho
  thấy bốn lớp phân biệt bằng màu: cỏ khô trên cùng, lá xanh, **tro trắng**, rồi đất. Đây là
  frame giải thích cả chương giường lá.
- [frame 188](extracted-frames/frame-188_13m39.73s.jpg) 13:39.73: một vách đá vẽ **chồng lớp
  lặp lại**: lá xanh, than đen, tro trắng, lá xanh, than đen, tro trắng, kèm caption "again".
  Chữ nói cho bạn rằng cái chồng đó lặp; hình cho bạn thấy nó lặp.

Ba diagram trong 26 phút. Phim tiết kiệm chúng tới mức mỗi lần xuất hiện là một sự kiện.

### 7. Người thức canh: một hình, sáu lần, và là frame cuối

Luận điểm của phim không được phát biểu, nó được vẽ sáu lần: **một người ngồi thức trong khi
người khác ngủ.**

[frame 229](extracted-frames/frame-229_16m35.57s.jpg) 16:35.57,
[frame 233](extracted-frames/frame-233_17m12.20s.jpg) 17:12.20,
[frame 246](extracted-frames/frame-246_18m02.57s.jpg) 18:02.57,
[frame 247](extracted-frames/frame-247_18m11.43s.jpg) 18:11.43 (bốn người đứng thành vòng
hướng ra ngoài quanh tám người đang ngủ, dưới trăng tròn),
[frame 258](extracted-frames/frame-258_19m01.27s.jpg) 19:01.27, và cuối cùng
[frame 348](extracted-frames/frame-348_26m13.20s.jpg) và
[frame 349](extracted-frames/frame-349_26m13.97s.jpg).

### 8. Caption dùng đúng ba lần chữ "you", và ba lần đó là ba cột mốc

Phim gần như không nói với người xem. Trong 45 frame có caption, chữ **"you"** chỉ xuất hiện
ba lần, và mỗi lần rơi vào một khoảnh khắc đã được chuẩn bị:

- [frame 212](extracted-frames/frame-212_15m12.43s.jpg) 15:12.43, trên **chiếc giường hoàn
  chỉnh** giữa nắng vàng.
- [frame 238](extracted-frames/frame-238_17m24.20s.jpg) 17:24.20, trên frame ấm nhất phim: một
  **người già tóc trắng chống gậy** và một người phụ nữ hai bên đống lửa, hai đứa trẻ ngủ giữa.
- [frame 310](extracted-frames/frame-310_22m52.10s.jpg) 22:52.10, bên **chiếc giường đá trống**.

Ba lần "you" ở ba lần phát minh thành công. Đó là cách dùng đại từ thứ hai đắt hơn nhiều so với
việc rắc nó khắp script.

### 9. Kiến trúc là nhân vật chính, không phải con người

Hold dài nhất phim là **27,10 giây** ở [frame 331](extracted-frames/frame-331_24m23.43s.jpg),
và không có mặt ai ở tiền cảnh. Nó có **khung lều xương voi ma mút bên trái, một nhà đá mái cỏ
trên mỏm đá bên phải, và một cái tổ chim ở tiền cảnh**, với một người nhỏ đi trên con đường ở
giữa. Ba loại chỗ ngủ, ba thời đại, một khung.

Nhìn cả năm hold dài nhất thì thấy quy luật rõ hơn: **bốn trên năm đều là một chỗ trú đang được
dựng, đang được ở, hoặc đang được so sánh.**

| Hold | Frame | Nội dung |
| ---: | --- | --- |
| 27,10s | [frame 331](extracted-frames/frame-331_24m23.43s.jpg) | ba loại chỗ ngủ trong một khung, người rất nhỏ |
| 21,37s | [frame 96](extracted-frames/frame-096_07m08.23s.jpg) | hai người lớn làm việc ngoài mưa, **một đứa trẻ giữ lửa bên trong lều tranh đang sáng**, sharp 31,81 |
| 17,27s | [frame 64](extracted-frames/frame-064_04m06.23s.jpg) | người hiện đại cuộn điện thoại, ngay sau frame CTA |
| 16,93s | [frame 346](extracted-frames/frame-346_25m54.17s.jpg) | người đặt một phiến đá lên bức tường thấp |
| 15,36s | [frame 78](extracted-frames/frame-078_05m31.77s.jpg) | người leo vách đá |

Hold không dành cho cảm xúc trên mặt, nó dành cho **chỗ trú và việc dựng chỗ trú**. Frame 64 là
ngoại lệ duy nhất, và nó là hệ quả của việc phim vừa xin một cú subscribe rồi phải để người xem
ngồi chờ.

Và frame chi tiết nhất toàn phim, sharpness 47,95, là
[frame 179](extracted-frames/frame-179_13m11.90s.jpg): một khu rừng nhiệt đới dày đặc dây leo,
dương xỉ và hoa vàng. Frame chi tiết thứ hai, 44,19, là
[frame 317](extracted-frames/frame-317_23m22.83s.jpg), người đang lợp mái bằng cỏ và đất cỏ.

### 10. Phá vỡ phong cách bốn lần, và ba trong bốn lần là sai

Phim vốn nhất quán: nhân vật đầu tròn màu kem, tay chân que đen, nền vẽ tay có texture. Bốn lần
nó phá cái đó:

- [frame 138](extracted-frames/frame-138_10m25.97s.jpg) 10:25.97: **những con bọ ảnh thật**,
  gần như nhiếp ảnh, bò trên tro trắng, trong cùng khung với một nhân vật que vẽ tay ở cửa hang.
- [frame 171](extracted-frames/frame-171_12m53.80s.jpg) 12:53.80: **một con muỗi ảnh thật** đậu
  trên một chiếc lá vẽ tay, do một bàn tay vẽ tay cầm.
- [frame 215](extracted-frames/frame-215_15m26.40s.jpg) 15:26.40: cùng chủ đề côn trùng nhưng
  **vẽ đúng theo phong cách phim**, một con bọ và một con rết doodle. Phim tự mâu thuẫn với chính
  nó trên cùng một chủ thể.
- [frame 218](extracted-frames/frame-218_15m40.80s.jpg) 15:40.80: một người trôi trong nước
  được vẽ thành **line-art trắng trên nền gần đen**, toàn đường viền, không tô. Sharpness 40,09.

Cái thứ tư là lần phá vỡ **thành công**: nó dành riêng một thứ ngôn ngữ hình cho một khoảnh
khắc chết chìm, và ngay frame sau
([frame 219](extracted-frames/frame-219_15m43.23s.jpg)) vẽ lại cùng khoảnh khắc theo phong
cách thường. Ba cái đầu thì chỉ là chất liệu không khớp.

## Phân tích từng chương

| Đoạn | Thời gian | Frame | Hình ảnh làm gì | Đạt được gì |
| --- | --- | --- | --- | --- |
| Hook | 00:00-00:34 | 001-011 | một người ngủ yên giữ 9,57 giây, rồi tấm da che mưa, rồi cùng người đó thao thức với điện thoại đang sạc, rồi một thân người phát sáng vàng, rồi nền giấy da trống | nêu đáp án ở giây thứ 9 rồi lấy nó đi, và chỉ tiêu 2 beat trong 15 giây đầu |
| Kiệt sức trong mưa | 00:39-01:13 | 012-022 | ba cảnh mưa cùng hành động ba nhiệt độ màu, trại bỏ hoang, giáo rơi, người ngã ngửa, năm con sói mắt cam, **một bộ não doodle trắng** trên đầu | dựng cái giá phải trả trước khi dựng giải pháp |
| Chỗ trú đầu tiên | 01:24-02:18 | 023-038 | ba người dựng lều chữ A, nội thất hang ấm, gương hiện đại (điện thoại, đồng hồ thông minh), hẻm núi **chuyển đen trắng**, Dải Ngân Hà, nhãn giấy xé "1.8 million years" | lần đầu có hợp tác, và lần duy nhất phim dùng nhãn nhiều chữ thay vì caption một chữ |
| Vòng đá và bằng chứng | 02:20-03:09 | 039-051 | ma mút trong rừng, **hố khai quật hiện đại**, chân, macro bàn tay, vòng đá hoàn thiện, lều phên với lớp vệt mưa động | ngữ pháp ba-lớp-scale ra mắt, và register khảo cổ hiện đại ra mắt |
| Lều dệt và lửa | 03:14-04:50 | 052-072 | caption "important" giữ nguyên qua một cú cắt lật ngược, vòng người quanh lửa trong lều, **tấm da giơ trên đầu lần hai**, tia nắng xuyên bão, **CTA "subscribe" gắn vào cảnh**, mái vòm dệt phát sáng | thủ pháp caption-bắc-cầu ra mắt, và phát minh trung tâm được giành lại |
| Khảo cổ hiện đại | 04:59-06:51 | 073-093 | bọt lửa bay lên trời sao, **bong bóng hai chữ Z**, hồn ma xanh, dấu chân, hố cột macro rồi vòng hố cột, bếp than, tường phên macro, "heidelbergensis" | đoạn chậm nhất phim, 10,8 beat mỗi phút, vì đây là đoạn phải đọc hình |
| Giường lá và tro | 07:02-11:10 | 094-149 | miệng hang đen tuyền, hold 21,37 giây trên một cái nhà, bong bóng "???", chuỗi caption "combination"/"actually"/"does", **CAPONLY "does"**, tro trắng rồi lá xanh lên trên, **bọ ảnh thật**, vành tro quanh giường, **cảnh mưa đen trắng** | chương dài nhất, và nó dựng phát minh chính bằng một cặp build hai bước |
| Truyền lại | 11:14-14:52 | 150-205 | người già bên lửa, tranh hang có hươu và vạch đếm, **khung split ngày và đêm**, **mặt cắt bốn lớp**, muỗi ảnh thật, rừng rậm 47,95, **người lớn đưa một chiếc lá cho đứa trẻ**, đoàn di cư tám người, **chồng lớp lặp lại "again"**, đốt giường cũ ba bước | chuyển từ phát minh sang di sản, và frame duy nhất có split-screen nằm ở đây |
| Thất bại và nước | 14:53-15:51 | 206-220 | hoàng hôn tím dữ dội, tia lửa đục đá, **lưỡi đá trong tro, đen trắng**, giường sập trong vũng nước, bọ doodle, băng giá, **người trôi vẽ bằng line-art** | phá vỡ phong cách thành công duy nhất, dùng cho khoảnh khắc chết |
| Vòng ngủ và người thức | 15:58-19:22 | 221-260 | tổ chim trống, vòng người quanh lửa bảy người, **trại ngủ hàng chục người phủ cả thung lũng**, cận cảnh mặt cực gần với con ngươi khe cam, **mắt thú phóng to nhòe**, cái ôm gia đình, **vòng ngủ ba mươi người với dấu bàn tay đỏ**, gương điện thoại | đoạn chậm thứ hai (11,5), và nó chứa frame mạnh nhất phim |
| Băng hà và lều xương | 19:33-21:58 | 261-298 | bão tuyết, đồng bằng trắng gần trống, **giấy da lần ba**, kéo xương, dựng vòm ngà, ma mút nguyên con, lồng xương sườn, macro xương hàm, khung xương hoàn thiện, **bốn người ngủ trong vòm xương** | palette rút về gần đơn sắc xanh trắng, và kiến trúc thành nhân vật |
| Nhà đá và giường đá | 22:01-23:54 | 299-322 | làng đá mái cỏ, mặt cắt nhà đá, hốc tường, **giường đá lót rêu**, **CAPONLY "And"**, "you" lần ba, bể nước có cá, **nội thất nhà đá về đêm với cả nhà ngủ**, mái tranh thoát nước | phát minh thành hạ tầng, và cutaway lần hai |
| Kết | 23:56-26:13 | 323-349 | **mưa nhìn qua cửa kính với một cốc trong tay**, thung lũng đầy đống lửa, vách dấu bàn tay, **hold 27,10 giây trên ba loại chỗ ngủ**, bong bóng Z hiện đại, **CAPONLY "is"**, phiến vỏ cây che mưa, người ngủ trên sofa cạnh điện thoại, và hai frame cuối: người thức bên đứa trẻ ngủ | không đóng vòng về frame đầu, và cố ý trao lời cuối cho quá khứ |

## Vì sao phần kết hiệu quả

Phần kết dài 27 frame, hai phút mười bảy giây, và nó **không** làm cái mà video 3-meals làm.
Nó không quay về frame mở đầu. Frame 1 là một phòng ngủ hiện đại; hai frame cuối là một đêm
lạnh trên đá cổ đại. Phim cố ý **trao lời cuối cho quá khứ**.

Bốn việc nó làm, theo thứ tự:

**Một, lật nghĩa của mưa.** [Frame 326](extracted-frames/frame-326_24m04.47s.jpg) ở 24:04.47 là
luận điểm của nửa hiện đại, và nó không có chữ nào: một người **đứng trong nhà, tay cầm cốc,
mỉm cười, nhìn mưa xối trên tấm kính lùa**. Suốt 24 phút mưa là thứ giết người. Ở frame này mưa
là thứ dễ chịu, và cái duy nhất thay đổi là **có một tấm kính**. Phát minh của cả phim, gói
trong một frame không lời.

**Hai, mở rộng từ một người sang tất cả.**
[Frame 329](extracted-frames/frame-329_24m13.93s.jpg) đặt một người bên một đống lửa, rồi
**một chuỗi khoảng hai mươi đống lửa nữa lùi dần lên thung lũng vào trong núi**. Rồi
[frame 330](extracted-frames/frame-330_24m19.97s.jpg) là một vách hang phủ **hàng chục dấu bàn
tay đỏ**, với người đang áp bàn tay mình lên đá. Từ một, sang nhiều, sang nghi lễ.

**Ba, hold 27,10 giây trên ba loại chỗ ngủ.**
[Frame 331](extracted-frames/frame-331_24m23.43s.jpg) là hold dài nhất phim và là frame tổng
kết: khung lều xương, nhà đá mái cỏ, và **một cái tổ chim ở tiền cảnh**. Phim để người xem tự
đọc rằng tổ chim cũng nằm trong cùng một dãy.

**Bốn, kết trên người thức canh, không phải trên phát minh.**
[Frame 347](extracted-frames/frame-347_26m11.10s.jpg) cho thấy chiếc giường hoàn chỉnh trong
hang lúc rạng sáng, và phim **không bình luận gì về nó**. Rồi
[frame 348](extracted-frames/frame-348_26m13.20s.jpg) và
[frame 349](extracted-frames/frame-349_26m13.97s.jpg): đêm lạnh trên đá ướt, một người ngồi
thức với đôi mắt buồn bên một đứa trẻ đang ngủ, caption "night" rồi "it". Hai frame cùng bố
cục, chỉ khác một chữ.

Phim kết thúc ở chỗ nó không hứa: không phải ở chiến thắng, mà ở việc vẫn phải có người thức.

## Những điểm không nên sao chép

### 1. File nguồn có một lỗi hiển thị, và nó nằm ngay trong khung

[Frame 25](extracted-frames/frame-025_01m27.10s.jpg) ở 01:27.10 mang **một khối chữ nhật đen
đặc**, khoảng 170x160 pixel, ở phần trên giữa khung, đè lên cảnh nội thất hang. Đây không phải
lựa chọn thiết kế; đó là lỗi giải mã hoặc lỗi render trong chính file. Tôi giữ frame lại vì
phần còn lại của nó là một trạng thái thật, nhưng nó là bằng chứng rằng **kể cả bản phát hành
của một kênh chạy tốt cũng có thể lọt lỗi hình**. Kiểm tra frame trước khi publish.

### 2. Caption cắt theo âm thanh, không cắt theo nghĩa

Vì phụ đề bám từng từ được đọc, phim dành hẳn một beat hình cho những từ không mang nội dung
nào. [Frame 173](extracted-frames/frame-173_12m56.47s.jpg) có caption **"in"**.
[Frame 324](extracted-frames/frame-324_23m57.20s.jpg) có caption **"of"**. Một giới từ trần
trụi được nâng lên thành một trạng thái hình ảnh.

Ngược lại, [frame 92](extracted-frames/frame-092_06m50.10s.jpg) đặt cả chữ
**"heidelbergensis"** vào một caption một-từ, không thẻ, không nhãn, không gợi ý phát âm, rồi
đi tiếp. Và [frame 225](extracted-frames/frame-225_16m12.33s.jpg) làm y vậy với
**"unconsciousness"**. Một danh từ trừu tượng năm âm tiết, một beat, hết.

Đây là hệ quả trực tiếp của việc để công cụ tạo phụ đề tự động quyết định nhịp chữ. TossExplains
đặt chữ theo ý, nên đừng nhập khẩu vấn đề này.

### 3. Quảng cáo gắn vào giữa mạch kể

[Frame 63](extracted-frames/frame-063_04m01.83s.jpg) ở 04:01.83 là một cảnh hiện đại đang kể
chuyện, và phim dán vào đó caption **"subscribe"** cộng **một nút subscribe đỏ của YouTube**
trượt vào từ mép phải. Nó nằm giữa một chương đang dựng luận điểm. Frame ngay sau nó,
[frame 64](extracted-frames/frame-064_04m06.23s.jpg), giữ 17,27 giây, tức phim vừa đòi một cú
click rồi bắt người xem chờ. TossExplains không nên trộn CTA vào một scene prompt.

### 4. Chất liệu không nhất quán trên cùng một chủ thể

Đã nêu ở cơ chế 10, và nó đáng nhắc lại ở đây vì đó là lỗi kiểm tra được, không phải ý kiến
thẩm mỹ: cùng chủ đề "côn trùng trong lớp lót giường" được vẽ **ảnh thật** ở
[frame 138](extracted-frames/frame-138_10m25.97s.jpg) và
[frame 171](extracted-frames/frame-171_12m53.80s.jpg), nhưng vẽ **doodle** ở
[frame 215](extracted-frames/frame-215_15m26.40s.jpg). Ba frame, hai chất liệu, một chủ đề.

### 5. Không thể sao chép phần render

Gần như toàn bộ vẻ đẹp của phim này bị `.agents/rules/visual-style.md` cấm:

- **Không có một frame nền trắng nào** trong 349 frame. TossExplains đòi **55 tới 75 phần trăm
  nền trắng phẳng**, và dự án 2 đã bị từ chối vì quá tối. Không lấy palette này.
- **Gradient và ánh sáng khí quyển** ở khắp nơi: tia nắng xuyên bão
  [frame 198](extracted-frames/frame-198_14m19.53s.jpg), lửa hắt lên mặt
  [frame 242](extracted-frames/frame-242_17m44.97s.jpg), ánh xanh điện thoại
  [frame 255](extracted-frames/frame-255_18m54.97s.jpg).
- **Texture**: giấy da [frame 11](extracted-frames/frame-011_00m34.63s.jpg), lông thú, đá, cỏ
  tranh, và **viền giấy vẽ trắng** lộ ra ở nhiều frame, ví dụ
  [frame 228](extracted-frames/frame-228_16m25.93s.jpg).
- **Đổ bóng và chiều sâu** trong mọi nội thất, ví dụ
  [frame 315](extracted-frames/frame-315_23m12.60s.jpg).
- **Nhòe chuyển động và zoom blur**: [frame 243](extracted-frames/frame-243_17m52.17s.jpg).
- **Chuyển đen trắng** làm nhấn: [frame 34](extracted-frames/frame-034_02m02.97s.jpg),
  [frame 143](extracted-frames/frame-143_10m47.97s.jpg),
  [frame 209](extracted-frames/frame-209_15m01.27s.jpg).
- **Line-art trắng trên nền tối**: [frame 218](extracted-frames/frame-218_15m40.80s.jpg).
- **Watermark nung vào mọi frame.** TossExplains không làm việc này.
- **Con ngươi vẽ thành khe cam** ở [frame 242](extracted-frames/frame-242_17m44.97s.jpg).
  Mắt TossExplains là dot eyes, luôn luôn.

## Cách áp dụng cho TossExplains

### Bốn chế độ, trong phạm vi style lock

Phim này chỉ có hai register và không dùng thẻ. TossExplains không sao chép được điều đó, nên
bản dịch là:

| Chế độ | Định nghĩa trong style lock | Nhiệm vụ |
| --- | --- | --- |
| `WHITE` | nền trắng phẳng, một tới bốn vật thể, chữ ALL CAPS ở đỉnh khung | thẻ khái niệm, số, diagram có nhãn |
| `SCENE` | nền trắng hoặc một khối màu từ tone map, có cast | công việc kể chuyện |
| `NARR` | một cast một mình trên nền trắng | dấu ngắt câu, câu hỏi trực tiếp |
| `SPLIT` | vạch chia đen dọc, trái tan `#C4965A` tổ tiên, phải trắng `@YOU` | gương ancient đối modern, xem cơ chế 2 |

Chú ý: phim này dùng **`SPLIT` đúng một lần** trong 26 phút
([frame 159](extracted-frames/frame-159_11m58.83s.jpg), nửa trái là hẻm núi ban ngày, nửa phải
là cùng hẻm núi ban đêm, nhân vật đứng đúng trên đường ghép). TossExplains có sẵn frame type
này và nên dùng nó nhiều hơn một lần, nhưng cách đặt nhân vật trên đường ghép thì đáng lấy.

### Mục tiêu nhịp: đừng lấy nhịp của phim này

**Đây là điểm quan trọng nhất của cả tài liệu.** 13,3 beat mỗi phút là nhịp của một phim kể
chuyện dài 26 phút có nhạc và có tiếng động. TossExplains là explainer 10 tới 14 phút, và hai
video đã được nghiên cứu trước chạy 30 tới 32 beat mỗi phút. **Không hạ nhịp TossExplains xuống
13.** Giữ mục tiêu **30 tới 34 beat mỗi phút**, tức 360 tới 410 timestamp cho một video 12 phút.

Những gì **nên** lấy từ bảng nhịp của phim này:

| Quy tắc | Bằng chứng |
| --- | --- |
| Giữ lâu hơn ở frame có nhiều thứ phải đọc | đoạn chậm nhất (10,8) là đoạn bằng chứng khảo cổ |
| Cho phép đúng một tới hai hold rất dài mỗi video, và dành chúng cho **vật thể**, không cho mặt | hold 27,10s và 21,37s đều không có mặt ai ở tiền cảnh |
| Biên độ nhịp giữa các chương không cần lớn | phim này chỉ dao động 10,8 tới 17,6 và vẫn giữ được người xem |

### Bảy kỹ thuật áp dụng được ngay, không phá style lock

1. **Nêu đáp án bằng hình ở giây thứ 10, rồi lấy nó đi.** Phim cho xem tấm da che mưa ở
   00:09.57, rồi bỏ nó suốt ba phút. TossExplains có thể làm đúng vậy: một timestamp sớm cho
   thấy trạng thái cuối, rồi cả video giải thích vì sao nó khó.
2. **Một hình, ba lần, cách nhau rất xa.** Tấm da xuất hiện ở 00:09, 03:39 và 25:38. Chọn một
   hành động, vẽ nó ba lần, và để lần thứ ba là gần cuối.
3. **Caption giữ nguyên khi hình lật ngược.** Cùng một dòng chữ ALL CAPS trên hai timestamp
   liên tiếp có nền và nội dung đối lập. Rẻ, và người xem tự nối.
4. **Ba lớp scale trên một chủ thể**: chân hoặc bàn tay, rồi macro chi tiết, rồi toàn cảnh
   hoàn thiện. Ba prompt, không cần texture.
5. **Cặp trước-sau trên đúng một bố cục.** Đổi một thứ duy nhất giữa hai timestamp: lửa lụi
   thành lửa cháy, giường sập thành giường lành, mái rò thành mái kín.
6. **Một beat nền trắng trống hoàn toàn giữa hai chương.** Đây là bản trong style lock của cú
   fade qua đen mà phim dùng 60 lần.
7. **Dành "you" cho ba tới bốn lần trong cả script.** Phim dùng nó ba lần và cả ba đều là cột
   mốc. Điều này không xung đột với quy tắc 2nd-person của `channel-dna.md`: giọng vẫn là "bạn"
   xuyên suốt, nhưng **chữ "YOU" hiện trên khung** thì chỉ ở các cột mốc.

### Ba quy tắc scene nên bổ sung

- **Kiến trúc và vật thể xứng đáng được giữ lâu.** Hai hold dài nhất của phim đều là nhà. Nếu
  một scene TossExplains là một vật thể mang cả ý (chiếc đồng hồ, cái giường, vòng lửa), cho nó
  nhiều giây hơn một frame có mặt người.
- **Chất liệu phải nhất quán trên cùng một chủ thể.** Nếu con bọ là doodle ở một timestamp, nó
  là doodle ở mọi timestamp. Đây là lỗi phim này mắc ba lần.
- **Không CTA trong scene prompt.** Nút subscribe thuộc về phần dựng, không thuộc về khung kể
  chuyện.

### Tỉ lệ đa dạng hình ảnh đề xuất

| Chế độ | Phim này | Đề xuất cho TossExplains |
| --- | ---: | ---: |
| `WHITE` (thẻ, diagram, số) | 0 phần trăm | 45 tới 55 phần trăm |
| `SCENE` (kể chuyện) | 85,8 phần trăm | 35 tới 45 phần trăm |
| `NARR` | 0 phần trăm | 6 tới 10 phần trăm |
| `SPLIT` | 0,3 phần trăm | 3 tới 6 phần trăm |

Đừng dịch cột giữa sang cột phải. Phim này chứng minh rằng **một register duy nhất cũng giữ
được người xem nếu thời tiết và ánh sáng thay đổi liên tục**, nhưng TossExplains không có
gradient hay ánh sáng để thay đổi, nên nó phải đổi **loại khung** thay vì đổi khí quyển. Giữ
nguyên ngân sách nền trong `visual-style.md`: trắng 55 tới 75 phần trăm, tan tới 15, cam tới
10, xanh cỏ cộng trời tới 10, cobalt 5 tới 15 và chỉ khi đang ở trong đầu ai đó.

## Checklist review cho mỗi video TossExplains tiếp theo

- [ ] Nhịp trung bình 30 tới 34 beat mỗi phút. **Không** hạ về 13 như phim này.
- [ ] Có một timestamp trong 15 giây đầu cho thấy trạng thái cuối cùng, rồi bỏ nó đi.
- [ ] Có một hành động hoặc vật thể xuất hiện đúng ba lần: mở, giữa, và gần cuối.
- [ ] Có ít nhất một cặp timestamp giữ nguyên caption trong khi hình lật sang mặt đối lập.
- [ ] Có ít nhất hai bộ ba-lớp-scale: chân hoặc tay, macro, toàn cảnh.
- [ ] Có ít nhất bốn cặp trước-sau trên đúng một bố cục, đổi duy nhất một thứ.
- [ ] Có một beat nền trắng trống hoàn toàn giữa các chương.
- [ ] Có một hoặc hai hold dài, và chúng dành cho vật thể, không cho mặt người.
- [ ] Chữ "YOU" chỉ hiện trên khung ở ba tới bốn cột mốc, không rắc đều.
- [ ] Diagram xuất hiện ít, và mỗi lần gánh cả một chương.
- [ ] Nền trắng phẳng đạt 55 tới 75 phần trăm. Cobalt không vượt 15 phần trăm.
- [ ] Chữ chỉ đen và đỏ, ALL CAPS, không chữ vàng trên nền sáng.
- [ ] Chất liệu nhất quán: một chủ thể được vẽ theo một phong cách ở mọi timestamp.
- [ ] Không nút subscribe, không CTA, không watermark trong bất kỳ scene prompt nào.
- [ ] Mắt luôn là dot eyes. Không con ngươi, không khe sáng.
- [ ] Không gradient, không đổ bóng, không texture, không blur, không đen trắng, không line-art.
- [ ] Soi từng frame đã render trước khi publish. Phim này lọt một khối đen 170x160 pixel.
- [ ] Bốn chuỗi verbatim trong `visual-style.md` khớp từng byte. Chạy `/check`.

## Thứ tự xem bộ frame

| Contact sheet | Frame | Timeline |
| --- | --- | --- |
| [01](contact-sheets/contact-sheet-01.jpg) | 001-024 | 00:00.00-01:26.40 |
| [02](contact-sheets/contact-sheet-02.jpg) | 025-048 | 01:27.10-02:57.33 |
| [03](contact-sheets/contact-sheet-03.jpg) | 049-072 | 03:03.90-04:50.27 |
| [04](contact-sheets/contact-sheet-04.jpg) | 073-096 | 04:59.87-07:08.23 |
| [05](contact-sheets/contact-sheet-05.jpg) | 097-120 | 07:29.60-08:57.80 |
| [06](contact-sheets/contact-sheet-06.jpg) | 121-144 | 09:00.77-10:51.17 |
| [07](contact-sheets/contact-sheet-07.jpg) | 145-168 | 10:53.53-12:41.23 |
| [08](contact-sheets/contact-sheet-08.jpg) | 169-192 | 12:45.23-13:58.27 |
| [09](contact-sheets/contact-sheet-09.jpg) | 193-216 | 13:59.10-15:28.20 |
| [10](contact-sheets/contact-sheet-10.jpg) | 217-240 | 15:33.77-17:37.57 |
| [11](contact-sheets/contact-sheet-11.jpg) | 241-264 | 17:43.30-19:50.47 |
| [12](contact-sheets/contact-sheet-12.jpg) | 265-288 | 19:53.37-21:06.50 |
| [13](contact-sheets/contact-sheet-13.jpg) | 289-312 | 21:10.67-23:05.67 |
| [14](contact-sheets/contact-sheet-14.jpg) | 313-336 | 23:07.53-25:02.07 |
| [15](contact-sheets/contact-sheet-15.jpg) | 337-349 | 25:12.27-26:13.97 |
