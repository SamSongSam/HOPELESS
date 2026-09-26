"""
================================================================================
 ISTRORIGAN - PART 01: APEX SPIRE & CITADEL (AAA SCULPTURAL TWIN-PYLON)
================================================================================
 Exact Match to LOTUS_ACADEMY_CITY.jpg:
   - Splaying Organic Root Buttresses at Base merging into Circular Podium
   - Streamlined Elliptical Shaft with Vertical Louver Fins
   - Soaring Twin-Pylon (Dual-Blade) Split Apex (+600m) with Central Void
   - Suspended Crown Observatory Chamber within the Aperture (+520m)
   - Vertical Glowing Cyan Illumination Light Slots
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

VEX_SCULPTURAL_SPIRE = load_vex("part01_apex_spire.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_citadel", "Citadel Core", [
        SIMPLE("f_core_spire", "Sculptural Twin-Blade Spire (Canon Ref)", [
            F("spireHeight", "Apex Spire Elevation (m)", 600.0, 200.0, 1200.0),
            F("citadelPlazaRadius", "Plaza Base Radius (m)", 150.0, 50.0, 350.0),
            F("citadelPlazaHeight", "Plaza Elevation Z (m)", 120.0, 20.0, 250.0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    citadel_w = wr(
        parent, "sys01_apex_spire", 0, VEX_SCULPTURAL_SPIRE,
        col, row, root_input,
        comment="Sculptural Twin-Blade Spire & Splayed Root Podium (Canon Ref)", cref=cref
    )
    all_nodes = [citadel_w]
    return citadel_w, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part01_apex_spire")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(get_parm_templates())
    ptg.append(TAB("tab_color", "Color", [
        COL("colCitadel", "Citadel Spire (Ivory Gold)", (0.95, 0.92, 0.82))
    ]))
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_spire", "PART 01: SCULPTURAL TWIN-BLADE SPIRE", (0.35, 0.30, 0.22), nodes)

    note_txt = (
        "====================================================\n"
        "PART 01: APEX SPIRE & CITADEL (+600m)\n"
        "====================================================\n"
        "* Sovereign Seat of the 17 Great States\n"
        "* Sculptural Twin-Blade Split Apex (+600m)\n"
        "* Central Void Aperture & Crown Observatory (+520m)\n"
        "* Splaying Organic Root Buttresses at Base\n"
        "* Streamlined Elliptical Shaft with Aerodynamic Louvers\n"
        "* Vertical Bioluminescent Cyan Illumination Slots\n"
        "===================================================="
    )
    stickynote(geo, "note_part01_specs", note_txt, col=2.5, row=0.0,
               width=5.0, height=3.2, color=(0.14, 0.16, 0.22), text_color=(0.95, 0.96, 1.0))
    print("[+] Part 01 Sculptural Twin-Blade Spire build complete -> /obj/part01_apex_spire")


if __name__ == "__main__":
    standalone_build()
# endregion

