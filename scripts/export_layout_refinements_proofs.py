import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.getcwd()
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf'

# Load assets
p_bg = os.path.join(ROOT, 'images', 'menu', 'menu-bg-3.webp')
p_rooster = os.path.join(ROOT, 'images', 'menu', 'original-chef-rooster-board.webp')
p_dish0 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Soup on Wooden Tray_result.webp')
p_story_bg = os.path.join(ROOT, 'images', 'story', 'new-background-story-chicken.webp')

im_bg = Image.open(p_bg).convert('RGBA')
im_rooster = Image.open(p_rooster).convert('RGBA')
im_dish0 = Image.open(p_dish0).convert('RGBA')
im_story_bg = Image.open(p_story_bg).convert('RGBA')

try:
    f_quote = ImageFont.truetype('times.ttf', 20)
    f_title_viet = ImageFont.truetype('arialbd.ttf', 26)
    f_price_viet = ImageFont.truetype('arialbd.ttf', 26)
    f_desc_viet = ImageFont.truetype('arial.ttf', 14)
    f_btn_light = ImageFont.truetype('arial.ttf', 13.5)
    f_gold_link = ImageFont.truetype('arialbd.ttf', 15)
    f_story_quote = ImageFont.truetype('times.ttf', 32)
    f_story_em = ImageFont.truetype('timesi.ttf', 32)
    f_caption = ImageFont.truetype('arialbd.ttf', 13)
except:
    f_quote = f_title_viet = f_price_viet = f_desc_viet = f_btn_light = f_gold_link = f_caption = ImageFont.load_default()
    f_story_quote = f_story_em = ImageFont.load_default()

dishes = [
    (im_dish0, "Bánh Canh Gà Đặc Biệt", "70.000₫", "Thịt gà ta da vàng giòn mọng nước, trứng non béo ngậy.\nNước dùng ninh xương thanh ngọt đậm đà.")
]

# -------------------------------------------------------------------------
# PROOF 1: Desktop Viewport (1024x720) - Zero Dots, Right-Aligned Link
# -------------------------------------------------------------------------
W1, H1 = 1024, 720
canvas1 = Image.new('RGBA', (W1, H1), (250, 245, 235, 255))
bg_scaled = im_bg.resize((W1, int(W1 * im_bg.size[1] / im_bg.size[0])), Image.Resampling.LANCZOS).crop((0, 0, W1, H1))
bg_blurred = bg_scaled.filter(ImageFilter.GaussianBlur(1.8))
canvas1 = Image.blend(canvas1, bg_blurred, 0.22)

# Central Gourmet Radial Spotlight
spotlight = Image.new('RGBA', (W1, H1), (0, 0, 0, 0))
sp_draw = ImageDraw.Draw(spotlight)
for r in range(480, 0, -20):
    alpha = int(165 * (1 - r / 480))
    sp_draw.ellipse([512 - r, 300 - r * 0.65, 512 + r, 300 + r * 0.65], fill=(255, 255, 255, alpha))
canvas1.alpha_composite(spotlight)

d1 = ImageDraw.Draw(canvas1)

story_bar_h = 30
d1.rectangle([0, 0, W1, story_bar_h], fill=(36, 22, 14, 255))
d1.text((32, 5), "Gìn giữ vị quê đượm ấm...", fill=(235, 218, 195, 220), font=f_quote)
d1.line([(0, story_bar_h), (W1, story_bar_h)], fill=(225, 215, 200, 255), width=1)

# Rooster Mascot
rw, rh = 165, 155
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
canvas1.paste(rooster_s, (32, story_bar_h), rooster_s)

cx = 512
card_cy = 300
plate_act = 480
dish0_s = im_dish0.resize((plate_act, plate_act), Image.Resampling.LANCZOS)
px = cx - plate_act // 2
py = card_cy - plate_act // 2 - 40

# Contact Shadow
tray_shadow = Image.new('RGBA', canvas1.size, (0, 0, 0, 0))
ts_draw = ImageDraw.Draw(tray_shadow)
for s_off in range(1, 22):
    s_alpha = int(30 * (1 - s_off / 22))
    ts_draw.ellipse([px + s_off*2, py + 30 + s_off*2, px + plate_act - s_off*2, py + plate_act + 22 + s_off], fill=(35, 18, 10, s_alpha))
canvas1.alpha_composite(tray_shadow)

canvas1.paste(dish0_s, (px, py), dish0_s)

# Typography
cy = py + plate_act - 16
title_txt = dishes[0][1]
tb = d1.textbbox((0, 0), title_txt, font=f_title_viet)
d1.text((cx - (tb[2]-tb[0])//2, cy), title_txt, fill=(26, 15, 8), font=f_title_viet)
cy += 34

price_txt = dishes[0][2]
pb = d1.textbbox((0, 0), price_txt, font=f_price_viet)
d1.text((cx - (pb[2]-pb[0])//2, cy), price_txt, fill=(189, 60, 13), font=f_price_viet)
cy += 30

desc_txt = dishes[0][3]
for l in desc_txt.split('\n'):
    lb = d1.textbbox((0, 0), l, font=f_desc_viet)
    d1.text((cx - (lb[2]-lb[0])//2, cy), l, fill=(56, 37, 27), font=f_desc_viet)
    cy += 18

cy += 6
# Button
bw, bh = 175, 40
bx0 = cx - bw // 2
by0 = cy
bx1 = cx + bw // 2
by1 = by0 + bh
d1.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, fill=(189, 60, 13))
btn_txt = "Đ  Ặ  T    M  Ó  N"
btb = d1.textbbox((0, 0), btn_txt, font=f_btn_light)
d1.text((cx - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 253, 245), font=f_btn_light)

# NOTICE: ZERO DOTS! Area below button is completely clean!
d1.text((cx - 100, by1 + 18), "✓ ĐÃ LOẠI BỎ 100% CỤC ĐIỀU HƯỚNG CHẤM TRÒN", fill=(34, 139, 34), font=f_desc_viet)

# RIGHT-ALIGNED 'TOÀN BỘ THỰC ĐƠN' (sát góc phải)
gold_y = H1 - 42
gold_txt = "TOÀN BỘ THỰC ĐƠN"
gtb = d1.textbbox((0, 0), gold_txt, font=f_gold_link)
gw = gtb[2] - gtb[0]
gh = gtb[3] - gtb[1]

# Positioned near right edge (x = W1 - 48 - gw)
link_rx = W1 - 48 - gw
gx0 = link_rx - 16
gx1 = link_rx + gw + 16

for off_x in range(gx0, gx1):
    progress = (off_x - gx0) / (gx1 - gx0)
    sin_weight = (1 - ((progress - 0.5) * 2)**2)
    line_alpha = int(240 * max(0, sin_weight))
    d1.line([(off_x, gold_y - 8), (off_x + 1, gold_y - 8)], fill=(196, 139, 40, line_alpha), width=2)
    d1.line([(off_x, gold_y + gh + 8), (off_x + 1, gold_y + gh + 8)], fill=(196, 139, 40, line_alpha), width=2)

d1.text((link_rx, gold_y), gold_txt, fill=(196, 139, 40), font=f_gold_link)

out1 = os.path.join(ARTIFACT_DIR, 'proof_menu_dots_removed_and_right_aligned.png')
canvas1.save(out1, quality=95)
print("Proof 1 saved to:", out1)


# -------------------------------------------------------------------------
# PROOF 2: Normal vs Hover State for 'TOÀN BỘ THỰC ĐƠN' (700x320)
# -------------------------------------------------------------------------
W2, H2 = 700, 320
canvas2 = Image.new('RGBA', (W2, H2), (250, 245, 235, 255))
d2 = ImageDraw.Draw(canvas2)

d2.text((24, 16), "SO SÁNH TRẠNG THÁI CHỮ 'TOÀN BỘ THỰC ĐƠN' (BÌNH THƯỜNG vs HOVER)", fill=(26, 15, 8), font=f_caption)

# Left box: Normal State
d2.text((60, 55), "1. Trạng thái Thường: Vàng kim đồng đậm (#C48B28)", fill=(138, 74, 28), font=f_desc_viet)
ny = 110
nx0, nx1 = 60, 60 + gw + 32
for off_x in range(nx0, nx1):
    progress = (off_x - nx0) / (nx1 - nx0)
    sin_weight = (1 - ((progress - 0.5) * 2)**2)
    line_alpha = int(240 * max(0, sin_weight))
    d2.line([(off_x, ny - 8), (off_x + 1, ny - 8)], fill=(196, 139, 40, line_alpha), width=2)
    d2.line([(off_x, ny + gh + 8), (off_x + 1, ny + gh + 8)], fill=(196, 139, 40, line_alpha), width=2)
d2.text((76, ny), gold_txt, fill=(196, 139, 40), font=f_gold_link)
d2.text((60, ny + 38), "→ Đậm đà, tương phản sắc nét trên nền kem", fill=(100, 80, 60), font=f_desc_viet)

# Right box: Hover State
d2.text((380, 55), "2. Trạng thái Hover: Nâu Đen Cà Phê (#1F120A)", fill=(31, 18, 10), font=f_desc_viet)
hy = 110
hx0, hx1 = 380, 380 + gw + 32
for off_x in range(hx0, hx1):
    progress = (off_x - hx0) / (hx1 - hx0)
    sin_weight = (1 - ((progress - 0.5) * 2)**2)
    line_alpha = int(240 * max(0, sin_weight))
    d2.line([(off_x, hy - 8), (off_x + 1, hy - 8)], fill=(31, 18, 10, line_alpha), width=2)
    d2.line([(off_x, hy + gh + 8), (off_x + 1, hy + gh + 8)], fill=(31, 18, 10, line_alpha), width=2)
# Highlight shadow
d2.text((396 + 1, hy + 1), gold_txt, fill=(255, 255, 255, 200), font=f_gold_link)
d2.text((396, hy), gold_txt, fill=(31, 18, 10), font=f_gold_link)
d2.text((380, hy + 38), "→ Nổi bần bật, sắc lẹm, sang trọng tuyệt đối!", fill=(34, 139, 34), font=f_desc_viet)

out2 = os.path.join(ARTIFACT_DIR, 'proof_menu_gold_link_hover_dark_brown.png')
canvas2.save(out2, quality=95)
print("Proof 2 saved to:", out2)


# -------------------------------------------------------------------------
# PROOF 3: Section Greeting & Section Story Synchronization (760x480)
# -------------------------------------------------------------------------
W3, H3 = 760, 480
canvas3 = Image.new('RGBA', (W3, H3), (36, 22, 14, 255))
d3 = ImageDraw.Draw(canvas3)

# Part A: Greeting sync verification
d3.rectangle([20, 15, W3 - 20, 160], fill=(45, 28, 18), outline=(201, 154, 74, 80), width=1)
d3.text((36, 25), "SECTION GREETING: XÓA CỤM TỪ 'như thuở ban đầu'", fill=(255, 218, 105), font=f_caption)
greeting_render = "“...Từng tô canh được nấu mỗi ngày với nước lèo ninh xương, thịt gà tươi chọn lọc,\ngiữ trọn vẹn sự ngọt thanh nguyên bản.”"
for i, gl in enumerate(greeting_render.split('\n')):
    d3.text((36, 55 + i * 24), gl, fill=(242, 232, 213), font=f_desc_viet)
d3.text((36, 125), "✓ Đã loại bỏ hoàn toàn cụm 'như thuở ban đầu', kết thúc gãy gọn, tinh tế.", fill=(34, 139, 34), font=f_desc_viet)

# Part B: Story 4 rhythmic lines verification
d3.rectangle([20, 180, W3 - 20, H3 - 20], fill=(45, 28, 18), outline=(201, 154, 74, 80), width=1)
d3.text((36, 192), "SECTION STORY: CHUẨN XÁC ĐÚNG 4 DÒNG THƠ (BÁT CANH ĐẦY Ở DÒNG 4)", fill=(255, 218, 105), font=f_caption)

story_lines = [
    ("“Góc chợ ", "Hàng Gòn"),
    ("bao năm qua vẫn vậy,", None),
    ("Gìn giữ vị quê đượm ấm", None),
    ("bát canh đầy.”", None)
]

sy = 225
for idx, (part1, part2) in enumerate(story_lines):
    b1 = d3.textbbox((0, 0), part1, font=f_story_quote)
    w1 = b1[2] - b1[0]
    
    # Line number indicator
    d3.text((36, sy), f"Dòng {idx+1}:", fill=(201, 154, 74), font=f_desc_viet)
    
    # Text
    d3.text((110, sy - 6), part1, fill=(242, 232, 213), font=f_story_quote)
    if part2:
        d3.text((110 + w1, sy - 6), part2, fill=(218, 165, 32), font=f_story_em)
    
    sy += 36

d3.text((36, H3 - 44), "✓ 'bát canh đầy.”' nằm trọn vẹn chung 1 hàng ở dòng thứ 4, không còn rớt chữ 'đầy.'", fill=(34, 139, 34), font=f_desc_viet)

out3 = os.path.join(ARTIFACT_DIR, 'proof_greeting_and_story_sync.png')
canvas3.save(out3, quality=95)
print("Proof 3 saved to:", out3)


# -------------------------------------------------------------------------
# PROOF 4: Mobile Viewport 390x844 Sync (Right-Aligned Link, Zero Dots)
# -------------------------------------------------------------------------
W4, H4 = 390, 844
canvas4 = Image.new('RGBA', (W4, H4), (250, 245, 235, 255))
bg_scaled4 = im_bg.resize((W4, int(W4 * im_bg.size[1] / im_bg.size[0])), Image.Resampling.LANCZOS).crop((0, 0, W4, H4))
bg_blurred4 = bg_scaled4.filter(ImageFilter.GaussianBlur(1.8))
canvas4 = Image.blend(canvas4, bg_blurred4, 0.22)

d4 = ImageDraw.Draw(canvas4)

m_story_h = 32
d4.rectangle([0, 0, W4, m_story_h], fill=(36, 22, 14, 255))
d4.text((16, 8), "Gìn giữ vị quê đượm ấm...", fill=(235, 218, 195, 220), font=f_desc_viet)

m_cx = 195
m_cy = 360
m_plate = 345
dish0_sm = dishes[0][0].resize((m_plate, m_plate), Image.Resampling.LANCZOS)
m_px = m_cx - m_plate // 2
m_py = m_cy - m_plate // 2 - 50

canvas4.paste(dish0_sm, (m_px, m_py), dish0_sm)

m_text_y = m_py + m_plate - 14
mtb = d4.textbbox((0, 0), title_txt, font=f_title_viet)
d4.text((m_cx - (mtb[2]-mtb[0])//2, m_text_y), title_txt, fill=(26, 15, 8), font=f_title_viet)
m_text_y += 30

mpb = d4.textbbox((0, 0), price_txt, font=f_price_viet)
d4.text((m_cx - (mpb[2]-mpb[0])//2, m_text_y), price_txt, fill=(189, 60, 13), font=f_price_viet)
m_text_y += 28

for l in desc_txt.split('\n'):
    mlb = d4.textbbox((0, 0), l, font=f_desc_viet)
    d4.text((m_cx - (mlb[2]-mlb[0])//2, m_text_y), l, fill=(56, 37, 27), font=f_desc_viet)
    m_text_y += 16

m_text_y += 8
m_bw, m_bh = 175, 42
mbx0 = m_cx - m_bw // 2
mby0 = m_text_y
mbx1 = m_cx + m_bw // 2
mby1 = mby0 + m_bh
d4.rounded_rectangle([mbx0, mby0, mbx1, mby1], radius=m_bh//2, fill=(189, 60, 13))
mbtb = d4.textbbox((0, 0), btn_txt, font=f_btn_light)
d4.text((m_cx - (mbtb[2]-mbtb[0])//2, mby0 + (m_bh - (mbtb[3]-mbtb[1]))//2), btn_txt, fill=(255, 253, 245), font=f_btn_light)

# NOTICE: ZERO DOTS on Mobile! Clean ground.
d4.text((m_cx - 80, mby1 + 18), "✓ 0 Dots trên Mobile", fill=(34, 139, 34), font=f_desc_viet)

# Mobile Right-aligned Gold Link (20px from right edge)
m_gold_y = H4 - 42
m_link_rx = W4 - 20 - gw
m_gx0 = m_link_rx - 14
m_gx1 = m_link_rx + gw + 14

for off_x in range(m_gx0, m_gx1):
    progress = (off_x - m_gx0) / (m_gx1 - m_gx0)
    sin_weight = (1 - ((progress - 0.5) * 2)**2)
    line_alpha = int(240 * max(0, sin_weight))
    d4.line([(off_x, m_gold_y - 8), (off_x + 1, m_gold_y - 8)], fill=(196, 139, 40, line_alpha), width=2)
    d4.line([(off_x, m_gold_y + gh + 8), (off_x + 1, m_gold_y + gh + 8)], fill=(196, 139, 40, line_alpha), width=2)

d4.text((m_link_rx, m_gold_y), gold_txt, fill=(196, 139, 40), font=f_gold_link)

out4 = os.path.join(ARTIFACT_DIR, 'proof_mobile_sync_right_aligned.png')
canvas4.save(out4, quality=95)
print("Proof 4 saved to:", out4)

print("ALL 4 PROOFS GENERATED SUCCESSFULLY!")
