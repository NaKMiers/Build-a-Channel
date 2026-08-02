# Phân tích hình ảnh - What Every Human Tribe Did That You Still Do Under Stress

Kênh: TossExplains | Lượt xem: chưa có, video chưa được đăng | Link: chưa có, đây là bản xuất cục bộ của Project 5.

Xác minh nguồn: người dùng xác nhận thủ công đây là video của Project 5. Bản phân tích gắn với file `Rituals Under Stress.mp4`, SHA-256 `a444e4f5b4d5d1cd58dba1d8ac211fe6fe06532df8be4dddeda9b8904b853985`. Không có bước kiểm tra YouTube vì video chưa được tải lên.

## Kết quả extract

- Thời lượng: **13:52.51**.
- Độ phân giải: **1934 x 1080**.
- Tốc độ: **30 fps**.
- Ước tính số frame mã hóa: **24.975**.
- Phương pháp: scene detection ở threshold **0.02**, sau đó xem thủ công toàn bộ **19 review sheets** chứa **111 candidates**.
- Giữ lại: **109 frame** trong `extracted-frames/`.
- Contact sheet: **5 sheet** trong `contact-sheets/`.
- Chỉ mục: [`frame-index.csv`](frame-index.csv), chứa timestamp, giây, source video frame và tên file của từng frame.
- Dung lượng deliverable: khoảng **24 MB** cho extracted frames và **3 MB** cho contact sheets, chưa tính file MP4 cục bộ.
- Drop `c038` tại **04:35.13**, diff **1.86**: một hold gần như trùng hoàn toàn với candidate trước, không thêm thông tin.
- Drop `c111` tại **13:49.37**, diff **7.78**: midpoint của transition, hình cây bút phóng lớn đè lên Toss đang blur.

## Kết luận quan trọng nhất

Video có một cơ chế hình ảnh rất rõ: biến ritual thành một **ngưỡng hành động có biên**, rồi dùng cây bút, đường đi, cánh cửa và chiếc thuyền để chứng minh rằng ritual giữ người thực hiện ổn định chứ không kiểm soát kết quả. Cơ chế đó nhất quán và có payoff, nhưng bản dựng hiện tại giữ plate quá lâu, nên sự rõ nghĩa chưa chuyển thành mật độ chú ý đủ mạnh.

Hook bắt đầu bằng hành động nhỏ có thể nhìn thấy, tay chỉnh lại cây bút vốn đã thẳng ở [frame 2](extracted-frames/frame-002_00m02.10s.jpg), rồi mở ngay sang mê cung của các kết quả bất định ở [frame 4](extracted-frames/frame-004_00m19.87s.jpg). Đến cuối, cánh cửa trở thành ranh giới giữa chuẩn bị và tham gia ở [frame 92](extracted-frames/frame-092_11m51.47s.jpg), còn chiếc thuyền thực sự đi vào biển ở [frame 106](extracted-frames/frame-106_13m26.10s.jpg). Đây là một causal visual chain hoàn chỉnh.

Điểm yếu nằm ở nhịp. Video chỉ có **7.9 trạng thái hình ảnh mới mỗi phút**, khoảng **7.66 giây giữa hai beat**, và **85 trong 108** khoảng cách dài ít nhất 4 giây. Một số plate đủ giàu để chịu hold dài, như chuỗi overload tăng dần từ [frame 82](extracted-frames/frame-082_10m40.17s.jpg) đến [frame 86](extracted-frames/frame-086_11m05.87s.jpg), nhưng những card đơn giản như ba vòng tròn xã hội ở [frame 61](extracted-frames/frame-061_07m47.50s.jpg) không đủ thông tin mới cho hold **21.83 giây**.

## Nhịp hình ảnh

| Chỉ số | Kết quả |
| --- | ---: |
| Tổng beat giữ lại | 109 |
| Beat mỗi phút | 7.9 |
| Khoảng cách trung bình giữa beat | 7.66 giây |
| Duration / beats | 7.64 giây |
| Khoảng cách trung vị | 7.20 giây |
| Khoảng cách không quá 1 giây | 0 |
| Khoảng cách không quá 2 giây | 2 / 108 |
| Khoảng cách ít nhất 4 giây | 85 / 108 |
| Beat trong 15 giây đầu | 3 |
| Hook 0-45 giây | 6 beat, 8.0 beat/phút, 7.94 giây/beat |

| Đoạn | Frame | Beat mỗi phút | Giây mỗi beat |
| --- | --- | ---: | ---: |
| Hook | 001-010 | 7.6 | 7.90 |
| Psychology | 011-018 | 9.8 | 6.12 |
| Lang experiment | 019-027 | 8.9 | 6.74 |
| Hobson experiment | 028-040 | 7.7 | 7.78 |
| Anthropology | 041-058 | 7.5 | 7.97 |
| Social ritual | 059-070 | 6.3 | 9.59 |
| Double edge | 071-075 | 6.0 | 10.05 |
| Unbounded loop | 076-081 | 8.8 | 6.83 |
| Modern mismatch | 082-087 | 10.3 | 5.85 |
| Shift | 088-098 | 8.4 | 7.13 |
| Synthesis | 099-106 | 8.0 | 7.46 |
| Ending | 107-109 | 6.4 | 9.43 |

Nhịp nhanh nhất nằm ở `Modern mismatch`, nơi plate bị lấp đầy dần bởi thông báo, giấy tờ, bánh răng và cửa sổ phần mềm từ [frame 82](extracted-frames/frame-082_10m40.17s.jpg) đến [frame 86](extracted-frames/frame-086_11m05.87s.jpg). Việc tăng tốc hợp với ý nghĩa: thế giới số không có ngưỡng kết thúc tự nhiên.

Nhịp chậm nhất nằm ở `Double edge`, nhưng [frame 71](extracted-frames/frame-071_09m09.47s.jpg) chỉ là một balance card và bị giữ **19.47 giây**. `Social ritual` cũng giữ [frame 61](extracted-frames/frame-061_07m47.50s.jpg) trong **21.83 giây**, dài nhất video. Đây không phải slow beat để khán giả đọc dữ liệu dày. Đây là plate tương đối đơn giản bị kéo dài hơn lượng thông tin nó chứa.

Năm hold dài nhất là **21.83 giây** trên [frame 61](extracted-frames/frame-061_07m47.50s.jpg), **21.50 giây** trên [frame 102](extracted-frames/frame-102_12m52.00s.jpg), **19.47 giây** trên [frame 71](extracted-frames/frame-071_09m09.47s.jpg), **18.93 giây** trên [frame 59](extracted-frames/frame-059_07m16.77s.jpg), và **18.20 giây** trên [frame 18](extracted-frames/frame-018_01m57.07s.jpg). Ba trong năm frame này là card hoặc hybrid diagram, nên vấn đề không phải thiếu chi tiết vẽ mà là thiếu delta đúng lúc.

## Bảy cơ chế hình ảnh làm video rõ nghĩa

### 1. Hook mở bằng hành động, không mở bằng định nghĩa

Frame đầu tiên đặt người xem vào POV bàn làm việc với hai tay đang căng ở [frame 1](extracted-frames/frame-001_00m00.00s.jpg). Tay phải chỉnh cây bút ở [frame 2](extracted-frames/frame-002_00m02.10s.jpg), Toss quay lại với vệt chuyển động lặp ở [frame 3](extracted-frames/frame-003_00m11.43s.jpg), rồi bất định hiện thành các nhánh sau màn hình ở [frame 4](extracted-frames/frame-004_00m19.87s.jpg). Câu hỏi được enact trước khi chữ `WHY ORDER?` xuất hiện ở [frame 10](extracted-frames/frame-010_01m11.13s.jpg).

### 2. Plate giữ nguyên, một biến đổi làm thay đổi nghĩa

Video dùng progressive build đúng ở nhiều nơi. Một con đường bình thường bị chặn ở [frame 12](extracted-frames/frame-012_01m22.67s.jpg), chuyển đỏ và phân nhánh ở [frame 13](extracted-frames/frame-013_01m27.30s.jpg), rồi trở thành một hệ rễ cứng nhắc ở [frame 15](extracted-frames/frame-015_01m37.97s.jpg). Trong thí nghiệm, một chuyển động lau đơn giản ở [frame 21](extracted-frames/frame-021_02m33.83s.jpg) tích lũy thành vòng lặp ở [frame 22](extracted-frames/frame-022_02m40.27s.jpg) và [frame 23](extracted-frames/frame-023_02m44.10s.jpg). Mỗi delta mang ý nghĩa, không chỉ tạo chuyển động.

### 3. Bốn register thay nhau theo vai trò của lập luận

Trong 109 frame, `STORY` chiếm **61 frame, 56.0%**, `HYBRID` chiếm **24 frame, 22.0%**, `DIRECT` chiếm **13 frame, 11.9%**, và `CARD` chiếm **11 frame, 10.1%**. Có **43 lần đổi register**, trung bình **2.48 beat cho mỗi run**.

Sự chuyển đổi có chức năng. Câu chuyện đi biển dùng `STORY` ở [frame 43](extracted-frames/frame-043_05m10.67s.jpg), risk gradient chuyển thành `HYBRID` ở [frame 48](extracted-frames/frame-048_05m46.90s.jpg), và kết luận `NOT A REPLACEMENT` được cô lại thành `CARD` ở [frame 49](extracted-frames/frame-049_05m54.73s.jpg). Register đổi khi vai trò của lập luận đổi.

### 4. Motif trở lại với nghĩa mới

Cây bút bắt đầu như một vật bị chỉnh lại vô ích ở [frame 2](extracted-frames/frame-002_00m02.10s.jpg), trở lại như hành vi cơ thể lặp trước bất định ở [frame 27](extracted-frames/frame-027_03m09.17s.jpg), rồi xuất hiện sau khi sequence kết thúc ở [frame 75](extracted-frames/frame-075_09m49.67s.jpg). Cánh cửa bắt đầu là lối thoát khỏi mê cung ở [frame 37](extracted-frames/frame-037_04m29.70s.jpg), trở thành `DOORWAY INTO WORK` ở [frame 40](extracted-frames/frame-040_04m50.10s.jpg), và cuối cùng là ngưỡng tham gia ở [frame 92](extracted-frames/frame-092_11m51.47s.jpg).

Chiếc thuyền cũng đổi nghĩa. Ban đầu nó là nơi kỹ năng thực tế và ritual cùng tồn tại ở [frame 50](extracted-frames/frame-050_05m58.37s.jpg). Đến cuối, thuyền hoàn thành ở [frame 101](extracted-frames/frame-101_12m43.93s.jpg) rồi thực sự xuống nước ở [frame 106](extracted-frames/frame-106_13m26.10s.jpg). Motif không chỉ lặp, nó chứng minh một giai đoạn mới của causal chain.

### 5. Nghiên cứu có visual receipt thay vì chỉ có scientist stock image

Martin Lang được gắn vào setup thí nghiệm ở [frame 19](extracted-frames/frame-019_02m15.27s.jpg), protocol `3 MIN PREP | 5 MIN SPEECH` được đặt vào chính phòng lab ở [frame 20](extracted-frames/frame-020_02m25.10s.jpg), và kết quả được nén thành so sánh `SMALLER ERROR REACTION` ở [frame 35](extracted-frames/frame-035_04m09.93s.jpg). Malinowski và `TROBRIAND ISLANDS` nằm trên bản đồ và collage thực địa ở [frame 42](extracted-frames/frame-042_05m00.63s.jpg). Dimitris Xygalatas mở một chuỗi hành vi nhóm ở [frame 59](extracted-frames/frame-059_07m16.77s.jpg). Đây là receipt có liên hệ với cơ chế đang kể.

### 6. Text nén ý, không chép lại narration

Các cụm chữ tốt nhất có thể chuyển thẳng thành logic scene prompt: `RISK UP | RITUAL UP` ở [frame 48](extracted-frames/frame-048_05m46.90s.jpg), `CONTROL COMPLETE | ENTER UNCERTAINTY` ở [frame 58](extracted-frames/frame-058_07m07.93s.jpg), `ACTION BEFORE CERTAINTY` ở [frame 70](extracted-frames/frame-070_09m02.27s.jpg), và `CONTAIN, THEN OPEN` ở [frame 104](extracted-frames/frame-104_13m16.90s.jpg). Mỗi cụm đặt tên cho quan hệ nhân quả hoặc điểm đảo nghĩa.

### 7. Tốc độ tăng theo áp lực của thế giới hiện đại

Phần modern mismatch bắt đầu với nhiều nguồn việc nhưng Toss vẫn ngồi giữa bố cục đọc được ở [frame 82](extracted-frames/frame-082_10m40.17s.jpg). Hệ thống tăng thêm bánh răng, deadline và cảnh báo ở [frame 83](extracted-frames/frame-083_10m50.33s.jpg), sau đó biến thành ba dòng vật thể khổng lồ ở [frame 84](extracted-frames/frame-084_10m53.50s.jpg) và giao diện lỗi chồng lên nhau ở [frame 86](extracted-frames/frame-086_11m05.87s.jpg). Đây là đoạn nhanh nhất video vì hình ảnh tự tăng entropy cùng luận điểm.

## Phân tích từng chương

| Chương | Thời gian | Frame | Hình ảnh làm gì | Tác dụng |
| --- | --- | --- | --- | --- |
| Hook | 0:00.000-1:11.140 | 001-010 | Từ cây bút ở [frame 2](extracted-frames/frame-002_00m02.10s.jpg) mở sang nhánh bất định ở [frame 4](extracted-frames/frame-004_00m19.87s.jpg), rồi đặt câu hỏi ở [frame 10](extracted-frames/frame-010_01m11.13s.jpg). | Enact điều bí ẩn trước khi gọi tên ritual. |
| Psychology | 1:11.140-2:15.300 | 011-018 | Đường đi phân nhánh, bị chặn, chuyển đỏ rồi co thành sequence ở [frame 15](extracted-frames/frame-015_01m37.97s.jpg) và [frame 18](extracted-frames/frame-018_01m57.07s.jpg). | Biến stress và ritualization thành hình học dễ hiểu. |
| Lang experiment | 2:15.300-3:16.640 | 019-027 | Lab, động tác lau, trace lặp và cây bút trở lại từ [frame 19](extracted-frames/frame-019_02m15.27s.jpg) đến [frame 27](extracted-frames/frame-027_03m09.17s.jpg). | Cho claim một apparatus và một hành vi đo được. |
| Hobson experiment | 3:16.640-4:52.329 | 028-040 | Từ storm trigger ở [frame 28](extracted-frames/frame-028_03m16.70s.jpg) sang EEG payoff ở [frame 35](extracted-frames/frame-035_04m09.93s.jpg), rồi tới doorway ở [frame 40](extracted-frames/frame-040_04m50.10s.jpg). | Chuyển từ hiệu ứng cơ thể sang ngưỡng bắt đầu hành động. |
| Anthropology | 4:52.329-7:16.769 | 041-058 | Malinowski, canoe prep, open sea và ranh giới control ở [frame 42](extracted-frames/frame-042_05m00.63s.jpg), [frame 50](extracted-frames/frame-050_05m58.37s.jpg), [frame 55](extracted-frames/frame-055_06m43.13s.jpg) và [frame 58](extracted-frames/frame-058_07m07.93s.jpg). | Chứng minh ritual song hành với kỹ năng, không thay kỹ năng. |
| Social ritual | 7:16.769-9:09.389 | 059-070 | Nghiên cứu nhóm, football memory và crew phối hợp ở [frame 59](extracted-frames/frame-059_07m16.77s.jpg), [frame 62](extracted-frames/frame-062_08m09.33s.jpg) và [frame 66](extracted-frames/frame-066_08m29.17s.jpg). | Mở cơ chế từ tự điều chỉnh sang khả năng dự đoán lẫn nhau. |
| Double edge | 9:09.389-9:53.916 | 071-075 | Balance card ở [frame 71](extracted-frames/frame-071_09m09.47s.jpg) chuyển sang sequence có điểm kết thúc ở [frame 75](extracted-frames/frame-075_09m49.67s.jpg). | Đặt guardrail: ritual hữu ích phải có biên. |
| Unbounded loop | 9:53.916-10:28.336 | 076-081 | Vòng lặp đỏ mở rộng ở [frame 77](extracted-frames/frame-077_09m56.93s.jpg), nhận lối thoát xanh ở [frame 78](extracted-frames/frame-078_10m01.53s.jpg), rồi so sánh threshold với circling ở [frame 80](extracted-frames/frame-080_10m20.00s.jpg). | Phân biệt kết thúc chuẩn bị với truy tìm certainty vô tận. |
| Modern mismatch | 10:28.336-11:15.416 | 082-087 | Plate công việc số bị lấp đầy từng lớp ở [frame 82](extracted-frames/frame-082_10m40.17s.jpg), [frame 84](extracted-frames/frame-084_10m53.50s.jpg) và [frame 86](extracted-frames/frame-086_11m05.87s.jpg). | Cho thấy vì sao công việc số không cung cấp physical threshold. |
| Shift | 11:15.416-12:33.756 | 088-098 | Cổng `FIXED FINAL ACTION` ở [frame 88](extracted-frames/frame-088_11m15.43s.jpg), threshold claim ở [frame 91](extracted-frames/frame-091_11m41.70s.jpg), rồi đường thẳng thắng mê cung ở [frame 98](extracted-frames/frame-098_12m26.70s.jpg). | Biến lời khuyên thành một thay đổi có thể nhìn thấy. |
| Synthesis | 12:33.756-13:28.596 | 099-106 | `SKILL FIRST` ở [frame 99](extracted-frames/frame-099_12m33.90s.jpg), thuyền hoàn thành ở [frame 101](extracted-frames/frame-101_12m43.93s.jpg), và `CONTAIN, THEN OPEN` ở [frame 104](extracted-frames/frame-104_13m16.90s.jpg). | Ghép kỹ năng, ritual và hành động thành một nguyên tắc duy nhất. |
| Ending | 13:28.596-13:52.522 | 107-109 | Cây bút trở lại ở [frame 107](extracted-frames/frame-107_13m28.57s.jpg), được dùng ở [frame 108](extracted-frames/frame-108_13m40.07s.jpg), rồi Toss trực diện xuất hiện ở [frame 109](extracted-frames/frame-109_13m47.43s.jpg). | Đóng vòng với vật thể mở đầu, nhưng outro bị lỗi continuity. |

## Vì sao phần kết hiệu quả

Phần synthesis trả lời đúng câu hỏi lớn bằng hành động. `SKILL FIRST` ở [frame 99](extracted-frames/frame-099_12m33.90s.jpg) ngăn ritual trở thành thay thế cho năng lực. Chiếc thuyền được hoàn thành trước khi nhân vật bước qua cổng `SKILL + RITUAL` ở [frame 101](extracted-frames/frame-101_12m43.93s.jpg). Chuỗi vật thể rời rạc được gom thành `CONTAIN, THEN OPEN` ở [frame 104](extracted-frames/frame-104_13m16.90s.jpg), và cuối cùng chiếc thuyền xuống biển thật ở [frame 106](extracted-frames/frame-106_13m26.10s.jpg). Payoff là participation, không phải certainty.

Việc quay lại bàn làm việc lúc hoàng hôn ở [frame 107](extracted-frames/frame-107_13m28.57s.jpg) cũng đúng về cấu trúc. Cây bút không còn được chỉnh để kiểm soát tương lai. Nó được cầm để làm việc ở [frame 108](extracted-frames/frame-108_13m40.07s.jpg). Nghĩa của motif đã đảo hoàn toàn.

Tuy nhiên, ending chỉ có **3 frame giữ lại** trong khoảng 24 giây và chậm xuống **6.4 beat/phút**. Frame cuối còn đột ngột thêm kính cho Toss ở [frame 109](extracted-frames/frame-109_13m47.43s.jpg), khiến closing image giống một nhân vật khác hơn là trạng thái cuối của cùng một người.

## Những điểm không nên sao chép

### 1. Không giữ một card đơn giản quá lâu chỉ vì narration còn tiếp tục

[Frame 61](extracted-frames/frame-061_07m47.50s.jpg) giữ ba bubble xã hội trong **21.83 giây**. [Frame 71](extracted-frames/frame-071_09m09.47s.jpg) giữ balance card trong **19.47 giây**. Cả hai có bố cục sạch, nhưng không có đủ progressive build để tái khởi động sự chú ý trong khoảng hold đó.

### 2. Không để continuity của mascot vỡ ở payoff cuối

Đây là lỗi có thể kiểm tra trực tiếp trong frame. Ở [frame 108](extracted-frames/frame-108_13m40.07s.jpg), Toss không đeo kính và đang cầm một cây bút trong khi một cây bút xanh thứ hai nằm trên bàn. Sang [frame 109](extracted-frames/frame-109_13m47.43s.jpg), Toss đột ngột đeo kính. Hai cây bút phá object continuity của recurring anchor, còn kính phá character continuity đúng lúc người xem cần nhận ra opening plate.

### 3. Không để visual receipt dừng ở tên nhà nghiên cứu và một kết luận chung

[Frame 20](extracted-frames/frame-020_02m25.10s.jpg) cho protocol `3 MIN PREP | 5 MIN SPEECH`, nhưng không giữ sample size hoặc citation đủ lâu trong bộ state đã extract. [Frame 35](extracted-frames/frame-035_04m09.93s.jpg) nói `SMALLER ERROR REACTION`, nhưng không hiển thị effect size, năm, hoặc tên paper. [Frame 59](extracted-frames/frame-059_07m16.77s.jpg) có tên Dimitris Xygalatas, nhưng chuỗi sau đó không có date hoặc sample receipt. Video có researcher identity, nhưng bằng chứng trên màn hình chưa đủ để người xem tự kiểm tra claim.

### 4. Không biến sự quá tải thành một plate không còn focal point

Build từ [frame 82](extracted-frames/frame-082_10m40.17s.jpg) tới [frame 84](extracted-frames/frame-084_10m53.50s.jpg) vẫn đọc được vì Toss nằm ở tâm của ba dòng áp lực. Đến [frame 86](extracted-frames/frame-086_11m05.87s.jpg), nhiều UI window, giấy, gear, máy tính và weather icon cạnh tranh ngang nhau. Ý nghĩa là overload, nhưng focal hierarchy cũng bị overload theo.

### 5. Không kết bằng một transition chưa settle

Candidate cuối tại 13:49.37 là giant pen đè lên Toss bị blur và đã phải drop. Transition này xuất hiện sau [frame 109](extracted-frames/frame-109_13m47.43s.jpg), nên outro không có một closing composition sạch để giữ đến hết timeline.

## Cơ chế và câu hỏi cần tranh luận

### Cơ chế có bằng chứng để cân nhắc chuyển giao

1. **Motif đổi nghĩa qua từng chương.** Cây bút ở [frame 2](extracted-frames/frame-002_00m02.10s.jpg), [frame 27](extracted-frames/frame-027_03m09.17s.jpg) và [frame 108](extracted-frames/frame-108_13m40.07s.jpg) tạo một vòng nhân quả rõ hơn việc lặp một mascot pose.
2. **Một base plate, một delta có nghĩa.** Chuỗi đường đỏ ở [frame 12](extracted-frames/frame-012_01m22.67s.jpg), [frame 13](extracted-frames/frame-013_01m27.30s.jpg) và [frame 15](extracted-frames/frame-015_01m37.97s.jpg) giải thích cơ chế bằng thay đổi, không bằng vật thể ngẫu nhiên.
3. **Đổi register theo vai trò lập luận.** STORY ở [frame 43](extracted-frames/frame-043_05m10.67s.jpg), HYBRID ở [frame 48](extracted-frames/frame-048_05m46.90s.jpg), rồi CARD ở [frame 49](extracted-frames/frame-049_05m54.73s.jpg) tạo nhịp nhận thức hợp lý.
4. **Text đặt tên cho quan hệ, không chép lời.** `CONTROL COMPLETE | ENTER UNCERTAINTY` ở [frame 58](extracted-frames/frame-058_07m07.93s.jpg) và `THRESHOLD, NOT OUTCOME` ở [frame 91](extracted-frames/frame-091_11m41.70s.jpg) là semantic compression tốt.
5. **Ending trả motif về hành động.** Chiếc thuyền xuống biển ở [frame 106](extracted-frames/frame-106_13m26.10s.jpg) và cây bút được dùng ở [frame 108](extracted-frames/frame-108_13m40.07s.jpg) biến payoff thành hành vi thay vì affirmation.

### Câu hỏi mở cho chủ kênh

1. Có nên thêm editor delta giữa các generated plate để đưa nhịp từ **7.9 beat/phút** lên một vùng thử nghiệm cao hơn, đặc biệt tại năm hold dài nhất, mà không tăng số ảnh AI?
2. `Social ritual` có cần một build riêng cho `MEMORY`, `IDENTITY`, và `EXPECTATION` thay vì giữ một plate đơn như [frame 61](extracted-frames/frame-061_07m47.50s.jpg) quá 21 giây không?
3. Phần `Modern mismatch` ở [frame 82](extracted-frames/frame-082_10m40.17s.jpg) đến [frame 86](extracted-frames/frame-086_11m05.87s.jpg) cho thấy tốc độ cao hơn hợp với entropy. Có nên áp dụng nhịp tăng dần này sớm hơn từ `Unbounded loop` không?
4. Có nên thay [frame 109](extracted-frames/frame-109_13m47.43s.jpg) bằng một clean hold của [frame 108](extracted-frames/frame-108_13m40.07s.jpg), sau khi sửa còn đúng một cây bút, để closing echo không bị kính và transition làm đứt continuity?
5. Các research receipt như [frame 35](extracted-frames/frame-035_04m09.93s.jpg) nên thêm sample size, năm, hay tên paper ở mức nào để tăng khả năng kiểm chứng mà không biến video thành slide học thuật?

## Thứ tự xem bộ frame

| Contact sheet | Frame | Timeline |
| --- | --- | --- |
| [01](contact-sheets/contact-sheet-01.jpg) | 001-024 | 00:00.00-02:47.17 |
| [02](contact-sheets/contact-sheet-02.jpg) | 025-048 | 02:55.63-05:46.90 |
| [03](contact-sheets/contact-sheet-03.jpg) | 049-072 | 05:54.73-09:28.93 |
| [04](contact-sheets/contact-sheet-04.jpg) | 073-096 | 09:40.17-12:14.07 |
| [05](contact-sheets/contact-sheet-05.jpg) | 097-109 | 12:18.43-13:47.43 |
