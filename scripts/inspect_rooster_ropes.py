import os, sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

p = 'images/menu/original-chef-rooster-board.webp'
im = Image.open(p)
print(f"Asset size: {im.size}, mode: {im.mode}")

# Find bbox of non-transparent pixels
bbox = im.getbbox()
print(f"Non-transparent bbox: {bbox}")

# Check top row of pixels
alpha = im.getchannel('A')
top_y = bbox[1]
print(f"Top-most non-transparent pixel is at y = {top_y}")
