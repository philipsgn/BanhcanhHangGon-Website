import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'(// === CAROUSEL.*?)(?=</script>)', c, re.DOTALL)
if not m:
    m = re.search(r'(updateCarousel.*?)(?=</script>)', c, re.DOTALL)

if m:
    print(m.group(0)[:1500])
