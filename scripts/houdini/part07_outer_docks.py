"""
================================================================================
 ISTRORIGAN - PART 07: ARCHITECTURAL FLOATING JETTIES & MARINAS (AAA QUALITY)
================================================================================
 Exact Match to LOTUS_ACADEMY_CITY.jpg:
   - High-Tech Marine Pontoons floating strictly in the water outside petal flanks
   - Arched Truss Gangway Ramps with Safety Railings descending from petal coaming
   - Chamfered Modular Pontoon Spine with Timber-Composite Deck Planks
   - Finger Slips with Berthing Cleats & Moored Futuristic Luxury Yachts
   - ZERO encroachment on petal surface ("ไม่เบียดกลีบ")
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

VEX_SCULPTURAL_DOCKS = load_vex("part07_outer_docks.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_docks", "Outer Floating Docks", [
        SIMPLE("f_dock_cfg", "Architectural Marina & Pontoons (Canon Ref)", [
            B("showOuterDocks", "Show Outer Floating Docks", 1),
            F("rampLength", "Gangway Ramp Length (m)", 65.0, 20.0, 120.0),
            F("rampWidth", "Ramp Deck Width (m)", 8.0, 3.0, 20.0),
            F("spineLength", "Floating Spine Length (m)", 95.0, 30.0, 200.0),
            F("spineWidth", "Floating Spine Width (m)", 14.0, 6.0, 30.0),
            I("fingerSlipCount", "Finger Pontoon Slips", 3, 1, 6),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    docks_w = wr(
        parent, "sys07_outer_docks", 0, VEX_SCULPTURAL_DOCKS,
        col, row, root_input,
        comment="Architectural Floating Pontoons & Berthed Yachts (Canon Ref)", cref=cref
    )
    docks_off = mk(parent, "null", "docks_off", col + 1, row + 1, "empty (OFF)")
    docks_sw = mk(parent, "switch", "docks_switch", col, row + 2, "showOuterDocks")
    docks_sw.setInput(0, docks_off)
    docks_sw.setInput(1, docks_w)
    sete(docks_sw, "input", f'ch("{cref}showOuterDocks")')
    
    all_nodes = [docks_w, docks_off, docks_sw]
    return docks_sw, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part07_outer_docks")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(TAB("tab_core_petals", "Core Settings", [
        I("petalCount", "Petal Count", 8, 4, 16)
    ]))
    ptg.append(get_parm_templates())
    ptg.append(TAB("tab_color", "Color", [
        COL("colDocks", "Floating Docks (Marine Grey)", (0.80, 0.82, 0.86))
    ]))
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_docks", "PART 07: SCULPTURAL FLOATING MARINA", (0.28, 0.36, 0.34), nodes)

    note_txt = (
        "====================================================\n"
        "PART 07: FLOATING PONTOON JETTIES & MARINAS\n"
        "====================================================\n"
        "* High-Tech Marine Pontoons outside Petal Flanks\n"
        "* ZERO Encroachment on Petal Hull Deck (ไม่เบียดกลีบ)\n"
        "* Arched Gangway Ramps (Length 65m, Width 8m)\n"
        "* Chamfered Floating Spine (Length 95m, Width 14m)\n"
        "* Finger Slips with Moored Futuristic Luxury Yachts\n"
        "* Navigational Clearance for Seaway Traffic\n"
        "===================================================="
    )
    stickynote(geo, "note_part07_specs", note_txt, col=2.8, row=0.5,
               width=5.4, height=3.8, color=(0.14, 0.18, 0.20), text_color=(0.90, 0.95, 0.98))
    print("[+] Part 07 Architectural Floating Marina build complete -> /obj/part07_outer_docks")


if __name__ == "__main__":
    standalone_build()
# endregion
