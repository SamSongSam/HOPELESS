"""
================================================================================
ISTRORIGAN MEGASTRUCTURE - HOUDINI MASTER MODULAR PARTS BUILDER
================================================================================
Run inside Houdini:
  1. Open Houdini (19.5, 20.0, 20.5+)
  2. Windows > Python Source Editor (or Python Shell)
  3. Paste this script and click Apply / Run
  Or via terminal: hython scripts/houdini_modular_parts_builder.py

What this builds in /obj:
  /obj/ISTRORIGAN_MASTER
    ├── [01] PART_01_APEX_SPIRE       (Citadel +600m & Council of Ten Spire)
    ├── [02] PART_02_HEX_BARRIER      (Hexagonal Forcefield Dome R=1,500m)
    ├── [03] PART_03_ACADEMIC_PETALS  (8 Articulated Petals, Scoop Hull, 45m Gap)
    ├── [04] PART_04_BIO_DOMES        (Botanical Geodesic Domes & Living Habitats)
    ├── [05] PART_05_STAMEN_PYLONS    (70 Golden Stamen Energy Towers Array)
    ├── [06] PART_06_CANAL_BRIDGES    (45m Waterway Gaps & Inter-Petal Skybridges)
    ├── [07] PART_07_OUTER_DOCKS      (Compact Floating Pontoon Jetties, Canon Ref)
    ├── [08] PART_08_STEM_RINGS       (12 Submerged Expanding Telescopic Rings)
    ├── [09] PART_09_SEABED_VAULT     (Abyssal Claws & Doomsday Knowledge Vault -1km)
    └── [MERGE] MERGE_ALL_PARTS ----> OUT_ISTRORIGAN_FINAL
================================================================================
"""

# region MODULE IMPORTS & ENVIRONMENT
import os
import sys

try:
    import hou  # type: ignore
    HOUDINI_AVAILABLE = True
except ImportError:
    HOUDINI_AVAILABLE = False
# endregion


# region HOUDINI MODULAR NETWORK BUILDER
def build_houdini_istrorigan():
    if not HOUDINI_AVAILABLE:
        print("[!] Houdini 'hou' module not found in standalone Python environment.")
        print("[!] Run this script inside Houdini (Python Source Editor) or via 'hython'.")
        return False

    obj = hou.node("/obj")
    
    # 1. Clean previous network if exists
    old_master = obj.node("ISTRORIGAN_MASTER")
    if old_master:
        old_master.destroy()

    master = obj.createNode("geo", "ISTRORIGAN_MASTER")
    master.setColor(hou.Color((0.15, 0.70, 0.95)))
    master.setComment("ISTRORIGAN MEGASTRUCTURE (YEAR 4205)\n"
                      "Modular 9-Part Procedural Architecture\n"
                      "Ready for Solaris/Karma, SOP Modeling & Rigging.")
    master.setGenericFlag(hou.nodeFlag.DisplayComment, True)

    # 2. Master Parameter Interface (Promoted Controls)
    ptg = master.parmTemplateGroup()

    def F(n, l, d, lo, hi):
        return hou.FloatParmTemplate(n, l, 1, default_value=(d,), min=lo, max=hi)

    def I(n, l, d, lo, hi):
        return hou.IntParmTemplate(n, l, 1, default_value=(d,), min=lo, max=hi)

    def B(n, l, d):
        return hou.ToggleParmTemplate(n, l, default_value=bool(d))

    def TAB(name, label, items):
        f = hou.FolderParmTemplate(name, label, folder_type=hou.folderType.Tabs)
        for it in items:
            f.addParmTemplate(it)
        return f

    def SIMPLE(name, label, items):
        f = hou.FolderParmTemplate(name, label, folder_type=hou.folderType.Simple)
        for it in items:
            f.addParmTemplate(it)
        return f

    # Master UI Tabs
    ptg.append(TAB("tab_global", "Global Controls", [
        SIMPLE("f_master", "Master Transforms", [
            F("masterScale", "Global Scale", 1.0, 0.1, 5.0),
            B("submersionActive", "Submerged Dive Mode", 0),
            F("petalPitchDeg", "Petal Pitch Angle (deg)", 2.5, 0.0, 45.0),
            F("barrierOpacity", "Hex Barrier Energy (30%-100%)", 0.35, 0.0, 1.0),
        ]),
        SIMPLE("f_visibility", "Parts Solo / Visibility", [
            B("vis_spire", "Show SYS_01: Apex Spire", 1),
            B("vis_barrier", "Show SYS_02: Hex Barrier", 1),
            B("vis_petals", "Show SYS_03: Academic Petals", 1),
            B("vis_biodomes", "Show SYS_04: Bio-Domes", 1),
            B("vis_pylons", "Show SYS_05: Stamen Pylons", 1),
            B("vis_bridges", "Show SYS_06: Canal Bridges", 1),
            B("vis_docks", "Show SYS_07: Outer Floating Docks", 1),
            B("vis_rings", "Show SYS_08: Submerged Rings", 1),
            B("vis_vault", "Show SYS_09: Seabed Vault", 1),
        ])
    ]))
    master.setParmTemplateGroup(ptg)

    # Resolve project output parts directory
    # Default relative to project root or absolute
    base_dir = "d:/2/OWN/HOPELESS/output/parts"

    parts_def = [
        # ROW 0: UPPER CITADEL & DEFENSE
        {
            "id": "SYS_01_APEX_SPIRE",
            "name": "PART_01_APEX_SPIRE",
            "file": "01_SYS_APEX_SPIRE.obj",
            "color": (0.95, 0.92, 0.82), # Warm Ivory Gold
            "col": 0, "row": 0, "layer": "citadel",
            "vis_parm": "vis_spire"
        },
        {
            "id": "SYS_02_HEX_BARRIER",
            "name": "PART_02_HEX_BARRIER",
            "file": "02_SYS_HEX_BARRIER.obj",
            "color": (0.10, 0.85, 1.0),  # Luminous Cyan
            "col": 1, "row": 0, "layer": "citadel",
            "vis_parm": "vis_barrier"
        },
        {
            "id": "SYS_05_STAMEN_PYLONS",
            "name": "PART_05_STAMEN_PYLONS",
            "file": "05_SYS_STAMEN_PYLONS.obj",
            "color": (1.0, 0.78, 0.15),  # Burnished Stamen Gold
            "col": 2, "row": 0, "layer": "citadel",
            "vis_parm": "vis_pylons"
        },

        # ROW 2: SURFACE MARITIME & CAMPUS
        {
            "id": "SYS_03_ACADEMIC_PETALS",
            "name": "PART_03_ACADEMIC_PETALS",
            "file": "03_SYS_ACADEMIC_PETALS_8X.obj",
            "color": (0.92, 0.94, 0.98), # Pure Futuristic White
            "col": 0, "row": 2, "layer": "surface",
            "vis_parm": "vis_petals"
        },
        {
            "id": "SYS_04_BIO_DOMES",
            "name": "PART_04_BIO_DOMES",
            "file": "04_SYS_BIO_DOMES.obj",
            "color": (0.25, 0.90, 0.55), # Emerald Botanical Glass
            "col": 1, "row": 2, "layer": "surface",
            "vis_parm": "vis_biodomes"
        },
        {
            "id": "SYS_06_CANAL_BRIDGES",
            "name": "PART_06_CANAL_BRIDGES",
            "file": "06_SYS_CANAL_BRIDGES.obj",
            "color": (0.75, 0.85, 0.95), # Composite Glass Skybridge
            "col": 2, "row": 2, "layer": "surface",
            "vis_parm": "vis_bridges"
        },
        {
            "id": "SYS_07_OUTER_DOCKS",
            "name": "PART_07_OUTER_DOCKS",
            "file": "07_SYS_OUTER_FLOATING_DOCK.obj",
            "color": (0.80, 0.82, 0.86), # Modular Floating Pontoon Grey
            "col": 3, "row": 2, "layer": "surface",
            "vis_parm": "vis_docks"
        },

        # ROW 4: SUBSEA BALLAST & BEDROCK ANCHORS
        {
            "id": "SYS_08_STEM_RINGS",
            "name": "PART_08_STEM_RINGS",
            "file": "08_SYS_STEM_RINGS.obj",
            "color": (0.15, 0.45, 0.65), # Deep Oceanic Metallic Teal
            "col": 0, "row": 4, "layer": "subsea",
            "vis_parm": "vis_rings"
        },
        {
            "id": "SYS_09_SEABED_VAULT",
            "name": "PART_09_SEABED_VAULT",
            "file": "09_SYS_SEABED_VAULT.obj",
            "color": (0.25, 0.28, 0.35), # Abyssal Bedrock Titanium
            "col": 1, "row": 4, "layer": "subsea",
            "vis_parm": "vis_vault"
        }
    ]

    col_w, row_h = 3.6, 2.6
    merge_node = master.createNode("merge", "MERGE_ALL_PARTS")
    merge_node.setPosition(hou.Vector2(1.5 * col_w, -row_h * 5.5))
    merge_node.setColor(hou.Color((0.9, 0.5, 0.1)))
    merge_node.setComment("Merge all 9 procedural parts")
    merge_node.setGenericFlag(hou.nodeFlag.DisplayComment, True)

    # Build Each Part Subnetwork inside ISTRORIGAN_MASTER
    citadel_nodes = []
    surface_nodes = []
    subsea_nodes = []

    for p in parts_def:
        sub = master.createNode("subnet", p["name"])
        sub.setPosition(hou.Vector2(p["col"] * col_w, -p["row"] * row_h))
        sub.setColor(hou.Color(p["color"]))
        sub.setComment(f"Subnetwork: {p['id']}\nMesh: {p['file']}")
        sub.setGenericFlag(hou.nodeFlag.DisplayComment, True)

        # Inside Subnet: File SOP -> AttributeCreate -> Color -> Output
        sub_file = sub.createNode("file", "read_obj")
        obj_path = f"{base_dir}/{p['file']}"
        sub_file.parm("file").set(obj_path)
        sub_file.setPosition(hou.Vector2(0, 0))
        sub_file.setComment(f"Read mesh from disk: {p['file']}")
        sub_file.setGenericFlag(hou.nodeFlag.DisplayComment, True)

        # Part ID Attribute
        sub_attr = sub.createNode("attribcreate", "set_part_id")
        sub_attr.parm("name1").set("part_id")
        sub_attr.parm("type1").set(3)  # string
        sub_attr.parm("string1").set(p["id"])
        sub_attr.setInput(0, sub_file)
        sub_attr.setPosition(hou.Vector2(0, -1.5))
        sub_attr.setComment("Stamp 'part_id' primitive attribute")
        sub_attr.setGenericFlag(hou.nodeFlag.DisplayComment, True)

        # Color SOP
        sub_col = sub.createNode("color", "base_color")
        sub_col.parm("colorr").set(p["color"][0])
        sub_col.parm("colorg").set(p["color"][1])
        sub_col.parm("colorb").set(p["color"][2])
        sub_col.setInput(0, sub_attr)
        sub_col.setPosition(hou.Vector2(0, -3.0))
        sub_col.setComment("Viewport preview color")
        sub_col.setGenericFlag(hou.nodeFlag.DisplayComment, True)

        # Output Null
        sub_out = sub.createNode("null", f"OUT_{p['id']}")
        sub_out.setInput(0, sub_col)
        sub_out.setPosition(hou.Vector2(0, -4.5))
        sub_out.setColor(hou.Color((0.0, 1.0, 0.5)))
        sub_out.setComment(f"Output: {p['id']}")
        sub_out.setGenericFlag(hou.nodeFlag.DisplayComment, True)
        sub_out.setDisplayFlag(True)
        sub_out.setRenderFlag(True)

        # Outside: Connect through a Switch controlled by the master visibility toggle
        sw = master.createNode("switch", f"switch_{p['id']}")
        sw.setComment(f"Toggle {p['vis_parm']}")
        sw.setGenericFlag(hou.nodeFlag.DisplayComment, True)
        null_empty = master.createNode("null", f"empty_{p['id']}")
        null_empty.setComment("Empty bypass")
        null_empty.setGenericFlag(hou.nodeFlag.DisplayComment, True)
        null_empty.setPosition(hou.Vector2(p["col"] * col_w + 1.2, -p["row"] * row_h - 1.0))

        sw.setPosition(hou.Vector2(p["col"] * col_w, -p["row"] * row_h - 1.2))
        sw.setInput(0, null_empty)
        sw.setInput(1, sub)
        # Link visibility toggle
        sw.parm("input").setExpression(f"ch('../../{p['vis_parm']}')")

        merge_node.setNextInput(sw)

        # Track for Network Boxes
        part_group = [sub, null_empty, sw]
        if p["layer"] == "citadel":
            citadel_nodes.extend(part_group)
        elif p["layer"] == "surface":
            surface_nodes.extend(part_group)
        elif p["layer"] == "subsea":
            subsea_nodes.extend(part_group)

    # Master Transform connected after Merge
    master_xform = master.createNode("xform", "MASTER_SCALE_XFORM")
    master_xform.setInput(0, merge_node)
    master_xform.setPosition(hou.Vector2(1.5 * col_w, -row_h * 6.5))
    master_xform.parm("scale").setExpression("ch('../masterScale')")
    master_xform.setComment("Master megastructure scale")
    master_xform.setGenericFlag(hou.nodeFlag.DisplayComment, True)

    # Final Output Null
    out_final = master.createNode("null", "OUT_ISTRORIGAN_FINAL")
    out_final.setInput(0, master_xform)
    out_final.setPosition(hou.Vector2(1.5 * col_w, -row_h * 7.5))
    out_final.setColor(hou.Color((0.0, 1.0, 0.0)))
    out_final.setComment("Final Combined Megastructure Output")
    out_final.setGenericFlag(hou.nodeFlag.DisplayComment, True)
    out_final.setDisplayFlag(True)
    out_final.setRenderFlag(True)

    master_nodes = [merge_node, master_xform, out_final]

    # Helpers for Network Boxes & Sticky Notes
    def make_netbox(parent, name, label, color, nodes):
        b = parent.createNetworkBox(name)
        b.setComment(label)
        b.setColor(hou.Color(color))
        for n in nodes:
            if n is not None:
                b.addNode(n)
        try:
            b.fitAroundContents()
        except Exception:
            pass
        return b

    def make_sticky(parent, name, text, pos, size, color, text_color):
        try:
            note = parent.createStickyNote(name)
            note.setPosition(hou.Vector2(pos[0], pos[1]))
            note.setSize(hou.Vector2(size[0], size[1]))
            note.setText(text)
            note.setColor(hou.Color(color))
            if hasattr(note, "setTextColor"):
                note.setTextColor(hou.Color(text_color))
            return note
        except Exception:
            return None

    # Houdini Network Boxes grouping each architectural layer
    make_netbox(master, "box_citadel", "01. UPPER CITADEL & FORCEFIELD DEFENSE",
                (0.35, 0.30, 0.20), citadel_nodes)
    make_netbox(master, "box_surface", "02. SURFACE CAMPUS & MARITIME HABITATS",
                (0.20, 0.35, 0.40), surface_nodes)
    make_netbox(master, "box_subsea", "03. SUB-AQUATIC BALLAST & BEDROCK ANCHORS",
                (0.14, 0.22, 0.32), subsea_nodes)
    make_netbox(master, "box_output", "04. MASTER MERGE & SCALED OUTPUT CHAIN",
                (0.38, 0.28, 0.16), master_nodes)

    # Sticky Note 1: Architecture Specifications & Registry
    note_overview = (
        "====================================================\n"
        "ISTRORIGAN MASTER MODULAR ASSET REGISTRY\n"
        "====================================================\n"
        "Sovereign Sanctuary of the 17 Great States (Year 4205)\n\n"
        "* 9 Autonomous Modular Subnetworks:\n"
        "  [01] Apex Spire & Citadel of Ten (+600m)\n"
        "  [02] Hexagonal Barrier Dome (R=1,500m)\n"
        "  [03] 8 Articulated Academic Petals (45m Waterways)\n"
        "  [04] Botanical Bio-Domes & Habitats\n"
        "  [05] 70 Golden Stamen Energy Pylons (R=220m)\n"
        "  [06] Inter-Petal Tubular Skybridges\n"
        "  [07] Outer Floating Pontoon Jetties (No Crowding)\n"
        "  [08] 12 Submerged Hydraulic Ballast Rings (-900m)\n"
        "  [09] Abyssal Doomsday Vault & Bedrock Claws (-1,000m)\n\n"
        "* Geometry Source: d:/2/OWN/HOPELESS/output/parts/\n"
        "===================================================="
    )
    make_sticky(master, "note_overview", note_overview,
                (-5.5, 0.0), (5.0, 6.2), (0.10, 0.14, 0.22), (0.95, 0.96, 1.0))

    # Sticky Note 2: Promoted Parameters & Pipeline Guide
    note_controls = (
        "====================================================\n"
        "PROMOTED MASTER CONTROLS & PIPELINE\n"
        "====================================================\n"
        "* Select /obj/ISTRORIGAN_MASTER to access promoted UI\n"
        "* Master Scale: Scales combined megastructure\n"
        "* Solo / Visibility toggles for all 9 subsystems\n"
        "* Submersion Mode & Barrier Energy opacity parameters\n"
        "* Each subnet stamps 'part_id' primitive attribute\n"
        "* Ready for Solaris/Karma USD staging & LOD pipeline\n"
        "===================================================="
    )
    make_sticky(master, "note_controls", note_controls,
                (col_w * 3.5 + 0.5, -row_h * 4.5), (5.2, 4.5),
                (0.12, 0.20, 0.18), (0.90, 1.0, 0.94))
    print("================================================================================")
    print("  [+] SUCCESS: Created /obj/ISTRORIGAN_MASTER with 9 Modular Part Subnetworks!")
    print("  [+] Output Null: /obj/ISTRORIGAN_MASTER/OUT_ISTRORIGAN_FINAL")
    print("  [+] All 9 parts connected to master visibility & scale parameters.")
    print("================================================================================")
    return True
# endregion


# region MAIN ENTRY
if __name__ == "__main__":
    build_houdini_istrorigan()
# endregion
