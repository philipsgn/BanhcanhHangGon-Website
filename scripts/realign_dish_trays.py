import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

images = [
    ('Bánh canh', 'images/menu/Vietnamese Chicken Soup on Wooden Tray_result.webp'),
    ('Cơm gà', 'images/menu/Vietnamese Chicken Rice Tray Feast_result.webp'),
    ('Gỏi gà', 'images/menu/goi-ga.webp'),
    ('Xôi gà', 'images/menu/Vietnamese Xôi Gà on a Wooden Tray_result.webp'),
    ('Mì gà', 'images/menu/mi-ga.webp')
]

TARGET_SIZE = 1000
PLATE_DIM = 820
TARGET_BOTTOM = 810  # Leaves 190px of transparent air at the bottom

for name, p in images:
    if not os.path.exists(p):
        print(f'Missing: {p}')
        continue
    im = Image.open(p).convert('RGBA')
    bbox = im.getbbox()
    cropped = im.crop(bbox)
    cw, ch = cropped.size
    
    scale = PLATE_DIM / max(cw, ch)
    nw = int(round(cw * scale))
    nh = int(round(ch * scale))
    resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)
    
    canvas = Image.new('RGBA', (TARGET_SIZE, TARGET_SIZE), (0, 0, 0, 0))
    px = (TARGET_SIZE - nw) // 2
    py = TARGET_BOTTOM - nh
    canvas.paste(resized, (px, py), resized)
    
    canvas.save(p, 'WEBP', quality=95)
    print(f'Processed {name} ({p}): nw={nw}, nh={nh}, px={px}, py={py}, bottom={py+nh}px')

print('All 5 dish tray images realigned successfully!')
