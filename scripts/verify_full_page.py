import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

print("--- SECTION TAGS ---")
for m in re.finditer(r'<section\b[^>]*id="([^"]+)"', c):
    print(f"Section id: {m.group(1)} at pos {m.start()}")

print("\n--- HERO VERIFICATION ---")
print("Has new-chicken-chef-desktop.webp:", "new-chicken-chef-desktop.webp" in c)
print("Has hero-quote:", "hero-quote" in c)

print("\n--- GREETING / WELCOME VERIFICATION ---")
print("Has welcome-corner-chick:", "welcome-corner-chick" in c)
print("Has cute-chicken.webp:", "cute-chicken.webp" in c)
print("Has framed-restaurant-storefront.webp:", "framed-restaurant-storefront.webp" in c)
print("Has welcome-divider:", "welcome-divider" in c)
print("Has welcome-label 'HƯƠNG VỊ GIA TRUYỀN':", "HƯƠNG VỊ GIA TRUYỀN" in c)

print("\n--- STORY VERIFICATION ---")
print("Has new-background-story-chicken.webp:", "new-background-story-chicken.webp" in c)
print("Has couplet 'Góc chợ Hàng Gòn bao năm qua vẫn vậy':", "Góc chợ <em>Hàng Gòn</em> bao năm qua vẫn vậy" in c)

print("\n--- MENU VERIFICATION ---")
print("Has original-chef-rooster-board.webp:", "original-chef-rooster-board.webp" in c)
print("Has 5 normalized dishes:", all(d in c for d in ["Vietnamese Chicken Soup", "Vietnamese Chicken Rice", "goi-ga.webp", "Vietnamese Xôi Gà", "mi-ga.webp"]))
print("Has menuTrack & menuDots:", "menuTrack" in c and "menuDots" in c)
