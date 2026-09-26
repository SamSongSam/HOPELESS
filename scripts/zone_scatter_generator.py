#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN ZONE SCATTER & PROP GENERATOR (YEAR 4205)
================================================================================
Implements 03_MEGASTRUCTURE/03_04_ZONES_AND_SCATTER.md:
- Jittered Poisson-Disk Micro-Scatter across 8 Petals and Receptacle Promenade
- Prop Archetypes:
    1. Bioluminescent Algae Light Columns (Night/Submerged illumination)
    2. Hexagonal Solar Pavement Tiles (Clean energy collection)
    3. Waterway Clearance Floating Marker Buoys (Warning lights for 45m channels)
    4. Harbor Docking Clamps & Submersible Winches (Outer tip berths)
    5. Atmospheric Re-breather Emergency Booths
================================================================================
Usage:
    py scripts/zone_scatter_generator.py
Outputs:
    output/istrorigan_scatter_props.json
    output/istrorigan_scatter_props.csv
================================================================================
"""

# region MODULE IMPORTS & PROP CATALOG
import os
import sys
import math
import json
import csv
import random

PROP_CATALOG = {
    "FACULTY": [
        {"mesh": "SM_Prop_BioLight_Column_01", "weight": 40, "scale_range": (0.9, 1.2), "z_offset_cm": 0.0},
        {"mesh": "SM_Prop_AtmosphereBooth_01", "weight": 20, "scale_range": (1.0, 1.0), "z_offset_cm": 0.0},
        {"mesh": "SM_Prop_SolarGlassPavement_Tile", "weight": 40, "scale_range": (1.0, 1.0), "z_offset_cm": 5.0}
    ],
    "TRANSIT": [
        {"mesh": "SM_Prop_Transit_InfoKiosk", "weight": 35, "scale_range": (1.0, 1.0), "z_offset_cm": 0.0},
        {"mesh": "SM_Prop_MaglevGuideLight_Line", "weight": 45, "scale_range": (0.9, 1.1), "z_offset_cm": 10.0},
        {"mesh": "SM_Prop_SecurityDrone_Dock", "weight": 20, "scale_range": (0.8, 1.0), "z_offset_cm": 250.0}
    ],
    "HARBOR": [
        {"mesh": "SM_Prop_Harbor_Bollard_Heavy", "weight": 50, "scale_range": (1.0, 1.3), "z_offset_cm": 0.0},
        {"mesh": "SM_Prop_Submersible_MooringClamp", "weight": 30, "scale_range": (1.0, 1.1), "z_offset_cm": -50.0},
        {"mesh": "SM_Prop_OceanSensorBeacon", "weight": 20, "scale_range": (0.8, 1.2), "z_offset_cm": 0.0}
    ],
    "WATERWAY": [
        {"mesh": "SM_Prop_Waterway_WarningBuoy_Luminescent", "weight": 100, "scale_range": (1.0, 1.4), "z_offset_cm": -100.0}
    ],
    "CORE": [
        {"mesh": "SM_Prop_Council_MemorialPylon", "weight": 30, "scale_range": (1.0, 1.5), "z_offset_cm": 0.0},
        {"mesh": "SM_Prop_Civic_Holosphere_Projector", "weight": 30, "scale_range": (1.0, 1.0), "z_offset_cm": 50.0},
        {"mesh": "SM_Prop_Promenade_IlluminationRing", "weight": 40, "scale_range": (1.0, 1.2), "z_offset_cm": 0.0}
    ]
}
# endregion


# region POISSON-DISK ZONE SCATTER ENGINE
def scatter_props(lattice_json_path):
    print("[*] Generating Micro-Scatter Props across Istrorigan zones (Centimeters)...")
    with open(lattice_json_path, "r", encoding="utf-8") as f:
        lattice_data = json.load(f)

    points = lattice_data.get("points", [])
    props = []
    random.seed(9999)

    for pt in points:
        zone_tag = pt.get("zone_tag", pt.get("zone", ""))
        
        if "WATERWAY" in zone_tag:
            category = "WATERWAY"
            if pt["id"] % 5 != 0: continue
        elif "CORE" in zone_tag:
            category = "CORE"
            if pt["id"] % 2 != 0: continue
        elif "HARBOR" in zone_tag:
            category = "HARBOR"
        elif "FACULTY" in zone_tag:
            category = "FACULTY"
            if pt["id"] % 2 == 0: continue
        else:
            continue

        catalog = PROP_CATALOG.get(category)
        if not catalog:
            continue

        # Select prop based on weighted random
        weights = [item["weight"] for item in catalog]
        chosen_item = random.choices(catalog, weights=weights, k=1)[0]

        # Jitter position slightly within cell (cm)
        jx = random.uniform(-400.0, 400.0)
        jy = random.uniform(-400.0, 400.0)
        rot_yaw = random.uniform(0.0, 360.0)
        scale_val = random.uniform(chosen_item["scale_range"][0], chosen_item["scale_range"][1])

        base_x = pt.get("x_cm", pt.get("x", 0.0))
        base_y = pt.get("y_cm", pt.get("y", 0.0))
        base_z = pt.get("z_cm", pt.get("z", 0.0))

        props.append({
            "prop_id": len(props) + 1,
            "anchor_id": pt["id"],
            "zone_tag": zone_tag,
            "mesh": chosen_item["mesh"],
            "x_cm": round(base_x + jx, 2),
            "y_cm": round(base_y + jy, 2),
            "z_cm": round(base_z + chosen_item["z_offset_cm"], 2),
            "yaw_deg": round(rot_yaw, 1),
        })

    print(f"[+] Successfully scattered {len(props):,} micro-props across all 8 petals & core.")
    return props
# endregion


# region JSON & CSV EXPORTERS
def export_props(props, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    json_path = os.path.join(output_dir, "istrorigan_scatter_props.json")
    csv_path = os.path.join(output_dir, "istrorigan_scatter_props.csv")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_props": len(props),
            "props": props
        }, f, indent=2)
    print(f"[+] Exported Scatter Props JSON: {json_path}")

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["prop_id", "anchor_id", "zone_tag", "mesh", "x_cm", "y_cm", "z_cm", "yaw_deg", "scale"])
        writer.writeheader()
        writer.writerows(props)
    print(f"[+] Exported Scatter Props CSV:  {csv_path}")
# endregion


# region MAIN ENTRY
def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lattice_path = os.path.join(root_dir, "output", "istrorigan_lattice.json")
    out_dir = os.path.join(root_dir, "output")

    if not os.path.exists(lattice_path):
        print(f"[!] Master lattice missing: {lattice_path}. Run istrorigan_pcg_generator.py first.")
        sys.exit(1)

    props = scatter_props(lattice_path)
    export_props(props, out_dir)


if __name__ == "__main__":
    main()
# endregion
