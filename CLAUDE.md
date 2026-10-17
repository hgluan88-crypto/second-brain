# Second Brain — anh Luận (Vua Bảo Hộ)

Claude đọc file này trước khi trả lời bất cứ câu hỏi nào.

## Người dùng
- Anh Luận (Mr Luận), chủ và người điều hành Công ty TNHH Vua Bảo Hộ (VBH).
- Xưng hô: Claude xưng "em", gọi "anh". Trả lời bằng tiếng Việt.

## Công ty
- Ngành: đồ bảo hộ lao động cao cấp và đồng phục doanh nghiệp. Website: vuabaoho.com.
- Trụ sở chính: Nam Định. Chi nhánh: Nghệ An.
- Hai mùa hàng: mùa hè bán áo điều hòa / áo quạt (cao điểm tháng 3–8), mùa đông bán áo sưởi / áo giữ ấm.
- Kênh bán: cửa hàng, Facebook, TikTok, Shopee, website, Zalo, hotline.
- Thế mạnh và trọng tâm phát triển: khách hàng doanh nghiệp (B2B).
- Năm 2026 lần đầu lập vị trí cửa hàng trưởng chính thức; đang cơ cấu lại lương và quy trình.
- Thang bậc nhân viên: Cấp độ 1 → Cấp độ 2 → Cấp độ 3 → CHT tập sự → CHT chuẩn.

## Liên hệ công khai (dùng cho bài viết, website)
- Hotline toàn quốc: 1900.3385
- Cửa hàng Nam Định: Số 202 Điện Biên, Phường Nam Định, tỉnh Ninh Bình — 0911.377.997
- Cửa hàng Nghệ An: Số 3 Phan Đình Phùng, Phường Thành Vinh, tỉnh Nghệ An — 0941.60.8118

## Website (Sapo)
- Quản trị: vuabaoho.mysapo.net. Mã API lưu trong Network secrets của môi trường, không ghi vào repo.
- Blog chính "Thông tin tiêu dùng" (alias tin-tuc), hơn 700 bài. Trước khi viết bài mới, kiểm tra bài cũ cùng từ khóa để tránh tự cạnh tranh.
- Sản phẩm quần áo bảo hộ đang tạo mỗi size là một sản phẩm và đều ẩn trên web; danh mục "Quần áo bảo hộ lao động" (alias quan-ao-bao-ho-lao-dong-1) đang trống.
- Đăng bài qua API: hiện bài bằng cách đặt `published_on` (trường `published` không có tác dụng); ảnh đại diện gửi bằng `image.base64`, alt ảnh nằm ở trường `alt_image`. Sapo chặn User-Agent mặc định của Python.
- Giao diện không hiện ảnh đại diện trong trang bài viết. API không tải được ảnh vào kho Tệp tin, nên ảnh giữa bài lưu trong sản phẩm ẩn "KHO ẢNH BÀI VIẾT – KHÔNG XÓA, KHÔNG BÁN" (id 94248792). Không xóa sản phẩm này.
- Giao diện đã tự sinh schema BreadcrumbList và NewsArticle; schema NewsArticle bị lỗi JSON (dấu phẩy thừa) trên mọi bài, cần sửa trong theme.

## Đăng bài SEO tự động
- Quy trình: skill `.claude/skills/dang-bai-seo`; công cụ `seo/scripts/sapo.py`; chiến lược `seo/chien-luoc.md`; kế hoạch `seo/ke-hoach-noi-dung.md`; tiêu chí duyệt `seo/tieu-chi-duyet-bai.md`.
- Chiến lược tổng 6 tháng (19/10/2026 → 18/04/2027, 4 ngành: áo điều hòa, đồ bảo hộ cho doanh nghiệp, giày bảo hộ, địa phương): `seo/chien-luoc-6-thang.md`. Sổ từ khóa (mỗi từ khóa một trang): `seo/tu-khoa-muc-tieu.md`. Mẫu SEO khi mở cửa hàng tỉnh mới: `seo/dia-phuong-mau.md`.
- Lịch tự động chạy 7h50 sáng mỗi ngày (giờ Việt Nam), mỗi lần một bài, gắn tag `seo-tu-dong`.
- 14 bài tự động đầu tiên để ẩn chờ anh duyệt, từ bài thứ 15 đăng thẳng.
- ChatGPT duyệt bài qua OpenAI API (Network secret cho api.openai.com). Chưa có mã thì Claude duyệt thay và ghi rõ trong báo cáo.

## Chữ viết tắt
- **CHT = Cửa hàng trưởng** (không phải chỉ huy trưởng)
- VBH = Vua Bảo Hộ
- NA = Nghệ An, NĐ = Nam Định
- NVBH = nhân viên bán hàng
- KH = khách hàng, DN = doanh nghiệp, KCN = khu công nghiệp

## Dữ liệu nằm ở đâu
- Notion, mục "Khu Vực Công Việc": nội quy, quy trình đào tạo, checklist NVBH, sứ mệnh và mục tiêu 2030.
- Notion, mục "Quản Lý Công Việc Liên Tục / Công việc hàng ngày / phỏng vấn Bán hàng": hồ sơ phỏng vấn.
- Google Drive: báo cáo doanh thu hàng ngày của Nghệ An và Nam Định, thư mục "Vua Bảo Hộ - Nghệ An", danh sách KCN Nghệ An.

## Quy tắc cho Claude
- Gặp chữ viết tắt hoặc tên người chưa rõ thì hỏi lại, không đoán.
- Tư vấn phải gắn với bối cảnh VBH: bán lẻ + B2B đồ bảo hộ, chi nhánh ở xa trụ sở.
- Repo này đang để **public**: không ghi thông tin cá nhân của nhân viên, doanh thu, lương vào đây.
  Ghi chú nhân sự lưu ở nơi riêng tư (Notion) hoặc chỉ ghi vào đây sau khi repo chuyển sang private.
