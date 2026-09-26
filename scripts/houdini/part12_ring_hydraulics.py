"""
================================================================================
 ISTRORIGAN - PART 12: INTER-RING HYDRAULIC EXPANSION DAMPERS (03.14)
================================================================================
 Canon: 03.14_RING_CONNECTION & 03.12_STEM_TELESCOPIC_SYSTEM
 12-Tier Telescopic Hydraulic Damper Cylinders & Articulated Couplers
 linking adjacent submerged ballast rings.
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

VEX_RING_HYDRAULICS = load_vex("part12_ring_hydraulics.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_hydraulics", "Ring Hydraulics", [
        SIMPLE("f_hydraulics_geom", "Inter-Ring Hydraulic Expansion Dampers (03.14)", [
            F("hydraulicExtension", "Hydraulic Extension Amount", 0.0, 0.0, 1.0),
            F("damperRadius", "Cylinder Body Radius (m)", 1.8, 0.5, 4.0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    hydraulics_w = wr(
        parent, "sys12_ring_hydraulics", 0, VEX_RING_HYDRAULICS,
        col, row, root_input,
        comment="Inter-Ring Hydraulic Dampers & Couplers (03.14)", cref=cref
    )
    all_nodes = [hydraulics_w]
    return hydraulics_w, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part12_ring_hydraulics")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(get_parm_templates())
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_hydraulics", "PART 12: INTER-RING HYDRAULICS", (0.22, 0.35, 0.32), nodes)
    print("[+] Part 12 Ring Hydraulics build complete -> /obj/part12_ring_hydraulics")


if __name__ == "__main__":
    standalone_build()
# endregion
