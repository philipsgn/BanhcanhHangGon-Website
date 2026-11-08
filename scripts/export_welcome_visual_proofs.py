import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.getcwd()
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf'

p_chick = os.path.join(ROOT, 'images', 'story', 'cute-chicken.webp')
p_framed = os.path.join(ROOT, 'images', 'story', 'framed-restaurant-storefront.webp')

chick = Image.open(p_chick).convert('RGBA')
framed = Image.open(p_framed).convert('RGBA')

# 1. Desktop Render (1400 x 700)
W, H = 1400, 700
desk_img = Image.new('RGB', (W, H), (63, 35, 17))
draw = ImageDraw.Draw(desk_img)

# Chicken: width=195, rotated 8 deg, at left: -14, bottom: -8
cw = 195
ch = int(cw * chick.height / chick.width)
chick_scaled = chick.resize((cw, ch), Image.Resampling.LANCZOS)
chick_rot = chick_scaled.rotate(-8, expand=True, resample=Image.Resampling.BICUBIC)

chick_x = -14
chick_y = H - chick_rot.height + 8
desk_img.paste(chick_rot, (chick_x, chick_y), chick_rot)

# Framed Storefront: top aligned at y = 64
fw = 440
fh = int(fw * framed.height / framed.width)
framed_scaled = framed.resize((fw, fh), Image.Resampling.LANCZOS)
fx = W - fw - 90
fy = 64 # Top edge of photo frame
desk_img.paste(framed_scaled, (fx, fy))

# Copy text in Desktop: Title is top-aligned with photo frame top at y = 64
try:
    font_title = ImageFont.truetype('georgiab.ttf', 46)
    font_body = ImageFont.truetype('georgiai.ttf', 21)
except:
    font_title = ImageFont.load_default()
    font_body = ImageFont.load_default()

# Title top matches photo frame top (fy = 64)
draw.text((220, 64), 'Chào mừng bạn', fill=(255, 246, 230), font=font_title)
draw.text((220, 122), 'đến với Hàng Gòn', fill=(212, 163, 89), font=font_title)

# Gold hairline divider
draw.line([(220, 202), (275, 202)], fill=(212, 163, 89), width=2)

# Italic quote body text
quote_lines = [
    '“Hàng Gòn tự hào mang đến hương vị bánh canh gà đậm đà',
    'giữa lòng thành phố. Từng tô canh được nấu mỗi ngày với',
    'nước lèo ninh xương, thịt gà tươi chọn lọc, giữ trọn vẹn sự',
    'ngọt thanh nguyên bản như thuở ban đầu.”'
]
y_cur = 228
for l in quote_lines:
    draw.text((220, y_cur), l, fill=(255, 244, 224), font=font_body)
    y_cur += 36

p_desk_out = os.path.join(ARTIFACT_DIR, 'proof_section2_welcome_desktop.png')
desk_img.save(p_desk_out)
print(f'Exported {p_desk_out}')

# 2. Mobile Render (420 x 820)
MW, MH = 420, 820
mob_img = Image.new('RGB', (MW, MH), (63, 35, 17))
mdraw = ImageDraw.Draw(mob_img)

# Framed image on top
mfw = 300
mfh = int(mfw * framed.height / framed.width)
framed_mob = framed.resize((mfw, mfh), Image.Resampling.LANCZOS)
mob_img.paste(framed_mob, ((MW - mfw) // 2, 40))

# Text below
try:
    mfont_title = ImageFont.truetype('georgiab.ttf', 28)
    mfont_body = ImageFont.truetype('georgiai.ttf', 17)
except:
    mfont_title = ImageFont.load_default()
    mfont_body = ImageFont.load_default()

mdraw.text(((MW - 215) // 2, 440), 'Chào mừng bạn', fill=(255, 246, 230), font=mfont_title)
mdraw.text(((MW - 230) // 2, 476), 'đến với Hàng Gòn', fill=(212, 163, 89), font=mfont_title)

# Gold hairline divider
mdraw.line([((MW - 40) // 2, 520), ((MW + 40) // 2, 520)], fill=(212, 163, 89), width=2)

mquote_lines = [
    '“Hàng Gòn tự hào mang đến hương vị bánh canh gà đậm đà',
    'giữa lòng thành phố. Từng tô canh được nấu mỗi ngày',
    'với nước lèo ninh xương, thịt gà tươi chọn lọc, giữ trọn',
    'vẹn sự ngọt thanh nguyên bản như thuở ban đầu.”'
]
my_cur = 538
for ml in mquote_lines:
    bbox = mdraw.textbbox((0, 0), ml, font=mfont_body)
    tw = bbox[2] - bbox[0]
    mdraw.text(((MW - tw) // 2, my_cur), ml, fill=(255, 244, 224), font=mfont_body)
    my_cur += 26

# Chick centered at bottom
mcw = 125
mch = int(mcw * chick.height / chick.width)
chick_mob = chick.resize((mcw, mch), Image.Resampling.LANCZOS).rotate(-5, expand=True, resample=Image.Resampling.BICUBIC)
mob_img.paste(chick_mob, ((MW - chick_mob.width) // 2, MH - chick_mob.height + 6), chick_mob)

p_mob_out = os.path.join(ARTIFACT_DIR, 'proof_section2_welcome_mobile.png')
mob_img.save(p_mob_out)
print(f'Exported {p_mob_out}')
