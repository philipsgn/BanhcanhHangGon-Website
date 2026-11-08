import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

start = c.find('/* ---------- SECTION 4 : MENU')
if start != -1:
    end = c.find('/* ---------- SECTION', start + 30)
    if end == -1:
        end = c.find('</style>', start)
    print("Found menu css, length:", end - start)
    print(c[start:start+2500])
else:
    print("Not found SECTION 4 : MENU")
