# 07 — SECTION: CUSTOMER REVIEWS (ĐÁNH GIÁ THỰC KHÁCH 5 SAO)

## 1. Ý Nghĩa Từ Ngữ & Sứ Mệnh (Semantics & Purpose)
- **Sứ mệnh**: Xây dựng niềm tin vững chắc (Social Proof) thông qua các đánh giá chân thật từ những thực khách đã đến quán và trải nghiệm trực tiếp trên Google Maps.
- **Giải nghĩa câu chữ & yếu tố cốt lõi**:
  - *"Khách hàng nói gì về Hàng Gòn?"*: Câu hỏi mở tự nhiên, trung thực.
  - *"Google Reviewer: 5/5"*: Huy hiệu xếp hạng thực tế xuất sắc trên nền tảng tìm kiếm Google.
  - *Biểu tượng Google có liên kết*: Cho phép thực khách nhấn trực tiếp vào để xem trang đánh giá chính thức của quán trên Google Maps, tạo tính minh bạch 100%.

---

## 2. Bố Cục & Wireframe (Layout Architecture)

### Trên Website Desktop (>= 1024px, 1440px)
- **Cấu trúc**: `<section id="customer-reviews">` với ảnh nền mờ `.reviews-bg`.
- **Bảng điều khiển trung tâm (`.review-panel`)**:
  - Tiêu đề `.review-title`: Font serif hoàng gia trang trọng.
  - Điểm số `.review-rating`: Google Reviewer: 5/5 sao.
  - Khung trích dẫn `.review-quote-wrap`: Dấu ngoặc kép lớn nghệ thuật ôm lấy lời bình luận thật của khách hàng.
  - Nút bấm điều hướng: 2 mũi tên bên hông (`.review-arrow-prev`, `.review-arrow-next`) và 4 chấm tròn trạng thái (`.review-dots`).

### Trên Website App Mobile (< 768px, 390px)
- Khung `.review-panel` tự động co giãn vừa vặn chiều ngang màn hình điện thoại (chiếm ~90-94% width).
- Dấu ngoặc kép thu gọn kích thước để không chiếm diện tích chữ của lời bình.

---

## 3. Bộ Asset & Hình Ảnh Liên Quan (Assets & Paths)

| Tên File | Đường Dẫn Thực Tế Trên Đĩa | Định Dạng / Kích Thước |
| :--- | :--- | :--- |
| **Ảnh nền Đánh giá** | `images/review/testimonials-bg_result.webp` | WebP nén tối ưu |
| **Google SVG Icon** | Mã SVG nội suy trực tiếp trong thẻ `<svg class="google-icon">` | Vector SVG sắc nét |

> [!CAUTION]
> Tuyệt đối không dùng đường dẫn cũ `/images/testimonials-bg_result.webp`. File ảnh chuẩn hiện nằm ở `images/review/testimonials-bg_result.webp`.

---

## 4. Hiệu Ứng & Trạng Thái Tương Tác (Interactions & Motion)
1. **Carousel Tự Động 6 Giây**: Tự động chuyển qua đánh giá tiếp theo sau mỗi 6000ms (`setInterval`).
2. **Tự động dừng khi tương tác**: Khi người dùng rê chuột vào (`mouseenter`) hoặc chạm ngón tay vào màn hình (`touchstart`), vòng lặp tự dừng để khách thong thả đọc; khi rời đi (`mouseleave` / `touchend`), vòng lặp tiếp tục chạy.
3. **Chuyển động chấm tròn (`.is-active`)**: Chấm tròn tương ứng với review đang xem sẽ sáng lên và chuyển màu vàng gold.

---

## 5. Ranh Giới Cô Lập (Isolation Boundary)
- **Dải HTML trong `index.html`**:
  ```html
  <!-- SECTION 5: CUSTOMER REVIEWS -->
  <section id="customer-reviews" aria-label="Đánh giá khách hàng">
    <img class="reviews-bg" src="images/review/testimonials-bg_result.webp" ...>
    <div class="review-panel">
      ...
    </div>
  </section>
  ```
- **Dải CSS trong `<style>`**:
  - Toàn bộ các quy tắc bắt đầu bằng `#customer-reviews`, `.reviews-bg`, `.review-panel`, `.review-title`, `.review-rating`, `.review-quote-wrap`, `.review-copy`, `.review-source`, `.review-arrow`, `.review-dots`.
- **Mã JS liên quan**: Biến mảng `reviews[]`, hàm `showReview(index)`, `startReviewCarousel()`, `stopReviewCarousel()`.

---

## 6. Checklist Nghiệm Thu Section (Verification Checklist)
- [ ] Ảnh nền `images/review/testimonials-bg_result.webp` hiển thị đẹp, không bị lỗi 404.
- [ ] Lời đánh giá tự động đổi sau 6 giây, không bị giật lag.
- [ ] Bấm các nút mũi tên hoặc chấm tròn chuyển review mượt mà.
- [ ] Bấm vào logo Google mở đúng trang đánh giá Google Maps của quán.

