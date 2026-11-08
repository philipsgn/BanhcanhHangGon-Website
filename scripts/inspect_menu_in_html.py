import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('id="menu"')
print("FOUND MENU AT:", pos)
if pos != -1:
    print("--- BEFORE MENU ---")
    print(c[max(0, pos-400):pos])
    print("--- MENU HTML START ---")
    print(c[pos:pos+1500])
