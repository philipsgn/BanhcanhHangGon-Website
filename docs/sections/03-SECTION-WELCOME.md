# 03 — SECTION: WELCOME (LỜI CHÀO & MẶT TIỀN QUÁN TRONG KHUNG TRANH NGHỆ THUẬT)

## 1. Ý Nghĩa Từ Ngữ & Sứ Mệnh (Semantics & Purpose)
- **Sứ mệnh**: Tạo cảm giác gần gũi, ấm áp và đáng tin cậy. Đón tiếp thực khách bằng linh vật chú gà ngộ nghĩnh và bức tranh khung gỗ chụp thực tế mặt tiền quán về đêm lung linh ánh đèn.
- **Giải nghĩa câu chữ cốt lõi**:
  - *"Chào mừng bạn đến với Hàng Gòn"*: Lời chào hiếu khách, chân phương nhưng đượm đà tình cảm Nam Bộ.
  - *"Hàng Gòn tự hào mang đến hương vị bánh canh gà đậm đà giữa lòng thành phố. Từng tô canh được nấu mỗi ngày với nước lèo ninh xương, thịt gà tươi chọn lọc, giữ trọn vẹn sự ngọt thanh nguyên bản như thuở ban đầu."*: Tuyên ngôn mộc mạc, tôn vinh kỹ nghệ ninh xương gà ta truyền thống — vị ngọt tự nhiên, không hóa chất, ấm lòng người ghé lại.
  - *Linh vật chú gà ngộ nghĩnh neo góc trái dưới*: Biểu tượng thương hiệu gần gũi, ngước nhìn chào đón thực khách với đôi mắt tròn xoe sinh động.
  - *Khung tranh mặt tiền quán về đêm bên phải*: Ánh đèn vàng ấm áp chiếu sáng bảng hiệu mộc mạc lấp đầy khung tranh gỗ cổ điển, tạo cảm giác như một bức họa lưu giữ di sản gia truyền.

---

## 2. Bố Cục & Wireframe (Layout Architecture)

### Trên Website Desktop (>= 881px)
- **Cấu trúc**: `<section id="welcome">` gồm 2 khối chính và linh vật góc:
  - **Linh vật góc trái dưới (`.welcome-corner-chick`)**: Chú gà ngộ nghĩnh (`cute-chicken.webp`) neo tại `left: 0; bottom: 0;`, khử 100% viền trắng, ngước nhìn User sinh động.
  - **Khối văn bản lệch trái (`.welcome-copy`)**: Tiêu đề Cormorant Garamond và đoạn văn chào mừng mới mượt mà, dịch sang trái hài hòa với tầm nhìn chú gà.
  - **Khung tranh mặt tiền (`.welcome-photo`)**: Bức tranh khung gỗ sang trọng (`framed-restaurant-storefront.webp`) chụp mặt tiền quán về đêm, phủ kín lòng khung gỗ (full-bleed), đổ bóng tranh tường 3D sống động.

### Trên Website App Mobile (<= 880px)
- **Bố cục dọc 1 cột mạch lạc**:
  1. Khung tranh mặt tiền quán ở phía trên (`max-width: 380px;`).
  2. Khối văn bản chào mừng ở giữa, căn giữa trang nhã.
  3. Chú gà ngộ nghĩnh đặt ở phía dưới, tạo điểm nhấn vui vẻ, thân thiện trước khi thực khách cuộn tiếp xuống phần Menu.

---

## 3. Bộ Asset & Hình Ảnh Liên Quan (Assets & Paths)

| Tên File | Đường Dẫn Thực Tế | Định Dạng / Kích Thước | Mục Đích |
| :--- | :--- | :--- | :--- |
| **Chú gà ngộ nghĩnh WebP** | `images/story/cute-chicken.webp` | 615 x 829 (~90KB) | Linh vật chào khách neo góc trái dưới |
| **Chú gà PNG gốc** | `images/story/cute-chicken.png` | 1024 x 1024 (769KB) | File gốc chất lượng cao |
| **Khung tranh mặt tiền WebP** | `images/story/framed-restaurant-storefront.webp` | 1200 x 1520 (~316KB) | Mặt tiền quán tràn kín lòng khung gỗ |
| **Khung tranh PNG gốc** | `images/story/frame-for-restaurant.png` | 2245 x 3179 (746KB) | Khung gỗ gốc phục vụ in ấn & mở rộng |
