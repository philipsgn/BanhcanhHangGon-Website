import os
import sys
from PIL import Image
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

src = 'images/menu/Gà trống mặc trang phục bên bảng gỗ.png'
im = Image.open(src).convert('RGBA')
arr = np.array(im)

# Let's crop a patch around the wing resting on the board:
# x: 600..900, y: 300..650
patch = im.crop((600, 300, 950, 650))
patch.save(r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\wing_patch.png')
print('Saved wing_patch.png')
