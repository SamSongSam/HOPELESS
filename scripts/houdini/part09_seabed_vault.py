"""
================================================================================
 ISTRORIGAN - PART 09: ABYSSAL DOOMSDAY VAULT & SEABED ANCHORS
================================================================================
 Scale: Abyssal Vault Bunker R=120m, 8 Hydraulic Bedrock Anchor Claws at -1,000m
 Architectural Features:
   - Heavily Armored Hexagonal Subterranean Knowledge Vault
   - Seafloor Geothermal Tap Conduits & Seismic Dampeners
   - Bedrock Claws Stabilizing Megastructure against Tsunami and Subsea Faults
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

VEX_SEABED_VAULT = load_vex("part09_seabed_vault.vfl")
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_vault", "Seabed Vault", [
        SIMPLE("f_vault_cfg", "Abyssal Doomsday Vault (-1,000m)", [
            B("showVault", "Show Seabed Vault & Anchors", 1),
            F("vaultBunkerRadius", "Bunker Hub Radius (m)", 120.0, 40.0, 250.0),
            I("anchorClawCount", "Hydraulic Bedrock Claws", 8, 4, 16),
            F("vaultDepth", "Vault Elevation Depth (m)", -1000.0, -1600.0, -200.0),
        ]),
    ])
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    vault_w = wr(
        parent, "sys09_seabed_vault", 0, VEX_SEABED_VAULT,
        col, row, root_input,
        comment="Abyssal Vault & Bedrock Anchor Claws", cref=cref
    )
    vault_off = mk(parent, "null", "vault_off", col + 1, row + 1, "empty (OFF)")
    vault_sw = mk(parent, "switch", "vault_switch", col, row + 2, "showVault")
    vault_sw.setInput(0, vault_off)
    vault_sw.setInput(1, vault_w)
    sete(vault_sw, "input", f'ch("{cref}showVault")')
    
    all_nodes = [vault_w, vault_off, vault_sw]
    return vault_sw, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part09_seabed_vault")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(get_parm_templates())
    ptg.append(TAB("tab_color", "Color", [
        COL("colVault", "Vault Armor (Titanium Basalt)", (0.28, 0.32, 0.38))
    ]))
    geo.setParmTemplateGroup(ptg)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_vault", "PART 09: SEABED VAULT", (0.12, 0.20, 0.28), nodes)

    note_txt = (
        "====================================================\n"
        "PART 09: ABYSSAL DOOMSDAY VAULT & ANCHORS\n"
        "====================================================\n"
        "* Subterranean Armored Knowledge Bunker at -1,000m\n"
        "* Bunker Hub Radius: 120m, Armored Hexagonal Shell\n"
        "* 8 Hydraulic Bedrock Anchor Claws\n"
        "* Seafloor Geothermal Conduits & Seismic Dampeners\n"
        "* Megastructure Tsunami & Tectonic Fault Stabilization\n"
        "===================================================="
    )
    stickynote(geo, "note_part09_specs", note_txt, col=2.8, row=0.5,
               width=5.2, height=3.5, color=(0.10, 0.14, 0.18), text_color=(0.85, 0.90, 0.95))
    print("[+] Part 09 Seabed Vault standalone build complete -> /obj/part09_seabed_vault")


if __name__ == "__main__":
    standalone_build()
# endregion
