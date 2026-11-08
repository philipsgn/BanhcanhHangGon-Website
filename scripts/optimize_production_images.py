import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

conversions = [
    ('images/order/background-order.jpg', 'images/order/background-order.webp', 86),
    ('images/order/clipboard_top_clamp.png', 'images/order/clipboard_top_clamp.webp', 90),
    ('images/order/add-to-cart.png', 'images/order/add-to-cart.webp', 90),
    ('images/order/cham-bi.jpg', 'images/order/cham-bi.webp', 88),
]

saved_bytes = 0
for src, dst, q in conversions:
    if os.path.exists(src):
        im = Image.open(src)
        im.save(dst, 'WEBP', quality=q, method=6)
        s1 = os.path.getsize(src)
        s2 = os.path.getsize(dst)
        saved = s1 - s2
        saved_bytes += saved
        print(f"Converted {src} ({s1/1024:.1f} KB) -> {dst} ({s2/1024:.1f} KB) [Saved {saved/1024:.1f} KB - {(1 - s2/s1)*100:.1f}%]")
    else:
        print(f"Source not found: {src}")

print(f"\nTotal image bytes saved from conversions: {saved_bytes/1024:.1f} KB ({saved_bytes/(1024*1024):.2f} MB)")
