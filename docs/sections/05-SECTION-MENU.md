# 05 — SECTION: MENU (THỰC ĐƠN MÓN NGON ĐẶC TRƯNG 3D)

## 1. Ý Nghĩa Từ Ngữ & Sứ Mệnh (Semantics & Purpose)
- **Sứ mệnh**: Section Menu là **trung tâm chuyển đổi (Conversion Engine)** quan trọng nhất trên Landing Page. Mục tiêu là kích thích sự thèm ăn tối đa, làm nổi bật giá trị của từng món ăn bản vị và thúc đẩy khách hàng nhấn ngay nút **"Đặt Món Ngay"**.
- **Giải nghĩa từng món ăn tinh hoa**:
  1. **Bánh Canh Gà Đặc Biệt (70.000 đ)**:
     - *Huy hiệu*: `MÓN ĐẶC BIỆT ❖❖❖`
     - *Thành phần*: Thịt gà ta da vàng giòn mọng nước, trứng non lòng đào dẻo béo, tim mề giòn sần sật, hành phi thơm nức mũi, nước dùng hầm xương ngọt thanh.
  2. **Xôi Gà Trứng Non (42.000 đ)**:
     - *Huy hiệu*: `HƯƠNG NẾP TRUYỀN THỐNG ❖❖❖`
     - *Thành phần*: Nếp cái hoa vàng hạt dẻo bóng ngào mỡ gà, gà luộc xé sợi, trứng non bùi béo, hành phi giòn và nước tương sa tế ớt đậm đà.
  3. **Cơm Gỏi Gà Xé (45.000 đ)**:
     - *Huy hiệu*: `MÓN MỚI BẢN VỊ ❖❖❖`
     - *Thành phần*: Hạt cơm vàng óng ánh màu nghệ tươi nấu từ nước luộc gà, đĩa gỏi bắp cải chua ngọt giòn giòn, nước mắm gừng tỏi ớt thơm nồng.
  4. **Gỏi Gà Xé Phay Rau Răm (65.000 đ)**:
     - *Huy hiệu*: `THANH MÁT GIÒN TAN ❖❖❖`
     - *Thành phần*: Gà ta thả vườn xé phay, bắp cải trắng thái sợi mỏng, bắp chuối bào, nước mắm chua ngọt Nam Bộ, đậu phộng rang củi và rau răm the mát.

---

## 2. Bố Cục & Wireframe (Layout Architecture)

### Trên Website Desktop (>= 1024px, 1440px)
- **Cấu trúc**: `<section id="menu">` với bố cục **Zigzag 3D Editorial** so le cực kỳ nghệ thuật:
  - **Món 1 (Bánh Canh)**: Cột thông tin bên Trái (`.menu-dish-info`), Khay gỗ 3D bên Phải (`.menu-dish-visual`).
  - **Món 2 (Xôi Gà)**: Có class `.menu-dish-row--reverse`: Khay gỗ 3D bên Trái, Cột thông tin bên Phải.
  - **Món 3 (Cơm Gà)**: Cột thông tin bên Trái, Khay gỗ 3D bên Phải.
  - **Món 4 (Gỏi Gà)**: Có class `.menu-dish-row--reverse`: Khay gỗ 3D bên Trái, Cột thông tin bên Phải.
- **Thành phần mỗi hàng món**:
  - Huy hiệu góc nhỏ mạ vàng (`.menu-dish-badge`).
  - Tên món phông chữ *Cormorant Garamond* đậm nét (`.menu-dish-name`).
  - Đoạn văn mô tả chi tiết hương vị giác quan (`.menu-dish-desc`).
  - Cụm giá tiền rõ ràng (`.menu-dish-price`) và nút bấm nổi bật `.menu-dish-btn` dẫn thẳng sang `order.html`.
- **Chân Section (`.menu-editorial-footer`)**: Nút lớn *"Xem Toàn Bộ Thực Đơn & Đặt Hàng"* với mũi tên điều hướng.

### Trên Website App Mobile (< 768px, 390px)
- Chuyển thành bố cục 1 cột thẳng đứng: Ảnh khay gỗ 3D hiển thị trước, thông tin món và nút đặt hiển thị ngay bên dưới để khách lướt ngón tay mượt mà không bị rối mắt.

---

## 3. Bộ Asset & Hình Ảnh Liên Quan (Assets & Paths)

| Món Ăn | Đường Dẫn Thực Tế Trên Đĩa | Định Dạng / Đặc Điểm |
| :--- | :--- | :--- |
| **Bánh Canh Gà Đặc Biệt** | `images/webp/tray_banh_canh.webp` | Khay gỗ WebP HD tách nền sắc nét |
| **Xôi Gà Trứng Non** | `images/webp/tray_xoi_ga.webp` | Khay gỗ WebP HD tách nền sắc nét |
| **Cơm Gỏi Gà Xé** | `images/webp/tray_com_ga.webp` | Khay gỗ WebP HD tách nền sắc nét |
| **Gỏi Gà Xé Phay Rau Răm** | `images/webp/tray_goi_ga.webp` | Khay gỗ WebP HD tách nền sắc nét |

> [!CAUTION]
> **Quy tắc bất di bất dịch**: KHÔNG BAO GIỜ trỏ đường dẫn ảnh về các file cũ như `images/menu/banhcanhga-t9...`. Luôn luôn sử dụng bộ khay gỗ chuẩn 3D: `images/webp/tray_*.webp`.

---

## 4. Hiệu Ứng & Trạng Thái Tương Tác (Interactions & Motion)
1. **Hover Lift Khay Gỗ 3D**: Khi di chuột vào khay món, hình ảnh khay gỗ nhấc nhẹ lên (`transform: translateY(-8px)`), bóng đổ tỏa rộng (`drop-shadow(0 28px 34px rgba(0, 0, 0, 0.26))`).
2. **Button Glow**: Nút "Đặt Món Ngay" phát sáng nhẹ viền vàng kim khi hover, tạo cảm giác thôi thúc hành động.

---

## 5. Ranh Giới Cô Lập (Isolation Boundary)
- **Dải HTML trong `index.html`**:
  ```html
  <!-- SECTION 3: MENU (ZIGZAG 3D EDITORIAL) -->
  <section id="menu">
    <div class="menu-decor-pattern" aria-hidden="true"></div>
    <div class="menu-editorial-container">
      ...
    </div>
  </section>
  ```
- **Dải CSS trong `<style>`**:
  - Toàn bộ các quy tắc bắt đầu bằng `#menu`, `.menu-editorial-container`, `.menu-dish-row`, `.menu-dish-info`, `.menu-dish-visual`, `.menu-dish-badge`, `.menu-dish-name`, `.menu-dish-desc`, `.menu-dish-meta`, `.menu-dish-btn`, `.menu-editorial-footer`.
- **Cam kết**: Khi chỉnh sửa Menu, không làm xáo trộn Section Story phía trên hoặc Section Backstage phía dưới.

---

## 6. Checklist Nghiệm Thu Section (Verification Checklist)
- [ ] Cả 4 khay ảnh WebP (`tray_banh_canh.webp`, `tray_xoi_ga.webp`, `tray_com_ga.webp`, `tray_goi_ga.webp`) tải sắc nét 100%, không bị 404.
- [ ] Bố cục Zigzag so le chuẩn xác trên Desktop (Trái-Phải / Phải-Trái xen kẽ).
- [ ] Giá tiền hiển thị rõ ràng, đúng đơn vị VND.
- [ ] Tất cả nút "Đặt Món Ngay" liên kết chính xác sang `order.html`.

