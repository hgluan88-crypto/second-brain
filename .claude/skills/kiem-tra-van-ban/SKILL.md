---
name: kiem-tra-van-ban
description: Kiểm tra (chấm) một văn bản của VBH theo bộ quy tắc viết quy-tac-viet-van-ban.md rồi báo lỗi và sửa. Dùng khi anh Luận nhờ "kiểm tra", "chấm", "rà", "duyệt", "xem bài này thế nào" cho bài SEO, bài Facebook, TikTok, Shopee, website, tin nhắn Zalo, báo giá, email, nội quy, tài liệu đào tạo. Cũng dùng để Claude tự rà bài của chính mình trước khi gửi.
---

# Kiểm tra văn bản theo quy tắc viết VBH

Luật gốc nằm ở `quy-tac-viet-van-ban.md` (gốc repo). Skill này là quy trình áp luật đó. Đọc lại file luật mỗi lần chạy, vì anh Luận có thể đã sửa luật.

## Bước 1. Tìm đúng văn bản

- Anh dán chữ hoặc gửi file thì dùng luôn.
- Anh gửi link: artifact claude.ai thì đọc bằng Artifact (action read). Google Docs thì đọc qua Google Drive. Notion thì dùng notion-fetch.
- Anh nói chung chung ("bài hôm qua", "bài SEO lần trước"):
  1. Gọi `list_sessions` (mine: true) để tìm phiên có tiêu đề khớp. Xem `external_metadata.artifacts` của phiên đó để lấy link artifact.
  2. Nếu không có, tìm trong Drive (search_files, list_recent_files) và Notion (notion-search) theo từ khóa và ngày.
  3. Tìm ra 2 bài trở lên mà không chắc là bài nào thì hỏi anh. Không đoán.
- Báo anh tên bài, nơi tìm thấy và ngày tạo trước khi chấm.

## Bước 2. Quét máy

Lưu văn bản vào scratchpad (HTML, Markdown hay text đều được) rồi chạy:

```
python3 .claude/skills/kiem-tra-van-ban/scripts/quet.py <file>
```

Script bắt các lỗi có mẫu cố định: Q1, Q2, Q3, Q4, Q5, Q6 (đề mục), Q8, Q9, Q10, Q11, Q13, Q15 (gợi ý), Q16 (gợi ý), Q17, Q22, Q25, Q26, Q27, và nhắc Q7.

Kết quả của script là danh sách nghi vấn, chưa phải phán quyết. Đọc từng dòng trong ngữ cảnh rồi bỏ những dòng bắt nhầm. Ví dụ "dưới đây là" nằm trong thân bài để dẫn vào danh sách thì không phải câu thoại AI.

## Bước 3. Rà tay những quy tắc máy không bắt được

Đọc toàn bài một lượt cho từng mục sau:

- Q6: tiêu đề SEO (meta title) và tiêu đề hiển thị trên Google. Script chỉ quét đề mục trong thân bài.
- Q12: một thứ có bị gọi bằng nhiều tên không.
- Q14: các bộ ba chỉ để câu nghe tròn. Bộ ba mô tả thật (ngực, lưng, ống tay) thì giữ.
- Q15, Q18: câu khen mà không có số liệu hoặc sự việc ("tăng năng suất", "tạo sự chuyên nghiệp").
- Q16: khoảng "từ ... đến ..." mà hai đầu không cùng một thang đo.
- Q19, Q21: nguồn mơ hồ, mục "giải thưởng" hoặc "triển vọng" không có nội dung thật.
- Q24, Q29: giọng văn và cách xưng hô có thống nhất từ đầu đến cuối không.
- Q7: văn bản sẽ đăng ở kênh nào. Nếu là Zalo, Facebook, TikTok hay Shopee thì không được có ký hiệu Markdown.

## Bước 4. Kiểm chứng sự thật (Q20, Q28)

- Văn bản pháp luật, tiêu chuẩn (Thông tư, Nghị định, TCVN, EN, ISO): tra WebSearch để xác nhận số hiệu, tên và ngày hiệu lực. Ghi nguồn đã tra.
- Link nội bộ vuabaoho.com: kiểm tra link có tồn tại không. Mạng bị chặn thì ghi "chưa kiểm được" và đưa vào mục cần anh xác nhận.
- Số liệu của VBH (địa chỉ, hotline, giá, năm kinh nghiệm, số khách DN): tìm trong Drive và Notion. Thấy số cũ thì đưa ra để anh xác nhận, không tự điền vào bài.
- Ảnh: đối chiếu thư mục nguồn của ảnh với chú thích. Ví dụ ảnh lấy từ thư mục của công ty khác mà chú thích ghi "hàng VBH" thì phải báo.
- Địa danh: từ 1/7/2025 nhiều tỉnh đã sáp nhập (Nam Định nay thuộc tỉnh Ninh Bình). Địa chỉ chính thức phải ghi theo đơn vị hành chính mới. Từ khóa SEO cũ thì vẫn giữ được.

## Bước 5. Báo cáo cho anh Luận

Viết theo đúng thứ tự dưới đây. Bản báo cáo cũng phải tuân thủ bộ quy tắc: không gạch dài, không emoji, không dùng kiểu gạch đầu dòng "**Tiêu đề:** nội dung".

1. Tên bài và nơi tìm thấy (1 dòng).
2. Kết luận: đăng được hay chưa. Nếu chưa thì nêu lý do chính trong 1 đến 2 câu. Nêu cả điểm bài làm đúng nếu có, ngắn gọn.
3. Các lỗi phải sửa: bảng 3 cột: Quy tắc | Chỗ vi phạm (trích nguyên văn) | Cách sửa. Gộp các lỗi cùng loại vào một dòng.
4. Cần anh xác nhận: những sự thật em không kiểm chứng được. Nói rõ em đã kiểm cái gì, kết quả ra sao, kèm nguồn.
5. Lỗi nhẹ: những điểm không bắt buộc sửa.
6. Bước tiếp theo: anh cần gửi gì để em sửa xong.
7. Nguồn: link các trang đã dùng để kiểm chứng.

Nếu trong lúc tìm bài thấy rủi ro bảo mật (ví dụ mật khẩu ghi dạng chữ thường trong file chia sẻ) thì báo anh 1 câu ở cuối.

## Bước 6. Sửa bài (khi anh đồng ý)

- Sửa đúng những lỗi đã báo. Chỗ trống chỉ điền bằng số liệu anh đưa. Không bịa.
- Chạy lại `quet.py` và rà tay lại Bước 3. Lặp đến khi script không còn lỗi thật.
- Cập nhật bài ở đúng nơi cũ (cùng link artifact, cùng file Drive hoặc trang Notion) để anh không phải tìm link mới.
- Báo anh: đã sửa những gì, còn gì chờ anh.

## Khi Claude tự viết văn bản cho VBH

Trước khi gửi bất kỳ văn bản nào cho anh Luận, Claude chạy Bước 2 và Bước 3 trên chính bản nháp của mình rồi sửa hết lỗi. Không cần gửi báo cáo kiểm tra trừ khi anh hỏi.

## Bảo trì

- Anh sửa `quy-tac-viet-van-ban.md` thêm hoặc bớt từ cấm thì cập nhật luôn danh sách tương ứng trong `scripts/quet.py` (các biến Q9, Q10, Q11, Q22, Q25, Q27).
- Script bắt nhầm hoặc bỏ sót một mẫu lặp lại nhiều lần thì sửa script, không sửa từng bài bằng tay.
