import os
import sys
from PIL import Image
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('images/menu/Gà trống mặc trang phục bên bảng gỗ.png')
# Crop the left rope and right rope
left_rope = im.crop((280, 0, 325, 120))
right_rope = im.crop((1255, 0, 1305, 120))

left_rope.save(r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\left_rope.png')
right_rope.save(r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\right_rope.png')
print('Ropes saved!')
