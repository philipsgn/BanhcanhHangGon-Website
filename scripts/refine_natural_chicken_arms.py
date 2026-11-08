"""
refine_natural_chicken_arms.py
------------------------------
Artisan refinement addressing user feedback:
1. "Bắp tay nhìn chưa thật tự nhiên":
   - Replace artificial high-arched tube with gentle, anatomically correct wing slope
     flowing naturally from shoulder (y=575) to wrist (y=650).
   - Use high-fidelity layered feather texturing (golden neck hackles on top, dark glossy coverts below).
   - Ensure seamless connection without abrupt cutoffs at x=1435.
2. "Móng vuốt chưa bám khớp vào khung gỗ":
   - Correct Y offset of .rooster-claw-top in order.html from top: -2px to top: -20px so the horizontal
     resting line sits exactly on the top wooden rail/bevel, and curved talons grip down firmly over the wood.
   - Update responsive media queries for consistent alignment across all screen sizes.
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

print("=== BẮT ĐẦU TINH CHỈNH TỰ NHIÊN 2 CÁNH TAY CHÚ GÀ ===")

# 1. Load Master Image
im_master = Image.open(MASTER_PATH).convert('RGBA')
arr_master = np.array(im_master)
H, W, _ = arr_master.shape

# -------------------------------------------------------------
# 1. TỔNG HỢP BẮP TAY LÔNG VŨ TỰ NHIÊN (GENTLE NATURAL WING SLOPE)
# -------------------------------------------------------------
# Sample genuine golden feathers from shoulder/neck (x: 820..1060, y: 480..640)
p_shoulder = arr_master[480:640, 820:1060].copy()
# Sample genuine dark wing coverts (x: 450..700, y: 700..900)
p_wing = arr_master[700:900, 450:700].copy()

gw, gh = 480, 200
p_sh_r = cv2.resize(p_shoulder, (gw, gh), interpolation=cv2.INTER_LANCZOS4)
p_wg_r = cv2.resize(p_wing, (gw, gh), interpolation=cv2.INTER_LANCZOS4)

y_grad = np.linspace(0, 1, gh)[:, None, None]
x_grad = np.linspace(0, 1, gw)[None, :, None]

# Natural feather blend: golden plumage on top, shading to rich dark plumage below
wing_texture = (p_sh_r * (1.0 - y_grad * 0.7 - x_grad * 0.25) + p_wg_r * (y_grad * 0.7 + x_grad * 0.25))
wing_texture = np.clip(wing_texture, 0, 255).astype(np.float32)

# Polygon for natural gentle wing slope:
# Follows the shoulder slope: (1000, 575) -> (1120, 550) -> (1240, 560) -> (1360, 600) -> (1460, 645) -> wrist
poly_pts = np.array([
    [990, 575],
    [1080, 555],
    [1180, 550],
    [1280, 570],
    [1380, 610],
    [1465, 645],
    [1495, 665],
    [1495, 730],
    [1420, 725],
    [1320, 710],
    [1220, 690],
    [1120, 675],
    [1020, 660],
    [980, 640]
], dtype=np.int32)

mask_full = np.zeros((H, W), dtype=np.float32)
cv2.fillPoly(mask_full, [poly_pts], 1.0)
mask_full_smooth = cv2.GaussianBlur(mask_full, (17, 17), 0)

rx1, ry1, rx2, ry2 = 980, 540, 1500, 740
sub_m = mask_full_smooth[ry1:ry2, rx1:rx2, None]

canvas_master = arr_master.copy()
canvas_patch = canvas_master[ry1:ry2, rx1:rx2].astype(np.float32)
orig_alpha = (arr_master[ry1:ry2, rx1:rx2, 3:4] / 255.0)

# Soft seamless blend
new_weight = sub_m * (1.0 - orig_alpha * 0.35)
tex_patch = cv2.resize(wing_texture, (rx2 - rx1, ry2 - ry1), interpolation=cv2.INTER_LANCZOS4)
tex_patch[:, :, 3] = 255.0

blended = canvas_patch * (1.0 - new_weight) + tex_patch * new_weight
canvas_master[ry1:ry2, rx1:rx2] = np.clip(blended, 0, 255).astype(np.uint8)
canvas_master[ry1:ry2, rx1:rx2, 3] = np.maximum(canvas_master[ry1:ry2, rx1:rx2, 3], (sub_m[:, :, 0] * 255).astype(np.uint8))

print("1. Đã tổng hợp bắp tay lông vũ với độ dốc tự nhiên (gentle organic slope).")

# -------------------------------------------------------------
# 2. XUẤT ROOSTER_MASCOT_BODY_OPT.WEBP (LAYER 1)
# -------------------------------------------------------------
body_arr = canvas_master.copy()

# In Layer 1, preserve the wing flowing naturally into the board.
# Erase the foreground claws (talons hooking front of board) past x=1480, y=650:
erase_top_claw = (np.arange(W)[None, :] >= 1485) & (np.arange(H)[:, None] >= 650) & (np.arange(H)[:, None] <= 860) & (np.arange(W)[None, :] <= 1850)
body_arr[erase_top_claw, 3] = 0

# Erase the mid claw past x=1007
erase_mid_claw = (np.arange(W)[None, :] >= 1007) & (np.arange(H)[:, None] >= 1270) & (np.arange(H)[:, None] <= 1690)
body_arr[erase_mid_claw, 3] = 0

# Resize to 1200px width
target_w = 1200
target_h = int(H * (target_w / W))
body_im = Image.fromarray(body_arr).resize((target_w, target_h), Image.Resampling.LANCZOS)
body_im.save(BODY_OUT, format='WEBP', quality=95)
print(f"2. Đã lưu Layer 1: {BODY_OUT} ({target_w}x{target_h})")

# -------------------------------------------------------------
# 3. XUẤT ROOSTER_CLAW_TOP.WEBP (LAYER 3)
# -------------------------------------------------------------
# Crop top claw from x: 1420..1820, y: 620..850
claw_top_crop = arr_master[620:850, 1420:1820].copy()
alpha_top = claw_top_crop[:, :, 3]
mask_top = (alpha_top > 10).astype(np.uint8)

# Zero white halo decontamination
dist_in = cv2.distanceTransform(mask_top, cv2.DIST_L2, 3)
rim_white = (alpha_top > 10) & (dist_in <= 3) & (claw_top_crop[:, :, 0] > 180) & (claw_top_crop[:, :, 1] > 180) & (claw_top_crop[:, :, 2] > 180)
claw_top_crop[rim_white, 0] = 45
claw_top_crop[rim_white, 1] = 38
claw_top_crop[rim_white, 2] = 30

claw_top_crop[dist_in <= 1.2, 3] = 0
alpha_clean = cv2.GaussianBlur(claw_top_crop[:, :, 3].astype(np.float32), (3, 3), 0.5)
claw_top_crop[:, :, 3] = np.clip(alpha_clean, 0, 255).astype(np.uint8)

claw_top_im = Image.fromarray(claw_top_crop)
claw_top_im.save(CLAW_TOP_OUT, format='WEBP', quality=95)
print(f"3. Đã lưu Layer 3 Top Claw: {CLAW_TOP_OUT}")

# -------------------------------------------------------------
# 4. CẬP NHẬT CSS TRONG ORDER.HTML (TOP: -20PX CHO CLAW BÁM GỖ)
# -------------------------------------------------------------
with open(ORDER_HTML, 'r', encoding='utf-8') as f:
    html = f.read()

# Desktop Claws
import re
desktop_claw_re = re.compile(r'/\* Foreground Claws.*?\n\s*\.rooster-claw-top\s*\{[^}]*\}\s*\.rooster-claw-mid\s*\{[^}]*\}', re.DOTALL)

refined_desktop_claw = """    /* Foreground Claws (Layer 3 - Multi-Layer 3D Depth & Tight Contact Shadows) */
    .rooster-claw-top {
      position: absolute;
      left: 107px;
      top: -20px;
      width: 100px;
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
    html = desktop_claw_re.sub(refined_desktop_claw, html)
    print("4. Đã cập nhật Desktop CSS: .rooster-claw-top top: -20px")

# Media query @media (max-width: 1023px)
media_1023_claw_re = re.compile(r'@media\s*\(\s*max-width:\s*1023px\s*\)\s*\{.*?\.rooster-claw-top\s*\{[^}]*\}\s*\.rooster-claw-mid\s*\{[^}]*\}', re.DOTALL)
def replace_media_1023(match):
    text = match.group(0)
    # replace claws inside
    text = re.sub(r'\.rooster-claw-top\s*\{[^}]*\}', """.rooster-claw-top {
        left: 85px;
        top: -16px;
        width: 80px;
      }""", text)
    text = re.sub(r'\.rooster-claw-mid\s*\{[^}]*\}', """.rooster-claw-mid {
        left: -4px;
        top: 138px;
        width: 28px;
      }""", text)
    return text

html = media_1023_claw_re.sub(replace_media_1023, html)

with open(ORDER_HTML, 'w', encoding='utf-8') as f:
    f.write(html)
print("5. Đã lưu order.html thành công!")

# -------------------------------------------------------------
# 5. XUẤT ẢNH NGHIỆM THU CHỨNG MINH THỊ GIÁC (PROOF ARTIFACTS)
# -------------------------------------------------------------
print("Bắt đầu render composite nghiệm thu sau tinh chỉnh...")

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

# 1. Mascot body
m_w = 620
m_h = int(620 * mascot_final.height / mascot_final.width)
mascot_scaled = mascot_final.resize((m_w, m_h), Image.Resampling.LANCZOS)
proof.paste(mascot_scaled, (0, 15), mascot_scaled)

# 2. Clipboard
board_x, board_y = 260, 175
proof.paste(board_final, (board_x, board_y), board_final)

# 3. Claws with refined dy = -20px
ct_w = 100
ct_h = int(100 * claw_top_final.height / claw_top_final.width)
claw_top_scaled = claw_top_final.resize((ct_w, ct_h), Image.Resampling.LANCZOS)
proof.paste(claw_top_scaled, (board_x + 107, board_y - 20), claw_top_scaled)

cm_w = 35
cm_h = int(35 * claw_mid_final.height / claw_mid_final.width)
claw_mid_scaled = claw_mid_final.resize((cm_w, cm_h), Image.Resampling.LANCZOS)
proof.paste(claw_mid_scaled, (board_x - 5, board_y + 172), claw_mid_scaled)

# Export Full Proof
full_path = os.path.join(ARTIFACT_DIR, 'full_chicken_arms_menu_preview.png')
proof.save(full_path)

# Export Top Arm Closeup (Showing natural wing slope and firm wood grip)
top_arm_closeup = proof.crop((230, 60, 530, 260))
top_path = os.path.join(ARTIFACT_DIR, 'inspect_top_arm_anatomical_bridge.png')
top_arm_closeup.save(top_path)

# Export Mid Arm Closeup
mid_arm_closeup = proof.crop((190, 280, 340, 480))
mid_path = os.path.join(ARTIFACT_DIR, 'inspect_mid_arm_organic_grip.png')
mid_arm_closeup.save(mid_path)

print(f"-> Đã xuất ảnh cận cảnh cánh tay trên: {top_path}")
print(f"-> Đã xuất ảnh toàn cảnh: {full_path}")
print("=== HOÀN TẤT TINH CHỈNH THÀNH CÔNG ===")

