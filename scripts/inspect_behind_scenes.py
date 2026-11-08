import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

for m in re.finditer(r'images/behind-scenes/[^"\'\s)]+', c):
    print("Found reference in index.html:", m.group(0))

# Find the section containing behind-scenes
pos = c.find('images/behind-scenes/')
if pos != -1:
    sec_start = c.rfind('<section', 0, pos)
    sec_end = c.find('</section>', pos)
    if sec_start != -1 and sec_end != -1:
        print("\n=== SECTION WITH BEHIND-SCENES ===")
        print(c[sec_start:sec_end+10])
