# 08 — SECTION: LOCATION & FOOTER (TỌA ĐỘ, BẢN ĐỒ & CHÂN TRANG)

## 1. Ý Nghĩa Từ Ngữ & Sứ Mệnh (Semantics & Purpose)
- **Sứ mệnh**: Cung cấp đầy đủ thông tin thực tế để khách ghé quán ăn tại chỗ hoặc liên hệ nhanh chóng. Khẳng định tính pháp lý minh bạch và bản quyền thương hiệu Bánh Canh Gà Hàng Gòn.
- **Giải nghĩa các thông tin cốt lõi**:
  - *Địa chỉ*: **490 Điện Biên Phủ, Thạnh Mỹ Tây, TP. Hồ Chí Minh** — Tuyến đường huyết mạch, trung tâm kết nối quận Bình Thạnh, Quận 1 và Thủ Đức.
  - *Giờ mở cửa*: **06:00 – 23:00 (Mỗi ngày)** — Phục vụ liên tục từ bữa sáng tinh mơ đến tận đêm muộn.
  - *Bộ đôi Hotline*: `0356 538 789` & `0358 345 987` — Đường dây nóng đặt bàn, đặt món số lượng lớn.
  - *Chỉ đường 1 chạm*: Mở ứng dụng Google Maps chỉ đường trực tiếp tới quán.

---

## 2. Bố Cục & Wireframe (Layout Architecture)

### Trên Website Desktop (>= 1024px, 1440px)
- **Cấu trúc**: `<section id="location">` gồm lưới `.loc-grid` 4 cột:
  - `Cột 1 (.loc-group--contact)`: Khối thông tin liên hệ (Địa chỉ, Giờ mở cửa, Hotline) + Nút bấm bản đồ `.loc-map-link`.
  - `Cột 2 (.loc-group--policy)`: Khối liên kết chính sách (Giấy phép, Chính sách bảo mật `chinh-sach-quyen-rieng-tu.html`, An toàn thực phẩm).
  - `Cột 3 (.loc-group--menu)`: Khối điều hướng nhanh (Trang chủ, Thực đơn, Đặt món, Về chúng tôi, Liên hệ).
  - `Cột 4 (.map-wrap)`: Khung nhúng Google Maps iframe tương tác trực tiếp.
- **Dòng chân trang (`.loc-copyright`)**: Chữ nhỏ trang nhã khẳng định bản quyền thương hiệu năm 2026.

### Trên Website App Mobile (< 768px, 390px)
- Lưới 4 cột tự động chuyển thành cột dọc 1 cột: Thông tin liên hệ -> Bản đồ iframe -> Các liên kết chính sách -> Bản quyền.
- Bản đồ iframe có chiều cao tối ưu 240px - 280px, cuộn mượt mà không bị kẹt ngón tay.

---

## 3. Bộ Asset & Iframe Liên Quan (Assets & Embeds)

| Loại Tài Nguyên | Chi Tiết Kỹ Thuật | Mục Đích |
| :--- | :--- | :--- |
| **Google Maps Iframe** | `https://www.google.com/maps/embed?...` | Nhúng bản đồ tọa độ chính xác của quán |
| **Link mở App Maps** | `https://maps.app.goo.gl/m2fKyMJy4xSPQMa87` | Nút "Chỉ đường trên Google Maps" |
| **Trang bảo mật** | `chinh-sach-quyen-rieng-tu.html` | Liên kết văn bản pháp lý chính sách |

---

## 4. Hiệu Ứng & Trạng Thái Tương Tác (Interactions & Motion)
1. **Interactive Map**: Cho phép thực khách phóng to, thu nhỏ và kéo bản đồ để xem các tuyến đường xung quanh (Điện Biên Phủ, Hàng Xanh, Cầu Sài Gòn).
2. **Hover Links**: Các liên kết danh mục và chính sách sáng màu vàng kim (`--gold`) khi di chuột.

---

## 5. Ranh Giới Cô Lập (Isolation Boundary)
- **Dải HTML trong `index.html`**:
  ```html
  <!-- SECTION 4: LOCATION -->
  <section id="location">
    <div class="loc-grid"> ... </div>
    <footer class="loc-copyright">© 2026 Bánh Canh Gà Hàng Gòn · 490 Điện Biên Phủ, TP.HCM</footer>
  </section>
  ```
- **Dải CSS trong `<style>`**:
  - Toàn bộ các quy tắc bắt đầu bằng `#location`, `.loc-grid`, `.loc-group`, `.loc-group-title`, `.loc-list`, `.loc-actions`, `.loc-map-link`, `.map-wrap`, `.loc-copyright`.
- **Cam kết**: Đây là Section cuối cùng của trang, không làm ảnh hưởng đến các Section phía trên.

---

## 6. Checklist Nghiệm Thu Section (Verification Checklist)
- [ ] Bản đồ Google Maps iframe tải đúng vị trí quán, không bị chặn hoặc lỗi xám màn hình.
- [ ] Số hotline click gọi được trực tiếp (`tel:0356538789`).
- [ ] Liên kết chính sách bảo mật mở đúng file `chinh-sach-quyen-rieng-tu.html`.

