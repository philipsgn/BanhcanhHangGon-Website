import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

INDEX_HTML = 'index.html'
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    content = f.read()

target = "Hàng Gòn tự hào mang đến hương vị bánh canh gà đậm đà giữa lòng thành phố. Từng"
assert target in content, "target not found"

# Replace the paragraph content
import re
pattern = re.compile(r'<p class="welcome-description">.*?</p>', re.DOTALL)
replacement = '''<p class="welcome-description">Hàng Gòn tự hào mang đến hương vị bánh canh gà đậm đà giữa lòng thành phố. Từng
          tô canh được nấu mỗi ngày với nước lèo ninh xương, thịt gà tươi chọn lọc, giữ trọn vẹn sự ngọt thanh nguyên
          bản như thuở ban đầu.
        </p>'''

content = pattern.sub(replacement, content, count=1)

with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated welcome-description successfully!")
