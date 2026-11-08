import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

bg_path = 'images/story/new-background-story-chicken.webp'
im = Image.open(bg_path).convert('RGBA')

# Target Section 3 render size: 1400 x 500
W, H = 1400, 500
scaled_bg = im.resize((W, int(W * im.height / im.width)), Image.Resampling.LANCZOS)
# Crop center
cy = (scaled_bg.height - H) // 2
crop_bg = scaled_bg.crop((0, max(0, cy), W, max(0, cy) + H))

# Apply gradient overlay:
# linear-gradient(90deg, rgba(18, 10, 7, .46), transparent 60%)
# linear-gradient(180deg, rgba(18, 10, 7, .08), rgba(18, 10, 7, .62))
overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
odraw = ImageDraw.Draw(overlay)

import numpy as np
ov_arr = np.zeros((H, W, 4), dtype=np.uint8)

for x in range(W):
    alpha_h = int(255 * 0.50 * max(0, 1.0 - x / (W * 0.65)))
    ov_arr[:, x, 0] = 18
    ov_arr[:, x, 1] = 10
    ov_arr[:, x, 2] = 7
    ov_arr[:, x, 3] = np.maximum(ov_arr[:, x, 3], alpha_h)

for y in range(H):
    alpha_v = int(255 * (0.10 + 0.55 * (y / H)))
    ov_arr[y, :, 0] = 18
    ov_arr[y, :, 1] = 10
    ov_arr[y, :, 2] = 7
    ov_arr[y, :, 3] = np.maximum(ov_arr[y, :, 3], alpha_v)

overlay = Image.fromarray(ov_arr, 'RGBA')
composite = Image.alpha_composite(crop_bg.convert('RGBA'), overlay)

# Draw quote text
draw = ImageDraw.Draw(composite)
try:
    font_quote = ImageFont.truetype('georgiab.ttf', 42)
except:
    font_quote = ImageFont.load_default()

# Shadow
shadow_color = (0, 0, 0, 180)
text_line1 = '“Góc chợ Hàng Gòn bao năm qua vẫn vậy,'
text_line2 = 'Gìn giữ vị quê đượm ấm bát canh đầy.”'

tx, ty = 80, H - 150
draw.text((tx+2, ty+2), text_line1, fill=(0, 0, 0), font=font_quote)
draw.text((tx+2, ty+52), text_line2, fill=(0, 0, 0), font=font_quote)

draw.text((tx, ty), text_line1, fill=(255, 246, 230), font=font_quote)
draw.text((tx, ty+50), text_line2, fill=(255, 246, 230), font=font_quote)

proof_out = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf\proof_section3_story.png'
composite.convert('RGB').save(proof_out)
print(f'Exported {proof_out}')
