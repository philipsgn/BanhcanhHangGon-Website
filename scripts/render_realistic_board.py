import os
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('images/menu/Gà trống mặc trang phục bên bảng gỗ.png').convert('RGBA')

# 1. Extend ropes upward by H_ext = 260px
H_ext = 260
new_H = im.height + H_ext
canvas = Image.new('RGBA', (im.width, new_H), (0, 0, 0, 0))

# Paste original image at y = H_ext
canvas.paste(im, (0, H_ext))

# Tile ropes up to y=0
left_segment = im.crop((287, 0, 318, 60))
right_segment = im.crop((1264, 0, 1295, 60))

for y in range(H_ext - 60, -60, -60):
    paste_y = max(0, y)
    crop_h = min(60, H_ext - y)
    canvas.paste(left_segment.crop((0, 0, left_segment.width, crop_h)), (287, paste_y))
    canvas.paste(right_segment.crop((0, 0, right_segment.width, crop_h)), (1264, paste_y))

# 2. Extract Wing Foreground Layer (to guarantee wing is on top of text)
# In original im: wing is roughly x=600..880, y=320..620
wing_fg = im.crop((600, 320, 880, 620))

# 3. Render "THỰC ĐƠN" onto the wooden board
# Center of board in canvas:
# In original im: cx ≈ 1060, cy ≈ 630
# In canvas: cx = 1060, cy = 630 + H_ext = 890
cx = 1060
cy = 890

txt_overlay = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(txt_overlay)

font_main = ImageFont.truetype('timesbd.ttf', 76)
font_sub = ImageFont.truetype('timesbd.ttf', 24)

text = "THỰC ĐƠN"
bbox = draw.textbbox((0, 0), text, font=font_main)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]

tx = cx - tw // 2
ty = cy - th // 2 - 10

# Engraved 3D wood effect:
# A) Dark inset shadow
draw.text((tx - 2, ty - 2), text, fill=(28, 12, 4, 220), font=font_main)
draw.text((tx - 1, ty - 1), text, fill=(38, 16, 5, 240), font=font_main)
# B) Warm gold bottom highlight
draw.text((tx + 1, ty + 2), text, fill=(255, 238, 195, 170), font=font_main)
# C) Main face: warm golden ivory leaf
draw.text((tx, ty), text, fill=(245, 218, 162, 255), font=font_main)

# Subtle decorative underline
line_y = ty + th + 18
draw.line([(cx - 70, line_y), (cx + 70, line_y)], fill=(245, 218, 162, 190), width=2)
draw.text((cx - 18, line_y - 12), "❖❖❖", fill=(245, 218, 162, 220), font=font_sub)

# Composite text onto canvas
canvas = Image.alpha_composite(canvas, txt_overlay)

# 4. Composite the Wing Foreground layer ON TOP of the text
# This ensures that any overlap is 100% underneath the rooster wing!
canvas.paste(wing_fg, (600, 320 + H_ext), wing_fg)

# Save test crop to verify
crop_proof = canvas.crop((550, 450, 1500, 1250))
crop_proof.save(r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\proof_wing_and_text_depth.png')
print('Saved proof_wing_and_text_depth.png!')

# Export optimized WebP
out_webp = 'images/menu/chef-rooster-board.webp'
canvas.save(out_webp, 'WEBP', quality=92, method=6)
print(f'Saved {out_webp}: size={os.path.getsize(out_webp)} bytes, dimensions={canvas.size}')
