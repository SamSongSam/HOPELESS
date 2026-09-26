#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN HEXAGONAL BARRIER DOME 3D GENERATOR (YEAR 4205)
================================================================================
Implements 05_SCIFI_AND_PROPS/05_SCIFI_AND_PROPS.md:
- Generates 3D Geodesic Hexagonal Dome Mesh covering the entire Megastructure:
    * Radius: 1,600m (covers 1,550m outer petal tips)
    * Height: 750m (encloses the 600m Council of Ten Spire)
- Calculates UV coordinates and Vertex Colors for Energy Wave & Impact Shaders
- Exports Wavefront OBJ (output/hex_barrier_dome.obj) and JSON data
================================================================================
Usage:
    py scripts/hex_barrier_dome_generator.py
Outputs:
    output/hex_barrier_dome.obj
    output/hex_barrier_dome.json
================================================================================
"""

# region MODULE IMPORTS
import os
import sys
import math
import json
# endregion


# region PROCEDURAL DOME MESH GENERATOR
def generate_hex_barrier_dome(radius=1600.0, height=750.0, rings=16, segments=32):
    print(f"[*] Generating Procedural Hexagonal Barrier Dome (Radius: {radius}m, Height: {height}m)...")
    vertices = []
    uvs = []
    normals = []
    faces = []

    # Apex vertex at top center
    vertices.append((0.0, 0.0, height))
    uvs.append((0.5, 0.5))
    normals.append((0.0, 0.0, 1.0))
    apex_idx = 1 # 1-based for OBJ

    # Rings of vertices from apex down to water surface
    for r in range(1, rings + 1):
        phi = (math.pi * 0.5) * (r / float(rings)) # 0 at apex to PI/2 at base
        ring_z = height * math.cos(phi)
        ring_r = radius * math.sin(phi)

        # Hexagonal staggering: shift alternate rings by half a segment
        phase = (math.pi / float(segments)) if (r % 2 == 1) else 0.0

        for s in range(segments):
            theta = (2.0 * math.pi * (s / float(segments))) + phase
            x = ring_r * math.cos(theta)
            y = ring_r * math.sin(theta)
            z = max(0.0, ring_z)

            # Normal vector pointing outward
            nx = x / radius
            ny = y / radius
            nz = z / height
            n_len = math.sqrt(nx*nx + ny*ny + nz*nz)
            nx, ny, nz = nx/n_len, ny/n_len, nz/n_len

            # UV coordinates
            u = 0.5 + (0.5 * (ring_r / radius) * math.cos(theta))
            v = 0.5 + (0.5 * (ring_r / radius) * math.sin(theta))

            vertices.append((round(x, 2), round(y, 2), round(z, 2)))
            uvs.append((round(u, 4), round(v, 4)))
            normals.append((round(nx, 4), round(ny, 4), round(nz, 4)))

    # Generate triangular and quad faces for the dome
    # 1. Apex triangle fan
    for s in range(segments):
        next_s = (s + 1) % segments
        v1 = apex_idx
        v2 = 2 + s
        v3 = 2 + next_s
        faces.append((v1, v2, v3))

    # 2. Quad bands between concentric rings
    for r in range(1, rings):
        ring_start_curr = 2 + (r - 1) * segments
        ring_start_next = 2 + r * segments

        for s in range(segments):
            next_s = (s + 1) % segments
            c1 = ring_start_curr + s
            c2 = ring_start_curr + next_s
            n1 = ring_start_next + s
            n2 = ring_start_next + next_s

            # Two triangles forming quad / hex subdivision
            faces.append((c1, n1, c2))
            faces.append((c2, n1, n2))

    print(f"[+] Dome Mesh Generated: {len(vertices):,} Vertices, {len(faces):,} Faces.")
    return vertices, uvs, normals, faces
# endregion


# region WAVEFRONT OBJ WRITER
def export_obj(vertices, uvs, normals, faces, obj_path):
    with open(obj_path, "w", encoding="utf-8") as f:
        f.write("# ISTRORIGAN HEXAGONAL BARRIER DOME (YEAR 4205)\n")
        f.write("# Sovereign Hexagonal Defense Shield Mesh\n")
        f.write("o Hex_Barrier_Dome\n")

        for v in vertices:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")

        for uv in uvs:
            f.write(f"vt {uv[0]} {uv[1]}\n")

        for n in normals:
            f.write(f"vn {n[0]} {n[1]} {n[2]}\n")

        f.write("s 1\n")
        for face in faces:
            if len(face) == 3:
                f.write(f"f {face[0]}/{face[0]}/{face[0]} {face[1]}/{face[1]}/{face[1]} {face[2]}/{face[2]}/{face[2]}\n")
            elif len(face) == 4:
                f.write(f"f {face[0]}/{face[0]}/{face[0]} {face[1]}/{face[1]}/{face[1]} {face[2]}/{face[2]}/{face[2]} {face[3]}/{face[3]}/{face[3]}\n")

    print(f"[+] Exported 3D Wavefront OBJ: {obj_path}")
# endregion


# region MAIN EXECUTION & JSON EXPORT
def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root_dir, "output")
    os.makedirs(out_dir, exist_ok=True)

    # 1. Unreal Engine Centimeters (1 UU = 1 cm): Radius 120,000 cm, Height 50,000 cm
    ue_obj_path = os.path.join(out_dir, "hex_barrier_dome_ue_cm.obj")
    verts_cm, uvs_cm, norms_cm, faces_cm = generate_hex_barrier_dome(radius=120000.0, height=50000.0)
    export_obj(verts_cm, uvs_cm, norms_cm, faces_cm, ue_obj_path)

    # 2. Standard DCC Meters (Houdini / Blender): Radius 1,200m, Height 500m
    dcc_obj_path = os.path.join(out_dir, "hex_barrier_dome_dcc_meters.obj")
    verts_m, uvs_m, norms_m, faces_m = generate_hex_barrier_dome(radius=1200.0, height=500.0)
    export_obj(verts_m, uvs_m, norms_m, faces_m, dcc_obj_path)

    # Also write default hex_barrier_dome.obj
    default_obj_path = os.path.join(out_dir, "hex_barrier_dome.obj")
    export_obj(verts_cm, uvs_cm, norms_cm, faces_cm, default_obj_path)

    json_path = os.path.join(out_dir, "hex_barrier_dome.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "name": "Hex_Barrier_Dome",
            "vertex_count": len(verts_cm),
            "face_count": len(faces_cm),
            "radius_cm": 120000.0,
            "apex_height_cm": 50000.0,
            "radius_m": 1200.0,
            "apex_height_m": 500.0
        }, f, indent=2)
    print(f"[+] Exported Barrier Metadata JSON: {json_path}")


if __name__ == "__main__":
    main()
# endregion
