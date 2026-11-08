import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find backstage section
m = re.search(r'<section id="backstage"[\s\S]*?</section>', text)
if m:
    print("=== HTML OF #backstage ===")
    print(m.group(0))

# Find backstage CSS
m_css = re.search(r'/\* ==+ SECTION: BACKSTAGE[\s\S]*?(?=/\* ==+|$)', text)
if m_css:
    print("\n=== CSS OF #backstage ===")
    print(m_css.group(0)[:1500])
