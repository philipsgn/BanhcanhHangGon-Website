import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Check welcome in CSS
m_welcome = re.search(r'/\* Section: welcome \*/.*?(?=/\*|\</style\>)', c, re.DOTALL)
if m_welcome:
    print("CURRENT WELCOME CSS:")
    print(m_welcome.group(0)[:800])
else:
    m_welcome2 = re.search(r'#welcome\s*\{.*?(?=/\*|\</style\>)', c, re.DOTALL)
    if m_welcome2:
        print("CURRENT WELCOME CSS 2:")
        print(m_welcome2.group(0)[:800])
    else:
        print("No welcome CSS found!")

# Check story in CSS
m_story = re.search(r'/\* ---------- SECTION 3 : STORY ---------- \*/.*?(?=/\* ---------- SECTION|\</style\>)', c, re.DOTALL)
if m_story:
    print("\nCURRENT STORY CSS:")
    print(m_story.group(0)[:800])
else:
    print("No story CSS found!")
