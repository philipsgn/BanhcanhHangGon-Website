import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = 'index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# -----------------------------------------------------------------------------
# 1. SECTION GREETING: Xóa "như thuở ban đầu"
# -----------------------------------------------------------------------------
old_greeting = '<p class="welcome-description">Hàng Gòn tự hào mang đến hương vị bánh canh gà đậm đà giữa lòng thành phố. Từng tô canh được nấu mỗi ngày với nước lèo ninh xương, thịt gà tươi chọn lọc, giữ trọn vẹn sự ngọt thanh nguyên bản như thuở ban đầu.</p>'
new_greeting = '<p class="welcome-description">Hàng Gòn tự hào mang đến hương vị bánh canh gà đậm đà giữa lòng thành phố. Từng tô canh được nấu mỗi ngày với nước lèo ninh xương, thịt gà tươi chọn lọc, giữ trọn vẹn sự ngọt thanh nguyên bản.</p>'

if old_greeting in content:
    content = content.replace(old_greeting, new_greeting)
    print("Updated Section Greeting (removed 'như thuở ban đầu').")
else:
    print("Old Section Greeting pattern not matched!")

# -----------------------------------------------------------------------------
# 2. SECTION STORY: Ngắt đúng 4 dòng thơ ("bát canh đầy." trọn vẹn dòng 4)
# -----------------------------------------------------------------------------
old_story = '<p class="story-slide__quote">“Góc chợ <em>Hàng Gòn</em> bao năm qua vẫn vậy,<br>Gìn giữ vị quê đượm ấm bát canh đầy.”</p>'
new_story = '<p class="story-slide__quote">“Góc chợ <em>Hàng Gòn</em><br>bao năm qua vẫn vậy,<br>Gìn giữ vị quê đượm ấm<br><span style="white-space: nowrap;">bát canh đầy.”</span></p>'

if old_story in content:
    content = content.replace(old_story, new_story)
    print("Updated Section Story to 4 rhythmic lines.")
else:
    print("Old Section Story pattern not matched!")

# -----------------------------------------------------------------------------
# 3. SECTION MENU CSS:
#    - Ẩn hoàn toàn .menu-dots
#    - Căn .menu-footer-clean sát góc phải
#    - Đổi màu thường #C48B28 và hover #1F120A (Nâu đen cà phê)
# -----------------------------------------------------------------------------
old_footer_css = """/* Thanh Footer Menu: Nền trơn không viền, Chữ vàng kim với 2 gạch trên dưới */
    .menu-footer-clean {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      margin-top: clamp(14px, 2.2vh, 24px);
      padding: 0;
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
      z-index: 5;
    }

    .menu-all-dishes-gold-link {
      position: relative;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 0;
      padding: 8px 24px 9px;
      color: #ffd978;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(15px, 1.3vw, 18px);
      font-weight: 600;
      letter-spacing: 2.8px;
      line-height: 1;
      text-transform: uppercase;
      text-decoration: none;
      text-shadow:
        0 1px 0 rgba(255, 246, 204, 0.42),
        0 0 10px rgba(255, 187, 58, 0.42),
        0 0 22px rgba(201, 112, 26, 0.28);
      background:
        linear-gradient(90deg, transparent 0%, rgba(144, 91, 28, 0.42) 18%, rgba(255, 218, 105, 0.92) 50%, rgba(144, 91, 28, 0.42) 82%, transparent 100%) center top / 100% 1.5px no-repeat,
        linear-gradient(90deg, transparent 0%, rgba(144, 91, 28, 0.45) 18%, rgba(255, 218, 105, 0.95) 50%, rgba(144, 91, 28, 0.45) 82%, transparent 100%) center bottom / 100% 1.5px no-repeat;
      transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-all-dishes-gold-link:hover,
    .menu-all-dishes-gold-link:focus-visible {
      color: #fff0b8;
      transform: translateY(-2px);
      text-shadow:
        0 1px 0 rgba(255, 246, 204, 0.65),
        0 0 14px rgba(255, 200, 70, 0.65),
        0 0 28px rgba(201, 112, 26, 0.45);
    }"""

new_footer_css = """/* Thanh Footer Menu: Nền trơn không viền, Chữ vàng kim đồng sang sát góc phải */
    .menu-dots {
      display: none !important; /* Loại bỏ các cục điều hướng theo yêu cầu */
    }

    .menu-footer-clean {
      display: flex;
      justify-content: flex-end; /* Nằm sát góc phải */
      align-items: center;
      width: 100%;
      max-width: 1440px;
      margin-top: clamp(14px, 2.2vh, 24px);
      padding: 0 clamp(20px, 3.5vw, 48px);
      box-sizing: border-box;
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
      z-index: 5;
    }

    .menu-all-dishes-gold-link {
      position: relative;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 0;
      padding: 8px 22px 9px;
      color: #C48B28; /* Vàng kim đồng đậm đà, đọc rõ nét trên nền kem */
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(14.5px, 1.25vw, 17.5px);
      font-weight: 700;
      letter-spacing: 2.4px;
      line-height: 1;
      text-transform: uppercase;
      text-decoration: none;
      background:
        linear-gradient(90deg, transparent 0%, rgba(196, 139, 40, 0.45) 18%, rgba(196, 139, 40, 0.95) 50%, rgba(196, 139, 40, 0.45) 82%, transparent 100%) center top / 100% 1.5px no-repeat,
        linear-gradient(90deg, transparent 0%, rgba(196, 139, 40, 0.45) 18%, rgba(196, 139, 40, 0.95) 50%, rgba(196, 139, 40, 0.45) 82%, transparent 100%) center bottom / 100% 1.5px no-repeat;
      transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
    }

    /* Khi hover: Lên màu Nâu Đen Cà Phê sắc lẹm, rõ nét 100% trên nền chính */
    .menu-all-dishes-gold-link:hover,
    .menu-all-dishes-gold-link:focus-visible {
      color: #1F120A; /* Nâu đen cà phê */
      transform: translateY(-2px);
      text-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);
      background:
        linear-gradient(90deg, transparent 0%, rgba(42, 22, 12, 0.5) 18%, rgba(31, 18, 10, 0.95) 50%, rgba(42, 22, 12, 0.5) 82%, transparent 100%) center top / 100% 1.8px no-repeat,
        linear-gradient(90deg, transparent 0%, rgba(42, 22, 12, 0.5) 18%, rgba(31, 18, 10, 0.95) 50%, rgba(42, 22, 12, 0.5) 82%, transparent 100%) center bottom / 100% 1.8px no-repeat;
    }"""

if old_footer_css in content:
    content = content.replace(old_footer_css, new_footer_css)
    print("Updated Menu Footer CSS (right-aligned, hidden dots, dark brown hover).")
else:
    print("Old Footer CSS block not matched!")

# -----------------------------------------------------------------------------
# 4. MOBILE CSS SYNC
# -----------------------------------------------------------------------------
old_mob_footer = """      .menu-footer-clean {
        margin-top: 14px;
      }"""

new_mob_footer = """      .menu-footer-clean {
        margin-top: 14px;
        justify-content: flex-end;
        padding: 0 20px;
      }"""

if old_mob_footer in content:
    content = content.replace(old_mob_footer, new_mob_footer)
    print("Updated Mobile Footer CSS (right-aligned on mobile).")
else:
    print("Mobile footer pattern not matched!")

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("ALL LAYOUT REFINEMENTS AND SYNC WRITTEN TO index.html SUCCESSFULLY!")
