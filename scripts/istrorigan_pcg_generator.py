#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN MEGASTRUCTURE PCG GENERATOR (YEAR 4205)
================================================================================
Procedural Point Cloud Generator strictly calibrated to:
- DT_District_Zoning.json & DT_Asset_Archetypes.json
- Unreal Engine Centimeter Scale (1 UU = 1 cm)
- Exact DataTable Row Names for ZoneTag (@ZoneTag = ZONE_FACULTY_...)
- 8 Discrete, Articulated Petals (4,500 cm = 45m Waterway Clearance)
- Outer Petal Tips Level at Sea Level (Z = 0.0 cm)
- Central Receptacle Citadel (R = 15,000 cm) & Council Spire (H = 35,000 cm)
- 70 Golden Stamen Pylons (H = 4,500 cm)
- 12 Telescopic Expanding Submerged Rings (-90,000 cm Abyssal Depth)
================================================================================
Usage:
    py scripts/istrorigan_pcg_generator.py
Outputs:
    output/istrorigan_lattice.json          (UE Centimeters + DT Row Names)
    output/istrorigan_lattice.csv           (UE Centimeters for Data Table Import)
    output/istrorigan_lattice_meters.csv    (Meters for Houdini / Blender)
================================================================================
"""

import os
import sys
import math
import json
import csv

# region CONFIGURATION & CANONICAL DIMENSIONS (CENTIMETERS - 1 UU = 1 CM)

PETAL_COUNT = 8
BASE_INNER_RADIUS_CM = 15000.0        # 150m (Matches ZONE_CORE_CITADEL MaxRadius)
PETAL_LENGTH_CM = 95000.0             # 950m (Tips at 110,000 cm = 1,100m, matches DT_District_Zoning MaxRadius)
PETAL_WIDTH_MAX_CM = 42000.0          # 420m max width
MIN_WATERWAY_CLEARANCE_CM = 4500.0    # 45m (4,500 cm) minimum safety channel

# Profile & Curvature (cm)
WIDTH_PROFILE_POWER = 1.20
WIDTH_SKEW = 0.52
CUP_DEPTH_CM = 3500.0                 # 35m bowl depression
KEEL_HEIGHT_CM = 2200.0               # 22m spine ridge
OPERATING_PITCH_DEG = 2.5             # Normal surface pitch

# Submerged Rings (Expanding Ballast Cradle in cm)
RING_TIER_COUNT = 12
SURFACE_NECK_RADIUS_CM = 8000.0       # 80m at citadel neck (Matches ZONE_STEM_TELESCOPIC MinRadius)
SEABED_ABYSSAL_RADIUS_CM = 35000.0    # 350m expanding bell (Matches ZONE_STEM_TELESCOPIC MaxRadius)
TOTAL_SUBMERGED_DEPTH_CM = -90000.0   # -900m abyssal seabed (Matches ZONE_STEM_TELESCOPIC MinDepth_Z)
RING_EXPANSION_EXPONENT = 1.65        # Flare curve
RING_ANGULAR_RES = 48

# Central Citadel & Stamens (cm)
RECEPTACLE_RADIUS_CM = 15000.0        # 150m circular deck
STAMEN_COUNT = 70                     # 70 golden stamen forcefield pylons
STAMEN_HEIGHT_CM = 4500.0             # 45m tall (Matches ARCH_BARRIER_PYLON_TOWER)
STAMEN_INWARD_LEAN_DEG = 14.0         # 14 degrees conical lean
APEX_SPIRE_HEIGHT_CM = 35000.0        # 350m Council of Ten Spire (Matches ZONE_CORE_CITADEL MaxElevation_Z)

# Sampling Resolution
PETAL_U_STEPS = 30                    # Points along length
PETAL_V_STEPS = 16                    # Points across width

# Exact DataTable Row Names from DT_District_Zoning.json
FACULTY_ZONES = [
    {"row_name": "ZONE_FACULTY_OCEANIC", "display_name": "Faculty of Oceanic Engineering & Power"},
    {"row_name": "ZONE_FACULTY_BIOSPHERE", "display_name": "Faculty of Biosphere & Marine Biology"},
    {"row_name": "ZONE_FACULTY_CLIMATE", "display_name": "Faculty of Geo-Atmospheric Stabilization"},
    {"row_name": "ZONE_FACULTY_MEGASTRUCT", "display_name": "Faculty of Floating Megastructure Civil Eng"},
    {"row_name": "ZONE_FACULTY_ARCHIVES", "display_name": "Grand Universal Library & Pre-Deluge Archives"},
    {"row_name": "ZONE_FACULTY_ABYSSAL", "display_name": "Faculty of Deep-Sea Mining & Trench Exploration"},
    {"row_name": "ZONE_FACULTY_DIPLOMACY", "display_name": "17-State Parliamentary Assembly & Living Campus"},
    {"row_name": "ZONE_FACULTY_MEDICINE", "display_name": "Faculty of Oceanic Medicine & Genetics"}
]

# endregion

# region MATHEMATICAL EVALUATION FUNCTIONS

def evaluate_petal_half_width(u):
    """Calculates half-width in cm while strictly enforcing 4,500 cm clearance."""
    u_clamped = max(0.0, min(1.0, u))
    radial_dist = BASE_INNER_RADIUS_CM + (u_clamped * PETAL_LENGTH_CM)
    
    half_slot_rad = math.pi / PETAL_COUNT
    max_permitted = (radial_dist * math.sin(half_slot_rad)) - (MIN_WATERWAY_CLEARANCE_CM * 0.5)
    max_permitted = max(max_permitted, 500.0) # 5m min structural spine

    vs = math.pow(u_clamped, WIDTH_SKEW)
    profile_sin = math.sin(math.pi * vs)
    profile_curve = math.pow(max(0.0, profile_sin), WIDTH_PROFILE_POWER)
    nominal = (PETAL_WIDTH_MAX_CM * 0.5) * profile_curve

    return min(nominal, max_permitted)


def evaluate_petal_surface_z(u, v):
    """Calculates surface elevation Z in cm, forcing outer tip flat at sea level (Z = 0 cm)."""
    u_clamped = max(0.0, min(1.0, u))
    v_clamped = max(-1.0, min(1.0, v))

    arch = math.sin(math.pi * u_clamped)
    keel_z = KEEL_HEIGHT_CM * (1.0 - abs(v_clamped)) * math.pow(arch, 0.65)
    cup_z = -CUP_DEPTH_CM * (v_clamped * v_clamped) * arch
    raw_z = keel_z + cup_z

    # Flat outer tip at sea level (Z = 0 cm) for harbor berths
    if u_clamped > 0.70:
        t = (u_clamped - 0.70) / 0.30
        blend = t * t * (3.0 - 2.0 * t)
        raw_z *= (1.0 - blend)

    return raw_z


def compute_petal_point(petal_idx, u, v, pitch_deg=OPERATING_PITCH_DEG):
    """Computes 3D Cartesian coordinates (X, Y, Z in cm) and normal vector."""
    center_angle_deg = petal_idx * (360.0 / PETAL_COUNT)
    center_rad = math.radians(center_angle_deg)

    rad_forward = (math.cos(center_rad), math.sin(center_rad))
    transverse = (-math.sin(center_rad), math.cos(center_rad))

    half_width = evaluate_petal_half_width(u)
    lat_offset = v * half_width

    pitch_rad = math.radians(pitch_deg)
    folded_spine_dist = (u * PETAL_LENGTH_CM) * math.cos(pitch_rad)
    
    # Outer tip rests level with ocean sea level (Z = 0)
    tip_level_blend = 1.0
    if u > 0.70:
        t = (u - 0.70) / 0.30
        tip_level_blend = 1.0 - (t * t * (3.0 - 2.0 * t))
        
    folded_z_offset = (u * PETAL_LENGTH_CM) * math.sin(pitch_rad) * tip_level_blend

    spine_x = (BASE_INNER_RADIUS_CM + folded_spine_dist) * rad_forward[0]
    spine_y = (BASE_INNER_RADIUS_CM + folded_spine_dist) * rad_forward[1]

    x = spine_x + (transverse[0] * lat_offset)
    y = spine_y + (transverse[1] * lat_offset)
    z = evaluate_petal_surface_z(u, v) + folded_z_offset

    # Normal vector approximation
    du = 0.01
    dv = 0.01
    z_u = evaluate_petal_surface_z(min(1.0, u + du), v)
    z_v = evaluate_petal_surface_z(u, min(1.0, v + dv))
    dzdu = (z_u - z) / (du * PETAL_LENGTH_CM)
    dzdv = (z_v - z) / (dv * max(half_width, 10.0))
    nx = -dzdu * rad_forward[0] - dzdv * transverse[0]
    ny = -dzdu * rad_forward[1] - dzdv * transverse[1]
    nz = 1.0
    n_len = math.sqrt(nx*nx + ny*ny + nz*nz)
    normal = (nx/n_len, ny/n_len, nz/n_len)

    return (x, y, z), normal


def calculate_submerged_radius(depth_z_cm):
    """Calculates expanding ring radius in cm at depth_z_cm (negative cm)."""
    norm_depth = max(0.0, min(1.0, abs(depth_z_cm) / abs(TOTAL_SUBMERGED_DEPTH_CM)))
    flare = math.pow(norm_depth, RING_EXPANSION_EXPONENT)
    return SURFACE_NECK_RADIUS_CM + ((SEABED_ABYSSAL_RADIUS_CM - SURFACE_NECK_RADIUS_CM) * flare)

# endregion

# region GENERATOR PIPELINE

def generate_istrorigan_dataset():
    all_points = []
    min_observed_clearance_cm = float('inf')
    clearance_violations = 0

    print("================================================================================")
    print(" GENERATING ISTRORIGAN MEGASTRUCTURE PCG LATTICE (CALIBRATED UE5 SCALE)")
    print("================================================================================")

    # 1. 8 Articulated Petals
    print(f"[*] Generating {PETAL_COUNT} discrete articulated petals (15,000 cm to 110,000 cm)...")
    for p_idx in range(PETAL_COUNT):
        fac = FACULTY_ZONES[p_idx]
        row_name = fac["row_name"]
        disp_name = fac["display_name"]

        for u_i in range(PETAL_U_STEPS + 1):
            u = u_i / float(PETAL_U_STEPS)
            r_dist = BASE_INNER_RADIUS_CM + (u * PETAL_LENGTH_CM)
            half_slot_rad = math.pi / PETAL_COUNT
            sector_chord = 2.0 * r_dist * math.sin(half_slot_rad)
            petal_width = evaluate_petal_half_width(u) * 2.0
            actual_clearance = sector_chord - petal_width

            if actual_clearance < min_observed_clearance_cm:
                min_observed_clearance_cm = actual_clearance
            if actual_clearance < MIN_WATERWAY_CLEARANCE_CM - 1.0:
                clearance_violations += 1

            for v_i in range(PETAL_V_STEPS + 1):
                v = -1.0 + (2.0 * (v_i / float(PETAL_V_STEPS)))
                (x, y, z), norm = compute_petal_point(p_idx, u, v)

                # Assign exact DataTable ZoneTag
                if abs(v) > 0.92:
                    zone_tag = "ZONE_CLEARANCE_WATERWAY"
                elif u > 0.85:
                    zone_tag = "ZONE_HARBOR_BERTH"
                else:
                    zone_tag = row_name

                radial_2d = math.sqrt(x*x + y*y)
                angle_deg = (math.degrees(math.atan2(y, x)) + 360.0) % 360.0

                all_points.append({
                    "id": len(all_points),
                    "component": "Petal",
                    "petal_index": p_idx,
                    "zone_tag": zone_tag,
                    "faculty_name": disp_name,
                    "u": round(u, 4),
                    "v": round(v, 4),
                    "x_cm": round(x, 2),
                    "y_cm": round(y, 2),
                    "z_cm": round(z, 2),
                    "x_m": round(x / 100.0, 3),
                    "y_m": round(y / 100.0, 3),
                    "z_m": round(z / 100.0, 3),
                    "radial_distance_cm": round(radial_2d, 2),
                    "angle_deg": round(angle_deg, 2),
                    "clearance_gap_cm": round(actual_clearance, 2),
                    "clearance_gap_m": round(actual_clearance / 100.0, 2),
                    "nx": round(norm[0], 4),
                    "ny": round(norm[1], 4),
                    "nz": round(norm[2], 4),
                    "target_buoyancy_kn": 35000.0,
                    "subcouncil": p_idx + 1
                })

    # 2. 70 Golden Stamen Forcefield Pylons
    print(f"[*] Generating {STAMEN_COUNT} golden stamen forcefield pylons (Radius: {RECEPTACLE_RADIUS_CM} cm)...")
    for s_idx in range(STAMEN_COUNT):
        az_deg = (360.0 / STAMEN_COUNT) * s_idx
        az_rad = math.radians(az_deg)
        x = RECEPTACLE_RADIUS_CM * math.cos(az_rad)
        y = RECEPTACLE_RADIUS_CM * math.sin(az_rad)
        z = 1200.0 # 12m = 1200 cm elevated deck

        all_points.append({
            "id": len(all_points),
            "component": "StamenPylon",
            "petal_index": -1,
            "zone_tag": "ZONE_CORE_CITADEL",
            "faculty_name": "Barrier Defense Forcefield Ring",
            "u": 0.0,
            "v": 0.0,
            "x_cm": round(x, 2),
            "y_cm": round(y, 2),
            "z_cm": round(z, 2),
            "x_m": round(x / 100.0, 3),
            "y_m": round(y / 100.0, 3),
            "z_m": round(z / 100.0, 3),
            "radial_distance_cm": round(RECEPTACLE_RADIUS_CM, 2),
            "angle_deg": round(az_deg, 2),
            "clearance_gap_cm": 0.0,
            "clearance_gap_m": 0.0,
            "nx": round(-math.cos(az_rad) * 0.24, 4),
            "ny": round(-math.sin(az_rad) * 0.24, 4),
            "nz": 0.97,
            "target_buoyancy_kn": 0.0,
            "subcouncil": 0
        })

    # 3. Central Receptacle & Council of Ten Apex Spire (Height: 35,000 cm = 350m)
    print(f"[*] Generating Council of Ten Citadel & Apex Spire (Spire Height: {APEX_SPIRE_HEIGHT_CM} cm)...")
    citadel_rings = 5
    for ring_i in range(1, citadel_rings + 1):
        r = (ring_i / float(citadel_rings)) * (RECEPTACLE_RADIUS_CM * 0.85)
        pts_in_ring = 8 * ring_i
        for pt_i in range(pts_in_ring):
            ang_deg = (360.0 / pts_in_ring) * pt_i
            ang_rad = math.radians(ang_deg)
            x = r * math.cos(ang_rad)
            y = r * math.sin(ang_rad)
            z = 1500.0 # 15m = 1500 cm

            all_points.append({
                "id": len(all_points),
                "component": "CitadelDeck",
                "petal_index": -1,
                "zone_tag": "ZONE_CORE_CITADEL",
                "faculty_name": "Grand Academic Citadel & Assembly Plaza",
                "u": round(ring_i / float(citadel_rings), 4),
                "v": round(pt_i / float(pts_in_ring), 4),
                "x_cm": round(x, 2),
                "y_cm": round(y, 2),
                "z_cm": round(z, 2),
                "x_m": round(x / 100.0, 3),
                "y_m": round(y / 100.0, 3),
                "z_m": round(z / 100.0, 3),
                "radial_distance_cm": round(r, 2),
                "angle_deg": round(ang_deg, 2),
                "clearance_gap_cm": 0.0,
                "clearance_gap_m": 0.0,
                "nx": 0.0,
                "ny": 0.0,
                "nz": 1.0,
                "target_buoyancy_kn": 0.0,
                "subcouncil": 0
            })

    # Council Apex Chamber Point
    all_points.append({
        "id": len(all_points),
        "component": "ApexSpire",
        "petal_index": -1,
        "zone_tag": "ZONE_CORE_CITADEL",
        "faculty_name": "Council of Ten Sovereign Spire Apex",
        "u": 0.0,
        "v": 0.0,
        "x_cm": 0.0,
        "y_cm": 0.0,
        "z_cm": APEX_SPIRE_HEIGHT_CM,
        "x_m": 0.0,
        "y_m": 0.0,
        "z_m": round(APEX_SPIRE_HEIGHT_CM / 100.0, 3),
        "radial_distance_cm": 0.0,
        "angle_deg": 0.0,
        "clearance_gap_cm": 0.0,
        "clearance_gap_m": 0.0,
        "nx": 0.0,
        "ny": 0.0,
        "nz": 1.0,
        "target_buoyancy_kn": 0.0,
        "subcouncil": 0
    })

    # 4. 12 Telescopic Expanding Underwater Ballast Rings
    print(f"[*] Generating {RING_TIER_COUNT} expanding underwater ballast rings ({TOTAL_SUBMERGED_DEPTH_CM} cm depth)...")
    for tier in range(RING_TIER_COUNT):
        norm_t = tier / float(RING_TIER_COUNT - 1)
        depth_z = norm_t * TOTAL_SUBMERGED_DEPTH_CM
        ring_r = calculate_submerged_radius(depth_z)
        pressure_bar = 1.0 + (abs(depth_z) / 100.0 * 0.10055)
        zone_tag = "ZONE_ROOT_VAULT" if norm_t > 0.85 else "ZONE_STEM_TELESCOPIC"

        for a_i in range(RING_ANGULAR_RES):
            ang_deg = (360.0 / RING_ANGULAR_RES) * a_i
            ang_rad = math.radians(ang_deg)
            x = ring_r * math.cos(ang_rad)
            y = ring_r * math.sin(ang_rad)

            all_points.append({
                "id": len(all_points),
                "component": "SubmergedRing",
                "petal_index": -1,
                "zone_tag": zone_tag,
                "faculty_name": f"Submerged Ballast Tier {tier + 1}",
                "u": round(norm_t, 4),
                "v": round(a_i / float(RING_ANGULAR_RES), 4),
                "x_cm": round(x, 2),
                "y_cm": round(y, 2),
                "z_cm": round(depth_z, 2),
                "x_m": round(x / 100.0, 3),
                "y_m": round(y / 100.0, 3),
                "z_m": round(depth_z / 100.0, 3),
                "radial_distance_cm": round(ring_r, 2),
                "angle_deg": round(ang_deg, 2),
                "clearance_gap_cm": round(pressure_bar, 2), # Stored pressure
                "clearance_gap_m": round(pressure_bar, 2),
                "nx": round(math.cos(ang_rad), 4),
                "ny": round(math.sin(ang_rad), 4),
                "nz": 0.0,
                "target_buoyancy_kn": -80000.0 if norm_t <= 0.85 else -150000.0,
                "subcouncil": 0
            })

    print("--------------------------------------------------------------------------------")
    print(f"[+] Total PCG Points Generated: {len(all_points):,}")
    print(f"[+] Minimum Waterway Clearance: {min_observed_clearance_cm:.2f} cm ({min_observed_clearance_cm/100:.2f} m)")
    print(f"[+] Waterway Clearance Safety Violations: {clearance_violations}")
    print(f"[+] Radius Range: Citadel = {RECEPTACLE_RADIUS_CM:,.0f} cm  -->  Petal Tips = 110,000 cm")
    print(f"[+] Underwater Flare: Neck = {SURFACE_NECK_RADIUS_CM:,.0f} cm  -->  Seabed = {SEABED_ABYSSAL_RADIUS_CM:,.0f} cm")
    print("--------------------------------------------------------------------------------")
    return all_points

# endregion

# region EXPORT

def export_datasets(points, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    json_path = os.path.join(output_dir, "istrorigan_lattice.json")
    csv_ue_path = os.path.join(output_dir, "istrorigan_lattice.csv")
    csv_m_path = os.path.join(output_dir, "istrorigan_lattice_meters.csv")

    # 1. JSON Export (Full precision with both cm and meters)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "city_name": "Istrorigan",
            "year": 4205,
            "units": "Centimeters (Unreal Units, 1 UU = 1 cm)",
            "petal_count": PETAL_COUNT,
            "min_waterway_clearance_cm": MIN_WATERWAY_CLEARANCE_CM,
            "base_radius_cm": BASE_INNER_RADIUS_CM,
            "max_petal_radius_cm": 110000.0,
            "total_points": len(points),
            "points": points
        }, f, indent=2)
    print(f"[+] Exported Master JSON Lattice (Calibrated UE5): {json_path}")

    # 2. CSV for Unreal Engine PCG Data Table (in Centimeters)
    fieldnames_ue = [
        "id", "component", "petal_index", "zone_tag", "faculty_name",
        "u", "v", "x_cm", "y_cm", "z_cm", "radial_distance_cm",
        "angle_deg", "clearance_gap_cm", "nx", "ny", "nz",
        "target_buoyancy_kn", "subcouncil"
    ]
    with open(csv_ue_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames_ue, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(points)
    print(f"[+] Exported UE5 PCG DataTable CSV (Centimeters): {csv_ue_path}")

    # 3. CSV for DCC / Houdini (in Meters)
    fieldnames_m = [
        "id", "component", "petal_index", "zone_tag", "faculty_name",
        "u", "v", "x_m", "y_m", "z_m", "clearance_gap_m",
        "nx", "ny", "nz", "subcouncil"
    ]
    with open(csv_m_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames_m, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(points)
    print(f"[+] Exported DCC / Houdini CSV (Meters):          {csv_m_path}")


def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root_dir, "output")
    points = generate_istrorigan_dataset()
    export_datasets(points, out_dir)


if __name__ == "__main__":
    main()
# endregion
