# Chiến lược SEO 6 tháng — vuabaoho.com

Lập ngày 17/10/2026. Thời gian: **19/10/2026 → 18/04/2027** (26 tuần, kết thúc đúng lúc vào mùa áo điều hòa 2027).

Đi kèm:
- `seo/tu-khoa-muc-tieu.md`: bản đồ từ khóa, mỗi từ khóa gắn với đúng một trang.
- `seo/dia-phuong-mau.md`: bộ mẫu SEO địa phương, dùng lại mỗi khi mở cửa hàng ở tỉnh mới.
- `seo/chien-luoc.md` và `seo/ke-hoach-noi-dung.md`: phần lịch viết bài tự động hằng ngày, đã chỉnh theo chiến lược này.

---

## 1. Mục tiêu và kỳ vọng thực tế

Bốn ngành cần lên top:

| # | Ngành | Khách chính | Mục tiêu 6 tháng | Khả năng đạt |
|---|---|---|---|---|
| 1 | Áo điều hòa | Doanh nghiệp | Top 3 cho nhóm "áo điều hòa cho công nhân / doanh nghiệp"; top 5 "áo điều hòa" khi vào mùa (tháng 4/2027) | Trung bình – khá. Đã có nền 539 bài, nhưng đối thủ có web chính hãng (yamako.vn, kenkovn.com) và Shopee |
| 2 | Đồ bảo hộ lao động (đủ loại) | Doanh nghiệp | Top 10 cho ít nhất một nửa trong 30 từ khóa doanh nghiệp; top 3 cho các từ khóa dài ("đồ bảo hộ cho công nhân xây dựng"…) | Trung bình. Hiện danh mục gần như trống sản phẩm, phải làm từ đầu |
| 3 | Giày bảo hộ | Lẻ + doanh nghiệp | Top 10 "giày bảo hộ", "giày bảo hộ lao động"; top 5 cho ít nhất 10 từ khóa phụ (Jogger, siêu nhẹ, chống tĩnh điện…) | Khá. Có hàng thật, có cửa hàng, có 48 bài nền |
| 4 | Đồ bảo hộ tại địa phương | Doanh nghiệp + khách lẻ trong tỉnh | **Top 3 Google Maps và top 1–3 kết quả tìm kiếm** cho "đồ bảo hộ lao động / giày bảo hộ / áo điều hòa + Nam Định / Nghệ An / Vinh" | **Cao.** Đối thủ địa phương rất yếu: kết quả hiện chủ yếu là trang danh bạ |

**Nói thẳng với anh:** top 1 toàn quốc cho các từ khóa gốc ("áo điều hòa", "giày bảo hộ", "đồ bảo hộ lao động") trong 6 tháng thì không ai cam kết được. Những từ này thường mất 9–18 tháng và cần nhiều liên kết từ web khác. Cái làm được chắc chắn trong 6 tháng: **thắng hẳn ở địa phương**, thắng phần lớn từ khóa doanh nghiệp dài, và đưa từ khóa gốc vào top 10 rồi leo dần.

Các con số mục tiêu trên sẽ chốt lại ở **tuần 2**, khi có số liệu Search Console cho biết hiện mỗi từ khóa đang đứng thứ mấy.

---

## 2. Hiện trạng: 8 điểm nghẽn (kiểm tra ngày 17/10/2026)

| # | Điểm nghẽn | Bằng chứng | Hậu quả |
|---|---|---|---|
| 1 | **Trang bán hàng chính (trang danh mục) gần như trống chữ** | Trang `/ao-dieu-hoa` có tiêu đề "Áo điều hoà", mô tả "Áo điều hoà", không có đoạn giới thiệu nào. Các danh mục khác cũng không có mô tả SEO | Google không có gì để hiểu trang này đáng xếp trên đối thủ. Từ khóa mua hàng ("áo điều hòa", "giày bảo hộ") Google ưu tiên trang danh mục, không ưu tiên bài blog |
| 2 | **Không có danh mục "Giày bảo hộ lao động"** | `/giay-bao-ho` và `/giay-bao-ho-lao-dong` báo lỗi 404. Giày chỉ nằm theo hãng (`/safety-jogger`, `/fiv-out`), trong đó `/fiv-out` lẫn cả giày thể thao | Không có trang nào để lên top cho từ khóa lớn nhất của ngành 3 |
| 3 | **96% sản phẩm đang ẩn** | 2.966 sản phẩm, chỉ 124 hiển thị. Ẩn 429 quần áo bảo hộ, 372 giày bảo hộ. Danh mục găng tay, mũ bảo hộ, quần áo bảo hộ hiện **0 sản phẩm**; ủng chỉ 1 | Ngành 2 không có gì để bán trên web. Nguyên nhân: mỗi size đang là một sản phẩm riêng |
| 4 | **Blog tự cạnh tranh với chính mình** | 539/728 bài là áo điều hòa: 33 bài kiểu "mua ở đâu", 32 bài về giá, 46 bài về pin, 61 bài về cách dùng. Riêng "mua áo điều hòa tại Nam Định" có ít nhất 5 bài | Google không biết trang nào là trang chính, nên chia nhỏ thứ hạng cho nhiều bài, không bài nào lên top. Vài bài còn nhắc "Yamako.vn" thay vì Vua Bảo Hộ |
| 5 | **Lỗi kỹ thuật trên mọi trang** | Dòng chữ lỗi "Lỗi liquid: The input string '2.333…' was not in a correct format" hiện trong mã trang ở mọi trang đã kiểm tra. Trang sản phẩm **không có schema Product** (giá, còn hàng). Schema NewsArticle của bài viết lỗi JSON | Google không hiện giá, tình trạng hàng trên kết quả tìm kiếm; trang bị đánh giá kém chất lượng |
| 6 | **Thông tin doanh nghiệp không thống nhất** | Chân trang ghi "Công ty Cổ Phần Vua Bảo Hộ", địa chỉ cũ "202 Điện Biên, P.Cửa Bắc, TP.Nam Định", **không có cửa hàng Nghệ An**. Trang "Về Vua Bảo Hộ" ghi "Công ty TNHH". Cài đặt Sapo ghi 405 Trần Thái Tông | Google Maps và Google Search cần tên, địa chỉ, số điện thoại giống hệt nhau ở mọi nơi mới tin tưởng; đây là gốc của SEO địa phương |
| 7 | **Chưa có trang riêng cho doanh nghiệp và cho từng tỉnh** | Không có trang báo giá doanh nghiệp, không có trang cửa hàng Nam Định / Nghệ An. Chỉ có bài blog rải rác | Khách doanh nghiệp không có chỗ để gửi yêu cầu báo giá; từ khóa địa phương không có trang đích |
| 8 | **Trang sản phẩm mỏng và trùng nhau** | Ví dụ giày Fiv Out PantherX đang hiện thành 4 trang theo size S39–S42 với nội dung y hệt. Tiêu đề sản phẩm không có mô tả SEO riêng; mô tả là bảng thông số của nhà nhập khẩu | Nội dung trùng lặp, Google bỏ qua |

Điểm mạnh để tận dụng: có cửa hàng thật ở 2 tỉnh, có hàng chính hãng (Safety Jogger, Yamako, Fiv Out), web đã có tuổi và hơn 700 bài, đối thủ địa phương yếu.

---

## 3. Năm nguyên tắc của chiến lược

1. **Trang bán hàng trước, blog sau.** Từ khóa mua hàng phải lên top bằng trang danh mục và trang đích. Blog chỉ trả lời câu hỏi và dẫn link về trang bán hàng.
2. **Mỗi từ khóa chỉ một trang.** Bản đồ ở `seo/tu-khoa-muc-tieu.md` là sổ đăng ký: từ khóa đã giao cho trang nào thì không trang nào khác được nhắm vào. Bài cũ trùng ý thì gộp về một trang và chuyển hướng 301.
3. **Doanh nghiệp cần trang giải pháp, không cần bài quảng cáo.** Phòng mua hàng và cán bộ an toàn tìm: quy định, danh sách theo ngành, chi phí, báo giá. Mỗi trang dẫn tới trang báo giá và hotline.
4. **Địa phương = Google Maps + trang tỉnh + đánh giá thật.** Ba thứ này làm theo một mẫu cố định để mở tỉnh nào cũng nhân bản được ngay (`seo/dia-phuong-mau.md`).
5. **Đi trước mùa ba tháng.** Áo điều hòa bán từ tháng 3 thì trang và nội dung phải xong trước giữa tháng 1, để Google kịp xếp hạng ổn định.

---

## 4. Kiến trúc website mới

Mỗi ngành là một "cụm": một trang chính ở trên, các trang con và bài blog bên dưới cùng trỏ link về trang chính.

```
Trang chủ
├── Áo điều hòa ............ /ao-dieu-hoa (danh mục, viết lại thành trang trụ cột)
│   ├── /ao-dieu-hoa-cho-doanh-nghiep (trang đích doanh nghiệp, MỚI)
│   ├── /phu-kien-ao-quat-dieu-hoa (pin, quạt)
│   ├── /bang-gia-ao-dieu-hoa (một trang giá duy nhất, cập nhật mỗi mùa)
│   └── 60–80 bài blog giữ lại sau khi gộp
├── Đồ bảo hộ lao động ..... /do-bao-ho-lao-dong (danh mục tổng, MỚI)
│   ├── /quan-ao-bao-ho-lao-dong-1, /mu-bao-ho-lao-dong, /gang-tay-bao-ho-lao-dong,
│   │   /ung-bao-ho-lao-dong (MỚI), /kinh-bao-ho-lao-dong, /bao-ho-lao-dong-khac
│   ├── /bao-gia-do-bao-ho-lao-dong (trang báo giá doanh nghiệp, MỚI)
│   ├── /dat-may-quan-ao-bao-ho-lao-dong-cho-doanh-nghiep (đồng phục in logo, đã có)
│   └── Bài giải pháp theo ngành: xây dựng, may mặc, cơ khí, điện tử, kho vận, thực phẩm
├── Giày bảo hộ ............ /giay-bao-ho-lao-dong (danh mục tổng, MỚI)
│   ├── Theo hãng: /safety-jogger, /giay-bhld-fiv-out
│   ├── Theo tính năng (tạo khi có từ 4 mẫu đang hiện): siêu nhẹ, chống tĩnh điện,
│   │   cách điện, cao cổ, giày nữ
│   └── Bài blog: ký hiệu, size, so sánh, đánh giá từng mẫu
└── Cửa hàng theo tỉnh
    ├── /bao-ho-lao-dong-nam-dinh, /giay-bao-ho-nam-dinh, /ao-dieu-hoa-nam-dinh (MỚI)
    ├── /bao-ho-lao-dong-nghe-an,  /giay-bao-ho-nghe-an,  /ao-dieu-hoa-nghe-an (MỚI)
    └── Tỉnh mới: nhân bản theo seo/dia-phuong-mau.md
```

Menu chính và chân trang phải có đủ 4 cụm này. Chân trang ghi đủ cả hai cửa hàng.

### Mẫu nội dung cho trang danh mục (áp dụng cho mọi danh mục)

- **Tiêu đề SEO** (dưới 60 ký tự): từ khóa chính + điểm khác biệt có thật + "| Vua Bảo Hộ". Ví dụ: "Giày bảo hộ lao động Jogger, Fiv Out chính hãng | Vua Bảo Hộ".
- **Mô tả SEO** (140–160 ký tự): có từ khóa, nói rõ có gì, mua ở đâu, hotline 1900.3385.
- **Đoạn đầu trên lưới sản phẩm** (80–150 chữ): trả lời ngay "ở đây bán gì, cho ai, chọn thế nào".
- **Phần dưới lưới sản phẩm** (600–1.200 chữ, có nút "xem thêm"): cách chọn theo công việc, bảng so sánh, tiêu chuẩn kỹ thuật, dịch vụ cho doanh nghiệp (báo giá, xuất hóa đơn nếu có), hai cửa hàng, 4–6 câu hỏi thường gặp.
- Link tới 3–5 bài blog hay nhất của cụm và tới trang báo giá.

---

## 5. Chiến lược cho từng ngành

### Ngành 1 — Áo điều hòa (ưu tiên số 1, khách doanh nghiệp)

Vấn đề không phải thiếu bài mà là **thừa bài và thiếu trang chính**. Việc cần làm:

1. **Viết lại `/ao-dieu-hoa` thành trang trụ cột** theo mẫu danh mục ở trên: cách chọn (quạt, pin, vải, kiểu áo), bảng so sánh các dòng đang bán, phần "mua cho công nhân", câu hỏi thường gặp.
2. **Tạo trang `/ao-dieu-hoa-cho-doanh-nghiep`**: giải pháp chống nóng cho công nhân, tính số lượng áo và pin dự phòng theo ca, quy trình đặt hàng, mẫu yêu cầu báo giá, nút gọi và Zalo. Nếu VBH có in logo lên áo điều hòa thì có thêm phần này (chờ anh xác nhận).
3. **Gộp bài trùng** (làm theo đợt, có anh duyệt danh sách):
   - Dùng số liệu Search Console 16 tháng: bài có lượt nhấp thì giữ và cập nhật; bài không có lượt nhấp và trùng ý với bài khác thì gộp nội dung tốt vào bài giữ lại, rồi chuyển hướng 301 (Sapo có sẵn chức năng chuyển hướng, web đang có 141 chuyển hướng).
   - Dự kiến từ 539 bài còn khoảng 60–80 bài mạnh, chia theo chủ đề: cách chọn, pin và quạt, bảo quản, theo đối tượng (công nhân, shipper, nông dân…), so sánh, giá.
   - Ví dụ: 5 bài "mua áo điều hòa tại Nam Định" gộp về trang `/ao-dieu-hoa-nam-dinh`; 32 bài về giá gộp về `/bang-gia-ao-dieu-hoa`.
   - Gộp trong tháng 11–12 để Google ổn định trước tháng 3.
4. **Bài mới chỉ viết góc doanh nghiệp** (chưa có bài nào): chống nóng cho người lao động theo quy định, chi phí trang bị cho 50–100 công nhân, quản lý sạc pin cho cả xưởng, sơ cứu say nắng ở công trường. Đã đưa vào kế hoạch bài tự động.
5. **Hàng mẫu 2027 lên web trước 15/02/2027**, có ảnh thật và thông số đầy đủ.

Câu hỏi quan trọng cho anh: **yamako.vn có phải web của anh không?** Một số bài trên vuabaoho.com nhắc "Yamako.vn". Nếu cùng chủ, hai web đang tranh nhau từ khóa "áo điều hòa" và cần chia vai trò (ví dụ yamako.vn giữ từ khóa thương hiệu Yamako, vuabaoho.com giữ từ khóa doanh nghiệp và địa phương).

### Ngành 2 — Đồ bảo hộ lao động cho doanh nghiệp

Muốn lên top thì trước hết **trên web phải có hàng**.

1. **Hiển thị sản phẩm** theo thứ tự: giày (tuần 1–4), quần áo bảo hộ, mũ, găng tay, ủng, áo phản quang (tuần 5–10). Mỗi mẫu gộp thành **một sản phẩm có nhiều size** (biến thể), trang size cũ chuyển hướng về trang gộp. Đây là việc nhập liệu lớn nhất của kế hoạch, cần 1 người làm 2–3 tuần.
2. **Tạo danh mục tổng `/do-bao-ho-lao-dong`** và viết mô tả cho từng danh mục con theo mẫu.
3. **Trang `/bao-gia-do-bao-ho-lao-dong`**: doanh nghiệp gửi danh sách cần mua, VBH báo giá. Có các phần: nhóm hàng cung cấp, quy trình (gửi yêu cầu → tư vấn → mẫu thử → báo giá → giao hàng), hai cửa hàng, mẫu form hoặc nút Zalo/hotline. Không ghi cam kết chưa có thật (thời gian giao, số lượng tối thiểu, chiết khấu).
4. **Bài giải pháp theo ngành**: xây dựng, may mặc (Nam Định là vùng dệt may), cơ khí, điện tử, kho vận, thực phẩm. Mỗi bài có danh sách đồ bảo hộ theo vị trí, liên kết tới danh mục và trang báo giá.
5. **Bài quy định**: trang cấp phương tiện bảo vệ cá nhân (Thông tư 25/2022, đã viết), quy trình cấp phát, mẫu biên bản cấp phát, kế hoạch an toàn vệ sinh lao động. Đây là nhóm Gemini, ChatGPT hay trích dẫn khi doanh nghiệp hỏi.

### Ngành 3 — Giày bảo hộ

1. **Tạo danh mục `/giay-bao-ho-lao-dong`** chứa mọi giày và ủng bảo hộ đang hiện (khoảng 30 mẫu hiện nay, tăng dần khi hiện thêm hàng). Đây là trang để lên top "giày bảo hộ", "giày bảo hộ lao động".
2. **Tách `/fiv-out`**: giày bảo hộ Fiv Out về `/giay-bhld-fiv-out`, giày thể thao để riêng.
3. **Danh mục theo tính năng** (tạo bằng danh mục tự động theo thẻ, chỉ khi đủ 4 mẫu trở lên): siêu nhẹ, chống tĩnh điện ESD, cách điện, cao cổ, giày nữ.
4. **Nâng cấp trang sản phẩm giày**: gộp size, tiêu đề SEO dạng "Giày bảo hộ Jogger Cador S1P chính hãng | Vua Bảo Hộ", mô tả tự viết (không chép nguyên bảng của nhà nhập khẩu), bảng size, ký hiệu tiêu chuẩn, ảnh chụp thật tại cửa hàng, video ngắn nếu có.
5. **Tận dụng cửa hàng thật**: trang `/giay-bao-ho-nam-dinh` và `/giay-bao-ho-nghe-an` ghi rõ "có sẵn để thử tại cửa hàng", ảnh kệ giày thật. Google Maps của hai cửa hàng đăng sản phẩm giày.
6. **Gộp trang trùng**: hai trang `/giay-bao-ho-nhap-khau-jogger` và `/dai-ly-giay-bao-ho-nhap-khau-jogger-chinh-hang` trùng ý với `/safety-jogger`, đề xuất gộp nội dung vào danh mục và chuyển hướng.

### Ngành 4 — Đồ bảo hộ tại địa phương (thắng nhanh nhất)

Làm theo `seo/dia-phuong-mau.md` cho Nam Định và Nghệ An ngay trong tháng đầu:

1. **Google Business Profile** cho mỗi cửa hàng: xác minh, đúng tên "Vua Bảo Hộ Nam Định" / "Vua Bảo Hộ Nghệ An" (đúng như biển hiệu), danh mục chính, giờ mở cửa, 30+ ảnh thật, sản phẩm, bài đăng hằng tuần.
2. **Đánh giá thật từ khách**: mã QR ở quầy, nhân viên xin đánh giá sau mỗi đơn. Mục tiêu 30 đánh giá mới mỗi cửa hàng trong 2 tháng. Không tặng quà đổi đánh giá, không tự viết đánh giá (Google cấm và có thể khóa hồ sơ).
3. **Ba trang cho mỗi tỉnh**: bảo hộ lao động, giày bảo hộ, áo điều hòa (trang áo điều hòa làm trước mùa, gộp các bài cũ cùng tỉnh).
4. **Thông tin giống hệt nhau** trên web, Google Maps, Facebook, Zalo, các trang danh bạ.
5. **Tên địa danh cũ và mới**: từ 01/07/2025 Nam Định thuộc tỉnh Ninh Bình, nhưng người mua vẫn gõ "Nam Định", "Vinh". Trang phải có cả hai: "Nam Định (tỉnh Ninh Bình)", "Vinh (phường Thành Vinh, Nghệ An)".
6. **Vùng lân cận** (sau tháng 3, chỉ khi VBH thật sự giao hàng và phục vụ ở đó): Hà Tĩnh, Thanh Hóa cho cửa hàng Nghệ An; Hà Nam, Thái Bình cũ cho cửa hàng Nam Định. Không tạo hồ sơ Google Maps ở nơi không có cửa hàng.

---

## 6. Sửa kỹ thuật (cần người sửa giao diện Sapo)

Nhờ bộ phận hỗ trợ Sapo hoặc thuê một lập trình viên giao diện Sapo. Thứ tự ưu tiên:

| # | Việc | Mức độ |
|---|---|---|
| 1 | Sửa lỗi Liquid hiện trên mọi trang | Gấp |
| 2 | Chân trang: đúng tên công ty, địa chỉ mới, đủ hai cửa hàng và số điện thoại | Gấp |
| 3 | Thêm schema Product cho trang sản phẩm (tên, ảnh, giá, còn hàng, thương hiệu) | Gấp |
| 4 | Giao diện danh mục hiện được phần mô tả trên và dưới lưới sản phẩm | Gấp |
| 5 | Sửa lỗi JSON của schema NewsArticle | Cao |
| 6 | Thêm schema LocalBusiness cho hai cửa hàng (trang liên hệ và trang tỉnh) | Cao |
| 7 | H1 trang chủ ngắn lại, chỉ một câu | Trung bình |
| 8 | Mẫu tiêu đề và mô tả SEO tự động cho sản phẩm chưa điền | Trung bình |
| 9 | Kiểm tra tốc độ trên điện thoại (PageSpeed Insights); trang chủ đang nặng 435 KB mã HTML | Trung bình |
| 10 | Gộp hai trang giới thiệu (`/gioi-thieu`, `/ve-vua-bao-ho`), sửa mô tả "Đây là trang giới thiệu." | Thấp |

Việc anh tự làm được: cập nhật địa chỉ trong Cài đặt Sapo, kết nối Google Search Console và Bing Webmaster Tools, gửi sitemap `https://vuabaoho.com/sitemap.xml`.

---

## 7. Uy tín và liên kết từ web khác

Từ khóa gốc toàn quốc cần web khác trỏ link về. Chỉ làm các nguồn thật:

1. **Hãng và nhà phân phối**: xin đưa tên và link Vua Bảo Hộ vào danh sách đại lý của Safety Jogger Việt Nam, Yamako, Fiv Out.
2. **Báo địa phương**: bài về hoạt động có thật, ví dụ khai trương, hoặc tặng áo điều hòa cho công nhân vệ sinh môi trường mùa nắng. Vừa có link, vừa có tiếng ở tỉnh.
3. **Hiệp hội và khu công nghiệp**: hội doanh nghiệp tỉnh, ban quản lý khu công nghiệp (danh bạ nhà cung cấp, hội viên).
4. **Khách doanh nghiệp**: xin phép đưa câu chuyện cung cấp hàng lên web (có sự đồng ý), đổi lại họ ghi nhà cung cấp.
5. **Danh bạ**: Trang Vàng Việt Nam, Yellow Pages, Bing Places, Apple Maps, Cốc Cốc, Zalo OA, Facebook.
6. **Video**: kênh YouTube và TikTok có video thử giày, áo, mô tả kèm link về trang sản phẩm; nhúng video vào trang sản phẩm.

Không mua link hàng loạt, không dùng mạng web vệ tinh, không spam bình luận. Google phạt những kiểu này.

---

## 8. Lộ trình 26 tuần

### Giai đoạn 1 — Nền móng và thắng nhanh địa phương (tuần 1–4: 19/10 → 15/11/2026)

- [ ] Kết nối Google Search Console, Bing Webmaster; gửi sitemap. Lấy số liệu 16 tháng, chốt thứ hạng hiện tại của 40 từ khóa chính.
- [ ] Sửa kỹ thuật mục 1–4 (lỗi Liquid, chân trang, schema Product, hiện mô tả danh mục).
- [ ] Google Business Profile hai cửa hàng: xác minh, điền đủ, 30 ảnh, bắt đầu xin đánh giá.
- [ ] Tạo danh mục `/giay-bao-ho-lao-dong`; viết mô tả và SEO cho 9 danh mục: áo điều hòa, giày bảo hộ, Safety Jogger, Fiv Out bảo hộ, kính, mũ, găng tay, quần áo bảo hộ, áo sưởi.
- [ ] Trang tỉnh: `/bao-ho-lao-dong-nam-dinh`, `/bao-ho-lao-dong-nghe-an`, `/giay-bao-ho-nam-dinh`, `/giay-bao-ho-nghe-an`.
- [ ] Trang `/bao-gia-do-bao-ho-lao-dong`.
- [ ] Gộp size và hiển thị giày bảo hộ.
- [ ] Blog tự động: giày, doanh nghiệp, chống rét (theo `seo/ke-hoach-noi-dung.md`).

### Giai đoạn 2 — Trang bán hàng đầy đủ, dọn áo điều hòa (tuần 5–12: 16/11/2026 → 10/01/2027)

- [ ] Hiển thị quần áo bảo hộ, mũ, găng tay, ủng (gộp size). Tạo `/do-bao-ho-lao-dong`, `/ung-bao-ho-lao-dong`.
- [ ] Danh mục giày theo tính năng (khi đủ hàng).
- [ ] Áo điều hòa: duyệt danh sách gộp bài, chuyển hướng theo đợt 50 bài/tuần, theo dõi Search Console sau mỗi đợt. Viết lại `/ao-dieu-hoa`. Tạo `/ao-dieu-hoa-cho-doanh-nghiep`.
- [ ] Sửa kỹ thuật mục 5–8.
- [ ] Đưa thông tin lên 10–15 trang danh bạ. Mỗi cửa hàng có thêm 30 đánh giá.
- [ ] Liên kết đợt 1: hãng và nhà phân phối, hội doanh nghiệp tỉnh.
- [ ] Blog: quà Tết cho công nhân (doanh nghiệp mua tháng 12), bài giải pháp theo ngành, bài quy định.

### Giai đoạn 3 — Chuẩn bị mùa áo điều hòa 2027 (tuần 13–20: 11/01 → 07/03/2027)

- [ ] Hàng mẫu 2027 lên web trước 15/02, có ảnh thật. Cập nhật `/bang-gia-ao-dieu-hoa`.
- [ ] Trang `/ao-dieu-hoa-nam-dinh`, `/ao-dieu-hoa-nghe-an` (gộp bài cũ cùng tỉnh).
- [ ] Bài áo điều hòa góc doanh nghiệp (chống nóng theo quy định, chi phí, quản lý pin, sơ cứu say nắng).
- [ ] 2–4 bài báo địa phương; video sản phẩm.
- [ ] Nghỉ Tết (đầu tháng 2/2027): lịch tự động vẫn chạy; Google Maps đăng lịch nghỉ Tết.

### Giai đoạn 4 — Tăng tốc mùa hè và đóng gói mẫu tỉnh mới (tuần 21–26: 08/03 → 18/04/2027)

- [ ] Mỗi tuần chọn các trang đang đứng thứ 4–15 trên Google, bổ sung nội dung, thêm link nội bộ để đẩy lên top 3.
- [ ] Bài đăng Google Maps 2 lần/tuần cho áo điều hòa.
- [ ] Hoàn thiện `seo/dia-phuong-mau.md` từ kinh nghiệm thật của hai tỉnh, sẵn sàng cho tỉnh mới.
- [ ] Tổng kết 6 tháng, lập kế hoạch 6 tháng tiếp theo.

---

## 9. Ai làm gì

| Người | Việc | Thời gian |
|---|---|---|
| **Claude (lịch tự động)** | Mỗi sáng 7h50 viết và đăng một bài blog theo kế hoạch | Hằng ngày |
| **Claude (khi anh nhờ)** | Viết nội dung danh mục, trang tỉnh, trang doanh nghiệp, trang sản phẩm (để ẩn chờ anh duyệt); lập danh sách gộp bài áo điều hòa; báo cáo Search Console hằng tuần | Theo từng phiên |
| **Anh Luận** | Duyệt nội dung, trả lời các câu hỏi ở mục 11, quyết ngân sách, kết nối Search Console | 30 phút/tuần |
| **Cửa hàng trưởng hai tỉnh** | Google Maps (ảnh, bài đăng, trả lời đánh giá), xin đánh giá khách, chụp ảnh hàng thật mỗi tháng | 3–4 giờ/tuần mỗi người |
| **1 nhân viên nhập liệu** | Gộp size, hiển thị sản phẩm, điền tiêu đề và mô tả SEO sản phẩm theo nội dung Claude soạn | 2–3 tuần làm chính, sau đó vài giờ/tuần |
| **Thuê ngoài / hỗ trợ Sapo** | Sửa giao diện (mục 6) | Một lần, trong tháng đầu |

---

## 10. Đo lường

- **Google Search Console** (bắt buộc): số lần hiển thị, lượt nhấp, vị trí trung bình theo từ khóa và theo trang. Để em đọc được và báo cáo tự động: mỗi thứ Hai xuất báo cáo Search Console sang Google Trang tính trong Google Drive (em đọc được Drive), hoặc cấp quyền xem cho em theo cách anh muốn.
- **Theo dõi 40 từ khóa chính** mỗi tuần (danh sách P1 trong `seo/tu-khoa-muc-tieu.md`).
- **Google Business Profile**: lượt gọi, lượt chỉ đường, lượt xem, số đánh giá và điểm trung bình.
- **Khách doanh nghiệp**: số yêu cầu báo giá từ web, Zalo, hotline. Nhân viên hỏi khách "anh chị biết Vua Bảo Hộ qua đâu" và ghi lại.

| Mốc | Phải đạt |
|---|---|
| Hết tháng 1 (15/11) | Search Console chạy; hết lỗi Liquid; chân trang đúng; 9 danh mục có nội dung; 4 trang tỉnh và trang báo giá đã hiện; giày đã gộp size; hai hồ sơ Google Maps đã xác minh |
| Hết tháng 2 (15/12) | Top 3 cho từ khóa địa phương chính; danh mục quần áo, mũ, găng tay có hàng; danh sách gộp bài áo điều hòa đã duyệt |
| Hết tháng 3 (10/01) | Gộp bài áo điều hòa xong; trang doanh nghiệp áo điều hòa đã hiện; 60 đánh giá Google mỗi cửa hàng (tính cả cũ) |
| Hết tháng 4 (07/02) | Hàng 2027 trên web; mục tiêu ngành 3 và ngành 4 đạt |
| Hết tháng 6 (18/04) | Đánh giá theo bảng mục tiêu ở mục 1 |

---

## 11. Cần anh trả lời để làm tiếp

1. **yamako.vn có phải web của anh không?** (quyết định cách chia từ khóa áo điều hòa giữa hai web)
2. **Tên pháp lý đúng là Công ty TNHH hay Công ty Cổ phần Vua Bảo Hộ?** Chân trang và trang giới thiệu đang ghi khác nhau.
3. **VBH có in hoặc thêu logo lên áo điều hòa không?** Có số lượng tối thiểu không? (để viết trang doanh nghiệp, không ghi khi chưa xác nhận)
4. **Anh đồng ý gộp bài áo điều hòa trùng và chuyển hướng 301 không?** Em sẽ lập danh sách cho anh duyệt trước, làm theo đợt, có thể hoàn tác bằng cách xóa chuyển hướng.
5. **Hai cửa hàng đã có hồ sơ Google Maps chưa, ai đang giữ tài khoản?**
6. **Ai làm phần nhập liệu sản phẩm và ai sửa giao diện?** Có ngân sách thuê ngoài và làm bài báo địa phương không?
7. **VBH có bán dây an toàn, mặt nạ phòng độc, quần áo chống hóa chất không?** Để quyết có tạo danh mục cho các nhóm này.
