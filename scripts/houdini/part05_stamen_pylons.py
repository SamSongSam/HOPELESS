"""
================================================================================
 ISTRORIGAN - PART 05: 70 GOLDEN STAMEN ENERGY PYLONS
================================================================================
 Scale: 70 Pylons, Height 45m, Ring Radius 220m
 Architectural Features:
   - Burnished Gold Fluted Pylons Arrayed around Citadel Perimeter
   - Crown Emitter Nodes with Plasma Arc Vectors pointing to Apex Spire
   - Fast Viewport Optimization (Proxies/Lines when interactive)
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

VEX_STAMEN_PYLONS = load_vex("part05_stamen_pylons.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_stamens", "Stamen Pylons", [
        SIMPLE("f_stamen_cfg", "70 Golden Forcefield Pylons", [
            B("showStamens", "Show Stamen Pylons", 1),
            I("stamenCount", "Pylon Count", 70, 8, 140),
            F("stamenHeight", "Pylon Height (m)", 45.0, 10.0, 100.0),
            F("stamenRingRadius", "Ring Radius (m)", 220.0, 150.0, 320.0),
            F("pylonFluteRadius", "Pylon Base Radius (m)", 4.5, 1.0, 15.0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    stamens_w = wr(
        parent, "sys05_stamen_pylons", 0, VEX_STAMEN_PYLONS,
        col, row, root_input,
        comment="70 Golden Stamen Energy Pylons", cref=cref
    )
    stamens_off = mk(parent, "null", "stamens_off", col + 1, row + 1, "empty (OFF)")
    stamens_sw = mk(parent, "switch", "stamens_switch", col, row + 2, "showStamens")
    stamens_sw.setInput(0, stamens_off)
    stamens_sw.setInput(1, stamens_w)
    sete(stamens_sw, "input", f'ch("{cref}showStamens")')
    
    all_nodes = [stamens_w, stamens_off, stamens_sw]
    return stamens_sw, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part05_stamen_pylons")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(get_parm_templates())
    ptg.append(TAB("tab_color", "Color", [
        COL("colStamens", "Stamens (Burnished Gold)", (1.0, 0.78, 0.15))
    ]))
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_stamens", "PART 05: STAMEN PYLONS", (0.42, 0.35, 0.15), nodes)

    note_txt = (
        "====================================================\n"
        "PART 05: 70 GOLDEN STAMEN ENERGY PYLONS\n"
        "====================================================\n"
        "* 70 Burnished Gold Fluted Pylons (Canon Ref)\n"
        "* Circular array around Citadel perimeter (R=220m)\n"
        "* Pylon Dimensions: Height 45m, Fluted Base R=4.5m\n"
        "* Crown Emitter Nodes with Plasma Arc Vectors\n"
        "* Fast Viewport Optimization (Proxies/Lines Mode)\n"
        "===================================================="
    )
    stickynote(geo, "note_part05_specs", note_txt, col=2.8, row=0.5,
               width=5.2, height=3.4, color=(0.22, 0.18, 0.10), text_color=(1.0, 0.95, 0.82))
    print("[+] Part 05 Stamen Pylons standalone build complete -> /obj/part05_stamen_pylons")


if __name__ == "__main__":
    standalone_build()
# endregion
