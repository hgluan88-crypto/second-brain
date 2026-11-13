# Tiêu chí duyệt bài SEO — vuabaoho.com

Dùng chung cho ChatGPT duyệt (script `seo/scripts/openai_review.py`) và cho Claude tự duyệt khi chưa có ChatGPT.

**Bài đạt khi:** tổng điểm từ 85/100 trở lên **và** không có lỗi nghiêm trọng nào.

## Bảng điểm (100 điểm)

| Mục | Điểm | Chấm gì |
|---|---|---|
| 1. Đúng ý định tìm kiếm | 15 | Bài trả lời đúng điều người tìm từ khóa chính muốn biết. Từ khóa chính có trong tiêu đề SEO, H1, 100 chữ đầu, mô tả SEO và ít nhất một H2. Dùng tự nhiên, không nhồi. |
| 2. Chính xác, không bịa | 20 | Mọi số liệu, quy định, tiêu chuẩn, giá, thông số đều có nguồn hoặc lấy từ dữ liệu sản phẩm trên web. Văn bản pháp luật ghi đúng số hiệu và năm. |
| 3. Hữu ích, chuyên sâu | 20 | Có kiến thức thực tế, ví dụ cụ thể theo bối cảnh Việt Nam (công trường, nhà xưởng, khu công nghiệp, mùa lạnh miền Bắc, nắng nóng miền Trung). Không viết chung chung, không lặp ý. |
| 4. Cấu trúc, dễ đọc | 10 | H2/H3 hợp lý, đoạn ngắn (2–4 câu), có danh sách hoặc bảng khi so sánh. Mỗi phần mở đầu bằng câu trả lời trực tiếp. |
| 5. Tối ưu cho Google và AI | 10 | Có đoạn trả lời ngắn gọn ngay đầu bài. Có 4–6 câu hỏi thường gặp kèm schema FAQPage. Nêu rõ tên doanh nghiệp, địa chỉ, hotline đúng như dưới đây. |
| 6. Liên kết và chuyển đổi | 10 | 2–4 liên kết nội bộ tới bài, sản phẩm hoặc danh mục đang hiển thị, đúng ngữ cảnh. Có lời kêu gọi liên hệ hotline hoặc ghé cửa hàng. |
| 7. Hình ảnh | 5 | Ảnh thật (ảnh sản phẩm của web hoặc ảnh trong kho ảnh). Alt mô tả đúng nội dung ảnh. Không dùng ảnh do AI tạo hoặc ảnh lấy từ web khác. |
| 8. Văn phong, chính tả | 10 | Tiếng Việt chuẩn, tự nhiên, xưng "anh chị" hoặc "doanh nghiệp". Không sáo rỗng kiểu "trong thời đại ngày nay", không phóng đại, không viết hoa tùy tiện. |

## Lỗi nghiêm trọng (có một lỗi là không đạt)

- Bịa giá, khuyến mãi, chính sách đổi trả, bảo hành, thời gian giao hàng, số lượng tối thiểu, số năm kinh nghiệm, số khách hàng, chứng nhận, giải thưởng.
- Bịa hoặc ghi sai số liệu, điều luật, tiêu chuẩn kỹ thuật (ví dụ ghi sai ngưỡng dB, sai ký hiệu tiêu chuẩn giày).
- Công dụng chữa bệnh hoặc giảm đau cho sản phẩm (áo sưởi chỉ nói giữ ấm, không nói chữa đau nhức).
- Sai thông tin liên hệ so với mục "Thông tin doanh nghiệp" bên dưới.
- Liên kết tới bài hoặc sản phẩm đang ẩn, hoặc link hỏng.
- Trùng chủ đề hoặc từ khóa chính với một bài cũ trên web.
- Chê bai, so sánh hạ thấp đối thủ cụ thể.
- Viết Yamako là cửa hàng, chi nhánh, thương hiệu con của Vua Bảo Hộ hoặc thuộc chuỗi Vua Bảo Hộ (Yamako là thương hiệu độc lập; Vua Bảo Hộ là nhà phân phối).
- Còn sót ghi chú nội bộ, chỗ trống kiểu [cần bổ sung], hoặc lời nói với người duyệt.

## Bài dạng "Top" và so sánh

- Đầu bài nêu rõ **tiêu chí chọn** (tiêu chuẩn kỹ thuật, có nhà phân phối chính hãng ở Việt Nam, phù hợp công việc, giá công khai). Thiếu tiêu chí: trừ ở mục 3.
- Mỗi mục có: hợp với ai, điểm mạnh, giới hạn, thông số có nguồn. Giá chỉ lấy từ trang sản phẩm vuabaoho.com, ghi "giá tham khảo tháng … năm …".
- Công khai Vua Bảo Hộ đang bán hãng nào trong danh sách, ngay đầu bài. Bài có Yamako phải ghi Vua Bảo Hộ là nhà phân phối Yamako; hãng chỉ nêu để tham khảo thì ghi rõ là tham khảo.
- Xếp các hãng theo chữ cái hoặc theo nhóm nhu cầu, ghi rõ "không phải xếp hạng". Mọi hãng viết cùng một khuôn, kể cả hãng Vua Bảo Hộ bán (cũng có mục giới hạn).
- Mỗi hãng có bằng chứng có mặt ở Việt Nam (trang tiếng Việt của hãng, pháp nhân hoặc nhà phân phối). Xuất xứ chỉ ghi theo giấy tờ, tài liệu hãng hoặc tem nhãn; chữ "Nhật Bản", "nhập khẩu" chỉ ghi khi có căn cứ.
- Không dùng "phổ biến", "mạnh", "ưa chuộng" khi không có số liệu; không dẫn trang xếp hạng kiểu toplist; không so sánh chất lượng theo nước sản xuất.
- Lỗi nghiêm trọng riêng của dạng này: ghi "số 1", "tốt nhất", "bán chạy nhất", "hàng đầu" mà không có số liệu kiểm chứng; nêu hãng không có mặt chính thức ở Việt Nam như thể đang bán phổ biến; ghi xuất xứ hoặc chứng nhận không có căn cứ; link sang cửa hàng khác; chê hãng hoặc đối thủ.
- Giày, ủng "cách điện": chỉ ghi khi tài liệu hãng hoặc tem sản phẩm ghi rõ tiêu chuẩn và mức điện áp. Giày chống tĩnh điện (ESD) **không** phải giày cách điện; viết lẫn hai loại là lỗi nghiêm trọng.

## Điểm pháp lý đã kiểm chứng (đối chiếu khi chấm)

- Nghị định 283/2026/NĐ-CP (ký 15/7/2026, hiệu lực 10/9/2026) thay thế Nghị định 12/2022/NĐ-CP về xử phạt vi phạm hành chính lĩnh vực lao động, bảo hiểm xã hội. Bài còn dẫn Nghị định 12/2022 như văn bản đang áp dụng là sai.
- Thông tư 25/2022/TT-BLĐTBXH (hiệu lực 01/4/2023, thay Thông tư 04/2014): **bắt buộc** lập sổ trang cấp theo mẫu Phụ lục II, có chữ ký xác nhận của người lao động hoặc đại diện tổ, đội, phân xưởng. Thông tư **không** ấn định thời hạn sử dụng từng loại phương tiện; người sử dụng lao động tự quyết theo yêu cầu công việc và khuyến nghị nhà sản xuất.
- Bộ luật Lao động 2019: cấm phạt tiền, cắt lương thay cho xử lý kỷ luật lao động (khoản 2 Điều 127); hình thức kỷ luật chỉ gồm khiển trách, kéo dài thời hạn nâng lương không quá 6 tháng, cách chức, sa thải (Điều 124).
- Giày EN ISO 20345: ký hiệu S3 không có chữ P (S3 đã gồm chống đâm xuyên). Bản 2022 bỏ SRA/SRB/SRC, dùng SR cho phép thử tùy chọn.
- Kính EN 166: ký hiệu 3, 4, 5 chỉ dành cho kính chụp, không có trên kính gọng.
- Rét đậm: nhiệt độ trung bình ngày từ 15 độ C trở xuống; rét hại: dưới 13 độ C (Quyết định 18/2021/QĐ-TTg).

Danh sách này chỉ để đối chiếu nhanh, người chấm vẫn tự kiểm chứng khi bài nói khác hoặc khi văn bản có thể đã thay đổi.

## Thông tin doanh nghiệp (đúng như sau)

- Công ty TNHH Vua Bảo Hộ — website vuabaoho.com — khẩu hiệu "Bảo vệ bạn như bảo vệ VUA".
- Hotline toàn quốc: 1900.3385.
- Cửa hàng Nam Định: Số 202 Điện Biên, Phường Nam Định, tỉnh Ninh Bình — 0911.377.997.
- Cửa hàng Nghệ An: Số 3 Phan Đình Phùng, Phường Thành Vinh, tỉnh Nghệ An — 0941.60.8118.
