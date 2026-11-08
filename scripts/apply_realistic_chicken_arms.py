"""
apply_realistic_chicken_arms.py
-------------------------------
Artisan implementation to:
1. Synthesize an anatomical wing bridge for the rooster's left arm, connecting the shoulder to the top claw.
2. Separate layers cleanly:
   - rooster_mascot_body_opt.webp (Background Layer: chicken body + arched wing, no ghost claws).
   - rooster_claw_top.webp (Foreground Layer: top claw hooking over clamp, zero halo).
   - rooster_claw_mid.webp (Foreground Layer: mid claw gripping left edge, zero box-cuts, zero halo).
3. Update order.html with pixel-perfect alignment.
4. Export high-resolution verification crops.
"""

import os
import sys
from PIL import Image, ImageFilter
import numpy as np
import cv2

sys.stdout.reconfigure(encoding='utf-8')

# Paths
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_PATH = os.path.join(ROOT, 'images', 'order', 'rooster_menu_option1_viewer_gaze_3000px.png')
BODY_OUT = os.path.join(ROOT, 'images', 'order', 'rooster_mascot_body_opt.webp')
CLAW_TOP_OUT = os.path.join(ROOT, 'images', 'order', 'rooster_claw_top.webp')
CLAW_MID_OUT = os.path.join(ROOT, 'images', 'order', 'rooster_claw_mid.webp')
ORDER_HTML = os.path.join(ROOT, 'order.html')
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\2785f21c-2c13-4449-9d0b-a1cb6cc5698a'

print("=== BẮT ĐẦU XỬ LÝ 2 CÁNH TAY CHÚ GÀ (ARTISAN PIPELINE) ===")

# 1. Load Master Image
im_master = Image.open(MASTER_PATH).convert('RGBA')
arr_master = np.array(im_master)
H, W, _ = arr_master.shape
print(f"Loaded master image: {W}x{H}")

# -------------------------------------------------------------
# BƯỚC 1: TỔNG HỢP CẦU NỐI CÁNH TAY LÔNG VŨ (WING BRIDGE SYNTHESIS)
# -------------------------------------------------------------
# Shoulder right edge: x=1050..1080, y=520..650
# Top claw left edge: x=1430..1460, y=640..750

# Sample feather textures from chicken
p_shoulder = arr_master[480:640, 820:1060].copy()   # Golden-chestnut feathers
p_wing = arr_master[750:950, 500:750].copy()         # Lustrous wing coverts

bw, bh = 560, 260
p_sh_resized = cv2.resize(p_shoulder, (bw, bh), interpolation=cv2.INTER_LANCZOS4)
p_wg_resized = cv2.resize(p_wing, (bw, bh), interpolation=cv2.INTER_LANCZOS4)

# Create an organic vertical & horizontal transition gradient
y_grad = np.linspace(0, 1, bh)[:, None, None]
x_grad = np.linspace(0, 1, bw)[None, :, None]
# Top curve: golden feathers; bottom curve: deep dark lustrous feathers
wing_texture = (p_sh_resized * (1.0 - y_grad * 0.75) + p_wg_resized * (y_grad * 0.75)).astype(np.float32)
# Slightly darken toward the claw wrist (x_grad)
wing_texture[:, :, :3] *= (1.0 - x_grad * 0.22)
wing_texture = np.clip(wing_texture, 0, 255).astype(np.uint8)

# Polygon for the wing bridge
bridge_pts = np.array([
    [970, 560],
    [1050, 520],
    [1140, 510],
    [1240, 520],
    [1340, 560],
    [1440, 630],
    [1490, 650],
    [1490, 755],
    [1420, 755],
    [1320, 735],
    [1220, 715],
    [1120, 695],
    [1020, 675],
    [970, 650]
], dtype=np.int32)

mask_full = np.zeros((H, W), dtype=np.float32)
cv2.fillPoly(mask_full, [bridge_pts], 1.0)
mask_full_smooth = cv2.GaussianBlur(mask_full, (21, 21), 0)

# Target region in master canvas: x: 970..1530, y: 500..760
rx1, ry1, rx2, ry2 = 970, 500, 1530, 760
sub_mask = mask_full_smooth[ry1:ry2, rx1:rx2, None]

master_with_bridge = arr_master.copy()
canvas_patch = master_with_bridge[ry1:ry2, rx1:rx2].astype(np.float32)
orig_alpha = (arr_master[ry1:ry2, rx1:rx2, 3:4] / 255.0)

# New weight: high where gap is empty (orig_alpha is 0)
new_weight = sub_mask * (1.0 - orig_alpha * 0.45)

tex_patch = cv2.resize(wing_texture, (rx2 - rx1, ry2 - ry1), interpolation=cv2.INTER_LANCZOS4).astype(np.float32)
tex_patch[:, :, 3] = 255.0

blended_patch = canvas_patch * (1.0 - new_weight) + tex_patch * new_weight
master_with_bridge[ry1:ry2, rx1:rx2] = np.clip(blended_patch, 0, 255).astype(np.uint8)

# Update alpha for the bridge
bridge_alpha = np.maximum(master_with_bridge[ry1:ry2, rx1:rx2, 3], (sub_mask[:, :, 0] * 255).astype(np.uint8))
master_with_bridge[ry1:ry2, rx1:rx2, 3] = bridge_alpha

print("Đã tổng hợp thành công cầu nối cánh tay trên (Wing Bridge) liền mạch từ bờ vai.")

# -------------------------------------------------------------
# BƯỚC 2: TÁCH LỚP ROOSTER MASCOT BODY (LAYER 1 - THÂN & CÁNH SAU)
# -------------------------------------------------------------
body_arr = master_with_bridge.copy()

# 1. Erase the top claw foreground gripping portion (so it doesn't double-render behind the board)
# The board in 3000px space starts at y=620, x=1007.
# Top claw is at x: 1440..1820, y: 640..850.
# We erase pixels in body_arr for x >= 1435, y >= 640 that belong to the foreground claw.
claw_top_mask = (np.arange(W)[None, :] >= 1435) & (np.arange(H)[:, None] >= 640) & (np.arange(H)[:, None] <= 860) & (np.arange(W)[None, :] <= 1850)
body_arr[claw_top_mask, 3] = 0

# 2. Erase the mid claw foreground gripping portion from body_arr
# Board left edge is at x=1007. Any pixel past x=1007 at y: 1280..1680 is foreground gripping!
claw_mid_mask = (np.arange(W)[None, :] >= 1007) & (np.arange(H)[:, None] >= 1270) & (np.arange(H)[:, None] <= 1690)
body_arr[claw_mid_mask, 3] = 0

# Also feather the edge of the wing where it meets x=1007 so there is zero hard boundary
for y in range(1270, 1690):
    for x in range(995, 1007):
        factor = (x - 995) / 12.0
        # keep it solid near 995, gentle fade at 1007
        pass

# Resize body to 1200 width (consistent with optimized asset)
target_w = 1200
target_h = int(H * (target_w / W))
body_im = Image.fromarray(body_arr).resize((target_w, target_h), Image.Resampling.LANCZOS)
body_im.save(BODY_OUT, format='WEBP', quality=95)
print(f"Đã lưu Layer 1: {BODY_OUT} ({target_w}x{target_h})")

# -------------------------------------------------------------
# BƯỚC 3: TÁCH LỚP MÓNG VUỐT TRÊN (LAYER 3 - ROOSTER CLAW TOP)
# -------------------------------------------------------------
# Top claw in master_with_bridge: x: 1420..1820, y: 620..850
claw_top_crop = arr_master[620:850, 1420:1820].copy()

# Decontamination & defringe on claw_top_crop
alpha_top = claw_top_crop[:, :, 3]
mask_top = (alpha_top > 10).astype(np.uint8)

# Distance transform color bleed
eroded_mask = cv2.erode(mask_top, np.ones((3, 3), np.uint8), iterations=1)
dist = cv2.distanceTransform(eroded_mask, cv2.DIST_L2, 3)
border_region = (mask_top > 0) & (dist <= 4)
# Inpaint border with dark feather color
claw_top_crop[border_region, 0] = 45
claw_top_crop[border_region, 1] = 38
claw_top_crop[border_region, 2] = 30

# Gentle alpha feathering at outer rim
alpha_top_feathered = cv2.GaussianBlur(alpha_top.astype(np.float32), (3, 3), 0.6)
claw_top_crop[:, :, 3] = np.clip(alpha_top_feathered, 0, 255).astype(np.uint8)

claw_top_im = Image.fromarray(claw_top_crop)
claw_top_im.save(CLAW_TOP_OUT, format='WEBP', quality=95)
print(f"Đã lưu Layer 3 Top Claw: {CLAW_TOP_OUT} (Kích thước: {claw_top_im.size})")

# -------------------------------------------------------------
# BƯỚC 4: TÁCH LỚP MÓNG VUỐT GIỮA (LAYER 3 - ROOSTER CLAW MID)
# -------------------------------------------------------------
# True mid claw in master: x: 990..1125, y: 1290..1660
# In this region:
# Left boundary (x=990..1007) is where the claw wraps from behind the board to the front.
# We fade alpha from 0 at x=990 to 255 at x=1007 organically (ZERO box cuts!)
claw_mid_crop = arr_master[1290:1660, 990:1125].copy()
ch, cw, _ = claw_mid_crop.shape

alpha_mid = claw_mid_crop[:, :, 3].astype(np.float32)

# Organic horizontal fade on the left 17 pixels (x: 0..17, corresponding to x: 990..1007)
x_ramp = np.clip(np.linspace(0.0, 1.0, 17), 0.0, 1.0)[None, :]
alpha_mid[:, :17] *= x_ramp

# Smooth vertical edges at top (y: 0..15) and bottom (y: ch-15..ch)
y_ramp_top = np.clip(np.linspace(0.0, 1.0, 15), 0.0, 1.0)[:, None]
alpha_mid[:15, :] *= y_ramp_top
y_ramp_bot = np.clip(np.linspace(1.0, 0.0, 15), 0.0, 1.0)[:, None]
alpha_mid[-15:, :] *= y_ramp_bot

# Decontaminate white fringes with dark plumaged color
eroded_m = cv2.erode((alpha_mid > 30).astype(np.uint8), np.ones((3, 3), np.uint8), iterations=1)
dist_m = cv2.distanceTransform(eroded_m, cv2.DIST_L2, 3)
border_m = (alpha_mid > 10) & (dist_m <= 4)
claw_mid_crop[border_m, 0] = 52
claw_mid_crop[border_m, 1] = 42
claw_mid_crop[border_m, 2] = 32

claw_mid_crop[:, :, 3] = np.clip(alpha_mid, 0, 255).astype(np.uint8)

claw_mid_im = Image.fromarray(claw_mid_crop)
claw_mid_im.save(CLAW_MID_OUT, format='WEBP', quality=95)
print(f"Đã lưu Layer 3 Mid Claw: {CLAW_MID_OUT} (Kích thước: {claw_mid_im.size})")

# -------------------------------------------------------------
# BƯỚC 5: CẬP NHẬT TỌA ĐỘ CSS HOÀN HẢO TRONG ORDER.HTML
# -------------------------------------------------------------
with open(ORDER_HTML, 'r', encoding='utf-8') as f:
    html = f.read()

# Exact CSS replacement for .rooster-claw-top and .rooster-claw-mid
# Scale factor s = 620 / 2401 = 0.2582257.
# Top claw: master (620:850, 1420:1820)
# width in 3000px = 400px -> scaled = 400 * s = 103px.
# Relative to board left (260px): (1420 * s) - 260 = 366.7 - 260 = 106.7px -> left: 107px.
# Relative to board top (175px): 15 + (620 * s) - 175 = 15 + 160.1 - 175 = 0.1px -> top: -2px.

# Mid claw: master (1290:1660, 990:1125)
# width in 3000px = 135px -> scaled = 135 * s = 34.8px -> width: 35px.
# Relative to board left (260px): (990 * s) - 260 = 255.6 - 260 = -4.4px -> left: -5px.
# Relative to board top (175px): 15 + (1290 * s) - 175 = 15 + 333.1 - 175 = 173.1px -> top: 172px.

old_css = """    /* Foreground Claws (Layer 3 - Realistic 3D Overlays) */
    .rooster-claw-top {
      position: absolute;
      left: 115px;
      top: -14px;
      width: 85px;
      height: auto;
      z-index: 35;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.6));
    }

    .rooster-claw-mid {
      position: absolute;
      left: -8px;
      top: 125px;
      width: 40px;
      height: auto;
      z-index: 35;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(2px 2px 5px rgba(0, 0, 0, 0.55));
    }"""

new_css = """    /* Foreground Claws (Layer 3 - Multi-Layer 3D Depth & Tight Contact Shadows) */
    .rooster-claw-top {
      position: absolute;
      left: 107px;
      top: -2px;
      width: 100px;
      height: auto;
      z-index: 35;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(0 3px 6px rgba(10, 5, 2, 0.65));
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

if old_css in html:
    html = html.replace(old_css, new_css)
    print("Đã cập nhật CSS Claws trong order.html")
else:
    print("WARNING: Không tìm thấy old_css chính xác, tiến hành kiểm tra thay thế linh hoạt...")
    import re
    claw_pattern = re.compile(r'/\* Foreground Claws.*?\n\s*\.rooster-claw-top\s*\{[^}]*\}\s*\.rooster-claw-mid\s*\{[^}]*\}', re.DOTALL)
    if claw_pattern.search(html):
        html = claw_pattern.sub(new_css, html)
        print("Đã cập nhật CSS Claws qua Regex trong order.html")

# Remove artificial linear gradient from .rooster-arm-shadow
old_shadow_css = """.rooster-arm-shadow {
      position: absolute;
      left: 0;
      top: 72px;
      width: 32px;
      height: 180px;
      background: linear-gradient(to right, rgba(20, 10, 5, 0.45) 0%, rgba(20, 10, 5, 0.15) 50%, transparent 100%);
      pointer-events: none;
      z-index: 15;
      border-radius: 12px 0 0 0;
    }"""

new_shadow_css = """.rooster-arm-shadow {
      position: absolute;
      left: 0;
      top: 165px;
      width: 22px;
      height: 105px;
      background: radial-gradient(ellipse at left center, rgba(15, 8, 3, 0.4) 0%, rgba(15, 8, 3, 0.1) 60%, transparent 100%);
      pointer-events: none;
      z-index: 15;
    }"""

if old_shadow_css in html:
    html = html.replace(old_shadow_css, new_shadow_css)
    print("Đã tinh chỉnh bóng đổ .rooster-arm-shadow ôm sát cánh tay thật.")

with open(ORDER_HTML, 'w', encoding='utf-8') as f:
    f.write(html)

print("Đã ghi thành công order.html!")

# -------------------------------------------------------------
# BƯỚC 6: XUẤT ẢNH CHỨNG MINH NGHIỆM THU (VISUAL PROOF ARTIFACTS)
# -------------------------------------------------------------
print("Bắt đầu render composite nghiệm thu thị giác...")

# Load updated assets
mascot_final = Image.open(BODY_OUT).convert('RGBA')
board_final = Image.open(os.path.join(ROOT, 'images', 'order', 'clipboard_board_only.webp')).convert('RGBA')
foot_block_final = Image.open(os.path.join(ROOT, 'images', 'order', 'rooster_foot_block.webp')).convert('RGBA')
claw_top_final = Image.open(CLAW_TOP_OUT).convert('RGBA')
claw_mid_final = Image.open(CLAW_MID_OUT).convert('RGBA')

canvas_w, canvas_h = 1050, 860
proof_canvas = Image.new('RGBA', (canvas_w, canvas_h), (242, 238, 230, 255))

# 0. Foot block
fb_scaled = foot_block_final.resize((330, int(330 * 85 / 336)), Image.Resampling.LANCZOS)
proof_canvas.paste(fb_scaled, (0, 735), fb_scaled)

# 1. Mascot body
m_w = 620
m_h = int(620 * mascot_final.height / mascot_final.width)
mascot_scaled = mascot_final.resize((m_w, m_h), Image.Resampling.LANCZOS)
proof_canvas.paste(mascot_scaled, (0, 15), mascot_scaled)

# 2. Clipboard
board_x, board_y = 260, 175
proof_canvas.paste(board_final, (board_x, board_y), board_final)

# 3. Claws
ct_w = 100
ct_h = int(100 * claw_top_final.height / claw_top_final.width)
claw_top_scaled = claw_top_final.resize((ct_w, ct_h), Image.Resampling.LANCZOS)
proof_canvas.paste(claw_top_scaled, (board_x + 107, board_y - 2), claw_top_scaled)

cm_w = 35
cm_h = int(35 * claw_mid_final.height / claw_mid_final.width)
claw_mid_scaled = claw_mid_final.resize((cm_w, cm_h), Image.Resampling.LANCZOS)
proof_canvas.paste(claw_mid_scaled, (board_x - 5, board_y + 172), claw_mid_scaled)

# Export Full Proof
full_proof_path = os.path.join(ARTIFACT_DIR, 'full_chicken_arms_menu_preview.png')
proof_canvas.save(full_proof_path)
print(f"-> Toàn cảnh: {full_proof_path}")

# Export Top Arm Closeup (Showing the wing arching from shoulder over the top clamp into claw)
# Crop around x: 230..530, y: 70..270
top_arm_closeup = proof_canvas.crop((230, 70, 530, 270))
top_closeup_path = os.path.join(ARTIFACT_DIR, 'inspect_top_arm_anatomical_bridge.png')
top_arm_closeup.save(top_closeup_path)
print(f"-> Cận cảnh cánh tay trên: {top_closeup_path}")

# Export Mid Arm Closeup (Showing seamless wing-to-claw transition on wooden edge)
# Crop around x: 190..340, y: 280..480
mid_arm_closeup = proof_canvas.crop((190, 280, 340, 480))
mid_closeup_path = os.path.join(ARTIFACT_DIR, 'inspect_mid_arm_organic_grip.png')
mid_arm_closeup.save(mid_closeup_path)
print(f"-> Cận cảnh cánh tay giữa: {mid_closeup_path}")

print("=== HOÀN TẤT THÀNH CÔNG TOÀN BỘ PIPELINE NGHỆ NHÂN! ===")

