import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.getcwd()
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf'

imgs = [
    ('highlights-1.webp', 'images/highlights/highlights-1.webp'),
    ('highlights-4.webp', 'images/highlights/highlights-4.webp'),
    ('hightlights.webp', 'images/highlights/hightlights.webp'),
    ('higlights-3.webp', 'images/highlights/higlights-3.webp')
]

# Create a 2x2 collage preview
w, h = 800, 800
canvas = Image.new('RGB', (w, h), (30, 25, 22))

for i, (name, rel_p) in enumerate(imgs):
    im = Image.open(os.path.join(ROOT, rel_p))
    # resize to 380x380
    im_fit = im.resize((380, 380), Image.Resampling.LANCZOS)
    col = i % 2
    row = i // 2
    x = 15 + col * 400
    y = 15 + row * 400
    canvas.paste(im_fit, (x, y))

out_p = os.path.join(ARTIFACT_DIR, 'highlights_preview_collage.jpg')
canvas.save(out_p, quality=85)
print('Saved collage preview to:', out_p)
