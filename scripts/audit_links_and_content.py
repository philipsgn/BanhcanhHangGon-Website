import os
import sys
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.getcwd()

def audit_file(fname):
    print(f"\n==========================================")
    print(f"AUDITING: {fname}")
    print(f"==========================================")
    
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Audit all section IDs
    sections = [s.get('id') for s in soup.find_all(id=True)]
    print(f"Available IDs in {fname}: {sections}")
    
    # 2. Audit all <a> tags
    print("\n--- AUDITING <A> LINKS ---")
    links = soup.find_all('a')
    for a in links:
        href = a.get('href', '')
        text = a.get_text(strip=True)
        classes = a.get('class', [])
        
        # Check target validity
        status = "OK"
        if href.startswith('#'):
            target_id = href[1:]
            if target_id and target_id not in sections:
                status = f"BROKEN ANCHOR: #{target_id} not in {fname}"
        elif href.endswith('.html') or '.html#' in href:
            parts = href.split('#')
            target_file = parts[0]
            target_anchor = parts[1] if len(parts) > 1 else ''
            
            if not os.path.exists(os.path.join(ROOT, target_file)):
                status = f"BROKEN FILE LINK: {target_file} not found"
            elif target_anchor:
                # check anchor in target file
                with open(os.path.join(ROOT, target_file), 'r', encoding='utf-8') as tf:
                    t_soup = BeautifulSoup(tf.read(), 'html.parser')
                    if not t_soup.find(id=target_anchor):
                        status = f"BROKEN CROSS-ANCHOR: #{target_anchor} not in {target_file}"
        elif href.startswith(('http://', 'https://', 'tel:', 'mailto:', 'javascript:')):
            status = "EXTERNAL/ACTION"
        elif href == '' or href == '#':
            status = "EMPTY OR DUMMY #"
            
        print(f"  [{status}] text: '{text[:25]}' | href: '{href}' | class: {classes}")

    # 3. Audit all <img> and <source> tags
    print("\n--- AUDITING IMAGE ASSETS ---")
    imgs = soup.find_all(['img', 'source'])
    broken_imgs = []
    leading_slash_imgs = []
    
    for el in imgs:
        src = el.get('src') or el.get('srcset')
        alt = el.get('alt', '')
        tag = el.name
        
        if src:
            clean_src = src.split('?')[0].split()[0]
            if clean_src.startswith('/'):
                leading_slash_imgs.append(clean_src)
                # check local without slash
                local_p = os.path.join(ROOT, clean_src.lstrip('/\\'))
            else:
                local_p = os.path.join(ROOT, clean_src)
                
            if not os.path.exists(local_p):
                broken_imgs.append((clean_src, tag, alt))
                print(f"  [MISSING FILE] <{tag}> src: '{src}' | alt: '{alt}'")
            elif not clean_src.endswith('.webp') and any(clean_src.endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
                print(f"  [NON-WEBP] <{tag}> src: '{src}'")
                
    if not broken_imgs:
        print("  All image assets exist on disk!")
    if leading_slash_imgs:
        print(f"  WARNING: {len(leading_slash_imgs)} images have leading slashes (e.g. {leading_slash_imgs[:3]})")
        
    # 4. Audit CSS url(...)
    print("\n--- AUDITING CSS URLS ---")
    css_urls = re.findall(r'url\([\'"]?([^\'")\s]+)[\'"]?\)', html)
    for u in set(css_urls):
        clean_u = u.split('?')[0]
        if clean_u.startswith('data:'):
            continue
        if clean_u.startswith('/'):
            local_p = os.path.join(ROOT, clean_u.lstrip('/\\'))
            print(f"  [LEADING SLASH CSS URL]: {u}")
        else:
            local_p = os.path.join(ROOT, clean_u)
            
        if not os.path.exists(local_p):
            print(f"  [MISSING CSS ASSET]: {u}")

def audit_consistency():
    print("\n==========================================")
    print("AUDITING CROSS-PAGE CONTENT CONSISTENCY")
    print("==========================================")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        t_index = f.read()
    with open('order.html', 'r', encoding='utf-8') as f:
        t_order = f.read()
        
    # Check Hours
    hours_index = set(re.findall(r'(?:\d{1,2}[:h]\d{2}\s*[-–]\s*\d{1,2}[:h]\d{2})', t_index))
    hours_order = set(re.findall(r'(?:\d{1,2}[:h]\d{2}\s*[-–]\s*\d{1,2}[:h]\d{2})', t_order))
    print(f"Hours in index.html: {hours_index}")
    print(f"Hours in order.html: {hours_order}")
    
    # Check Hotline
    hotline_index = set(re.findall(r'09\d[\s\.]?\d{3}[\s\.]?\d{3,4}', t_index))
    hotline_order = set(re.findall(r'09\d[\s\.]?\d{3}[\s\.]?\d{3,4}', t_order))
    print(f"Hotline in index.html: {hotline_index}")
    print(f"Hotline in order.html: {hotline_order}")
    
    # Check Address
    addr_match_index = re.findall(r'178/14[^\n<]+', t_index)
    addr_match_order = re.findall(r'178/14[^\n<]+', t_order)
    print(f"Address in index.html: {addr_match_index[:2]}")
    print(f"Address in order.html: {addr_match_order[:2]}")

if __name__ == '__main__':
    audit_file('index.html')
    audit_file('order.html')
    audit_consistency()
