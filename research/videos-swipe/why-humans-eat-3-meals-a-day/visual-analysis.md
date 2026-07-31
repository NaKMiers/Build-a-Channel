# Phân tích hình ảnh - Why Humans Eat 3 Meals a Day

Kênh: Past Tense (`https://www.youtube.com/@PastTense01`). Link gốc:
`https://www.youtube.com/watch?v=N2Y4-_dkKe0`. Số view không đọc được bằng script vì
YouTube chặn bot ở watch page, nên không ghi ở đây. Xác minh file bằng
`tools/youtube-verify.py`: VERIFIED, video id `N2Y4-_dkKe0` nằm trong tên file, tiêu đề
và tên kênh lấy trực tiếp từ oEmbed.

## Kết quả extract

- Video nguồn: 08:25.82 (505.82 giây), 1920x1080, 30 FPS, khoảng 15.175 frame mã hóa.
- Bộ nghiên cứu: **272 trạng thái hình ảnh** khác nhau, giữ nguyên 1920x1080.
- Contact sheet: **12 trang**, mỗi frame có số thứ tự và timestamp.
- Index: `frame-index.csv` (273 dòng, 1 dòng header).
- Phương pháp: phát hiện thay đổi nội dung ở ngưỡng thấp (scene threshold 0.02) để bắt cả
  cut lớn và từng bước build nhỏ. Từ **274 ứng viên**, loại đúng **2 frame**:
  - `02:11.86` (ứng viên c094): chữ "Ariston" đã rời khỏi khung và cái bàn mới trượt vài
    pixel sang phải, không thêm bất cứ thông tin nào so với frame trước. Đây là frame giữa
    hai trạng thái, không phải một bước build.
  - `08:17.40` (ứng viên c272): cách frame trước đúng **0,03 giây**, tức một frame ở 30 FPS.
    Bộ phát hiện scene bắn hai lần trên cùng một cut, hai ảnh là cùng một timeline lệch vài
    pixel.

Không frame nào bị loại vì blur. Video này có **ba frame cố tình làm nhòe hậu cảnh** để
đồ họa nổi lên: [frame 144](extracted-frames/frame-144_03m56.60s.jpg),
[frame 153](extracted-frames/frame-153_04m19.77s.jpg) và
[frame 253](extracted-frames/frame-253_07m38.33s.jpg). Cả ba đều được giữ. Danh sách
edge-energy thấp mà tool cảnh báo gồm tám frame, và tất cả đều là thẻ phẳng sạch chứ không
phải blur: [frame 9](extracted-frames/frame-009_00m08.53s.jpg) và
[frame 74](extracted-frames/frame-074_01m45.93s.jpg) là base plate rỗng cố ý,
[frame 61](extracted-frames/frame-061_01m26.80s.jpg) là icon quả địa cầu phẳng,
[frame 166](extracted-frames/frame-166_04m44.80s.jpg) là thẻ chữ phẳng,
[frame 180](extracted-frames/frame-180_05m10.60s.jpg) là một phòng gần như trống.

"272 frame" không phải 272 frame ngẫu nhiên. Đó là 272 visual beat: mỗi beat là một trạng
thái mà người xem nhận thêm thông tin, dù chỉ là một icon xuất hiện, một nhãn mở ra, một
chữ đè lên, hay một nền đổi màu.

## Kết luận quan trọng nhất

Video này giữ được người xem **không phải bằng cảnh, mà bằng thẻ**. Cơ chế trung tâm là:
**một base plate màu ấm, giữ nguyên, rồi thêm từng phần tử một lần một, và khi thẻ đã đầy
thì đè một chữ đỏ lên chính nó để chốt lập luận.** Hook chỉ dài 12 beat, nhưng bốn beat
trong đó là một chuỗi build trên đúng một tấm thẻ vàng.

Đây là toàn bộ chuỗi mở màn, đọc theo đúng thứ tự:

| Frame | Thời điểm | Nội dung thẻ |
| --- | --- | --- |
| [9](extracted-frames/frame-009_00m08.53s.jpg) | 00:08.53 | thẻ vàng **rỗng hoàn toàn** |
| [10](extracted-frames/frame-010_00m08.73s.jpg) | 00:08.73 | thêm dĩa trứng thịt xông khói bánh mì, cốc cà phê, chữ "Breakfast" |
| [11](extracted-frames/frame-011_00m09.33s.jpg) | 00:09.33 | thêm mũi tên đỏ, dĩa sandwich, quả táo, chữ "Lunch" |
| [12](extracted-frames/frame-012_00m10.03s.jpg) | 00:10.03 | thêm mũi tên đỏ thứ hai, dĩa bò bít tết, chữ "Dinner" |

Bốn beat trong 1,5 giây, và ba beat cuối bị tool đánh dấu "diff thấp" đúng vì mỗi bước chỉ
thay đổi một phần khung. Nếu loại chúng theo gợi ý của tool thì cơ chế cốt lõi của video sẽ
biến mất khỏi bộ nghiên cứu.

Cơ chế này không phải chuyện một lần. Nó lặp lại **tám lần** trong 8 phút:
[frames 9 tới 12](extracted-frames/frame-012_00m10.03s.jpg) (ba bữa ăn),
[37 tới 39](extracted-frames/frame-039_00m50.40s.jpg) (ba bộ xương),
[74 tới 77](extracted-frames/frame-077_01m48.43s.jpg) (bình, cột, địa cầu, mặt trời),
[84 tới 86](extracted-frames/frame-086_01m59.63s.jpg) (ba món Ai Cập),
[207 tới 210](extracted-frames/frame-210_06m13.93s.jpg) (bốn khái niệm sinh học),
[220 tới 222](extracted-frames/frame-222_06m36.07s.jpg) (ba icon hậu quả),
[229 tới 231](extracted-frames/frame-231_06m52.93s.jpg) (ba icon thay thế nhau) và
[246 tới 248](extracted-frames/frame-248_07m26.27s.jpg) (ba lợi ích xã hội).

Và cơ chế thứ hai, luôn đi kèm: **chữ đỏ viết tay đè lên chính hình vừa dựng xong**. Không
phải caption ở trên đầu khung, mà chữ nằm chồng lên hình, to bằng một phần ba khung. Có bảy
lần: [frame 8](extracted-frames/frame-008_00m07.30s.jpg) "Never",
[frame 53](extracted-frames/frame-053_01m11.23s.jpg) "Result",
[frame 88](extracted-frames/frame-088_02m01.70s.jpg) "Not three",
[frame 161](extracted-frames/frame-161_04m35.37s.jpg) "Solution",
[frame 198](extracted-frames/frame-198_05m53.30s.jpg) "It worked",
[frame 219](extracted-frames/frame-219_06m31.70s.jpg) "Outcome changes",
[frame 228](extracted-frames/frame-228_06m49.93s.jpg) "Not Passive". Mỗi lần là một câu kết
luận, và mỗi lần đều đè lên đúng cái hình vừa mất mấy beat để dựng. Người xem đọc hình
trước, rồi mới nhận phán quyết.

Điểm khác biệt lớn nhất so với hai video đã nghiên cứu trước: **video này không có thẻ
trắng nào cả.** Mọi frame đều nằm trên một nền màu ấm (kem, hổ phách, vàng, cam đất, nâu
đỏ). Nền trắng không tồn tại trong 272 frame. Đó là một quyết định thẩm mỹ nhất quán, và
cũng chính là phần TossExplains không được sao chép.

## Nhịp hình ảnh

Số của tool, không làm tròn lại:

- beat: **272**
- beat mỗi phút: **32,3**
- khoảng cách trung bình giữa các beat: **1,85 giây**
- khoảng cách trung vị: **1,73 giây**
- khoảng cách dưới 1 giây: 36 lần
- khoảng cách dưới 2 giây: 175 trên 271
- khoảng cách từ 4 giây trở lên: chỉ 6 lần
- beat trong 15 giây đầu: **14**
- hook (0 tới 45 giây): 35 beat, **1,36 giây mỗi beat**, tức 46,7 beat mỗi phút
- hold dài nhất: 4,80 giây ở frame 264, 4,33 giây ở frame 225, 4,23 giây ở frame 241,
  4,23 giây ở frame 129, 4,20 giây ở frame 254

Ở toàn bộ tài liệu này, "giây mỗi beat" luôn là **khoảng cách trung bình giữa các beat**,
không phải thời lượng chia số beat.

| Đoạn | Frame | Beat mỗi phút | Giây mỗi beat |
| --- | --- | ---: | ---: |
| Hook | 001-012 | 65,8 | 0,91 |
| Luận đề | 013-027 | 43,7 | 1,37 |
| Ohalo II | 028-054 | 38,8 | 1,54 |
| Nông nghiệp | 055-077 | 38,4 | 1,56 |
| Ai Cập | 078-088 | 48,9 | 1,23 |
| Hy Lạp | 089-099 | 37,2 | 1,61 |
| La Mã | 100-114 | 27,7 | 2,16 |
| Thực dân | 115-131 | 28,8 | 2,08 |
| Thời thuyền buồm | 132-144 | 24,9 | 2,41 |
| Cách mạng công nghiệp | 145-167 | 27,3 | 2,20 |
| Tu sĩ và công nhân | 168-185 | 30,4 | 1,97 |
| Kellogg và quảng cáo | 186-198 | 24,9 | 2,41 |
| Sinh học | 199-233 | 33,0 | 1,82 |
| Thời điểm ăn | 234-251 | 29,3 | 2,05 |
| Kết | 252-272 | 27,9 | 2,15 |

Đọc bảng này thì thấy một hình dạng rất rõ, và nó **ngược** với video ancient-humans đã
nghiên cứu trước.

**Video nhanh nhất ở đầu, rồi chậm dần đều.** Hook chạy 65,8 beat mỗi phút, gần gấp đôi
trung bình toàn video. Ba đoạn cuối cùng chạy 27 tới 29 beat mỗi phút, tức chậm hơn hook
hơn hai lần. Đây không phải lỗi, đây là chiến lược: **12 beat đầu tiêu hết ngân sách hình
ảnh để mua sự chú ý, sau đó video tiêu chậm dần vì đã có quyền tiêu chậm.**

Hai ngoại lệ nói lên nhiều điều:

1. **Ai Cập chạy 48,9 beat mỗi phút**, nhanh thứ hai toàn video, dù nằm ở phút thứ hai.
   Đoạn đó gồm 11 frame trong 13 giây, và bên trong nó có đúng một chuỗi build ba bước
   ([frames 84 tới 86](extracted-frames/frame-086_01m59.63s.jpg)) cộng một cú chữ đè
   ([frame 88](extracted-frames/frame-088_02m01.70s.jpg)). Cơ chế build luôn kéo nhịp lên.
2. **Kellogg và quảng cáo chậm nhất, 24,9 beat mỗi phút**, cùng với Thời thuyền buồm. Đó là
   đoạn có hai frame chi tiết nhất toàn video: biển quảng cáo
   [frame 192](extracted-frames/frame-192_05m40.53s.jpg) (sharpness 41,3, cao nhất trong 272
   frame) và tờ rơi [frame 193](extracted-frames/frame-193_05m42.23s.jpg). Frame nào có
   nhiều chữ để đọc thì được giữ lâu hơn. Đó là một quy tắc dùng được ngay.

Chỉ 6 lần trong toàn video có khoảng nghỉ từ 4 giây trở lên. Video này gần như không cho
người xem một giây trống nào.

## Mười một cơ chế làm video cuốn

### 1. Hook là hai frame, và hai frame đó quay lại ở cuối

Hook mở bằng một thân người, không bằng một câu: cậu bé vừa thức dậy
[frame 1](extracted-frames/frame-001_00m00.00s.jpg), rồi ăn sáng
[frame 2](extracted-frames/frame-002_00m01.20s.jpg), rồi một cái đồng hồ tường khổng lồ
[frame 3](extracted-frames/frame-003_00m02.20s.jpg) không có chữ nào (cái đồng hồ **là**
chữ), rồi ăn trưa ở bàn làm việc [frame 4](extracted-frames/frame-004_00m03.07s.jpg), rồi
thành phố lúc hoàng hôn [frame 5](extracted-frames/frame-005_00m04.23s.jpg), rồi nhìn xuyên
qua cửa sổ vào cậu bé đang ăn tối [frame 6](extracted-frames/frame-006_00m04.93s.jpg).

Sáu beat trong 5 giây, không một chữ nào.

Rồi ở 08:19, video đóng lại bằng **đúng hai frame đó**, nguyên xi, cùng thứ tự:
[frame 271](extracted-frames/frame-271_08m19.37s.jpg) là frame 5, và
[frame 272](extracted-frames/frame-272_08m20.17s.jpg) là frame 6. Đó là frame cuối cùng của
video. Vòng lặp đóng bằng tài sản có sẵn, chi phí bằng không.

### 2. Chữ nằm trên nền màu, không nằm trên thẻ trắng, và chỉ có ba màu chữ

Video ancient-humans đẩy toàn bộ chữ sang thẻ trắng riêng. Video này làm khác: chữ nằm ngay
trên nền màu ấm, và trật tự đến từ **màu chữ** thay vì từ nền.

- **Đen viết tay** là mặc định: nhãn nhân vật, tên chương, tên món.
- **Đỏ có viền** dành cho phán quyết và phủ định: "Never", "Result", "Not three",
  "Solution", "It worked", "Outcome changes", "Not Passive", "Stored Fat", "When?".
- **Trắng có viền tối** chỉ dùng đúng hai lần, và cả hai lần đều đè lên một hậu cảnh cố ý
  làm nhòe: "Historical Origin" ở [frame 253](extracted-frames/frame-253_07m38.33s.jpg) và
  "Why do we eat 3x a day?" ở [frame 255](extracted-frames/frame-255_07m44.23s.jpg).

Hệ ba màu này ổn định suốt 8 phút. Không có một chữ vàng nào trên nền sáng, ngoại trừ hai
frame etymology sẽ nói ở cơ chế 6.

### 3. Dấu X đỏ vẽ tay là công cụ phủ định duy nhất, và nó dùng 12 lần

Video không nói "điều này sai". Video vẽ một dấu X đỏ vẽ tay lên hình. Đếm được ít nhất 12
lần: [frame 7](extracted-frames/frame-007_00m06.13s.jpg) (mặt cậu bé),
[frame 14](extracted-frames/frame-014_00m13.77s.jpg) (ba người đang tranh cãi),
[frame 16](extracted-frames/frame-016_00m16.77s.jpg) (bác sĩ),
[frame 17](extracted-frames/frame-017_00m18.33s.jpg) (già làng),
[frame 44](extracted-frames/frame-044_00m58.60s.jpg) (một dĩa cơm),
[frame 46](extracted-frames/frame-046_01m00.83s.jpg) (đống thức ăn),
[frame 52](extracted-frames/frame-052_01m09.83s.jpg) (người đang ăn),
[frame 63](extracted-frames/frame-063_01m29.63s.jpg) (người đi săn),
[frame 99](extracted-frames/frame-099_02m18.80s.jpg) (đồng hồ Hy Lạp),
[frame 104](extracted-frames/frame-104_02m30.20s.jpg) (người La Mã ăn tiệc),
[frame 127](extracted-frames/frame-127_03m14.43s.jpg) (đồng hồ, cạnh một người bản địa),
[frame 172](extracted-frames/frame-172_04m55.93s.jpg) (bát cháo).

Và có ba biến thể: **gạch ngang đỏ** thay cho X khi đối tượng là chữ
([frame 42](extracted-frames/frame-042_00m56.20s.jpg) "3x",
[frame 43](extracted-frames/frame-043_00m57.57s.jpg) "twice",
[frame 71](extracted-frames/frame-071_01m42.00s.jpg) "Did not Exist"), một **hàng tick và X
trắng đỏ** thay cho một câu hoàn chỉnh ở
[frame 97](extracted-frames/frame-097_02m16.97s.jpg), và **X rồi chữ**: X biến mất và một
chữ đỏ thay chỗ nó ở [frames 7 sang 8](extracted-frames/frame-008_00m07.30s.jpg) và
[frames 52 sang 53](extracted-frames/frame-053_01m11.23s.jpg).

Một ký hiệu, dùng 12 lần, không đổi hình dạng. Đó là lý do nó đọc được ngay lần thứ 12.

### 4. Dựng set rỗng trước, rồi cho nhân vật vào sau

Đây là mẹo rẻ nhất trong toàn bộ video, và nó dùng ba lần:

| Set rỗng | Set có người | Nội dung |
| --- | --- | --- |
| [frame 67](extracted-frames/frame-067_01m36.07s.jpg) | [frame 68](extracted-frames/frame-068_01m37.67s.jpg) | bếp thời đá mới: lò đất, nồi treo, bàn, giỏ |
| [frame 94](extracted-frames/frame-094_02m12.90s.jpg) | [frame 95](extracted-frames/frame-095_02m14.17s.jpg) | bàn "DEIPNON" tròn thấp, năm gối ngồi |
| [frame 110](extracted-frames/frame-110_02m42.03s.jpg) | [frame 111](extracted-frames/frame-111_02m44.10s.jpg) | sáu món "Cena" |

Cùng một tài sản, hai beat. Beat đầu cho người xem đọc đồ ăn, beat sau cho người xem đọc
con người. Ở cặp thứ hai, video còn đổi cả thời gian trong ngày: bàn rỗng ở nền kem, bàn có
người ở đêm tím với mặt trăng và hai bó đuốc. Chữ "DEIPNON" giữ nguyên vị trí ở cả hai
frame, chỉ nền và người thay đổi.

### 5. Một set, hai lần chiếu sáng: ngày và đêm

Video dùng lại chính một bố cục và chỉ đổi ánh sáng, ba lần:

- Bếp công nhân: [frame 156](extracted-frames/frame-156_04m25.97s.jpg) buổi sáng, cửa sổ
  sáng, bàn gần trống. [frame 158](extracted-frames/frame-158_04m28.37s.jpg) buổi đêm, cửa
  sổ tối có đèn nhà bên, thêm một cây nến và một đồng hồ mặt lò sưởi.
- Bàn ăn sáng hiện đại: [frame 215](extracted-frames/frame-215_06m24.07s.jpg) ban ngày, cửa
  sổ có mặt trời. [frame 218](extracted-frames/frame-218_06m29.73s.jpg) ban đêm, cửa sổ
  xanh navy có mặt trăng và sao, tường sẫm lại. Đúng cùng cái dĩa bánh pancake, cùng cái
  bánh donut hồng, cùng cái đồng hồ.
- Thẻ "Dinner": [frame 176](extracted-frames/frame-176_05m03.90s.jpg) trên nền hổ phách, và
  [frame 182](extracted-frames/frame-182_05m15.53s.jpg) trên nền đêm navy có mặt trăng và
  sao.

Đó là cách kể một thời gian biểu mà không cần vẽ một cái lịch nào.

### 6. Cả video chỉ có một frame nền tối, và nó là frame quan trọng nhất

Trong 272 frame, nền tối gần đen xuất hiện đúng **một** lần:
[frame 167](extracted-frames/frame-167_04m46.57s.jpg), đọc "BREAK the FAST".

Và đó là cú chuyển có diff lớn nhất toàn video: **123,8**. Đường dẫn tới nó là ba beat:

1. [frame 165](extracted-frames/frame-165_04m42.17s.jpg): hai bàn tay đưa ra một dĩa ăn
   sáng đầy đủ, nền xanh bạc hà, chữ đen "Breakfast", có vệt vàng tỏa xung quanh.
2. [frame 166](extracted-frames/frame-166_04m44.80s.jpg): dĩa biến mất, còn lại chữ
   "breakfast" chữ nhỏ trong một khối vàng, cùng nền xanh.
3. [frame 167](extracted-frames/frame-167_04m46.57s.jpg): **nền chuyển sang gần đen**, khối
   vàng giữ nguyên vị trí, chữ đổi thành "BREAK the FAST" trên ba dòng.

Ba beat, một tài sản, và cú reveal etymology hạ cánh chỉ bằng việc đổi nền. Frame ngay sau
đó [frame 168](extracted-frames/frame-168_04m48.60s.jpg) bật lại nền xanh cỏ với diff 118,7,
tức video cũng không ở lại trong bóng tối quá một beat.

TossExplains **không** được sao chép hai frame này nguyên trạng, vì chữ vàng trên nền sáng
ở frames 165 và 166 là điều `visual-style.md` cấm thẳng. Nhưng cơ chế "một beat nền tối duy
nhất cho một reveal duy nhất" thì chuyển được, dùng chữ đỏ hoặc đen.

### 7. Nguồn dẫn được vẽ thành vật thể, không thành chú thích

Video có ba nguồn dẫn, và không nguồn nào xuất hiện dưới dạng text citation:

- **Người**: nhà sử học Caroline Yeldham thành một nhân vật vẽ tay với chữ đen
  "Historian Caroline Yeldham" ở [frame 106](extracted-frames/frame-106_02m34.83s.jpg), rồi
  ngay beat sau [frame 107](extracted-frames/frame-107_02m36.40s.jpg) luận điểm của bà bị
  nén thành một bong bóng suy nghĩ chứa ba ký hiệu: icon đền thờ, dấu "=", và một cái dạ
  dày. Cùng cách với Abigail Carroll ở
  [frame 121](extracted-frames/frame-121_03m02.17s.jpg) và John Harvey Kellogg ở
  [frame 189](extracted-frames/frame-189_05m32.50s.jpg).
- **Sách**: bìa "Three Squares: The Invention of the American Meal" được vẽ lại thành một
  cuốn sách thật ở [frame 122](extracted-frames/frame-122_03m04.17s.jpg).
- **Tạp chí**: "Current Biology" thành một số báo có ảnh bìa ở
  [frame 205](extracted-frames/frame-205_06m06.67s.jpg).

Ba lần đều dùng cùng một logic: nguồn dẫn là một **đồ vật trong khung**, không phải một
dòng chữ nhỏ ở góc. Người xem không đọc citation, người xem nhìn một quyển sách.

### 8. Ba lần dùng độ sâu trường ảnh, và cả ba lần đều để tách đồ họa ra khỏi cảnh

Video này chủ yếu phẳng, nhưng ba lần nó cố tình làm nhòe hậu cảnh để một lớp đồ họa nét
nằm đè lên:

- [frame 144](extracted-frames/frame-144_03m56.60s.jpg): người thủy thủ đang kéo dây bị
  nhòe, phía trước là ba mặt trời (mọc, đứng, lặn) nối bằng hai mũi tên đỏ.
- [frame 153](extracted-frames/frame-153_04m19.77s.jpg): xưởng dệt bị nhòe, phía trước là
  một cái đồng hồ tường lớn nét căng.
- [frame 253](extracted-frames/frame-253_07m38.33s.jpg): thẻ "3x" bị nhòe, chữ
  "Historical Origin" nét nằm trên.

Ba lần, cùng một ngữ pháp: **cảnh là ngữ cảnh, đồ họa là câu.** Đây là phần TossExplains
không sao chép được, vì blur nằm ngoài style lock. Nhưng cùng ý đó làm được bằng cách khác:
để cảnh nhạt bớt số vật thể xuống hai hoặc ba, rồi đặt đồ họa lên nền phẳng.

### 9. Diagram thật, không phải diagram trang trí

Đoạn sinh học dùng ngữ pháp diagram khoa học thật, đơn giản hóa mà không làm sai:

- [frame 214](extracted-frames/frame-214_06m21.90s.jpg): màng tế bào cắt lớp, năm thụ thể
  hồng bắt các hạt cam, các điểm tín hiệu tím lan vào trong theo mũi tên đen.
- [frame 223](extracted-frames/frame-223_06m37.90s.jpg): "Ghrelin" là chuỗi hạt đỏ, cắm vào
  "Ghrelin receptor" xanh dương. "Leptin" là khối tím, cắm vào "Leptin receptor" xanh lá.
  Bốn nhãn chữ nhỏ.
- [frame 238](extracted-frames/frame-238_07m07.40s.jpg): đường tiêu hóa vẽ đúng giải phẫu,
  gan, túi mật, dạ dày, tụy, ruột non, ruột già. Không nhãn, không nhân vật.
- [frame 212](extracted-frames/frame-212_06m17.73s.jpg): đồng hồ đo bảy nấc từ xanh LOW tới
  đỏ HIGH, kim ở vùng đỏ, chữ "CORTISOL".

Và ngay sau diagram phức tạp nhất, video **quay lại phiên bản đơn giản**:
[frame 224](extracted-frames/frame-224_06m39.03s.jpg) chỉ còn hai phân tử trôi tự do với hai
cái nhãn. Đó là thứ tự ngược với thói quen thường thấy, và nó hoạt động: diagram đầy đủ dạy
người xem hình dạng của phân tử, phiên bản rút gọn cho họ dùng lại hình dạng đó.

Điểm đối trọng: khi cần một phép ẩn dụ chứ không cần chính xác, video vẽ **cơ thể thành nhà
máy** ở [frame 213](extracted-frames/frame-213_06m18.73s.jpg), bốn công nhân đội mũ bảo hộ
bên trong thân người, một cái phễu nhận hamburger và bông cải. Frame đó có sharpness 39,3,
tức là một trong những frame dày nhất video, và nó là frame lavender duy nhất.

### 10. Ba dĩa ăn quay lại bốn lần, mỗi lần mang một nghĩa khác

Cùng một motif, bốn lần, và mỗi lần nghĩa của nó bị viết lại:

| Frame | Thời điểm | Trạng thái |
| --- | --- | --- |
| [49](extracted-frames/frame-049_01m05.70s.jpg) | 01:05.70 | ba dĩa trên thẻ vàng, chưa có chữ |
| [50](extracted-frames/frame-050_01m06.73s.jpg) | 01:06.73 | thêm tiêu đề "Eating Schedule" |
| [51](extracted-frames/frame-051_01m07.90s.jpg) | 01:07.90 | thêm một người thời đá với dấu "?" nhìn lên chúng |
| [131](extracted-frames/frame-131_03m25.40s.jpg) | 03:25.40 | ba dĩa đặt lên bản đồ thế giới |
| [160](extracted-frames/frame-160_04m32.87s.jpg) | 04:32.87 | ba dĩa dưới ba nhãn highlight vàng, hồng, xanh |
| [233](extracted-frames/frame-233_06m56.13s.jpg) | 06:56.13 | ba dĩa lành mạnh, chữ "What matters most" |
| [264](extracted-frames/frame-264_08m06.83s.jpg) | 08:06.83 | ba dĩa dưới tiêu đề "Three Meals" |

Chú ý frame 51: **thêm một nhân vật vào một thẻ diagram sẽ biến diagram thành câu hỏi.** Ba
dĩa một mình là thông tin. Ba dĩa cộng một người đang bối rối là một luận đề. Đó là một
thao tác một beat, và nó đáng học.

### 11. Recap ở cuối chỉ dùng tài sản đã có, năm frame liền

Từ 07:46 tới 07:57, video chạy một chuỗi recap gồm năm frame, mỗi frame lấy lại **nguyên
xi** một frame từ một chương trước, theo đúng thứ tự thời gian của chương:

| Frame recap | Lấy lại từ | Chương |
| --- | --- | --- |
| [256](extracted-frames/frame-256_07m46.43s.jpg) | frame 143 | thời thuyền buồm |
| [257](extracted-frames/frame-257_07m48.03s.jpg) | frame 173 | xưởng dệt |
| [258](extracted-frames/frame-258_07m50.63s.jpg) | frame 171 | tu sĩ |
| [259](extracted-frames/frame-259_07m53.80s.jpg) | frame 133 | phố Tudor có đồng hồ công cộng |
| [260](extracted-frames/frame-260_07m57.13s.jpg) | frame 197 | quảng cáo Sunny O's |

Không một hình mới nào được vẽ cho recap. Ngoài ra còn ít nhất bảy frame khác là tái sử
dụng: [frame 177](extracted-frames/frame-177_05m05.20s.jpg) lặp lại
[frame 151](extracted-frames/frame-151_04m14.13s.jpg),
[frame 227](extracted-frames/frame-227_06m48.93s.jpg) lặp lại diagram nội quan ở
[frame 15](extracted-frames/frame-015_00m15.13s.jpg) sau bảy phút,
[frame 240](extracted-frames/frame-240_07m11.90s.jpg) lặp lại thẻ số ở
[frame 27](extracted-frames/frame-027_00m30.30s.jpg), và
[frames 242 tới 244](extracted-frames/frame-244_07m20.33s.jpg) lặp lại xưởng dệt, ông chủ
ký sổ, và biển quảng cáo.

Ước tính: khoảng **15 trong 272 frame** là tái sử dụng, tức 5,5 phần trăm bộ frame được làm
với chi phí bằng không. Và cú tái sử dụng đắt giá nhất là diagram nội quan: nó xuất hiện ở
00:15 như một sự thật trung tính, rồi quay lại ở 06:49 với chữ đỏ "Not Passive" đè lên
([frame 228](extracted-frames/frame-228_06m49.93s.jpg)). Cùng một hình, hai lần, và lần thứ
hai nó là một lập luận.

## Phân tích từng chương

| Đoạn | Thời gian | Frame | Hình ảnh làm gì | Đạt được gì |
| --- | --- | --- | --- | --- |
| Hook | 00:00-00:10 | 001-012 | sáu beat cảnh hiện đại không chữ, rồi chuỗi build ba bữa ăn trên một thẻ vàng | 65,8 beat mỗi phút, và nêu chủ đề bằng hình trước khi nêu bằng chữ |
| Luận đề | 00:11-00:30 | 013-027 | nền xanh cobalt cho narrator, diagram nội quan, gag ba nhịp "3x meals a day" đưa cho bác sĩ, già làng, con sư tử | biến một thói quen thành một câu hỏi bằng cách cho ba nhân vật từ chối nó |
| Ohalo II | 00:32-01:12 | 028-054 | bản đồ Israel, nhà khảo cổ, cọ quét lộ hạt và xương, thẻ số "140", chuỗi phủ định 3x / twice / whenever | dựng bằng chứng vật lý trước khi kể kết luận |
| Nông nghiệp | 01:14-01:48 | 055-077 | trồng cây cận cảnh, thẻ "10,000 BCE", bản đồ Lưỡi liềm Phì nhiêu, làng đá mới, set bếp rỗng rồi có người | chuyển từ săn bắt sang trồng trọt bằng ba mức zoom, macro tới toàn cảnh |
| Ai Cập | 01:49-02:01 | 078-088 | pharaoh cầm hai khay, chữ vàng "Two" và "Meals", nhãn "BREAD" "BEER", chuỗi build ba món, "2x" rồi "Not three" | đoạn nhanh thứ hai toàn video, nhờ một chuỗi build cộng một cú chữ đè |
| Hy Lạp | 02:02-02:18 | 089-099 | ba tên bữa ăn Akratisma, Ariston, DEIPNON, mỗi tên trên một bàn khác nhau, bàn tiệc đêm có đuốc, "Not Everyone" | dạy ba từ ngoại ngữ mà không dịch, chỉ bằng cách gắn mỗi từ vào một bàn ăn |
| La Mã | 02:20-02:50 | 100-114 | quân đoàn, bản đồ đế quốc làm đạo cụ trong cảnh, "Cena", "Ientaculum", bong bóng thoại "I am still hungry." | bong bóng thoại duy nhất toàn video, dùng đúng lúc một nhân vật cần phàn nàn |
| Thực dân | 02:52-03:25 | 115-131 | thuyền caravel, bản đồ thế giới, conquistador sốc, Abigail Carroll, "UNCIVILIZED" trong bong bóng suy nghĩ | đặt định kiến vào trong đầu nhân vật, không vào lời kể |
| Thời thuyền buồm | 03:27-03:56 | 132-144 | phố Tudor, đồng hồ công cộng, diagram khẩu phần tàu có nhãn, "practical", lát cắt khoang tàu | frame nhiều chữ nhất được giữ lâu nhất, 2,41 giây mỗi beat |
| Cách mạng công nghiệp | 03:58-04:46 | 145-167 | ống khói, đồng hồ nhà máy khổng lồ, máy bấm thẻ giờ, giờ nghỉ, "Solution", di cư, "BREAK the FAST" | motif đồng hồ leo từ đồ trang trí thành công cụ kiểm soát, rồi payoff etymology trên nền tối |
| Tu sĩ và công nhân | 04:48-05:22 | 168-185 | tu sĩ cho bánh, tu sĩ từ chối bánh, bếp sáng và bếp đêm, thẻ "Dinner" ban đêm, "1850" | dùng một bàn tay chặn thay cho một câu giải thích |
| Kellogg và quảng cáo | 05:24-05:53 | 186-198 | mảnh ghép thiếu, bóng đen với dấu "?", Kellogg, biển quảng cáo, tờ rơi, nhà khoa học, ông chủ ký sổ, "It worked" | dựng một reveal danh tính bằng ba beat, và nêu động cơ tiền bằng đồ vật, không bằng lời |
| Sinh học | 05:54-06:56 | 199-233 | nền cobalt cho hai beat narrator, vòng tuần hoàn circadian, bốn thẻ khái niệm, gauge cortisol, cơ thể thành nhà máy, thụ thể ghrelin và leptin, "Not Passive" | nhịp tăng trở lại 33,0 beat mỗi phút nhờ mật độ chuỗi build cao nhất video |
| Thời điểm ăn | 06:59-07:33 | 234-251 | "When?", lưới 15 món với "2x" rồi "4x", đường tiêu hóa, mảnh ghép được lấp, gia đình thời đá, ba icon lợi ích xã hội | chuyển từ sinh học sang hành vi bằng một con số đổi trên cùng một lưới |
| Kết | 07:37-08:20 | 252-272 | "Historical Origin", câu hỏi tiêu đề nói đủ ở 07:44, recap năm frame, đống nguồn dẫn, người trong suốt rồi mặc áo, "Three Meals", hai frame hook trở lại | đóng vòng lặp bằng đúng hai frame đã mở nó |

## Vì sao phần kết hiệu quả

Phần kết dài 21 frame, 43 giây, và nó làm bốn việc theo thứ tự.

**Một, nói lại câu hỏi tiêu đề, đầy đủ, ở phút thứ tám.** Chữ "Why do we eat 3x a day?"
xuất hiện nguyên văn ở [frame 255](extracted-frames/frame-255_07m44.23s.jpg), tức ở 07:44
trên 08:25. Trước đó video chưa bao giờ viết ra cả câu. Nền cobalt xanh, narrator thời đá
tay chống má. Và ngay trước nó, [frame 253](extracted-frames/frame-253_07m38.33s.jpg) đóng
khung câu trả lời thành hai chữ: "Historical Origin". Câu hỏi và câu trả lời cách nhau đúng
2 beat.

**Hai, recap không tốn tài sản mới.** Năm frame liên tiếp, mỗi frame là một chương, đã mô tả
ở cơ chế 11. Người xem nhận được cảm giác "mình vừa đi qua nhiều thứ" mà video không phải
vẽ thêm gì.

**Ba, một frame cho bằng chứng, một frame cho cơ thể.**
[Frame 261](extracted-frames/frame-261_08m00.57s.jpg) vẽ toàn bộ nguồn dẫn thành một đống
vật thể: sách, cuộn giấy, bình cổ, mảnh cột, đồng tiền vàng, phiến đá có tranh hang động, có
vệt sáng vàng dưới đáy. Rồi
[frame 262](extracted-frames/frame-262_08m02.73s.jpg) và
[frame 263](extracted-frames/frame-263_08m04.47s.jpg) là một cặp: cùng một người đang đi
dạo, frame đầu nhìn thấu nội quan, frame sau nội quan tắt và anh ta mặc một cái áo xanh.
diff chỉ 4,22, và tool đánh dấu nó là "thay đổi thấp". Nhưng **cái tắt của lớp x-ray chính
là câu kết luận**: cơ thể vẫn ở đó, chỉ là bạn không nhìn thấy nó nữa.

**Bốn, đóng vòng bằng hai frame hook.** [Frame 271](extracted-frames/frame-271_08m19.37s.jpg)
và [frame 272](extracted-frames/frame-272_08m20.17s.jpg) là frame 5 và frame 6, nguyên xi.
Không chữ, không call to action trong khung. Video kết thúc ở chính nơi nó bắt đầu, và người
xem nhận ra điều đó mà không cần ai nói.

Một chi tiết nhỏ đáng học: [frame 269](extracted-frames/frame-269_08m16.13s.jpg) là hai
người thời đá cơ bắp cuồn cuộn, mặt nghiêm, trên nền cobalt. Đó là frame duy nhất trong 272
frame có vẽ cơ giải phẫu, và nó là một câu đùa. Đặt một beat hài ngay trước bốn beat đóng
vòng khiến phần kết không bị nặng.

## Những điểm không nên sao chép

### 1. Định dạng số không nhất quán, và đây là lỗi kiểm tra được

Video viết **"23.000 years ago"** ở [frame 27](extracted-frames/frame-027_00m30.30s.jpg) và
lặp lại **"23.000 years"** ở [frame 240](extracted-frames/frame-240_07m11.90s.jpg), dùng dấu
chấm làm dấu phân cách hàng nghìn. Nhưng ở
[frame 58](extracted-frames/frame-058_01m19.07s.jpg) video viết **"10,000 BCE"** với dấu
phẩy.

Hai quy ước ngược nhau, trong cùng một video, cho cùng một loại đại lượng. Theo quy ước
Anh Mỹ mà toàn bộ phần chữ còn lại của video dùng, thì "23.000" đọc là hai mươi ba phẩy
không, tức sai ba bậc độ lớn. Đây không phải chuyện thẩm mỹ, đây là một con số bị viết sai
hai lần và không ai bắt được. TossExplains phải chọn một quy ước và ghi nó vào rule file.

Con số **"140"** ở [frame 35](extracted-frames/frame-035_00m44.70s.jpg) thì đúng: Ohalo II
thực sự cho ra hơn 140 loài thực vật. Nhưng frame đó không có một chữ nguồn nào, chỉ có số
140 và các hạt rải quanh. Con số đúng mà không có nguồn trong khung vẫn là một con số người
xem phải tin không điều kiện.

### 2. Bản đồ dùng biên giới hiện đại cho một mốc 10.000 năm trước Công nguyên

[Frame 60](extracted-frames/frame-060_01m23.57s.jpg) đặt Lưỡi liềm Phì nhiêu lên một bản đồ
chính trị **hiện đại**, có TURKEY tô cam, và các nhãn SYRIA, IRAQ, IRAN, Black Sea,
Mediterranean Sea, Persian Gulf. Video không hề ghi chú rằng những đường biên đó ra đời sau
sự kiện đang kể khoảng mười hai nghìn năm. Đây là cách nhanh nhất để người xem định vị, và
cũng là cách nhanh nhất để họ nhớ sai. Nếu TossExplains dùng bản đồ cho một mốc tiền sử,
phải vẽ địa hình chứ không vẽ biên giới.

Vấn đề tương tự ở [frame 29](extracted-frames/frame-029_00m34.13s.jpg): "Israel" tô đỏ cam
với một mũi tên, cho một di chỉ 23.000 năm tuổi.

### 3. Chữ hoa chữ thường trôi dạt, không có hệ thống

Đếm trong cùng một video:

- ALL CAPS: "BREAD", "BEER" ở [frame 82](extracted-frames/frame-082_01m55.10s.jpg);
  "UNCIVILIZED" ở [frame 128](extracted-frames/frame-128_03m16.77s.jpg); "CORTISOL" ở
  [frame 212](extracted-frames/frame-212_06m17.73s.jpg); "DEIPNON" ở
  [frame 94](extracted-frames/frame-094_02m12.90s.jpg).
- chữ thường: "bread", "wine" ở [frame 92](extracted-frames/frame-092_02m08.53s.jpg);
  "practical" ở [frame 141](extracted-frames/frame-141_03m50.13s.jpg); "human" ở
  [frame 202](extracted-frames/frame-202_06m01.40s.jpg).
- Title Case: "Breakfast", "Lunch", "Dinner" ở
  [frame 264](extracted-frames/frame-264_08m06.83s.jpg).

Và một lỗi rõ ràng trong đúng một khung:
[frame 185](extracted-frames/frame-185_05m22.10s.jpg) ghi **"USA"** viết hoa cạnh
**"europe"** viết thường. Hai nhãn cùng loại, cùng khung, khác quy ước.

TossExplains đã có quy tắc rồi: bold ALL CAPS, đen là mặc định, đỏ dành cho nguy hiểm và
phủ định. Giữ đúng nó và bỏ qua sự trôi dạt này.

### 4. Frame bản đồ thế giới cộng ba dĩa nói mạnh hơn bằng chứng

[Frame 131](extracted-frames/frame-131_03m25.40s.jpg) đặt ba dĩa ăn hiện đại lên toàn bộ bản
đồ thế giới, hàm ý một thời gian biểu ba bữa phổ quát toàn cầu. Nhưng chính lập luận thực
dân của video, ở [frame 129](extracted-frames/frame-129_03m19.67s.jpg) với bốn mũi tên toả
từ châu Âu ra bốn lục địa, nói rằng lịch ba bữa là thứ được **áp đặt**, không phải thứ có
mặt khắp nơi. Hình phổ quát hóa đúng cái mà lời kể vừa nói là cục bộ. Đây là kiểu mâu thuẫn
mà một frame làm được vì hình đọc nhanh hơn lời.

### 5. Không thể sao chép phần render

Rất nhiều thứ trong video này đẹp và bị `.agents/rules/visual-style.md` cấm thẳng:

- **Không có nền trắng.** 272 trên 272 frame nằm trên nền màu ấm. TossExplains yêu cầu
  **55 tới 75 phần trăm nền trắng phẳng**, và đã có một dự án bị từ chối vì quá tối. Không
  được lấy bảng nền ấm này.
- **Gradient**: vệt sáng vàng dưới đống nguồn dẫn
  [frame 261](extracted-frames/frame-261_08m00.57s.jpg), quầng sáng quanh dĩa ăn sáng
  [frame 165](extracted-frames/frame-165_04m42.17s.jpg), đèn dầu
  [frame 180](extracted-frames/frame-180_05m10.60s.jpg), các starburst quảng cáo
  [frame 197](extracted-frames/frame-197_05m50.13s.jpg).
- **Bóng đổ**: mặt bằng lều
  [frame 33](extracted-frames/frame-033_00m40.80s.jpg), bóng mềm dưới gauge
  [frame 212](extracted-frames/frame-212_06m17.73s.jpg).
- **Texture**: giấy, gạch, vải, gỗ trong hầu hết cảnh nội thất, ví dụ
  [frame 41](extracted-frames/frame-041_00m54.23s.jpg) và
  [frame 136](extracted-frames/frame-136_03m37.80s.jpg).
- **Sepia**: [frame 194](extracted-frames/frame-194_05m44.77s.jpg) là một đoạn tông nâu rút
  màu, không tồn tại trong palette TossExplains.
- **Blur và depth of field**: frames 144, 153, 253.
- **Phối cảnh nội thất có chiều sâu**: [frame 163](extracted-frames/frame-163_04m39.57s.jpg)
  là một thị trấn vẽ theo phối cảnh đẳng trục.
- **Chữ vàng trên nền sáng**: frames 165 và 166. Điều này bị cấm dứt khoát, vì không đọc
  được, và dự án 2 đã mắc đúng lỗi này bốn lần.
- **Khối chữ 3D và radial burst comic**:
  [frame 188](extracted-frames/frame-188_05m28.60s.jpg) có một dấu "?" vàng viền xanh dày
  kiểu 3D trên một vụ nổ tia đỏ trắng. Đẹp, và nằm ngoài style lock.
- **Áo màu để phân biệt nhân vật**: frames 250 và 251 dùng màu áo để tách năm người bạn.
  TossExplains dùng **mã màu đầu** (đỏ là ngượng hoặc nóng, trắng là trung tính, xanh nhạt
  là buồn hoặc lạnh), không dùng màu áo.

## Cách áp dụng cho TossExplains

### Định nghĩa chế độ, trong phạm vi style lock

Video này có sáu chế độ trên nền ấm. TossExplains không sao chép nền ấm, nên dịch sang bốn
chế độ trên nền trắng:

| Chế độ | Định nghĩa trong style lock | Nhiệm vụ |
| --- | --- | --- |
| `WHITE` | nền trắng phẳng, một tới bốn vật thể, có thể có chữ ALL CAPS ở đỉnh khung | thẻ khái niệm, con số, diagram có nhãn, base plate cho chuỗi build |
| `SCENE` | nền trắng hoặc một khối màu duy nhất từ tone map, có nhân vật cast | công việc kể chuyện, cảm xúc trên mày và miệng |
| `NARR` | một thành viên cast một mình trên nền trắng, không đạo cụ | dấu ngắt câu, chuyển chương, câu hỏi trực tiếp |
| `SPLIT` | vạch chia đen dọc, trái tan `#C4965A` với cast tổ tiên, phải trắng với `@YOU` | gương ancient đối modern |

Chế độ `MAP` của video gốc **không** chuyển sang được cho các mốc tiền sử, xem lỗi số 2 ở
trên. Nếu cần bản đồ, dùng địa hình phẳng không biên giới, trên nền trắng.

### Mục tiêu nhịp đề xuất

Lấy từ số thật của video này, quy về khung 10 tới 14 phút của TossExplains:

| Đoạn | Beat mỗi phút | Giây mỗi beat | Ghi chú |
| --- | ---: | ---: | --- |
| Hook (0 tới 15 giây) | 60 tới 66 | 0,9 tới 1,0 | video gốc chạy 65,8. Nhét một chuỗi build vào ngay đây. |
| Hook mở rộng (15 tới 45 giây) | 44 tới 48 | 1,25 tới 1,4 | video gốc chạy 43,7 ở Luận đề |
| Psychology (35 phần trăm giữa) | 33 tới 39 | 1,55 tới 1,85 | tăng nhịp ở mỗi chuỗi build |
| Anthropology (30 phần trăm) | 28 tới 33 | 1,8 tới 2,2 | giảm nhịp, cảnh dày hơn |
| Modern mismatch và The Shift | 28 tới 33 | 1,8 tới 2,2 | video gốc chạy 29,3 ở Thời điểm ăn |
| Kết | 27 tới 30 | 2,0 tới 2,2 | chậm nhất, và đóng bằng frame của hook |

Trung bình toàn video: **30 tới 34 beat mỗi phút**. Một video 12 phút do đó cần khoảng
**360 tới 410 timestamp**, không phải 150.

Quy tắc phái sinh: **frame nào có nhiều chữ để đọc thì giữ lâu hơn.** Video gốc giữ hai
frame chữ dày nhất (frames 192 và 193) trong một đoạn chạy 2,41 giây mỗi beat, đoạn chậm
nhất video. Số beat trên 4 giây chỉ 6 lần trong 8 phút, nên không được để một hold nào vượt
4 giây trừ khi có chữ phải đọc.

### Bảy kỹ thuật áp dụng được ngay, không phá style lock

1. **Base plate cộng build từng bước.** Một nền trắng, giữ nguyên, thêm một vật thể mỗi
   timestamp. Chi phí render gần bằng không vì cùng một prompt chỉ khác danh sách vật thể.
   Dùng ba tới bốn bước, không hơn. Đây là cơ chế trung tâm và nó không cần một pixel nào
   nằm ngoài style lock.
2. **Chữ đè lên hình vừa dựng xong.** Sau khi build đủ, một timestamp cuối đè một chữ đỏ
   ALL CAPS lên chính hình đó. Đỏ vì đây luôn là một phán quyết hoặc một phủ định, đúng
   đúng quy tắc màu chữ hiện có.
3. **Một ký hiệu phủ định duy nhất, dùng lại.** Chọn dấu X đỏ vẽ tay, và chỉ dùng nó. Không
   xen thêm dấu gạch, dấu cấm, hay chữ "NO". Video gốc dùng đúng một ký hiệu 12 lần và người
   xem đọc được nó ngay lần đầu.
4. **Set rỗng rồi set có người.** Vẽ bàn, phòng thí nghiệm, vòng lửa mà không có ai, một
   timestamp. Rồi cùng bố cục đó với cast, timestamp sau. Hai beat, một prompt.
5. **Thêm một nhân vật vào một thẻ để biến nó thành câu hỏi.** Một diagram một mình là thông
   tin. Cùng diagram cộng `@YOU` với bong bóng "?" là một luận đề. Một beat.
6. **Một beat nền tối cho một reveal duy nhất trong cả video.** Video gốc dùng nền gần đen
   đúng một lần, cho cú etymology, và nó tạo ra cú chuyển lớn nhất phim. TossExplains không
   có nền đen trong tone map, nên phiên bản trong style lock là: **một frame duy nhất có
   chữ đỏ chiếm một phần ba khung trên nền trắng trống hoàn toàn, không vật thể nào khác.**
   Dùng đúng một lần mỗi video, cho câu chốt.
7. **Nguồn dẫn thành đồ vật.** Nhà nghiên cứu thành một thành viên cast có nhãn tên ALL CAPS
   (frame type 7 đã có sẵn trong `visual-style.md`). Nghiên cứu thành một quyển sách hoặc
   một số tạp chí vẽ trên nền trắng. Không bao giờ là một dòng citation nhỏ.

### Ba quy tắc scene nên bổ sung vào quy trình

- **Mọi motif quay lại phải đổi nghĩa.** Video gốc đưa motif ba dĩa quay lại bốn lần, và
  lần nào nghĩa cũng khác: chưa đặt tên, có tên, bị hỏi, phổ quát hóa, được dán nhãn, lành
  mạnh, kết luận. Nếu một motif quay lại mà không đổi nghĩa thì đó là lười, không phải
  callback.
- **Recap chỉ dùng frame đã có.** Trước phần kết, chạy bốn tới năm timestamp lấy lại nguyên
  văn prompt của một scene tiêu biểu mỗi chương, theo thứ tự. Đây là 5,5 phần trăm bộ frame
  làm với chi phí bằng không.
- **Frame đầu và frame cuối phải là cùng một prompt.** Video gốc đóng bằng đúng frame 5 và
  frame 6. TossExplains đã có quy tắc "câu cuối phản chiếu câu đầu" trong `channel-dna.md`.
  Áp dụng nó cho hình: timestamp cuối cùng dùng lại prompt của timestamp đầu tiên.

### Tỉ lệ đa dạng hình ảnh đề xuất

| Chế độ | Video gốc | Đề xuất cho TossExplains |
| --- | ---: | ---: |
| `WHITE` (thẻ, diagram, số) | 43,1 phần trăm | 45 tới 55 phần trăm |
| `SCENE` (kể chuyện) | 49,6 phần trăm | 35 tới 45 phần trăm |
| `NARR` (một cast trên nền trắng) | 4,7 phần trăm | 6 tới 10 phần trăm |
| `SPLIT` | 0,4 phần trăm | 3 tới 6 phần trăm |

Video gốc đếm được **121 lần đổi chế độ** trên 274 ứng viên, tức đổi register sau mỗi
**2,26 beat**. Đó là con số phải đạt: không được để bốn timestamp liên tiếp cùng một chế độ.

Về nền, giữ nguyên ngân sách trong `visual-style.md`, không dịch từ video này:

| Nền | Tỉ lệ |
| --- | ---: |
| trắng phẳng | 55 tới 75 phần trăm |
| tan `#C4965A` | tới 15 phần trăm |
| cam `#F5820D` | tới 10 phần trăm |
| xanh cỏ cộng trời xanh | tới 10 phần trăm |
| cobalt `#2D5FBF` | 5 tới 15 phần trăm, chỉ khi trong đầu ai đó |

## Checklist review cho mỗi video TossExplains tiếp theo

- [ ] Nhịp trung bình đạt 30 tới 34 beat mỗi phút. Video 12 phút có 360 tới 410 timestamp.
- [ ] 15 giây đầu có từ 14 beat trở lên.
- [ ] Hook chạy 60 beat mỗi phút hoặc nhanh hơn, và có ít nhất một chuỗi build trong 12 beat
      đầu.
- [ ] Có từ 4 tới 8 chuỗi build trên base plate, mỗi chuỗi 3 tới 4 bước.
- [ ] Mỗi chuỗi build kết thúc bằng một timestamp đè chữ đỏ ALL CAPS lên chính hình đó.
- [ ] Chỉ dùng một ký hiệu phủ định trong toàn video, và dùng nó ít nhất 6 lần.
- [ ] Có ít nhất 2 cặp set rỗng rồi set có người.
- [ ] Có đúng một timestamp dùng cú chốt nền trắng trống với chữ đỏ chiếm một phần ba khung.
- [ ] Không hold nào vượt 4 giây, trừ frame có chữ phải đọc.
- [ ] Không quá 3 timestamp liên tiếp cùng một chế độ. Đổi register sau mỗi 2 tới 3 beat.
- [ ] Nền trắng phẳng đạt 55 tới 75 phần trăm. Cobalt không vượt 15 phần trăm và chỉ dùng
      khi khung đang ở trong đầu ai đó.
- [ ] Chữ chỉ có đen và đỏ. Không một chữ vàng nào trên nền sáng.
- [ ] Mọi chữ trên khung là ALL CAPS. Không trôi dạt sang chữ thường hay Title Case.
- [ ] Mọi con số dùng một quy ước phân cách hàng nghìn duy nhất, và quy ước đó ghi trong
      artifact.
- [ ] Mỗi nhà nghiên cứu được nêu tên có một timestamp riêng, vẽ thành cast với nhãn tên.
- [ ] Mỗi motif quay lại phải đổi nghĩa so với lần trước.
- [ ] Có một recap 4 tới 5 timestamp trước phần kết, dùng lại prompt đã có.
- [ ] Timestamp cuối cùng dùng lại prompt của timestamp đầu tiên.
- [ ] Không bản đồ nào có biên giới quốc gia hiện đại cho một mốc tiền sử.
- [ ] Không gradient, không bóng đổ, không texture, không blur, không sepia, không chữ 3D.
- [ ] Bốn chuỗi verbatim trong `visual-style.md` khớp từng byte. Chạy `/check`.

## Thứ tự xem bộ frame

| Contact sheet | Frame | Timeline |
| --- | --- | --- |
| [01](contact-sheets/contact-sheet-01.jpg) | 001-024 | 00:00.00-00:28.00 |
| [02](contact-sheets/contact-sheet-02.jpg) | 025-048 | 00:28.03-01:04.07 |
| [03](contact-sheets/contact-sheet-03.jpg) | 049-072 | 01:05.70-01:43.47 |
| [04](contact-sheets/contact-sheet-04.jpg) | 073-096 | 01:44.53-02:16.03 |
| [05](contact-sheets/contact-sheet-05.jpg) | 097-120 | 02:16.97-03:00.33 |
| [06](contact-sheets/contact-sheet-06.jpg) | 121-144 | 03:02.17-03:56.60 |
| [07](contact-sheets/contact-sheet-07.jpg) | 145-168 | 03:58.17-04:48.60 |
| [08](contact-sheets/contact-sheet-08.jpg) | 169-192 | 04:49.97-05:40.53 |
| [09](contact-sheets/contact-sheet-09.jpg) | 193-216 | 05:42.23-06:25.97 |
| [10](contact-sheets/contact-sheet-10.jpg) | 217-240 | 06:28.40-07:11.90 |
| [11](contact-sheets/contact-sheet-11.jpg) | 241-264 | 07:13.97-08:06.83 |
| [12](contact-sheets/contact-sheet-12.jpg) | 265-272 | 08:11.63-08:20.17 |
