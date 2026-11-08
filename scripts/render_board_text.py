import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

src = 'images/menu/Gà trống mặc trang phục bên bảng gỗ.png'
im = Image.open(src).convert('RGBA')

# Target board area center in original image:
# x ≈ 1120, y ≈ 620
# Let's test placing "THỰC ĐƠN"
# Font: serif or clean display
try:
    font_large = ImageFont.truetype('georgiab.ttf', 72)
    font_sub = ImageFont.truetype('georgiai.ttf', 32)
except:
    font_large = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# We can render onto an overlay
txt_overlay = Image.new('RGBA', im.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(txt_overlay)

text = "THỰC ĐƠN"
# Measure text
bbox = draw.textbbox((0, 0), text, font=font_large)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]

# Center of board surface: cx ≈ 1140, cy ≈ 610
cx, cy = 1140, 610
tx = cx - tw // 2
ty = cy - th // 2

# Subtle engraved effect:
# 1. Dark inner bevel shadow (offset -1, -1)
draw.text((tx - 1, ty - 1), text, fill=(35, 15, 5, 200), font=font_large)
# 2. Warm gold / cream highlight (offset +1, +1)
draw.text((tx + 1, ty + 1), text, fill=(255, 235, 190, 160), font=font_large)
# 3. Main face: rich warm ivory/gold leaf
draw.text((tx, ty), text, fill=(248, 222, 170, 240), font=font_large)

# Small decorative flourish underneath
line_y = ty + th + 18
draw.line([(cx - 60, line_y), (cx + 60, line_y)], fill=(248, 222, 170, 180), width=2)
draw.text((cx - 6, line_y - 8), "❖", fill=(248, 222, 170, 220), font=font_sub)

# Composite
result = Image.alpha_composite(im, txt_overlay)

# Save test crop
crop_test = result.crop((700, 250, 1500, 980))
crop_test.convert('RGB').save(r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\board_with_text_test.jpg', 'JPEG')
print('Board with text test saved!')

# Also export full WebP version
out_webp = 'images/menu/chef-rooster-board.webp'
result.save(out_webp, 'WEBP', quality=92, method=6)
print(f'Saved full {out_webp}, size = {os.path.getsize(out_webp)} bytes')
