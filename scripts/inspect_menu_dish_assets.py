import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

menu_files = [
    'Vietnamese Chicken Soup on Wooden Tray_result.webp',
    'Vietnamese Chicken Rice Tray Feast_result.webp',
    'Vietnamese Chicken Salad on Wooden Tray_result.webp',
    'Vietnamese Xôi Gà on a Wooden Tray_result.webp',
    'Gà trống mặc trang phục bên bảng gỗ.png'
]

for mf in menu_files:
    p = os.path.join('images/menu', mf)
    if os.path.exists(p):
        im = Image.open(p)
        print(f'{mf}: size={im.size}, mode={im.mode}')
    else:
        print(f'{mf}: NOT FOUND')
