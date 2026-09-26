"""
================================================================================
 ISTRORIGAN - PART 08: CASCADING SUBMERGED AQUA TIERS (AAA CINEMATIC QUALITY)
================================================================================
 Exact Match to LOTUS_ACADEMY_CITY.jpg:
   - Spectacular Concentric Stepped Terraces in Foreground Sea Channel
   - Bioluminescent Bullnose Step Lips emitting vibrant Electric Cyan (#00e5ff)
   - Radial Hydraulic Spillway Fins & Stabilizing Underwater Buttresses
   - 12 Deep-Sea Telescopic High-Pressure Titanium Rings descending to -900m
   - Clean Quad Topography for Oceanic Caustics & Karma SSS Shading
================================================================================
"""

# region MODULE IMPORTS & VEX BINDING
import sys
import os

try:
    from .helpers import (
        mk, setp, sete, wr, netbox, stickynote, load_vex,
        F, I, B, COL, SEP, SIMPLE, TAB, create_standalone_geo, get_hou
    )
except ImportError:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from helpers import (
        mk, setp, sete, wr, netbox, stickynote, load_vex,
        F, I, B, COL, SEP, SIMPLE, TAB, create_standalone_geo, get_hou
    )

VEX_SCULPTURAL_SUBMERGED = load_vex("part08_submerged_rings.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_submerged", "Submerged Stem", [
        SIMPLE("f_stem_cfg", "Cascading Aqua Tiers & Stem (Canon Ref)", [
            B("showSubmerged", "Show Submerged Structure", 1),
            I("ringTierCount", "Telescopic Deep Rings", 12, 3, 24),
            F("surfaceNeckRadius", "Neck Radius (m)", 80.0, 30.0, 150.0),
            F("seabedAbyssalRadius", "Abyssal Radius (m)", 350.0, 100.0, 600.0),
            F("totalSubmergedDepth", "Total Depth (m)", -900.0, -1500.0, -200.0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    submerged_w = wr(
        parent, "sys08_submerged_rings", 0, VEX_SCULPTURAL_SUBMERGED,
        col, row, root_input,
        comment="Cascading Glowing Cyan Tiers & 12 Telescopic Rings (Canon Ref)", cref=cref
    )
    submerged_off = mk(parent, "null", "submerged_off", col + 1, row + 1, "empty (OFF)")
    submerged_sw = mk(parent, "switch", "submerged_switch", col, row + 2, "showSubmerged")
    submerged_sw.setInput(0, submerged_off)
    submerged_sw.setInput(1, submerged_w)
    sete(submerged_sw, "input", f'ch("{cref}showSubmerged")')
    
    all_nodes = [submerged_w, submerged_off, submerged_sw]
    return submerged_sw, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part08_submerged_rings")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(get_parm_templates())
    ptg.append(TAB("tab_color", "Color", [
        COL("colSubmerged", "Submerged Rings (Abyssal Teal)", (0.15, 0.45, 0.65))
    ]))
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_rings", "PART 08: SCULPTURAL SUBMERGED TIERS", (0.16, 0.28, 0.38), nodes)

    note_txt = (
        "====================================================\n"
        "PART 08: CASCADING AQUA TIERS & STEM RINGS\n"
        "====================================================\n"
        "* Spectacular Concentric Stepped Terraces in Sea\n"
        "* Bioluminescent Cyan Bullnose Step Lips (#00e5ff)\n"
        "* Radial Hydraulic Spillway Fins & Stabilizers\n"
        "* 12 Telescopic High-Pressure Titanium Ballast Rings\n"
        "* Descends from Waterline (0m) to Deep Sea (-900m)\n"
        "* Clean Quad Topology for Karma Ocean Caustics\n"
        "===================================================="
    )
    stickynote(geo, "note_part08_specs", note_txt, col=2.8, row=0.5,
               width=5.4, height=3.8, color=(0.10, 0.16, 0.22), text_color=(0.85, 0.95, 1.0))
    print("[+] Part 08 Sculptural Submerged Tiers build complete -> /obj/part08_submerged_rings")


if __name__ == "__main__":
    standalone_build()
# endregion
