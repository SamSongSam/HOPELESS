"""
================================================================================
 ISTRORIGAN - PART 13: VERTICAL DEEP-SEA TRANSIT ELEVATOR CORE (03.13)
================================================================================
 Canon: 03.13_STEM_TRANSPORT
 Deep-sea vertical maglev transit spine from Citadel (+120m) to Seabed (-1,000m)
 featuring 4 guide tracks and 5 pressurized airlock transit hubs.
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

VEX_ELEVATOR_CORE = load_vex("part13_elevator_core.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_elevator", "Elevator Core", [
        SIMPLE("f_elevator_geom", "Vertical Deep-Sea Transit Elevator (03.13)", [
            F("elevatorTopZ", "Elevator Top Elevation Z (m)", 120.0, 0.0, 300.0),
            F("elevatorBotZ", "Elevator Bottom Elevation Z (m)", -980.0, -1200.0, -500.0),
            F("elevatorRadius", "Central Shaft Radius (m)", 12.0, 5.0, 30.0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    elevator_w = wr(
        parent, "sys13_elevator_core", 0, VEX_ELEVATOR_CORE,
        col, row, root_input,
        comment="Vertical Deep-Sea Transit Elevator Core (03.13)", cref=cref
    )
    all_nodes = [elevator_w]
    return elevator_w, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part13_elevator_core")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(get_parm_templates())
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_elevator", "PART 13: DEEP-SEA ELEVATOR CORE", (0.18, 0.28, 0.35), nodes)
    print("[+] Part 13 Elevator Core build complete -> /obj/part13_elevator_core")


if __name__ == "__main__":
    standalone_build()
# endregion
