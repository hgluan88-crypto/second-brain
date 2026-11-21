# Lượt đăng khoảng 14h – vuabaoho.com

Lịch riêng, chạy khoảng 13h33 giờ Việt Nam. Lượt này **không viết bài mới**: chỉ đăng các bài lượt 7h50 đã viết, đã đạt duyệt và đang chờ đăng (tag `cho-dang`), trừ bài anh ghi "Không đăng" trong sheet ("im lặng là đồng ý").

Đọc trước `CLAUDE.md`. Công cụ: `python3 seo/scripts/sapo.py <lệnh>`. Lệnh `publish` chỉ đăng bài có tag `cho-dang` và tạo từ 2 giờ trước; bị chặn thì để nguyên và báo cáo, không tìm cách khác. ID Google Sheet nằm trong lời nhắc của lịch, không ghi vào repo.

## Bước 1. Đăng các bài chờ đăng

1. `sapo.py pending` để lấy danh sách bài ẩn đang chờ đăng (tag `cho-dang`).
2. Với từng bài, tìm hàng có cùng Id Sapo trong Google Sheet theo dõi (cột như Bước 8 của `SKILL.md`):
   - Cột "Anh duyệt" có chữ `Không đăng` (không phân biệt hoa thường, có hoặc không dấu): `sapo.py mark-ready <id> --bo`, để ẩn, ghi Trạng thái `Để ẩn – anh không duyệt`.
   - Ngược lại: `sapo.py publish <id>`, rồi kiểm tra như Bước 2. Ổn thì ghi Trạng thái `Đã đăng`, Link bài `https://vuabaoho.com/<alias>`, Giờ đăng `hh:mm dd/mm/yyyy`.
   - Không thấy hàng của bài trong sheet thì vẫn đăng (anh đã chọn "im lặng là đồng ý") và ghi chú trong báo cáo.
3. Nếu phiên không có connector Google Sheets: vẫn đăng các bài đang chờ, báo rõ là không đọc được cột "Anh duyệt".
4. Báo cáo ngắn: bài nào đã đăng (link), bài nào anh chặn, lỗi nếu có. Không có bài chờ thì báo một dòng.

## Bước 2. Kiểm tra sau khi đăng

- `sapo.py check-live <đường dẫn>`. Cần có: `title`, `meta_description` đúng, `h1` đúng, `schema` có `FAQPage`, `json_lo_ra_ngoai` = false, `anh_loi` rỗng, `anh_khong_thay_tren_trang` rỗng. Mục `schema` có "LỖI JSON" ở NewsArticle là lỗi sẵn có của giao diện, không phải lỗi của bài.
- Có lỗi thì sửa bằng `sapo.py update-article <id> <spec.json>`. Không sửa được ngay thì `sapo.py hide <id>`, ghi Trạng thái `Đã ẩn lại – lỗi sau khi đăng` và báo cáo.

## Không được làm

- Viết bài mới, đăng bài không có tag `cho-dang`, gọi API Sapo trực tiếp để đặt `published_on`.
- Sửa hàng của bài khác trong sheet, đổi tên hay xóa tab.
- Commit hay push lên repo.
