import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

# Check sizes and bounding boxes of all 5 dish images
dish_files = [
    'images/menu/Vietnamese Chicken Soup on Wooden Tray_result.webp',
    'images/menu/Vietnamese Chicken Rice Tray Feast_result.webp',
    'images/menu/goi-ga.webp',
    'images/menu/Vietnamese Xôi Gà on a Wooden Tray_result.webp',
    'images/menu/mi-ga.webp',
    'images/menu/original-chef-rooster-board.webp'
]

for p in dish_files:
    try:
        im = Image.open(p)
        bbox = im.getbbox()
        print(f"File: {p}")
        print(f"  Canvas size: {im.size}")
        print(f"  Non-transparent BBox: {bbox}")
        if bbox:
            print(f"  Visible Content: width={bbox[2]-bbox[0]}, height={bbox[3]-bbox[1]}")
            print(f"  Top padding: {bbox[1]}px, Bottom padding: {im.size[1]-bbox[3]}px")
    except Exception as e:
        print(f"Error {p}: {e}")
