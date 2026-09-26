"""
================================================================================
 ISTRORIGAN - PART 15: 8 FACULTY SUB-COUNCIL ASSEMBLY HALLS (03.06 / 03.03)
================================================================================
 Canon: 03.06_FLOWER_ZONE & 03.03_PETAL_STRUCTURE
 8 Civic Assembly Amphitheaters and Faculty Legislative Chambers located on each
 petal with cantilever clamshell canopies and glowing faculty crest beacons.
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

VEX_SUBCOUNCIL_HALLS = load_vex("part15_subcouncil_halls.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_subcouncil", "Sub-Council Halls", [
        SIMPLE("f_subcouncil_geom", "8 Faculty Sub-Council Halls (03.06)", [
            F("subcouncilRadialDist", "Assembly Hall Radial Distance (m)", 380.0, 200.0, 700.0),
            F("subcouncilPodiumR", "Plaza Podium Radius (m)", 42.0, 15.0, 80.0),
            F("subcouncilCanopyH", "Canopy Arch Elevation (m)", 48.0, 20.0, 100.0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    subcouncil_w = wr(
        parent, "sys15_subcouncil_halls", 0, VEX_SUBCOUNCIL_HALLS,
        col, row, root_input,
        comment="8 Faculty Sub-Council Assembly Halls (03.06 / 03.03)", cref=cref
    )
    all_nodes = [subcouncil_w]
    return subcouncil_w, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part15_subcouncil_halls")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(get_parm_templates())
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_subcouncil", "PART 15: 8 SUB-COUNCIL HALLS", (0.32, 0.28, 0.40), nodes)
    print("[+] Part 15 Sub-Council Halls build complete -> /obj/part15_subcouncil_halls")


if __name__ == "__main__":
    standalone_build()
# endregion
