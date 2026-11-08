import os
import sys
from PIL import Image
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('images/menu/Gà trống mặc trang phục bên bảng gỗ.png')
arr = np.array(im)

# Sample a 200x200 patch in the middle of the board
patch = arr[500:700, 1000:1200, :3]
print('Patch mean RGB:', np.mean(patch, axis=(0,1)))
print('Patch min RGB:', np.min(patch, axis=(0,1)))
print('Patch max RGB:', np.max(patch, axis=(0,1)))
