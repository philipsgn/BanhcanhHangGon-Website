import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Search for updateCarousel or carousel script
m = re.findall(r'(\.menu-card\.is-active[^{]*\{[^}]+\})', c)
for r in m:
    print("ACTIVE CARD CSS:", r)

# Search for carousel JS logic
js_match = re.search(r'(function\s+updateCarousel\b.*?)(?=</script>)', c, re.DOTALL)
if js_match:
    print("JS CAROUSEL:")
    print(js_match.group(0)[:1500])
else:
    # search any carousel script
    m2 = re.search(r'(menuTrack.*?)(?=</script>)', c, re.DOTALL)
    if m2:
        print("JS TRACK SCRIPT:")
        print(m2.group(0)[:1500])
