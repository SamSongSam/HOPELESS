#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN MODULAR BUILDING ASSEMBLER (YEAR 4205)
================================================================================
Implements 02_ARCHITECTURE/02_MODULAR_ASSEMBLY.md & Kit-of-Parts Grammar:
- Reads lattice anchor points from output/istrorigan_lattice.json
- Stacks modular architectural components:
    1. FC_Building_Base (Slope-compensated foundation keeping floors horizontal)
    2. FC_Ground_Lobby (Airlock doors, transit terminals, pressurized gates)
    3. FC_Mid_Academic_Floors (Faculty labs, lecture chambers, quantum racks)
    4. FC_Roof_Dome (Bio-domes, observation platforms, drone ports)
- Enforces District Zoning height limits and mass/buoyancy budgets
================================================================================
Usage:
    py scripts/modular_building_assembler.py
Outputs:
    output/istrorigan_building_assemblies.json
    output/istrorigan_building_assemblies.csv
================================================================================
"""

import os
import sys
import math
import json
import csv
import random

# region ARCHITECTURAL KIT-OF-PARTS CATALOG

MODULE_CATALOG = {
    "Base_Foundation": {
        "mesh": "SM_FC_Foundation_SlopeCompensated_12x12",
        "height_m": 4.0,
        "mass_tons": 850.0,
        "buoyancy_kn": 1200.0,
        "is_watertight": True
    },
    "Ground_Lobby": {
        "mesh": "SM_FC_Ground_Lobby_Transit_12x12",
        "height_m": 6.0,
        "mass_tons": 450.0,
        "buoyancy_kn": 600.0,
        "is_watertight": True
    },
    "Academic_Lab_Floor": {
        "mesh": "SM_FC_Mid_Academic_Lab_12x12",
        "height_m": 4.0,
        "mass_tons": 320.0,
        "buoyancy_kn": 400.0,
        "is_watertight": True
    },
    "Faculty_Chamber_Floor": {
        "mesh": "SM_FC_Mid_Faculty_Chambers_12x12",
        "height_m": 4.0,
        "mass_tons": 280.0,
        "buoyancy_kn": 400.0,
        "is_watertight": True
    },
    "BioDome_Roof": {
        "mesh": "SM_FC_Roof_BioDome_12x12",
        "height_m": 8.0,
        "mass_tons": 180.0,
        "buoyancy_kn": 300.0,
        "is_watertight": True
    },
    "Solar_Observatory_Roof": {
        "mesh": "SM_FC_Roof_SolarObservatory_12x12",
        "height_m": 5.0,
        "mass_tons": 140.0,
        "buoyancy_kn": 250.0,
        "is_watertight": False
    },
    "Harbor_Docking_Pylon": {
        "mesh": "SM_FC_Harbor_Submersible_Berth",
        "height_m": 3.0,
        "mass_tons": 600.0,
        "buoyancy_kn": 900.0,
        "is_watertight": True
    }
}

# Max building height per zone in centimeters (matching DT_District_Zoning)
ZONE_HEIGHT_LIMITS = {
    "ZONE_CORE_CITADEL": 18000.0,       # 180m citadel spires (ARCH_CORE_COUNCIL_TEN_SPIRE)
    "ZONE_FACULTY_OCEANIC": 4500.0,     # 45m lab campuses
    "ZONE_FACULTY_BIOSPHERE": 4500.0,
    "ZONE_FACULTY_CLIMATE": 4500.0,
    "ZONE_FACULTY_MEGASTRUCT": 4500.0,
    "ZONE_FACULTY_ARCHIVES": 5000.0,
    "ZONE_FACULTY_ABYSSAL": 4500.0,
    "ZONE_FACULTY_DIPLOMACY": 4500.0,
    "ZONE_FACULTY_MEDICINE": 4500.0,
    "ZONE_HARBOR_BERTH": 1200.0,        # 12m low-profile harbor & marine berths
    "ZONE_CLEARANCE_WATERWAY": 0.0      # Strictly NO buildings in 45m waterways!
}

# Module catalog heights in centimeters
MODULE_CATALOG_CM = {
    "Base_Foundation": {
        "mesh": "SM_FC_Foundation_SlopeCompensated_12x12",
        "height_cm": 400.0,
        "mass_tons": 850.0,
        "buoyancy_kn": 1200.0,
        "is_watertight": True
    },
    "Ground_Lobby": {
        "mesh": "SM_FC_Ground_Lobby_Transit_12x12",
        "height_cm": 600.0,
        "mass_tons": 450.0,
        "buoyancy_kn": 600.0,
        "is_watertight": True
    },
    "Academic_Lab_Floor": {
        "mesh": "SM_FC_Mid_Academic_Lab_12x12",
        "height_cm": 400.0,
        "mass_tons": 320.0,
        "buoyancy_kn": 400.0,
        "is_watertight": True
    },
    "Faculty_Chamber_Floor": {
        "mesh": "SM_FC_Mid_Faculty_Chambers_12x12",
        "height_cm": 400.0,
        "mass_tons": 280.0,
        "buoyancy_kn": 400.0,
        "is_watertight": True
    },
    "BioDome_Roof": {
        "mesh": "SM_FC_Roof_BioDome_12x12",
        "height_cm": 800.0,
        "mass_tons": 180.0,
        "buoyancy_kn": 300.0,
        "is_watertight": True
    },
    "Solar_Observatory_Roof": {
        "mesh": "SM_FC_Roof_SolarObservatory_12x12",
        "height_cm": 500.0,
        "mass_tons": 140.0,
        "buoyancy_kn": 250.0,
        "is_watertight": False
    },
    "Harbor_Docking_Pylon": {
        "mesh": "SM_FC_Harbor_Submersible_Berth",
        "height_cm": 300.0,
        "mass_tons": 600.0,
        "buoyancy_kn": 900.0,
        "is_watertight": True
    }
}

# endregion

# region MODULAR ASSEMBLY SOLVER & STRUCTURAL CALCULATOR
def assemble_buildings(lattice_json_path):
    print("[*] Loading master lattice points for modular building assembly (Centimeters)...")
    with open(lattice_json_path, "r", encoding="utf-8") as f:
        lattice_data = json.load(f)

    points = lattice_data.get("points", [])
    candidate_points = [p for p in points if p["component"] in ("Petal", "CitadelDeck") and p.get("zone_tag") != "ZONE_CLEARANCE_WATERWAY"]

    # Sample anchor sites for modular buildings (skip waterways and avoid excessive density)
    sampled_anchors = [p for p in candidate_points if p["id"] % 3 == 0]
    print(f"[*] Identified {len(sampled_anchors)} anchor sites for modular structures.")

    assemblies = []
    total_modules_placed = 0
    total_mass_tons = 0.0
    total_buoyancy_kn = 0.0

    random.seed(4205) # Canon year seed

    for anchor in sampled_anchors:
        zone_tag = anchor.get("zone_tag", "ZONE_FACULTY_OCEANIC")
        max_height = ZONE_HEIGHT_LIMITS.get(zone_tag, 4500.0)
        if max_height <= 0.0:
            continue

        base_x = anchor.get("x_cm", anchor.get("x", 0.0))
        base_y = anchor.get("y_cm", anchor.get("y", 0.0))
        base_z = anchor.get("z_cm", anchor.get("z", 0.0))
        petal_idx = anchor["petal_index"]

        building_id = len(assemblies) + 1
        building_modules = []
        current_z_offset = 0.0

        # region 1. FOUNDATION BASE (SLOPE COMPENSATION)
        base_mod = MODULE_CATALOG_CM["Base_Foundation"]
        building_modules.append({
            "module_index": len(building_modules),
            "type": "Foundation",
            "mesh": base_mod["mesh"],
            "x_cm": base_x,
            "y_cm": base_y,
            "z_cm": round(base_z + current_z_offset, 2),
            "height_cm": base_mod["height_cm"],
            "mass_tons": base_mod["mass_tons"],
            "buoyancy_kn": base_mod["buoyancy_kn"],
            "pitch_compensation_deg": -2.5
        })
        current_z_offset += base_mod["height_cm"]
        # endregion

        # region 2. GROUND FLOOR & TRANSIT GATEWAYS
        if zone_tag == "ZONE_HARBOR_BERTH":
            g_mod = MODULE_CATALOG_CM["Harbor_Docking_Pylon"]
        else:
            g_mod = MODULE_CATALOG_CM["Ground_Lobby"]

        building_modules.append({
            "module_index": len(building_modules),
            "type": "GroundFloor",
            "mesh": g_mod["mesh"],
            "x_cm": base_x,
            "y_cm": base_y,
            "z_cm": round(base_z + current_z_offset, 2),
            "height_cm": g_mod["height_cm"],
            "mass_tons": g_mod["mass_tons"],
            "buoyancy_kn": g_mod["buoyancy_kn"],
            "pitch_compensation_deg": 0.0
        })
        current_z_offset += g_mod["height_cm"]
        # endregion

        # region 3. INTERMEDIATE ACADEMIC FLOORS
        allowed_floors = int((max_height - current_z_offset - 800.0) / 400.0)
        num_floors = max(0, min(allowed_floors, random.randint(1, 6)))

        for f_idx in range(num_floors):
            floor_type = "Academic_Lab_Floor" if (f_idx % 2 == 0) else "Faculty_Chamber_Floor"
            m_info = MODULE_CATALOG_CM[floor_type]
            building_modules.append({
                "module_index": len(building_modules),
                "type": "IntermediateFloor",
                "mesh": m_info["mesh"],
                "x_cm": base_x,
                "y_cm": base_y,
                "z_cm": round(base_z + current_z_offset, 2),
                "height_cm": m_info["height_cm"],
                "mass_tons": m_info["mass_tons"],
                "buoyancy_kn": m_info["buoyancy_kn"],
                "pitch_compensation_deg": 0.0
            })
            current_z_offset += m_info["height_cm"]
        # endregion

        # region 4. ROOF STRUCTURE & OBSERVATORIES
        roof_type = "BioDome_Roof" if (petal_idx % 2 == 0) else "Solar_Observatory_Roof"
        r_mod = MODULE_CATALOG_CM[roof_type]
        building_modules.append({
            "module_index": len(building_modules),
            "type": "Roof",
            "mesh": r_mod["mesh"],
            "x_cm": base_x,
            "y_cm": base_y,
            "z_cm": round(base_z + current_z_offset, 2),
            "height_cm": r_mod["height_cm"],
            "mass_tons": r_mod["mass_tons"],
            "buoyancy_kn": r_mod["buoyancy_kn"],
            "pitch_compensation_deg": 0.0
        })
        current_z_offset += r_mod["height_cm"]
        # endregion

        # region 5. STRUCTURAL MASS & BUOYANCY AGGREGATION
        b_mass = sum(m["mass_tons"] for m in building_modules)
        b_buoyancy = sum(m["buoyancy_kn"] for m in building_modules)
        total_mass_tons += b_mass
        total_buoyancy_kn += b_buoyancy
        total_modules_placed += len(building_modules)

        assemblies.append({
            "building_id": building_id,
            "anchor_lattice_id": anchor["id"],
            "petal_index": petal_idx,
            "zone_tag": zone_tag,
            "total_height_cm": round(current_z_offset, 2),
            "total_height_m": round(current_z_offset / 100.0, 2),
            "module_count": len(building_modules),
            "mass_tons": round(b_mass, 1),
            "buoyancy_kn": round(b_buoyancy, 1),
            "is_buoyant": b_buoyancy >= (b_mass * 9.81 / 10.0),
            "modules": building_modules
        })
        # endregion

    print(f"[+] Assembled {len(assemblies)} modular buildings ({total_modules_placed:,} individual modules).")
    print(f"[+] Total Structural Mass: {total_mass_tons:,.1f} Metric Tons | Buoyant Lift: {total_buoyancy_kn:,.1f} kN")
    return assemblies
# endregion


# region DATASET EXPORTERS (JSON & CSV)
def export_assemblies(assemblies, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    json_path = os.path.join(output_dir, "istrorigan_building_assemblies.json")
    csv_path = os.path.join(output_dir, "istrorigan_building_assemblies.csv")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_buildings": len(assemblies),
            "buildings": assemblies
        }, f, indent=2)
    print(f"[+] Exported Building Assemblies JSON: {json_path}")

    flat_modules = []
    for b in assemblies:
        for m in b["modules"]:
            flat_modules.append({
                "building_id": b["building_id"],
                "petal_index": b["petal_index"],
                "zone_tag": b["zone_tag"],
                "module_index": m["module_index"],
                "type": m["type"],
                "mesh": m["mesh"],
                "x_cm": m["x_cm"],
                "y_cm": m["y_cm"],
                "z_cm": m["z_cm"],
                "height_cm": m["height_cm"],
                "mass_tons": m["mass_tons"],
                "buoyancy_kn": m["buoyancy_kn"]
            })

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "building_id", "petal_index", "zone_tag", "module_index", "type", "mesh", "x_cm", "y_cm", "z_cm", "height_cm", "mass_tons", "buoyancy_kn"
        ])
        writer.writeheader()
        writer.writerows(flat_modules)
    print(f"[+] Exported Building Modules CSV:     {csv_path}")
# endregion


# region MAIN EXECUTION PIPELINE
def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lattice_path = os.path.join(root_dir, "output", "istrorigan_lattice.json")
    out_dir = os.path.join(root_dir, "output")

    if not os.path.exists(lattice_path):
        print(f"[!] Master lattice missing: {lattice_path}. Run istrorigan_pcg_generator.py first.")
        sys.exit(1)

    assemblies = assemble_buildings(lattice_path)
    export_assemblies(assemblies, out_dir)


if __name__ == "__main__":
    main()
# endregion

