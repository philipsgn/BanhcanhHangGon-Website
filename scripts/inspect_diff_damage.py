import subprocess

# Let's inspect what was removed in git diff
p = subprocess.run(['git', 'diff', 'index.html'], capture_output=True, text=True, encoding='utf-8')
lines = p.stdout.split('\n')
removed_sections = set()
for l in lines:
    if l.startswith('-') and not l.startswith('---'):
        if 'SECTION' in l or '#greeting' in l or '#story' in l or '.greeting' in l or '.story' in l:
            removed_sections.add(l)

for r in list(removed_sections)[:30]:
    print(r)
