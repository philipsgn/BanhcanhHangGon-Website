import os
import sys
from PIL import Image
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

p = 'images/menu/Gà trống mặc trang phục bên bảng gỗ.png'
im = Image.open(p)
w, h = im.size
print(f'Original size: {w}x{h}')

# Let's inspect where the board surface is
# Let's crop a few test patches of the board to find the center of the wooden board
# In previous check: board is around x=700..1400, y=350..850
board_crop = im.crop((850, 420, 1350, 780))
board_crop.convert('RGB').save(r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\board_center_test.jpg', 'JPEG')
print('Board center test saved!')
