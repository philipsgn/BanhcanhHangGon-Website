import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

src_path = 'images/menu/Gà trống mặc trang phục bên bảng gỗ.png'
im = Image.open(src_path).convert('RGBA')

# Canvas with H_ext = 260 for ceiling ropes
H_ext = 260
new_H = im.height + H_ext
canvas = Image.new('RGBA', (im.width, new_H), (0, 0, 0, 0))
canvas.paste(im, (0, H_ext))

# Tile ropes up to ceiling
left_segment = im.crop((287, 0, 318, 60))
right_segment = im.crop((1264, 0, 1295, 60))
for y in range(H_ext - 60, -60, -60):
    paste_y = max(0, y)
    crop_h = min(60, H_ext - y)
    canvas.paste(left_segment.crop((0, 0, left_segment.width, crop_h)), (287, paste_y))
    canvas.paste(right_segment.crop((0, 0, right_segment.width, crop_h)), (1264, paste_y))

# Text layer - shifted down to lower half of wooden board
# Wing ends at y = 690 + 260 = 950.
# Board bottom is at y = 960 + 260 = 1220.
# Center text vertically in the clear area: cy = 800 + 260 = 1060px.
txt_layer = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(txt_layer)

font = ImageFont.truetype('timesbd.ttf', 125)
text = "HÀNG GÒN"
bbox = draw.textbbox((0, 0), text, font=font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]

cx = 760  # Center of wooden board horizontally
cy = 800 + H_ext  # Shifted down vertically, zero touching with feathers
tx = cx - tw // 2
ty = cy - th // 2

# 3D carved wood effect
# Deep carved inner shadow
draw.text((tx - 3, ty - 3), text, fill=(20, 8, 3, 230), font=font)
draw.text((tx - 1, ty - 1), text, fill=(30, 12, 4, 240), font=font)
# Warm bottom specular bevel
draw.text((tx + 2, ty + 3), text, fill=(255, 240, 200, 180), font=font)
# Golden ivory face
draw.text((tx, ty), text, fill=(248, 224, 170, 255), font=font)

# Merge text onto canvas
canvas = Image.alpha_composite(canvas, txt_layer)

# Save as optimized webp
out_path = 'images/menu/chef-rooster-board.webp'
canvas.save(out_path, 'WEBP', quality=95)
print(f'Successfully re-exported {out_path} with text shifted down cleanly!')
