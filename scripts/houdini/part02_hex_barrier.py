"""
================================================================================
 ISTRORIGAN - PART 02: HEXAGONAL BARRIER FORCEFIELD DOME
================================================================================
 Scale: R=1,500m Outer Radius, H=+650m Apex
 Architectural Features:
   - Geodesic Hexagonal Honeycomb Forcefield Grid
   - Translucent Cyan Energy Modulation (PBR Alpha 0.35 - 1.0)
   - Atmospheric Deflection & Solar Radiation Filtration
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

VEX_HEX_BARRIER = load_vex("part02_hex_barrier.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_barrier", "Hex Barrier", [
        SIMPLE("f_barrier_cfg", "Forcefield Dome (R=1,500m)", [
            B("showBarrier", "Show Hex Barrier Dome", 1),
            F("barrierRadius", "Dome Radius (m)", 1500.0, 500.0, 3000.0),
            F("barrierHeight", "Dome Height (m)", 650.0, 200.0, 1500.0),
            F("barrierEnergy", "Barrier Energy Level (0.3 - 1.0)", 0.35, 0.0, 1.0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    barrier_w = wr(
        parent, "sys02_hex_barrier", 0, VEX_HEX_BARRIER,
        col, row, root_input,
        comment="Hexagonal Forcefield Dome", cref=cref
    )
    barrier_off = mk(parent, "null", "barrier_off", col + 1, row + 1, "empty (OFF)")
    barrier_sw = mk(parent, "switch", "barrier_switch", col, row + 2, "showBarrier")
    barrier_sw.setInput(0, barrier_off)
    barrier_sw.setInput(1, barrier_w)
    sete(barrier_sw, "input", f'ch("{cref}showBarrier")')
    
    all_nodes = [barrier_w, barrier_off, barrier_sw]
    return barrier_sw, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part02_hex_barrier")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(get_parm_templates())
    ptg.append(TAB("tab_color", "Color", [
        COL("colBarrier", "Hex Barrier (Luminous Cyan)", (0.10, 0.85, 1.0))
    ]))
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_barrier", "PART 02: HEX BARRIER", (0.12, 0.38, 0.45), nodes)

    note_txt = (
        "====================================================\n"
        "PART 02: HEXAGONAL BARRIER FORCEFIELD DOME\n"
        "====================================================\n"
        "* Planetary Defense & Climate Stabilization Shield\n"
        "* Geodesic Hexagonal Honeycomb Matrix\n"
        "* Dimensions: Radius 1,500m, Height +650m Apex\n"
        "* Translucent Cyan Energy Modulation (PBR 0.35 - 1.0)\n"
        "* Solar Radiation Filtration & Atmospheric Deflection\n"
        "===================================================="
    )
    stickynote(geo, "note_part02_specs", note_txt, col=2.8, row=0.5,
               width=5.0, height=3.2, color=(0.10, 0.18, 0.24), text_color=(0.85, 0.96, 1.0))
    print("[+] Part 02 Hex Barrier standalone build complete -> /obj/part02_hex_barrier")


if __name__ == "__main__":
    standalone_build()
# endregion
