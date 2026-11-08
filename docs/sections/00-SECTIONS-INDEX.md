# 00 — CHỈ MỤC TỔNG & NGUYÊN TẮC VẬN HÀNH THEO SECTION

> **QUY TẮC BẮT BUỘC DÀNH CHO AI TRỢ LÝ (MANDATORY RULE FOR AI ASSISTANTS)**:
> 1. Mỗi khi người dùng nhắc đến hoặc yêu cầu thiết kế / chỉnh sửa một **Section cụ thể** (ví dụ: Section Menu, Section Hero, Section Story, Section Nav...), bạn **BẮT BUỘC PHẢI DÙNG CÔNG CỤ ĐỌC TÀI LIỆU CỦA SECTION ĐÓ TRƯỚC TIÊN**.
> 2. Đọc kỹ mục **1. Ý nghĩa từ ngữ & Sứ mệnh** để hiểu thấu đáo ý đồ trong prompt của người dùng.
> 3. Nắm vững mục **2. Bố cục & Wireframe** trên cả màn hình Desktop (1440px) và Mobile Web App (390px).
> 4. Chỉ sử dụng đúng các tệp hình ảnh được liệt kê trong mục **3. Bộ Asset & Hình ảnh liên quan** (tồn tại 100% trên đĩa).
> 5. Tuân thủ mục **5. Ranh giới cô lập**, chỉ sửa đúng vùng mã của Section được giao, tuyệt đối không làm ảnh hưởng đến các Section khác trong trang.

---

## Bản Đồ Các Section Trong Dự Án (Section Map)

| Mã File | Tên Section | Thẻ HTML & Vị Trí | Mô Tả Trọng Tâm |
| :--- | :--- | :--- | :--- |
| **01-NAV-HEADER.md** | Điều Hướng & Thanh Top Bar | `<nav id="siteNav">` & `.social-corner` | Logo dập vàng, menu liên kết, Hotline, nút đặt hàng, mạng xã hội |
| **02-SECTION-HERO.md** | Section #hero (Trang Chủ) | `<section id="hero">` | Panorama gắp gà ta, khẩu hiệu gánh canh phố thị, snap scroll di động |
| **03-SECTION-WELCOME.md**| Section #welcome (Chào Mừng) | `<section id="welcome">` | 2 Cột: Giới thiệu hương vị Hàng Gòn & Ảnh mặt tiền quán về đêm |
| **04-SECTION-STORY.md** | Section #story (Di Sản) | `<section id="story">` | Ký ức gánh canh đất đỏ Hàng Gòn, triết lý nấu nước lèo mộc mạc |
| **05-SECTION-MENU.md** | Section #menu (Thực Đơn 3D) | `<section id="menu">` | Thực đơn Zigzag 3D: Bánh canh, Xôi gà, Cơm gỏi, Gỏi xé phay, khay gỗ |
| **06-SECTION-BACKSTAGE.md** | Section #backstage (Hậu Trường)| `<section id="backstage">` | Lưới Bento 5 ảnh: Trứng non, chan nước lèo, gà luộc, không gian quán |
| **07-SECTION-REVIEWS.md** | Section #customer-reviews | `<section id="customer-reviews">` | Huy hiệu Google 5★, trích dẫn thực khách, Carousel xoay vòng |
| **08-SECTION-LOCATION.md** | Section #location (Tọa Độ) | `<section id="location">` | 490 Điện Biên Phủ, giờ mở cửa 06:00–23:00, Hotline, Google Maps iframe |
| **09-ORDER-BOARD.md** | Trang Đặt Món Bàn Gỗ | `order.html` | Bàn gỗ mở đôi 2 cánh, phiếu dán đơn order, form đặt món, Supabase |

---

## Bảng Ánh Xạ Từ Khóa Prompt Thường Gặp (Prompt Keyword Mapping)

Khi người dùng gửi prompt chứa các từ khóa dưới đây, AI phải mở ngay file tài liệu tương ứng:

- **"Header", "Menu bar", "Logo", "Thanh điều hướng", "Hotline góc phải"**
  👉 Đọc file: `docs/sections/01-NAV-HEADER.md`
- **"Home", "Hero", "Đầu trang", "Gắp gà", "Khẩu hiệu", "Panorama"**
  👉 Đọc file: `docs/sections/02-SECTION-HERO.md`
- **"Welcome", "Chào mừng", "Giới thiệu", "Mặt tiền đêm", "Về chúng tôi"**
  👉 Đọc file: `docs/sections/03-SECTION-WELCOME.md`
- **"Story", "Di sản", "Lịch sử", "Câu chuyện Hàng Gòn", "Gánh canh xưa"**
  👉 Đọc file: `docs/sections/04-SECTION-STORY.md`
- **"Menu", "Món ăn", "Thực đơn", "Khay gỗ", "Bánh canh", "Xôi gà", "Cơm gà", "Gỏi gà"**
  👉 Đọc file: `docs/sections/05-SECTION-MENU.md`
- **"Backstage", "Hậu trường", "Bếp", "Nước lèo", "Trứng non", "Gà luộc", "Không gian"**
  👉 Đọc file: `docs/sections/06-SECTION-BACKSTAGE.md`
- **"Reviews", "Đánh giá", "Khách hàng nói gì", "Google Review", "5 sao", "Lời khen"**
  👉 Đọc file: `docs/sections/07-SECTION-REVIEWS.md`
- **"Location", "Địa chỉ", "Bản đồ", "Vị trí", "Giờ mở cửa", "Chân trang", "Footer"**
  👉 Đọc file: `docs/sections/08-SECTION-LOCATION-FOOTER.md`
- **"Order", "Đặt hàng", "Bàn gỗ", "Phiếu order", "Giỏ hàng", "Khung gỗ", "Thanh toán"**
  👉 Đọc file: `docs/sections/09-ORDER-BOARD.md`

---

## Nguyên Tắc Thực Thi Cô Lập (Isolation Principle)

1. **Không can thiệp ngoài phạm vi**: Khi prompt yêu cầu thay đổi Section A, tuyệt đối không tự ý viết lại, xóa bỏ hay tái cấu trúc Section B, C, D...
2. **Bảo tồn đường dẫn Asset tĩnh**: Chỉ dùng đường dẫn tương đối hoặc bắt đầu bằng `/images/...` khớp 100% với file vật lý hiện có trên đĩa.
3. **Giữ nguyên kết nối API & ID**: Mọi thẻ ID dùng cho điều hướng (`#hero`, `#welcome`, `#menu`, `#location`, v.v.) hoặc kết nối script (`#reviewCopy`, `#reviewDots`...) phải được giữ nguyên vẹn.

