import os
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('images/menu/Gà trống mặc trang phục bên bảng gỗ.png').convert('RGBA')

# Canvas with H_ext = 260 for ceiling ropes
H_ext = 260
new_H = im.height + H_ext
canvas = Image.new('RGBA', (im.width, new_H), (0, 0, 0, 0))
canvas.paste(im, (0, H_ext))

# Tile ropes
left_segment = im.crop((287, 0, 318, 60))
right_segment = im.crop((1264, 0, 1295, 60))
for y in range(H_ext - 60, -60, -60):
    paste_y = max(0, y)
    crop_h = min(60, H_ext - y)
    canvas.paste(left_segment.crop((0, 0, left_segment.width, crop_h)), (287, paste_y))
    canvas.paste(right_segment.crop((0, 0, right_segment.width, crop_h)), (1264, paste_y))

# Wing foreground layer in original im: x=600..880, y=320..620
# In canvas: y is shifted by H_ext
wing_fg = im.crop((600, 320, 880, 620))

# Test different font sizes and positions for "HÀNG GÒN"
# Wooden board center is around cx = 1040, cy = 600..660 in original im -> 860..920 in canvas.
# Wing feathers reach up to x ≈ 820..840, y_canvas ≈ 800..850.
# If "HÀNG GÒN" is at cx ≈ 1040, cy ≈ 840 (center of board height):
# With font size 100px:
# Width of "HÀNG GÒN" is ~550px.
# Left edge tx = 1040 - 275 = 765px!
# Notice: tx = 765px is directly under the wing feathers (x=650..840)!
# The letter 'H' and 'À' will fall between x=765 and x=870!
# This means 'H' and part of 'À' will be partially covered by the wing feathers!

txt_overlay = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(txt_overlay)

font_main = ImageFont.truetype('timesbd.ttf', 108)

text = "HÀNG GÒN"
bbox = draw.textbbox((0, 0), text, font=font_main)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]

cx = 1060
cy = 840
tx = cx - tw // 2
ty = cy - th // 2

print(f'Text bbox: x from {tx} to {tx+tw}, y from {ty} to {ty+th}')

# 3D carved wood effect
# A) Dark inset shadow
draw.text((tx - 2, ty - 2), text, fill=(24, 10, 4, 230), font=font_main)
draw.text((tx - 1, ty - 1), text, fill=(34, 14, 5, 240), font=font_main)
# B) Warm gold bottom highlight
draw.text((tx + 1, ty + 2), text, fill=(255, 238, 195, 175), font=font_main)
# C) Main face: rich warm golden ivory leaf
draw.text((tx, ty), text, fill=(246, 220, 166, 255), font=font_main)

# Composite text onto canvas
canvas = Image.alpha_composite(canvas, txt_overlay)

# Stamp wing foreground ON TOP of text
canvas.paste(wing_fg, (600, 320 + H_ext), wing_fg)

# Save test crop to verify visual overlap
test_crop = canvas.crop((550, 480, 1500, 1250))
test_crop.save(r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\test_hang_gon_wing_overlap.png')
print('Saved test_hang_gon_wing_overlap.png successfully!')
