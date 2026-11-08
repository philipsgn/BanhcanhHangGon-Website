import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

pairs = [
    ('images/webp/tray_banh_canh.webp', 'images/menu/Vietnamese Chicken Soup on Wooden Tray_result.webp'),
    ('images/webp/tray_com_ga.webp', 'images/menu/Vietnamese Chicken Rice Tray Feast_result.webp'),
    ('images/webp/tray_goi_ga.webp', 'images/menu/Vietnamese Chicken Salad on Wooden Tray_result.webp'),
    ('images/webp/tray_xoi_ga.webp', 'images/menu/Vietnamese Xôi Gà on a Wooden Tray_result.webp')
]

for p1, p2 in pairs:
    s1 = f'size={Image.open(p1).size}' if os.path.exists(p1) else 'NOT FOUND'
    s2 = f'size={Image.open(p2).size}' if os.path.exists(p2) else 'NOT FOUND'
    print(f'{p1}: {s1} | {p2}: {s2}')
