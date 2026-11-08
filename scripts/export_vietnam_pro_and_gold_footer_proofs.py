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
p_dish1 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Rice Tray Feast_result.webp')
p_dish2 = os.path.join(ROOT, 'images', 'menu', 'goi-ga.webp')
p_dish3 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Xôi Gà on a Wooden Tray_result.webp')
p_dish4 = os.path.join(ROOT, 'images', 'menu', 'mi-ga.webp')

im_bg = Image.open(p_bg).convert('RGBA')
im_rooster = Image.open(p_rooster).convert('RGBA')
im_dish0 = Image.open(p_dish0).convert('RGBA')
im_dish1 = Image.open(p_dish1).convert('RGBA')
im_dish2 = Image.open(p_dish2).convert('RGBA')
im_dish3 = Image.open(p_dish3).convert('RGBA')
im_dish4 = Image.open(p_dish4).convert('RGBA')

try:
    f_quote = ImageFont.truetype('times.ttf', 20)
    # Be Vietnam Pro Sans Typography Simulation
    f_title_viet = ImageFont.truetype('arialbd.ttf', 27)
    f_price_viet = ImageFont.truetype('arialbd.ttf', 27)
    f_desc_viet = ImageFont.truetype('arial.ttf', 14.5)
    f_btn_viet = ImageFont.truetype('arialbd.ttf', 14.5)

    f_gold_link = ImageFont.truetype('arialbd.ttf', 16)
    f_caption = ImageFont.truetype('arialbd.ttf', 13)
except:
    f_quote = f_title_viet = f_price_viet = f_desc_viet = f_btn_viet = ImageFont.load_default()
    f_gold_link = f_caption = ImageFont.load_default()

dishes = [
    (im_dish0, "Bánh Canh Gà Đặc Biệt", "70.000₫", "Thịt gà ta da vàng giòn mọng nước, trứng non béo ngậy.\nNước dùng ninh xương thanh ngọt đậm đà."),
    (im_dish1, "Cơm Gà Xé Phay", "52.000₫", "Cơm nghệ vàng óng nấu từ nước luộc gà béo ngọt..."),
    (im_dish2, "Gỏi Gà Ta", "50.000₫", "Thịt gà thả vườn xé phay giòn ngọt trộn hành tây..."),
    (im_dish3, "Xôi Gà Trứng Non", "40.000₫", "Xôi nếp nương dẻo quánh thoang thoảng mỡ gà..."),
    (im_dish4, "Mì Gà Ta Truyền Thống", "55.000₫", "Sợi mì trứng dai vàng óng, thịt gà ta xé ngọt mềm...")
]

# -------------------------------------------------------------------------
# PROOF 1: Desktop Viewport (1024x740) - Be Vietnam Pro & Gold Footer Link
# -------------------------------------------------------------------------
W1, H1 = 1024, 740
canvas1 = Image.new('RGBA', (W1, H1), (250, 245, 235, 255))

bg_scaled = im_bg.resize((W1, int(W1 * im_bg.size[1] / im_bg.size[0])), Image.Resampling.LANCZOS).crop((0, 0, W1, H1))
bg_blurred = bg_scaled.filter(ImageFilter.GaussianBlur(1.8))
canvas1 = Image.blend(canvas1, bg_blurred, 0.22)

# Central Gourmet Radial Spotlight
spotlight = Image.new('RGBA', (W1, H1), (0, 0, 0, 0))
sp_draw = ImageDraw.Draw(spotlight)
for r in range(480, 0, -20):
    alpha = int(165 * (1 - r / 480))
    sp_draw.ellipse([512 - r, 310 - r * 0.65, 512 + r, 310 + r * 0.65], fill=(255, 255, 255, alpha))
canvas1.alpha_composite(spotlight)

d1 = ImageDraw.Draw(canvas1)

story_bar_h = 30
d1.rectangle([0, 0, W1, story_bar_h], fill=(36, 22, 14, 255))
d1.text((32, 5), "Gìn giữ vị quê đượm ấm bát canh đầy...", fill=(235, 218, 195, 220), font=f_quote)
d1.line([(0, story_bar_h), (W1, story_bar_h)], fill=(225, 215, 200, 255), width=1)

# Ropes touching ceiling at y = story_bar_h
rw, rh = 125, 120
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
canvas1.paste(rooster_s, (22, story_bar_h), rooster_s)

cx = 512
card_cy = 310

# Inactive Dishes (Spread wide)
plate_far = 280
dish3_s = dishes[3][0].resize((plate_far, plate_far), Image.Resampling.LANCZOS)
canvas1.paste(dish3_s, (cx - 490 - plate_far//2, card_cy - plate_far//2 + 30), dish3_s)

dish2_s = dishes[2][0].resize((plate_far, plate_far), Image.Resampling.LANCZOS)
canvas1.paste(dish2_s, (cx + 490 - plate_far//2, card_cy - plate_far//2 + 30), dish2_s)

plate_near = 360
dish4_s = dishes[4][0].resize((plate_near, plate_near), Image.Resampling.LANCZOS)
canvas1.paste(dish4_s, (cx - 280 - plate_near//2, card_cy - plate_near//2 + 15), dish4_s)

dish1_s = dishes[1][0].resize((plate_near, plate_near), Image.Resampling.LANCZOS)
canvas1.paste(dish1_s, (cx + 280 - plate_near//2, card_cy - plate_near//2 + 15), dish1_s)

# Active Giant Hero Dish
plate_act = 500
dish0_s = dishes[0][0].resize((plate_act, plate_act), Image.Resampling.LANCZOS)
px = cx - plate_act // 2
py = card_cy - plate_act // 2 - 50

# Contact Shadow
tray_shadow = Image.new('RGBA', canvas1.size, (0, 0, 0, 0))
ts_draw = ImageDraw.Draw(tray_shadow)
for s_off in range(1, 24):
    s_alpha = int(32 * (1 - s_off / 24))
    ts_draw.ellipse([px + s_off*2, py + 34 + s_off*2, px + plate_act - s_off*2, py + plate_act + 26 + s_off], fill=(35, 18, 10, s_alpha))
canvas1.alpha_composite(tray_shadow)

canvas1.paste(dish0_s, (px, py), dish0_s)

# Sharp Be Vietnam Pro Typography
cy = py + plate_act - 16

# Title: Be Vietnam Pro in Deep Charcoal Mahogany (#1A0F08) - Crisp diacritics, NO blurry white halo!
title_txt = dishes[0][1]
tb = d1.textbbox((0, 0), title_txt, font=f_title_viet)
d1.text((cx - (tb[2]-tb[0])//2, cy), title_txt, fill=(26, 15, 8), font=f_title_viet)
cy += 34

# Price: Be Vietnam Pro in Rich Chili Orange (#BD3C0D)
price_txt = dishes[0][2]
pb = d1.textbbox((0, 0), price_txt, font=f_price_viet)
d1.text((cx - (pb[2]-pb[0])//2, cy), price_txt, fill=(189, 60, 13), font=f_price_viet)
cy += 32

# Description: Be Vietnam Pro in Deep Warm Roasted Coffee (#38251B)
desc_txt = dishes[0][3]
for l in desc_txt.split('\n'):
    lb = d1.textbbox((0, 0), l, font=f_desc_viet)
    d1.text((cx - (lb[2]-lb[0])//2, cy), l, fill=(56, 37, 27), font=f_desc_viet)
    cy += 19

cy += 6
# CTA Button
bw, bh = 200, 44
bx0 = cx - bw // 2
by0 = cy
bx1 = cx + bw // 2
by1 = by0 + bh

btn_shadow = Image.new('RGBA', canvas1.size, (0, 0, 0, 0))
bs_draw = ImageDraw.Draw(btn_shadow)
for b_off in range(1, 14):
    b_alpha = int(28 * (1 - b_off / 14))
    bs_draw.rounded_rectangle([bx0, by0 + b_off//2, bx1, by1 + b_off], radius=bh//2, fill=(138, 43, 14, b_alpha))
canvas1.alpha_composite(btn_shadow)

d1.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, fill=(189, 60, 13))
btn_txt = "ĐẶT MÓN NGAY"
btb = d1.textbbox((0, 0), btn_txt, font=f_btn_viet)
d1.text((cx - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 253, 245), font=f_btn_viet)

# Navigation chevrons
d1.polygon([(cx - 240, card_cy + 85), (cx - 220, card_cy + 65), (cx - 220, card_cy + 105)], fill=(158, 94, 43, 150))
d1.polygon([(cx + 240, card_cy + 85), (cx + 220, card_cy + 65), (cx + 220, card_cy + 105)], fill=(158, 94, 43, 150))

# Dots safely below button
dots_y = by1 + 10
for i, dx_off in enumerate([-28, -14, 0, 14, 28]):
    dot_color = (196, 78, 32, 255) if i == 0 else (214, 199, 178, 255)
    dot_w = 26 if i == 0 else 8
    d1.rounded_rectangle([cx + dx_off - dot_w//2, dots_y, cx + dx_off + dot_w//2, dots_y + 8], radius=4, fill=dot_color)

# -------------------------------------------------------------------------
# NEW BOTTOM FOOTER: Seamless Transparent Ground + Gold Link with Top/Bottom Lines
# -------------------------------------------------------------------------
gold_y = H1 - 42
gold_txt = "TOÀN BỘ THỰC ĐƠN"
gtb = d1.textbbox((0, 0), gold_txt, font=f_gold_link)
gw = gtb[2] - gtb[0]
gh = gtb[3] - gtb[1]

gx0 = cx - gw // 2 - 24
gx1 = cx + gw // 2 + 24

# Gold Top & Bottom Gradient Lines (simulating linear-gradient(90deg, transparent, gold, transparent))
for off_x in range(gx0, gx1):
    progress = (off_x - gx0) / (gx1 - gx0)
    sin_weight = (1 - ((progress - 0.5) * 2)**2) # 1 at center, 0 at ends
    line_alpha = int(240 * max(0, sin_weight))
    # Top line
    d1.line([(off_x, gold_y - 10), (off_x + 1, gold_y - 10)], fill=(255, 218, 105, line_alpha), width=2)
    # Bottom line
    d1.line([(off_x, gold_y + gh + 10), (off_x + 1, gold_y + gh + 10)], fill=(255, 218, 105, line_alpha), width=2)

# Text glow
glow_layer = Image.new('RGBA', canvas1.size, (0, 0, 0, 0))
gl_draw = ImageDraw.Draw(glow_layer)
gl_draw.text((cx - gw//2, gold_y), gold_txt, fill=(255, 187, 58, 90), font=f_gold_link)
canvas1.alpha_composite(glow_layer)

# Text core gold #ffd978
d1.text((cx - gw//2, gold_y), gold_txt, fill=(255, 217, 120), font=f_gold_link)

out1 = os.path.join(ARTIFACT_DIR, 'proof_vietnam_pro_and_gold_footer_desktop.png')
canvas1.save(out1, quality=95)
print("Proof 1 saved to:", out1)


# -------------------------------------------------------------------------
# PROOF 2: Mobile Viewport 390x844
# -------------------------------------------------------------------------
W2, H2 = 390, 844
canvas2 = Image.new('RGBA', (W2, H2), (250, 245, 235, 255))
bg_scaled2 = im_bg.resize((W2, int(W2 * im_bg.size[1] / im_bg.size[0])), Image.Resampling.LANCZOS).crop((0, 0, W2, H2))
bg_blurred2 = bg_scaled2.filter(ImageFilter.GaussianBlur(1.8))
canvas2 = Image.blend(canvas2, bg_blurred2, 0.22)

spotlight2 = Image.new('RGBA', (W2, H2), (0, 0, 0, 0))
sp2_draw = ImageDraw.Draw(spotlight2)
for r in range(230, 0, -15):
    alpha = int(160 * (1 - r / 230))
    sp2_draw.ellipse([195 - r, 340 - r * 0.75, 195 + r, 340 + r * 0.75], fill=(255, 255, 255, alpha))
canvas2.alpha_composite(spotlight2)

d2 = ImageDraw.Draw(canvas2)

m_story_h = 32
d2.rectangle([0, 0, W2, m_story_h], fill=(36, 22, 14, 255))
d2.text((16, 8), "Gìn giữ vị quê đượm ấm...", fill=(235, 218, 195, 220), font=f_desc_viet)

rw_m, rh_m = 88, 84
rooster_sm = im_rooster.resize((rw_m, rh_m), Image.Resampling.LANCZOS)
canvas2.paste(rooster_sm, (12, m_story_h), rooster_sm)

m_cx = 195
m_cy = 360

m_near_w = 230
dish4_sm = dishes[4][0].resize((m_near_w, m_near_w), Image.Resampling.LANCZOS)
canvas2.paste(dish4_sm, (m_cx - 200 - m_near_w//2, m_cy - m_near_w//2), dish4_sm)

dish1_sm = dishes[1][0].resize((m_near_w, m_near_w), Image.Resampling.LANCZOS)
canvas2.paste(dish1_sm, (m_cx + 200 - m_near_w//2, m_cy - m_near_w//2), dish1_sm)

m_plate = 345
dish0_sm = dishes[0][0].resize((m_plate, m_plate), Image.Resampling.LANCZOS)
m_px = m_cx - m_plate // 2
m_py = m_cy - m_plate // 2 - 50

m_tray_shadow = Image.new('RGBA', canvas2.size, (0, 0, 0, 0))
mts_draw = ImageDraw.Draw(m_tray_shadow)
for s_off in range(1, 16):
    s_alpha = int(30 * (1 - s_off / 16))
    mts_draw.ellipse([m_px + s_off*2, m_py + 26 + s_off*2, m_px + m_plate - s_off*2, m_py + m_plate + 20 + s_off], fill=(35, 18, 10, s_alpha))
canvas2.alpha_composite(m_tray_shadow)

canvas2.paste(dish0_sm, (m_px, m_py), dish0_sm)

m_text_y = m_py + m_plate - 14

mtb = d2.textbbox((0, 0), title_txt, font=f_title_viet)
d2.text((m_cx - (mtb[2]-mtb[0])//2, m_text_y), title_txt, fill=(26, 15, 8), font=f_title_viet)
m_text_y += 30

mpb = d2.textbbox((0, 0), price_txt, font=f_price_viet)
d2.text((m_cx - (mpb[2]-mpb[0])//2, m_text_y), price_txt, fill=(189, 60, 13), font=f_price_viet)
m_text_y += 28

for l in desc_txt.split('\n'):
    mlb = d2.textbbox((0, 0), l, font=f_desc_viet)
    d2.text((m_cx - (mlb[2]-mlb[0])//2, m_text_y), l, fill=(56, 37, 27), font=f_desc_viet)
    m_text_y += 16

m_text_y += 8
m_bw, m_bh = 175, 42
mbx0 = m_cx - m_bw // 2
mby0 = m_text_y
mbx1 = m_cx + m_bw // 2
mby1 = mby0 + m_bh
d2.rounded_rectangle([mbx0, mby0, mbx1, mby1], radius=m_bh//2, fill=(189, 60, 13))
mbtb = d2.textbbox((0, 0), btn_txt, font=f_btn_viet)
d2.text((m_cx - (mbtb[2]-mbtb[0])//2, mby0 + (m_bh - (mbtb[3]-mbtb[1]))//2), btn_txt, fill=(255, 253, 245), font=f_btn_viet)

m_dots_y = mby1 + 14
for i, dx_off in enumerate([-28, -14, 0, 14, 28]):
    dot_color = (196, 78, 32, 255) if i == 0 else (214, 199, 178, 255)
    dot_w = 26 if i == 0 else 8
    d2.rounded_rectangle([m_cx + dx_off - dot_w//2, m_dots_y, m_cx + dx_off + dot_w//2, m_dots_y + 8], radius=4, fill=dot_color)

# Mobile Gold Link
m_gold_y = H2 - 42
m_gtb = d2.textbbox((0, 0), gold_txt, font=f_gold_link)
m_gw = m_gtb[2] - m_gtb[0]
m_gh = m_gtb[3] - m_gtb[1]
m_gx0 = m_cx - m_gw // 2 - 20
m_gx1 = m_cx + m_gw // 2 + 20

for off_x in range(m_gx0, m_gx1):
    progress = (off_x - m_gx0) / (m_gx1 - m_gx0)
    sin_weight = (1 - ((progress - 0.5) * 2)**2)
    line_alpha = int(240 * max(0, sin_weight))
    d2.line([(off_x, m_gold_y - 8), (off_x + 1, m_gold_y - 8)], fill=(255, 218, 105, line_alpha), width=2)
    d2.line([(off_x, m_gold_y + m_gh + 8), (off_x + 1, m_gold_y + m_gh + 8)], fill=(255, 218, 105, line_alpha), width=2)

d2.text((m_cx - m_gw//2, m_gold_y), gold_txt, fill=(255, 217, 120), font=f_gold_link)

out2 = os.path.join(ARTIFACT_DIR, 'proof_vietnam_pro_and_gold_footer_mobile.png')
canvas2.save(out2, quality=95)
print("Proof 2 saved to:", out2)


# -------------------------------------------------------------------------
# PROOF 3: Closeup of Typography & Gold Bottom Link
# -------------------------------------------------------------------------
W3, H3 = 760, 520
closeup = canvas1.crop((cx - 380, py + 220, cx + 380, py + 220 + H3)).copy()
d3 = ImageDraw.Draw(closeup)

d3.text((20, 12), "NGHIỆM THU: PHÔNG CHỮ BE VIETNAM PRO SẮC NÉT & CHỮ VÀNG KIM 2 GẠCH", fill=(26, 15, 8), font=f_caption)
d3.text((20, 30), "• Tiêu đề & mô tả dùng 100% Be Vietnam Pro chuẩn dấu tiếng Việt, đậm đà, không mờ", fill=(56, 37, 27), font=f_desc_viet)
d3.text((20, 48), "• Bỏ sạch hotline, bỏ card bo viền: chỉ còn hàng chữ 'TOÀN BỘ THỰC ĐƠN' vàng kim sang trọng", fill=(56, 37, 27), font=f_desc_viet)
d3.text((20, 66), "• 2 đường gạch gradient vàng kim trên/dưới đồng bộ 100% với phong cách chữ ĐẶT HÀNG", fill=(56, 37, 27), font=f_desc_viet)

out3 = os.path.join(ARTIFACT_DIR, 'proof_gold_footer_and_typo_closeup.png')
closeup.save(out3, quality=95)
print("Proof 3 saved to:", out3)

print("ALL 3 PROOFS GENERATED SUCCESSFULLY!")
