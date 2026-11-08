import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.getcwd()

def update_order_html():
    p = os.path.join(ROOT, 'order.html')
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Update site-nav links in order.html
    old_nav = '''  <nav class="site-nav" id="siteNav">
    <a class="logo" href="/home" aria-label="Bánh Canh Gà Ta Hàng Gòn">
      <img src="images/menu/icon-quan-an_result.webp" alt="Bánh Canh Gà Ta" decoding="async">
    </a>

    <ul>
      <li><a href="/home">Trang chủ</a></li>
      <li><a href="/home/welcome">Giới thiệu</a></li>
      <li><a href="/home/menu">Menu</a></li>
      <li><a href="/home/location">Vị trí</a></li>
      <li><a class="nav-order-link" href="/order">Đặt hàng</a></li>
    </ul>

    <a class="mobile-order-btn" href="#openCheck" onclick="toggleMobileSheet(true); return false;">Đặt hàng</a>'''

    new_nav = '''  <nav class="site-nav" id="siteNav">
    <a class="logo" href="index.html#hero" aria-label="Bánh Canh Gà Ta Hàng Gòn">
      <img src="images/menu/icon-quan-an_result.webp" alt="Bánh Canh Gà Ta" decoding="async">
    </a>

    <ul>
      <li><a href="index.html#hero">Trang chủ</a></li>
      <li><a href="index.html#welcome">Giới thiệu</a></li>
      <li><a href="index.html#menu">Menu</a></li>
      <li><a href="index.html#location">Vị trí</a></li>
      <li><a class="nav-order-link" href="#clipboardWrapper">Đặt hàng</a></li>
    </ul>

    <a class="mobile-order-btn" href="#guestCheckCard" onclick="toggleMobileSheet(true); return false;">Đặt hàng</a>'''

    if old_nav in content:
        content = content.replace(old_nav, new_nav)
        print("Updated navbar in order.html!")
    else:
        # Regex replacement if whitespace differs
        pattern = re.compile(r'<nav class="site-nav" id="siteNav">[\s\S]*?<a class="mobile-order-btn" href="#openCheck"[^>]*>Đặt hàng</a>')
        if pattern.search(content):
            content = pattern.sub(new_nav, content)
            print("Updated navbar in order.html via pattern!")
        else:
            print("Warning: Could not match exact old_nav in order.html")

    # 2. Update hotline in order.html
    old_hotline = '<span>Hotline: 090 123 4567 • Mở cửa: 06:00 - 23:00</span>'
    new_hotline = '<span>Hotline: 0356 538 789 • Mở cửa: 06:00 - 23:00</span>'
    if old_hotline in content:
        content = content.replace(old_hotline, new_hotline)
        print("Synchronized hotline 0356 538 789 in order.html!")
    else:
        content = content.replace('090 123 4567', '0356 538 789')
        print("Replaced 090 123 4567 in order.html!")

    # 3. Add smooth scroll for #clipboardWrapper in order.html if clicked
    nav_click_script = '''    // Handle internal #clipboardWrapper smooth scroll on order.html
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[href="#clipboardWrapper"]');
      if (link) {
        e.preventDefault();
        const target = document.getElementById('clipboardWrapper') || document.getElementById('roosterMenuHolder');
        if (target) {
          const top = target.getBoundingClientRect().top + window.pageYOffset - 70;
          window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
        }
      }
    });'''

    if 'clipboardWrapper smooth scroll' not in content:
        content = content.replace("checkPendingOrderFromMenu();", "checkPendingOrderFromMenu();\n\n" + nav_click_script)
        print("Added smooth scroll handler for #clipboardWrapper in order.html!")

    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("order.html updated successfully!")


def update_index_html():
    p = os.path.join(ROOT, 'index.html')
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Normalize leading slash image paths in head and hero
    content = content.replace('href="/images/menu/icon-quan-an_result.webp"', 'href="images/menu/icon-quan-an_result.webp"')
    content = content.replace('href="/images/home/new-chicken-chef-desktop.webp"', 'href="images/home/new-chicken-chef-desktop.webp"')
    content = content.replace('href="/images/home/new-chicken-chef-mobile.webp"', 'href="images/home/new-chicken-chef-mobile.webp"')
    content = content.replace('srcset="/images/home/new-chicken-chef-mobile.webp"', 'srcset="images/home/new-chicken-chef-mobile.webp"')
    content = content.replace('srcset="/images/home/new-chicken-chef-desktop.webp"', 'srcset="images/home/new-chicken-chef-desktop.webp"')
    print("Normalized leading slash image paths in index.html!")

    # 2. Update navbar links in index.html
    old_nav = '''  <nav class="site-nav" id="siteNav">
    <a class="logo" href="/home" aria-label="Bánh Canh Gà Ta">
      <img src="images/menu/icon-quan-an_result.webp" alt="Bánh Canh Gà Ta" decoding="async">
    </a>
    <ul>
      <li><a href="/home">Trang chủ</a></li>
      <li><a href="/home/welcome">Giới thiệu</a></li>
      <li><a href="/home/menu">Menu</a></li>
      <li><a href="/home/location">Vị trí</a></li>
      <li><a class="nav-order-link" href="/order">Đặt hàng</a></li>
    </ul>
    <a class="mobile-order-btn" href="/order">Đặt hàng</a>'''

    new_nav = '''  <nav class="site-nav" id="siteNav">
    <a class="logo" href="#hero" aria-label="Bánh Canh Gà Ta Hàng Gòn">
      <img src="images/menu/icon-quan-an_result.webp" alt="Bánh Canh Gà Ta" decoding="async">
    </a>
    <ul>
      <li><a href="#hero">Trang chủ</a></li>
      <li><a href="#welcome">Giới thiệu</a></li>
      <li><a href="#menu">Menu</a></li>
      <li><a href="#location">Vị trí</a></li>
      <li><a class="nav-order-link" href="order.html">Đặt hàng</a></li>
    </ul>
    <a class="mobile-order-btn" href="order.html">Đặt hàng</a>'''

    if old_nav in content:
        content = content.replace(old_nav, new_nav)
        print("Updated navbar in index.html!")
    else:
        pattern = re.compile(r'<nav class="site-nav" id="siteNav">[\s\S]*?<a class="mobile-order-btn" href="/order">Đặt hàng</a>')
        if pattern.search(content):
            content = pattern.sub(new_nav, content)
            print("Updated navbar in index.html via pattern!")
        else:
            print("Warning: Could not match exact old_nav in index.html")

    # 3. Update footer links in index.html
    old_footer_links = '''<ul class="loc-links">
          <li><a href="/home">Trang chủ</a></li>
          <li><a href="/home/menu">Thực đơn</a></li>
          <li><a href="/order">Đặt món</a></li>
          <li><a href="/home/welcome">Về chúng tôi</a></li>
          <li><a href="/home/location">Liên hệ</a></li>
        </ul>'''

    new_footer_links = '''<ul class="loc-links">
          <li><a href="#hero">Trang chủ</a></li>
          <li><a href="#menu">Thực đơn</a></li>
          <li><a href="order.html">Đặt món</a></li>
          <li><a href="#welcome">Về chúng tôi</a></li>
          <li><a href="#location">Liên hệ</a></li>
        </ul>'''

    if old_footer_links in content:
        content = content.replace(old_footer_links, new_footer_links)
        print("Updated footer links in index.html!")
    else:
        # Replace individual footer links if needed
        content = content.replace('<li><a href="/order">Đặt món</a></li>', '<li><a href="order.html">Đặt món</a></li>')
        content = content.replace('<li><a href="/home/menu">Thực đơn</a></li>', '<li><a href="#menu">Thực đơn</a></li>')
        content = content.replace('<li><a href="/home/welcome">Về chúng tôi</a></li>', '<li><a href="#welcome">Về chúng tôi</a></li>')
        content = content.replace('<li><a href="/home/location">Liên hệ</a></li>', '<li><a href="#location">Liên hệ</a></li>')
        content = content.replace('<li><a href="/home">Trang chủ</a></li>', '<li><a href="#hero">Trang chủ</a></li>')
        print("Replaced footer links in index.html individually!")

    # 4. Fix routing and smooth scroll logic in index.html
    # We replace the old scrollSectionForPath and click listener
    old_router_block = '''    const sectionRouteMap = {
      '/': 'hero',
      '/home': 'hero',
      '/home/welcome': 'welcome',
      '/home/menu': 'menu',
      '/home/location': 'location'
    };

    function getSectionIdForPath(pathname) {
      const clean = pathname.replace(/\\/+$/, '') || '/';
      return sectionRouteMap[clean] || sectionRouteMap[clean + '/'];
    }

    function scrollSectionForPath(pathname) {
      const targetId = getSectionIdForPath(pathname);
      if (!targetId) return false;
      const target = document.getElementById(targetId);
      if (!target) return false;
      requestAnimationFrame(() => target.scrollIntoView({ behavior: 'smooth', block: 'start' }));
      return true;
    }

    document.addEventListener('click', (event) => {
      const link = event.target.closest('a[href^="/home"], a[href="/"]');
      if (!link) return;
      const href = link.getAttribute('href');
      const nextPath = href === '/' ? '/' : href.replace(/\\/+$/, '') || '/';
      if (nextPath === window.location.pathname.replace(/\\/+$/, '') || '/') {
        event.preventDefault();
        scrollSectionForPath(nextPath);
        closeMobileNav();
        return;
      }
      event.preventDefault();
      window.history.pushState({}, '', href);
      scrollSectionForPath(nextPath);
      closeMobileNav();
      window.scrollTo({ top: 0, behavior: 'instant' });
    });

    window.addEventListener('popstate', () => {
      scrollSectionForPath(window.location.pathname);
    });

    scrollSectionForPath(window.location.pathname);'''

    new_router_block = '''    // Header offset for precise smooth scrolling
    function scrollToSection(targetId) {
      if (!targetId) return;
      const target = document.getElementById(targetId);
      if (!target) return;
      const headerOffset = 68;
      const elementPosition = target.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      window.scrollTo({
        top: Math.max(0, offsetPosition),
        behavior: 'smooth'
      });
    }

    // Handle hash landing on page load (e.g. index.html#menu, index.html#welcome)
    function handleHashLanding() {
      const hash = window.location.hash.replace('#', '');
      if (hash) {
        setTimeout(() => {
          scrollToSection(hash);
        }, 150);
      }
    }
    window.addEventListener('DOMContentLoaded', handleHashLanding);
    window.addEventListener('load', handleHashLanding);
    window.addEventListener('hashchange', () => {
      const hash = window.location.hash.replace('#', '');
      if (hash) scrollToSection(hash);
    });

    // Handle internal nav link clicks smoothly without jumping to top
    document.addEventListener('click', (event) => {
      const link = event.target.closest('a[href^="#"]');
      if (!link) return;
      const href = link.getAttribute('href');
      if (href === '#' || href === '#!') return;
      const targetId = href.substring(1);
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        event.preventDefault();
        closeMobileNav();
        scrollToSection(targetId);
        if (history.replaceState) {
          history.replaceState(null, '', href);
        }
      }
    });'''

    if old_router_block in content:
        content = content.replace(old_router_block, new_router_block)
        print("Replaced old router block with robust smooth scroll & hash landing in index.html!")
    else:
        # Pattern match router block
        pattern = re.compile(r'const sectionRouteMap\s*=[\s\S]*?scrollSectionForPath\(window\.location\.pathname\);')
        if pattern.search(content):
            content = pattern.sub(new_router_block, content)
            print("Replaced router block via regex pattern in index.html!")
        else:
            print("Warning: Could not match old_router_block in index.html")

    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated successfully!")


if __name__ == '__main__':
    print("=== UPDATING order.html ===")
    update_order_html()
    print("\n=== UPDATING index.html ===")
    update_index_html()
