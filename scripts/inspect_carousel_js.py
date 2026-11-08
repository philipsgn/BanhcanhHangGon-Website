import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find the carousel script
match = re.search(r'// =+\s*CAROUSEL.*?// =+', c, re.DOTALL)
if not match:
    match = re.search(r'function updateMenuCarousel.*?function', c, re.DOTALL)
if not match:
    match = re.search(r'const menuCards =.*?function update', c, re.DOTALL)

if match:
    print("Found carousel script:")
    print(match.group(0)[:2000])
else:
    # search for menuCards
    pos = c.find('menuCards')
    if pos != -1:
        print("Found menuCards at pos:", pos)
        print(c[pos-100:pos+1500])
    else:
        print("menuCards not found")
