#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN MEGASTRUCTURE - COMPLETE 3D TRANSIT & LOGISTICS NETWORK MAP
================================================================================
Generates a 1920x1080 Sci-Fi Master Transit Schematic Diagram:
- Radial Maglev Lines (Lines M1 to M8, color-coded per Faculty)
- Inner Loop Ring Line (Line R0 - Hinge Interchange at R=250m)
- Vertical Deep-Sea Transit Elevator Core (Line V1: +120m to -980m, 5 Airlocks)
- Emergency Pneumatic Evac Hyperloop Tubes (6-minute bunker protocol)
- 45m Inter-Petal Canal Waterway Ferry Routes & Outer Marina Jetties
- Technical Line Directory, Station Inventory, and Fleet Operations Telemetry
================================================================================
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_JPG = os.path.join(WORKSPACE_DIR, "08_PRESENTATION", "ISTRORIGAN_TRANSIT_NETWORK_MAP.jpg")
OUTPUT_PNG = os.path.join(WORKSPACE_DIR, "08_PRESENTATION", "ISTRORIGAN_TRANSIT_NETWORK_MAP.png")
OUTPUT_ROOT_JPG = os.path.join(WORKSPACE_DIR, "ISTRORIGAN_TRANSIT_NETWORK_MAP.jpg")


def draw_dashed_line(draw, p1, p2, fill, width=1, dash_len=8, gap_len=6):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    vx = dx / dist
    vy = dy / dist
    curr = 0.0
    while curr < dist:
        end = min(curr + dash_len, dist)
        draw.line([(x1 + vx * curr, y1 + vy * curr), (x1 + vx * end, y1 + vy * end)], fill=fill, width=width)
        curr += dash_len + gap_len


def generate_transit_map():
    w, h = 1920, 1080
    img = Image.new("RGBA", (w, h), (7, 12, 22, 255))
    draw = ImageDraw.Draw(img)

    # Grid background
    grid_col = (16, 28, 48, 140)
    for x in range(0, w, 40):
        draw.line([(x, 0), (x, h)], fill=grid_col, width=1)
    for y in range(0, h, 40):
        draw.line([(0, y), (w, y)], fill=grid_col, width=1)

    # Fonts
    font_bold_path = "C:/Windows/Fonts/tahomabd.ttf" if os.path.exists("C:/Windows/Fonts/tahomabd.ttf") else "C:/Windows/Fonts/arialbd.ttf"
    font_reg_path = "C:/Windows/Fonts/tahoma.ttf" if os.path.exists("C:/Windows/Fonts/tahoma.ttf") else "C:/Windows/Fonts/arial.ttf"

    f_title = ImageFont.truetype(font_bold_path, 24)
    f_sub = ImageFont.truetype(font_reg_path, 12)
    f_sec = ImageFont.truetype(font_bold_path, 13)
    f_body = ImageFont.truetype(font_reg_path, 11)
    f_bold = ImageFont.truetype(font_bold_path, 11)
    f_small = ImageFont.truetype(font_reg_path, 9)

    # HEADER BANNER
    draw.rectangle([0, 0, w, 70], fill=(5, 14, 26, 245))
    draw.line([(0, 70), (w, 70)], fill=(0, 210, 255, 220), width=2)
    draw.text((35, 12), "ISTRORIGAN (อิสโตรริแกน) — 3D TRANSIT & LOGISTICS NETWORK MASTER SCHEMATIC", font=f_title, fill=(240, 250, 255))
    draw.text((35, 45), "ERA: 4205 | 136 ROUTES | 76 STATIONS | 150,000 PASSENGERS/HR | 6-MINUTE EMERGENCY EVACUATION HYPERLOOP", font=f_sub, fill=(0, 210, 240))
    draw.text((w - 420, 16), "SYS_10: 3D MAGLEV & EVAC MULTI-LAYER TRANSIT", font=f_sec, fill=(255, 200, 60))
    draw.text((w - 420, 36), "UNIFIED RAPID TRANSIT COMMAND | ALL LINES OPERATIONAL", font=f_small, fill=(0, 255, 180))

    # FOOTER BANNER
    draw.rectangle([0, h - 55, w, h], fill=(5, 14, 26, 245))
    draw.line([(0, h - 55), (w, h - 55)], fill=(0, 210, 255, 180), width=1)
    footer_cols = [
        ("LINE M1-M8: RADIAL MAGLEV", "Top Speed: 350 km/h | 30s Headway | Surface Spine"),
        ("LINE R0: INNER RING LOOP", "Inter-Petal Hinge Crossing at R=250m | Elevated +38m Skybridges"),
        ("LINE V1: DEEP-SEA ELEVATOR", "1.1 km Vertical Core | 25 m/s Maglev Cabs | 5 Pressure Airlocks"),
        ("EVAC HYPERLOOP NETWORK", "64 Pneumatic Tubes | 600 km/h | Complete City Evac in < 6 Mins")
    ]
    for i, (title_str, val_str) in enumerate(footer_cols):
        cx = 35 + i * 460
        draw.text((cx, h - 45), title_str, font=f_bold, fill=(0, 225, 255))
        draw.text((cx, h - 25), val_str, font=f_small, fill=(190, 215, 235))

    # LEFT PANEL: Vertical Transit Profile (SYS_13 Deep-Sea Elevator Core)
    v_panel_x = 35
    v_panel_y = 90
    v_panel_w = 340
    v_panel_h = 910
    draw.rectangle([v_panel_x, v_panel_y, v_panel_x + v_panel_w, v_panel_y + v_panel_h], fill=(10, 20, 36, 220), outline=(0, 180, 230, 120), width=1)
    draw.rectangle([v_panel_x, v_panel_y, v_panel_x + v_panel_w, v_panel_y + 35], fill=(14, 30, 54, 255))
    draw.text((v_panel_x + 12, v_panel_y + 9), "LINE V1: VERTICAL ELEVATOR CORE (1.1 KM)", font=f_sec, fill=(255, 220, 80))

    # Draw vertical elevator schematic
    shaft_x = v_panel_x + 70
    shaft_top_y = v_panel_y + 60
    shaft_bot_y = v_panel_y + v_panel_h - 70
    draw.rectangle([shaft_x - 14, shaft_top_y, shaft_x + 14, shaft_bot_y], fill=(15, 35, 60, 255), outline=(0, 220, 255, 180), width=2)
    # Maglev rail lines inside shaft
    draw.line([(shaft_x - 5, shaft_top_y), (shaft_x - 5, shaft_bot_y)], fill=(0, 255, 200, 150), width=1)
    draw.line([(shaft_x + 5, shaft_top_y), (shaft_x + 5, shaft_bot_y)], fill=(0, 255, 200, 150), width=1)

    airlock_stations = [
        ("+600m", shaft_top_y + 10, "Apex Citadel Observatory", "Council Only / VIP Cabs"),
        ("+120m", shaft_top_y + 140, "Grand Central Faculty Plaza", "Interchange with M1-M8 Spines"),
        ("0.0m",  shaft_top_y + 260, "Sea Level / Canal Terminal", "Hydrofoil & Bulkhead Ferry Dock"),
        ("-250m", shaft_top_y + 440, "Bathyal Stem Airlock Hub", "Upper Ballast & Hyperbaric Labs"),
        ("-500m", shaft_top_y + 590, "Abyssal Geothermal Junction", "Power Generators & Sub Docks"),
        ("-750m", shaft_top_y + 720, "Lower Expansion Ring Depot", "Shock Absorber Maintenance Ring"),
        ("-980m", shaft_bot_y - 20, "Doomsday Knowledge Vault", "DNA Bank & Bedrock Claws Anchor")
    ]

    for elev_str, sy, st_name, st_desc in airlock_stations:
        # Station node box
        draw.rectangle([shaft_x - 20, sy - 8, shaft_x + 20, sy + 8], fill=(255, 180, 0, 255), outline=(255, 255, 255), width=2)
        # Callout line to right
        draw.line([(shaft_x + 20, sy), (shaft_x + 45, sy)], fill=(0, 220, 255, 200), width=2)
        # Station texts
        draw.text((shaft_x + 52, sy - 14), st_name, font=f_bold, fill=(240, 250, 255))
        draw.text((shaft_x + 52, sy + 1), f"ELEV: {elev_str} | {st_desc}", font=f_small, fill=(160, 210, 240))
        # Elevation marker on left
        draw.text((shaft_x - 62, sy - 6), elev_str, font=f_bold, fill=(0, 230, 255))

    draw.text((v_panel_x + 15, v_panel_y + v_panel_h - 45), "• 4 Pressurized Maglev Cabs @ 25 m/s (2.5 mins total trip)\n• 200 Bar Titanium Shaft Wall (80cm thickness)", font=f_small, fill=(180, 210, 230))

    # CENTER AREA: Radial Polar Transit Map of Istrorigan (3,000m diameter)
    cx = 1000
    cy = 530
    max_r = 380

    # Draw sea/water background circle
    draw.ellipse([cx - max_r - 20, cy - max_r - 20, cx + max_r + 20, cy + max_r + 20], fill=(9, 18, 32, 255), outline=(0, 160, 220, 90), width=1)

    # Concentric distance rings
    ring_radii = [
        (int(max_r * (150/1100)), "R=150m (Core Hub)"),
        (int(max_r * (350/1100)), "R=350m (Inner Hinge Ring R0)"),
        (int(max_r * (750/1100)), "R=750m (Mid-Living / Domes)"),
        (int(max_r * (1100/1100)), "R=1,100m (Outer Esplanade & Docks)")
    ]
    for r_val, r_lbl in ring_radii:
        draw.ellipse([cx - r_val, cy - r_val, cx + r_val, cy + r_val], outline=(0, 180, 240, 60), width=1)

    # Draw 8 Petal Outlines (Discrete flower petals separated by 45m canals)
    faculties = [
        {"id": "M1", "deg": 0,   "name": "Line M1: Oceanic Power",     "col": (40, 140, 255), "pet": "Petal 0: Engineering"},
        {"id": "M2", "deg": 45,  "name": "Line M2: Biosphere & Marine", "col": (40, 230, 120), "pet": "Petal 1: Biology"},
        {"id": "M3", "deg": 90,  "name": "Line M3: Climate Defense",    "col": (150, 230, 255),"pet": "Petal 2: Atmosphere"},
        {"id": "M4", "deg": 135, "name": "Line M4: Megastructure Civ",  "col": (255, 145, 50), "pet": "Petal 3: Architecture"},
        {"id": "M5", "deg": 180, "name": "Line M5: Universal Library",  "col": (200, 100, 255),"pet": "Petal 4: Humanities"},
        {"id": "M6", "deg": 225, "name": "Line M6: Abyssal Mining",     "col": (255, 215, 40), "pet": "Petal 5: Deep-Sea"},
        {"id": "M7", "deg": 270, "name": "Line M7: 17-State Assembly",  "col": (255, 190, 0),  "pet": "Petal 6: Diplomacy"},
        {"id": "M8", "deg": 315, "name": "Line M8: Oceanic Medicine",   "col": (255, 60, 90),  "pet": "Petal 7: Genetics"}
    ]

    # Draw 45m Inter-Petal Waterways (Canals) radiating between petals
    for i in range(8):
        canal_deg = i * 45 + 22.5
        rad = math.radians(canal_deg)
        x2 = cx + int(max_r * 1.05 * math.cos(rad))
        y2 = cy + int(max_r * 1.05 * math.sin(rad))
        draw_dashed_line(draw, (cx, cy), (x2, y2), fill=(0, 210, 255, 120), width=2, dash_len=6, gap_len=4)

    # Draw Inner Loop Ring Line (Line R0 - Circular Maglev connecting all 8 petal bases)
    r_inner_loop = int(max_r * (350/1100))
    draw.ellipse([cx - r_inner_loop, cy - r_inner_loop, cx + r_inner_loop, cy + r_inner_loop], outline=(255, 220, 60, 230), width=3)

    # Draw the 8 Radial Spine Lines (Lines M1 to M8)
    for fac in faculties:
        deg = fac["deg"]
        rad = math.radians(deg)
        col = fac["col"]

        p_core = (cx + int(50 * math.cos(rad)), cy + int(50 * math.sin(rad)))
        p_hinge = (cx + int(r_inner_loop * math.cos(rad)), cy + int(r_inner_loop * math.sin(rad)))
        p_mid = (cx + int(max_r * 0.65 * math.cos(rad)), cy + int(max_r * 0.65 * math.sin(rad)))
        p_tip = (cx + int(max_r * 0.98 * math.cos(rad)), cy + int(max_r * 0.98 * math.sin(rad)))

        # Draw main spine line
        draw.line([p_core, p_hinge, p_mid, p_tip], fill=col, width=4)

        # Draw emergency evacuation dotted conduits parallel
        rad_evac = math.radians(deg + 3.0)
        e_start = (cx + int(60 * math.cos(rad_evac)), cy + int(60 * math.sin(rad_evac)))
        e_end = (cx + int(max_r * 0.92 * math.cos(rad_evac)), cy + int(max_r * 0.92 * math.sin(rad_evac)))
        draw_dashed_line(draw, e_start, e_end, fill=(255, 120, 30, 160), width=2, dash_len=4, gap_len=4)

        # Station nodes
        # 1. Hinge interchange station (transfer with R0)
        draw.ellipse([p_hinge[0]-7, p_hinge[1]-7, p_hinge[0]+7, p_hinge[1]+7], fill=(255, 255, 255), outline=col, width=2)
        # 2. Mid Campus Station
        draw.rectangle([p_mid[0]-5, p_mid[1]-5, p_mid[0]+5, p_mid[1]+5], fill=col, outline=(255, 255, 255), width=1)
        # 3. Outer Tip Harbor Station
        draw.ellipse([p_tip[0]-6, p_tip[1]-6, p_tip[0]+6, p_tip[1]+6], fill=(0, 230, 255), outline=(255, 255, 255), width=2)

        # Petal Tip Badge Label
        lbl_x = cx + int((max_r + 32) * math.cos(rad))
        lbl_y = cy + int((max_r + 32) * math.sin(rad))
        draw.rectangle([lbl_x - 30, lbl_y - 12, lbl_x + 30, lbl_y + 12], fill=(8, 22, 40, 240), outline=col, width=2)
        draw.text((lbl_x - 14, lbl_y - 8), fac["id"], font=f_bold, fill=col)

    # Central Spire Grand Central Terminal
    draw.ellipse([cx - 45, cy - 45, cx + 45, cy + 45], fill=(25, 45, 80, 240), outline=(0, 230, 255, 255), width=3)
    draw.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=(255, 215, 0, 255), outline=(255, 255, 255), width=2)
    draw.text((cx - 36, cy + 50), "GRAND CENTRAL HUB", font=f_bold, fill=(255, 220, 80))
    draw.text((cx - 48, cy + 64), "[Council Citadel + Spire]", font=f_small, fill=(0, 220, 255))

    # RIGHT PANEL: Line Directory, Station Inventory, and Fleet Operations Telemetry
    r_panel_x = w - 460
    r_panel_y = 90
    r_panel_w = 425
    r_panel_h = 910
    draw.rectangle([r_panel_x, r_panel_y, r_panel_x + r_panel_w, r_panel_y + r_panel_h], fill=(10, 20, 36, 220), outline=(0, 180, 230, 120), width=1)
    draw.rectangle([r_panel_x, r_panel_y, r_panel_x + r_panel_w, r_panel_y + 35], fill=(14, 30, 54, 255))
    draw.text((r_panel_x + 14, r_panel_y + 9), "TRANSIT DIRECTORY & NETWORK METROLOGY", font=f_sec, fill=(0, 240, 255))

    dy = r_panel_y + 48
    draw.text((r_panel_x + 14, dy), "RADIAL MAGLEV SPINES (LINES M1 - M8)", font=f_bold, fill=(255, 200, 60))
    dy += 18

    for fac in faculties:
        col = fac["col"]
        draw.rectangle([r_panel_x + 14, dy + 2, r_panel_x + 36, dy + 18], fill=col)
        draw.text((r_panel_x + 18, dy + 3), fac["id"], font=f_bold, fill=(10, 20, 30))
        draw.text((r_panel_x + 44, dy + 3), f"{fac['name']} ({fac['pet']})", font=f_small, fill=(230, 240, 250))
        dy += 22

    dy += 10
    draw.line([(r_panel_x + 14, dy), (r_panel_x + r_panel_w - 14, dy)], fill=(0, 180, 230, 80), width=1)
    dy += 12

    # Ring & Aux Lines
    draw.text((r_panel_x + 14, dy), "INTER-DISTRICT & VERTICAL TRANSIT", font=f_bold, fill=(255, 200, 60))
    dy += 20

    aux_lines = [
        ("LINE R0", (255, 220, 60), "Inner Loop Hinge Interchange (Circumferential 8-Petal Crossing at R=250m)"),
        ("LINE V1", (255, 180, 0),  "Deep-Sea 1.1km Elevator Core (Citadel +120m to Seabed Vault -980m)"),
        ("EVAC-6M", (255, 120, 30), "Pneumatic Evac Tubes (600 km/h Direct to Subsurface Bunker)"),
        ("CANAL-F", (0, 210, 255),  "Hydrofoil Maritime Ferry (45m Waterway Gap Transit & Cargo)")
    ]
    for code, col, desc in aux_lines:
        draw.rectangle([r_panel_x + 14, dy + 2, r_panel_x + 68, dy + 18], fill=col)
        draw.text((r_panel_x + 18, dy + 3), code, font=f_bold, fill=(10, 20, 30))
        draw.text((r_panel_x + 76, dy + 3), desc, font=f_small, fill=(210, 230, 245))
        dy += 24

    dy += 10
    draw.line([(r_panel_x + 14, dy), (r_panel_x + r_panel_w - 14, dy)], fill=(0, 180, 230, 80), width=1)
    dy += 12

    # Operations & Fleet Telemetry Table
    draw.text((r_panel_x + 14, dy), "NETWORK TELEMETRY & CAPACITY SPECIFICATIONS", font=f_bold, fill=(0, 240, 255))
    dy += 22

    specs = [
        ("Total Network Routes", "136 Routes (Radial, Loop, Vertical, Marine)"),
        ("Active Passenger Stations", "76 Multi-Level Stations & Terminals"),
        ("Hourly System Throughput", "150,000 Passengers / Hour"),
        ("Maximum Maglev Speed", "350 km/h (Surface) / 180 km/h (Undersea)"),
        ("Vertical Cab Velocity", "25 m/s (1.1 km shaft in 2.5 minutes)"),
        ("Evacuation Clearance Time", "< 6.0 Minutes (125,000 citizens to bunker)"),
        ("Canal Ferry Fleet", "48 Electric Hydrofoil & Cargo Shuttles"),
        ("Power Supply Grid", "Dual Induction Linear Motor + Geothermal Siphon")
    ]
    for key, val in specs:
        draw.text((r_panel_x + 14, dy), f"• {key}:", font=f_bold, fill=(180, 220, 240))
        draw.text((r_panel_x + 175, dy), val, font=f_small, fill=(255, 255, 255))
        dy += 22

    dy += 15
    draw.rectangle([r_panel_x + 14, dy, r_panel_x + r_panel_w - 14, dy + 110], fill=(14, 28, 48, 200), outline=(0, 210, 255, 120), width=1)
    draw.text((r_panel_x + 22, dy + 8), "TRANSIT SAFETY & LOCKDOWN RULES (SYS_10 & SYS_14):", font=f_bold, fill=(255, 200, 60))
    draw.text((r_panel_x + 22, dy + 28),
              "1. Monsoon Submergence: Line R0 elevated skybridges seal hermetic shutters.\n"
              "2. Quarantine Lockdown: Bulkhead gates guillotine drop in 15 seconds,\n"
              "   severing maglev conduits to affected petal while keeping 7 others live.\n"
              "3. Fail-Safe Gravity Brakes: Deepsea cabs auto-clamp to titanium guide rails.",
              font=f_small, fill=(200, 225, 240))

    # Save to files
    img_rgb = img.convert("RGB")
    img_rgb.save(OUTPUT_PNG, "PNG")
    img_rgb.save(OUTPUT_JPG, "JPEG", quality=95)
    img_rgb.save(OUTPUT_ROOT_JPG, "JPEG", quality=95)

    print(f"[+] Successfully generated 3D Transit Schematic:")
    print(f"    - {OUTPUT_PNG}")
    print(f"    - {OUTPUT_JPG}")
    print(f"    - {OUTPUT_ROOT_JPG}")
    return True


if __name__ == "__main__":
    generate_transit_map()
