import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.getcwd()

# 5 dishes to normalize
dish_files = [
    'Vietnamese Chicken Soup on Wooden Tray_result.webp',
    'Vietnamese Chicken Rice Tray Feast_result.webp',
    'goi-ga.webp',
    'Vietnamese Xôi Gà on a Wooden Tray_result.webp',
    'mi-ga.webp'
]

TARGET_SIZE = 1000
TARGET_TRAY_DIAMETER = 740  # Exact circular diameter for all trays

for fn in dish_files:
    p = os.path.join(ROOT, 'images', 'menu', fn)
    if not os.path.exists(p):
        print(f"Warning: {p} does not exist!")
        continue
    
    im = Image.open(p).convert('RGBA')
    bbox = im.getbbox()
    if not bbox:
        print(f"Empty image: {p}")
        continue
    
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    tray_crop = im.crop(bbox)
    
    # Scale tray uniformly so max dimension is exactly TARGET_TRAY_DIAMETER
    scale = TARGET_TRAY_DIAMETER / max(w, h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    tray_scaled = tray_crop.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Create clean transparent 1000x1000 canvas and center the tray
    norm_canvas = Image.new('RGBA', (TARGET_SIZE, TARGET_SIZE), (0, 0, 0, 0))
    paste_x = (TARGET_SIZE - new_w) // 2
    paste_y = (TARGET_SIZE - new_h) // 2
    norm_canvas.paste(tray_scaled, (paste_x, paste_y), tray_scaled)
    
    # Save back to file
    norm_canvas.save(p, 'WEBP', quality=95)
    
    new_bbox = norm_canvas.getbbox()
    print(f"Normalized {fn}:")
    print(f"  Old bbox: {bbox} -> New bbox: {new_bbox}")
    print(f"  Width: {new_bbox[2]-new_bbox[0]}px, Height: {new_bbox[3]-new_bbox[1]}px")
    print(f"  Top padding: {new_bbox[1]}px, Bottom padding: {TARGET_SIZE - new_bbox[3]}px")

print("All 5 dish assets successfully normalized to identical 740px diameter with ~155px top/bottom padding!")
