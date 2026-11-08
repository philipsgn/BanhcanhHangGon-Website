import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

sections = re.findall(r'<section\b[^>]*id="([^"]+)"', c)
print("Sections in index.html:", sections)

comments = re.findall(r'/\* ---------- (SECTION [0-9]+ [^\*]+) ---------- \*/', c)
print("CSS Sections in index.html:", comments)

# Check specifically for Greeting & Story CSS classes
greeting_checks = ['.welcome-quote', '.welcome-section', '#welcome', '.welcome-content', '.hero-section', '#hero']
story_checks = ['#story', '.story-slider', '.story-slide', '.story-grid', '.story-visual-modern']

print("\nGreeting/Welcome CSS present:")
for g in greeting_checks:
    print(f"  {g}: {g in c}")

print("\nStory CSS present:")
for s in story_checks:
    print(f"  {s}: {s in c}")
