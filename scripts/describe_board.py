import os
import sys
from PIL import Image
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open(r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\board_full.jpg')
arr = np.array(im)
print('Board full size:', im.size)

# Let's inspect along a vertical slice down the middle of the board (x = 400 in this crop)
col = arr[:, 400, :3]
for y in range(0, len(col), 40):
    print(f'y={y}: RGB={col[y]}')
