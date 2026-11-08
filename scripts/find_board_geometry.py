import os
import sys
from PIL import Image
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

im = Image.open('images/menu/Gà trống mặc trang phục bên bảng gỗ.png')
arr = np.array(im)
alpha = arr[:, :, 3]

# Where are the edges of the board?
# In the right region (x > 800):
# Find top and bottom edge of the board across x=900, 1000, 1100, 1200, 1300
for x in [850, 950, 1050, 1150, 1250, 1350]:
    ys = np.where(alpha[:, x] > 50)[0]
    if len(ys) > 0:
        print(f'x={x}: y_min={ys[0]}, y_max={ys[-1]}, height={ys[-1]-ys[0]}')
