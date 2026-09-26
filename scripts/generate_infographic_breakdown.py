#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN MEGASTRUCTURE - FINAL INFOGRAPHIC & ANATOMY BREAKDOWN GENERATOR
================================================================================
Generates a 1920x1080 Sci-Fi Master Presentation Infographic Poster:
- Embedded High-Res Canon Render (LOTUS_BARRIER_ACADEMY.jpg)
- HUD Leader Lines, Reticles & Badges
- Callout Explanations for all 8 Core Architectural Systems
- Elevation & Depth Gauges (+600m to -1,000m)
- Engineering Specs, Telemetry & Canon Worldbuilding Data
================================================================================
"""

# region MODULE IMPORTS & PATHS
import os
import math
try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter  # type: ignore
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_PATH = os.path.join(WORKSPACE_DIR, "LOTUS_BARRIER_ACADEMY.jpg")
OUTPUT_IMAGE = os.path.join(WORKSPACE_DIR, "ISTRORIGAN_FINAL_BREAKDOWN.png")
OUTPUT_JPG = os.path.join(WORKSPACE_DIR, "ISTRORIGAN_FINAL_BREAKDOWN.jpg")
# endregion

# region INFOGRAPHIC IMAGE COMPOSITOR
def create_infographic():
    if not PIL_AVAILABLE:
        print("[!] PIL (Pillow) is not installed. Run 'pip install Pillow' to generate infographics.")
        return False

    canvas_w = 1920
    canvas_h = 1080

    # Create dark sci-fi background canvas
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (8, 12, 20, 255))
    draw = ImageDraw.Draw(canvas)

    # Subtle grid background
    grid_color = (20, 35, 55, 120)
    for x in range(0, canvas_w, 40):
        draw.line([(x, 0), (x, canvas_h)], fill=grid_color, width=1)
    for y in range(0, canvas_h, 40):
        draw.line([(0, y), (canvas_w, y)], fill=grid_color, width=1)

    # Load and position the main render
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: {IMAGE_PATH} not found")
        return False

    base_render = Image.open(IMAGE_PATH).convert("RGBA")
    
    # Scale render to fit central display (approx 1280x714)
    target_rw = 1240
    target_rh = int(base_render.height * (target_rw / base_render.width))
    render_resized = base_render.resize((target_rw, target_rh), Image.Resampling.LANCZOS)

    # Position render centered horizontally, slightly offset vertically
    rx = (canvas_w - target_rw) // 2
    ry = 95
    canvas.paste(render_resized, (rx, ry), render_resized)

    # Draw sleek sci-fi HUD frame around the render
    frame_color = (0, 210, 255, 200)
    frame_bg = (10, 25, 45, 100)
    
    # Outer frame border
    draw.rectangle([rx - 2, ry - 2, rx + target_rw + 1, ry + target_rh + 1], outline=(0, 150, 200, 100), width=1)
    
    # Corner brackets for camera HUD feel
    corner_len = 30
    for cx, cy in [(rx, ry), (rx + target_rw, ry), (rx, ry + target_rh), (rx + target_rw, ry + target_rh)]:
        dx = 1 if cx == rx else -1
        dy = 1 if cy == ry else -1
        draw.line([(cx, cy), (cx + dx * corner_len, cy)], fill=(0, 240, 255, 255), width=3)
        draw.line([(cx, cy), (cx, cy + dy * corner_len)], fill=(0, 240, 255, 255), width=3)

    # Fonts
    font_title_path = "C:/Windows/Fonts/tahomabd.ttf" if os.path.exists("C:/Windows/Fonts/tahomabd.ttf") else "C:/Windows/Fonts/arialbd.ttf"
    font_reg_path = "C:/Windows/Fonts/tahoma.ttf" if os.path.exists("C:/Windows/Fonts/tahoma.ttf") else "C:/Windows/Fonts/arial.ttf"

    f_title = ImageFont.truetype(font_title_path, 25)
    f_sub = ImageFont.truetype(font_reg_path, 13)
    f_badge = ImageFont.truetype(font_title_path, 12)
    f_card_title = ImageFont.truetype(font_title_path, 12)
    f_card_body = ImageFont.truetype(font_reg_path, 11)
    f_tag = ImageFont.truetype(font_reg_path, 10)

    # TOP HEADER BANNER
    draw.rectangle([0, 0, canvas_w, 75], fill=(5, 15, 28, 240))
    draw.line([(0, 75), (canvas_w, 75)], fill=(0, 200, 255, 200), width=2)
    
    # Header titles
    draw.text((35, 14), "ISTRORIGAN (อิสโตรริแกน) — MEGASTRUCTURE MASTER ANATOMY", font=f_title, fill=(240, 250, 255))
    draw.text((35, 48), "ERA: 4205 | SOVEREIGN SANCTUARY OF 17 GREAT STATES | 8-PETAL PROCEDURAL PCG ARCHITECTURE", font=f_sub, fill=(0, 210, 240))

    # Header right telemetry
    draw.text((canvas_w - 480, 18), "GRID COORD: 14°22'N, 142°50'E [PACIFIC DEEP TRENCH]", font=f_tag, fill=(150, 200, 225))
    draw.text((canvas_w - 480, 34), "STATUS: ONLINE | BARRIER: 100% | ELEVATION: +600M TO -1,000M", font=f_tag, fill=(0, 255, 180))
    draw.text((canvas_w - 480, 50), "DIAMETER: 3,000M | PETALS: 8 DISCRETE | POPULATION: 250,000", font=f_tag, fill=(200, 220, 240))

    # BOTTOM FOOTER BANNER
    footer_y = canvas_h - 75
    draw.rectangle([0, footer_y, canvas_w, canvas_h], fill=(5, 15, 28, 240))
    draw.line([(0, footer_y), (canvas_w, footer_y)], fill=(0, 200, 255, 200), width=2)

    footer_items = [
        ("01. ARCHITECTURE", "8 Discrete Petal Campuses (No Interpenetration)"),
        ("02. SAFETY CLEARANCE", "45.0m Navigable Waterways Between Petals"),
        ("03. DEFENSE MATRIX", "70 Golden Stamen Pylons + Hexagonal Forcefield"),
        ("04. DIVE PROFILE", "12 Telescopic Hydraulic Rings (-1000m Abyssal Vault)")
    ]
    for i, (head, val) in enumerate(footer_items):
        col_x = 35 + i * 460
        draw.text((col_x, footer_y + 16), head, font=f_card_title, fill=(0, 220, 255))
        draw.text((col_x, footer_y + 40), val, font=f_card_body, fill=(210, 225, 235))

    # CALLOUT DEFINITIONS
    # Coordinates mapped to target_rw (1240) and target_rh (692) placed at (rx=340, ry=95)
    sx = target_rw / 1376.0
    sy = target_rh / 768.0

    def pt(orig_x, orig_y):
        return (int(rx + orig_x * sx), int(ry + orig_y * sy))

    card_width = 315

    # 8 Key Systems to annotate
    callouts = [
        # LEFT COLUMN (System 01 - 04)
        {
            "id": "01",
            "title": "หอคอยสภาสิบ & แกนกลาง (Apex Spire)",
            "elev": "+600m Peak | Core Zone",
            "body": "ศูนย์บัญชาการ The Council of Ten สถาบันปกครอง 17 รัฐ\nและเสาส่งสัญญาณเครือข่ายความเร็วสูงกลางมหานคร",
            "target": pt(688, 255),
            "card_x": 15,
            "card_y": 105,
            "card_w": card_width,
            "card_h": 100,
            "align": "left",
            "color": (255, 185, 45)
        },
        {
            "id": "02",
            "title": "ม่านบาเรียพลังงานรังผึ้ง (Hex Dome)",
            "elev": "Radius 1,500m | Outer Barrier",
            "body": "เกราะสนามแม่เหล็กไฟฟ้าความถี่สูง ป้องกันพายุคลื่นยักษ์\nและรังสีภายนอก ทำงานประสานกับเสาสนามพลัง 70 ต้น",
            "target": pt(430, 160),
            "card_x": 15,
            "card_y": 240,
            "card_w": card_width,
            "card_h": 100,
            "align": "left",
            "color": (0, 240, 255)
        },
        {
            "id": "03",
            "title": "วิทยาเขตกลีบดอกไม้ (8 Academic Petals)",
            "elev": "Radius 300m - 1,500m | Academic",
            "body": "8 กลีบเอกเทศสำหรับ 8 คณะใหญ่แห่งมวลมนุษยชาติ\nประกอบด้วยอัฒจันทร์บรรยายกลางแจ้ง และลานกิจกรรม",
            "target": pt(410, 545),
            "card_x": 15,
            "card_y": 380,
            "card_w": card_width,
            "card_h": 105,
            "align": "left",
            "color": (120, 255, 160)
        },
        {
            "id": "04",
            "title": "โดมวิจัยสิ่งแวดล้อม & หอพักนานาชาติ",
            "elev": "Sub-Campus Bio-Domes & Living",
            "body": "โดมชีววิทยาปรับสภาพอากาศเพาะเลี้ยงพืชพันธุ์หายาก\nและยูนิตพักอาศัยโมดูลาร์สำหรับคณาจารย์และนักศึกษา",
            "target": pt(255, 500),
            "card_x": 15,
            "card_y": 525,
            "card_w": card_width,
            "card_h": 95,
            "align": "left",
            "color": (100, 220, 255)
        },

        # RIGHT COLUMN (System 05 - 08)
        {
            "id": "05",
            "title": "เสาสนามพลังงาน 70 ต้น (Stamen Pylons)",
            "elev": "Height +45m | Perimeter Matrix",
            "body": "เสากำเนิดพลาสมาสีทอง 70 ต้นรอบ Citadel ทำหน้าที่\nฉายพลังงานค้ำจุนม่านบาเรียรังผึ้งและสายกริดพลังงาน",
            "target": pt(760, 375),
            "card_x": canvas_w - card_width - 15,
            "card_y": 105,
            "card_w": card_width,
            "card_h": 100,
            "align": "right",
            "color": (255, 200, 60)
        },
        {
            "id": "06",
            "title": "ร่องน้ำสัญจร 45 เมตร (Inter-Petal Canal)",
            "elev": "Clearance Gap: 45.0m Constant",
            "body": "ช่องว่างปลอดภัยระหว่างกลีบป้องกันการชนกันขณะพับกลีบ\nใช้เป็นร่องน้ำเดินเรือเฟอร์รี่และเส้นทางอพยพฉุกเฉิน",
            "target": pt(500, 530),
            "card_x": canvas_w - card_width - 15,
            "card_y": 240,
            "card_w": card_width,
            "card_h": 100,
            "align": "right",
            "color": (0, 230, 255)
        },
        {
            "id": "07",
            "title": "ท่าเรือปลายกลีบแนวนอน (Deep-Sea Berth)",
            "elev": "Sea Level (Z = 0.0m) | Outer Tip",
            "body": "ปลายกลีบระนาบเสมอผิวน้ำทะเล รองรับเรือสำรวจสมุทร\nสถานีเชื่อมต่อเรือโดยสารจาก 17 รัฐ และชานชาลา Maglev",
            "target": pt(1070, 530),
            "card_x": canvas_w - card_width - 15,
            "card_y": 380,
            "card_w": card_width,
            "card_h": 100,
            "align": "right",
            "color": (0, 255, 200)
        },
        {
            "id": "08",
            "title": "วงแหวนถ่วงน้ำหนักยืดหด 12 ชั้น (Stem Rings)",
            "elev": "-50m to -1,000m Abyssal Depth",
            "body": "กระบอกไฮดรอลิกถ่วงน้ำหนัก ขยายรัศมีจาก 80m สู่ 350m\nรองรับการดำน้ำหลบพายุปีละ 2 ครั้ง และคลัง DNA ใต้สมุทร",
            "target": pt(710, 640),
            "card_x": canvas_w - card_width - 15,
            "card_y": 525,
            "card_w": card_width,
            "card_h": 105,
            "align": "right",
            "color": (0, 255, 230)
        }
    ]

    # DRAW CALLOUTS, CARDS AND CONNECTING LEADER LINES
    for c in callouts:
        cx, cy, cw, ch = c["card_x"], c["card_y"], c["card_w"], c["card_h"]
        target_coords = c["target"]
        tx, ty = int(target_coords[0]), int(target_coords[1])
        col = c["color"]

        # 1. Semi-transparent card background
        card_overlay = Image.new("RGBA", (cw, ch), (10, 20, 35, 220))
        canvas.paste(card_overlay, (cx, cy), card_overlay)
        
        # Card border & accent
        draw.rectangle([cx, cy, cx + cw, cy + ch], outline=(col[0], col[1], col[2], 180), width=1)
        draw.line([cx, cy, cx + cw, cy], fill=(col[0], col[1], col[2], 255), width=3)

        # ID Badge
        draw.rectangle([cx + 8, cy + 8, cx + 34, cy + 28], fill=(col[0], col[1], col[2], 50), outline=col, width=1)
        draw.text((cx + 12, cy + 10), c["id"], font=f_badge, fill=col)

        # Titles
        draw.text((cx + 42, cy + 8), c["title"], font=f_card_title, fill=(255, 255, 255))
        draw.text((cx + 42, cy + 26), f"ELEVATION: {c['elev']}", font=f_tag, fill=col)

        # Body text
        draw.text((cx + 10, cy + 45), c["body"], font=f_card_body, fill=(205, 220, 230))

        # 2. Leader Line connecting Card to Target Point
        if c["align"] == "left":
            start_pt = (cx + cw, cy + 20)
            elbow_pt = (cx + cw + 25, cy + 20)
        else:
            start_pt = (cx, cy + 20)
            elbow_pt = (cx - 25, cy + 20)

        # Draw glowing line
        draw.line([start_pt, elbow_pt, (tx, ty)], fill=(col[0], col[1], col[2], 220), width=2)

        # Target Reticle at (tx, ty)
        r_inner = 5
        r_outer = 11
        draw.ellipse([tx - r_inner, ty - r_inner, tx + r_inner, ty + r_inner], fill=(col[0], col[1], col[2], 255))
        draw.ellipse([tx - r_outer, ty - r_outer, tx + r_outer, ty + r_outer], outline=(col[0], col[1], col[2], 200), width=2)
        # Crosshair ticks
        draw.line([tx - r_outer - 4, ty, tx - r_outer + 1, ty], fill=col, width=1)
        draw.line([tx + r_outer - 1, ty, tx + r_outer + 4, ty], fill=col, width=1)
        draw.line([tx, ty - r_outer - 4, tx, ty - r_outer + 1], fill=col, width=1)
        draw.line([tx, ty + r_outer - 1, tx, ty + r_outer + 4], fill=col, width=1)

    # 3. Add Vertical Depth / Elevation Ruler on the left of render
    ruler_x = rx + 15
    draw.line([ruler_x, ry + 20, ruler_x, ry + target_rh - 20], fill=(0, 200, 255, 120), width=1)
    
    elevation_markers = [
        ("+600m", ry + int(255 * sy), "APEX SPIRE"),
        ("+120m", ry + int(400 * sy), "FACULTY PLAZA"),
        ("0.0m",  ry + int(560 * sy), "SEA LEVEL / WATERWAYS"),
        ("-200m", ry + int(630 * sy), "UPPER BALLAST RING"),
        ("-500m", ry + int(680 * sy), "ABYSSAL EXPANDING RING"),
        ("-1000m",ry + target_rh - 25, "SEABED CLAW & VAULT")
    ]
    for lbl, y_pos, desc in elevation_markers:
        draw.line([ruler_x - 6, y_pos, ruler_x + 6, y_pos], fill=(0, 230, 255, 200), width=2)
        draw.text((ruler_x + 10, y_pos - 7), f"{lbl}  [{desc}]", font=f_tag, fill=(0, 230, 255, 220))

    # Convert to RGB and save
    final_img = canvas.convert("RGB")
    final_img.save(OUTPUT_IMAGE, "PNG")
    final_img.save(OUTPUT_JPG, "JPEG", quality=95)

    print(f"[+] Successfully Generated Master Infographic:")
    print(f"    - {OUTPUT_IMAGE}")
    print(f"    - {OUTPUT_JPG}")
    return True
# endregion


# region MAIN ENTRY
if __name__ == "__main__":
    create_infographic()
# endregion
