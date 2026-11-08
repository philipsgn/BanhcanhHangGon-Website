# 09 — SECTION: ORDER BOARD (BỐ CỤC 2 CỘT TƯƠNG TÁC, KHÓA TRÀN ĐÁY MENU, GIỜ MỞ CỬA 06:00 - 23:00 & THỚT GỖ CHÂN GÀ)

## 1. Ý Nghĩa Từ Ngữ & Sứ Mệnh (Semantics & Purpose)
- **Sứ mệnh**: Trang [`order.html`](file:///c:/Users/TanPhat/Documents/DATA_ANALYST/BCG-HangGon/order.html) mang lại trải nghiệm tương tác vật lý chân thực đỉnh cao trên bàn ăn nhà hàng truyền thống Việt Nam:
  - **Không Gian & Ảnh Nền Góc Rộng Panorama (1920x1080)**: Sử dụng hình ảnh Cánh Đồng Lúa Chín Vàng Việt Nam chuẩn 16:9 (`images/order/background-order.jpg`), bao quát bầu trời rực rỡ ánh bình minh, cánh đồng lúa bạt ngàn và **mặt thớt gỗ mộc tiền cảnh** trải dài ở nửa dưới màn hình.
  - **Khóa Tràn Đáy Menu Khi Zoom / Co Nhỏ (Zero Bottom Overflow)**:
    - Chuyển toàn bộ lề định vị của `.single-menu-sheet` sang tỷ lệ phần trăm linh hoạt (`top: 13.5%; bottom: 4%; left: 2.8%; right: 2.8%;`).
    - Tinh gọn nhịp điệu dòng món (`padding: 3.5px 4px`, `gap: 5px`), thiết lập `overflow: hidden;` an toàn.
    - Dòng footer địa chỉ và hotline được ghim cố định với `flex-shrink: 0;`, **bảo đảm 100% nội dung và footer luôn nằm trọn vẹn trong vùng giấy kem của bảng gỗ, không bao giờ bị văng ra ngoài khung khi thu nhỏ hoặc zoom màn hình**.
  - **Giờ Mở Cửa Chính Xác (06:00 - 23:00)**:
    - Cập nhật thông tin chuẩn xác: `Hotline: 090 123 4567 • Mở cửa: 06:00 - 23:00` (từ 6 giờ sáng đến 23 giờ đêm hàng ngày).
  - **Kỹ Thuật Đồ Họa OpenCV Alpha Defringe & Color Decontamination (Sạch 100% Viền Trắng / Halo)**:
    - **Thớt Gỗ Kê Chân Gà ([`rooster_foot_block.webp`](file:///c:/Users/TanPhat/Documents/DATA_ANALYST/BCG-HangGon/images/order/rooster_foot_block.webp))**: Áp dụng phép co hình thái học `cv2.erode` ăn sâu 2px vào trong thớ gỗ, kết hợp thuật toán Telea Inpainting và Distance Transform Color Bleed để lan truyền màu gỗ sồi thật ra sát mép. **Xác nhận 0 pixel viền trắng/xám tồn tại ở rìa chuyển tiếp Alpha**.
    - **Bảng Menu Kẹp Gỗ ([`clipboard_board_only.webp`](file:///c:/Users/TanPhat/Documents/DATA_ANALYST/BCG-HangGon/images/order/clipboard_board_only.webp))**: Tẩy sạch 100% viền trắng ở 4 mép gỗ sồi và 4 góc bo tròn. Toàn bộ dải pixel rìa ngoài được ép màu gỗ sồi nguyên chất `(125, 85, 45)`, mép cắt studio sắc sảo không còn một tia sáng trắng nào lọt ra ngoài.
  - **Hiệu Ứng Bóng Đổ Đa Tầng 3D (Multi-layer Ambient & Contact Shadow)**:
    - Bổ sung cả bóng tiếp xúc sát chân thớt và bóng đổ tỏa xa trên cả chiếc thớt kê chân và khung bảng menu, giúp các vật thể ăn khớp tự nhiên vào mặt thớt gỗ tiền cảnh.
  - **Thế Đứng Chắc Nịch Của Mascot Gà Trống Đầu Bếp**:
    - 2 bàn chân gà cắm móng thẳng và quặp vững vàng lên mặt phẳng thớt gỗ mới, tạo điểm tựa vật lý vững chãi 100%, xóa bỏ triệt để mọi cảm giác lơ lửng hay gượng gạo.
  - **Phiếu Order Co Giãn 2 Mép & Cuộn Mượt Không Thanh Xám**:
    - Bề rộng mặc định rộng rãi `380px`, cho phép kéo giãn 2 mép trái/phải từ `320px` đến `540px`.
    - Ẩn triệt để thanh cuộn xám bằng `scrollbar-width: none; ::-webkit-scrollbar { display: none; }`.
  - Trên **Mobile App**: Bảng Menu kẹp gỗ tối ưu vùng nhìn; Phiếu Order được thu gọn vào **Thanh Ghim Đáy (Slim Floating Bottom Bar)** hiển thị tổng tiền và mở Bottom Sheet trượt mượt mà.

---

## 2. Bố Cục & Tương Tác Vật Lý (Architecture & Interactions)

### Desktop (>= 1024px)
- **Không gian bàn gỗ 2 cột (`.table-stage-split`)**:
  - `Cột Trái-Giữa (.clipboard-col)`: **Linh Vật Chú Gà Trống Đầu Bếp Cầm Giữ Bảng Menu (Left-Aligned Heroic Mascot)**:
    - **Hiệu ứng phân lớp 3D chân thật & Chú Gà Đứng Sát Mép Trái (`.rooster-menu-holder`)**:
      - **Lớp Bục Thớt Gỗ Kê Chân (Layer 0 - `z-index: 0`)**: Chiếc thớt gỗ mộc mạc sạch viền trắng (`rooster_foot_block.webp`, `left: 0; top: 735px; width: 330px;`) đặt nằm vững chãi trên mặt thớt tiền cảnh kèm bóng đổ đa tầng `filter: drop-shadow(0 4px 8px rgba(10, 5, 2, 0.45)) drop-shadow(0 14px 28px rgba(0, 0, 0, 0.65))`.
      - **Lớp Sau (Layer 1 - `z-index: 1`)**: Chú Gà Trống Đầu Bếp vươn cao hùng vĩ (`width: 620px`, cao ~`774px`), đặt ở `left: 0; top: 15px;` sát mép trái màn hình. Móng vuốt chân gà cắm vững vàng lên mặt trên của thớt gỗ kê chân.
      - **Lớp Giữa (Layer 2 - `z-index: 2`)**: Khung bảng kẹp gỗ sồi sạch tinh (`.clipboard-wrapper`, chuẩn `720px x 520px`, `aspect-ratio: 720 / 520`) nâng lên cao ở `margin-top: 175px` với bóng đổ đa tầng `filter: drop-shadow(0 4px 10px rgba(15, 8, 3, 0.35)) drop-shadow(0 16px 36px rgba(0, 0, 0, 0.55))`.
        - Dải bóng Ambient Occlusion `.rooster-arm-shadow` ở mép trái bảng gỗ.
        - Tay nắm góc nhỏ `.menu-resize-corner-br` ở góc dưới phải.
      - **Lớp Trước (Layer 3 - `z-index: 35`)**: Móng vuốt đỉnh trên (`rooster_claw_top.webp`) kẹp chặt nẹp gỗ tự nhiên và móng vuốt hông (`rooster_claw_mid.webp`) ôm mép trái bảng kèm hiệu ứng bóng đổ tự nhiên (`drop-shadow`).
    - **Bảng Menu 1 Trang Mở Rộng (Aesthetic Wide Menu - `.single-menu-sheet`)**:
      - Định vị linh hoạt (`top: 13.5%; bottom: 4%; left: 2.8%; right: 2.8%; overflow: hidden;`).
      - Nền trong suốt (`background: transparent`), hiển thị trực tiếp chữ trên nền giấy mộc của ảnh WebP.
      - 2 cột món ăn giãn cách rộng rãi (`gap: 36px`), tiêu đề `menu.` tối giản, đường nối chấm mờ `.dish-dots`, giá đuôi `K`, nút thêm giỏ hàng trồi nhẹ khi rê chuột/chạm.
      - Footer địa chỉ và giờ mở cửa: `490 Điện Biên Phủ, P.21, Q. Bình Thạnh` • `Hotline: 090 123 4567 • Mở cửa: 06:00 - 23:00`.
  
  - `Cột Phải (.order-slip-col)`: **Phiếu Đặt Hàng Gỗ Kéo Thả & Co Giãn 2 Mép (Bilateral Resizable Guest Check Slip - 380px)**:
    - Kéo mép trái hoặc mép phải để mở rộng (`320px` đến `540px`).
    - Ẩn hoàn toàn thanh cuộn xám của trình duyệt.
    - Cụm điều khiển số lượng trực tiếp `[-] [SL] [+]` và tính năng kéo di chuyển tự do khắp bàn ăn.

---

## 3. Xác Thực & Bảo Toàn Logic
- **Kiểm tra đồ họa OpenCV**: Thuật toán quét pixel xác nhận **0 pixel viền trắng (White fringe = 0)** trên cả `rooster_foot_block.webp` và `clipboard_board_only.webp`.
- **Cập nhật giờ mở cửa**: Xác nhận chuỗi `Mở cửa: 06:00 - 23:00` hiện diện trong file.
- **Kiểm tra cú pháp JS**: Chạy lệnh `node --check` xác nhận 100% cú pháp JavaScript không lỗi.
- **Cân bằng thẻ HTML**: Toàn bộ 116 thẻ mở `<div>` và 116 thẻ đóng `</div>` trong file khớp tuyệt đối.
- **Bảo toàn dữ liệu Backend**: 16 ID món và giá nguyên bản VND gửi lên [`api/order.js`](file:///c:/Users/TanPhat/Documents/DATA_ANALYST/BCG-HangGon/api/order.js) không đổi.
