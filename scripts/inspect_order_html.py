import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

if os.path.exists('order.html'):
    with open('order.html', 'r', encoding='utf-8') as f:
        text = f.read()
    print("order.html length:", len(text))
    # Find dishes or sections
    import re
    dishes = re.findall(r'<div class=[\"\']item-name[\"\']>(.*?)</div>', text)
    print("Dishes in order.html:", len(dishes))
    for d in dishes[:15]:
        print("-", d)
