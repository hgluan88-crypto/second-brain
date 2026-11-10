---
name: dang-bai-seo
description: Viết và đăng một bài blog chuẩn SEO lên vuabaoho.com (Sapo) theo kế hoạch nội dung của Vua Bảo Hộ, có ảnh thật, được duyệt trước khi đăng. Dùng cho lịch đăng bài tự động hằng ngày, hoặc khi anh Luận nhờ viết, đăng hay sửa một bài SEO trên website.
---

# Đăng một bài SEO lên vuabaoho.com

Quy trình có **hai lượt mỗi ngày**:
- **Lượt 7h50** (Bước 0–9): viết đúng một bài, duyệt, tạo bài ẩn, đánh dấu chờ đăng nếu đạt, ghi vào Google Sheet, báo cáo. Không đăng.
- **Lượt khoảng 14h** (Bước 10–11): đăng các bài đã đạt, trừ bài anh ghi "Không đăng" trong sheet; cập nhật sheet; báo cáo.

Chất lượng hơn số lượng. Làm lần lượt từng bước. Không bỏ bước duyệt và bước kiểm tra.

Đọc trước: `CLAUDE.md` (thông tin doanh nghiệp, quy tắc), `seo/chien-luoc.md`, `seo/ke-hoach-noi-dung.md`, `seo/tu-khoa-muc-tieu.md`, `seo/tieu-chi-duyet-bai.md`.

Công cụ: `python3 seo/scripts/sapo.py <lệnh>` (chạy `--help` để xem lệnh). Mã API Sapo do proxy tự gắn, không cần và không được ghi mã vào đâu. Làm việc trong một thư mục tạm, ví dụ `W=$(mktemp -d)`; không ghi file bài viết vào repo, không commit.

## Bước 0. Chuẩn bị

1. Đang đứng ở thư mục gốc repo `second-brain`. Nếu phiên chưa có repo: `git clone https://github.com/hgluan88-crypto/second-brain.git && cd second-brain`.
2. `python3 -c "import PIL" || pip install -q pillow`
3. `python3 seo/scripts/sapo.py count-auto` để chạy thử kết nối. Lỗi kết nối hoặc 401/403 thì dừng, báo lỗi trong báo cáo cuối (bước 9).

## Bước 1. Chọn chủ đề

1. Đi từ trên xuống bảng trong `seo/ke-hoach-noi-dung.md`. Với mỗi dòng chạy `sapo.py alias-exists <đường dẫn>`: "CÓ" thì bỏ qua; "CHƯA CÓ" thì chọn dòng đó.
2. Chống trùng: `sapo.py search-articles <2–4 từ khóa của chủ đề>`. Nếu có bài cũ cùng ý định tìm kiếm (người tìm sẽ thấy hai bài trả lời cùng một câu hỏi), đổi góc viết cho khác hẳn và ghi lý do vào báo cáo. Nếu không đổi được, bỏ qua chủ đề này, ghi vào báo cáo, chọn dòng kế tiếp.
   Tra thêm `seo/tu-khoa-muc-tieu.md`: từ khóa đã giao cho trang danh mục, trang tỉnh hay trang doanh nghiệp thì bài không được nhắm vào từ khóa đó, chỉ đặt link về trang ấy (khi trang đã hiện).
3. Hết bảng: tự đề xuất một chủ đề theo `seo/chien-luoc.md` (đúng mùa, chưa có bài, ưu tiên nhóm A và D), đặt đường dẫn không dấu, gạch nối, dưới 70 ký tự. Ghi "ĐÃ HẾT KẾ HOẠCH" vào báo cáo.

## Bước 2. Thu thập dữ liệu (không bịa)

1. Sản phẩm đang hiện liên quan: `sapo.py products --q <từ khóa> --out $W/sp.json`. Mở trang sản phẩm (`curl -s https://vuabaoho.com/<đường dẫn>`) để lấy thông số và giá đang ghi. Giá chỉ ghi kèm chữ "tham khảo" và tháng năm viết.
2. Bài liên quan để liên kết nội bộ: `sapo.py search-articles ...`, chỉ lấy bài `[hiện]`.
3. Nghiên cứu bằng WebSearch (và WebFetch nếu mạng cho phép) cho quy định, tiêu chuẩn, số liệu. Ghi lại link nguồn. Điều gì không kiểm chứng được thì **không viết**.
4. Không bao giờ viết: giá chung chung, khuyến mãi, chính sách đổi trả, bảo hành, thời gian giao hàng, số lượng tối thiểu, số năm kinh nghiệm, số khách hàng, chứng nhận, tên khách hàng, công dụng chữa bệnh.

## Bước 3. Chọn ảnh thật (3–5 ảnh trong bài + 1 ảnh đại diện)

Thứ tự ưu tiên:
1. **Ảnh sản phẩm** của các sản phẩm được liên kết (trường `images` trong `sp.json`). Dùng thẳng link ảnh, alt mô tả đúng sản phẩm.
2. **Kho ảnh bài viết**: `sapo.py kho-images --q <từ khóa>` (lọc theo mô tả). Dùng thẳng link ảnh.
3. **Google Drive** (connector Google Drive) khi cần ảnh mới: tìm ảnh (`mimeType contains 'image/'`, theo tên file hoặc tên thư mục). Ảnh quần áo bảo hộ nằm trong thư mục tên "Bảo hộ TBC" (ảnh chụp thật có watermark VUBAHO). Kết quả `download_file_content` thường quá lớn và được lưu ra file JSON; lấy trường `content` (base64) để giải mã: `jq -r .content <file> | base64 -d > $W/goc.png`.
   - Thu nhỏ để **xem ảnh** trước khi dùng (công cụ Read đọc được ảnh). Alt phải mô tả đúng cái nhìn thấy.
   - Chữ "VUBAHO" mờ ở giữa ảnh là watermark, **không phải logo in trên áo**; không viết là "in logo".
   - Không dùng ảnh catalogue có watermark TBC.
   - Chuẩn bị rồi tải lên kho: `sapo.py prep-image $W/goc.png $W/ten-anh.jpg --quality 78` (thêm `--crop-dark` nếu ảnh có viền đen), rồi `sapo.py kho-upload $W/ten-anh.jpg --alt "<mô tả>" --filename ten-anh-khong-dau.jpg`. Lệnh in ra link ảnh để chèn vào bài.
4. Cấm: ảnh do AI tạo dùng như ảnh sản phẩm thật; ảnh lấy từ web khác.

Ảnh đại diện: chọn ảnh đẹp nhất, tải về (`sapo.py download <link> $W/dai-dien-goc.jpg`), chuẩn bị bằng `prep-image`, đặt tên file theo từ khóa chính. Giao diện không hiện ảnh đại diện trong trang bài, nên ảnh đó vẫn phải có trong nội dung.

Mẫu chèn ảnh (ảnh đầu tiên `loading="eager"`, các ảnh sau `lazy`; điền đúng kích thước ảnh):
```html
<figure style="margin:20px 0;text-align:center"><img src="LINK" alt="MÔ TẢ" width="1200" height="800" loading="lazy" style="max-width:100%;height:auto"><figcaption style="font-size:14px;color:#666;margin-top:6px">Chú thích ngắn</figcaption></figure>
```

## Bước 4. Viết bài

Ghi nội dung HTML vào `$W/bai.html`. **Không** có thẻ `<h1>` (giao diện tự lấy tiêu đề làm H1).

Khung bài, khoảng 1.200–1.800 chữ:
1. Mở bài 2–4 câu: trả lời thẳng câu hỏi chính, có từ khóa chính trong câu đầu hoặc câu thứ hai. Ngay sau là ảnh đầu tiên.
2. 4–7 mục `<h2>`, có `<h3>` khi cần. Mỗi mục bắt đầu bằng một câu trả lời ngắn rồi mới giải thích. Đoạn 2–4 câu. Dùng `<ul>`/`<ol>`, và bảng khi so sánh: bọc bảng trong `<div style="overflow-x:auto">…</div>`.
3. Bối cảnh Việt Nam và VBH: công trường, nhà xưởng, khu công nghiệp, mùa rét miền Bắc, nắng nóng miền Trung; khách doanh nghiệp và khách lẻ.
4. 2–4 liên kết nội bộ dạng `<a href="/duong-dan">chữ mô tả</a>`, chỉ tới trang đang hiện, trong đó có trang đích của nhóm (bảng trong `seo/chien-luoc.md`) nếu trang đó đã hiện. Kiểm tra từng link: `curl -s -o /dev/null -w "%{http_code}" https://vuabaoho.com/duong-dan` phải ra 200.
5. Mục `<h2>Câu hỏi thường gặp</h2>` gồm 4–6 câu: mỗi câu là `<h3>` câu hỏi, ngay sau là một `<p>` trả lời 1–3 câu.
6. Mục `<h2>` cuối: liên hệ, ghi đúng thông tin doanh nghiệp trong `CLAUDE.md` (hotline 1900.3385, hai cửa hàng kèm số điện thoại, website).
7. Chạy `sapo.py faq-schema $W/bai.html` để gắn schema FAQPage vào cuối bài.

Bài dạng Top hoặc so sánh: theo mục "Dạng nội dung và cách phối" trong `seo/chien-luoc.md` và mục "Bài dạng Top và so sánh" trong `seo/tieu-chi-duyet-bai.md` (tiêu chí chọn ở đầu bài, công khai hãng Vua Bảo Hộ đang bán, không "số 1" khi không có số liệu). Chủ đề ghi "cập nhật bài cũ" trong kế hoạch thì không tạo bài mới: dùng `update-article` cho bài cũ đó, và chỉ làm khi bài cũ do quy trình tự động tạo; nếu không, bỏ qua và báo anh.

Văn phong: tiếng Việt tự nhiên, xưng "anh chị" (bài cho doanh nghiệp có thể dùng "doanh nghiệp"). Không sáo rỗng, không phóng đại, không viết hoa cả câu, không dùng biểu tượng cảm xúc, không giật tít. Viết đúng thuật ngữ ngành (ví dụ S1P, SRC, EN ISO 20345, dB).

Thông tin SEO:
- `title`: dưới 70 ký tự, chứa từ khóa chính.
- `meta_title`: dưới 60 ký tự, chứa từ khóa chính, kết thúc bằng " | Vua Bảo Hộ" nếu đủ chỗ.
- `meta_description`: 140–160 ký tự, chứa từ khóa chính, nói rõ người đọc được gì.
- `summary`: 1–2 câu cho danh sách tin.
- `tags`: tên nhóm chủ đề và từ khóa chính (lệnh tạo bài tự thêm tag `seo-tu-dong`).

## Bước 5. Duyệt bài (tối đa 3 lượt chấm)

1. Tạo `$W/brief.json`: `tu_khoa_chinh`, `tieu_de`, `meta_title`, `meta_description`, `duong_dan`, `nhom_chu_de`, `dang_noi_dung` (ví dụ "top hãng", "so sánh", "hướng dẫn"), `nguon_tham_khao` (link và ghi chú dữ liệu sản phẩm đã dùng).
2. Chấm bằng ChatGPT: `python3 seo/scripts/openai_review.py --article $W/bai.html --brief $W/brief.json --out $W/review.json`.
3. Nếu lệnh thoát với mã 2 (chưa có mã OpenAI API hoặc mạng chặn): Claude duyệt bằng **hai agent riêng, lần lượt** (công cụ Agent):
   - **Agent kiểm tra**: đóng vai biên tập viên khó tính. Đưa đường dẫn `seo/tieu-chi-duyet-bai.md`, `$W/brief.json`, `$W/bai.html`. Yêu cầu kiểm chứng bằng WebSearch **mọi** số liệu, điều luật, số hiệu văn bản, tiêu chuẩn, ngưỡng kỹ thuật (ghi URL nguồn), đối chiếu mục "Điểm pháp lý đã kiểm chứng" trong tiêu chí, kiểm tra link nội bộ trả 200, rồi trả về JSON đúng định dạng của script (`diem`, `loi_nghiem_trong`, `can_sua`, `nhan_xet`).
   - **Agent phản biện**: nhận bài và kết quả của agent kiểm tra, tự kiểm chứng lại từng lỗi nghiêm trọng bằng WebSearch (người trước có thể nhầm), chỉ giữ lỗi chắc chắn sai, và chấm lại. Kết quả cuối là kết quả của agent phản biện.
   - Ghi người chấm là "Claude (kiểm tra + phản biện)".
4. Đạt khi `diem` ≥ 85 và `loi_nghiem_trong` rỗng. Chưa đạt thì sửa theo `loi_nghiem_trong` và `can_sua`, chạy lại `faq-schema`, rồi chấm lại (cả hai agent).
5. Sau 3 lượt vẫn chưa đạt: vẫn tạo bài nhưng **để ẩn, không đánh dấu chờ đăng**, ghi lý do vào sheet và báo cáo.

Người chấm chỉ góp ý. Điều gì người chấm nêu mà trái với dữ liệu đã kiểm chứng thì giữ bản đúng và ghi lý do vào báo cáo.

## Bước 6. Tạo bài trên Sapo (luôn tạo ở chế độ ẩn)

Tạo `$W/spec.json`:
```json
{"title": "...", "alias": "...", "meta_title": "...", "meta_description": "...", "summary": "...",
 "tags": "...", "content_file": "/duong/dan/bai.html",
 "image_file": "/duong/dan/anh-dai-dien.jpg", "image_filename": "tu-khoa-chinh.jpg", "image_alt": "mô tả ảnh"}
```
Chạy `sapo.py create-article $W/spec.json` (tạo ẩn, tác giả "Vua Bảo Hộ", tag `seo-tu-dong`). Ghi lại `id`. Kiểm tra: `sapo.py check-draft <id>`: không có `anh_loi`, có FAQ schema, số chữ hợp lý.

## Bước 7. Đánh dấu chờ đăng (lượt 7h50 KHÔNG đăng bài)

- Bài **đạt** duyệt: `sapo.py mark-ready <id>`. Bài vẫn ẩn; lượt đăng khoảng 14h (Bước 10) sẽ đăng nếu anh không chặn.
- Bài **chưa đạt**: không đánh dấu, để ẩn.
- Lượt 7h50 **không bao giờ** chạy `publish`. **Không bao giờ** dùng cờ `--anh-da-duyet` trong lịch tự động; cờ này chỉ dành cho phiên trò chuyện khi chính anh vừa bảo đăng một bài cụ thể.

## Bước 8. Ghi vào Google Sheet theo dõi

ID của Google Sheet nằm trong lời nhắc của lịch tự động (không ghi vào repo, vì repo để public và sheet để chế độ ai có link đều xem được). Dùng connector **Google Sheets** (`get_values`, `update_values`; nếu có skill google-workspace thì đọc `references/sheets.md` trước). Ghi vào tab đầu tiên.

1. Đọc hàng 1. Nếu chưa có tiêu đề cột thì ghi đúng hàng tiêu đề sau vào A1:Q1:
   `Ngày viết | Id Sapo | Tiêu đề | Đường dẫn | Từ khóa chính | Dạng nội dung | Nhóm | Người chấm | Điểm | Lỗi nghiêm trọng | Góp ý chính | Kết luận | Anh duyệt | Trạng thái | Link bài | Giờ đăng | Tóm tắt`
2. Thêm **một hàng mới** ngay dưới hàng cuối có dữ liệu (đọc cột A để tìm hàng trống đầu tiên). Không sửa hàng của ngày khác, không xóa gì.
   - Ngày viết dạng `dd/mm/yyyy`; Id Sapo là số id; Đường dẫn là `/alias`.
   - Kết luận: `Đạt` hoặc `Chưa đạt`. Anh duyệt: **để trống** (anh ghi `Không đăng` nếu muốn chặn). Trạng thái: `Chờ đăng 14h` nếu đạt, `Để ẩn – chưa đạt` nếu chưa đạt.
   - Lỗi nghiêm trọng, Góp ý chính: tóm tắt ngắn, mỗi ý một dòng, không quá 500 ký tự mỗi ô. Tóm tắt: 2–3 câu nói bài viết gì.
3. Đọc lại hàng vừa ghi để chắc dữ liệu đúng ô.
4. Nếu phiên không có connector Google Sheets: bỏ qua bước này và ghi rõ trong báo cáo "chưa ghi được vào sheet (chưa có kết nối Google Sheets)".

## Bước 9. Báo cáo lượt 7h50 (tin nhắn cuối cùng của phiên)

Viết tiếng Việt, ngắn, xưng "em", gọi "anh". Đây là nội dung anh nhận trên điện thoại:
- Tiêu đề bài, từ khóa chính, dạng nội dung, nhóm chủ đề.
- Điểm duyệt, người chấm (ChatGPT model gì, hoặc "Claude kiểm tra + phản biện"), lỗi đã sửa.
- Trạng thái: **chờ đăng khoảng 14h** (muốn chặn thì ghi "Không đăng" vào cột "Anh duyệt" trong sheet trước giờ đó), hoặc **để ẩn vì chưa đạt** kèm lý do.
- Số ảnh, nguồn ảnh. Các link nội bộ đã gắn. Đã ghi sheet hay chưa.
- Điều cần anh lưu ý; chủ đề dự kiến cho lần chạy sau; kế hoạch còn dưới 5 chủ đề thì nói rõ.

## Bước 10. Lượt đăng khoảng 14h (lịch riêng, không viết bài mới)

1. `sapo.py pending` để lấy danh sách bài ẩn đang chờ đăng (tag `cho-dang`).
2. Với từng bài, tìm hàng có cùng Id Sapo trong sheet (Bước 8):
   - Cột "Anh duyệt" có chữ `Không đăng` (không phân biệt hoa thường, có hoặc không dấu): `sapo.py mark-ready <id> --bo`, để ẩn, ghi Trạng thái `Để ẩn – anh không duyệt`.
   - Ngược lại: `sapo.py publish <id>`, rồi kiểm tra như Bước 11. Ổn thì ghi Trạng thái `Đã đăng`, Link bài `https://vuabaoho.com/<alias>`, Giờ đăng `hh:mm dd/mm/yyyy`.
   - Không thấy hàng của bài trong sheet thì vẫn đăng (anh đã chọn "im lặng là đồng ý") và ghi chú trong báo cáo.
3. Nếu phiên không có connector Google Sheets: vẫn đăng các bài đang chờ, báo rõ là không đọc được cột "Anh duyệt".
4. Báo cáo ngắn: bài nào đã đăng (link), bài nào anh chặn, lỗi nếu có. Không có bài chờ thì báo một dòng.

## Bước 11. Kiểm tra sau khi đăng

- `sapo.py check-live <đường dẫn>`. Cần có: `title`, `meta_description` đúng, `h1` đúng, `schema` có `FAQPage`, `json_lo_ra_ngoai` = false, `anh_loi` rỗng, `anh_khong_thay_tren_trang` rỗng. Mục `schema` có "LỖI JSON" ở NewsArticle là lỗi sẵn có của giao diện, không phải lỗi của bài.
- Có lỗi thì sửa bằng `sapo.py update-article <id> <spec.json>`. Không sửa được ngay thì `sapo.py hide <id>`, ghi Trạng thái `Đã ẩn lại – lỗi sau khi đăng` và báo cáo.

## Không được làm

- Xóa hoặc sửa bài cũ không do quy trình này tạo ra; sửa hoặc ẩn sản phẩm; đổi giao diện, cài đặt cửa hàng, danh mục.
- Xóa ảnh trong kho ảnh (bài cũ đang dùng).
- Viết quá một bài mỗi lượt 7h50; đăng bài trong lượt 7h50.
- Sửa, xóa hàng của ngày khác trong Google Sheet; đổi tên hay xóa tab.
- Ghi mã API, mật khẩu, ID Google Sheet vào repo, bài viết hoặc báo cáo.
- Commit hay push thay đổi lên repo (repo đang để public; kế hoạch do anh duyệt).
