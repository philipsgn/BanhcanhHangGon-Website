import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the definitive, clean, modern Menu CSS block
new_menu_css = """/* ==========================================================================
   SECTION 4: MENU (PANORAMA 5 MÓN & BIỂN GÀ NGHỆ THUẬT - LOGICAL BODY FLOW)
   Zero Ceiling Collision: Stage anchored in Section Body with >= 60px Clearance
   Normalized 740px Trays | Clean Modern Typography | Full Mobile Support
   ========================================================================== */
    #menu {
      position: relative;
      min-height: 100vh;
      min-height: 100svh;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      background-color: #FAF8F5;
      background-image:
        radial-gradient(circle at 12% 18%, rgba(201, 154, 74, 0.06) 0%, transparent 40%),
        radial-gradient(circle at 88% 82%, rgba(181, 118, 42, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.6) 0%, transparent 100%);
      color: #1A1410;
      overflow: visible;
      isolation: isolate;
      padding: clamp(24px, 3.8vh, 40px) clamp(16px, 2.5vw, 40px) clamp(14px, 2vh, 22px);
    }

    .menu-decor-pattern {
      position: absolute;
      left: 0;
      top: 15%;
      width: clamp(60px, 8vw, 130px);
      height: 70%;
      background-repeat: repeat-y;
      background-size: 100% auto;
      background-image: url("data:image/svg+xml,%3Csvg width='80' height='160' viewBox='0 0 80 160' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 40L40 0L80 40L40 80L0 40Z' fill='%23C99A4A' fill-opacity='0.08'/%3E%3Cpath d='M0 120L40 80L80 120L40 160L0 120Z' fill='%23C99A4A' fill-opacity='0.08'/%3E%3Ccircle cx='40' cy='40' r='10' fill='%23C99A4A' fill-opacity='0.06'/%3E%3Ccircle cx='40' cy='120' r='10' fill='%23C99A4A' fill-opacity='0.06'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 0;
      opacity: 0.85;
    }

    /* Biển gà nghệ thuật nguyên bản: Treo góc trái, dây thừng cách trần an toàn */
    .menu-hero-header {
      position: absolute;
      top: clamp(12px, 1.8vh, 22px);
      left: clamp(16px, 3.5vw, 48px);
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      width: auto;
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      z-index: 10;
      pointer-events: none;
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      position: relative;
      margin: 0;
      width: auto;
      pointer-events: auto;
    }

    .menu-rooster-img {
      width: clamp(110px, 11vw, 145px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 10px 20px rgba(45, 26, 18, 0.14));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.02) translateY(-2px);
    }

    /* SÂN KHẤU PANORAMA: NẰM HOÀN TOÀN TRONG BODY SECTION, CÁCH TRẦN >= 60PX */
    .menu-stage-wrapper {
      position: relative;
      max-width: 1280px;
      flex: 1;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: clamp(16px, 2.5vh, 32px) auto 0;
      z-index: 2;
    }

    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: clamp(325px, 46vh, 395px);
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1200px;
      margin: 0;
      cursor: grab;
      user-select: none;
    }

    .menu-carousel-track:active {
      cursor: grabbing;
    }

    /* Thẻ Card: Neo chuẩn tại top: 50%, left: 50%, không dùng margin âm trôi nổi */
    .menu-card {
      position: absolute;
      top: 50%;
      left: 50%;
      width: clamp(215px, 20vw, 260px);
      padding: 10px 16px 18px;
      border-radius: 22px;
      border: none;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1),
                  opacity 0.45s ease,
                  background-color 0.45s ease,
                  box-shadow 0.5s ease;
      will-change: transform, opacity;
      cursor: pointer;
    }

    /* Mâm Món Ăn: Nằm tự nhiên trong thẻ, không tràn ra ngoài trần section */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 0;
      margin-bottom: clamp(6px, 1vh, 12px);
      z-index: 3;
    }

    .menu-card-plate {
      width: clamp(110px, 15vh, 140px);
      height: clamp(110px, 15vh, 140px);
      aspect-ratio: 1 / 1;
      object-fit: contain;
      filter: drop-shadow(0 8px 16px rgba(36, 22, 16, 0.16));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-card:not(.is-active) .menu-card-plate {
      transform: none !important;
    }

    .menu-card.is-active .menu-card-plate {
      transform: scale(1.02);
      filter: drop-shadow(0 12px 22px rgba(36, 22, 16, 0.22));
    }

    /* Thân thẻ: Typography chuẩn mực, không bị che lấp */
    .menu-card-body {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      padding-top: 2px;
    }

    .menu-card-title {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(13px, 1.12vw, 15.5px);
      font-weight: 800;
      letter-spacing: 0.02em;
      margin: 0 0 4px;
      text-transform: uppercase;
      line-height: 1.25;
      color: #1A1410;
      transition: color 0.35s ease;
    }

    .menu-card-price {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(17px, 1.45vw, 19.5px);
      font-weight: 900;
      margin: 0 0 5px;
      letter-spacing: 0.03em;
      color: #8A4A1C;
      transition: color 0.35s ease;
    }

    .menu-card-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(10px, 0.82vw, 11.5px);
      line-height: 1.38;
      font-weight: 300;
      margin: 0 0 10px;
      max-width: 230px;
      color: #4A3C33;
      transition: opacity 0.35s ease, color 0.35s ease;
    }

    .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(11px, 0.9vw, 12px);
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      text-decoration: none;
      border-radius: 999px;
      width: clamp(140px, 14vw, 165px);
      height: 34px;
      transition: all 0.35s cubic-bezier(0.25, 1, 0.5, 1);
    }

    /* Card Active: Nổi bật, sang trọng, tương phản cao */
    .menu-card.is-active {
      background: #EFE8DD;
      color: #1A1410;
      border: none !important;
      transform: translate3d(-50%, -50%, 40px) scale(1);
      opacity: 1;
      z-index: 6;
      box-shadow: 0 20px 45px rgba(36, 22, 16, 0.12);
      cursor: default;
    }

    .menu-card.is-active .menu-card-title {
      color: #1A1410;
    }

    .menu-card.is-active .menu-card-price {
      color: #8A4A1C;
    }

    .menu-card.is-active .menu-card-desc {
      color: #4A3C33;
      opacity: 1;
    }

    .menu-card.is-active .menu-card-cta {
      background: #9E5E2B;
      color: #FFFFFF;
      box-shadow: 0 6px 16px rgba(158, 94, 43, 0.28);
      opacity: 1;
      pointer-events: auto;
    }

    .menu-card.is-active .menu-card-cta:hover {
      background: #B56E35;
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(158, 94, 43, 0.38);
    }

    /* 4 Thẻ Phụ: Mờ nhẹ, tạo chiều sâu thị giác */
    .menu-card:not(.is-active) {
      background: #FAF7F2;
      border: none !important;
    }

    .menu-card:not(.is-active) .menu-card-title {
      color: #33241C;
    }

    .menu-card:not(.is-active) .menu-card-price {
      color: #9E5E2B;
    }

    .menu-card:not(.is-active) .menu-card-desc {
      color: #6A584D;
      opacity: 0.8;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .menu-card:not(.is-active) .menu-card-cta {
      background: transparent;
      color: #9E5E2B;
      border: 1px solid #C48E59;
      padding: 6px 16px;
      font-size: 11px;
      opacity: 0.85;
    }

    .menu-card:not(.is-active) .menu-card-cta:hover {
      background: #9E5E2B;
      color: #FFFFFF;
      border-color: #9E5E2B;
    }

    /* 3D Transform Positions */
    .menu-card.is-near-prev {
      transform: translate3d(calc(-50% - 92%), calc(-50% + 10px), -40px) scale(0.85);
      opacity: 0.65;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.06);
    }

    .menu-card.is-near-next {
      transform: translate3d(calc(-50% + 92%), calc(-50% + 10px), -40px) scale(0.85);
      opacity: 0.65;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.06);
    }

    .menu-card.is-far-prev {
      transform: translate3d(calc(-50% - 176%), calc(-50% + 20px), -90px) scale(0.72);
      opacity: 0.35;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.04);
    }

    .menu-card.is-far-next {
      transform: translate3d(calc(-50% + 176%), calc(-50% + 20px), -90px) scale(0.72);
      opacity: 0.35;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.04);
    }

    .menu-card.is-hidden {
      opacity: 0;
      transform: translate3d(-50%, calc(-50% + 30px), -140px) scale(0.65);
      pointer-events: none;
      z-index: 1;
    }

    /* Chấm chuyển trang (Pagination Dots) */
    .menu-dots {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      margin: clamp(6px, 1vh, 12px) auto clamp(8px, 1.2vh, 14px);
      z-index: 5;
    }

    .menu-dot {
      width: 7px;
      height: 7px;
      border-radius: 999px;
      background: #D8CEBE;
      border: none;
      padding: 0;
      cursor: pointer;
      transition: all 0.35s ease;
    }

    .menu-dot:hover {
      background: #B56E35;
      transform: scale(1.2);
    }

    .menu-dot.is-active {
      width: 22px;
      background: #9E5E2B;
      box-shadow: 0 2px 8px rgba(158, 94, 43, 0.35);
    }

    /* Menu Footer Bar */
    .menu-footer-bar {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: clamp(16px, 3vw, 40px);
      width: 100%;
      max-width: 680px;
      padding: clamp(6px, 1vh, 10px) clamp(16px, 2.5vw, 28px);
      background: #FAF7F2;
      border: 1px solid rgba(201, 154, 74, 0.22);
      border-radius: 999px;
      box-sizing: border-box;
      box-shadow: 0 6px 18px rgba(45, 26, 18, 0.04);
      margin: 2px auto 0;
      z-index: 4;
    }

    .menu-footer-contact {
      display: flex;
      align-items: baseline;
      gap: 12px;
      flex-wrap: wrap;
    }

    .menu-footer-tagline {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #7A6658;
    }

    .menu-footer-phone {
      font-size: clamp(13px, 1.1vw, 15px);
      font-weight: 800;
      color: #8A4A1C;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: color 0.2s ease;
    }

    .menu-footer-phone:hover {
      color: #6B3410;
    }

    .menu-footer-hours {
      font-size: 11px;
      color: #8C7B70;
      border-left: 1px solid rgba(201, 154, 74, 0.3);
      padding-left: 12px;
    }

    .menu-view-all-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 7px 18px;
      background: #1A1410;
      color: #FAF8F5;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      border-radius: 999px;
      transition: all 0.3s ease;
      white-space: nowrap;
    }

    .menu-view-all-btn:hover {
      background: #8A4A1C;
      transform: translateY(-1px);
    }

    /* ==========================================================================
       RESPONSIVE & MOBILE ADAPTATION
       ========================================================================== */
    @media (max-width: 1024px) {
      .menu-hero-header {
        left: clamp(10px, 2vw, 20px);
      }
      .menu-rooster-img {
        width: clamp(95px, 10vw, 120px);
      }
      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 80%), calc(-50% + 10px), -40px) scale(0.82) !important;
      }
      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 80%), calc(-50% + 10px), -40px) scale(0.82) !important;
      }
      .menu-card.is-far-prev {
        transform: translate3d(calc(-50% - 150%), calc(-50% + 20px), -80px) scale(0.68) !important;
      }
      .menu-card.is-far-next {
        transform: translate3d(calc(-50% + 150%), calc(-50% + 20px), -80px) scale(0.68) !important;
      }
    }

    @media (max-width: 600px) {
      #menu {
        min-height: 100vh;
        min-height: 100svh;
        padding: clamp(10px, 1.5vh, 16px) 12px clamp(12px, 1.8vh, 18px);
        overflow: visible;
      }

      .menu-hero-header {
        position: absolute;
        top: 10px;
        left: 12px;
        margin: 0;
        padding: 0;
        z-index: 6;
      }

      .menu-rooster-img {
        width: clamp(80px, 20vw, 95px);
      }

      .menu-stage-wrapper {
        margin-top: clamp(48px, 7vh, 64px);
      }

      .menu-carousel-track {
        height: clamp(335px, 48vh, 375px);
      }

      .menu-card {
        width: 78vw;
        max-width: 260px;
        padding: 10px 14px 16px;
      }

      .menu-card.is-active {
        transform: translate3d(-50%, -50%, 40px) scale(1) !important;
      }

      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 68%), calc(-50% + 8px), -40px) scale(0.78) !important;
        opacity: 0.35;
      }

      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 68%), calc(-50% + 8px), -40px) scale(0.78) !important;
        opacity: 0.35;
      }

      .menu-card.is-far-prev,
      .menu-card.is-far-next {
        opacity: 0;
        pointer-events: none;
      }

      .menu-footer-bar {
        border-radius: 16px;
        padding: 10px 14px;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        text-align: center;
      }

      .menu-footer-contact {
        justify-content: center;
        gap: 8px;
      }

      .menu-footer-hours {
        border-left: none;
        padding-left: 0;
        width: 100%;
        text-align: center;
      }

      .menu-view-all-btn {
        width: 100%;
        justify-content: center;
        min-height: 44px;
      }
    }"""

# Replace the existing Section 4 Menu CSS block in index.html
start_marker = "/* ==========================================================================\n   SECTION 4: MENU"
if start_marker not in html:
    start_marker = "/* SECTION 4: MENU"
if start_marker not in html:
    # Look for #menu {
    m_start = html.find("#menu {")
    # find comment preceding it
    m_comment = html.rfind("/*", 0, m_start)
    start_pos = m_comment if m_comment != -1 else m_start
else:
    start_pos = html.find(start_marker)

# Find the end of this CSS block (before SECTION 5 or </style>)
end_marker = "/* ==========================================================================\n   SECTION 5"
if end_marker not in html:
    end_marker = "/* SECTION 5"
if end_marker not in html:
    end_marker = "</style>"

end_pos = html.find(end_marker, start_pos)
if end_pos == -1:
    end_pos = html.find("</style>", start_pos)

print(f"Found Menu CSS block from {start_pos} to {end_pos} (length {end_pos-start_pos})")

# Replace
updated_html = html[:start_pos] + new_menu_css.strip() + "\n\n    " + html[end_pos:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print("Applied clean logical body architecture to index.html successfully!")
