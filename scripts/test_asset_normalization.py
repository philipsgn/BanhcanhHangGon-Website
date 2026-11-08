import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.getcwd()

# 5 dishes
dish_paths = [
    os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Soup on Wooden Tray_result.webp'),
    os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Rice Tray Feast_result.webp'),
    os.path.join(ROOT, 'images', 'menu', 'goi-ga.webp'),
    os.path.join(ROOT, 'images', 'menu', 'Vietnamese Xôi Gà on a Wooden Tray_result.webp'),
    os.path.join(ROOT, 'images', 'menu', 'mi-ga.webp')
]

TARGET_SIZE = 1000
TARGET_TRAY_DIAMETER = 740 # Tray will be exactly 740px diameter, leaving (1000-740)/2 = 130px top and bottom padding!

for p in dish_paths:
    im = Image.open(p).convert('RGBA')
    bbox = im.getbbox()
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    tray_crop = im.crop(bbox)
    
    # Scale tray so its max dimension is exactly TARGET_TRAY_DIAMETER
    scale = TARGET_TRAY_DIAMETER / max(w, h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    tray_scaled = tray_crop.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Place on 1000x1000 square perfectly centered
    norm_canvas = Image.new('RGBA', (TARGET_SIZE, TARGET_SIZE), (0, 0, 0, 0))
    paste_x = (TARGET_SIZE - new_w) // 2
    paste_y = (TARGET_SIZE - new_h) // 2
    norm_canvas.paste(tray_scaled, (paste_x, paste_y), tray_scaled)
    
    new_bbox = norm_canvas.getbbox()
    print(f"File {os.path.basename(p)}:")
    print(f"  Old bbox: {bbox} -> New bbox: {new_bbox}")
    print(f"  Top padding: {new_bbox[1]}px, Bottom padding: {TARGET_SIZE - new_bbox[3]}px")
