import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [line for line in text.splitlines() if 'storySlider' in line or 'story-slide' in line]
for l in matches:
    print(l)
