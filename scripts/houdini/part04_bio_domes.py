"""
================================================================================
 ISTRORIGAN - PART 04: BOTANICAL DOMES & AMPHITHEATERS (AAA QUALITY)
================================================================================
 Exact Match to LOTUS_ACADEMY_CITY.jpg:
   - Alternating Petal Layout:
       * Even Petals: Geodesic Glass Bio-Domes with internal vegetation and wrapping campus wings
       * Odd Petals: Sculptural Terraced Amphitheaters with curved student forums
   - Curved futuristic faculty buildings and terraced gardens conforming to petal contours
   - OpenSubdiv-ready quad and tri topology with PBR glass alpha and glowing frames
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

VEX_SCULPTURAL_DOMES = load_vex("part04_bio_domes.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_biodomes", "Bio-Domes & Habitats", [
        SIMPLE("f_dome_cfg", "Sculptural Domes & Amphitheaters (Canon Ref)", [
            B("showBioDomes", "Show Bio-Domes & Amphitheaters", 1),
            F("domeRadius", "Bio-Dome Radius (m)", 60.0, 20.0, 120.0),
            F("domeRadialDist", "Feature Distance on Petal (m)", 680.0, 250.0, 1000.0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    domes_w = wr(
        parent, "sys04_bio_domes", 0, VEX_SCULPTURAL_DOMES,
        col, row, root_input,
        comment="Sculptural Domes & Open-Air Amphitheaters (Canon Ref)", cref=cref
    )
    domes_off = mk(parent, "null", "biodomes_off", col + 1, row + 1, "empty (OFF)")
    domes_sw = mk(parent, "switch", "biodomes_switch", col, row + 2, "showBioDomes")
    domes_sw.setInput(0, domes_off)
    domes_sw.setInput(1, domes_w)
    sete(domes_sw, "input", f'ch("{cref}showBioDomes")')
    
    all_nodes = [domes_w, domes_off, domes_sw]
    return domes_sw, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part04_bio_domes")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(TAB("tab_petals_core", "Core Settings", [
        I("petalCount", "Petal Count", 8, 4, 16)
    ]))
    ptg.append(get_parm_templates())
    ptg.append(TAB("tab_color", "Color", [
        COL("colBioDome", "Bio-Dome Glass (Emerald)", (0.25, 0.90, 0.55))
    ]))
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_domes", "PART 04: SCULPTURAL DOMES & AMPHITHEATERS", (0.18, 0.40, 0.32), nodes)

    note_txt = (
        "====================================================\n"
        "PART 04: BOTANICAL DOMES & AMPHITHEATERS\n"
        "====================================================\n"
        "* Alternating Petal Architecture (Canon Ref):\n"
        "  - Even Petals: Geodesic Glass Bio-Domes (R=60m)\n"
        "    with internal flora and wrapped campus wings\n"
        "  - Odd Petals: Sculptural Terraced Amphitheaters\n"
        "    with curved student forums & botanical steps\n"
        "* Curved Futuristic Faculty Buildings & Plazas\n"
        "* Emerald Glass Shading with Glowing Rib Frames\n"
        "===================================================="
    )
    stickynote(geo, "note_part04_specs", note_txt, col=2.8, row=0.5,
               width=5.2, height=3.5, color=(0.10, 0.20, 0.16), text_color=(0.88, 1.0, 0.92))
    print("[+] Part 04 Sculptural Domes & Amphitheaters build complete -> /obj/part04_bio_domes")


if __name__ == "__main__":
    standalone_build()
# endregion
