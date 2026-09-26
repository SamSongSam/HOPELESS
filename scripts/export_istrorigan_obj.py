#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN MEGASTRUCTURE 3D OBJ EXPORTER (YEAR 4205)
================================================================================
Assembles and exports the complete master 3D mesh for the Istrorigan Megastructure:
- All 16 Canonical Subsystems (Parts 01 to 16)
- 8 Distinct Academic Faculty Petals with 45m Waterway Clearances
- Central Citadel Receptacle Plaza & +600m Twin-Blade Apex Spire
- 70 Golden Stamen Forcefield Pylon Towers
- 1,280 Modular Buildings (All 7,623 Stacked Floors from CSV)
- Botanical Bio-Domes, Canal Skybridges, Outer Floating Marina Docks
- 12 Submerged Telescopic Rings, Inter-Ring Hydraulics & Collar
- Abyssal Doomsday Vault & Bedrock Claws (-1,000m)
- Vertical Deep-Sea Elevator Core & Emergency Bulkhead Gates
================================================================================
Exports:
    output/istrorigan_flower_city_ue_cm.obj      (Unreal Engine Centimeters, 1 UU = 1 cm)
    output/istrorigan_flower_city_dcc_meters.obj (Standard DCC Meters: Houdini/Blender)
================================================================================
"""

# region MODULE IMPORTS & PATH CONFIG
import os
import sys

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "output")
PARTS_DIR = os.path.join(OUTPUT_DIR, "parts")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PARTS_DIR, exist_ok=True)

# List of all 16 canonical subsystems in assembly order
SUBSYSTEM_PARTS = [
    ("01_SYS_APEX_SPIRE", "01_SYS_APEX_SPIRE.obj"),
    ("02_SYS_HEX_BARRIER", "02_SYS_HEX_BARRIER.obj"),
    ("03_SYS_ACADEMIC_PETALS_8X", "03_SYS_ACADEMIC_PETALS_8X.obj"),
    ("04_SYS_BIO_DOMES", "04_SYS_BIO_DOMES.obj"),
    ("05_SYS_STAMEN_PYLONS", "05_SYS_STAMEN_PYLONS.obj"),
    ("06_SYS_CANAL_BRIDGES", "06_SYS_CANAL_BRIDGES.obj"),
    ("07_SYS_OUTER_FLOATING_DOCK", "07_SYS_OUTER_FLOATING_DOCK.obj"),
    ("08_SYS_STEM_RINGS", "08_SYS_STEM_RINGS.obj"),
    ("09_SYS_SEABED_VAULT", "09_SYS_SEABED_VAULT.obj"),
    ("10_SYS_TRANSIT_CONDUITS", "10_SYS_TRANSIT_CONDUITS.obj"),
    ("11_SYS_CORE_STEM_COLLAR", "11_SYS_CORE_STEM_COLLAR.obj"),
    ("12_SYS_INTER_RING_HYDRAULICS", "12_SYS_INTER_RING_HYDRAULICS.obj"),
    ("13_SYS_DEEPSEA_ELEVATOR_CORE", "13_SYS_DEEPSEA_ELEVATOR_CORE.obj"),
    ("14_SYS_EMERGENCY_BULKHEAD_GATES", "14_SYS_EMERGENCY_BULKHEAD_GATES.obj"),
    ("15_SYS_SUBCOUNCIL_HALLS_8X", "15_SYS_SUBCOUNCIL_HALLS_8X.obj"),
    ("16_SYS_MODULAR_BUILDINGS", "16_SYS_MODULAR_BUILDINGS.obj"),
]
# endregion


# region OBJ PARSER
def parse_obj_file(filepath):
    """Parses standard Wavefront OBJ file into vertices, normals, uvs, and faces."""
    verts = []
    normals = []
    uvs = []
    faces = []

    if not os.path.exists(filepath):
        return verts, normals, uvs, faces

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            tokens = line.split()
            cmd = tokens[0]
            if cmd == "v":
                verts.append((float(tokens[1]), float(tokens[2]), float(tokens[3])))
            elif cmd == "vn":
                normals.append((float(tokens[1]), float(tokens[2]), float(tokens[3])))
            elif cmd == "vt":
                uvs.append((float(tokens[1]), float(tokens[2])))
            elif cmd == "f":
                face_items = []
                for tok in tokens[1:]:
                    parts = tok.split("/")
                    v_idx = int(parts[0]) if parts[0] else 0
                    vt_idx = int(parts[1]) if len(parts) > 1 and parts[1] else 0
                    vn_idx = int(parts[2]) if len(parts) > 2 and parts[2] else 0
                    face_items.append((v_idx, vt_idx, vn_idx))
                faces.append(face_items)

    return verts, normals, uvs, faces
# endregion


# region MASTER OBJ COMPILER
def compile_master_obj(output_filepath, scale_factor=1.0, is_ue=False):
    """
    Compiles all 16 canonical subsystems into a single master Wavefront OBJ file
    with separate 'o' and 'g' group headers for each component.
    """
    unit_str = "Centimeters (1 UU = 1 cm)" if is_ue else "Meters (1 unit = 1 m)"
    print(f"[*] Compiling Master Flower City OBJ: {os.path.basename(output_filepath)} [{unit_str}]...")

    total_v = 0
    total_vt = 0
    total_vn = 0
    total_faces = 0

    with open(output_filepath, "w", encoding="utf-8") as out:
        out.write("# ================================================================================\n")
        out.write("# ISTRORIGAN MEGASTRUCTURE - COMPLETE FLOWER CITY 3D MODEL (YEAR 4205)\n")
        out.write(f"# Units: {unit_str}\n")
        out.write("# Components: All 16 Canonical Subsystems & 7,623 Modular Building Floors\n")
        out.write("# ================================================================================\n\n")

        for group_name, part_filename in SUBSYSTEM_PARTS:
            part_path = os.path.join(PARTS_DIR, part_filename)
            p_verts, p_normals, p_uvs, p_faces = parse_obj_file(part_path)

            if not p_verts:
                print(f"    [WARN] Subsystem missing: {part_filename}, skipping.")
                continue

            out.write(f"o {group_name}\n")
            out.write(f"g {group_name}\n")
            out.write("s 1\n")

            # Write Vertices
            for vx, vy, vz in p_verts:
                out.write(f"v {vx * scale_factor:.4f} {vy * scale_factor:.4f} {vz * scale_factor:.4f}\n")

            # Write UVs
            for u, v in p_uvs:
                out.write(f"vt {u:.4f} {v:.4f}\n")

            # Write Normals
            for nx, ny, nz in p_normals:
                out.write(f"vn {nx:.4f} {ny:.4f} {nz:.4f}\n")

            # Write Faces with global 1-based index offsets
            for face in p_faces:
                f_tokens = []
                for v_idx, vt_idx, vn_idx in face:
                    new_v = v_idx + total_v if v_idx > 0 else v_idx
                    if vt_idx > 0 and vn_idx > 0:
                        new_vt = vt_idx + total_vt
                        new_vn = vn_idx + total_vn
                        f_tokens.append(f"{new_v}/{new_vt}/{new_vn}")
                    elif vn_idx > 0:
                        new_vn = vn_idx + total_vn
                        f_tokens.append(f"{new_v}//{new_vn}")
                    elif vt_idx > 0:
                        new_vt = vt_idx + total_vt
                        f_tokens.append(f"{new_v}/{new_vt}")
                    else:
                        f_tokens.append(f"{new_v}")
                out.write(f"f {' '.join(f_tokens)}\n")

            out.write("\n")
            total_v += len(p_verts)
            total_vt += len(p_uvs)
            total_vn += len(p_normals)
            total_faces += len(p_faces)
            print(f"    [+] Embedded {group_name:<32} ({len(p_verts):,} verts, {len(p_faces):,} faces)")

    size_bytes = os.path.getsize(output_filepath)
    print(f"[+] Successfully Exported Master OBJ: {output_filepath}")
    print(f"    Total: {total_v:,} vertices, {total_faces:,} polygons, {size_bytes:,} bytes\n")
    return total_v, total_faces
# endregion


# region MAIN DISPATCHER
def main():
    # 1. Ensure all individual modular parts are up-to-date
    import export_modular_parts_obj
    export_modular_parts_obj.export_all()

    # 2. Export in Unreal Engine Centimeters (1 UU = 1 cm)
    ue_obj_path = os.path.join(OUTPUT_DIR, "istrorigan_flower_city_ue_cm.obj")
    compile_master_obj(ue_obj_path, scale_factor=100.0, is_ue=True)

    # 3. Export in Standard DCC Meters (Houdini, Blender, Maya)
    dcc_obj_path = os.path.join(OUTPUT_DIR, "istrorigan_flower_city_dcc_meters.obj")
    compile_master_obj(dcc_obj_path, scale_factor=1.0, is_ue=False)


if __name__ == "__main__":
    main()
# endregion
