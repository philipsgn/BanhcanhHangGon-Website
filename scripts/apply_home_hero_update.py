import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

INDEX_HTML = 'index.html'
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Preload in <head>
old_preload = '<link rel="preload" as="image" href="/images/home/background_result.webp" fetchpriority="high">'
new_preload = '''  <link rel="preload" as="image" href="/images/home/new-chicken-chef-desktop.webp" media="(min-width: 881px)" fetchpriority="high">
  <link rel="preload" as="image" href="/images/home/new-chicken-chef-mobile.webp" media="(max-width: 880px)" fetchpriority="high">'''

assert old_preload in content, "old_preload not found"
content = content.replace(old_preload, new_preload, 1)
print("1. Preload updated in <head>")

# 2. Add .hero-picture and update .hero-bg-photo in Desktop CSS
old_hero_desktop_css = '''    .hero-panorama {
      position: absolute;
      inset: 0;
      z-index: 0;
      overflow: hidden;
    }

    .hero-bg-photo {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 42%;
      z-index: 0;
    }'''

new_hero_desktop_css = '''    .hero-panorama {
      position: absolute;
      inset: 0;
      z-index: 0;
      overflow: hidden;
    }

    .hero-picture {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      display: block;
      z-index: 0;
    }

    .hero-bg-photo {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center center;
      z-index: 0;
    }'''

assert old_hero_desktop_css in content, "old_hero_desktop_css not found"
content = content.replace(old_hero_desktop_css, new_hero_desktop_css, 1)
print("2. Desktop CSS updated")

# 3. Clean up .hero-bg-photo polish override
content = content.replace('    .hero-bg-photo {\n      object-position: 66% 46%;\n    }', '    .hero-bg-photo {\n      object-position: center center;\n    }', 1)
print("3. Polish override updated")

# 4. Update Mobile Media Query (first occurrence around line 1800)
# Replace lines 1795-1864 block for hero
old_mobile_hero_1 = re.compile(r'#hero\s*\{[^}]*display:\s*flex;\s*flex-direction:\s*column;.*?\.hero-bg-photo\s*\{[^}]*aspect-ratio:\s*1672\s*/\s*941;[^}]*\}', re.DOTALL)
new_mobile_hero_1 = '''#hero {
        min-height: 100svh;
        height: 100svh;
        display: flex;
        align-items: flex-end;
        justify-content: flex-start;
        position: relative;
        overflow: hidden;
        background: var(--bg-deep);
      }

      .hero-panorama {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        flex: none;
        overflow: hidden;
      }

      .hero-picture {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        display: block;
      }

      .hero-bg-photo {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center top;
        user-select: none;
        -webkit-user-drag: none;
      }

      .hero-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg,
            rgba(16, 8, 5, 0.45) 0%,
            rgba(16, 8, 5, 0.05) 30%,
            rgba(16, 8, 5, 0.15) 60%,
            rgba(24, 14, 8, 0.88) 100%);
        pointer-events: none;
        z-index: 1;
      }

      .hero-content {
        position: relative;
        z-index: 2;
        width: 100%;
        min-height: auto;
        padding: 0 24px clamp(32px, 6svh, 56px);
        display: flex;
        align-items: flex-end;
        justify-content: flex-start;
        background: transparent;
        pointer-events: none;
      }

      .hero-quote {
        white-space: normal;
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(24px, 6.5vw, 34px);
        font-weight: 600;
        line-height: 1.25;
        color: var(--cream);
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.9);
        letter-spacing: 0.2px;
      }'''

assert old_mobile_hero_1.search(content), "old_mobile_hero_1 not found"
content = old_mobile_hero_1.sub(new_mobile_hero_1, content, count=1)
print("4. Mobile Media Query 1 updated")

# 5. Update Mobile Media Query (second occurrence around line 2600)
old_mobile_hero_2 = re.compile(r'#hero\s*\{[^}]*min-height:\s*100svh;\s*display:\s*block;.*?\.hero-quote\s*\{[^}]*line-height:\s*1\.22;[^}]*\}', re.DOTALL)
new_mobile_hero_2 = '''#hero {
        min-height: 100svh;
        height: 100svh;
        display: flex;
        align-items: flex-end;
        justify-content: flex-start;
        position: relative;
        overflow: hidden;
      }

      .hero-panorama {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
      }

      .hero-picture {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        display: block;
      }

      .hero-bg-photo {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center top;
      }

      .hero-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg,
            rgba(16, 8, 5, 0.45) 0%,
            rgba(16, 8, 5, 0.05) 30%,
            rgba(16, 8, 5, 0.15) 60%,
            rgba(24, 14, 8, 0.88) 100%);
      }

      .hero-content {
        position: relative;
        inset: auto;
        width: 100%;
        padding: 0 24px clamp(32px, 6svh, 56px);
        display: flex;
        align-items: flex-end;
        justify-content: flex-start;
        background: transparent;
      }

      .hero-quote {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(24px, 6.5vw, 34px);
        line-height: 1.25;
        font-weight: 600;
        color: var(--cream);
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.9);
      }'''

assert old_mobile_hero_2.search(content), "old_mobile_hero_2 not found"
content = old_mobile_hero_2.sub(new_mobile_hero_2, content, count=1)
print("5. Mobile Media Query 2 updated")

# 6. Update HTML Markup of #hero
old_hero_html = re.compile(r'<!-- SECTION 1: HERO -->\s*<section id="hero">\s*<div class="hero-panorama" aria-hidden="true">.*?</div>\s*<div class="hero-overlay"></div>\s*<div class="hero-content">\s*<p class="hero-quote">"Đưa gánh bánh canh Hàng Gòn về giữa phố thị"</p>\s*</div>\s*</section>', re.DOTALL)
new_hero_html = '''<!-- SECTION 1: HERO -->
  <section id="hero">
    <div class="hero-panorama" aria-hidden="true">
      <picture class="hero-picture">
        <source media="(max-width: 880px)" srcset="/images/home/new-chicken-chef-mobile.webp" width="941" height="1672">
        <source media="(min-width: 881px)" srcset="/images/home/new-chicken-chef-desktop.webp" width="1672" height="941">
        <img class="hero-bg-photo" src="/images/home/new-chicken-chef-desktop.webp" width="1672" height="941"
          fetchpriority="high" decoding="async"
          alt="Chú gà đầu bếp Hàng Gòn bên tô bánh canh gà ta bốc khói nghi ngút">
      </picture>
    </div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <p class="hero-quote">"Đưa gánh bánh canh Hàng Gòn về giữa phố thị"</p>
    </div>
  </section>'''

assert old_hero_html.search(content), "old_hero_html not found"
content = old_hero_html.sub(new_hero_html, content, count=1)
print("6. HTML Markup updated with <picture>")

# 7. Remove obsolete JS centerHeroPanorama
old_js = '''    const heroPanorama = document.querySelector('.hero-panorama');

    function centerHeroPanorama() {
      if (!heroPanorama || window.innerWidth > 880) return;
      const maxScroll = heroPanorama.scrollWidth - heroPanorama.clientWidth;
      if (maxScroll > 0) {
        heroPanorama.scrollLeft = maxScroll * 0.68;
      }
    }

    // Run immediately when script runs to snap as early as possible
    centerHeroPanorama();

    // Also run on DOMContentLoaded and load to ensure layout updates are covered
    document.addEventListener('DOMContentLoaded', centerHeroPanorama);
    window.addEventListener('load', centerHeroPanorama);
    window.addEventListener('resize', centerHeroPanorama);'''

if old_js in content:
    content = content.replace(old_js, '// Mobile hero now uses dedicated vertical asset with 100svh full fit', 1)
    print("7. Obsolete JS scroll hack removed")

# Save file
with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print("-> index.html successfully updated!")
