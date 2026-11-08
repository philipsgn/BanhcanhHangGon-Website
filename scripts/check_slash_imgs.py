import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

slash_imgs = re.findall(r'src=["\']/images/[^"\']+', c)
print(f"Total images with leading slash /images/: {len(slash_imgs)}")
for s in slash_imgs:
    print(s)
