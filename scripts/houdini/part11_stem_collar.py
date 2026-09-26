"""
================================================================================
 ISTRORIGAN - PART 11: CORE-TO-STEM RING 1 COLLAR INTERFACE (03.15)
================================================================================
 Canon: 03.15_FLOWER_STEM_CONNECTION & 03.02.07 Center Coupling
 Structural interface collar transferring radial loads and vertical weight
 between Citadel Core (Z=0m) and Submerged Ring 1 (Z=-45m).
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

VEX_STEM_COLLAR = load_vex("part11_stem_collar.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_collar", "Stem Collar", [
        SIMPLE("f_collar_geom", "Core-to-Stem Ring 1 Interface Collar (03.15)", [
            F("collarTopZ", "Collar Top Elevation Z (m)", 0.0, -20.0, 50.0),
            F("collarBotZ", "Collar Bottom Elevation Z (m)", -50.0, -120.0, 0.0),
            F("collarTopRadius", "Collar Top Flange Radius (m)", 95.0, 50.0, 200.0),
            F("collarBotRadius", "Collar Bottom Interface Radius (m)", 82.0, 40.0, 180.0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    collar_w = wr(
        parent, "sys11_stem_collar", 0, VEX_STEM_COLLAR,
        col, row, root_input,
        comment="Core-to-Stem Ring 1 Structural Ring Interface (03.15)", cref=cref
    )
    all_nodes = [collar_w]
    return collar_w, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part11_stem_collar")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(get_parm_templates())
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_collar", "PART 11: CORE-TO-STEM RING 1 COLLAR", (0.24, 0.32, 0.38), nodes)
    print("[+] Part 11 Stem Collar build complete -> /obj/part11_stem_collar")


if __name__ == "__main__":
    standalone_build()
# endregion
