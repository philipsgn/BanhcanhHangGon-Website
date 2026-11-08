import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's inspect everything between `<style>` and `</style>` that mentions `menu-`
matches = re.findall(r'(\.[a-zA-Z0-9_-]*menu[a-zA-Z0-9_-]*\s*\{[^}]+\})', c)
print(f"Found {len(matches)} menu rules:")
for r in matches:
    print(r)
