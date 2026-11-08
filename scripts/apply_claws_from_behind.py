"""
apply_claws_from_behind.py
--------------------------
1. Restore rooster_mascot_body_opt.webp from clean master image:
   - Erase 100% of any synthetic red patches or floating fragments above the board.
   - Body stays 100% behind the board.
2. Refine rooster_claw_top.webp:
   - Claw hooks naturally from behind over the top wood rail.
   - Zero white halo (OpenCV decontamination).
3. Update order.html (desktop and responsive media queries).
4. Export visual inspection proofs.
"""

import os
import sys
from PIL import Image
import numpy as np
import cv2

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_PATH = os.path.join(ROOT, 'images', 'order', 'rooster_menu_option1_viewer_gaze_3000px.png')
BODY_OUT = os.path.join(ROOT, 'images', 'order', 'rooster_mascot_body_opt.webp')
CLAW_TOP_OUT = os.path.join(ROOT, 'images', 'order', 'rooster_claw_top.webp')
CLAW_MID_OUT = os.path.join(ROOT, 'images', 'order', 'rooster_claw_mid.webp')
ORDER_HTML = os.path.join(ROOT, 'order.html')
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\2785f21c-2c13-4449-9d0b-a1cb6cc5698a'

print("=== BẮT ĐẦU XỬ LÝ CÁNH TAY NHÔ TỪ SAU LÊN & XÓA SẠCH CÁNH ĐỎ ===")

# 1. Load clean master image
im_master = Image.open(MASTER_PATH).convert('RGBA')
arr_master = np.array(im_master)
H, W, _ = arr_master.shape

# -------------------------------------------------------------
# 1. KHÔI PHỤC LAYER 1 (ROOSTER_MASCOT_BODY_OPT.WEBP)
# -------------------------------------------------------------
# The board in 3000px space: starts at x=1007, y=620.
# Any pixel at x >= 1007 that is NOT part of the natural chicken body should be clean.
# Specifically:
# - Erase all floating claws or artifacts at x >= 1007:
#   Top claw at x: 1420..1850, y: 620..870 -> ERASE from background layer
#   Mid claw at x >= 1007, y: 1270..1700 -> ERASE from background layer (held in foreground claw)
# - Absolutely NO synthetic bridge or red patches anywhere!

body_arr = arr_master.copy()

# Erase the top claw region from Layer 1
erase_top = (np.arange(W)[None, :] >= 1200) & (np.arange(H)[:, None] >= 600) & (np.arange(H)[:, None] <= 900)
body_arr[erase_top, 3] = 0

# Erase any mid claw pixels overlapping into the board (x >= 1007)
erase_mid = (np.arange(W)[None, :] >= 1007) & (np.arange(H)[:, None] >= 1270) & (np.arange(H)[:, None] <= 1700)
body_arr[erase_mid, 3] = 0

# Verify: Count red pixels at x >= 1007, y <= 700
sub_check = body_arr[:700, 1007:]
red_check = (sub_check[:, :, 3] > 20) & (sub_check[:, :, 0] > 130) & (sub_check[:, :, 1] < 90) & (sub_check[:, :, 2] < 90)
print(f"Số lượng pixel đỏ thừa ở vùng trên bảng sau khi dọn sạch: {np.sum(red_check)}")

# Resize cleanly to 1200px width
target_w = 1200
target_h = int(H * (target_w / W))
body_clean = Image.fromarray(body_arr).resize((target_w, target_h), Image.Resampling.LANCZOS)
body_clean.save(BODY_OUT, format='WEBP', quality=95)
print(f"-> Đã lưu Layer 1 sạch: {BODY_OUT} ({target_w}x{target_h})")

# -------------------------------------------------------------
# 2. TÁCH CHIẾT MÓNG VUỐT TRÊN NHÔ TỪ SAU LÊN (ROOSTER_CLAW_TOP.WEBP)
# -------------------------------------------------------------
# In master: claw is at x: 1440..1810, y: 640..845
claw_crop = arr_master[640:845, 1440:1810].copy()
ch, cw, _ = claw_crop.shape

# The hand is coming from BEHIND the board and curling forward:
# The top edge of the hand rises smoothly.
# The bottom fingers hook down over the wood rail.
# Clean white fringes using OpenCV Distance Transform
alpha = claw_crop[:, :, 3]
mask = (alpha > 15).astype(np.uint8)

dist = cv2.distanceTransform(mask, cv2.DIST_L2, 3)
# Decontaminate border pixels
rim = (alpha > 10) & (dist <= 3)
claw_crop[rim, 0] = 48
claw_crop[rim, 1] = 40
claw_crop[rim, 2] = 32

# Soft edge feathering
claw_crop[dist <= 1.0, 3] = 0
alpha_soft = cv2.GaussianBlur(claw_crop[:, :, 3].astype(np.float32), (3, 3), 0.6)
claw_crop[:, :, 3] = np.clip(alpha_soft, 0, 255).astype(np.uint8)

claw_im = Image.fromarray(claw_crop)
claw_im.save(CLAW_TOP_OUT, format='WEBP', quality=95)
print(f"-> Đã lưu Layer 3 Top Claw nhô từ sau lên: {CLAW_TOP_OUT} (Kích thước: {claw_im.size})")

# -------------------------------------------------------------
# 3. CẬP NHẬT CSS TRONG ORDER.HTML
# -------------------------------------------------------------
with open(ORDER_HTML, 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Update Desktop CSS
desktop_claw_re = re.compile(r'/\* Foreground Claws.*?\n\s*\.rooster-claw-top\s*\{[^}]*\}\s*\.rooster-claw-mid\s*\{[^}]*\}', re.DOTALL)

new_desktop_claw = """    /* Foreground Claws (Layer 3 - Emerging Naturally from Behind over Board Rim) */
    .rooster-claw-top {
      position: absolute;
      left: 105px;
      top: -14px;
      width: 85px;
      height: auto;
      z-index: 35;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(0 3px 5px rgba(10, 5, 2, 0.65));
      transition: all 0.3s ease;
    }

    .rooster-claw-mid {
      position: absolute;
      left: -5px;
      top: 172px;
      width: 35px;
      height: auto;
      z-index: 35;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(2px 2px 5px rgba(10, 5, 2, 0.65));
      transition: all 0.3s ease;
    }"""

if desktop_claw_re.search(html):
    html = desktop_claw_re.sub(new_desktop_claw, html)
    print("-> Đã cập nhật Desktop CSS: .rooster-claw-top left: 105px, top: -14px, width: 85px")

# Update Media Query 1023px
media_1023_re = re.compile(r'(@media\s*\(\s*max-width:\s*1023px\s*\)\s*\{.*?\.rooster-claw-top\s*\{)[^}]*(\}\s*\.rooster-claw-mid\s*\{)[^}]*(\})', re.DOTALL)
if media_1023_re.search(html):
    def rep_1023(m):
        return f"{m.group(1)}\n        left: 80px;\n        top: -12px;\n        width: 68px;\n      {m.group(2)}\n        left: -4px;\n        top: 138px;\n        width: 28px;\n      {m.group(3)}"
    html = media_1023_re.sub(rep_1023, html)
    print("-> Đã đồng bộ Responsive CSS @media (max-width: 1023px)")

# Update Media Query 767px
media_767_top_re = re.compile(r'(@media\s*\(\s*max-width:\s*767px\s*\)\s*\{.*?\.rooster-claw-top\s*\{)[^}]*(\})', re.DOTALL)
if media_767_top_re.search(html):
    def rep_767(m):
        return f"{m.group(1)}\n        left: 65px;\n        top: -10px;\n        width: 55px;\n      {m.group(2)}"
    html = media_767_top_re.sub(rep_767, html)
    print("-> Đã đồng bộ Responsive CSS @media (max-width: 767px)")

with open(ORDER_HTML, 'w', encoding='utf-8') as f:
    f.write(html)
print("-> Đã lưu order.html thành công!")

# -------------------------------------------------------------
# 4. RENDER COMPOSITE NGHIỆM THU THỊ GIÁC (VISUAL PROOFS)
# -------------------------------------------------------------
print("Bắt đầu render composite nghiệm thu sau dọn sạch...")

mascot_final = Image.open(BODY_OUT).convert('RGBA')
board_final = Image.open(os.path.join(ROOT, 'images', 'order', 'clipboard_board_only.webp')).convert('RGBA')
foot_block_final = Image.open(os.path.join(ROOT, 'images', 'order', 'rooster_foot_block.webp')).convert('RGBA')
claw_top_final = Image.open(CLAW_TOP_OUT).convert('RGBA')
claw_mid_final = Image.open(CLAW_MID_OUT).convert('RGBA')

canvas_w, canvas_h = 1050, 860
proof = Image.new('RGBA', (canvas_w, canvas_h), (242, 238, 230, 255))

# 0. Foot block
fb_scaled = foot_block_final.resize((330, int(330 * 85 / 336)), Image.Resampling.LANCZOS)
proof.paste(fb_scaled, (0, 735), fb_scaled)

# 1. Mascot body (Clean Layer 1 behind board)
m_w = 620
m_h = int(620 * mascot_final.height / mascot_final.width)
mascot_scaled = mascot_final.resize((m_w, m_h), Image.Resampling.LANCZOS)
proof.paste(mascot_scaled, (0, 15), mascot_scaled)

# 2. Clipboard (Layer 2)
board_x, board_y = 260, 175
proof.paste(board_final, (board_x, board_y), board_final)

# 3. Claws (Layer 3 - emerging naturally from behind)
ct_w = 85
ct_h = int(85 * claw_top_final.height / claw_top_final.width)
claw_top_scaled = claw_top_final.resize((ct_w, ct_h), Image.Resampling.LANCZOS)
proof.paste(claw_top_scaled, (board_x + 105, board_y - 14), claw_top_scaled)

cm_w = 35
cm_h = int(35 * claw_mid_final.height / claw_mid_final.width)
claw_mid_scaled = claw_mid_final.resize((cm_w, cm_h), Image.Resampling.LANCZOS)
proof.paste(claw_mid_scaled, (board_x - 5, board_y + 172), claw_mid_scaled)

# Export Full Proof
full_path = os.path.join(ARTIFACT_DIR, 'full_chicken_from_behind_preview.png')
proof.save(full_path)

# Export Top Claw Closeup (Showing clean wood top rail, zero red wings, natural grip from behind)
top_arm_closeup = proof.crop((230, 80, 530, 250))
top_path = os.path.join(ARTIFACT_DIR, 'inspect_top_claw_from_behind.png')
top_arm_closeup.save(top_path)

print(f"-> Đã xuất cận cảnh móng vuốt nhô từ sau lên: {top_path}")
print(f"-> Đã xuất toàn cảnh: {full_path}")
print("=== HOÀN TẤT THÀNH CÔNG TOÀN BỘ YÊU CẦU! ===")

