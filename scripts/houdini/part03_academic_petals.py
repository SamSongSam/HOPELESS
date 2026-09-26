"""
================================================================================
 ISTRORIGAN - PART 03: SCULPTURAL ACADEMIC PETALS (AAA CINEMATIC QUALITY)
================================================================================
 Exact Match to LOTUS_ACADEMY_CITY.jpg:
   - Sculptural Superyacht Hull Architecture with continuous compound curvature
   - Flared Aerodynamic Outer Coaming Rim (Rising to +48m above water)
   - Recessed Interior Accent Light Channel (Emissive Magenta / Pink #fa7298)
   - Multi-Tiered Sunken Campus Basin with Terraced Plazas
   - Hydrodynamic V-Keel Underside with Smooth Chines
   - Strictly Guaranteed 45m Navigable Seaway Clearance
   - Clean Quad Topology designed for OpenSubdiv smoothing
================================================================================
"""

# region MODULE IMPORTS & VEX BINDING
import sys
import os

try:
    from .helpers import (
        mk, setp, sete, wr, netbox, stickynote, load_vex,
        F, I, B, COL, SEP, SIMPLE, TAB, MULTI, create_standalone_geo, get_hou
    )
except ImportError:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from helpers import (
        mk, setp, sete, wr, netbox, stickynote, load_vex,
        F, I, B, COL, SEP, SIMPLE, TAB, MULTI, create_standalone_geo, get_hou
    )

VEX_SCULPTURAL_PETALS = load_vex("part03_academic_petals.vfl")

D_SEC_R = "{ autoPetalSection == 0 }"
D_SEC_M = "{ autoPetalSection == 1 }"
D_GUARD = "{ collisionGuard == 0 }"
# endregion


# region PARAMETER TEMPLATES
def get_parm_templates():
    return TAB("tab_petals", "Academic Petals", [
        SIMPLE("f_petal_plan", "Plan Outline", [
            I("petalCount", "Petal Count", 8, 4, 16, strict=True),
            F("petalRootRadius", "Root Radius from Centre (m)   (hinge line)", 150.0, 50.0, 600.0),
            F("petalLength", "Length (m)", 950.0, 300.0, 2500.0),
            F("petalWidthMax", "Max Beam Width (m)   (clamped by the 45m canal)", 420.0, 100.0, 1000.0),
            F("petalPeakPos", "Widest-Point Position   (0 stern .. 1 bow)", 0.55, 0.1, 0.9, strict=True),
            F("petalWidthProfile", "Width Profile   (>1 = slimmer / pointier)", 0.85, 0.3, 3.0, strict=True),
            F("petalBaseNarrow", "Stern Bluntness   (0 = pointed stern)", 0.15, 0.0, 1.0, strict=True),
            F("petalTipSharpness", "Bow Sharpness   (1 = pointed bow)", 0.85, 0.0, 1.0, strict=True),
            F("minWaterwayClearance", "Min Waterway Clearance (m)", 45.0, 10.0, 120.0),
        ]),
        SEP("s_pt1"),
        SIMPLE("f_petal_size", "Hull Size", [
            F("deckHeight", "Campus Deck Height above Sea (m)", 8.0, 0.0, 40.0),
            B("autoPetalSection", "Auto Size   (rim / keel scale with length and beam)", 1),
            F("rimHeightRatio", "Rim Height Ratio   (x length)", 0.04, 0.005, 0.12, dw=D_SEC_R),
            F("rimWidthRatio", "Rim Width Ratio   (x beam)", 0.043, 0.01, 0.15, dw=D_SEC_R),
            F("keelDraftRatio", "Keel Draft Ratio   (x length)", 0.019, 0.002, 0.08, dw=D_SEC_R),
            F("rimHeightManual", "Manual Rim Height (m)", 38.0, 5.0, 90.0, dw=D_SEC_M),
            F("rimWidthManual", "Manual Rim Width (m)", 18.0, 4.0, 60.0, dw=D_SEC_M),
            F("keelDraftManual", "Manual Keel Draft (m)", 18.0, 2.0, 60.0, dw=D_SEC_M),
            F("petalRimHeight", "petalRimHeight", 38.0, 0.0, 500.0, hidden=True),
            F("petalRimWidth", "petalRimWidth", 18.0, 0.0, 500.0, hidden=True),
            F("keelDepth", "keelDepth", 18.0, 0.0, 500.0, hidden=True),
        ]),
        SEP("s_pt2"),
        SIMPLE("f_petal_section", "Hull Cross-Section   (ranges locked so the section never folds)", [
            F("hullKeelV", "Keel V   (0 flat bottom .. 1 sharp V)", 0.13, 0.0, 1.0, strict=True),
            F("hullBilgeRound", "Bilge Roundness", 0.5, 0.0, 1.0, strict=True),
            F("hullFlare", "Hull Flare   (waterline inset x beam)", 0.02, 0.0, 0.25, strict=True),
            F("hullFlareHeight", "Max-Beam Height   (x rim height)", 0.58, 0.2, 0.9, strict=True),
            F("rimRoundness", "Rim Roundness", 0.5, 0.0, 1.0, strict=True),
            F("lightRevealHeight", "Magenta Reveal Height (m)", 2.5, 0.2, 10.0, strict=True),
            F("lightRevealDepth", "Magenta Reveal Depth (m)", 0.8, 0.1, 5.0, strict=True),
            F("innerWallRun", "Inner Wall Run (m)", 8.0, 1.0, 40.0, strict=True),
            F("basinCup", "Basin Cup   (deck centre drop, m)", 0.0, 0.0, 12.0, strict=True),
        ]),
        SEP("s_pt3"),
        SIMPLE("f_petal_curve", "Spine Curvature   (Spine_Deformation_Spline)", [
            F("spineCurve", "Lengthwise Curve (deg)", 0.0, -15.0, 30.0, strict=True),
            F("tipCurl", "Bow Curl (deg)", 6.0, 0.0, 40.0, strict=True),
            F("tipCurlStart", "Curl Start   (along length)", 0.75, 0.3, 0.98, strict=True),
        ]),
        SEP("s_pt4"),
        SIMPLE("f_petal_pose", "Hinge Pose   (openAmount / submergeAmount live on Master Global)", [
            F("closedPitch", "Closed Pitch (deg)   (openAmount = 0)", 60.0, 0.0, 65.0, strict=True),
            F("submergeTuckPitch", "Submerge Tuck Pitch (deg)", 8.0, 0.0, 30.0, strict=True),
            F("pitchMax", "Angular Limit Pitch Max (deg)", 65.0, 0.0, 90.0, strict=True),
            B("collisionGuard", "Inter-Petal Collision Guard   (limits pitch to keep the canal)", 1),
            I("guardIterations", "Guard Search Steps", 10, 2, 20, dw=D_GUARD),
        ]),
        SEP("s_pt5"),
        SIMPLE("f_petal_var", "Per-Petal Variation   (breaks the perfect symmetry)", [
            I("petalSeed", "Seed", 4205, 0, 10000),
            F("lengthJitter", "Length Jitter", 0.0, 0.0, 0.3, strict=True),
            F("widthJitter", "Width Jitter", 0.0, 0.0, 0.3, strict=True),
            F("azimuthJitter", "Azimuth Jitter (deg)", 0.0, 0.0, 8.0, strict=True),
            F("pitchJitter", "Pitch Jitter (deg)", 0.0, 0.0, 15.0, strict=True),
            F("rimJitter", "Rim Height Jitter", 0.0, 0.0, 0.4, strict=True),
            MULTI("petalOverrides", "Per-Petal Overrides   (Independent_Pitch_Angle etc.)", [
                B("ovEnable#", "Enable", 1),
                I("ovPetal#", "Petal Index", 0, 0, 15),
                F("ovLength#", "Length Scale", 1.0, 0.5, 1.5),
                F("ovWidth#", "Width Scale", 1.0, 0.5, 1.5),
                F("ovPitch#", "Extra Pitch (deg)", 0.0, -30.0, 60.0),
                F("ovAzimuth#", "Azimuth Offset (deg)", 0.0, -10.0, 10.0),
                F("ovRim#", "Rim Height Scale", 1.0, 0.3, 2.0),
            ]),
        ]),
        SEP("s_pt6"),
        SIMPLE("f_petal_col", "Petal Colors", [
            COL("colPetalLight", "Rim Reveal (Magenta)", (0.98, 0.42, 0.72)),
            COL("colPetalDeck", "Campus Deck", (0.88, 0.90, 0.92)),
            COL("colPetalUnder", "Underside", (0.80, 0.83, 0.88)),
        ]),
        SEP("s_pt7"),
        SIMPLE("f_petal_res", "Resolution", [
            I("petalURes", "Lengthwise Rings", 160, 16, 600),
            F("petalFuseDist", "Weld Distance (m)", 0.05, 0.0, 2.0),
        ]),
    ])


def setup_expressions(node):
    """Resolve the Auto/Manual hidden parms on the node that owns the petal tab."""
    node.parm("petalRimHeight").setExpression(
        'if(ch("autoPetalSection"), ch("petalLength")*ch("rimHeightRatio"), ch("rimHeightManual"))')
    node.parm("petalRimWidth").setExpression(
        'if(ch("autoPetalSection"), ch("petalWidthMax")*ch("rimWidthRatio"), ch("rimWidthManual"))')
    node.parm("keelDepth").setExpression(
        'if(ch("autoPetalSection"), ch("petalLength")*ch("keelDraftRatio"), ch("keelDraftManual"))')
# endregion


# region NODE NETWORK BUILDER
def build_nodes(parent, root_input=None, col=0, row=0, cref="../"):
    petals_w = wr(
        parent, "sys03_academic_petals", 0, VEX_SCULPTURAL_PETALS,
        col, row, root_input,
        comment="Lotus-grade petal hulls + hinge pose + 45m collision guard", cref=cref
    )
    fuse = mk(parent, "fuse", "sys03_petal_weld", col, row + 0.6, "weld coincident points")
    fuse.setInput(0, petals_w)
    sete(fuse, "dist", 'ch("%spetalFuseDist")' % cref)
    clean = mk(parent, "clean", "sys03_petal_clean", col, row + 1.2, "drop degenerate prims")
    clean.setInput(0, fuse)
    nrm = mk(parent, "normal", "sys03_petal_normals", col, row + 1.8, "hard edges at rim/light reveal")
    nrm.setInput(0, clean)
    setp(nrm, "cuspangle", 35.0)
    all_nodes = [petals_w, fuse, clean, nrm]
    return nrm, all_nodes
# endregion


# region STANDALONE BUILD & TEST
def standalone_build():
    hou = get_hou()
    geo = create_standalone_geo("part03_academic_petals")
    
    ptg = geo.parmTemplateGroup()
    ptg.append(get_parm_templates())
    ptg.append(TAB("tab_state", "State", [
        F("openAmount", "Open Amount   (0 closed .. 1 flat on the sea)", 1.0, 0.0, 1.0),
        F("submergeAmount", "Submerge Amount", 0.0, 0.0, 1.0),
    ]))
    ptg.append(TAB("tab_color", "Color", [
        COL("colPetalHull", "Petal Hull (Pure White)", (0.94, 0.95, 0.98))
    ]))
    geo.setParmTemplateGroup(ptg)
    setup_expressions(geo)
    
    root = mk(geo, "null", "root", 0, 0, "root trigger")
    out, nodes = build_nodes(geo, root, 0, 1, cref="../")
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    netbox(geo, "box_petals", "PART 03: SCULPTURAL PETALS (AAA CANON)", (0.24, 0.32, 0.42), nodes)

    note_txt = (
        "====================================================\n"
        "PART 03: SCULPTURAL ACADEMIC PETALS (CANON REF)\n"
        "====================================================\n"
        "* 8 Articulated Superyacht Cantilever Hulls\n"
        "* Proportions: Length 950m, Max Beam 420m, Keel 18m\n"
        "* Guaranteed >= 45.0m Navigable Waterway Clearances\n"
        "* Flared Aerodynamic Coaming Rim (+45m elevation)\n"
        "* Recessed Interior Emissive Magenta Light Accent Lip\n"
        "* Sunken Multi-Tiered Campus Basin Forums\n"
        "* Hydrodynamic V-Keel Underside with Smooth Chines\n"
        "* Clean Quad Topography for OpenSubdiv\n"
        "===================================================="
    )
    stickynote(geo, "note_part03_specs", note_txt, col=2.6, row=0.0,
               width=5.4, height=3.8, color=(0.12, 0.16, 0.24), text_color=(0.95, 0.96, 1.0))
    print("[+] Part 03 Sculptural Academic Petals build complete -> /obj/part03_academic_petals")


if __name__ == "__main__":
    standalone_build()
# endregion
