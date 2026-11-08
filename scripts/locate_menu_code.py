import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Locate CSS
start_css = c.find('/* ---------- SECTION 4 : MENU')
end_css = c.find('/* ---------- SECTION', start_css + 30)
if end_css == -1:
    end_css = c.find('</style>', start_css)
print(f"CSS range: {start_css} to {end_css} (length {end_css - start_css})")

# Locate Carousel JS in Script 1
s1_start = c.find('(function () {\n      const track = document.getElementById(\'menuTrack\');')
if s1_start == -1:
    s1_start = c.find('const track = document.getElementById(\'menuTrack\');')
print(f"JS start pos: {s1_start}")
if s1_start != -1:
    s1_end = c.find('})();', s1_start)
    if s1_end != -1:
        s1_end += 5
    print(f"JS end pos: {s1_end}")
    print(c[s1_start:s1_start+400])
