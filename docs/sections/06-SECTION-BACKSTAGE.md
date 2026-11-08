# 06 — SECTION: BACKSTAGE (HẬU TRƯỜNG KỸ NGHỆ BẾP & KHÔNG GIAN)

## 1. Ý Nghĩa Từ Ngữ & Sứ Mệnh (Semantics & Purpose)
- **Sứ mệnh**: Đưa thực khách bước vào không gian bếp chân thật, minh bạch về chất lượng nguyên liệu tươi sống mỗi ngày. Tạo niềm tin vững chắc về vệ sinh an toàn thực phẩm và sự tận tâm của người đứng bếp.
- **Giải nghĩa câu chữ & hình ảnh**:
  - *"Mỗi tô bánh canh được nấu như bữa cơm nhà, nóng hổi, đậm đà và đầy tình thương"*: Khẳng định tinh thần hiếu khách, nấu cho khách ăn như nấu cho chính người thân yêu trong gia đình.
  - *Bộ 5 góc chụp phóng sự*:
    1. *Vị chấm không thể thiếu*: Chén nước mắm ớt hiểm sánh quyện lòng đỏ trứng non.
    2. *Nước lèo ngọt thanh*: Hành động múc vá nước lèo nóng hổi nghi ngút khói.
    3. *Gà tuyển chọn mỗi sáng*: Những con gà ta luộc vàng ươm còn nguyên da giòn căng mọng.
    4. *Góc quán mỗi trưa*: Bàn ăn gọn gàng đón tiếp giới văn phòng và gia đình.
    5. *Mặt tiền Hàng Gòn*: Không gian mặt tiền thoáng đãng, dễ nhận diện tại 490 Điện Biên Phủ.

---

## 2. Bố Cục & Wireframe (Layout Architecture)

### Trên Website Desktop (>= 1024px, 1440px)
- **Cấu trúc**: `<section id="backstage">` bao gồm khung `.bs-shell` và lưới ảnh Bento Grid `.bs-grid` (`display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;`).
- **Phân chia ô lưới Bento**:
  - `.bs-hero` (Ô chính lớn): Chiếm diện tích nổi bật dành cho trứng non chấm mắm.
  - `.bs-vert1` & `.bs-vert2` (Ô dọc): Dành cho hành động chan nước lèo và gà luộc.
  - `.bs-wide1` & `.bs-wide2` (Ô ngang rộng): Dành cho không gian quán và mặt tiền.
- **Chú thích ảnh (`.bs-caption`)**: Dải chú thích mờ nhẹ gắn dưới đáy mỗi ảnh, tăng tính báo chí cho phóng sự.

### Trên Website App Mobile (< 768px, 390px)
- Tự động sắp xếp lại thành lưới 2 cột gọn gàng, các bức ảnh tự co giãn theo tỷ lệ vuông/chữ nhật tự nhiên, không bị biến dạng tỷ lệ khung hình.

---

## 3. Bộ Asset & Hình Ảnh Liên Quan (Assets & Paths)

| Tên Ảnh | Đường Dẫn Thực Tế Trên Đĩa | Định Dạng / Kích Thước |
| :--- | :--- | :--- |
| **Trứng non nước mắm** | `images/highlights/trung-non-nuoc-cham_result.webp` | WebP nén tối ưu |
| **Chan nước lèo nóng** | `images/highlights/chan-nuoc-leo_result.webp` | WebP nén tối ưu |
| **Gà luộc tại quán** | `images/highlights/ga-luoc-quan_result.webp` | WebP nén tối ưu |
| **Một góc nhỏ của quán** | `images/highlights/mot-goc-nho-cua-quan_result.webp` | WebP nén tối ưu |
| **Không gian quán** | `images/highlights/khong-gian-quan_result.webp` | WebP nén tối ưu |

> [!CAUTION]
> Tuyệt đối không dùng đường dẫn cũ `images/behind-scenes/...`. Toàn bộ ảnh hậu trường chuẩn hiện nằm ở `images/highlights/...`.

---

## 4. Hiệu Ứng & Trạng Thái Tương Tác (Interactions & Motion)
1. **Hover Zoom & Brightness**: Khi di chuột vào từng khung ảnh, ảnh phóng to nhẹ 4% (`scale(1.04)`), độ sáng tăng nhẹ, thanh chú thích hiện rõ ràng hơn.
2. **Smooth Transition**: Áp dụng `transition: transform .45s ease, filter .45s ease`.

---

## 5. Ranh Giới Cô Lập (Isolation Boundary)
- **Dải HTML trong `index.html`**:
  ```html
  <!-- SECTION 3.5: BACKSTAGE -->
  <section id="backstage">
    <div class="bs-shell">
      <div class="bs-head"> ... </div>
      <div class="bs-grid"> ... </div>
    </div>
  </section>
  ```
- **Dải CSS trong `<style>`**:
  - Toàn bộ các quy tắc bắt đầu bằng `#backstage`, `.bs-shell`, `.bs-head`, `.bs-quote`, `.bs-grid`, `.bs-item`, `.bs-caption`.
- **Cam kết**: Cô lập hoàn toàn, không đụng tới Section Menu hoặc Section Reviews.

---

## 6. Checklist Nghiệm Thu Section (Verification Checklist)
- [ ] Cả 5 bức ảnh trong `images/highlights/` tải nhanh chóng, không bị lỗi 404.
- [ ] Lưới Bento Grid sắp xếp cân đối, các đường biên thẳng hàng.
- [ ] Dòng trích dẫn triết lý hiển thị nổi bật, không bị lỗi gãy chữ trên di động.

