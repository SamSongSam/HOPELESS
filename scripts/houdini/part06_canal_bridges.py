"""
================================================================================
 ISTRORIGAN - PART 06: TUBULAR RING SKYBRIDGES (AAA CINEMATIC QUALITY)
================================================================================
 Exact Match to LOTUS_ACADEMY_CITY.jpg:
   - High-Speed Maglev & Pedestrian Transit Portals spanning 45m Seaways
   - Aerodynamic Cylindrical Torus Rings with 360-degree Equatorial Glass Gallery
   - Structural Pier Anchors rooted into the Petal Coaming Rim
   - High Overhead Clearance for Surface Ocean Barges & Shuttles
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

VEX_SCULPTURAL_BRIDGES = load_vex("part06_canal_bridges.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_bridges", "Canal Bridges", [
        SIMPLE("f_bridge_cfg", "Tubular Ring Skybridges (Canon Ref)", [
            B("showBridges", "Show Inter-Petal Bridges", 1),
            F("tubeRingRadius", "Ring Outer Radius (m)", 15.0, 6.0, 30.0),
            F("tubeThickness", "Shell Wall Thickness (m)", 2.8, 0.5, 6.0),
            F("bridgeRadialDist", "Radial Placement (m)", 560.0, 250.0, 950.0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    bridges_w = wr(
        parent, "sys06_canal_bridges", 0, VEX_SCULPTURAL_BRIDGES,
        col, row, root_input,
        comment="Tubular Ring Skybridges with Glass Galleries (Canon Ref)", cref=cref
    )
    bridges_off = mk(parent, "null", "bridges_off", col + 1, row + 1, "empty (OFF)")
    bridges_sw = mk(parent, "switch", "bridges_switch", col, row + 2, "showBridges")
    bridges_sw.setInput(0, bridges_off)
    bridges_sw.setInput(1, bridges_w)
    sete(bridges_sw, "input", f'ch("{cref}showBridges")')
    
    all_nodes = [bridges_w, bridges_off, bridges_sw]
    return bridges_sw, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part06_canal_bridges")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(TAB("tab_core_petals", "Core Settings", [
        I("petalCount", "Petal Count", 8, 4, 16)
    ]))
    ptg.append(get_parm_templates())
    ptg.append(TAB("tab_color", "Color", [
        COL("colBridges", "Canal Bridges (Alloy Grey)", (0.75, 0.78, 0.82))
    ]))
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_bridges", "PART 06: SCULPTURAL TUBULAR BRIDGES", (0.30, 0.35, 0.40), nodes)

    note_txt = (
        "====================================================\n"
        "PART 06: TUBULAR RING SKYBRIDGES (CANON REF)\n"
        "====================================================\n"
        "* High-Speed Maglev & Pedestrian Inter-Petal Portals\n"
        "* Spans strictly across 45m Navigable Seaways\n"
        "* Radial Placement: 560m, Ring Outer Radius: 15m\n"
        "* Shell Wall Thickness: 2.8m with 360-deg Glass Gallery\n"
        "* High Overhead Vessel Clearance for Marine Barges\n"
        "===================================================="
    )
    stickynote(geo, "note_part06_specs", note_txt, col=2.8, row=0.5,
               width=5.2, height=3.5, color=(0.14, 0.18, 0.22), text_color=(0.90, 0.95, 1.0))
    print("[+] Part 06 Sculptural Tubular Skybridges build complete -> /obj/part06_canal_bridges")


if __name__ == "__main__":
    standalone_build()
# endregion
