"""
================================================================================
 ISTRORIGAN - PART 14: EMERGENCY BULKHEAD GATES (03.19)
================================================================================
 Canon: 03.19_STATE_DEPENDENCY & 03.18_STRUCTURE_CLEARANCE
 8 Emergency Watertight Floodgate Towers & Canal Isolation Blast Doors
 straddling the 45m navigable fairways at the inner petal canals (R=165m).
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

VEX_BULKHEAD_GATES = load_vex("part14_bulkhead_gates.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_bulkhead", "Bulkhead Gates", [
        SIMPLE("f_bulkhead_geom", "Emergency Watertight Floodgates (03.19)", [
            F("bulkheadCloseAmount", "Bulkhead Gate Close Amount", 0.0, 0.0, 1.0),
            B("bulkheadLockdownOverride", "Local Bulkhead Lockdown Override", 0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    bulkhead_w = wr(
        parent, "sys14_bulkhead_gates", 0, VEX_BULKHEAD_GATES,
        col, row, root_input,
        comment="Emergency Watertight Bulkhead Doors & Canal Isolation Gates (03.19)", cref=cref
    )
    all_nodes = [bulkhead_w]
    return bulkhead_w, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part14_bulkhead_gates")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(get_parm_templates())
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_bulkhead", "PART 14: EMERGENCY BULKHEAD GATES", (0.35, 0.32, 0.22), nodes)
    print("[+] Part 14 Bulkhead Gates build complete -> /obj/part14_bulkhead_gates")


if __name__ == "__main__":
    standalone_build()
# endregion
