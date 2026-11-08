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

# Crop wing foreground layer from original im (x=650..860, y=420..710)
wing_fg = im.crop((650, 420, 860, 710))

# Text layer
txt_layer = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(txt_layer)

font = ImageFont.truetype('timesbd.ttf', 135)
text = "HÀNG GÒN"
bbox = draw.textbbox((0, 0), text, font=font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]

cx = 760  # Center of wooden board
cy = 715 + H_ext  # Center of wooden board vertically in canvas
tx = cx - tw // 2
ty = cy - th // 2

# 3D carved wood effect
# Deep carved inner shadow
draw.text((tx - 3, ty - 3), text, fill=(20, 8, 3, 230), font=font)
draw.text((tx - 1, ty - 1), text, fill=(30, 12, 4, 240), font=font)
# Soft warm bottom specular bevel
draw.text((tx + 2, ty + 3), text, fill=(255, 240, 200, 180), font=font)
# Golden ivory face
draw.text((tx, ty), text, fill=(248, 224, 170, 255), font=font)

# Merge text
canvas = Image.alpha_composite(canvas, txt_layer)

# Composite wing foreground ON TOP of text
canvas.paste(wing_fg, (650, 420 + H_ext), wing_fg)

# Save as optimized webp
out_path = 'images/menu/chef-rooster-board.webp'
canvas.save(out_path, 'WEBP', quality=95)
print(f'Successfully exported {out_path} with size {canvas.size}')

# Also save full preview for inspection
proof_path = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\proof_chef_rooster_board_final.png'
canvas.save(proof_path)
print(f'Saved proof: {proof_path}')
