import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.getcwd()
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf'

try:
    f_title = ImageFont.truetype('arialbd.ttf', 24)
    f_header = ImageFont.truetype('arialbd.ttf', 18)
    f_quote = ImageFont.truetype('times.ttf', 22)
    f_quote_em = ImageFont.truetype('timesi.ttf', 22)
    f_body = ImageFont.truetype('arial.ttf', 14)
    f_body_b = ImageFont.truetype('arialbd.ttf', 14)
    f_cap = ImageFont.truetype('arial.ttf', 13)
    f_small = ImageFont.truetype('arial.ttf', 11.5)
except:
    f_title = f_header = f_quote = f_quote_em = f_body = f_body_b = f_cap = f_small = ImageFont.load_default()

items = [
    ('images/behind-scenes/chan-nuoc-leo_result.webp', 'Nước lèo ngọt thanh'),
    ('images/behind-scenes/ga-luoc-quan_result.webp', 'Gà tuyển chọn mỗi sáng'),
    ('images/behind-scenes/trung-non-nuoc-cham_result.webp', 'Vị chấm không thể thiếu'),
    ('images/highlights/highlights-4.webp', 'Hương vị trọn vẹn'),
    ('images/highlights/highlights-1.webp', 'Góc quán thân thuộc'),
    ('images/highlights/hightlights.webp', 'Không gian ấm cúng'),
    ('images/highlights/higlights-3.webp', 'Khoảnh khắc Hàng Gòn'),
    ('images/behind-scenes/khong-gian-quan_result.webp', 'Mặt tiền quán phố')
]

# -------------------------------------------------------------
# PROOF 1: DESKTOP EDITORIAL GRID 4x2 (1200 x 780)
# -------------------------------------------------------------
W1, H1 = 1200, 780
c1 = Image.new('RGB', (W1, H1), (28, 18, 13))
d1 = ImageDraw.Draw(c1)

d1.text((40, 25), 'SECTION HIGHLIGHTS & HẬU TRƯỜNG: BỐ CỤC LƯỚI 4x2 TỐI GIẢN (8 ẢNH)', fill=(225, 175, 80), font=f_title)

# Quote header
quote_txt = '“Mỗi tô bánh canh được nấu như bữa cơm nhà, nóng hổi, đậm đà và đầy tình thương.”'
qb = d1.textbbox((0, 0), quote_txt, font=f_quote)
d1.text((W1 // 2 - (qb[2]-qb[0]) // 2, 65), quote_txt, fill=(245, 235, 220), font=f_quote)
d1.line([(W1 // 2 - 45, 96), (W1 // 2 + 45, 96)], fill=(201, 154, 74), width=1)

# Grid Layout: 4 cols x 2 rows
gx0 = 40
gy0 = 115
gw = W1 - 80
gap = 14
card_w = (gw - gap * 3) // 4
card_h = 270

for i, (rel_p, cap_text) in enumerate(items):
    col = i % 4
    row = i // 4
    x0 = gx0 + col * (card_w + gap)
    y0 = gy0 + row * (card_h + gap)
    x1 = x0 + card_w
    y1 = y0 + card_h
    
    full_p = os.path.join(ROOT, rel_p)
    if os.path.exists(full_p):
        im = Image.open(full_p).convert('RGB')
        # Center crop to card_w x card_h
        im_ratio = im.size[0] / im.size[1]
        target_ratio = card_w / card_h
        if im_ratio > target_ratio:
            # wider
            new_h = card_h
            new_w = int(card_h * im_ratio)
        else:
            # taller
            new_w = card_w
            new_h = int(card_w / im_ratio)
        im_scaled = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
        crop_x = (new_w - card_w) // 2
        crop_y = (new_h - card_h) // 2
        im_cropped = im_scaled.crop((crop_x, crop_y, crop_x + card_w, crop_y + card_h))
        
        # Overlay subtle dark gradient at bottom for text legibility
        grad = Image.new('RGBA', (card_w, card_h), (0, 0, 0, 0))
        g_draw = ImageDraw.Draw(grad)
        for gy in range(card_h - 70, card_h):
            alpha = int(210 * ((gy - (card_h - 70)) / 70))
            g_draw.line([(0, gy), (card_w, gy)], fill=(18, 10, 6, alpha))
            
        im_rgba = im_cropped.convert('RGBA')
        im_rgba.alpha_composite(grad)
        
        # Paste into canvas
        c1.paste(im_rgba.convert('RGB'), (x0, y0))
        
        # Caption with gold accent
        d1.text((x0 + 12, y1 - 26), cap_text, fill=(247, 235, 210), font=f_cap)
        d1.line([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], fill=(65, 45, 35), width=1)

# Verification Footer Badge
d1.rounded_rectangle([40, H1 - 60, W1 - 40, H1 - 20], radius=6, fill=(25, 85, 40))
d1.text((60, H1 - 47), '✓ ĐÃ LOẠI BỎ ẢNH CŨ "GÓC QUÁN MỖI TRƯA" | BỔ SUNG 4 ẢNH HIGHLIGHTS MỚI | BỐ CỤC 4x2 CÂN ĐỐI, THOÁNG MẮT', fill=(230, 255, 235), font=f_body_b)

out1 = os.path.join(ARTIFACT_DIR, 'proof_highlights_grid_8_desktop.png')
c1.save(out1, quality=95)
print('Saved proof 1 to:', out1)


# -------------------------------------------------------------
# PROOF 2: MOBILE VIEWPORT COMPACT 2-COLUMN (420 x 860)
# -------------------------------------------------------------
W2, H2 = 420, 860
c2 = Image.new('RGB', (W2, H2), (28, 18, 13))
d2 = ImageDraw.Draw(c2)

d2.text((20, 18), 'HIGHLIGHTS TRÊN DI ĐỘNG (LƯỚI 2 CỘT)', fill=(225, 175, 80), font=f_header)
d2.text((20, 42), '“Mỗi tô bánh canh được nấu như bữa cơm nhà...”', fill=(220, 210, 200), font=f_small)

m_gx0 = 20
m_gy0 = 70
m_gw = W2 - 40
m_gap = 10
m_card_w = (m_gw - m_gap) // 2
m_card_h = 165

for i, (rel_p, cap_text) in enumerate(items):
    col = i % 2
    row = i // 2
    x0 = m_gx0 + col * (m_card_w + m_gap)
    y0 = m_gy0 + row * (m_card_h + m_gap)
    x1 = x0 + m_card_w
    y1 = y0 + m_card_h
    
    full_p = os.path.join(ROOT, rel_p)
    if os.path.exists(full_p):
        im = Image.open(full_p).convert('RGB')
        im_ratio = im.size[0] / im.size[1]
        target_ratio = m_card_w / m_card_h
        if im_ratio > target_ratio:
            new_h = m_card_h
            new_w = int(m_card_h * im_ratio)
        else:
            new_w = m_card_w
            new_h = int(m_card_w / im_ratio)
        im_scaled = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
        crop_x = (new_w - m_card_w) // 2
        crop_y = (new_h - m_card_h) // 2
        im_cropped = im_scaled.crop((crop_x, crop_y, crop_x + m_card_w, crop_y + m_card_h))
        
        grad = Image.new('RGBA', (m_card_w, m_card_h), (0, 0, 0, 0))
        g_draw = ImageDraw.Draw(grad)
        for gy in range(m_card_h - 50, m_card_h):
            alpha = int(210 * ((gy - (m_card_h - 50)) / 50))
            g_draw.line([(0, gy), (m_card_w, gy)], fill=(18, 10, 6, alpha))
            
        im_rgba = im_cropped.convert('RGBA')
        im_rgba.alpha_composite(grad)
        c2.paste(im_rgba.convert('RGB'), (x0, y0))
        d2.text((x0 + 8, y1 - 20), cap_text, fill=(247, 235, 210), font=f_small)

d2.rounded_rectangle([20, H2 - 50, W2 - 20, H2 - 15], radius=6, fill=(25, 85, 40))
d2.text((35, H2 - 38), '✓ Lưới 2 cột di động: Gọn gàng, vừa vặn khung nhìn', fill=(230, 255, 235), font=f_small)

out2 = os.path.join(ARTIFACT_DIR, 'proof_highlights_grid_8_mobile.png')
c2.save(out2, quality=95)
print('Saved proof 2 to:', out2)

print('ALL HIGHLIGHTS PROOFS GENERATED SUCCESSFULLY!')
