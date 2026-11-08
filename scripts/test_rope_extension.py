import os
import sys
from PIL import Image
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('images/menu/Gà trống mặc trang phục bên bảng gỗ.png').convert('RGBA')
arr = np.array(im)

# Left rope is at x=287..318
# Right rope is at x=1264..1295
# Let's inspect the rope segment between y=0 and y=60:
left_segment = im.crop((287, 0, 318, 60))
right_segment = im.crop((1264, 0, 1295, 60))

# If we extend the image upward by H_ext = 260px:
H_ext = 260
new_H = im.height + H_ext
new_im = Image.new('RGBA', (im.width, new_H), (0, 0, 0, 0))

# Paste original image at y = H_ext
new_im.paste(im, (0, H_ext))

# Tile the left rope and right rope seamlessly upward from y=H_ext to y=0:
# Segment height is 60px
for y in range(H_ext - 60, -60, -60):
    paste_y = max(0, y)
    crop_h = min(60, H_ext - y)
    new_im.paste(left_segment.crop((0, 0, left_segment.width, crop_h)), (287, paste_y))
    new_im.paste(right_segment.crop((0, 0, right_segment.width, crop_h)), (1264, paste_y))

print('Extended image size:', new_im.size)
# Verify that ropes reach y=0
arr_new = np.array(new_im)
print('Alpha at y=0, left rope:', np.max(arr_new[0, 287:318, 3]))
print('Alpha at y=0, right rope:', np.max(arr_new[0, 1264:1295, 3]))

new_im.save(r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\extended_ropes_test.png')
print('Saved extended_ropes_test.png')
