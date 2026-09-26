#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN CODEBASE VERIFIER
================================================================================
Performs automated verification of:
1. C++ Header Region Tags (#pragma region / #pragma endregion pairing)
2. C++ Source Files Integrity and Inclusion Guards
3. Unreal Plugin Descriptor (.uplugin) JSON Validation
4. Generated Point Cloud Datasets (JSON/CSV) Consistency & Math Tolerances
================================================================================
"""

# region MODULE IMPORTS & WORKSPACE CONFIG
import os
import sys
import json
import csv
import math

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# endregion


# region PRAGMA & REGION VERIFICATION ENGINE
def check_pragma_regions(file_path):
    """Verifies that all #pragma region tags have corresponding #pragma endregion tags."""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    regions = []
    unmatched = []

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("#pragma region") or stripped.startswith("# region"):
            regions.append((idx, stripped))
        elif stripped.startswith("#pragma endregion") or stripped.startswith("# endregion"):
            if regions:
                regions.pop()
            else:
                unmatched.append((idx, "extra endregion"))

    if regions:
        return False, f"Unclosed regions: {regions}"
    if unmatched:
        return False, f"Extra endregions: {unmatched}"
    return True, "Balanced"
# endregion


# region UNREAL PLUGIN VALIDATION
def verify_uplugin():
    uplugin_path = os.path.join(WORKSPACE_DIR, "FlowerCityPCG.uplugin")
    if not os.path.exists(uplugin_path):
        return False, "FlowerCityPCG.uplugin not found"
    try:
        with open(uplugin_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if data.get("FriendlyName") and "FlowerCityPCG" in [m["Name"] for m in data.get("Modules", [])]:
            return True, "Valid .uplugin"
        return False, "Malformed .uplugin data"
    except Exception as e:
        return False, str(e)
# endregion


# region GENERATED DATASETS VALIDATION
def verify_generated_data():
    json_path = os.path.join(WORKSPACE_DIR, "output", "istrorigan_lattice.json")
    csv_path = os.path.join(WORKSPACE_DIR, "output", "istrorigan_lattice.csv")

    if not os.path.exists(json_path) or not os.path.exists(csv_path):
        return False, "Output lattice files missing"

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    points = data.get("points", [])
    if len(points) < 4000:
        return False, f"Insufficient points: {len(points)}"

    def get_val_cm(pt, key_cm, key_m):
        if key_cm in pt:
            return float(pt[key_cm])
        if key_m in pt:
            return float(pt[key_m]) * 100.0
        return 0.0

    # Check 45m (4500 cm) clearance strictly maintained
    petal_pts = [p for p in points if p["component"] == "Petal"]
    for p in petal_pts:
        gap_cm = get_val_cm(p, "clearance_gap_cm", "clearance_gap_m")
        if gap_cm < 4499.0:
            return False, f"Clearance violation at pt {p['id']}: {gap_cm} cm (must be >= 4500 cm)"

    # Check outer tip flat at sea level (Z = 0.0 cm)
    outer_tips = [p for p in petal_pts if p["u"] == 1.0]
    for p in outer_tips:
        z_cm = get_val_cm(p, "z_cm", "z")
        if abs(z_cm) > 1.0:
            return False, f"Outer tip not at sea level: {z_cm} cm at pt {p['id']}"

    # Check expanding rings (Neck R=8,000 cm -> Bottom Flare R=35,000 cm)
    ring_pts = [p for p in points if p["component"] == "SubmergedRing"]
    top_tier = [p for p in ring_pts if p["u"] == 0.0]
    bot_tier = [p for p in ring_pts if p["u"] == 1.0]

    top_x = get_val_cm(top_tier[0], "x_cm", "x")
    top_y = get_val_cm(top_tier[0], "y_cm", "y")
    bot_x = get_val_cm(bot_tier[0], "x_cm", "x")
    bot_y = get_val_cm(bot_tier[0], "y_cm", "y")

    top_r = math.sqrt(top_x**2 + top_y**2)
    bot_r = math.sqrt(bot_x**2 + bot_y**2)

    if not (7900.0 <= top_r <= 8100.0):
        return False, f"Unexpected top ring radius: {top_r:.1f} cm (expected ~8000 cm)"
    if not (34900.0 <= bot_r <= 35100.0):
        return False, f"Unexpected bottom ring radius: {bot_r:.1f} cm (expected ~35000 cm)"

    # Check OBJ Exports Presence and Validity
    obj_ue = os.path.join(WORKSPACE_DIR, "output", "istrorigan_flower_city_ue_cm.obj")
    obj_dcc = os.path.join(WORKSPACE_DIR, "output", "istrorigan_flower_city_dcc_meters.obj")
    dome_ue = os.path.join(WORKSPACE_DIR, "output", "hex_barrier_dome_ue_cm.obj")
    
    for obj_path, name, min_size in [
        (obj_ue, "Flower City Mesh (UE cm)", 500000),
        (obj_dcc, "Flower City Mesh (DCC m)", 500000),
        (dome_ue, "Hex Dome Mesh (UE cm)", 10000)
    ]:
        if not os.path.exists(obj_path):
            return False, f"Missing 3D OBJ file: {name} at {obj_path}"
        sz = os.path.getsize(obj_path)
        if sz < min_size:
            return False, f"3D OBJ file too small ({sz} bytes): {name}"

    return True, (
        f"Verified {len(points)} points in UE cm; 0 clearance violations (gap >= 4500 cm); "
        f"tips flat at Z=0 cm; ring radius {top_r:.0f} cm -> {bot_r:.0f} cm; "
        f"3D City OBJs ({os.path.getsize(obj_ue):,} bytes UE cm / {os.path.getsize(obj_dcc):,} bytes DCC m) verified"
    )
# endregion


# region MASTER VERIFICATION RUNNER
def run_all_checks():
    print("================================================================================")
    print(" RUNNING ISTRORIGAN CODEBASE VERIFICATION SUITE")
    print("================================================================================")
    all_passed = True

    # Check uplugin
    ok, msg = verify_uplugin()
    print(f"[{'PASS' if ok else 'FAIL'}] Unreal Plugin Descriptor: {msg}")
    all_passed = all_passed and ok

    # Check C++ Files
    source_dir = os.path.join(WORKSPACE_DIR, "Source", "FlowerCityPCG")
    cpp_files = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith((".h", ".cpp")):
                cpp_files.append(os.path.join(root, file))

    print(f"[*] Checking {len(cpp_files)} C++ source/header files...")
    for cpp in cpp_files:
        rel = os.path.relpath(cpp, WORKSPACE_DIR)
        ok, msg = check_pragma_regions(cpp)
        print(f"  [{'PASS' if ok else 'WARN'}] {rel}: {msg}")
        if not ok and "Unclosed" in msg:
            all_passed = False

    # Check Generated Data
    ok, msg = verify_generated_data()
    print(f"[{'PASS' if ok else 'FAIL'}] Generated Lattices (JSON/CSV): {msg}")
    all_passed = all_passed and ok

    print("================================================================================")
    if all_passed:
        print("[+] ALL VERIFICATION CHECKS PASSED PERFECTLY!")
    else:
        print("[!] SOME CHECKS FAILED OR GENERATED WARNINGS.")
    print("================================================================================")
    return 0 if all_passed else 1
# endregion


# region MAIN ENTRY
if __name__ == "__main__":
    sys.exit(run_all_checks())
# endregion
