import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

rooster = Image.open('images/menu/chef-rooster-board.webp').convert('RGBA')

# Target Header Banner: 1200 x 500
W, H = 1200, 500
bg = Image.new('RGB', (W, H), (247, 245, 240)) # Warm paper tone
draw = ImageDraw.Draw(bg)

# Scale rooster
rw = 480
rh = int(rw * rooster.height / rooster.width)
rooster_scaled = rooster.resize((rw, rh), Image.Resampling.LANCZOS)

# Paste rooster on the left of header
bg.paste(rooster_scaled, (40, (H - rh) // 2 + 10), rooster_scaled)

# Right of header: Text and Badge like reference
try:
    font_script = ImageFont.truetype('georgiai.ttf', 36)
    font_badge = ImageFont.truetype('arialbd.ttf', 24)
    font_sub = ImageFont.truetype('arial.ttf', 16)
except:
    font_script = ImageFont.load_default()
    font_badge = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# Script: Hàng Gòn
draw.text((560, 140), "Hàng Gòn", fill=(181, 107, 48), font=font_script)

# Black badge: THỰC ĐƠN ĐẶC SẢN
badge_x, badge_y = 560, 195
badge_w, badge_h = 280, 52
draw.rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + badge_h], fill=(20, 20, 20))
draw.text((badge_x + 22, badge_y + 12), "THỰC ĐƠN ĐẶC SẢN", fill=(255, 255, 255), font=font_badge)

# Subtitle
sub_text = [
    "Khách ghé Hàng Gòn, hãy thong thả dừng chân thưởng thức",
    "hương vị gà ta truyền thống ngọt thanh từ xương ninh,",
    "thịt gà tươi chọn lọc — phục vụ nóng hổi mỗi ngày."
]
sy = 270
for st in sub_text:
    draw.text((560, sy), st, fill=(80, 70, 65), font=font_sub)
    sy += 26

test_out = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\menu_header_test.jpg'
bg.save(test_out, 'JPEG', quality=88)
print('Saved menu_header_test.jpg')
