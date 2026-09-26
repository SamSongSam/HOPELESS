#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN MEGASTRUCTURE - 6-TIER SPATIAL ZONING & 4 URBAN TYPOLOGIES MAP
================================================================================
Generates a 1920x1080 Sci-Fi Master Urban Architecture Poster:
- 6-Tier Spatial Rings: DIST_CORE, DIST_PETAL_BASE, DIST_PETAL_MID, DIST_PETAL_TIP,
  DIST_STEM_COLUMN, and DIST_ROOT_ANCHOR
- 4 Core Urban Typology Overlays:
  1. ลานกิจกรรม (Activity Plazas, Open-Air Fora & Arenas)
  2. ที่อยู่อาศัย (Residential Housing, Scholar Dorms & Living Quarters)
  3. พื้นที่ทดลอง (Experimental Proving Grounds & Extreme Simulation Labs)
  4. พื้นที่สาธารณะ (Public Spaces, Waterfront Esplanades & Bio-Parks)
- 8 Academic Faculty Petals spatial programming & density falloff curves
================================================================================
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_JPG = os.path.join(WORKSPACE_DIR, "08_PRESENTATION", "ISTRORIGAN_ZONING_URBAN_MAP.jpg")
OUTPUT_PNG = os.path.join(WORKSPACE_DIR, "08_PRESENTATION", "ISTRORIGAN_ZONING_URBAN_MAP.png")
OUTPUT_ROOT_JPG = os.path.join(WORKSPACE_DIR, "ISTRORIGAN_ZONING_URBAN_MAP.jpg")


def generate_zoning_map():
    w, h = 1920, 1080
    img = Image.new("RGBA", (w, h), (7, 11, 20, 255))
    draw = ImageDraw.Draw(img)

    # Grid background
    grid_col = (18, 30, 50, 130)
    for x in range(0, w, 40):
        draw.line([(x, 0), (x, h)], fill=grid_col, width=1)
    for y in range(0, h, 40):
        draw.line([(0, y), (w, y)], fill=grid_col, width=1)

    # Fonts
    font_bold_path = "C:/Windows/Fonts/tahomabd.ttf" if os.path.exists("C:/Windows/Fonts/tahomabd.ttf") else "C:/Windows/Fonts/arialbd.ttf"
    font_reg_path = "C:/Windows/Fonts/tahoma.ttf" if os.path.exists("C:/Windows/Fonts/tahoma.ttf") else "C:/Windows/Fonts/arial.ttf"

    f_title = ImageFont.truetype(font_bold_path, 23)
    f_sub = ImageFont.truetype(font_reg_path, 12)
    f_sec = ImageFont.truetype(font_bold_path, 13)
    f_body = ImageFont.truetype(font_reg_path, 11)
    f_bold = ImageFont.truetype(font_bold_path, 11)
    f_small = ImageFont.truetype(font_reg_path, 9)
    f_badge = ImageFont.truetype(font_bold_path, 10)

    # HEADER BANNER
    draw.rectangle([0, 0, w, 70], fill=(5, 14, 26, 245))
    draw.line([(0, 70), (w, 70)], fill=(0, 210, 255, 220), width=2)
    draw.text((35, 12), "ISTRORIGAN (อิสโตรริแกน) — 6-TIER SPATIAL ZONING & 4 URBAN TYPOLOGIES MAP", font=f_title, fill=(240, 250, 255))
    draw.text((35, 45), "ERA: 4205 | 3,000M DIAMETER | 6 SPATIAL TIERS | 8 PETAL FACULTIES | 125,000 CITIZENS & RESEARCHERS", font=f_sub, fill=(0, 210, 240))
    draw.text((w - 440, 16), "DISTRICT MASTER PLAN & CIVIC PROGRAMMING", font=f_sec, fill=(255, 200, 60))
    draw.text((w - 440, 36), "PLAZAS • RESIDENTIAL • EXPERIMENTAL • PUBLIC SPACES", font=f_small, fill=(0, 255, 180))

    # FOOTER BANNER
    draw.rectangle([0, h - 55, w, h], fill=(5, 14, 26, 245))
    draw.line([(0, h - 55), (w, h - 55)], fill=(0, 210, 255, 180), width=1)
    footer_cols = [
        ("1. ลานกิจกรรม (PLAZAS)", "Grand Solar Agora (60k) | 8 Amphitheaters (3.5k) | Water Stages"),
        ("2. ที่อยู่อาศัย (RESIDENTIAL)", "Stepped Terraces (350u/blk) | Biosphere Pods | 125,000 Residents"),
        ("3. พื้นที่ทดลอง (EXPERIMENT)", "Hyperbaric 1,500 Bar Tanks | 300m Wave Flumes | Cyclone Domes"),
        ("4. พื้นที่สาธารณะ (PUBLIC)", "12 km Lotus Esplanade | Glazed Skywalks | 17-State Bazaar Pods")
    ]
    for i, (title_str, val_str) in enumerate(footer_cols):
        cx = 35 + i * 460
        draw.text((cx, h - 45), title_str, font=f_bold, fill=(0, 225, 255))
        draw.text((cx, h - 25), val_str, font=f_small, fill=(190, 215, 235))

    # LEFT/CENTER AREA: Polar District Zoning Plan (3,000m Diameter)
    cx = 580
    cy = 530
    max_r = 390

    # Draw ocean backdrop
    draw.ellipse([cx - max_r - 20, cy - max_r - 20, cx + max_r + 20, cy + max_r + 20], fill=(8, 16, 28, 255), outline=(0, 150, 200, 80), width=1)

    # 6 Radial Tiers filled/outlined
    # Tier 3: DIST_PETAL_TIP (R=750 to 1100m)
    draw.ellipse([cx - max_r, cy - max_r, cx + max_r, cy + max_r], fill=(12, 28, 48, 120), outline=(0, 210, 255, 150), width=2)
    # Tier 2: DIST_PETAL_MID (R=350 to 750m)
    r_mid = int(max_r * (750 / 1100))
    draw.ellipse([cx - r_mid, cy - r_mid, cx + r_mid, cy + r_mid], fill=(16, 36, 62, 160), outline=(0, 255, 200, 150), width=2)
    # Tier 1: DIST_PETAL_BASE (R=150 to 350m)
    r_base = int(max_r * (350 / 1100))
    draw.ellipse([cx - r_base, cy - r_base, cx + r_base, cy + r_base], fill=(22, 48, 80, 200), outline=(255, 200, 50, 180), width=2)
    # Tier 0: DIST_CORE (R=0 to 150m)
    r_core = int(max_r * (150 / 1100))
    draw.ellipse([cx - r_core, cy - r_core, cx + r_core, cy + r_core], fill=(45, 75, 120, 240), outline=(255, 255, 255, 255), width=3)

    # Draw 8 Petal Sectors & Radial Divisions
    petals = [
        {"deg": 0,   "code": "P0", "name": "Oceanic Power",      "color": (50, 140, 255)},
        {"deg": 45,  "code": "P1", "name": "Biosphere Marine",  "color": (50, 230, 120)},
        {"deg": 90,  "code": "P2", "name": "Climate Defense",   "color": (140, 220, 255)},
        {"deg": 135, "code": "P3", "name": "Megastructure Civ", "color": (255, 140, 50)},
        {"deg": 180, "code": "P4", "name": "Universal Library", "color": (200, 110, 255)},
        {"deg": 225, "code": "P5", "name": "Abyssal Mining",    "color": (255, 215, 50)},
        {"deg": 270, "code": "P6", "name": "17-State Assembly", "color": (255, 190, 0)},
        {"deg": 315, "code": "P7", "name": "Oceanic Medicine",  "color": (255, 70, 100)}
    ]

    # Draw 45m Waterways between petals
    for i in range(8):
        c_deg = i * 45 + 22.5
        c_rad = math.radians(c_deg)
        x2 = cx + int((max_r + 15) * math.cos(c_rad))
        y2 = cy + int((max_r + 15) * math.sin(c_rad))
        draw.line([(cx, cy), (x2, y2)], fill=(0, 210, 255, 160), width=3)

    # Plot 4 Urban Typology Markers across each petal
    # Marker symbols: [A] Plaza (Gold), [R] Housing (Coral), [T] Test Lab (Green), [P] Public Park (Cyan)
    for p in petals:
        deg = p["deg"]
        rad = math.radians(deg)

        # 1. Activity Plaza marker [A] in Petal Mid (R=380m)
        r_a = int(max_r * (480 / 1100))
        ax = cx + int(r_a * math.cos(rad - 0.12))
        ay = cy + int(r_a * math.sin(rad - 0.12))
        draw.rectangle([ax - 9, ay - 9, ax + 9, ay + 9], fill=(255, 185, 30, 240), outline=(255, 255, 255), width=1)
        draw.text((ax - 4, ay - 6), "A", font=f_badge, fill=(10, 20, 30))

        # 2. Residential Housing marker [R] in Petal Mid (R=550m)
        r_r = int(max_r * (620 / 1100))
        rx_pos = cx + int(r_r * math.cos(rad + 0.10))
        ry_pos = cy + int(r_r * math.sin(rad + 0.10))
        draw.rectangle([rx_pos - 9, ry_pos - 9, rx_pos + 9, ry_pos + 9], fill=(255, 90, 80, 240), outline=(255, 255, 255), width=1)
        draw.text((rx_pos - 4, ry_pos - 6), "R", font=f_badge, fill=(255, 255, 255))

        # 3. Experimental Testing marker [T] in Petal Tip (R=920m)
        r_t = int(max_r * (900 / 1100))
        tx = cx + int(r_t * math.cos(rad - 0.08))
        ty = cy + int(r_t * math.sin(rad - 0.08))
        draw.rectangle([tx - 9, ty - 9, tx + 9, ty + 9], fill=(40, 240, 140, 240), outline=(255, 255, 255), width=1)
        draw.text((tx - 4, ty - 6), "T", font=f_badge, fill=(10, 20, 30))

        # 4. Public Esplanade & Pier marker [P] in Outer Tip
        r_p = int(max_r * (1020 / 1100))
        px = cx + int(r_p * math.cos(rad + 0.08))
        py = cy + int(r_p * math.sin(rad + 0.08))
        draw.rectangle([px - 9, py - 9, px + 9, py + 9], fill=(0, 220, 255, 240), outline=(255, 255, 255), width=1)
        draw.text((px - 4, py - 6), "P", font=f_badge, fill=(10, 20, 30))

        # Petal Tag Badge
        bx = cx + int((max_r + 42) * math.cos(rad))
        by = cy + int((max_r + 42) * math.sin(rad))
        draw.rectangle([bx - 36, by - 12, bx + 36, by + 12], fill=(10, 24, 42, 240), outline=p["color"], width=2)
        draw.text((bx - 16, by - 8), p["code"], font=f_bold, fill=p["color"])

    # Center Grand Solar Agora callout in Core
    draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], fill=(255, 215, 0, 255), outline=(255, 255, 255), width=2)
    draw.text((cx - 4, cy - 7), "A", font=f_badge, fill=(10, 20, 30))
    draw.text((cx - 45, cy + 22), "DIST_CORE", font=f_bold, fill=(255, 255, 255))
    draw.text((cx - 65, cy + 36), "Grand Solar Agora (60k)", font=f_small, fill=(255, 215, 0))

    # Ring Tier Callout Badges on Left
    tier_callouts = [
        ("TIER 0: DIST_CORE (R=0-150m)", cx - r_core, cy - 25, (255, 255, 255)),
        ("TIER 1: DIST_PETAL_BASE (R=150-350m)", cx - r_base, cy - 70, (255, 200, 50)),
        ("TIER 2: DIST_PETAL_MID (R=350-750m)", cx - r_mid, cy - 120, (0, 255, 200)),
        ("TIER 3: DIST_PETAL_TIP (R=750-1100m)", cx - max_r, cy - 170, (0, 210, 255))
    ]
    for t_title, tx, ty, col in tier_callouts:
        draw.line([(tx, ty), (tx - 40, ty)], fill=col, width=1)
        draw.rectangle([tx - 240, ty - 12, tx - 40, ty + 12], fill=(10, 22, 38, 220), outline=col, width=1)
        draw.text((tx - 232, ty - 6), t_title, font=f_small, fill=col)

    # Subsurface Tier Badges (Tier -1 and Tier -2) in box on bottom-left
    draw.rectangle([35, h - 230, 280, h - 75], fill=(10, 20, 35, 220), outline=(0, 180, 230, 120), width=1)
    draw.text((45, h - 220), "SUBSURFACE ZONING TIERS", font=f_bold, fill=(255, 200, 60))
    draw.text((45, h - 200), "• TIER -1: DIST_STEM_COLUMN\n  Depth: 0m to -900m | R=80-350m\n  Ballast Tanks, Hyperbaric Labs, Bunks\n• TIER -2: DIST_ROOT_ANCHOR\n  Depth: -1,000m Seabed | R=0-250m\n  Doomsday Vault, Bedrock Claws", font=f_small, fill=(200, 225, 240))

    # RIGHT AREA: 4 Detailed Urban Typology Panels
    panel_x = 1140
    panel_y = 90
    panel_w = 745
    card_h = 215

    typologies = [
        {
            "id": "[A]",
            "title": "1. ลานกิจกรรมและเวทีกลางแจ้ง (ACTIVITY PLAZAS & EVENT GROUNDS)",
            "col": (255, 185, 30),
            "items": [
                ("Grand Solar Agora", "Citadel Plaza +120m (R=150m) | จุ 60,000 คน | พิธีเปิดภาคเรียน & วันครีษมายัน"),
                ("8 Faculty Amphitheaters", "อัฒจันทร์หินอ่อนรูปเกือกม้า (3,500 ที่นั่ง/คณะ รวม 28,000 ที่นั่ง) ระบบเสียงธรรมชาติ"),
                ("Inter-Petal Water Stages", "เวทีลอยน้ำไฮดรอลิกในร่องน้ำ 45m จัดแสดงละครโอเปร่าและคอนเสิร์ตแสงสีเสียงข้ามกลีบ"),
                ("Campus Maker Quads", "ลานนิทรรศการสิ่งประดิษฐ์กลางแจ้ง การแข่งหุ่นยนต์กู้ภัยทางทะเล และสนามแข่งโดรน")
            ]
        },
        {
            "id": "[R]",
            "title": "2. ระบบที่อยู่อาศัยและชุมชนเมือง (RESIDENTIAL HOUSING - 125,000 POP)",
            "col": (255, 90, 80),
            "items": [
                ("Stepped-Terrace Scholar Blocks", "โมดูล 12x24m สูง 4-8 ชั้น (350 ยูนิต/คอมเพล็กซ์) รวม 125,000 ประชากร"),
                ("Private Hydroponic Balconies", "ระเบียงเกษตรลอยฟ้า 15-25 ตร.ม./ยูนิต ผลิตอาหารสดและออกซิเจนหมุนเวียน"),
                ("Hermetic Blast Shutters", "บานเกล็ดนิรภัยไททาเนียมเลื่อนปิดล็อกอัตโนมัติใน 12 วินาทีเมื่อเมืองดำน้ำลึก"),
                ("Civic Living Amenities", "โรงอาหาร 17 รัฐ, คลินิกสุขภาพชุมชน, โรงเรียนประถม, ระบบส่งขยะและซักรีดสูญญากาศ")
            ]
        },
        {
            "id": "[T]",
            "title": "3. พื้นที่ทดลองและแปลงวิจัยภาคสนาม (EXPERIMENTAL PROVING GROUNDS)",
            "col": (40, 240, 140),
            "items": [
                ("Hyperbaric Trench Testing Tanks", "แท็งก์ทดสอบแรงดัน 1,500 Bar (-200m) ทดสอบยานดำน้ำลึกและเซ็นเซอร์โซนาร์"),
                ("Open-Ocean Wave Flumes", "แอ่งทดสอบคลื่นทะเลเปิด 300 เมตร ที่ปลายปีกกลีบ ทดสอบความลู่ลมของเรือไฮโดรฟอยล์"),
                ("Atmospheric Stress Domes", "โดมจำลองพายุหมุน 400 km/h และเสาปล่อยประจุฟ้าผ่าใน Petal 2 ทดสอบม่านบาเรีย"),
                ("Abyssal Drill Rig Sites", "แท่นทดสอบขุดเจาะแร่ก้นสมุทร -1,000m ติดตั้งบนก้ามปูหินไททาเนียม Bedrock Claws")
            ]
        },
        {
            "id": "[P]",
            "title": "4. พื้นที่สาธารณะและทางเดินเลียบสมุทร (PUBLIC SPACES & COMMONS)",
            "col": (0, 220, 255),
            "items": [
                ("Grand Lotus Esplanade", "ทางเดินเท้าและเลนจักรยานเลียบสมุทรยาว 12 กิโลเมตร ชมวิวเส้นขอบฟ้า 360 องศา"),
                ("Glazed Skywalk Network", "สะพานลอยฟ้ากระจกปรับอากาศ +38m เชื่อมทุกอาคารและข้ามกลีบโดยไม่ต้องกลัวฝนลม"),
                ("Botanical Bio-Parks & Lagoons", "สวนสาธารณะในโดมแก้วและลากูนน้ำกร่อยเทียม พืชป่าฝนและสัตว์น้ำปรับสายพันธุ์"),
                ("17-State Cultural Bazaar", "พ็อดตลาดนัดนานาชาติ 64 ยูนิต จำหน่ายงานศิลปะ หนังสือ และอาหารพื้นเมือง 17 มหารัฐ")
            ]
        }
    ]

    for idx, typ in enumerate(typologies):
        ty_y = panel_y + idx * (card_h + 10)
        col = typ["col"]

        # Card container
        draw.rectangle([panel_x, ty_y, panel_x + panel_w, ty_y + card_h], fill=(10, 20, 36, 225), outline=(col[0], col[1], col[2], 140), width=1)
        # Header banner
        draw.rectangle([panel_x, ty_y, panel_x + panel_w, ty_y + 30], fill=(14, 28, 48, 255))
        draw.line([panel_x, ty_y, panel_x + panel_w, ty_y], fill=col, width=3)

        # ID Badge
        draw.rectangle([panel_x + 8, ty_y + 6, panel_x + 32, ty_y + 24], fill=(col[0], col[1], col[2], 60), outline=col, width=1)
        draw.text((panel_x + 12, ty_y + 7), typ["id"], font=f_badge, fill=col)
        # Title
        draw.text((panel_x + 40, ty_y + 7), typ["title"], font=f_sec, fill=(255, 255, 255))

        # Items
        item_y = ty_y + 38
        for name_str, desc_str in typ["items"]:
            draw.text((panel_x + 14, item_y), f"• {name_str}:", font=f_bold, fill=col)
            draw.text((panel_x + 225, item_y), desc_str, font=f_small, fill=(210, 230, 245))
            item_y += 24

    # Save to outputs
    img_rgb = img.convert("RGB")
    img_rgb.save(OUTPUT_PNG, "PNG")
    img_rgb.save(OUTPUT_JPG, "JPEG", quality=95)
    img_rgb.save(OUTPUT_ROOT_JPG, "JPEG", quality=95)

    print(f"[+] Successfully generated 6-Tier Zoning & 4 Urban Typologies Map:")
    print(f"    - {OUTPUT_PNG}")
    print(f"    - {OUTPUT_JPG}")
    print(f"    - {OUTPUT_ROOT_JPG}")
    return True


if __name__ == "__main__":
    generate_zoning_map()
