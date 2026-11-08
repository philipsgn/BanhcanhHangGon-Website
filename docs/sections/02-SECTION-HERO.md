# 02 — SECTION: HERO (TRANG CHỦ & CỬA NGÕ VỊ NGON)

## 1. Ý Nghĩa Từ Ngữ & Sứ Mệnh (Semantics & Purpose)
- **Sứ mệnh**: Section Hero là "cú chạm thị giác" đầu tiên, kích thích vị giác của thực khách ngay trong 2 giây đầu tiên vào trang bằng hình ảnh chú gà đầu bếp Hàng Gòn bên cạnh tô bánh canh tươi ngon, nước lèo óng ả và sợi bánh canh nóng hổi.
- **Giải nghĩa câu khẩu hiệu cốt lõi**:
  - *"Đưa gánh bánh canh Hàng Gòn về giữa phố thị"*: Tuyên ngôn mang linh hồn di sản của gánh canh truyền thống từ vùng quê Hàng Gòn (Đồng Nai) về phục vụ trọn vẹn giữa lòng đô thị Sài Gòn phồn hoa.
  - *Hình ảnh chú gà đầu bếp & đôi đũa gắp thịt gà*: Thể hiện linh hồn linh vật biểu tượng của quán cùng hành động thưởng thức sống động ("chạm vào món ăn"), khoe trọn từng thớ thịt gà ta dai chắc, lớp da vàng óng mọng nước và chén muối tiêu chanh ớt bên cạnh.

---

## 2. Bố Cục & Wireframe (Layout Architecture)

### Trên Website Desktop (>= 881px)
- **Cấu trúc**: `<section id="hero">` chiếm trọn vẹn màn hình đầu tiên (`height: 100vh`).
- **Phân lớp (Layering)**:
  - `Lớp 1 (Dưới cùng)`: `.hero-panorama` chứa thẻ `<picture>` nạp ảnh WebP phong cảnh ngang tối ưu nghệ nhân (`/images/home/new-chicken-chef-desktop.webp`, $1672 \times 941$), căn giữa hoàn hảo (`object-fit: cover; object-position: center center;`).
  - `Lớp 2 (Ở giữa)`: `.hero-overlay` lớp phủ gradient màu cà phê ấm (`#241610`) chuyển dần sang trong suốt để tạo độ sâu điện ảnh.
  - `Lớp 3 (Trên cùng)`: `.hero-content` chứa câu khẩu hiệu nghệ thuật phông chữ *Cormorant Garamond* in nghiêng trang nhã, viền bóng chữ sang trọng.

### Trên Website App Mobile (<= 880px)
- **Chiều cao**: Tối ưu vừa vặn toàn màn hình điện thoại di động (`100svh`).
- **Tài sản chuyên biệt (Dedicated Mobile Asset)**:
  - Sử dụng ảnh WebP khổ dọc chuyên biệt (`/images/home/new-chicken-chef-mobile.webp`, $941 \times 1672$), ôm trọn tỉ lệ 9:16 của smartphone từ đầu chú gà đến hết tô bánh canh.
  - Loại bỏ hoàn toàn cơ chế cuộn ngang (`scrollLeft`) chắp vá cũ. Trang tải mượt mà tức thì, không giật lag, không lệch tâm.
  - Câu khẩu hiệu đặt êm ái ở đáy màn hình với dải gradient tối mờ, bảo đảm độ tương phản chuẩn WCAG AA mà không che khuất món ăn.

---

## 3. Bộ Asset & Hình Ảnh Liên Quan (Assets & Paths)

| Tên File | Đường Dẫn Thực Tế | Độ Phân Giải / Định Dạng | Mục Đích |
| :--- | :--- | :--- | :--- |
| **Ảnh Desktop WebP** | `images/home/new-chicken-chef-desktop.webp` | 1672 x 941 (~293KB) | Ảnh nền Hero chủ đạo trên Desktop |
| **Ảnh Desktop PNG gốc** | `images/home/new-chicken-chef-desktop.png` | 1672 x 941 (2.35MB) | Ảnh gốc lưu trữ chất lượng cao |
| **Ảnh Mobile WebP** | `images/home/new-chicken-chef-mobile.webp` | 941 x 1672 (~262KB) | Ảnh nền Hero dọc chuẩn di động |
| **Ảnh Mobile PNG gốc** | `images/home/new-chicken-chef-mobile.png` | 941 x 1672 (2.23MB) | Ảnh gốc lưu trữ chất lượng cao |
| **Preload Header** | `<link rel="preload" as="image" ...>` | Phân tách media query | Tối ưu LCP trên cả Desktop và Mobile |

---

## 4. Hiệu Ứng & Trạng Thái Tương Tác (Interactions & Motion)
1. **Responsive Picture Element**: Trình duyệt tự động chỉ tải duy nhất 1 bức ảnh phù hợp với thiết bị, tiết kiệm băng thông và tối đa hóa điểm hiệu năng Core Web Vitals.
2. **Hiệu ứng Parallax / Depth**: Khung ảnh nền cố định nhẹ nhàng khi thực khách bắt đầu cuộn xuống khám phá câu chuyện Hàng Gòn.
