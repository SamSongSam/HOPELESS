"""
================================================================================
 ISTRORIGAN MEGASTRUCTURE (YEAR 4205) - MASTER PROCEDURAL SYSTEM RUNNER
================================================================================
 One-shot master orchestrator that imports and compiles all 9 modular subsystems
 into a unified, production-grade SOP Digital Asset (HDA):

   Part 01: Apex Spire & Citadel of Ten (+600m)
   Part 02: Hexagonal Forcefield Barrier Dome (R=1,500m)
   Part 03: 8 Academic Petals (45m Waterway Clearance & Keel Hull)
   Part 04: Botanical Bio-Domes & Terraced Living Habitats
   Part 05: 70 Golden Stamen Energy Pylons
   Part 06: Inter-Petal Canals & Skybridges (45m Gaps)
   Part 07: Outer Floating Pontoon Jetties (Canon Ref, No Petal Crowding)
   Part 08: 12 Submerged Telescopic Hydraulic Ballast Rings
   Part 09: Abyssal Doomsday Vault & Bedrock Anchor Claws (-1,000m)

 Triple Output Architecture:
   - Output 0: Master Game-Ready City Mesh (Triangulate, UV, UE5 Scale x100)
   - Output 1: Guide Geometry (45m Clearances & Radii) [Template Flag On]
   - Output 2: Level Instancing Point Cloud (unreal_instance, unreal_material)
   - ROP FBX & glTF Export Nodes ready for 1-click disk baking

 Execution:
   In Houdini: Windows > Python Source Editor -> paste -> Run
   In CLI:     hython scripts/houdini/build_istrorigan_master.py [save]
================================================================================
"""

# region MODULE IMPORTS & CONSTANTS
import sys
import os

# Ensure package directory is on path
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
if PACKAGE_DIR not in sys.path:
    sys.path.insert(0, PACKAGE_DIR)

from helpers import (
    COL_W, ROW_H, mk, setp, sete, wr, netbox, stickynote, load_vex,
    F, I, B, COL, SEP, STR, SIMPLE, TAB, get_hou
)

import part01_apex_spire
import part02_hex_barrier
import part03_academic_petals
import part04_bio_domes
import part05_stamen_pylons
import part06_canal_bridges
import part07_outer_docks
import part08_submerged_rings
import part09_seabed_vault
import part11_stem_collar
import part12_ring_hydraulics
import part13_elevator_core
import part14_bulkhead_gates
import part15_subcouncil_halls
import pcg_stages

CREF = "../"
# project root = two levels above scripts/houdini (portable, no absolute paths)
PROJECT_ROOT = os.path.abspath(os.path.join(PACKAGE_DIR, "..", "..")).replace("\\", "/")
OUTPUT_DIR = PROJECT_ROOT + "/output"
# endregion


# region DATA-DRIVEN URBAN LAYERS PYTHON CODE
PYTHON_BUILDINGS_CODE = r'''
import csv, os, hou
ROOT = hou.pwd().parent().evalParm("blueprintRoot")   # project root ($HIP/..)
geo = hou.pwd().geometry()
geo.clear()
csv_path = ROOT + "/output/istrorigan_building_assemblies.csv"
if os.path.exists(csv_path):
    geo.addAttrib(hou.attribType.Point, "Cd", (0.7, 0.7, 0.7))
    geo.addAttrib(hou.attribType.Prim, "Cd", (0.7, 0.7, 0.7))
    geo.addAttrib(hou.attribType.Prim, "zone", "")
    geo.addAttrib(hou.attribType.Prim, "mesh_name", "")
    geo.addAttrib(hou.attribType.Prim, "building_id", 0)

    cd_map = {
        "ZONE_CORE_CITADEL": (1.0, 0.85, 0.3),
        "ZONE_FACULTY_OCEANIC": (0.1, 0.5, 0.9),
        "ZONE_FACULTY_BIOSPHERE": (0.2, 0.85, 0.4),
        "ZONE_FACULTY_CLIMATE": (0.7, 0.9, 1.0),
        "ZONE_FACULTY_MEGASTRUCT": (0.9, 0.6, 0.2),
        "ZONE_FACULTY_ARCHIVES": (0.6, 0.3, 0.8),
        "ZONE_FACULTY_ABYSSAL": (0.15, 0.35, 0.55),
        "ZONE_FACULTY_DIPLOMACY": (0.95, 0.92, 0.85),
        "ZONE_FACULTY_MEDICINE": (0.95, 0.4, 0.5),
        "ZONE_CLEARANCE_WATERWAY": (1.0, 0.3, 0.3),
        "ZONE_HARBOR_BERTH": (0.6, 0.65, 0.7),
    }

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            x = float(row["x_cm"]) * 0.01
            z = float(row["y_cm"]) * 0.01
            y = float(row["z_cm"]) * 0.01
            h = float(row["height_cm"]) * 0.01
            w = 12.0
            zone = row["zone_tag"]
            col = cd_map.get(zone, (0.7, 0.7, 0.7))
            b_id = int(row["building_id"])
            m_name = row["mesh"]
            
            hw = w * 0.5
            p0 = geo.createPoint(); p0.setPosition((x - hw, y, z - hw))
            p1 = geo.createPoint(); p1.setPosition((x + hw, y, z - hw))
            p2 = geo.createPoint(); p2.setPosition((x + hw, y, z + hw))
            p3 = geo.createPoint(); p3.setPosition((x - hw, y, z + hw))
            p4 = geo.createPoint(); p4.setPosition((x - hw, y + h, z - hw))
            p5 = geo.createPoint(); p5.setPosition((x + hw, y + h, z - hw))
            p6 = geo.createPoint(); p6.setPosition((x + hw, y + h, z + hw))
            p7 = geo.createPoint(); p7.setPosition((x - hw, y + h, z + hw))
            
            faces = [
                (p0, p1, p2, p3), (p7, p6, p5, p4),
                (p0, p4, p5, p1), (p1, p5, p6, p2),
                (p2, p6, p7, p3), (p3, p7, p4, p0)
            ]
            for f_pts in faces:
                poly = geo.createPolygon()
                for pt in f_pts:
                    poly.addVertex(pt)
                poly.setAttribValue("Cd", col)
                poly.setAttribValue("zone", zone)
                poly.setAttribValue("mesh_name", m_name)
                poly.setAttribValue("building_id", b_id)
'''

PYTHON_TRANSIT_CODE = r'''
import csv, os, hou
ROOT = hou.pwd().parent().evalParm("blueprintRoot")   # project root ($HIP/..)
geo = hou.pwd().geometry()
geo.clear()
geo.addAttrib(hou.attribType.Prim, "layer", "")
geo.addAttrib(hou.attribType.Prim, "edge_type", "")
geo.addAttrib(hou.attribType.Prim, "capacity", 0.0)
geo.addAttrib(hou.attribType.Prim, "Cd", (1.0, 0.8, 0.1))

edges_csv = ROOT + "/output/istrorigan_graph_edges.csv"
nodes_csv = ROOT + "/output/istrorigan_graph_nodes.csv"
if os.path.exists(nodes_csv) and os.path.exists(edges_csv):
    node_pos = {}
    with open(nodes_csv, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            node_pos[int(r["node_id"])] = (float(r["x"]) * 0.01, float(r["z"]) * 0.01 + 2.0, float(r["y"]) * 0.01)

    type_colors = {
        "MaglevRail": (0.1, 0.8, 1.0),
        "EvacTube": (0.2, 1.0, 0.4),
        "ServiceTrunk": (1.0, 0.6, 0.1),
        "PneumaticConduit": (0.9, 0.3, 0.8),
    }

    with open(edges_csv, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            u, v = int(r["start_node"]), int(r["end_node"])
            if u in node_pos and v in node_pos:
                p1 = geo.createPoint(); p1.setPosition(node_pos[u])
                p2 = geo.createPoint(); p2.setPosition(node_pos[v])
                poly = geo.createPolygon()
                poly.addVertex(p1)
                poly.addVertex(p2)
                e_type = r.get("edge_type", "MaglevRail")
                poly.setAttribValue("edge_type", e_type)
                poly.setAttribValue("layer", e_type)
                poly.setAttribValue("Cd", type_colors.get(e_type, (1.0, 0.8, 0.1)))
                poly.setAttribValue("capacity", float(r.get("max_throughput", 1000.0)))
'''

PYTHON_SCATTER_CODE = r'''
import csv, os, hou
ROOT = hou.pwd().parent().evalParm("blueprintRoot")   # project root ($HIP/..)
geo = hou.pwd().geometry()
geo.clear()
geo.addAttrib(hou.attribType.Point, "instance", "")
geo.addAttrib(hou.attribType.Point, "Cd", (0.9, 0.8, 0.4))
geo.addAttrib(hou.attribType.Point, "scale", 1.0)
geo.addAttrib(hou.attribType.Point, "yaw", 0.0)
geo.addAttrib(hou.attribType.Point, "zone", "")

cd_map = {
    "ZONE_CORE_CITADEL": (1.0, 0.85, 0.3),
    "ZONE_FACULTY_OCEANIC": (0.1, 0.5, 0.9),
    "ZONE_FACULTY_BIOSPHERE": (0.2, 0.85, 0.4),
    "ZONE_FACULTY_CLIMATE": (0.7, 0.9, 1.0),
    "ZONE_FACULTY_MEGASTRUCT": (0.9, 0.6, 0.2),
    "ZONE_FACULTY_ARCHIVES": (0.6, 0.3, 0.8),
    "ZONE_FACULTY_ABYSSAL": (0.15, 0.35, 0.55),
    "ZONE_FACULTY_DIPLOMACY": (0.95, 0.92, 0.85),
    "ZONE_FACULTY_MEDICINE": (0.95, 0.4, 0.5),
    "ZONE_CLEARANCE_WATERWAY": (1.0, 0.3, 0.3),
    "ZONE_HARBOR_BERTH": (0.6, 0.65, 0.7),
}

props_csv = ROOT + "/output/istrorigan_scatter_props.csv"
if os.path.exists(props_csv):
    with open(props_csv, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            pt = geo.createPoint()
            pt.setPosition((float(r["x_cm"]) * 0.01, float(r["z_cm"]) * 0.01 + 0.5, float(r["y_cm"]) * 0.01))
            zone = r.get("zone_tag", "")
            pt.setAttribValue("instance", r.get("mesh", ""))
            pt.setAttribValue("zone", zone)
            scale_val = float(r["scale"]) if r.get("scale") else 1.0
            pt.setAttribValue("scale", scale_val)
            pt.setAttribValue("yaw", float(r.get("yaw_deg", 0.0)))
            pt.setAttribValue("Cd", cd_map.get(zone, (0.9, 0.8, 0.4)))
'''

PYTHON_LATTICE_CODE = r'''
import csv, os, hou
ROOT = hou.pwd().parent().evalParm("blueprintRoot")   # project root ($HIP/..)
geo = hou.pwd().geometry()
geo.clear()
geo.addAttrib(hou.attribType.Point, "Cd", (1.0, 1.0, 1.0))
geo.addAttrib(hou.attribType.Point, "zone", "")
geo.addAttrib(hou.attribType.Point, "petal_idx", 0)
geo.addAttrib(hou.attribType.Point, "faculty", "")
geo.addAttrib(hou.attribType.Point, "clearance_gap", 0.0)

cd_map = {
    "ZONE_CORE_CITADEL": (1.0, 0.85, 0.3),
    "ZONE_FACULTY_OCEANIC": (0.1, 0.5, 0.9),
    "ZONE_FACULTY_BIOSPHERE": (0.2, 0.85, 0.4),
    "ZONE_FACULTY_CLIMATE": (0.7, 0.9, 1.0),
    "ZONE_FACULTY_MEGASTRUCT": (0.9, 0.6, 0.2),
    "ZONE_FACULTY_ARCHIVES": (0.6, 0.3, 0.8),
    "ZONE_FACULTY_ABYSSAL": (0.15, 0.35, 0.55),
    "ZONE_FACULTY_DIPLOMACY": (0.95, 0.92, 0.85),
    "ZONE_FACULTY_MEDICINE": (0.95, 0.4, 0.5),
    "ZONE_CLEARANCE_WATERWAY": (1.0, 0.3, 0.3),
    "ZONE_HARBOR_BERTH": (0.6, 0.65, 0.7),
}

lattice_csv = ROOT + "/output/istrorigan_lattice_meters.csv"
if os.path.exists(lattice_csv):
    with open(lattice_csv, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            pt = geo.createPoint()
            pt.setPosition((float(r["x_m"]), float(r["z_m"]), float(r["y_m"])))
            zone = r.get("zone_tag", "")
            pt.setAttribValue("zone", zone)
            pt.setAttribValue("petal_idx", int(r.get("petal_index", -1)))
            pt.setAttribValue("faculty", r.get("faculty_name", ""))
            pt.setAttribValue("clearance_gap", float(r.get("clearance_gap_m", 0.0)))
            pt.setAttribValue("Cd", cd_map.get(zone, (0.8, 0.8, 0.8)))
'''
# endregion


def build_master_istrorigan_system(save_hip=False, rebuild=False):
    hou = get_hou()
    obj = hou.node("/obj")

    # region 1. MASTER SUBNET & PROMOTED PARAMETER INTERFACE
    old = obj.node("istrorigan_city")
    if old and not rebuild:
        # never wipe a scene that may hold hand-tuned parms; upgrade it instead
        print("[!] /obj/istrorigan_city already exists - nothing rebuilt.")
        print("[!] Upgrade in place:  update_in_place.py   (keeps your parm values)")
        print("[!] Full wipe + rebuild: pass 'rebuild' (discards every edit in this node)")
        return old
    if old:
        old.destroy()
    old_ctrl = obj.node("istrorigan_CTRL")
    if old_ctrl:
        old_ctrl.destroy()

    geo = obj.createNode("geo", "istrorigan_city")
    sub = geo.createNode("subnet", "istrorigan")
    sub.setComment("ISTRORIGAN MEGASTRUCTURE (YEAR 4205)\n"
                   "Sovereign Sanctuary of the 17 Great States.\n"
                   "Unified 9-Part Modular Architecture.\n"
                   "Select me, all master controls are on the parameter interface.\n"
                   "RMB -> Create Digital Asset when ready.")
    sub.setGenericFlag(hou.nodeFlag.DisplayComment, True)
    sub.setColor(hou.Color((0.12, 0.60, 0.92)))

    ptg = hou.ParmTemplateGroup()

    # Tab 0: Master Global Controls & State Machine (03.01)
    ptg.append(TAB("tab_master", "Master Global", [
        SIMPLE("f_master_state", "03.01 Global State Machine (Year 4205)", [
            I("annualCycleState", "Annual Cycle (0=Spring, 1=Summer Dive, 2=Autumn Diplomacy, 3=Winter Dive)", 0, 0, 3),
            F("submergeAmount", "Global Submersion Amount (0=Surface, 1=Abyssal Depth)", 0.0, 0.0, 1.0),
            F("currentDepthMeters", "Current Submersion Depth (m)", 0.0, -1000.0, 0.0),
            F("openAmount", "Academic Petals Open / Tuck Amount", 1.0, 0.0, 1.0),
            B("emergencyState", "Council Emergency Quarantine & Lockdown", 0),
            B("councilQuorumActive", "Council of Ten Quorum Active (>= 7/10)", 1),
            F("barrierEnergyLoad", "Hex Barrier Shield Energy Load", 0.85, 0.0, 1.0),
            B("deepSeaMode", "Abyssal Hydrostatic Pressure Mode", 0),
        ]),
        SIMPLE("f_master_xform", "City Scale & Viewport Modes", [
            F("cityScale", "City Global Scale", 1.0, 0.05, 5.0),
            B("fastViewport", "Fast Viewport (Optimized low-res proxies & curves)", 0),
            B("showGuide", "Show Guides (45m Waterway Clearances + Petal Axes)", 1),
            SEP("s_mst1"),
            B("doSubdiv", "Subdivide Meshes", 0, dw="{ fastViewport == 1 }"),
            I("subdivIter", "Subdiv Iterations", 1, 0, 3, dw="{ fastViewport == 1 }"),
        ]),
    ]))

    # Append Part Tabs from each module (All 14 Subsystems)
    ptg.append(part01_apex_spire.get_parm_templates())
    ptg.append(part02_hex_barrier.get_parm_templates())
    ptg.append(part03_academic_petals.get_parm_templates())
    ptg.append(part04_bio_domes.get_parm_templates())
    ptg.append(part05_stamen_pylons.get_parm_templates())
    ptg.append(part06_canal_bridges.get_parm_templates())
    ptg.append(part07_outer_docks.get_parm_templates())
    ptg.append(part08_submerged_rings.get_parm_templates())
    ptg.append(part09_seabed_vault.get_parm_templates())
    ptg.append(part11_stem_collar.get_parm_templates())
    ptg.append(part12_ring_hydraulics.get_parm_templates())
    ptg.append(part13_elevator_core.get_parm_templates())
    ptg.append(part14_bulkhead_gates.get_parm_templates())
    ptg.append(part15_subcouncil_halls.get_parm_templates())
    ptg.append(pcg_stages.get_parm_templates())

    # Unified Master Color Palette Tab
    ptg.append(TAB("tab_color", "Color & Shading", [
        SIMPLE("f_palette", "Megastructure Material Colors", [
            COL("colCitadel", "Citadel Spire (Ivory Gold)", (0.95, 0.92, 0.82)),
            COL("colPetalHull", "Petal Hull (Pure White)", (0.94, 0.95, 0.98)),
            COL("colStamens", "Stamens (Burnished Gold)", (1.0, 0.78, 0.15)),
            COL("colBioDome", "Bio-Dome Glass (Emerald)", (0.25, 0.90, 0.55)),
            COL("colBridges", "Canal Bridges (Alloy Grey)", (0.75, 0.78, 0.82)),
            COL("colDocks", "Floating Docks (Marine Grey)", (0.80, 0.82, 0.86)),
            COL("colSubmerged", "Submerged Rings (Abyssal Teal)", (0.15, 0.45, 0.65)),
            COL("colVault", "Vault Armor (Titanium Basalt)", (0.28, 0.32, 0.38)),
            COL("colBarrier", "Hex Barrier (Luminous Cyan)", (0.10, 0.85, 1.0)),
            COL("colCollar", "Stem Collar (Heavy Alloy)", (0.32, 0.38, 0.44)),
            COL("colHydraulics", "Ring Hydraulics (Polished Alloy)", (0.75, 0.78, 0.82)),
            COL("colElevator", "Deep-Sea Elevator (Titanium Core)", (0.22, 0.26, 0.30)),
            COL("colBulkhead", "Bulkhead Gates (Naval Armor)", (0.35, 0.36, 0.38)),
            COL("colSubcouncil", "Sub-Council Halls (Limestone & Glass)", (0.85, 0.84, 0.82)),
        ]),
    ]))

    # Data-Driven Urban & Buildings Tab
    ptg.append(TAB("tab_urban", "Urban & Buildings", [
        SIMPLE("f_urban_toggles", "Data-Driven Urban Layers", [
            B("showBuildings", "Show Buildings (LEGACY baked CSV - replaced by PCG Stage 4-5)", 0),
            B("showTransit", "Show PCG Transit & Resource Graph (Stage 3, live)", 1),
            B("showScatter", "Show Props (LEGACY baked CSV - replaced by PCG Stage 5)", 0),
            B("showLattice", "Show PCG Zoned Lattice (Stage 1-2, live)", 1),
            SEP("s_urb1"),
            B("useHighResParts", "Use Baked OBJ Meshes (legacy, not updated)", 0),
        ]),
    ]))

    # Unreal Engine 5 Game-Ready Export Tab
    ptg.append(TAB("tab_engine", "Engine Export", [
        SIMPLE("f_engine_out", "Unreal Engine 5 Game-Ready Chain", [
            B("gameReady", "Game-Ready Output (UV + Triangulate + UE Scale)", 0),
            F("exportScale", "Export Scale (UE = 100, DCC = 1)", 1.0, 0.001, 1000.0),
            B("triangulate", "Triangulate Meshes", 1, dw="{ gameReady == 0 }"),
            B("doUV", "Auto UV Unwrap", 1, dw="{ gameReady == 0 }"),
            STR("targetMaterial", "Unreal Material Path (-> unreal_material)"),
            STR("instanceAssetPath", "Instance Asset Path (output 2)"),
        ]),
    ]))

    sub.setParmTemplateGroup(ptg)
    part03_academic_petals.setup_expressions(sub)
    if hou.hipFile.isNewFile() and not save_hip:
        sub.parm("blueprintRoot").set(PROJECT_ROOT)   # $HIP/.. once saved in output/
    # endregion

    # region 2. 14 MODULAR SUBSYSTEM INSTANTIATION
    root = mk(sub, "null", "root", -2, 0, "root generator trigger")

    out_spire, nodes_spire = part01_apex_spire.build_nodes(sub, root, col=0, row=1, cref=CREF)
    out_barrier, nodes_barrier = part02_hex_barrier.build_nodes(sub, root, col=2, row=1, cref=CREF)
    out_petals, nodes_petals = part03_academic_petals.build_nodes(sub, root, col=4, row=1, cref=CREF)
    out_domes, nodes_domes = part04_bio_domes.build_nodes(sub, root, col=6, row=1, cref=CREF)
    out_stamens, nodes_stamens = part05_stamen_pylons.build_nodes(sub, root, col=8, row=1, cref=CREF)
    out_bridges, nodes_bridges = part06_canal_bridges.build_nodes(sub, root, col=10, row=1, cref=CREF)
    out_docks, nodes_docks = part07_outer_docks.build_nodes(sub, root, col=12, row=1, cref=CREF)
    out_submerged, nodes_submerged = part08_submerged_rings.build_nodes(sub, root, col=14, row=1, cref=CREF)
    out_vault, nodes_vault = part09_seabed_vault.build_nodes(sub, root, col=16, row=1, cref=CREF)
    out_collar, nodes_collar = part11_stem_collar.build_nodes(sub, root, col=18, row=1, cref=CREF)
    out_hydraulics, nodes_hydraulics = part12_ring_hydraulics.build_nodes(sub, root, col=20, row=1, cref=CREF)
    out_elevator, nodes_elevator = part13_elevator_core.build_nodes(sub, root, col=22, row=1, cref=CREF)
    out_bulkhead, nodes_bulkhead = part14_bulkhead_gates.build_nodes(sub, root, col=24, row=1, cref=CREF)
    out_subcouncil, nodes_subcouncil = part15_subcouncil_halls.build_nodes(sub, root, col=26, row=1, cref=CREF)

    # 14 Canonical High-Res OBJ Meshes with Procedural Fallback Switches
    subsystem_objs = [
        ("file_spire", "`chs(\"../blueprintRoot\")`/output/parts/01_SYS_APEX_SPIRE.obj", out_spire, 0, nodes_spire),
        ("file_barrier", "`chs(\"../blueprintRoot\")`/output/parts/02_SYS_HEX_BARRIER.obj", out_barrier, 2, nodes_barrier),
        ("file_petals", "`chs(\"../blueprintRoot\")`/output/parts/03_SYS_ACADEMIC_PETALS_8X.obj", out_petals, 4, nodes_petals),
        ("file_domes", "`chs(\"../blueprintRoot\")`/output/parts/04_SYS_BIO_DOMES.obj", out_domes, 6, nodes_domes),
        ("file_stamens", "`chs(\"../blueprintRoot\")`/output/parts/05_SYS_STAMEN_PYLONS.obj", out_stamens, 8, nodes_stamens),
        ("file_bridges", "`chs(\"../blueprintRoot\")`/output/parts/06_SYS_CANAL_BRIDGES.obj", out_bridges, 10, nodes_bridges),
        ("file_docks", "`chs(\"../blueprintRoot\")`/output/parts/07_SYS_OUTER_FLOATING_DOCK.obj", out_docks, 12, nodes_docks),
        ("file_submerged", "`chs(\"../blueprintRoot\")`/output/parts/08_SYS_STEM_RINGS.obj", out_submerged, 14, nodes_submerged),
        ("file_vault", "`chs(\"../blueprintRoot\")`/output/parts/09_SYS_SEABED_VAULT.obj", out_vault, 16, nodes_vault),
        ("file_collar", "`chs(\"../blueprintRoot\")`/output/parts/11_SYS_CORE_STEM_COLLAR.obj", out_collar, 18, nodes_collar),
        ("file_hydraulics", "`chs(\"../blueprintRoot\")`/output/parts/12_SYS_INTER_RING_HYDRAULICS.obj", out_hydraulics, 20, nodes_hydraulics),
        ("file_elevator", "`chs(\"../blueprintRoot\")`/output/parts/13_SYS_DEEPSEA_ELEVATOR_CORE.obj", out_elevator, 22, nodes_elevator),
        ("file_bulkhead", "`chs(\"../blueprintRoot\")`/output/parts/14_SYS_EMERGENCY_BULKHEAD_GATES.obj", out_bulkhead, 24, nodes_bulkhead),
        ("file_subcouncil", "`chs(\"../blueprintRoot\")`/output/parts/15_SYS_SUBCOUNCIL_HALLS_8X.obj", out_subcouncil, 26, nodes_subcouncil),
    ]

    final_subsystem_outs = []
    for f_name, obj_path, vex_out, col_idx, node_list in subsystem_objs:
        f_node = mk(sub, "file", f_name, col_idx + 0.8, 3, "High-Res OBJ Mesh")
        setp(f_node, "file", obj_path)
        # OBJs are exported Z-up (UE convention); rotate into Houdini Y-up
        zup_fix = mk(sub, "xform", "zup_" + f_name, col_idx + 0.8, 3.5, "Z-up OBJ -> Y-up")
        setp(zup_fix, "rx", -90.0)
        zup_fix.setInput(0, f_node)
        sw_node = mk(sub, "switch", "sw_" + f_name, col_idx, 4, "Procedural vs High-Res")
        sw_node.setInput(0, vex_out)
        sw_node.setInput(1, zup_fix)
        sete(sw_node, "input", 'ch("../useHighResParts")')
        node_list.extend([f_node, zup_fix, sw_node])
        final_subsystem_outs.append(sw_node)
    # endregion

    # region 2B. DATA-DRIVEN URBAN LAYERS & PROCEDURAL PCG CHAINS
    # Modular Buildings (7,623 Floors / 1,280 Buildings)
    py_bld = mk(sub, "python", "py_buildings", 28, 1, "7,623 modular building floors")
    setp(py_bld, "python", PYTHON_BUILDINGS_CODE)
    bld_attribs = wr(sub, "bld_metadata_attribs", 1,
                     's@unreal_material = "MI_Istrorigan_ModularArchitecture";\n'
                     'f@structural_mass_tons = 400.0;\n'
                     'f@buoyant_lift_kn = 554.0;',
                     28, 2, py_bld, comment="Building Material & Physics Metadata", cref=CREF)
    null_bld_off = mk(sub, "null", "null_bld_off", 29, 2, "bld off")
    sw_bld = mk(sub, "switch", "sw_buildings", 28, 3, "buildings toggle")
    sw_bld.setInput(0, null_bld_off)
    sw_bld.setInput(1, bld_attribs)
    sete(sw_bld, "input", 'ch("../showBuildings")')

    # Transit & Maglev Network (136 Routes)
    py_transit = mk(sub, "python", "py_transit", 30, 1, "136 transit routes")
    setp(py_transit, "python", PYTHON_TRANSIT_CODE)
    transit_tubes = mk(sub, "polywire", "transit_conduits_3d", 30, 2, "3D Maglev Cylindrical Conduit Sweep")
    setp(transit_tubes, "radius", 1.8)
    setp(transit_tubes, "segs", 6)
    transit_tubes.setInput(0, py_transit)
    null_transit_off = mk(sub, "null", "null_transit_off", 31, 2, "transit off")
    sw_transit = mk(sub, "switch", "sw_transit", 30, 3, "transit toggle")
    sw_transit.setInput(0, null_transit_off)
    sw_transit.setInput(1, transit_tubes)
    sete(sw_transit, "input", 'ch("../showTransit")')

    # Zone Scatter Props (2,356 Props)
    py_scatter = mk(sub, "python", "py_scatter", 32, 1, "2,356 zone props")
    setp(py_scatter, "python", PYTHON_SCATTER_CODE)
    scatter_orient = wr(sub, "scatter_orient_solver", 2,
                        'float rad = radians(f@yaw);\n'
                        '@N = normalize(set(sin(rad), 0.0, cos(rad)));\n'
                        '@up = set(0.0, 1.0, 0.0);\n'
                        'f@pscale = clamp(f@scale, 0.5, 2.5);\n'
                        's@unreal_instance = s@instance;',
                        32, 2, py_scatter, comment="Orientation & Instancing Solver", cref=CREF)
    null_scatter_off = mk(sub, "null", "null_scatter_off", 33, 2, "scatter off")
    sw_scatter = mk(sub, "switch", "sw_scatter", 32, 3, "scatter toggle")
    sw_scatter.setInput(0, null_scatter_off)
    sw_scatter.setInput(1, scatter_orient)
    sete(sw_scatter, "input", 'ch("../showScatter")')

    # PCG Stages 0-2: blueprint -> polar lattice on live petal decks -> zoning
    pcg = pcg_stages.build_nodes(sub, root, out_petals, col=34, row=1, cref=CREF)
    pcg_view, pcg_nodes = pcg["lattice_view"], pcg["nodes"]
    # Stage 3 graph replaces the baked-CSV transit layer
    sw_transit.setInput(1, pcg["graph_view"])
    null_lattice_off = mk(sub, "null", "null_lattice_off", 35, 5, "lattice off")
    sw_lattice = mk(sub, "switch", "sw_lattice", 34, 6, "lattice toggle")
    sw_lattice.setInput(0, null_lattice_off)
    sw_lattice.setInput(1, pcg_view)
    sete(sw_lattice, "input", 'ch("../showLattice")')
    # endregion

    # region 3. MASTER MERGE & OPENSUBDIV SHADING
    city_merge = mk(sub, "merge", "city_merge", 13, 6, "merge all 14 parts & 4 urban layers")
    for i, s_out in enumerate(final_subsystem_outs):
        city_merge.setInput(i, s_out)
    n_sub = len(final_subsystem_outs)
    city_merge.setInput(n_sub + 0, sw_bld)
    city_merge.setInput(n_sub + 1, sw_transit)
    city_merge.setInput(n_sub + 2, sw_scatter)
    city_merge.setInput(n_sub + 3, sw_lattice)

    city_subdiv = mk(sub, "subdivide", "city_subdiv", 15, 7, "OpenSubdiv")
    city_subdiv.setInput(0, city_merge)
    sete(city_subdiv, "iterations", 'ch("../subdivIter")')

    subdiv_sw = mk(sub, "switch", "subdiv_switch", 13, 7, "subdiv gate")
    subdiv_sw.setInput(0, city_merge)
    subdiv_sw.setInput(1, city_subdiv)
    sete(subdiv_sw, "input", 'if(ch("../fastViewport"), 0, ch("../doSubdiv"))')

    city_normal = mk(sub, "normal", "city_normal", 13, 8, "shading normals")
    city_normal.setInput(0, subdiv_sw)
    setp(city_normal, "cuspangle", 45.0)

    master_xform = mk(sub, "xform", "master_scale", 13, 9, "global city scale")
    master_xform.setInput(0, city_normal)
    sete(master_xform, "scale", 'ch("../cityScale")')
    # endregion

    # region 4. UNREAL ENGINE 5 GAME-READY EXPORT CHAIN
    gr_tri = mk(sub, "divide", "gr_triangulate", 15, 11, "triangulate convex 3-sides")
    setp(gr_tri, "convex", 1)
    setp(gr_tri, "numsides", 3)
    gr_tri.setInput(0, master_xform)

    gr_tri_sw = mk(sub, "switch", "gr_tri_switch", 13, 11, "triangulate gate")
    gr_tri_sw.setInput(0, master_xform)
    gr_tri_sw.setInput(1, gr_tri)
    sete(gr_tri_sw, "input", 'if(ch("../gameReady"), ch("../triangulate"), 0)')

    gr_uv = mk(sub, "uvunwrap", "gr_uvunwrap", 15, 12, "auto UV atlas")
    gr_uv.setInput(0, gr_tri_sw)

    gr_uv_sw = mk(sub, "switch", "gr_uv_switch", 13, 12, "UV gate")
    gr_uv_sw.setInput(0, gr_tri_sw)
    gr_uv_sw.setInput(1, gr_uv)
    sete(gr_uv_sw, "input", 'if(ch("../gameReady"), ch("../doUV"), 0)')

    gr_mat = wr(sub, "gr_material_attribs", 0, load_vex("gr_material.vfl"),
                15, 13, gr_uv_sw, comment="unreal_material slot", cref=CREF)

    gr_scale = mk(sub, "xform", "gr_export_scale", 15, 14, "meters -> UE cm (x100)")
    gr_scale.setInput(0, gr_mat)
    sete(gr_scale, "scale", 'ch("../exportScale")')

    gr_sw = mk(sub, "switch", "gameready_switch", 13, 14, "raw vs game-ready")
    gr_sw.setInput(0, master_xform)
    gr_sw.setInput(1, gr_scale)
    sete(gr_sw, "input", 'ch("../gameReady")')

    # OUTPUT 0: MASTER MESH
    OUT_MAIN = mk(sub, "output", "OUT", 13, 16, "output 0 -> Istrorigan Mesh")
    OUT_MAIN.setInput(0, gr_sw)
    setp(OUT_MAIN, "outputidx", 0)
    OUT_MAIN.setDisplayFlag(True)
    OUT_MAIN.setRenderFlag(True)
    # endregion

    # region 5. GUIDE GEOMETRY & INSTANCING OUTPUTS
    guide_w = wr(sub, "guide_network_gen", 0, load_vex("guide_network.vfl"), 36, 1, root,
                 comment="45m Waterway Clearances & Concentric Radii", cref=CREF)
    guide_off = mk(sub, "null", "guide_off", 37, 2, "empty")
    guide_sw = mk(sub, "switch", "guide_switch", 36, 3, "showGuide")
    guide_sw.setInput(0, guide_off)
    guide_sw.setInput(1, guide_w)
    sete(guide_sw, "input", 'ch("../showGuide")')
    try:
        guide_sw.setTemplateFlag(True)
    except Exception:
        pass

    OUT_GUIDE = mk(sub, "output", "OUT_guide", 36, 5, "output 1 -> Guide Overlays")
    OUT_GUIDE.setInput(0, guide_sw)
    setp(OUT_GUIDE, "outputidx", 1)

    inst_pt = mk(sub, "add", "instance_point", 19, 16, "instancing point")
    setp(inst_pt, "points", 1)
    inst_w = wr(sub, "instance_attribs", 2, load_vex("instance_attribs.vfl"),
                19, 17, inst_pt, comment="unreal_instance attribute", cref=CREF)

    OUT_INST = mk(sub, "output", "OUT_instance", 19, 18, "output 2 -> Instancing point")
    OUT_INST.setInput(0, inst_w)
    setp(OUT_INST, "outputidx", 2)
    # endregion

    # region 6. DISK EXPORT ROPS & NETWORK BOXES
    rop_fbx = mk(sub, "rop_fbx", "EXPORT_fbx", 13, 18, "Save to Disk -> FBX")
    rop_fbx.setInput(0, OUT_MAIN)
    setp(rop_fbx, "sopoutput", "`chs(\"../blueprintRoot\")`/output/istrorigan_city.fbx")
    ENGINE_EXTRA = []
    try:
        rop_gltf = mk(sub, "rop_gltf", "EXPORT_gltf", 15, 18, "Save to Disk -> glTF / GLB")
        rop_gltf.setInput(0, OUT_MAIN)
        setp(rop_gltf, "file", "`chs(\"../blueprintRoot\")`/output/istrorigan_city.glb")
        ENGINE_EXTRA.append(rop_gltf)
    except Exception:
        pass

    netbox(sub, "box_spire", "01. APEX SPIRE (+600M)", (0.35, 0.30, 0.22), nodes_spire)
    netbox(sub, "box_barrier", "02. HEX BARRIER DOME", (0.12, 0.38, 0.45), nodes_barrier)
    netbox(sub, "box_petals", "03. 8 PETALS (45M CLEARANCE)", (0.24, 0.32, 0.42), nodes_petals)
    netbox(sub, "box_domes", "04. BIO-DOMES & HABITATS", (0.18, 0.40, 0.32), nodes_domes)
    netbox(sub, "box_stamens", "05. 70 STAMEN PYLONS", (0.42, 0.35, 0.15), nodes_stamens)
    netbox(sub, "box_bridges", "06. CANAL BRIDGES", (0.30, 0.35, 0.40), nodes_bridges)
    netbox(sub, "box_docks", "07. OUTER FLOATING DOCKS", (0.28, 0.36, 0.34), nodes_docks)
    netbox(sub, "box_submerged", "08. 12 SUBMERGED RINGS", (0.16, 0.28, 0.38), nodes_submerged)
    netbox(sub, "box_vault", "09. SEABED VAULT (-1,000M)", (0.12, 0.20, 0.28), nodes_vault)
    netbox(sub, "box_collar", "10. CORE-TO-STEM RING 1 COLLAR", (0.24, 0.32, 0.38), nodes_collar)
    netbox(sub, "box_hydraulics", "11. INTER-RING HYDRAULICS", (0.22, 0.35, 0.32), nodes_hydraulics)
    netbox(sub, "box_elevator", "12. DEEP-SEA ELEVATOR CORE", (0.18, 0.28, 0.35), nodes_elevator)
    netbox(sub, "box_bulkhead", "13. EMERGENCY BULKHEAD GATES", (0.35, 0.32, 0.22), nodes_bulkhead)
    netbox(sub, "box_subcouncil", "14. 8 SUB-COUNCIL HALLS", (0.32, 0.28, 0.40), nodes_subcouncil)
    netbox(sub, "box_assemble", "15. ASSEMBLE & NORMALS", (0.32, 0.30, 0.40),
           [city_merge, city_subdiv, subdiv_sw, city_normal, master_xform])
    netbox(sub, "box_engine", "16. ENGINE & ROPS", (0.20, 0.38, 0.35),
           [gr_tri, gr_tri_sw, gr_uv, gr_uv_sw, gr_mat, gr_scale, gr_sw, OUT_MAIN, inst_pt, inst_w, OUT_INST, rop_fbx] + ENGINE_EXTRA)
    netbox(sub, "box_guide", "17. 45M GUIDES (TEMPLATE ON)", (0.42, 0.40, 0.18),
           [guide_w, guide_off, guide_sw, OUT_GUIDE])
    netbox(sub, "box_urban", "18. MODULAR BUILDINGS & URBAN DATA", (0.22, 0.42, 0.28),
           [py_bld, bld_attribs, null_bld_off, sw_bld,
            py_transit, transit_tubes, null_transit_off, sw_transit,
            py_scatter, scatter_orient, null_scatter_off, sw_scatter,
            null_lattice_off, sw_lattice] + pcg_nodes)

    # STICKY NOTE 1: Architectural Canon Specifications
    note_canon = (
        "====================================================================\n"
        "ISTRORIGAN MEGASTRUCTURE (YEAR 4205) - CANON SPECIFICATIONS\n"
        "====================================================================\n"
        "Sovereign Sanctuary of the 17 Great States\n\n"
        "[01] Apex Spire & Citadel of Ten: Elevation +600m\n"
        "     - Sculptural twin-blade split apex with central void chamber\n"
        "     - Splaying organic root buttresses rooted into circular podium\n"
        "[02] Hex Barrier Dome: Outer Radius R=1,500m, Height +650m\n"
        "     - Geodesic honeycomb forcefield & atmospheric deflection\n"
        "[03] 8 Academic Petals: Length 950m, Max Beam 420m, Hull Draft 18m\n"
        "     - Flared aerodynamic rim (+45m) with recessed pink accent lip\n"
        "     - Guaranteed >= 45.0m navigable inter-petal seaway clearance\n"
        "[04] Botanical Bio-Domes & Habitats:\n"
        "     - Even petals: Geodesic glass domes (R=60m) with flora & faculty\n"
        "     - Odd petals: Sculptural stepped open-air amphitheaters\n"
        "[05] 70 Golden Stamen Energy Pylons: Perimeter R=220m, Height 45m\n"
        "     - Conical defense array with apex plasma emitter arcs\n"
        "[06] Inter-Petal Skybridges: Radial Distance 560m, Torus R=15m\n"
        "     - Tubular ring transit portals spanning 45m waterways\n"
        "[07] Outer Floating Pontoons & Marina: Spine 95m x 14m, Gangway 65m\n"
        "     - Modular pontoons floating outside petal flanks (ZERO crowding)\n"
        "[08] 12 Submerged Hydraulic Ballast Rings: Depths down to -900m\n"
        "     - Cascading sea terraces with electric cyan bioluminescent steps\n"
        "[09] Abyssal Doomsday Vault & Bedrock Claws: Depth -1,000m\n"
        "     - Armored bunker (R=120m) & 8 hydraulic seismic dampener claws\n"
        "[10] Core-to-Stem Ring 1 Collar: Z=0m to -50m, R=95m to 82m\n"
        "     - 8 radial shear key gussets & deep-sea hydrostatic gasket\n"
        "[11] Inter-Ring Hydraulic Couplers: 12 tiers x 8 dual cylinders\n"
        "     - Telescopic expansion damping and articulated utility bridges\n"
        "[12] Vertical Deep-Sea Elevator Core: Elev +120m to -980m (1.1km)\n"
        "     - 4 maglev guide tracks & 5 pressurized airlock transit hubs\n"
        "[13] Emergency Watertight Bulkhead Gates: 8 fairways at R=165m\n"
        "     - Twin gantry towers & movable guillotine blast isolation doors\n"
        "[14] 8 Faculty Sub-Council Assembly Halls: Radial distance 380m\n"
        "     - Stepped limestone podium, cantilever clamshell, faculty beacons\n"
        "===================================================================="
    )
    stickynote(sub, "note_canon_specs", note_canon,
               col=-4.5, row=0.5, width=6.2, height=6.5,
               color=(0.10, 0.14, 0.22), text_color=(0.95, 0.96, 1.0))

    # STICKY NOTE 2: Assembly & OpenSubdiv Pipeline
    note_subdiv = (
        "====================================================\n"
        "SUBSYSTEM MERGE & OPENSUBDIV PIPELINE\n"
        "====================================================\n"
        "* city_merge combines all 14 modular procedural streams\n"
        "  AND 4 data-driven urban layers (18 streams total)\n"
        "* OpenSubdiv quad subdivision controlled by:\n"
        "  - doSubdiv (toggle) & subdivIter (0-3 iterations)\n"
        "  - fastViewport: instantly bypasses heavy subdiv for 60fps\n"
        "* Shading Normals computed with 45.0-degree cusp angle\n"
        "* Master Scale transform scales entire megastructure\n"
        "====================================================\n"
    )
    stickynote(sub, "note_assemble_pipeline", note_subdiv,
               col=9.5, row=6.5, width=4.8, height=3.0,
               color=(0.18, 0.14, 0.24), text_color=(0.92, 0.94, 1.0))

    # STICKY NOTE 3: Unreal Engine 5 & Game-Ready Export Chain
    note_engine = (
        "====================================================\n"
        "UNREAL ENGINE 5 GAME-READY EXPORT CHAIN\n"
        "====================================================\n"
        "* OUTPUT 0: Master Game-Ready City Mesh\n"
        "  - Triangulation (Convex 3-sides, clean planar splitting)\n"
        "  - Auto UV Atlas unwrapping (gr_uvunwrap)\n"
        "  - Attribute 'unreal_material' assigned for master shader\n"
        "  - Coordinate conversion: Meters -> Unreal cm (x100)\n"
        "* OUTPUT 1: 45m Waterway Clearance Guides (Template ON)\n"
        "* OUTPUT 2: Level Instancing Point Cloud\n"
        "  - 'unreal_instance' attribute for sub-level spawning\n"
        "* DISK EXPORT ROPS:\n"
        "  - EXPORT_fbx -> istrorigan_city.fbx\n"
        "  - EXPORT_gltf -> istrorigan_city.glb\n"
        "===================================================="
    )
    stickynote(sub, "note_engine_export", note_engine,
               col=3.8, row=11.5, width=4.8, height=4.2,
               color=(0.10, 0.18, 0.15), text_color=(0.88, 1.0, 0.92))

    # STICKY NOTE 4: 45m Waterway Clearance & Fairways
    note_fairways = (
        "====================================================\n"
        "45m SEAWAY NAVIGATION CLEARANCE RULES\n"
        "====================================================\n"
        "* Inter-petal waterway fairways maintain >= 45.0m width\n"
        "* Ensures unhindered passage for oceanographic research\n"
        "  vessels, freight barges, and civilian sea shuttles\n"
        "* Tubular skybridges elevated with overhead clearance\n"
        "* Outer floating docks moored radially in open water\n"
        "* Guide network overlay active in viewport (yellow/cyan)\n"
        "===================================================="
    )
    stickynote(sub, "note_waterway_clearance", note_fairways,
               col=27.0, row=6.5, width=4.8, height=3.2,
               color=(0.08, 0.18, 0.22), text_color=(0.85, 0.96, 1.0))

    # STICKY NOTE 5: Modular Buildings & Urban Data
    note_urban = (
        "====================================================\n"
        "DATA-DRIVEN URBAN LAYERS & MODULAR ARCHITECTURE\n"
        "====================================================\n"
        "* 1,280 Modular Buildings (7,623 stacked floors):\n"
        "  - Zoned by 10 Academic Faculties & Core Citadel\n"
        "  - Attributes: Cd (zoning tint), zone, building_id, mesh_name\n"
        "* 136 Transit & Maglev Network Routes:\n"
        "  - 76 Inter-Petal Stations & Terminals\n"
        "  - MaglevRail, EvacTube, ServiceTrunk conduits\n"
        "* 2,356 Zone Micro-Scatter Props:\n"
        "  - Navigational buoys, atmospheric monitors, streetlights\n"
        "* 4,983 Spatial Anchor Lattice Points:\n"
        "  - Metrological reference anchors & clearance verification\n"
        "* 9 High-Res Canonical OBJ Meshes:\n"
        "  - Instant toggle via 'useHighResParts' parameter\n"
        "===================================================="
    )
    stickynote(sub, "note_urban_data", note_urban,
               col=18.0, row=4.8, width=7.2, height=4.0,
               color=(0.14, 0.26, 0.18), text_color=(0.90, 1.0, 0.92))

    sub.setDisplayFlag(True)
    sub.setRenderFlag(True)
    # endregion

    # region 7. DIGITAL ASSET (HDA) & HIP FILE SAVER
    asset = sub
    try:
        _ext = {hou.licenseCategoryType.Commercial: "hda",
                hou.licenseCategoryType.Indie: "hdalc",
                hou.licenseCategoryType.Apprentice: "hdanc"}.get(
                    hou.licenseCategoryType(), "hda")
        hda_path = OUTPUT_DIR + "/istrorigan_city.%s" % _ext
        asset = sub.createDigitalAsset(
            name="istrorigan_city",
            hda_file_name=hda_path,
            description="Istrorigan Megastructure (Year 4205)",
            min_num_inputs=0,
            max_num_inputs=0,
        )
        try:
            asset.setName("istrorigan", unique_name=True)
        except Exception:
            pass
        print("[+] HDA created -> %s" % hda_path)
    except Exception as e:
        print("=" * 64)
        print("[*] Subnet 'istrorigan' ready with full promoted parameter tabs.")
        print("[*] RMB 'istrorigan' -> 'Create Digital Asset' to save HDA.")
        print("=" * 64)

    try:
        geo.layoutChildren()
    except Exception:
        pass

    asset.setCurrent(True, clear_all_selected=True)
    print("[+] DONE -> %s" % asset.path())

    if save_hip:
        hip_path = OUTPUT_DIR + "/istrorigan_city.hip"
        hou.hipFile.save(hip_path)
        print("[+] Saved HIP file -> %s" % hip_path)

    return asset
    # endregion


# region MAIN EXECUTION ENTRY POINT
if __name__ == "__main__":
    build_master_istrorigan_system(save_hip="save" in sys.argv, rebuild="rebuild" in sys.argv)
# endregion

