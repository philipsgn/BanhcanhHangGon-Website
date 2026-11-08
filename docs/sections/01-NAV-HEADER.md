# 01 — SECTION: SITE NAVIGATION & HEADER

## 1. Ý Nghĩa Từ Ngữ & Sứ Mệnh (Semantics & Purpose)
- **Sứ mệnh**: Thanh điều hướng đóng vai trò là "chiếc la bàn" cao cấp dẫn dắt thực khách, duy trì nhận diện thương hiệu dập nổi hoàng gia và cung cấp kênh liên hệ / đặt hàng nhanh chóng tức thì.
- **Giải nghĩa thuật ngữ & biểu tượng**:
  - `Logo Gà Trống Vàng`: Biểu tượng văn hóa gà ta bản vị, mộc mạc và uy nghiêm, đổ bóng vàng kim (`filter: drop-shadow`).
  - `Nav Order Link ("Đặt hàng")`: Nút bấm có màu vàng nổi bật khác biệt (`#ffd978`) với hiệu ứng dập nổi, thu hút ánh nhìn và dẫn thẳng sang trang order bàn gỗ.
  - `Hotline Nổi ("0356 538 789")`: Nút gọi điện nhanh ghim góc màn hình giúp khách đặt bàn, đặt tiệc hoặc hỏi đường ngay lập tức.
  - `Social Corner`: Cụm icon kênh truyền thông đa nền tảng (Facebook, TikTok) và ứng dụng giao thức ăn (ShopeeFood, GrabFood).

---

## 2. Bố Cục & Wireframe (Layout Architecture)

### Trên Website Desktop (>= 1024px)
- **Vị trí**: `<nav class="site-nav" id="siteNav">` cố định trên đỉnh màn hình (`position: fixed; top: 0; left: 0; width: 100%; z-index: 100;`).
- **Bố cục Flexbox**:
  - `Trái`: Logo quán dạng tròn 76x76px (`.logo`).
  - `Phải`: Danh sách liên kết `<ul>`: Trang chủ (`#hero`), Giới thiệu (`#welcome`), Menu (`#menu`), Vị trí (`#location`), Đặt hàng (`order.html`).
- **Góc nổi (`.social-corner`)**:
  - Cố định ở góc dưới bên phải (`position: fixed; bottom: 30px; right: 28px; z-index: 90;`).
  - Xếp dọc các nút tròn: Hotline -> Facebook -> TikTok -> ShopeeFood -> GrabFood.

### Trên Website App Mobile (< 768px, 390px)
- **Header thu gọn**: Logo thu nhỏ (52x52px), nút hamburger menu (`.nav-toggle`) gồm 3 vạch ngang.
- **Nút Đặt Hàng Di Động**: Nút `.mobile-order-btn` hiển thị cạnh hamburger menu để khách chốt đơn nhanh mà không cần mở menu.
- **Menu tràn màn hình (`.site-nav.nav-open`)**: Khi bấm hamburger, menu xổ xuống toàn màn hình với nền mờ tối (`backdrop-filter: blur(12px)`), các liên kết chữ lớn dễ chạm (Touch Target >= 48px).

---

## 3. Bộ Asset & Hình Ảnh Liên Quan (Assets & Paths)

| Loại Tài Nguyên | Đường Dẫn Thực Tế Trên Đĩa | Ý Nghĩa / Mục Đích |
| :--- | :--- | :--- |
| **Logo quán** | `images/menu/icon-quan-an_result.webp` | Biểu tượng thương hiệu tròn trên Header |
| **Icon ShopeeFood** | `images/icon/icon-shopee_result.webp` | Icon nút đặt hàng qua ShopeeFood |
| **Icon GrabFood** | `images/icon/icon-grab-food_result.webp` | Icon nút đặt hàng qua GrabFood |
| **SVG Icons** | Mã SVG nội suy trực tiếp trong HTML | Icon Hotline, Facebook, TikTok, Hamburger vạch |

---

## 4. Hiệu Ứng & Trạng Thái Tương Tác (Interactions & Motion)
1. **Smart Auto-Hide khi cuộn**:
   - Khi người dùng cuộn chuột xuống (`scrollDown > 8px`): Header tự động trượt ẩn lên trên (`transform: translateY(-100%); opacity: 0;`).
   - Khi người dùng cuộn chuột lên (`scrollUp < -8px`) hoặc ở đầu trang (`scrollY < 80px`): Header trượt xuống êm dịu (`transform: translateY(0); opacity: 1;`).
2. **Animation nút Hamburger**:
   - Khi mở (`.nav-open`): Vạch 1 xoay 45°, vạch 2 biến mất, vạch 3 xoay -45° tạo thành dấu `✕` thanh lịch.
3. **Ẩn tạm thời Social Corner khi cuộn**: Khi người dùng lướt nhanh, cụm icon xã hội mờ đi để tránh che khuất nội dung, sau đó sáng lại sau 220ms dừng cuộn.

---

## 5. Ranh Giới Cô Lập (Isolation Boundary)
- **Dải HTML trong `index.html`**:
  - Từ `<nav class="site-nav" id="siteNav">` đến hết `</nav>`.
  - Khối `<div class="social-corner">` đến hết `</div>`.
  - Thẻ `<div class="dotnav" id="dotnav"></div>`.
- **Dải CSS trong `<style>`**:
  - Toàn bộ các quy tắc bắt đầu bằng `.site-nav`, `.nav-toggle`, `.social-corner`, `.dotnav`.
- **Cam kết**: Khi chỉnh sửa Header, không can thiệp vào các section nội dung bên dưới (`#hero`, `#welcome`...).

---

## 6. Checklist Nghiệm Thu Section (Verification Checklist)
- [ ] Logo hiển thị sắc nét, không vỡ hạt trên màn hình Retina/OLED.
- [ ] Bấm các liên kết menu nhảy mượt mà đến đúng Section tương ứng (Smooth Scroll).
- [ ] Trên điện thoại, bấm nút hamburger menu mở ra mượt mà và chuyển thành dấu `✕`.
- [ ] Nút hotline bấm gọi được ngay trên điện thoại (`tel:0356538789`).
- [ ] Các liên kết ShopeeFood và GrabFood mở đúng trang quán trong tab mới.

