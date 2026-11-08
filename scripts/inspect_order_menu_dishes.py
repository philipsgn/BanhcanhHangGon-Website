import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('order.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'data-id="([^"]+)"\s+data-name="([^"]+)"\s+data-price="([^"]+)"', text)
print(f"Total dish items in order.html: {len(matches)}")
for d_id, d_name, d_price in matches:
    print(f"  {d_id}: '{d_name}' -> {int(d_price):,}₫")
