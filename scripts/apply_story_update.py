import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

INDEX_HTML = 'index.html'
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for Section 3: Story
old_story_re = re.compile(
    r'<!-- SECTION 3: STORY -->\s*'
    r'<section id="story">.*?'
    r'</section>',
    re.DOTALL
)

new_story_html = '''<!-- SECTION 3: STORY -->
  <section id="story">
    <div class="story-slider" aria-label="Câu chuyện Hàng Gòn">
      <article class="story-slide is-active">
        <picture>
          <source srcset="images/story/new-background-story-chicken.webp" type="image/webp">
          <img src="images/story/new-background-story-chicken.png" alt="Không gian mộc mạc và câu chuyện truyền thống quán Bánh Canh Gà Hàng Gòn"
            loading="lazy" decoding="async">
        </picture>
        <div class="story-slide__content">
          <p class="story-slide__quote">“Góc chợ <em>Hàng Gòn</em> bao năm qua vẫn vậy,<br>Gìn giữ vị quê đượm ấm bát canh đầy.”</p>
        </div>
      </article>
    </div>
  </section>'''

assert old_story_re.search(content), "old_story_re not matched"
content = old_story_re.sub(new_story_html, content, count=1)
print("1. Section 3 markup updated with new background image and poetic quote")

with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(content)

print("-> index.html successfully updated!")
