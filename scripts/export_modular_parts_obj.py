#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN MEGASTRUCTURE - MODULAR 3D PARTS EXPORTER FOR HOUDINI & DCC
================================================================================
Exports all 9 canonical architectural parts as standalone 3D OBJ meshes:
  1. output/parts/01_SYS_APEX_SPIRE.obj
  2. output/parts/02_SYS_HEX_BARRIER.obj
  3. output/parts/03_SYS_ACADEMIC_PETAL_SINGLE.obj
  4. output/parts/03_SYS_ACADEMIC_PETALS_8X.obj
  5. output/parts/04_SYS_BIO_DOMES.obj
  6. output/parts/05_SYS_STAMEN_PYLONS.obj
  7. output/parts/06_SYS_CANAL_BRIDGES.obj
  8. output/parts/07_SYS_OUTER_FLOATING_DOCK.obj (Canon LOTUS_ACADEMY_CITY.jpg)
  9. output/parts/08_SYS_STEM_RINGS.obj
 10. output/parts/09_SYS_SEABED_VAULT.obj

Scales: Standard DCC Meters (1 unit = 1m) for native Houdini import.
================================================================================
"""

# region MODULE IMPORTS & CANONICAL DIMENSIONS
import os
import sys
import math

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "output", "parts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Canonical Dimensions (Meters)
PETAL_COUNT = 8
BASE_INNER_RADIUS_M = 150.0
PETAL_LENGTH_M = 950.0
PETAL_WIDTH_MAX_M = 420.0
MIN_WATERWAY_CLEARANCE_M = 45.0
RECEPTACLE_RADIUS_M = 150.0
APEX_SPIRE_HEIGHT_M = 600.0
CITADEL_BASE_HEIGHT_M = 120.0
STAMEN_COUNT = 70
STAMEN_HEIGHT_M = 45.0
RING_TIER_COUNT = 12
SURFACE_NECK_RADIUS_M = 80.0
SEABED_ABYSSAL_RADIUS_M = 350.0
TOTAL_SUBMERGED_DEPTH_M = -900.0
# endregion


# region OBJ FILE WRITER UTILITY
def write_obj_file(filepath, vertices, normals, uvs, faces, obj_name="mesh"):
    """Writes standard Wavefront OBJ file."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Istrorigan Megastructure Part: {obj_name}\n")
        f.write(f"# Exported for Houdini & DCC (Units: Meters)\n")
        f.write(f"o {obj_name}\n\n")

        for v in vertices:
            f.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
        f.write(f"# {len(vertices)} vertices\n\n")

        for vn in normals:
            f.write(f"vn {vn[0]:.4f} {vn[1]:.4f} {vn[2]:.4f}\n")
        f.write(f"# {len(normals)} normals\n\n")

        for vt in uvs:
            f.write(f"vt {vt[0]:.4f} {vt[1]:.4f}\n")
        f.write(f"# {len(uvs)} texture coords\n\n")

        f.write(f"s 1\n")
        for face in faces:
            # face elements are 1-indexed (v, vt, vn)
            tokens = [f"{idx[0]}/{idx[1]}/{idx[2]}" for idx in face]
            f.write(f"f {' '.join(tokens)}\n")
        f.write(f"# {len(faces)} polygons\n")
    print(f"  [+] Exported: {os.path.basename(filepath)} ({len(vertices)} verts, {len(faces)} polys)")
# endregion


# region PART 01: APEX SPIRE & CITADEL (SYS_01)
# -----------------------------------------------------------------------------
# PART 1: APEX SPIRE & CITADEL (SYS_01)
# -----------------------------------------------------------------------------
def export_part_01():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    # Base Receptacle Colonnade Plaza (Radius 150m, Height 120m)
    segs = 32
    rings = 6
    for ri in range(rings + 1):
        r_frac = ri / float(rings)
        r = 150.0 * (1.0 - 0.35 * r_frac)
        z = r_frac * CITADEL_BASE_HEIGHT_M
        for s in range(segs):
            th = 2.0 * math.pi * (s / float(segs))
            add_v(r * math.cos(th), r * math.sin(th), z, s / float(segs), r_frac, math.cos(th), math.sin(th), 0.2)

    for ri in range(rings):
        for s in range(segs):
            s_next = (s + 1) % segs
            v1 = ri * segs + s + 1
            v2 = ri * segs + s_next + 1
            v3 = (ri + 1) * segs + s_next + 1
            v4 = (ri + 1) * segs + s + 1
            faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    # Spire Shaft rising from 120m to 600m
    spire_base = len(verts)
    spire_rings = 16
    for si in range(spire_rings + 1):
        sf = si / float(spire_rings)
        sz = CITADEL_BASE_HEIGHT_M + sf * (APEX_SPIRE_HEIGHT_M - CITADEL_BASE_HEIGHT_M)
        sr = 45.0 * math.pow(1.0 - sf, 1.8) + 3.0  # slender taper
        for s in range(segs):
            th = 2.0 * math.pi * (s / float(segs))
            # Organic scalloped flute
            flute = 1.0 + 0.15 * math.cos(8 * th)
            r_flute = sr * flute
            add_v(r_flute * math.cos(th), r_flute * math.sin(th), sz, s / float(segs), sf, math.cos(th), math.sin(th), 0.1)

    for si in range(spire_rings):
        for s in range(segs):
            s_next = (s + 1) % segs
            v1 = spire_base + si * segs + s + 1
            v2 = spire_base + si * segs + s_next + 1
            v3 = spire_base + (si + 1) * segs + s_next + 1
            v4 = spire_base + (si + 1) * segs + s + 1
            faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    # Council of Ten Crown Observatory (Z = 540m to 580m)
    crown_base = len(verts)
    for c_i in range(5):
        cz = 530.0 + c_i * 12.0
        cr = 28.0 + 8.0 * math.sin(c_i * 0.7)
        for s in range(segs):
            th = 2.0 * math.pi * (s / float(segs))
            add_v(cr * math.cos(th), cr * math.sin(th), cz, s / float(segs), c_i / 4.0, math.cos(th), math.sin(th), 0.0)

    for c_i in range(4):
        for s in range(segs):
            s_next = (s + 1) % segs
            v1 = crown_base + c_i * segs + s + 1
            v2 = crown_base + c_i * segs + s_next + 1
            v3 = crown_base + (c_i + 1) * segs + s_next + 1
            v4 = crown_base + (c_i + 1) * segs + s + 1
            faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    write_obj_file(os.path.join(OUTPUT_DIR, "01_SYS_APEX_SPIRE.obj"), verts, normals, uvs, faces, "SYS_01_APEX_SPIRE")
# endregion


# region PART 02: HEX BARRIER DOME (SYS_02)
# -----------------------------------------------------------------------------
# PART 2: HEX BARRIER DOME (SYS_02)
# -----------------------------------------------------------------------------
def export_part_02():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    dome_r = 1500.0
    dome_h = 650.0
    rings = 18
    segs = 36

    for ri in range(rings + 1):
        phi = (math.pi * 0.5) * (ri / float(rings))  # 0 at apex, pi/2 at base
        z = dome_h * math.cos(phi)
        r = dome_r * math.sin(phi)
        for si in range(segs):
            th = 2.0 * math.pi * (si / float(segs))
            # slight hex offset per ring
            th_offset = (math.pi / segs) if (ri % 2 == 1) else 0.0
            x = r * math.cos(th + th_offset)
            y = r * math.sin(th + th_offset)
            nx = math.sin(phi) * math.cos(th + th_offset)
            ny = math.sin(phi) * math.sin(th + th_offset)
            nz = math.cos(phi)
            add_v(x, y, z, si / float(segs), ri / float(rings), nx, ny, nz)

    for ri in range(rings):
        for si in range(segs):
            si_next = (si + 1) % segs
            v1 = ri * segs + si + 1
            v2 = ri * segs + si_next + 1
            v3 = (ri + 1) * segs + si_next + 1
            v4 = (ri + 1) * segs + si + 1
            # Triangle fan for apex ring, quads/triangles elsewhere
            if ri == 0:
                faces.append([(v1, v1, v1), (v3, v3, v3), (v4, v4, v4)])
            else:
                faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    write_obj_file(os.path.join(OUTPUT_DIR, "02_SYS_HEX_BARRIER.obj"), verts, normals, uvs, faces, "SYS_02_HEX_BARRIER")
# endregion


# region PART 03: ACADEMIC PETAL BLADE (SYS_03 - Single & 8x Radial)
# -----------------------------------------------------------------------------
# PART 3: ACADEMIC PETAL BLADE (SYS_03 - Single & 8x Radial)
# -----------------------------------------------------------------------------
def build_single_petal_mesh(az_deg=0.0):
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    u_res = 24
    v_res = 14
    az_rad = math.radians(az_deg)
    cos_a, sin_a = math.cos(az_rad), math.sin(az_rad)
    trans_x, trans_y = -sin_a, cos_a

    def eval_half_w(u):
        r_dist = BASE_INNER_RADIUS_M + (u * PETAL_LENGTH_M)
        half_slot = math.pi / PETAL_COUNT
        max_p = (r_dist * math.sin(half_slot)) - (MIN_WATERWAY_CLEARANCE_M * 0.5)
        max_p = max(max_p, 5.0)
        vs = math.pow(u, 0.52)
        curve = math.pow(max(0.0, math.sin(math.pi * vs)), 1.20)
        return min((PETAL_WIDTH_MAX_M * 0.5) * curve, max_p)

    def eval_deck_z(u, v):
        arch = math.sin(math.pi * u)
        keel_z = 22.0 * (1.0 - abs(v)) * math.pow(arch, 0.65)
        cup_z = -35.0 * (v * v) * arch
        z = keel_z + cup_z
        if u > 0.70:
            t = (u - 0.70) / 0.30
            blend = t * t * (3.0 - 2.0 * t)
            z *= (1.0 - blend)
        return z

    top_grid = []
    bot_grid = []

    # Deck and Bottom Hull
    for ui in range(u_res + 1):
        u = ui / float(u_res)
        r = BASE_INNER_RADIUS_M + u * PETAL_LENGTH_M
        hw = eval_half_w(u)
        top_row = []
        bot_row = []
        for vi in range(v_res + 1):
            v = -1.0 + 2.0 * (vi / float(v_res))
            w = v * hw
            z_top = eval_deck_z(u, v)
            z_bot = z_top - (12.0 + 16.0 * (1.0 - abs(v)) * math.sin(math.pi * u))

            px = r * cos_a + w * trans_x
            py = r * sin_a + w * trans_y
            v_top = add_v(px, py, z_top, u, (v + 1) * 0.5, 0.0, 0.0, 1.0)
            v_bot = add_v(px, py, z_bot, u, (v + 1) * 0.5, 0.0, 0.0, -1.0)
            top_row.append(v_top)
            bot_row.append(v_bot)
        top_grid.append(top_row)
        bot_grid.append(bot_row)

    # Faces: Top Deck
    for ui in range(u_res):
        for vi in range(v_res):
            v1 = top_grid[ui][vi]
            v2 = top_grid[ui + 1][vi]
            v3 = top_grid[ui + 1][vi + 1]
            v4 = top_grid[ui][vi + 1]
            faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    # Faces: Bottom Hull
    for ui in range(u_res):
        for vi in range(v_res):
            v1 = bot_grid[ui][vi]
            v2 = bot_grid[ui][vi + 1]
            v3 = bot_grid[ui + 1][vi + 1]
            v4 = bot_grid[ui + 1][vi]
            faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    # Side Flanks
    for ui in range(u_res):
        # Left wall (v = -1)
        v1 = top_grid[ui][0]
        v2 = bot_grid[ui][0]
        v3 = bot_grid[ui + 1][0]
        v4 = top_grid[ui + 1][0]
        faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])
        # Right wall (v = +1)
        v1 = top_grid[ui][v_res]
        v2 = top_grid[ui + 1][v_res]
        v3 = bot_grid[ui + 1][v_res]
        v4 = bot_grid[ui][v_res]
        faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    return verts, normals, uvs, faces


def export_part_03():
    # Single Petal
    s_verts, s_norms, s_uvs, s_faces = build_single_petal_mesh(0.0)
    write_obj_file(os.path.join(OUTPUT_DIR, "03_SYS_ACADEMIC_PETAL_SINGLE.obj"), s_verts, s_norms, s_uvs, s_faces, "SYS_03_PETAL_SINGLE")

    # All 8 Petals Combined
    all_v, all_vn, all_vt, all_f = [], [], [], []
    v_offset = 0
    for p in range(PETAL_COUNT):
        deg = p * (360.0 / PETAL_COUNT)
        pv, pvn, pvt, pf = build_single_petal_mesh(deg)
        all_v.extend(pv)
        all_vn.extend(pvn)
        all_vt.extend(pvt)
        for face in pf:
            offset_face = [(idx[0] + v_offset, idx[1] + v_offset, idx[2] + v_offset) for idx in face]
            all_f.append(offset_face)
        v_offset += len(pv)

    write_obj_file(os.path.join(OUTPUT_DIR, "03_SYS_ACADEMIC_PETALS_8X.obj"), all_v, all_vn, all_vt, all_f, "SYS_03_PETALS_8X")
# endregion


# region PART 04: BIO-DOMES & LIVING HABITATS (SYS_04)
# -----------------------------------------------------------------------------
# PART 4: BIO-DOMES & LIVING HABITATS (SYS_04)
# -----------------------------------------------------------------------------
def export_part_04():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    # 8 Main Botanical Domes (one per petal at r = 650m)
    for p in range(PETAL_COUNT):
        az = math.radians(p * (360.0 / PETAL_COUNT))
        cx = 650.0 * math.cos(az)
        cy = 650.0 * math.sin(az)
        cz = 12.0  # petal deck height
        dome_rad = 55.0

        dome_start = len(verts)
        d_rings = 8
        d_segs = 16
        for ri in range(d_rings + 1):
            phi = (math.pi * 0.5) * (ri / float(d_rings))
            dz = dome_rad * math.cos(phi)
            dr = dome_rad * math.sin(phi)
            for si in range(d_segs):
                th = 2.0 * math.pi * (si / float(d_segs))
                x = cx + dr * math.cos(th)
                y = cy + dr * math.sin(th)
                z = cz + dz
                nx = math.sin(phi) * math.cos(th)
                ny = math.sin(phi) * math.sin(th)
                nz = math.cos(phi)
                add_v(x, y, z, si / float(d_segs), ri / float(d_rings), nx, ny, nz)

        for ri in range(d_rings):
            for si in range(d_segs):
                si_next = (si + 1) % d_segs
                v1 = dome_start + ri * d_segs + si + 1
                v2 = dome_start + ri * d_segs + si_next + 1
                v3 = dome_start + (ri + 1) * d_segs + si_next + 1
                v4 = dome_start + (ri + 1) * d_segs + si + 1
                if ri == 0:
                    faces.append([(v1, v1, v1), (v3, v3, v3), (v4, v4, v4)])
                else:
                    faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    write_obj_file(os.path.join(OUTPUT_DIR, "04_SYS_BIO_DOMES.obj"), verts, normals, uvs, faces, "SYS_04_BIO_DOMES")
# endregion


# region PART 05: 70 GOLDEN STAMEN FORCEFIELD PYLONS (SYS_05)
# -----------------------------------------------------------------------------
# PART 5: 70 GOLDEN STAMEN FORCEFIELD PYLONS (SYS_05)
# -----------------------------------------------------------------------------
def export_part_05():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    r_stamen = 220.0
    segs = 8
    rings = 6

    for s_idx in range(STAMEN_COUNT):
        th = 2.0 * math.pi * (s_idx / float(STAMEN_COUNT))
        base_x = r_stamen * math.cos(th)
        base_y = r_stamen * math.sin(th)
        base_z = 0.0

        p_start = len(verts)
        for ri in range(rings + 1):
            rf = ri / float(rings)
            pz = base_z + rf * STAMEN_HEIGHT_M
            # Lotus stamen profile: curved bulbed neck and flared tip
            pr = (4.5 - 2.5 * rf) + 1.2 * math.sin(rf * math.pi)
            for si in range(segs):
                sth = 2.0 * math.pi * (si / float(segs))
                x = base_x + pr * math.cos(sth)
                y = base_y + pr * math.sin(sth)
                add_v(x, y, pz, si / float(segs), rf, math.cos(sth), math.sin(sth), 0.1)

        for ri in range(rings):
            for si in range(segs):
                si_next = (si + 1) % segs
                v1 = p_start + ri * segs + si + 1
                v2 = p_start + ri * segs + si_next + 1
                v3 = p_start + (ri + 1) * segs + si_next + 1
                v4 = p_start + (ri + 1) * segs + si + 1
                faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    write_obj_file(os.path.join(OUTPUT_DIR, "05_SYS_STAMEN_PYLONS.obj"), verts, normals, uvs, faces, "SYS_05_STAMEN_PYLONS")
# endregion


# region PART 06: 45M CANAL & INTER-PETAL SKYBRIDGES (SYS_06)
# -----------------------------------------------------------------------------
# PART 6: 45M CANAL & INTER-PETAL SKYBRIDGES (SYS_06)
# -----------------------------------------------------------------------------
def export_part_06():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    # 8 Arching Inter-Petal Skybridges connecting adjacent petals at r = 500m
    bridge_r = 500.0
    half_deg = 360.0 / (PETAL_COUNT * 2)

    for p in range(PETAL_COUNT):
        slot_center_deg = (p * (360.0 / PETAL_COUNT)) + half_deg
        slot_rad = math.radians(slot_center_deg)

        # Arch across the canal (span: -22m to +22m from slot center)
        b_start = len(verts)
        b_steps = 10
        width = 12.0  # bridge deck width
        for bi in range(b_steps + 1):
            bf = -1.0 + 2.0 * (bi / float(b_steps))  # -1 to +1
            tangent_offset = bf * 25.0
            arch_z = 38.0 + 12.0 * (1.0 - bf * bf)  # high arch over 45m waterway

            # center of this slice
            cx = bridge_r * math.cos(slot_rad) - tangent_offset * math.sin(slot_rad)
            cy = bridge_r * math.sin(slot_rad) + tangent_offset * math.cos(slot_rad)

            # cross width
            dx = math.cos(slot_rad) * (width * 0.5)
            dy = math.sin(slot_rad) * (width * 0.5)

            v1 = add_v(cx - dx, cy - dy, arch_z, 0.0, bi / float(b_steps), 0.0, 0.0, 1.0)
            v2 = add_v(cx + dx, cy + dy, arch_z, 1.0, bi / float(b_steps), 0.0, 0.0, 1.0)

        for bi in range(b_steps):
            v1 = b_start + bi * 2 + 1
            v2 = b_start + (bi + 1) * 2 + 1
            v3 = b_start + (bi + 1) * 2 + 2
            v4 = b_start + bi * 2 + 2
            faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    write_obj_file(os.path.join(OUTPUT_DIR, "06_SYS_CANAL_BRIDGES.obj"), verts, normals, uvs, faces, "SYS_06_CANAL_BRIDGES")
# endregion


# region PART 07: OUTER FLOATING PONTOON JETTY (SYS_07 - Canon LOTUS_ACADEMY_CITY.jpg)
# -----------------------------------------------------------------------------
# PART 7: OUTER FLOATING PONTOON JETTY (SYS_07 - Canon LOTUS_ACADEMY_CITY.jpg)
# -----------------------------------------------------------------------------
def export_part_07():
    """
    Compact modular floating pontoon jetty located strictly in the water outside the petal hull.
    Features:
      - Inclined hydraulic access ramp connecting down from petal rim to water (Z=0)
      - Sleek central floating spine
      - Branching finger pontoons for multi-vessel berthing (large ships outside, small boats inside)
      - 8 instances (one per petal flank)
    """
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    def add_box(cx, cy, cz, sx, sy, sz, rot_rad=0.0):
        b_start = len(verts)
        # 8 corners of local box
        dx, dy, dz = sx * 0.5, sy * 0.5, sz * 0.5
        corners = [
            (-dx, -dy, -dz), (dx, -dy, -dz), (dx, dy, -dz), (-dx, dy, -dz),
            (-dx, -dy, dz), (dx, -dy, dz), (dx, dy, dz), (-dx, dy, dz)
        ]
        cos_r, sin_r = math.cos(rot_rad), math.sin(rot_rad)
        for (lx, ly, lz) in corners:
            wx = cx + (lx * cos_r - ly * sin_r)
            wy = cy + (lx * sin_r + ly * cos_r)
            wz = cz + lz
            add_v(wx, wy, wz, 0.0, 0.0, 0.0, 0.0, 1.0)

        # 6 faces (quads)
        # Bottom, Top, Front, Back, Left, Right
        box_faces = [
            (0, 3, 2, 1), (4, 5, 6, 7),
            (0, 1, 5, 4), (2, 3, 7, 6),
            (3, 0, 4, 7), (1, 2, 6, 5)
        ]
        for bf in box_faces:
            v1, v2, v3, v4 = [b_start + idx + 1 for idx in bf]
            faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    # Generate one dock per petal on outer flank
    for p in range(PETAL_COUNT):
        az_deg = p * (360.0 / PETAL_COUNT)
        az_rad = math.radians(az_deg)

        # Petal outer flank anchor point (r = 1050m, slightly offset clockwise)
        flank_offset_deg = az_deg - 7.5
        flank_rad = math.radians(flank_offset_deg)

        # 1. Retractable Inclined Ramp from Petal Rim (Z = 12m) to Water (Z = 0.5m)
        ramp_x1 = 1000.0 * math.cos(flank_rad)
        ramp_y1 = 1000.0 * math.sin(flank_rad)
        ramp_z1 = 12.0

        ramp_x2 = 1060.0 * math.cos(flank_rad)
        ramp_y2 = 1060.0 * math.sin(flank_rad)
        ramp_z2 = 0.5

        rcx = (ramp_x1 + ramp_x2) * 0.5
        rcy = (ramp_y1 + ramp_y2) * 0.5
        rcz = (ramp_z1 + ramp_z2) * 0.5
        add_box(rcx, rcy, rcz, 8.0, 60.0, 1.5, flank_rad)

        # 2. Central Floating Pontoon Spine (Length 90m, Width 14m, floating at Z = 0.6m)
        spine_cx = 1120.0 * math.cos(flank_rad)
        spine_cy = 1120.0 * math.sin(flank_rad)
        add_box(spine_cx, spine_cy, 0.6, 14.0, 90.0, 1.8, flank_rad)

        # 3. Three Finger Pontoon Slips extending perpendicular into the water
        for finger_i in [-1, 0, 1]:
            finger_dist = 1120.0 + finger_i * 28.0
            # perpendicular direction
            perp_rad = flank_rad + (math.pi * 0.5)
            fcx = finger_dist * math.cos(flank_rad) + 35.0 * math.cos(perp_rad)
            fcy = finger_dist * math.sin(flank_rad) + 35.0 * math.sin(perp_rad)
            add_box(fcx, fcy, 0.5, 6.0, 50.0, 1.6, perp_rad)

    write_obj_file(os.path.join(OUTPUT_DIR, "07_SYS_OUTER_FLOATING_DOCK.obj"), verts, normals, uvs, faces, "SYS_07_OUTER_FLOATING_DOCK")
# endregion


# region PART 08: 12 SUBMERGED TELESCOPIC STEM RINGS (SYS_08)
# -----------------------------------------------------------------------------
# PART 8: 12 SUBMERGED TELESCOPIC STEM RINGS (SYS_08)
# -----------------------------------------------------------------------------
def export_part_08():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    segs = 32
    for tier in range(RING_TIER_COUNT):
        tf = tier / float(RING_TIER_COUNT - 1)
        z_top = -50.0 - tf * (900.0 - 50.0)
        z_bot = z_top - 35.0

        r_outer = SURFACE_NECK_RADIUS_M + tf * (SEABED_ABYSSAL_RADIUS_M - SURFACE_NECK_RADIUS_M)
        r_inner = r_outer - 18.0

        ring_start = len(verts)
        # Cylinder outer wall
        for s in range(segs):
            th = 2.0 * math.pi * (s / float(segs))
            add_v(r_outer * math.cos(th), r_outer * math.sin(th), z_top, s / float(segs), 1.0, math.cos(th), math.sin(th), 0.0)
            add_v(r_outer * math.cos(th), r_outer * math.sin(th), z_bot, s / float(segs), 0.0, math.cos(th), math.sin(th), 0.0)

        for s in range(segs):
            s_next = (s + 1) % segs
            v1 = ring_start + s * 2 + 1
            v2 = ring_start + s_next * 2 + 1
            v3 = ring_start + s_next * 2 + 2
            v4 = ring_start + s * 2 + 2
            faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    write_obj_file(os.path.join(OUTPUT_DIR, "08_SYS_STEM_RINGS.obj"), verts, normals, uvs, faces, "SYS_08_STEM_RINGS")
# endregion


# region PART 09: ABYSSAL CLAWS & SEABED DOOMSDAY VAULT (SYS_09)
# -----------------------------------------------------------------------------
# PART 9: ABYSSAL CLAWS & SEABED DOOMSDAY VAULT (SYS_09)
# -----------------------------------------------------------------------------
def export_part_09():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    # 1. Central Monolithic Doomsday Vault Bunker (-950m to -1000m)
    v_start = len(verts)
    segs = 16
    v_rad = 120.0
    for vi in range(segs):
        th = 2.0 * math.pi * (vi / float(segs))
        add_v(v_rad * math.cos(th), v_rad * math.sin(th), -950.0, vi / float(segs), 1.0, math.cos(th), math.sin(th), 0.0)
        add_v(v_rad * 1.25 * math.cos(th), v_rad * 1.25 * math.sin(th), -1000.0, vi / float(segs), 0.0, math.cos(th), math.sin(th), 0.0)

    for vi in range(segs):
        v_next = (vi + 1) % segs
        v1 = v_start + vi * 2 + 1
        v2 = v_start + v_next * 2 + 1
        v3 = v_start + v_next * 2 + 2
        v4 = v_start + vi * 2 + 2
        faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    # 2. Four Giant Hydraulic Anchoring Claws
    for c_i in range(4):
        c_rad = (math.pi * 0.5) * c_i
        claw_start = len(verts)
        # Claw strut extending from center to seabed bedrock
        p1 = (100.0 * math.cos(c_rad), 100.0 * math.sin(c_rad), -950.0)
        p2 = (280.0 * math.cos(c_rad), 280.0 * math.sin(c_rad), -970.0)
        p3 = (380.0 * math.cos(c_rad), 380.0 * math.sin(c_rad), -1000.0)

        # Simple triangular truss for claw
        add_v(p1[0], p1[1], p1[2], 0.0, 0.0)
        add_v(p2[0], p2[1], p2[2], 0.5, 0.0)
        add_v(p3[0], p3[1], p3[2], 1.0, 0.0)
        add_v(p2[0], p2[1], p2[2] + 25.0, 0.5, 1.0)

        faces.append([
            (claw_start + 1, claw_start + 1, claw_start + 1),
            (claw_start + 2, claw_start + 2, claw_start + 2),
            (claw_start + 4, claw_start + 4, claw_start + 4)
        ])
        faces.append([
            (claw_start + 2, claw_start + 2, claw_start + 2),
            (claw_start + 3, claw_start + 3, claw_start + 3),
            (claw_start + 4, claw_start + 4, claw_start + 4)
        ])

    write_obj_file(os.path.join(OUTPUT_DIR, "09_SYS_SEABED_VAULT.obj"), verts, normals, uvs, faces, "SYS_09_SEABED_VAULT")
# endregion


# region PART 10: 3D MAGLEV & EVAC TRANSIT CONDUITS (SYS_10)
# -----------------------------------------------------------------------------
# PART 10: 3D MAGLEV & EVAC TRANSIT CONDUITS (SYS_10)
# -----------------------------------------------------------------------------
def export_part_10():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    ring_radii = [260.0, 520.0]
    tube_r = 2.2
    segs = 32
    tube_segs = 6

    for r_center in ring_radii:
        for s in range(segs):
            s_next = (s + 1) % segs
            th1 = 2.0 * math.pi * (s / float(segs))
            th2 = 2.0 * math.pi * (s_next / float(segs))

            c1 = (r_center * math.cos(th1), r_center * math.sin(th1), 8.0)
            c2 = (r_center * math.cos(th2), r_center * math.sin(th2), 8.0)

            dir_vec = (c2[0] - c1[0], c2[1] - c1[1], c2[2] - c1[2])
            length = math.sqrt(dir_vec[0]**2 + dir_vec[1]**2 + dir_vec[2]**2 + 1e-6)
            dx, dy, dz = dir_vec[0] / length, dir_vec[1] / length, dir_vec[2] / length
            ux, uy, uz = 0.0, 0.0, 1.0
            sx, sy, sz = dy * uz - dz * uy, dz * ux - dx * uz, dx * uy - dy * ux

            p_start = len(verts)
            for ts in range(tube_segs):
                t_ang = 2.0 * math.pi * (ts / float(tube_segs))
                off_x = sx * math.cos(t_ang) * tube_r + ux * math.sin(t_ang) * tube_r
                off_y = sy * math.cos(t_ang) * tube_r + uy * math.sin(t_ang) * tube_r
                off_z = sz * math.cos(t_ang) * tube_r + uz * math.sin(t_ang) * tube_r
                add_v(c1[0] + off_x, c1[1] + off_y, c1[2] + off_z)
                add_v(c2[0] + off_x, c2[1] + off_y, c2[2] + off_z)

            for ts in range(tube_segs):
                ts_next = (ts + 1) % tube_segs
                v1 = p_start + ts * 2 + 1
                v2 = p_start + ts * 2 + 2
                v3 = p_start + ts_next * 2 + 2
                v4 = p_start + ts_next * 2 + 1
                faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    for i in range(8):
        th = 2.0 * math.pi * (i / 8.0)
        cos_th, sin_th = math.cos(th), math.sin(th)
        r_start, r_end = 150.0, 850.0
        steps = 10
        for st in range(steps):
            r1 = r_start + (st / float(steps)) * (r_end - r_start)
            r2 = r_start + ((st + 1) / float(steps)) * (r_end - r_start)
            z1 = 12.0 + 4.0 * math.sin((r1 - 150.0) / 700.0 * math.pi)
            z2 = 12.0 + 4.0 * math.sin((r2 - 150.0) / 700.0 * math.pi)

            c1 = (r1 * cos_th, r1 * sin_th, z1)
            c2 = (r2 * cos_th, r2 * sin_th, z2)

            p_start = len(verts)
            for ts in range(tube_segs):
                t_ang = 2.0 * math.pi * (ts / float(tube_segs))
                nx, ny, nz = -sin_th, cos_th, 0.0
                ux, uy, uz = 0.0, 0.0, 1.0
                off_x = nx * math.cos(t_ang) * tube_r + ux * math.sin(t_ang) * tube_r
                off_y = ny * math.cos(t_ang) * tube_r + uy * math.sin(t_ang) * tube_r
                off_z = nz * math.cos(t_ang) * tube_r + uz * math.sin(t_ang) * tube_r
                add_v(c1[0] + off_x, c1[1] + off_y, c1[2] + off_z)
                add_v(c2[0] + off_x, c2[1] + off_y, c2[2] + off_z)

            for ts in range(tube_segs):
                ts_next = (ts + 1) % tube_segs
                v1 = p_start + ts * 2 + 1
                v2 = p_start + ts * 2 + 2
                v3 = p_start + ts_next * 2 + 2
                v4 = p_start + ts_next * 2 + 1
                faces.append([(v1, v1, v1), (v2, v2, v2), (v3, v3, v3), (v4, v4, v4)])

    write_obj_file(os.path.join(OUTPUT_DIR, "10_SYS_TRANSIT_CONDUITS.obj"), verts, normals, uvs, faces, "SYS_10_TRANSIT_CONDUITS")
# endregion


# region PART 11: CORE-TO-STEM RING 1 COLLAR INTERFACE (SYS_11)
# -----------------------------------------------------------------------------
# PART 11: CORE-TO-STEM RING 1 COLLAR INTERFACE (SYS_11)
# -----------------------------------------------------------------------------
def export_part_11():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    top_z, bot_z = 0.0, -50.0
    top_r, bot_r = 95.0, 82.0
    segs = 32
    rings = 6

    for r in range(rings):
        v1 = r / float(rings)
        v2 = (r + 1) / float(rings)
        z1 = top_z + v1 * (bot_z - top_z)
        z2 = top_z + v2 * (bot_z - top_z)
        r1 = top_r + v1 * (bot_r - top_r)
        r2 = top_r + v2 * (bot_r - top_r)

        p_start = len(verts)
        for s in range(segs):
            th = 2.0 * math.pi * (s / float(segs))
            add_v(r1 * math.cos(th), r1 * math.sin(th), z1, s / float(segs), v1)
            add_v(r2 * math.cos(th), r2 * math.sin(th), z2, s / float(segs), v2)

        for s in range(segs):
            s_next = (s + 1) % segs
            v1_idx = p_start + s * 2 + 1
            v2_idx = p_start + s * 2 + 2
            v3_idx = p_start + s_next * 2 + 2
            v4_idx = p_start + s_next * 2 + 1
            faces.append([(v1_idx, v1_idx, v1_idx), (v2_idx, v2_idx, v2_idx), (v3_idx, v3_idx, v3_idx), (v4_idx, v4_idx, v4_idx)])

    # 8 Radial load gussets
    for i in range(8):
        ang = i * (math.pi * 0.25)
        cos_a, sin_a = math.cos(ang), math.sin(ang)
        p1 = (cos_a * top_r, sin_a * top_r, top_z)
        p2 = (cos_a * (top_r + 20.0), sin_a * (top_r + 20.0), top_z - 8.0)
        p3 = (cos_a * (bot_r + 8.0), sin_a * (bot_r + 8.0), bot_z + 10.0)
        p4 = (cos_a * bot_r, sin_a * bot_r, bot_z)

        g_start = len(verts)
        add_v(p1[0], p1[1], p1[2], 0.0, 1.0)
        add_v(p2[0], p2[1], p2[2], 1.0, 1.0)
        add_v(p3[0], p3[1], p3[2], 1.0, 0.0)
        add_v(p4[0], p4[1], p4[2], 0.0, 0.0)

        faces.append([
            (g_start + 1, g_start + 1, g_start + 1),
            (g_start + 2, g_start + 2, g_start + 2),
            (g_start + 3, g_start + 3, g_start + 3),
            (g_start + 4, g_start + 4, g_start + 4)
        ])

    write_obj_file(os.path.join(OUTPUT_DIR, "11_SYS_CORE_STEM_COLLAR.obj"), verts, normals, uvs, faces, "SYS_11_CORE_STEM_COLLAR")
# endregion


# region PART 12: INTER-RING HYDRAULIC EXPANSION DAMPERS (SYS_12)
# -----------------------------------------------------------------------------
# PART 12: INTER-RING HYDRAULIC EXPANSION DAMPERS (SYS_12)
# -----------------------------------------------------------------------------
def export_part_12():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    tiers = 12
    neck_r, seabed_r = 80.0, 350.0
    max_depth = -900.0

    for t in range(tiers - 1):
        v1 = t / float(tiers)
        v2 = (t + 1) / float(tiers)
        r1 = neck_r + (v1 ** 1.4) * (seabed_r - neck_r)
        r2 = neck_r + (v2 ** 1.4) * (seabed_r - neck_r)
        z1 = v1 * max_depth
        z2 = v2 * max_depth

        for s in range(8):
            base_ang = s * (math.pi * 0.25)
            for pair in [-0.04, 0.04]:
                ang = base_ang + pair
                cos_a, sin_a = math.cos(ang), math.sin(ang)

                pt_top = (cos_a * (r1 * 0.96), sin_a * (r1 * 0.96), z1)
                pt_bot = (cos_a * (r2 * 0.96), sin_a * (r2 * 0.96), z2)

                # Cylinder segments
                cyl_start = len(verts)
                c_segs = 5
                cyl_r = 1.6
                for cs in range(c_segs):
                    ca = cs / float(c_segs) * math.pi * 2.0
                    dx = -sin_a * math.cos(ca) * cyl_r
                    dy = cos_a * math.cos(ca) * cyl_r
                    dz = math.sin(ca) * cyl_r
                    add_v(pt_top[0] + dx, pt_top[1] + dy, pt_top[2] + dz)
                    add_v(pt_bot[0] + dx, pt_bot[1] + dy, pt_bot[2] + dz)

                for cs in range(c_segs):
                    cs_next = (cs + 1) % c_segs
                    v1_idx = cyl_start + cs * 2 + 1
                    v2_idx = cyl_start + cs * 2 + 2
                    v3_idx = cyl_start + cs_next * 2 + 2
                    v4_idx = cyl_start + cs_next * 2 + 1
                    faces.append([(v1_idx, v1_idx, v1_idx), (v2_idx, v2_idx, v2_idx), (v3_idx, v3_idx, v3_idx), (v4_idx, v4_idx, v4_idx)])

    write_obj_file(os.path.join(OUTPUT_DIR, "12_SYS_INTER_RING_HYDRAULICS.obj"), verts, normals, uvs, faces, "SYS_12_INTER_RING_HYDRAULICS")
# endregion


# region PART 13: VERTICAL DEEP-SEA TRANSIT ELEVATOR CORE (SYS_13)
# -----------------------------------------------------------------------------
# PART 13: VERTICAL DEEP-SEA TRANSIT ELEVATOR CORE (SYS_13)
# -----------------------------------------------------------------------------
def export_part_13():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    top_z, bot_z = 120.0, -980.0
    core_r = 12.0
    segs = 20
    v_steps = 24

    for vs in range(v_steps):
        frac1 = vs / float(v_steps)
        frac2 = (vs + 1) / float(v_steps)
        z1 = top_z + frac1 * (bot_z - top_z)
        z2 = top_z + frac2 * (bot_z - top_z)

        p_start = len(verts)
        for s in range(segs):
            th = 2.0 * math.pi * (s / float(segs))
            add_v(core_r * math.cos(th), core_r * math.sin(th), z1)
            add_v(core_r * math.cos(th), core_r * math.sin(th), z2)

        for s in range(segs):
            s_next = (s + 1) % segs
            v1_idx = p_start + s * 2 + 1
            v2_idx = p_start + s * 2 + 2
            v3_idx = p_start + s_next * 2 + 2
            v4_idx = p_start + s_next * 2 + 1
            faces.append([(v1_idx, v1_idx, v1_idx), (v2_idx, v2_idx, v2_idx), (v3_idx, v3_idx, v3_idx), (v4_idx, v4_idx, v4_idx)])

    # 5 Pressurized Airlock Station Hubs
    station_depths = [0.0, -250.0, -500.0, -750.0, -950.0]
    st_r = 25.0
    st_h = 16.0
    for sz in station_depths:
        p_start = len(verts)
        for s in range(segs):
            th = 2.0 * math.pi * (s / float(segs))
            add_v(st_r * math.cos(th), st_r * math.sin(th), sz + st_h * 0.5)
            add_v(st_r * math.cos(th), st_r * math.sin(th), sz - st_h * 0.5)

        for s in range(segs):
            s_next = (s + 1) % segs
            v1_idx = p_start + s * 2 + 1
            v2_idx = p_start + s * 2 + 2
            v3_idx = p_start + s_next * 2 + 2
            v4_idx = p_start + s_next * 2 + 1
            faces.append([(v1_idx, v1_idx, v1_idx), (v2_idx, v2_idx, v2_idx), (v3_idx, v3_idx, v3_idx), (v4_idx, v4_idx, v4_idx)])

    write_obj_file(os.path.join(OUTPUT_DIR, "13_SYS_DEEPSEA_ELEVATOR_CORE.obj"), verts, normals, uvs, faces, "SYS_13_DEEPSEA_ELEVATOR_CORE")
# endregion


# region PART 14: EMERGENCY BULKHEAD GATES (SYS_14)
# -----------------------------------------------------------------------------
# PART 14: EMERGENCY BULKHEAD GATES (SYS_14)
# -----------------------------------------------------------------------------
def export_part_14():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    gate_r = 165.0
    channel_w = 45.0
    tower_w = 8.0
    tower_h = 38.0

    for i in range(8):
        canal_ang = (i + 0.5) * (math.pi * 0.25)
        cos_a, sin_a = math.cos(canal_ang), math.sin(canal_ang)
        cross_x, cross_z = -sin_a, cos_a
        c_x, c_y = cos_a * gate_r, sin_a * gate_r

        # Twin Gantry Towers
        for side in [-1, 1]:
            tx = c_x + cross_x * (channel_w * 0.5 + tower_w * 0.5) * side
            ty = c_y + cross_z * (channel_w * 0.5 + tower_w * 0.5) * side
            hw = tower_w * 0.5
            hd = 5.0

            p_start = len(verts)
            p0 = (tx - hw * cross_x - hd * cos_a, ty - hw * cross_z - hd * sin_a, 0.0)
            p1 = (tx + hw * cross_x - hd * cos_a, ty + hw * cross_z - hd * sin_a, 0.0)
            p2 = (tx + hw * cross_x + hd * cos_a, ty + hw * cross_z + hd * sin_a, 0.0)
            p3 = (tx - hw * cross_x + hd * cos_a, ty - hw * cross_z + hd * sin_a, 0.0)

            add_v(p0[0], p0[1], p0[2])
            add_v(p1[0], p1[1], p1[2])
            add_v(p2[0], p2[1], p2[2])
            add_v(p3[0], p3[1], p3[2])
            add_v(p0[0], p0[1], tower_h)
            add_v(p1[0], p1[1], tower_h)
            add_v(p2[0], p2[1], tower_h)
            add_v(p3[0], p3[1], tower_h)

            pts = [p_start + k + 1 for k in range(8)]
            box_faces = [
                (pts[0], pts[1], pts[2], pts[3]),
                (pts[7], pts[6], pts[5], pts[4]),
                (pts[0], pts[4], pts[5], pts[1]),
                (pts[1], pts[5], pts[6], pts[2]),
                (pts[2], pts[6], pts[7], pts[3]),
                (pts[3], pts[7], pts[4], pts[0])
            ]
            for bf in box_faces:
                faces.append([(idx, idx, idx) for idx in bf])

        # Cross Beam Gantry
        span = channel_w + tower_w * 2.0
        g_start = len(verts)
        b1 = (c_x - cross_x * (span * 0.5), c_y - cross_z * (span * 0.5), tower_h)
        b2 = (c_x + cross_x * (span * 0.5), c_y + cross_z * (span * 0.5), tower_h)
        b3 = (b2[0], b2[1], tower_h + 6.0)
        b4 = (b1[0], b1[1], tower_h + 6.0)

        add_v(b1[0], b1[1], b1[2])
        add_v(b2[0], b2[1], b2[2])
        add_v(b3[0], b3[1], b3[2])
        add_v(b4[0], b4[1], b4[2])

        faces.append([
            (g_start + 1, g_start + 1, g_start + 1),
            (g_start + 2, g_start + 2, g_start + 2),
            (g_start + 3, g_start + 3, g_start + 3),
            (g_start + 4, g_start + 4, g_start + 4)
        ])

    write_obj_file(os.path.join(OUTPUT_DIR, "14_SYS_EMERGENCY_BULKHEAD_GATES.obj"), verts, normals, uvs, faces, "SYS_14_EMERGENCY_BULKHEAD_GATES")
# endregion


# region PART 15: 8 FACULTY SUB-COUNCIL ASSEMBLY HALLS (SYS_15)
# -----------------------------------------------------------------------------
# PART 15: 8 FACULTY SUB-COUNCIL ASSEMBLY HALLS (SYS_15)
# -----------------------------------------------------------------------------
def export_part_15():
    verts, normals, uvs, faces = [], [], [], []

    def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts.append((x, y, z))
        normals.append((nx, ny, nz))
        uvs.append((u, v))
        return len(verts)

    hall_r = 380.0
    podium_r = 42.0
    canopy_h = 48.0

    for p in range(8):
        petal_ang = p * (math.pi * 0.25)
        cos_p, sin_p = math.cos(petal_ang), math.sin(petal_ang)
        center_x, center_y = cos_p * hall_r, sin_p * hall_r

        # Stepped Podium
        segs = 16
        for t in range(3):
            r_step = podium_r * (1.0 - t * 0.12)
            z_bot = 10.0 + t * 2.5
            z_top = 10.0 + (t + 1) * 2.5

            p_start = len(verts)
            for s in range(segs):
                th = 2.0 * math.pi * (s / float(segs))
                add_v(center_x + r_step * math.cos(th), center_y + r_step * math.sin(th), z_bot)
                add_v(center_x + r_step * math.cos(th), center_y + r_step * math.sin(th), z_top)

            for s in range(segs):
                s_next = (s + 1) % segs
                v1_idx = p_start + s * 2 + 1
                v2_idx = p_start + s * 2 + 2
                v3_idx = p_start + s_next * 2 + 2
                v4_idx = p_start + s_next * 2 + 1
                faces.append([(v1_idx, v1_idx, v1_idx), (v2_idx, v2_idx, v2_idx), (v3_idx, v3_idx, v3_idx), (v4_idx, v4_idx, v4_idx)])

        # Cantilever Canopy
        c_rings = 8
        c_cols = 8
        for cr in range(c_rings):
            u1 = cr / float(c_rings)
            u2 = (cr + 1) / float(c_rings)
            for cc in range(c_cols):
                v1 = (cc / float(c_cols)) - 0.5
                v2 = ((cc + 1) / float(c_cols)) - 0.5

                f1 = u1 * podium_r * 1.3 - podium_r * 0.4
                f2 = u2 * podium_r * 1.3 - podium_r * 0.4
                w1 = (podium_r * 0.9) * math.sqrt(max(0.01, 1.0 - u1 * 0.7))
                w2 = (podium_r * 0.9) * math.sqrt(max(0.01, 1.0 - u2 * 0.7))

                z1 = 18.0 + math.sin(u1 * math.pi * 0.85) * canopy_h - (v1 * 2.0) ** 2 * 6.0
                z2 = 18.0 + math.sin(u2 * math.pi * 0.85) * canopy_h - (v2 * 2.0) ** 2 * 6.0

                q1 = (center_x + cos_p * f1 - sin_p * (v1 * w1), center_y + sin_p * f1 + cos_p * (v1 * w1), z1)
                q2 = (center_x + cos_p * f1 - sin_p * (v2 * w1), center_y + sin_p * f1 + cos_p * (v2 * w1), z1)
                q3 = (center_x + cos_p * f2 - sin_p * (v2 * w2), center_y + sin_p * f2 + cos_p * (v2 * w2), z2)
                q4 = (center_x + cos_p * f2 - sin_p * (v1 * w2), center_y + sin_p * f2 + cos_p * (v1 * w2), z2)

                can_start = len(verts)
                add_v(q1[0], q1[1], q1[2])
                add_v(q2[0], q2[1], q2[2])
                add_v(q3[0], q3[1], q3[2])
                add_v(q4[0], q4[1], q4[2])

                faces.append([
                    (can_start + 1, can_start + 1, can_start + 1),
                    (can_start + 2, can_start + 2, can_start + 2),
                    (can_start + 3, can_start + 3, can_start + 3),
                    (can_start + 4, can_start + 4, can_start + 4)
                ])

    write_obj_file(os.path.join(OUTPUT_DIR, "15_SYS_SUBCOUNCIL_HALLS_8X.obj"), verts, normals, uvs, faces, "SYS_15_SUBCOUNCIL_HALLS_8X")
# endregion


# region PART 16: MODULAR BUILDINGS (SYS_16)
# -----------------------------------------------------------------------------
# PART 16: MODULAR BUILDINGS (SYS_16) - 1,280 BUILDINGS / 7,623 FLOORS
# -----------------------------------------------------------------------------
def export_part_16():
    import csv

    # 1. Export 16_SYS_MODULAR_BUILDING_SINGLE.obj (12m x 12m Stacked Kit-of-Parts)
    verts_s, normals_s, uvs_s, faces_s = [], [], [], []

    def add_vs(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
        verts_s.append((x, y, z))
        normals_s.append((nx, ny, nz))
        uvs_s.append((u, v))
        return len(verts_s)

    single_floors = [
        ("Foundation", 0.0, 4.0, 13.0),
        ("GroundLobby", 4.0, 6.0, 12.0),
        ("AcademicLab", 10.0, 4.0, 12.0),
        ("FacultyChambers", 14.0, 4.0, 12.0),
        ("RoofGarden", 18.0, 8.0, 10.0),
    ]

    for fname, z_base, f_h, w in single_floors:
        hw = w * 0.5
        v_start = len(verts_s)
        p0 = (-hw, -hw, z_base)
        p1 = ( hw, -hw, z_base)
        p2 = ( hw,  hw, z_base)
        p3 = (-hw,  hw, z_base)
        p4 = (-hw, -hw, z_base + f_h)
        p5 = ( hw, -hw, z_base + f_h)
        p6 = ( hw,  hw, z_base + f_h)
        p7 = (-hw,  hw, z_base + f_h)

        for pt in [p0, p1, p2, p3, p4, p5, p6, p7]:
            add_vs(pt[0], pt[1], pt[2])

        pts = [v_start + k + 1 for k in range(8)]
        box_faces = [
            (pts[0], pts[1], pts[2], pts[3]),
            (pts[7], pts[6], pts[5], pts[4]),
            (pts[0], pts[4], pts[5], pts[1]),
            (pts[1], pts[5], pts[6], pts[2]),
            (pts[2], pts[6], pts[7], pts[3]),
            (pts[3], pts[7], pts[4], pts[0])
        ]
        for bf in box_faces:
            faces_s.append([(idx, idx, idx) for idx in bf])

    write_obj_file(os.path.join(OUTPUT_DIR, "16_SYS_MODULAR_BUILDING_SINGLE.obj"),
                   verts_s, normals_s, uvs_s, faces_s, "SYS_16_MODULAR_BUILDING_SINGLE")

    # 2. Export 16_SYS_MODULAR_BUILDINGS.obj (All 7,623 Modular Floors from CSV)
    csv_path = os.path.join(WORKSPACE_DIR, "output", "istrorigan_building_assemblies.csv")
    if os.path.exists(csv_path):
        verts, normals, uvs, faces = [], [], [], []

        def add_v(x, y, z, u=0.0, v=0.0, nx=0.0, ny=0.0, nz=1.0):
            verts.append((x, y, z))
            normals.append((nx, ny, nz))
            uvs.append((u, v))
            return len(verts)

        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # In meters for parts OBJ
                x = float(row["x_cm"]) * 0.01
                y = float(row["y_cm"]) * 0.01
                z = float(row["z_cm"]) * 0.01
                h = float(row["height_cm"]) * 0.01
                w = 12.0
                hw = w * 0.5

                v_start = len(verts)
                p0 = (x - hw, y - hw, z)
                p1 = (x + hw, y - hw, z)
                p2 = (x + hw, y + hw, z)
                p3 = (x - hw, y + hw, z)
                p4 = (x - hw, y - hw, z + h)
                p5 = (x + hw, y - hw, z + h)
                p6 = (x + hw, y + hw, z + h)
                p7 = (x - hw, y + hw, z + h)

                for pt in [p0, p1, p2, p3, p4, p5, p6, p7]:
                    add_v(pt[0], pt[1], pt[2])

                pts = [v_start + k + 1 for k in range(8)]
                box_faces = [
                    (pts[0], pts[1], pts[2], pts[3]),
                    (pts[7], pts[6], pts[5], pts[4]),
                    (pts[0], pts[4], pts[5], pts[1]),
                    (pts[1], pts[5], pts[6], pts[2]),
                    (pts[2], pts[6], pts[7], pts[3]),
                    (pts[3], pts[7], pts[4], pts[0])
                ]
                for bf in box_faces:
                    faces.append([(idx, idx, idx) for idx in bf])

        write_obj_file(os.path.join(OUTPUT_DIR, "16_SYS_MODULAR_BUILDINGS.obj"),
                       verts, normals, uvs, faces, "SYS_16_MODULAR_BUILDINGS_7623X")
# endregion


# region MAIN DISPATCHER & CLI
# -----------------------------------------------------------------------------
# MAIN DISPATCHER
# -----------------------------------------------------------------------------
def export_all():
    print("================================================================================")
    print("ISTRORIGAN MEGASTRUCTURE - GENERATING ALL MODULAR 3D PARTS FOR HOUDINI & DCC")
    print("================================================================================")
    export_part_01()
    export_part_02()
    export_part_03()
    export_part_04()
    export_part_05()
    export_part_06()
    export_part_07()
    export_part_08()
    export_part_09()
    export_part_10()
    export_part_11()
    export_part_12()
    export_part_13()
    export_part_14()
    export_part_15()
    export_part_16()
    print("================================================================================")
    print(f"[*] ALL CANONICAL PART MESHES SUCCESSFULLY EXPORTED TO: {OUTPUT_DIR}")
    print("================================================================================")


if __name__ == "__main__":
    export_all()
# endregion

