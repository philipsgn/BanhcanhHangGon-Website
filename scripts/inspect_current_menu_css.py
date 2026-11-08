import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

start_css = c.find('/* ---------- SECTION 4 : MENU')
end_css = c.find('/* ---------- SECTION', start_css + 30)
if end_css == -1:
    end_css = c.find('</style>', start_css)

print(f"Current menu CSS length: {end_css - start_css}")
print(c[start_css:start_css+1500])
