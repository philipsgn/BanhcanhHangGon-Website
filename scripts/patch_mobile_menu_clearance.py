import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace mobile menu styles in index.html to guarantee zero rooster-card collision on mobile
old_mobile_css = """@media (max-width: 600px) {
      #menu {
        min-height: 100vh;
        min-height: 100svh;
        padding: 12px 10px 14px;
        overflow: visible;
      }

      .menu-hero-header {
        position: absolute;
        top: 0;
        left: 10px;
        margin: 0;
        padding: 0;
      }

      .menu-hero-mascot {
        margin: 0 !important;
      }

      .menu-rooster-img {
        width: clamp(100px, 22vw, 130px);
      }

      .menu-carousel-track {
        height: clamp(330px, 48vh, 375px);
        margin-top: 0;
      }"""

new_mobile_css = """@media (max-width: 600px) {
      #menu {
        min-height: 100vh;
        min-height: 100svh;
        padding: clamp(8px, 1.5vh, 14px) 10px clamp(12px, 1.8vh, 18px);
        overflow: visible;
      }

      .menu-hero-header {
        position: absolute;
        top: clamp(6px, 1vh, 12px);
        left: clamp(8px, 2.5vw, 14px);
        margin: 0;
        padding: 0;
        z-index: 6;
      }

      .menu-hero-mascot {
        margin: 0 !important;
      }

      .menu-rooster-img {
        width: clamp(80px, 20vw, 96px);
      }

      .menu-carousel-track {
        height: clamp(335px, 48vh, 375px);
        margin-top: clamp(52px, 7.5vh, 68px);
      }"""

if old_mobile_css in html:
    html = html.replace(old_mobile_css, new_mobile_css)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated mobile CSS with zero-collision margin successfully!")
else:
    print("Old mobile CSS pattern not found verbatim, checking regex...")
    pattern = r'@media \(max-width:\s*600px\)\s*\{\s*#menu\s*\{[^}]*\}\s*\.menu-hero-header\s*\{[^}]*\}\s*\.menu-hero-mascot\s*\{[^}]*\}\s*\.menu-rooster-img\s*\{[^}]*\}\s*\.menu-carousel-track\s*\{[^}]*\}'
    if re.search(pattern, html):
        html = re.sub(pattern, new_mobile_css.strip(), html)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated via regex successfully!")
    else:
        print("Pattern match failed.")
