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
- Bài viết mới đăng ở chế độ ẩn để anh duyệt trước.
- Đăng bài qua API: hiện bài bằng cách đặt `published_on` (trường `published` không có tác dụng); ảnh đại diện gửi bằng `image.base64`, alt ảnh nằm ở trường `alt_image`.
- Giao diện không hiện ảnh đại diện trong trang bài viết; ảnh giữa bài cần quyền Tệp tin/Files (API files.json đang báo 403).
- Giao diện đã tự sinh schema BreadcrumbList và NewsArticle; schema NewsArticle bị lỗi JSON (dấu phẩy thừa) trên mọi bài, cần sửa trong theme.

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
