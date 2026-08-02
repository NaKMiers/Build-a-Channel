# Tổng hợp chiến lược video-swipe cho TossExplains

Nguồn chính:

1. [`the-rarest-human-possible/visual-analysis.md`](the-rarest-human-possible/visual-analysis.md)
2. [`the-rarest-human-possible/SYNTHETIC.md`](the-rarest-human-possible/SYNTHETIC.md)
3. [`what-did-ancient-humans-do-when-it-rained-all-week/visual-analysis.md`](what-did-ancient-humans-do-when-it-rained-all-week/visual-analysis.md)
4. [`what-did-ancient-humans-do-when-it-rained-all-week/SYNTHETIC.md`](what-did-ancient-humans-do-when-it-rained-all-week/SYNTHETIC.md)
5. [`how-did-ancient-humans-sleep-through-endless-rain/SYNTHETIC.md`](how-did-ancient-humans-sleep-through-endless-rain/SYNTHETIC.md), chỉ dùng làm đối chứng thất bại.

Snapshot hiệu suất do chủ kênh cung cấp:

| Ưu tiên | Video | Kênh | Hiệu suất tại thời điểm ghi nhận | Vai trò trong tổng hợp |
| ---: | --- | --- | --- | --- |
| 1 | `The Rarest Human Possible` | Past Tense | Khoảng 1 triệu view sau 19 ngày | Mẫu vận hành chính cần học chuyên sâu |
| 2 | `What Did Ancient Humans Do When It Rained All Week?` | Ink Explainer | Khoảng 1 triệu view sau 28 ngày | Nguồn bổ sung những cơ chế Past Tense còn thiếu |
| 3 | `How Did Ancient Humans Sleep Through Endless Rain?` | Before Civilization | Khoảng 45 nghìn view sau 8 ngày | Đối chứng âm, chỉ xem điều cần tránh |

Trạng thái: **ĐÃ ĐƯỢC CHỦ KÊNH DUYỆT NGÀY 2026-08-02 VÀ ĐÃ TRIỂN KHAI VÀO HỆ THỐNG**.

Tài liệu này là hồ sơ quyết định và nguồn đối chiếu chiến lược. Các quyết định đã được chuyển thành rule, skill và validator canonical. Artifact của project sản xuất không được tự động viết lại hoặc tự động tái duyệt.

## Cách đọc bằng chứng hiệu suất

Video 2 và video 3 đều là tín hiệu thành công mạnh, vì cùng đạt khoảng 1 triệu view trong chưa đầy một tháng. Chúng xứng đáng được ưu tiên hơn video 1.

Tuy nhiên, view count chỉ cho biết **gói hoàn chỉnh đã hoạt động**, không chứng minh riêng progressive disclosure, màu nền, hook hay nhịp là nguyên nhân duy nhất. Chủ đề, title, thumbnail, lịch sử kênh và nguồn traffic cũng có thể ảnh hưởng. Vì vậy bản tổng hợp này sao chép hệ thống đã quan sát được như một giả thuyết có xác suất cao, rồi yêu cầu kiểm tra bằng video TossExplains thực tế.

Video 1 không được dùng để tạo quy tắc tích cực. Hiệu suất thấp hơn khiến nó chỉ phù hợp để nhận diện những lựa chọn có thể làm video chậm, thiếu nhất quán hoặc khó bản địa hóa.

## Kết luận quan trọng nhất

TossExplains nên lấy **hệ điều hành thị giác của Past Tense** làm xương sống, giữ chủ đề, mascot và lời hứa nội dung của TossExplains, rồi bổ sung **hệ register, visual receipt và convergent ending của Ink Explainer**.

Câu định nghĩa ngắn nhất:

> **Một video TossExplains phải diễn ra như một câu chuyện nhìn thấy được, trong đó mỗi luận điểm quan trọng tạo ra một visual proof, mỗi base plate tiến triển bằng delta có ý nghĩa, và toàn bộ video hội tụ về một payoff đã được gieo từ đầu.**

Đích đến không phải là thêm thật nhiều hậu cảnh hay thay ảnh liên tục. Đích đến là sao chép cách Past Tense điều tiết sự chú ý:

- Khi cần cảm xúc, cho người xem sống trong một scene.
- Khi cần hiểu, rút scene thành diagram hoặc card.
- Khi cần quy mô, biến con số thành một trải nghiệm nhìn thấy được.
- Khi cần giữ continuity, giữ base plate và thay đúng một biến.
- Khi cần nối chương, quay lại một recurring anchor đã thay đổi.
- Khi cần kết, gom các bằng chứng cũ thành một ý nghĩa mới.

## Lập trường về mục tiêu "COPY 100%"

Tôi đồng ý với mục tiêu học chuyên sâu và tái tạo sát hệ thống làm video của Past Tense. Tôi không đồng ý rằng chỉ cần đổi topic thì mọi thứ sao chép tự động trở thành tài sản nguyên bản của TossExplains.

Trong tài liệu này, "COPY 100%" được định nghĩa như sau:

> **Sao chép 100% logic có thể chuyển giao, sao chép 0% asset và bố cục nhận diện cụ thể.**

Được sao chép:

- Cách mở hook.
- Cách chia visual beat.
- Cách điều tiết mật độ.
- Cách dùng progressive disclosure.
- Cách luân phiên scene, portrait, diagram, infographic và scale metaphor.
- Cách dùng base plate, delta, crop, reveal, return và payoff.
- Cách mở curiosity loop theo quan hệ nhân quả.
- Cách xây recurring visual anchor.
- Cách tăng tốc hoặc giảm tốc theo nhiệm vụ của đoạn.
- Cách dùng màu, khoảng trống và cỡ cảnh để dẫn mắt.

Không được sao chép:

- Nhân vật, mascot hoặc thiết kế nhận diện của Past Tense.
- Một frame cụ thể, cách đặt nhân vật và đạo cụ giống đến mức truy nguyên được.
- Chuỗi shot đặc trưng của `The Rarest Human Possible` chỉ đổi tên chủ thể.
- Bảng màu được bê nguyên như một mã nhận diện.
- Text, icon, phép ẩn dụ, câu kết hoặc câu chuyện công viên của video mẫu.
- Sai số khoa học, cách tính xác suất và affirmation chung chung ở phần kết.

Ranh giới này không làm mức học hỏi yếu đi. Nó buộc TossExplains tái tạo **năng lực đạo diễn**, thay vì chỉ mô phỏng bề mặt.

## Phần phải học gần như toàn bộ từ video 2

### 1. Hook phải được diễn ra trước khi được giải thích

Video dùng 29 visual beat trong khoảng 47 giây để dẫn người xem qua công viên, chi tiết nhân vật, mối quan hệ, giấc mơ và cú lật trước khi nêu câu hỏi chính. Chuỗi bắt đầu ở [frame 001](the-rarest-human-possible/extracted-frames/frame-001_00m00.00s.jpg) và chỉ hoàn thành reframe ở [frame 029](the-rarest-human-possible/extracted-frames/frame-029_00m44.20s.jpg).

TossExplains nên sao chép cấu trúc:

`một tình huống cụ thể -> chi tiết lạ xuất hiện -> stake hoặc mâu thuẫn tăng -> cú lật -> câu hỏi trung tâm`.

Hook không được mở bằng lời giới thiệu chủ đề, danh sách nội dung hoặc định nghĩa. Với TossExplains, tình huống hiện đại mà người xem từng trải qua vẫn là lựa chọn mặc định. Cảnh thí nghiệm hoặc tổ tiên chỉ mở video khi nó kết nối ngay với đời sống bên trong của người xem.

### 2. Đơn vị hình ảnh là thay đổi ý nghĩa

Past Tense khiến gần như mọi luận điểm quan trọng tạo ra một hệ quả nhìn thấy được. Tay trái được thể hiện bằng hành động, melanin được nối với da, tóc và mắt, còn xác suất cực nhỏ được đổi thành sao, cát và số lượng Trái Đất.

TossExplains không nên hiểu điều này thành "mỗi câu một ảnh" hoặc "mỗi danh từ một icon". Quy tắc đúng là:

> Khi narration thêm một hành động, nguyên nhân, trạng thái, bằng chứng, quy mô hoặc cách hiểu mới, hình ảnh phải phản hồi bằng một visual proof.

### 3. Controlled density là nền tảng của chất lượng

Cảnh công viên cần cây, đường đi, ghế và chiều sâu vì địa điểm đang tạo cảm xúc. Phép tính cần nền sạch vì chỉ có quan hệ con số là quan trọng. Portrait cần ít vật thể vì biểu cảm là trung tâm.

TossExplains không được thay "mọi scene nền trắng" bằng "mọi scene nhiều hậu cảnh". Hệ thống mới phải biết chủ động tăng và giảm mật độ.

Mỗi chi tiết chỉ được giữ khi nó làm ít nhất một việc:

- Xác định không gian.
- Làm rõ hành động hoặc quan hệ.
- Dẫn mắt.
- Tăng cảm xúc hoặc không khí.
- Làm bằng chứng đáng tin hơn.
- Tạo continuity hoặc recurring motif.

### 4. Mỗi frame có một câu hỏi thị giác chính

Một frame có thể dày đặc nhưng vẫn phải trả lời được:

1. Mắt nhìn vào đâu trước?
2. Mắt đi đâu tiếp theo?
3. Người xem phải nhận ra điều gì?

[Frame 175](the-rarest-human-possible/extracted-frames/frame-175_05m55.80s.jpg) chứa rất nhiều biểu tượng nhưng vẫn chỉ có một luận điểm chính: còn vô số biến chưa được tính. Đây là ví dụ tốt hơn quy tắc cứng "mỗi frame chỉ có một vật thể".

### 5. Progressive disclosure phải trở thành thói quen mặc định

Chuỗi [frame 030](the-rarest-human-possible/extracted-frames/frame-030_00m47.50s.jpg) đến [frame 037](the-rarest-human-possible/extracted-frames/frame-037_00m49.67s.jpg) thêm từng đặc điểm vào cùng một bố cục. Người xem vừa hiểu từng phần, vừa chờ phần tiếp theo.

Các cấu trúc nên dùng:

- `Build-first`: A -> A+B -> A+B+C.
- `Overview-first`: toàn bộ -> cận A -> cận B -> cận C.
- `Parallel to synthesis`: A -> B -> C -> frame gộp.
- `State update`: cùng scoreboard -> thêm biến -> cập nhật kết quả.

Số phần tử đi theo nội dung, không bắt buộc là ba.

### 6. Base plate cộng delta là đơn vị sản xuất chủ đạo

Một base plate tốt phải tạo được nhiều visual reward mà không cần generate lại toàn bộ thế giới.

Delta hợp lệ gồm:

- Thêm hoặc bớt một nhân vật hay vật thể có ý nghĩa.
- Đổi số lượng.
- Đổi trạng thái cảm xúc.
- Cho thấy nguyên nhân hoặc hệ quả mới.
- Cập nhật một con số hoặc scoreboard.
- Thêm nhãn, mũi tên hoặc highlight.
- Reframe để chuyển điểm nhìn sang một chi tiết đã có.
- Quay lại plate cũ với ý nghĩa mới.

Camera drift, đổi pose vô nghĩa, zoom trang trí và generate lại cùng scene nhưng làm nhân vật trôi không phải delta.

### 7. Recurring visual anchor phải gánh cấu trúc video

Tấm `Rarest Human` nền olive quay lại nhiều lần, gồm [frame 057](the-rarest-human-possible/extracted-frames/frame-057_01m27.27s.jpg), [frame 083](the-rarest-human-possible/extracted-frames/frame-083_02m17.73s.jpg), [frame 119](the-rarest-human-possible/extracted-frames/frame-119_03m33.27s.jpg) và [frame 164](the-rarest-human-possible/extracted-frames/frame-164_05m31.37s.jpg).

Nó đồng thời là:

- Scoreboard.
- Progress bar.
- Recap ngắn.
- Cầu nối chương.
- Lời hứa về payoff tiếp theo.

Mỗi script TossExplains phải được kiểm tra xem có một vật thể, bố cục, phép đo, trạng thái hay câu hỏi nào có thể quay lại với ý nghĩa thay đổi hay không. Không ép mọi video có scoreboard, nhưng không được bỏ qua câu hỏi thiết kế này.

### 8. Mỗi chương là một vòng curiosity có nhân quả

Video 2 liên tục dùng vòng:

`đặt một biến -> giải thích cơ chế -> trả con số hoặc visual payoff -> cho thấy hệ quả chưa giải thích -> mở biến tiếp theo`.

TossExplains nên dùng cấu trúc tương ứng:

`trải nghiệm hiện đại -> cơ chế tâm lý -> bằng chứng -> nguồn gốc tổ tiên -> modern mismatch -> twist -> một shift có thể sống cùng`.

Không dùng teaser hoặc câu hỏi tu từ không liên quan chỉ để giữ người xem.

### 9. Cỡ cảnh phải tham gia lập luận

Wide định vị thế giới hoặc quy mô. Medium kể hành động. Close-up khóa cảm xúc hoặc vật thể quyết định. Macro biến bàn tay, mắt, nút bấm, dấu vết hoặc chi tiết thí nghiệm thành một sự kiện.

Không đổi góc chỉ để tạo cảm giác video có nhiều hình. Mỗi thay đổi khoảng cách phải làm lộ thông tin mới.

### 10. Màu phải tạo semantic anchor

Video 2 dùng một hệ màu ấm đủ thống nhất, đồng thời gắn một số nền và accent với các khái niệm quay lại. TossExplains nên học tính nhất quán và chức năng ghi nhớ, không sao chép palette cụ thể.

Nguyên tắc đề xuất:

- Mỗi base plate có một palette giới hạn và cố định.
- Variant giữ nguyên palette của plate.
- Màu background phục vụ ý nghĩa scene.
- Màu chapter ưu tiên làm accent, label hoặc recurring motif, không tự động chiếm toàn bộ background.
- Màu nguy hiểm, phủ định và payoff phải được dùng nhất quán.

### 11. Nhịp là tiến triển, không phải thay toàn bộ ảnh

Video 2 có 181 visual beat trong 6:18, trung bình 2,05 giây giữa các beat và trung vị 1,87 giây. Nhưng 81 khoảng chuyển dài hơn 2 giây và 37 khoảng dài hơn 3 giây.

Bài học phải sao chép là nhịp **phần thưởng thị giác**, không phải quota ảnh mới:

- Hook nhanh nhất.
- Đoạn giải thích chậm hơn.
- Frame dày thông tin được giữ lâu hơn.
- Payoff có thể tăng tốc hoặc tạo một reveal mạnh.
- Đoạn kết có đủ thời gian để ý nghĩa hạ xuống.

Một crop, reveal, delta, update hoặc return đều có thể là visual beat mà không cần ảnh AI độc lập.

### 12. Scene cảm xúc và scene khoa học phải nằm trong cùng một hệ

Past Tense chuyển tự nhiên giữa đời sống, portrait, diagram, infographic và scale metaphor. Video không bị biến thành bài giảng vì science liên tục quay lại con người. TossExplains nên sao chép chính nhịp luân phiên này.

## Những nâng cấp phải lấy từ video 3

### 1. Tách function khỏi register

Ink Explainer cho thấy cùng một nhiệm vụ có thể được trình bày bằng nhiều hình thức. TossExplains cần hai trục riêng.

Function trả lời frame làm gì:

- `WORLD`
- `REACTION`
- `MECHANISM`
- `CONTRAST`
- `PAYOFF`

Register trả lời thông tin sống ở đâu:

- `STORY`: scene có không gian và hành động.
- `CARD`: nền sạch cho số, nguồn, object, diagram hoặc semantic text.
- `DIRECT`: Toss hoặc nhân vật nói trực tiếp, phản ứng, đặt câu hỏi hay nêu caveat.
- `HYBRID`: scene có không gian cộng diagram hoặc nhãn khi vị trí là bằng chứng.

Không biến function và register thành một danh sách mode lẫn cấp.

### 2. Đổi register để chống thích nghi thị giác

Video 3 đổi register 138 lần trong 355 beat, trung bình khoảng 2,6 beat một lần. Con số này không phải quota cho TossExplains. Nó chứng minh rằng mắt cần được đổi cách tiếp nhận thông tin, ngay cả khi nội dung vẫn nằm trong cùng một chương.

Sau khoảng 2 đến 3 beat cùng một register, visual plan nên kiểm tra xem người xem có cần chuyển cách trình bày không. Nếu plate vẫn progressive build và delta còn mang ý nghĩa, có thể tiếp tục giữ.

### 3. Visual receipt chỉ dành cho anchor claim

Ink Explainer làm nghiên cứu có vẻ hữu hình bằng bản đồ, ngày tháng, hiện vật, thiết bị và thẻ nghiên cứu. TossExplains nên bổ sung receipt cho:

- Nghiên cứu hoặc nhà nghiên cứu được gọi tên.
- Một con số quyết định lập luận.
- Ngày, địa điểm, hiện vật hoặc apparatus cụ thể.
- Một claim có thể gây tranh luận.

Không tạo receipt cho mọi câu. Mức chắc chắn phải nhìn thấy được bằng `?`, `~`, khoảng, `MAY` hoặc `POSSIBLE` khi phù hợp.

### 4. Diagram có thể sống trong scene

Chuỗi top-down sàn hang ở [frame 145](what-did-ancient-humans-do-when-it-rained-all-week/extracted-frames/frame-145_04m21.67s.jpg) đến [frame 147](what-did-ancient-humans-do-when-it-rained-all-week/extracted-frames/frame-147_04m28.30s.jpg) giữ bối cảnh, nhân vật và lập luận trong cùng một hình.

TossExplains nên dùng `HYBRID` khi vị trí là bằng chứng. Nếu cần câu dài hoặc diagram phức tạp, chuyển sang `CARD`.

### 5. Direct cut-in phải đánh dấu đổi vai tu từ

Toss cut-in chỉ có giá trị khi người kể:

- Đặt câu hỏi mới.
- Nêu caveat hoặc mức độ bất định.
- Lật một giả định.
- Nói trực tiếp với người xem.
- Kết một đoạn dày và định hướng bước tiếp theo.

Không đặt cut-in theo đồng hồ 20 đến 40 giây. Cut-in vô chức năng chỉ là filler rẻ.

### 6. Ancient-modern mirror phải trở thành ngôn ngữ đặc trưng

Cặp cảnh modern và ancient ở [frame 040](what-did-ancient-humans-do-when-it-rained-all-week/extracted-frames/frame-040_01m02.83s.jpg) và [frame 046](what-did-ancient-humans-do-when-it-rained-all-week/extracted-frames/frame-046_01m11.83s.jpg) cho người xem nhận ra hai thời đại đang phản ứng với cùng một tín hiệu.

TossExplains có thể dùng:

- Hai frame liên tiếp cùng hành động và bố cục nhưng đổi thời đại.
- Match cut qua một object bridge.
- Split khi hai trạng thái cần được thấy đồng thời.
- Cùng sound lettering trong hai bối cảnh.

Không dùng tổ tiên để khiến người hiện đại trông lười, yếu hoặc đáng xấu hổ.

### 7. Phần kết phải hội tụ

Video 3 mạnh hơn video 2 ở cấu trúc ending. Nó gọi lại câu hỏi, montage bằng chứng, merge các mảnh và trả ý nghĩa về người xem. TossExplains nên dùng cấu trúc:

1. Echo hình ảnh hoặc câu hỏi mở đầu.
2. Trả một câu ngắn đã được video chứng minh.
3. Gọi lại hai đến bốn motif hoặc bằng chứng.
4. Merge chúng thành một cơ chế bậc cao hơn.
5. Phản chiếu cơ chế về đời sống hiện đại.
6. Đưa ra một shift cụ thể.
7. Kết bằng visual release.

Ending phải được gieo từ script. Giai đoạn scene không thể tự cứu một ending không có setup.

### 8. Ánh sáng và semantic text phải có chức năng

Video 3 dùng ấm quanh lửa cho an toàn, xám lạnh cho nguy hiểm và bình minh cho release. TossExplains có thể học warm-cool contrast, nhưng phải giữ hình doodle và continuity.

Semantic text chỉ nên:

- Đặt tên một ý.
- Nén một kết luận.
- Đảo nghĩa.
- Tạo punch hoặc payoff.
- Biểu diễn âm thanh có vị trí.

Không burn toàn bộ narration vào hình.

## Bộ lọc lỗi bắt buộc

### Lỗi của video 2 không được sao chép

1. [Frame 082](the-rarest-human-possible/extracted-frames/frame-082_02m16.20s.jpg) ghi sai xác suất ethnic origin một bậc 10.
2. [Frame 164](the-rarest-human-possible/extracted-frames/frame-164_05m31.37s.jpg) gọi sai bậc số lớn, tạo sai lệch 1.000 lần.
3. Phép nhân giả định các đặc điểm độc lập dù chúng có thể phụ thuộc di truyền, giới tính và quần thể.
4. Một số nhãn khoa học quá nhỏ để đọc trên điện thoại, ví dụ phổ bước sóng ở [frame 127](the-rarest-human-possible/extracted-frames/frame-127_03m51.60s.jpg).
5. Một số cut giữ frame blur hoặc trạng thái chuyển tiếp không thêm thông tin.
6. Đoạn `Keep Swimming` tạo cảm xúc nhưng lỏng khỏi chuỗi bằng chứng. TossExplains không kết bằng affirmation chung chung.
7. Nhân vật và line weight vẫn có độ trôi giữa các scene. TossExplains phải khóa mascot và cast chặt hơn video mẫu.

### Lỗi của video 3 không được sao chép

1. Không trình bày giả thuyết như sự thật, như bản đồ `ALL CAVE ART = PLACES WHERE PEOPLE GOT STUCK INSIDE`.
2. Không dùng một con số dễ nhớ khi chưa xác định chính xác đại lượng, như thẻ `WET 25x`.
3. Không ép mọi chữ sang card. Punch word, nhãn không gian và sound lettering có thể sống trong scene.
4. Không tạo visual receipt cho mọi khẳng định.
5. Không đặt Direct cut-in theo đồng hồ.
6. Không khóa rule of three.
7. Không dùng split ancient-modern để phán xét người xem.
8. Không dùng title card hoặc màu full-background như thủ tục bắt buộc cho mọi chương.

### Video 1 chỉ đóng vai trò đối chứng thất bại

Không lấy bất kỳ ưu điểm nào của video 1 làm nền tảng chiến lược. Chỉ ghi nhận các cảnh báo:

1. Không lấy plate rate 13,3 beat/phút làm mục tiêu cho TossExplains. Phương pháp extract của video 1 cũng bỏ phần lớn caption state, nên con số không cùng đơn vị với video 2 và 3.
2. Không dùng fade qua đen làm dấu câu mặc định cho một channel có nhịp nhanh.
3. Không burn karaoke caption từng chữ vào hình. Nó làm video khó bản địa hóa, dễ đè caption YouTube và biến speech rate thành visual noise.
4. Không để painterly detail che sự trôi của mascot, khuôn mặt, tỉ lệ cơ thể và quần áo.
5. Không kéo dài hold kiến trúc hoặc phong cảnh nếu hình không còn tạo tiến triển ý nghĩa.
6. Không phá style bằng ảnh thật hoặc render khác chỉ vì AI tạo được. Ngoại lệ phải báo hiệu một chuyển biến nội dung rõ.
7. Không biến motif riêng của một kịch bản thành công thức cho mọi video.

Video 1 có thể chưa phải thất bại tuyệt đối chỉ từ snapshot 45 nghìn view sau 8 ngày, nhưng so với hai mẫu 1 triệu view, nó không đủ trọng lượng để đặt hướng phát triển.

## Visual grammar đề xuất cho TossExplains

Mỗi visual beat được quyết định bằng năm trục độc lập.

### Trục 1: Function

| Function | Nhiệm vụ chính |
| --- | --- |
| `WORLD` | Diễn một sự kiện hiện đại, thí nghiệm hoặc tổ tiên trong một địa điểm |
| `REACTION` | Thể hiện cảm xúc, suy nghĩ, nhận ra hoặc giao tiếp với người xem |
| `MECHANISM` | Giải thích nguyên nhân, hệ thống, cơ thể, não, thí nghiệm hoặc luồng thông tin |
| `CONTRAST` | So sánh thời đại, lựa chọn, nguyên nhân hoặc trạng thái |
| `PAYOFF` | Trả câu hỏi, lộ bằng chứng, đảo cách hiểu hoặc tổng hợp |

### Trục 2: Register

| Register | Hình thức |
| --- | --- |
| `STORY` | Scene có không gian, hành động và không khí |
| `CARD` | Không gian sạch cho con số, receipt, object, diagram hoặc semantic text |
| `DIRECT` | Toss hoặc nhân vật phản ứng, hỏi, cảnh báo hay nói trực tiếp |
| `HYBRID` | Scene có không gian cộng nhãn, mũi tên hoặc diagram mà vị trí có ý nghĩa |

### Trục 3: Shot scale

- `WIDE`
- `MEDIUM`
- `CLOSE_UP`
- `MACRO`
- `NONE` cho card hoặc diagram không có khoảng cách camera có ý nghĩa.

### Trục 4: Progression

| Progression | Thay đổi nhìn thấy được |
| --- | --- |
| `NEW_PLATE` | Mở một địa điểm, layout hoặc visual proposition mới |
| `DELTA` | Giữ plate và đổi một biến có ý nghĩa |
| `REFRAME` | Crop, zoom hoặc đổi cỡ để chuyển điểm nhìn |
| `REVEAL` | Thêm thành phần, nhãn, số hoặc hệ quả theo lớp |
| `MERGE` | Gộp các phần đã học thành payoff |
| `RETURN` | Quay lại plate cũ với trạng thái hoặc ý nghĩa mới |
| `NONE` | Hold có chủ đích để người xem đọc hoặc cảm nhận |

### Trục 5: Production

| Production | Công việc thực tế |
| --- | --- |
| `HERO` | Generate một base plate mới |
| `VARIANT` | Dùng reference hoặc continuation, chỉ thay delta được chỉ định |
| `EDIT` | Crop, zoom, label, arrow, highlight, number hoặc sound lettering ở khâu dựng |
| `HOLD` | Giữ trạng thái hiện tại |
| `REUSE` | Dùng lại nguyên plate hoặc asset đã có |

Năm trục này tạo đa dạng có kiểm soát. Chúng không phải năm danh sách quota.

## Phong cách scene đề xuất

### Bản sắc giữ lại của TossExplains

- Hand-drawn 2D doodle cartoon.
- Bold black outline và nét marker hơi không hoàn hảo.
- Mascot Toss và cast có identity ổn định.
- Hình đơn giản, biểu cảm rõ, đọc nhanh trên điện thoại.
- Psychology, anthropology và self-help vẫn là ba trụ nội dung.

### Phần cần tiến gần Past Tense

- Scene đời sống có địa điểm cụ thể, không phải nhân vật đứng trên slide.
- Foreground, midground và background tạo chiều sâu bằng overlap, scale và placement.
- Bảng màu hài hòa, giới hạn theo từng base plate.
- Độ chi tiết thay đổi theo nhiệm vụ scene.
- Mỗi chapter có một visual proposition riêng nhưng vẫn cùng một thế giới.
- Wide, medium, close-up và macro được dùng như cú pháp kể chuyện.
- Diagram, infographic và scale metaphor có cùng line language với scene kể chuyện.

### Vai trò mới của nền trắng

Nền trắng không biến mất và cũng không còn là mặc định cho phần lớn scene.

Dùng nền trắng hoặc cream khi:

- Dữ liệu cần đọc nhanh.
- Diagram phức tạp cần khoảng trống.
- Toss giao tiếp trực tiếp.
- Reaction hoặc punchline cần cô lập.
- Một object hoặc con số là toàn bộ luận điểm.

Dùng scene có môi trường khi:

- Địa điểm, khoảng cách hoặc quan hệ xã hội là nội dung.
- Hành động cần được diễn ra.
- Tâm trạng cần được cảm nhận qua thế giới.
- Modern và ancient cần được mirror bằng bố cục.

Không chốt tỉ lệ phần trăm nền trắng trước pilot.

## Chính sách chữ và bằng chứng

- Caption đầy đủ được upload qua YouTube, không burn vào scene.
- Text trong hình là semantic text, không phải transcription.
- Punch word có thể overlay scene nếu nó là điểm nhìn chính.
- Dữ liệu, định nghĩa dài và diagram phức tạp ưu tiên `CARD`.
- Sound lettering và spatial label có thể nằm trong `STORY` hoặc `HYBRID`.
- Chữ quan trọng phải đọc được khi frame thu còn 25% kích thước.
- Con số, ngày tháng, tên nghiên cứu và quan hệ nhân quả phải được kiểm tra độc lập.
- Mức độ chắc chắn của bằng chứng phải được thể hiện trong hình.

## Nhịp mục tiêu cho pilot

Không khóa một quota toàn channel. Dùng profile của video 2 làm điểm xuất phát:

| Phần | Nhịp tham chiếu | Ý nghĩa |
| --- | --- | --- |
| Hook | Khoảng 1,6 đến 1,9 giây mỗi visual reward | Escalation nhanh, nhiều thay đổi cỡ cảnh và chi tiết |
| Thân bài | Khoảng 2,0 đến 2,5 giây mỗi visual reward | Đủ nhanh để có tiến triển, đủ chậm để hiểu cơ chế |
| Frame dày thông tin | Có thể giữ trên 3 giây | Cho mắt thời gian quét và đọc |
| Payoff | Có thể tăng nhịp hoặc dùng một reveal lớn | Nhịp theo cảm xúc và mức nén thông tin |
| Ending | Khoảng 2,5 đến 3,0 giây ở các beat chính | Cho ý nghĩa hội tụ và hạ xuống |

Visual reward không đồng nghĩa với ảnh mới. Nhịp được tạo bằng `HERO`, `VARIANT`, `EDIT`, `HOLD` và `REUSE`.

TossExplains hiện đã có nhịp khoảng 2 đến 3 giây mỗi beat. Điều cần đổi trước tiên không phải ép nhịp nhanh hơn, mà là làm mỗi beat có tiến triển ý nghĩa và thay đổi loại phần thưởng thị giác có chủ đích.

## Kiến trúc một video TossExplains theo hướng mới

### Hook

1. Mở trong một tình huống đang xảy ra.
2. Dùng wide để đặt địa điểm.
3. Dùng close-up hoặc macro để tạo chi tiết lạ.
4. Tăng stake bằng một thay đổi nhìn thấy được.
5. Reveal câu hỏi trung tâm sau khi người xem đã đầu tư cảm xúc.

### Mỗi chương thân bài

1. Mở một câu hỏi do chương trước tạo ra.
2. Cho người xem thấy một scene hoặc thí nghiệm cụ thể.
3. Chuyển sang mechanism hoặc receipt khi cần hiểu.
4. Progressive build bằng base plate cộng delta.
5. Trả một payoff nhìn thấy được.
6. Cập nhật recurring anchor nếu kịch bản có anchor phù hợp.
7. Để hệ quả của payoff mở chương tiếp theo.

### Modern mismatch

1. Match một hành động hoặc tín hiệu ở tổ tiên với hiện đại.
2. Cho thấy cơ chế giống nhau.
3. Cho thấy môi trường đã thay đổi.
4. Không phán xét người xem.
5. Dẫn đến một reframe thay vì lời khuyên rời rạc.

### Ending

1. Return về hook.
2. Recall hai đến bốn visual proof đã gieo.
3. Merge chúng thành một câu trả lời cao hơn.
4. Trả câu trả lời về trải nghiệm hiện tại.
5. Đưa ra một shift cụ thể.
6. Kết bằng visual release, không bằng affirmation chung chung.

## Tiêu chuẩn review cho từng scene

Một scene chỉ đạt khi trả lời được tất cả câu hỏi liên quan:

1. Meaning change nào khiến beat này tồn tại?
2. Function chính là gì?
3. Register này có phải cách trình bày rõ nhất không?
4. Mắt nhìn vào đâu trước và đi đâu tiếp theo?
5. Chi tiết nào đang xác định không gian, giải thích, dẫn mắt hoặc tạo cảm xúc?
6. Có thể dùng plate hiện tại với delta thay vì generate scene mới không?
7. Cỡ cảnh mới có làm lộ thông tin mới không?
8. Text có semantic value hay chỉ lặp voiceover?
9. Claim và con số đã được kiểm tra chưa?
10. Mascot, cast, camera, palette và major object có giữ continuity không?
11. Beat có đọc được trên điện thoại không?
12. Beat đang mở, trả hay nối curiosity loop nào?

Không dùng checklist này như quota. Nó là bộ câu hỏi để phát hiện scene không có lý do tồn tại.

## Tiêu chuẩn thành công của hệ mới

Hướng mới thành công khi:

1. Video có cảm giác đang diễn ra, không giống chuỗi slide minh họa.
2. Mỗi luận điểm chính có visual proof thay vì icon trang trí.
3. Scene giàu không gian và scene tối giản hỗ trợ lẫn nhau.
4. Base plate tạo được nhiều reward mà không làm nhân vật hoặc camera trôi.
5. Mỗi frame có một điểm vào mắt rõ.
6. Register đổi theo vai trò lập luận, không theo đồng hồ.
7. Recurring anchor giúp người xem nhớ và cảm thấy tiến độ khi nội dung phù hợp.
8. Bằng chứng nhìn đáng tin và thể hiện đúng mức độ chắc chắn.
9. Ancient-modern mirror tạo nhận ra, không tạo xấu hổ.
10. Ending gom được những gì video đã gieo.
11. Toss vẫn có bản sắc riêng dù hệ đạo diễn học sát Past Tense.
12. Số visual reward tăng mà số ảnh AI độc lập không tăng tuyến tính.

## Những điều không được biến thành luật cứng

- Không bắt buộc mỗi câu narration một ảnh.
- Không vẽ riêng từng danh từ.
- Không bắt buộc ảnh mới mỗi 1 đến 2 giây.
- Không khóa tỉ lệ register từ video 2 hoặc video 3.
- Không bắt buộc mỗi video có scoreboard.
- Không bắt buộc rule of three.
- Không đặt Direct cut-in theo số giây.
- Không tạo receipt cho mọi claim.
- Không bắt buộc màu full-background riêng cho từng chương.
- Không bắt buộc chữ luôn nằm trên nền trắng.
- Không bắt buộc mọi scene có hậu cảnh.
- Không burn caption đầy đủ vào hình.
- Không kết bằng affirmation không được phần thân chứng minh.
- Không copy một frame, asset hoặc chuỗi shot đặc trưng của đối thủ.

## Phạm vi cập nhật hệ thống đã triển khai

Sau khi chủ kênh duyệt, hệ thống hiện tại đã được audit theo chênh lệch và cập nhật các khu vực liên quan:

1. `channel-dna.md`: enacted hook, causal curiosity chain, recurring anchor và convergent ending.
2. `visual-style.md`: scene depth, controlled density, function, register, shot scale, progression, palette, text và visual receipt.
3. Skill `script`: gieo visual anchor, causal chapter loop và ending từ đầu.
4. Skill `visual-plan`: lập kế hoạch theo meaning change, function, register, shot, progression và production.
5. Skill `scenes`: tạo base plate và variant có continuity, không generate một ảnh độc lập cho mọi beat.
6. Skill `check`: kiểm tra visual proof, mobile readability, evidence accuracy, continuity và ending convergence ở mức có thể kiểm tra được.
7. `file-formats.md` và validator liên quan, chỉ khi schema thực thi cần thay đổi.

Các file không được cập nhật bằng cách chép nguyên văn tài liệu này. Việc triển khai giữ phần canonical đã đúng, bổ sung các chênh lệch thật sự, giữ tương thích với artifact legacy và biến các quyết định phù hợp thành contract có thể kiểm tra.

## Các quyết định chủ kênh đã chốt

1. "COPY 100%" nghĩa là sao chép toàn bộ hệ vận hành có thể chuyển giao, không sao chép asset, frame và chuỗi shot nhận diện.
2. Past Tense là xương sống, Ink Explainer là lớp nâng cấp và Before Civilization chỉ là đối chứng âm.
3. Giữ nhịp TossExplains hiện tại làm nền, thay loại visual reward trước khi tăng beat rate.
4. Nền trắng trở thành một register có chức năng, không còn là mặc định và cũng không bị loại bỏ.
5. Dùng năm trục `function + register + shot scale + progression + production` làm grammar chính, với render tier là lớp kiểm soát trình bày riêng.
6. Chỉ dùng visual receipt cho anchor claim và luôn biểu diễn đúng mức độ chắc chắn.
7. Ancient-modern mirror và convergent ending trở thành hai năng lực đặc trưng của TossExplains.

## Kết luận đã chốt

Past Tense là mẫu chính vì nó mạnh nhất ở điều TossExplains đang thiếu: **biến lời kể thành tiến triển nhìn thấy được mà vẫn điều tiết được độ phức tạp**. Ink Explainer bổ sung những thứ giúp hệ đó đáng tin và có cấu trúc hơn: register rõ, receipt có bằng chứng, hybrid diagram, ancient-modern mirror và ending hội tụ.

Video 1 không cung cấp nền tảng cho hướng mới. Nó nhắc TossExplains tránh nhịp plate chậm, caption karaoke, fade mặc định, hold không tiến triển và render AI thiếu consistency.

Nguyên tắc triển khai trung tâm là:

> **TossExplains giữ chủ đề, giọng kể, mascot và trách nhiệm khoa học của mình, nhưng vận hành hình ảnh theo kỷ luật của Past Tense, được nâng cấp bằng cấu trúc bằng chứng và phần kết của Ink Explainer.**
