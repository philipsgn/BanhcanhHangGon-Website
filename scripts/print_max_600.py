import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('@media (max-width: 600px)')
if pos != -1:
    print(c[pos:pos+1500])
