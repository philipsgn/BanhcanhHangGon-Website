import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

start = c.find('/* ---------- SECTION 4 : MENU')
end = c.find('/* ---------- SECTION 3 : STORY', start)
print(f"Current Menu CSS length: {end - start} chars")
print(c[start:start+600])
