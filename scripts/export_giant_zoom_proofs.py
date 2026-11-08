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
    # Giant elevated typography
    f_title_serif = ImageFont.truetype('timesbd.ttf', 28)
    f_price_sans = ImageFont.truetype('arialbd.ttf', 28)
    f_desc_sans = ImageFont.truetype('arial.ttf', 14.5)
    f_btn_sans = ImageFont.truetype('arialbd.ttf', 14.5)

    f_footer_label = ImageFont.truetype('arial.ttf', 10)
    f_footer_phone = ImageFont.truetype('arialbd.ttf', 14)
    f_footer_btn = ImageFont.truetype('arialbd.ttf', 11.5)

    f_m_title = ImageFont.truetype('timesbd.ttf', 23)
    f_m_price = ImageFont.truetype('arialbd.ttf', 23)
    f_m_desc = ImageFont.truetype('arial.ttf', 13.5)
    f_m_btn = ImageFont.truetype('arialbd.ttf', 13.5)
    
    f_caption = ImageFont.truetype('arialbd.ttf', 13)
except:
    f_quote = f_title_serif = f_price_sans = f_desc_sans = f_btn_sans = ImageFont.load_default()
    f_footer_label = f_footer_phone = f_footer_btn = ImageFont.load_default()
    f_m_title = f_m_price = f_m_desc = f_m_btn = ImageFont.load_default()
    f_caption = ImageFont.load_default()

dishes = [
    (im_dish0, "Bánh Canh Gà Đặc Biệt", "70.000₫", "Thịt gà ta da vàng giòn mọng nước, trứng non béo ngậy.\nNước dùng ninh xương thanh ngọt đậm đà."),
    (im_dish1, "Cơm Gà Xé Phay", "52.000₫", "Cơm nghệ vàng óng nấu từ nước luộc gà béo ngọt..."),
    (im_dish2, "Gỏi Gà Ta", "50.000₫", "Thịt gà thả vườn xé phay giòn ngọt trộn hành tây..."),
    (im_dish3, "Xôi Gà Trứng Non", "40.000₫", "Xôi nếp nương dẻo quánh thoang thoảng mỡ gà..."),
    (im_dish4, "Mì Gà Ta Truyền Thống", "55.000₫", "Sợi mì trứng dai vàng óng, thịt gà ta xé ngọt mềm...")
]

# -------------------------------------------------------------------------
# PROOF 1: Desktop Viewport (1024x720) - Giant Dishes & Soft Faded BG
# -------------------------------------------------------------------------
W1, H1 = 1024, 720
# Base clean light warm parchment
canvas1 = Image.new('RGBA', (W1, H1), (250, 245, 235, 255))

# Soft blurred faded menu-bg-3 (opacity 22%, blur 2px)
bg_scaled = im_bg.resize((W1, int(W1 * im_bg.size[1] / im_bg.size[0])), Image.Resampling.LANCZOS).crop((0, 0, W1, H1))
bg_blurred = bg_scaled.filter(ImageFilter.GaussianBlur(1.8))
# Blend with 0.22 opacity
canvas1 = Image.blend(canvas1, bg_blurred, 0.22)

# Central Gourmet Radial Spotlight
spotlight = Image.new('RGBA', (W1, H1), (0, 0, 0, 0))
sp_draw = ImageDraw.Draw(spotlight)
for r in range(460, 0, -20):
    alpha = int(160 * (1 - r / 460))
    sp_draw.ellipse([512 - r, 300 - r * 0.65, 512 + r, 300 + r * 0.65], fill=(255, 255, 255, alpha))
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

# 1. Inactive Far Dishes (Zoomed x2-x3 to 280px, spread wide)
plate_far = 280
dish3_s = dishes[3][0].resize((plate_far, plate_far), Image.Resampling.LANCZOS)
canvas1.paste(dish3_s, (cx - 490 - plate_far//2, card_cy - plate_far//2 + 30), dish3_s)

dish2_s = dishes[2][0].resize((plate_far, plate_far), Image.Resampling.LANCZOS)
canvas1.paste(dish2_s, (cx + 490 - plate_far//2, card_cy - plate_far//2 + 30), dish2_s)

# 2. Inactive Near Dishes (Zoomed x2-x3 to 360px, spread wide)
plate_near = 360
dish4_s = dishes[4][0].resize((plate_near, plate_near), Image.Resampling.LANCZOS)
canvas1.paste(dish4_s, (cx - 280 - plate_near//2, card_cy - plate_near//2 + 15), dish4_s)

dish1_s = dishes[1][0].resize((plate_near, plate_near), Image.Resampling.LANCZOS)
canvas1.paste(dish1_s, (cx + 280 - plate_near//2, card_cy - plate_near//2 + 15), dish1_s)

# 3. Active Giant Hero Dish (Zoomed x5 to 500px!)
plate_act = 500
dish0_s = dishes[0][0].resize((plate_act, plate_act), Image.Resampling.LANCZOS)
px = cx - plate_act // 2
py = card_cy - plate_act // 2 - 50

# Deep Contact Shadow for giant tray
tray_shadow = Image.new('RGBA', canvas1.size, (0, 0, 0, 0))
ts_draw = ImageDraw.Draw(tray_shadow)
for s_off in range(1, 24):
    s_alpha = int(32 * (1 - s_off / 24))
    ts_draw.ellipse([px + s_off*2, py + 34 + s_off*2, px + plate_act - s_off*2, py + plate_act + 26 + s_off], fill=(35, 18, 10, s_alpha))
canvas1.alpha_composite(tray_shadow)

# Paste Giant Hero Dish
canvas1.paste(dish0_s, (px, py), dish0_s)

# 4. Elevated Large Typography directly below tray
cy = py + plate_act - 16

# Title: Playfair Display in Deep Mahogany Coffee (#24120A)
title_txt = dishes[0][1]
tb = d1.textbbox((0, 0), title_txt, font=f_title_serif)
d1.text((cx - (tb[2]-tb[0])//2 + 1, cy + 1), title_txt, fill=(255, 255, 255, 190), font=f_title_serif)
d1.text((cx - (tb[2]-tb[0])//2, cy), title_txt, fill=(36, 18, 10), font=f_title_serif)
cy += 34

# Price: Plus Jakarta Sans in Warm Chili Orange (#BD3C0D)
price_txt = dishes[0][2]
pb = d1.textbbox((0, 0), price_txt, font=f_price_sans)
d1.text((cx - (pb[2]-pb[0])//2 + 1, cy + 1), price_txt, fill=(255, 255, 255, 180), font=f_price_sans)
d1.text((cx - (pb[2]-pb[0])//2, cy), price_txt, fill=(189, 60, 13), font=f_price_sans)
cy += 32

# Description: Plus Jakarta Sans in Warm Chestnut Brown (#4A3528)
desc_txt = dishes[0][3]
for l in desc_txt.split('\n'):
    lb = d1.textbbox((0, 0), l, font=f_desc_sans)
    d1.text((cx - (lb[2]-lb[0])//2, cy), l, fill=(74, 53, 40), font=f_desc_sans)
    cy += 18

cy += 6
# Prominent Warm CTA Button
bw, bh = 200, 44
bx0 = cx - bw // 2
by0 = cy
bx1 = cx + bw // 2
by1 = by0 + bh

# Button shadow
btn_shadow = Image.new('RGBA', canvas1.size, (0, 0, 0, 0))
bs_draw = ImageDraw.Draw(btn_shadow)
for b_off in range(1, 14):
    b_alpha = int(28 * (1 - b_off / 14))
    bs_draw.rounded_rectangle([bx0, by0 + b_off//2, bx1, by1 + b_off], radius=bh//2, fill=(138, 43, 14, b_alpha))
canvas1.alpha_composite(btn_shadow)

d1.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, fill=(189, 60, 13))
btn_txt = "ĐẶT MÓN NGAY"
btb = d1.textbbox((0, 0), btn_txt, font=f_btn_sans)
d1.text((cx - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 253, 245), font=f_btn_sans)

# Navigation chevrons
d1.polygon([(cx - 240, card_cy + 85), (cx - 220, card_cy + 65), (cx - 220, card_cy + 105)], fill=(158, 94, 43, 150))
d1.polygon([(cx + 240, card_cy + 85), (cx + 220, card_cy + 65), (cx + 220, card_cy + 105)], fill=(158, 94, 43, 150))

# Dots safely below button
dots_y = by1 + 12
for i, dx_off in enumerate([-28, -14, 0, 14, 28]):
    dot_color = (196, 78, 32, 255) if i == 0 else (214, 199, 178, 255)
    dot_w = 26 if i == 0 else 8
    d1.rounded_rectangle([cx + dx_off - dot_w//2, dots_y, cx + dx_off + dot_w//2, dots_y + 8], radius=4, fill=dot_color)

# Footer Bar
fy = H1 - 42
d1.rounded_rectangle([48, fy, W1 - 48, fy + 34], radius=16, fill=(255, 255, 255, 215), outline=(201, 154, 74, 50), width=1)
d1.text((68, fy + 4), "ĐẶT GIAO TẬN NƠI • HOTLINE", fill=(138, 74, 28), font=f_footer_label)
d1.text((68, fy + 16), "090 642 79 38", fill=(26, 20, 16), font=f_footer_phone)
btn_lbl = "Xem Toàn Bộ Thực Đơn  →"
bb = d1.textbbox((0, 0), btn_lbl, font=f_footer_btn)
d1.rounded_rectangle([W1 - 250, fy + 3, W1 - 65, fy + 31], radius=14, fill=(26, 20, 16))
d1.text((W1 - 250 + (185 - (bb[2]-bb[0]))//2, fy + 8), btn_lbl, fill=(250, 248, 245), font=f_footer_btn)

# Visual measurement annotation
plate_top_y = py
gap_val = plate_top_y - story_bar_h
d1.line([(cx + 260, story_bar_h), (cx + 260, plate_top_y)], fill=(34, 139, 34, 220), width=2)
d1.text((cx + 268, story_bar_h + gap_val // 2 - 8), f"Khoảng thở trần an toàn: {gap_val}px (>= 28px)", fill=(34, 139, 34, 255), font=f_desc_sans)

out1 = os.path.join(ARTIFACT_DIR, 'proof_giant_zoom_desktop.png')
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

# Mobile spotlight
spotlight2 = Image.new('RGBA', (W2, H2), (0, 0, 0, 0))
sp2_draw = ImageDraw.Draw(spotlight2)
for r in range(230, 0, -15):
    alpha = int(160 * (1 - r / 230))
    sp2_draw.ellipse([195 - r, 340 - r * 0.75, 195 + r, 340 + r * 0.75], fill=(255, 255, 255, alpha))
canvas2.alpha_composite(spotlight2)

d2 = ImageDraw.Draw(canvas2)

m_story_h = 32
d2.rectangle([0, 0, W2, m_story_h], fill=(36, 22, 14, 255))
d2.text((16, 8), "Gìn giữ vị quê đượm ấm...", fill=(235, 218, 195, 220), font=f_desc_sans)

rw_m, rh_m = 88, 84
rooster_sm = im_rooster.resize((rw_m, rh_m), Image.Resampling.LANCZOS)
canvas2.paste(rooster_sm, (12, m_story_h), rooster_sm)

m_cx = 195
m_cy = 360

# Flanking dishes on mobile
m_near_w = 230
dish4_sm = dishes[4][0].resize((m_near_w, m_near_w), Image.Resampling.LANCZOS)
canvas2.paste(dish4_sm, (m_cx - 200 - m_near_w//2, m_cy - m_near_w//2), dish4_sm)

dish1_sm = dishes[1][0].resize((m_near_w, m_near_w), Image.Resampling.LANCZOS)
canvas2.paste(dish1_sm, (m_cx + 200 - m_near_w//2, m_cy - m_near_w//2), dish1_sm)

# Center Dish Mobile (Zoomed x5 to 345px)
m_plate = 345
dish0_sm = dishes[0][0].resize((m_plate, m_plate), Image.Resampling.LANCZOS)
m_px = m_cx - m_plate // 2
m_py = m_cy - m_plate // 2 - 50

# Mobile contact shadow
m_tray_shadow = Image.new('RGBA', canvas2.size, (0, 0, 0, 0))
mts_draw = ImageDraw.Draw(m_tray_shadow)
for s_off in range(1, 16):
    s_alpha = int(30 * (1 - s_off / 16))
    mts_draw.ellipse([m_px + s_off*2, m_py + 26 + s_off*2, m_px + m_plate - s_off*2, m_py + m_plate + 20 + s_off], fill=(35, 18, 10, s_alpha))
canvas2.alpha_composite(m_tray_shadow)

canvas2.paste(dish0_sm, (m_px, m_py), dish0_sm)

# Mobile Typography
m_text_y = m_py + m_plate - 14

mtb = d2.textbbox((0, 0), title_txt, font=f_m_title)
d2.text((m_cx - (mtb[2]-mtb[0])//2 + 1, m_text_y + 1), title_txt, fill=(255, 255, 255, 190), font=f_m_title)
d2.text((m_cx - (mtb[2]-mtb[0])//2, m_text_y), title_txt, fill=(36, 18, 10), font=f_m_title)
m_text_y += 30

mpb = d2.textbbox((0, 0), price_txt, font=f_m_price)
d2.text((m_cx - (mpb[2]-mpb[0])//2 + 1, m_text_y + 1), price_txt, fill=(255, 255, 255, 180), font=f_m_price)
d2.text((m_cx - (mpb[2]-mpb[0])//2, m_text_y), price_txt, fill=(189, 60, 13), font=f_m_price)
m_text_y += 28

for l in desc_txt.split('\n'):
    mlb = d2.textbbox((0, 0), l, font=f_m_desc)
    d2.text((m_cx - (mlb[2]-mlb[0])//2, m_text_y), l, fill=(74, 53, 40), font=f_m_desc)
    m_text_y += 16

m_text_y += 8
m_bw, m_bh = 175, 42
mbx0 = m_cx - m_bw // 2
mby0 = m_text_y
mbx1 = m_cx + m_bw // 2
mby1 = mby0 + m_bh
d2.rounded_rectangle([mbx0, mby0, mbx1, mby1], radius=m_bh//2, fill=(189, 60, 13))
mbtb = d2.textbbox((0, 0), btn_txt, font=f_m_btn)
d2.text((m_cx - (mbtb[2]-mbtb[0])//2, mby0 + (m_bh - (mbtb[3]-mbtb[1]))//2), btn_txt, fill=(255, 253, 245), font=f_m_btn)

# Mobile dots
m_dots_y = mby1 + 14
for i, dx_off in enumerate([-28, -14, 0, 14, 28]):
    dot_color = (196, 78, 32, 255) if i == 0 else (214, 199, 178, 255)
    dot_w = 26 if i == 0 else 8
    d2.rounded_rectangle([m_cx + dx_off - dot_w//2, m_dots_y, m_cx + dx_off + dot_w//2, m_dots_y + 8], radius=4, fill=dot_color)

# Mobile footer
m_fy = H2 - 58
d2.rounded_rectangle([16, m_fy, W2 - 16, m_fy + 44], radius=14, fill=(255, 255, 255, 215), outline=(201, 154, 74, 50), width=1)
d2.text((28, m_fy + 6), "ĐẶT GIAO TẬN NƠI • HOTLINE", fill=(138, 74, 28), font=f_footer_label)
d2.text((28, m_fy + 18), "090 642 79 38", fill=(26, 20, 16), font=f_footer_phone)
m_btn_lbl = "Xem Toàn Bộ Thực Đơn  →"
m_bb = d2.textbbox((0, 0), m_btn_lbl, font=f_footer_btn)
d2.rounded_rectangle([W2 - 180, m_fy + 6, W2 - 24, m_fy + 38], radius=12, fill=(26, 20, 16))
d2.text((W2 - 180 + (156 - (m_bb[2]-m_bb[0]))//2, m_fy + 12), m_btn_lbl, fill=(250, 248, 245), font=f_footer_btn)

out2 = os.path.join(ARTIFACT_DIR, 'proof_giant_zoom_mobile_390.png')
canvas2.save(out2, quality=95)
print("Proof 2 saved to:", out2)


# -------------------------------------------------------------------------
# PROOF 3: Typography & Dish Detail Closeup (760x540)
# -------------------------------------------------------------------------
W3, H3 = 760, 540
closeup = canvas1.crop((cx - 380, py + 120, cx + 380, py + 120 + H3)).copy()
d3 = ImageDraw.Draw(closeup)

d3.text((18, 12), "CẬN CẢNH MÂM GÀ TA KHỔNG LỒ X5 & TYPOGRAPHY PHÓNG TO SẮC NÉT", fill=(36, 18, 10), font=f_caption)
d3.text((18, 30), "• Nền giấy mộc làm mờ 78% & khử sạch họa tiết gây rối, giúp món ăn nổi bật tuyệt đối", fill=(74, 53, 40), font=f_desc_sans)
d3.text((18, 48), "• Tiêu đề Playfair Display phóng to 28px nét thanh nét đậm sang nhã, rõ ràng", fill=(74, 53, 40), font=f_desc_sans)
d3.text((18, 66), "• Giá tiền 28px màu cam ớt đậm vị, mô tả 14.5px thoáng mắt, nút Đặt món 44px bề thế", fill=(74, 53, 40), font=f_desc_sans)

out3 = os.path.join(ARTIFACT_DIR, 'proof_giant_zoom_closeup.png')
closeup.save(out3, quality=95)
print("Proof 3 saved to:", out3)

print("ALL 3 GIANT ZOOM PROOFS COMPLETED SUCCESSFULLY!")
