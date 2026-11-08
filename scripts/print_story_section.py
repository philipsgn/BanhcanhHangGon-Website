import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

start = c.find('id="story"')
end = c.find('</section>', start)
print(c[start-20:end+12])
