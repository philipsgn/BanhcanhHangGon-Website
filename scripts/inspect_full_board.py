import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

# Let's save a view of the full board area
im = Image.open('images/menu/Gà trống mặc trang phục bên bảng gỗ.png')
board_full = im.crop((700, 250, 1500, 980))
board_full.convert('RGB').save(r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\board_full.jpg', 'JPEG')
print('Saved board_full.jpg')
