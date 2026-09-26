"""
================================================================================
 ISTRORIGAN PCG PIPELINE - STAGES 0-3 (04_PCG_PIPELINE/01_PCG_GENERATION_PIPELINE)
================================================================================
   Stage 0  Blueprint loader   - zoning table read live from the project .md
   Stage 1  Polar lattice      - points on the live petal decks + core plaza
   Stage 2  Zoning & filtering - zone lookup, districts, density, restrictions
   Stage 3  Graph & splines    - L1 maglev / L2 utility / L3 pedestrian-evac graph,
                                 ring bridges, flood isolation, Dijkstra evac routing
 Replaces the old CSV-driven 'py_lattice' / 'py_transit' layers (static data
 baked by external scripts) with nodes that re-cook from the HDA parameters.
================================================================================
"""

import sys
import os

try:
    from .helpers import mk, setp, sete, wr, load_vex, F, I, B, STR, SEP, SIMPLE, TAB, get_hou
    from .pcg_blueprint_loader import LOADER_CODE
except ImportError:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from helpers import mk, setp, sete, wr, load_vex, F, I, B, STR, SEP, SIMPLE, TAB, get_hou
    from pcg_blueprint_loader import LOADER_CODE

RELOAD_CB = ("n = kwargs['node'].node('pcg_s0_blueprint')\n"
             "n.cook(force=True) if n else None")


def get_parm_templates():
    hou = get_hou()
    reload_btn = hou.ButtonParmTemplate(
        "blueprintReload", "Reload Blueprint (.md)",
        script_callback=RELOAD_CB,
        script_callback_language=hou.scriptLanguage.Python)
    return TAB("tab_pcg", "PCG Pipeline", [
        SIMPLE("f_pcg_bp", "Stage 0 - Blueprint (source of truth)", [
            STR("blueprintRoot", "Project Root   (folder holding 00_CORE/DATA_TABLES)", "$HIP/.."),
            reload_btn,
            I("pcgSeed", "Global Master Seed   (00_CORE_SETTINGS)", 133742, 0, 999999),
        ]),
        SEP("s_pcg1"),
        SIMPLE("f_pcg_s1", "Stage 1 - Polar Lattice", [
            F("latticeSpacing", "Lattice Spacing (m)   (smaller = denser)", 4.0, 0.5, 50.0),
            F("coreDeckRadius", "Core Plaza Radius (m)", 140.0, 10.0, 600.0),
            F("coreDeckHeight", "Core Plaza Elevation (m)", 8.0, -50.0, 400.0),
            F("tierBaseStart", "Tier 1 Petal Base from (m)   (01_WORLD)", 150.0, 0.0, 2000.0),
            F("tierMidStart", "Tier 2 Petal Mid from (m)", 350.0, 0.0, 2000.0),
            F("tierTipStart", "Tier 3 Petal Tip from (m)", 750.0, 0.0, 3000.0),
        ]),
        SEP("s_pcg2"),
        SIMPLE("f_pcg_s2", "Stage 2 - Zoning, Restrictions & Density", [
            F("buildDensityScale", "Build Candidate Density", 0.35, 0.0, 1.0),
            F("centerConeClearance", "Center_Cone_Clearance (m)", 40.0, 0.0, 300.0),
            F("protectionPylonClearance", "Protection_Pylon_Clearance (m)", 8.0, 0.0, 60.0),
            F("petalInnerClearance", "Petal_Inner_Clearance - hinge (m)", 25.0, 0.0, 200.0),
            F("petalEdgeClearance", "Petal Left/Right Clearance - promenade (m)", 10.0, 0.0, 80.0),
            F("transportClearance", "Transport_Clearance - spine half width (m)", 6.0, 0.0, 40.0),
            F("emergencyAccessSpacing", "Emergency_Access spacing (m)   (0 = off)", 120.0, 0.0, 600.0),
            F("emergencyAccessWidth", "Emergency_Access width (m)", 8.0, 0.0, 40.0),
            F("barrierHeadroom", "Barrier headroom under dome (m)", 30.0, 0.0, 300.0),
            F("minBuildingHeight", "Min buildable height (m)", 6.0, 0.0, 60.0),
            B("buildableClosedState", "Buildable_Closed_State", 1),
            SEP("s_pcg3"),
            B("latticeCandidatesOnly", "Viewport: show build candidates only", 0),
        ]),
        SEP("s_pcg4"),
        SIMPLE("f_pcg_s3", "Stage 3 - Transit & Resource Graph   (04_PCG_PIPELINE/03)", [
            F("graphStep", "Spline Sample Step (m)", 10.0, 1.0, 100.0),
            F("coreRingRadius", "FC_Center_Ring_Corridor radius (m)", 90.0, 10.0, 600.0),
            F("maglevLift", "Maglev rail height above deck (m)", 4.0, 0.0, 40.0),
            F("utilityOffset", "Utility trunk offset from spine (m)", 4.0, 0.0, 40.0),
            F("utilityDepth", "Utility trunk depth below deck (m)", 3.0, 0.0, 40.0),
            F("evacTubeDepth", "Evac pressurised tube depth (m)", 6.0, 0.0, 60.0),
            F("stationSpacing", "Petal station spacing (m)   (0 = none)", 250.0, 0.0, 2000.0),
            F("bunkerDepth", "Core Citadel Bunker depth (m)", 60.0, 0.0, 500.0),
            F("o2PlantDepth", "Core O2 & Desalination plant depth (m)", 10.0, 0.0, 300.0),
            F("stemReactorDepth", "Geothermal stem reactor depth (m)", 40.0, 0.0, 1000.0),
            SEP("s_pcg5"),
            STR("bridgeRadii", "Ring bridge radii (m)   (blueprint: Tier 2 = 500, Tier 3 = 900)", "500 900"),
            F("bridgeArch", "Bridge arch height (m)", 15.0, 0.0, 120.0),
            F("bridgeWaterClearance", "Bridge min height over sea (m)", 20.0, 0.0, 120.0),
            F("bridgeMaxSpan", "FC_Center_Bridge_State: max span (m)", 500.0, 10.0, 1500.0),
            F("bridgeMaxFoldDelta", "FC_Center_Bridge_State: max pitch difference (deg)", 3.0, 0.0, 60.0),
            F("bridgeMaxFold", "FC_Center_Bridge_State: max petal pitch (deg)", 12.0, 0.0, 65.0),
            SEP("s_pcg6"),
            STR("floodedPetals", "Disaster Isolation: flooded petals   (e.g. '3 5')", ""),
            B("evacUseBridges", "Evacuation may use ring bridges", 1),
            B("graphAsTubes", "Viewport: show graph as tubes", 0),
            F("graphTubeRadius", "Tube radius (m)", 1.5, 0.1, 10.0, dw="{ graphAsTubes == 0 }"),
        ]),
    ])


def build_nodes(parent, root_input, petals_out, col=36, row=1, cref="../"):
    """Returns dict: lattice_view, s2_out, graph_view, s3_out, nodes."""
    s0 = mk(parent, "python", "pcg_s0_blueprint", col, row, "Stage 0: blueprint tables from .md")
    setp(s0, "python", LOADER_CODE)

    s1 = wr(parent, "pcg_s1_polar_lattice", 0, load_vex("pcg_s1_polar_lattice.vfl"),
            col + 1, row, root_input, petals_out,
            comment="Stage 1: polar lattice on live petal decks", cref=cref)
    s2 = wr(parent, "pcg_s2_zoning", 2, load_vex("pcg_s2_zoning.vfl"),
            col + 1, row + 1, s1, s0,
            comment="Stage 2: zoning, restrictions, density", cref=cref)

    view = mk(parent, "blast", "pcg_s2_candidates_only", col + 2, row + 2, "keep build_candidate")
    view.setInput(0, s2)
    setp(view, "group", "build_candidate")
    setp(view, "grouptype", 3)          # points
    setp(view, "negate", 1)             # delete everything NOT in the group
    sw = mk(parent, "switch", "pcg_s2_view_switch", col + 1, row + 3, "latticeCandidatesOnly")
    sw.setInput(0, s2)
    sw.setInput(1, view)
    sete(sw, "input", 'ch("%slatticeCandidatesOnly")' % cref)

    out = mk(parent, "null", "PCG_S2_OUT", col + 1, row + 4, "zoned lattice -> Stage 3")
    out.setInput(0, s2)

    s3, s3b, g_view, g_out, g_nodes = build_stage3(parent, root_input, petals_out, col + 4, row, cref)
    return dict(lattice_view=sw, s2_out=out, graph_view=g_view, s3_out=g_out,
                nodes=[s0, s1, s2, view, sw, out] + g_nodes)


def build_stage3(parent, root_input, petals_out, col, row, cref="../"):
    s3 = wr(parent, "pcg_s3_graph", 0, load_vex("pcg_s3_graph.vfl"),
            col, row, root_input, petals_out,
            comment="Stage 3: L1/L2/L3 graph + ring bridges", cref=cref)
    s3b = wr(parent, "pcg_s3_evac", 0, load_vex("pcg_s3_evac.vfl"),
             col, row + 1, s3,
             comment="Stage 3b: flood isolation + Dijkstra evac", cref=cref)
    tubes = mk(parent, "polywire", "pcg_s3_tubes", col + 1, row + 2, "graph as tubes")
    tubes.setInput(0, s3b)
    sete(tubes, "radius", 'ch("%sgraphTubeRadius")' % cref)
    setp(tubes, "segs", 6)
    sw = mk(parent, "switch", "pcg_s3_view_switch", col, row + 3, "graphAsTubes")
    sw.setInput(0, s3b)
    sw.setInput(1, tubes)
    sete(sw, "input", 'ch("%sgraphAsTubes")' % cref)
    out = mk(parent, "null", "PCG_S3_OUT", col, row + 4, "transit & resource graph -> Stage 4")
    out.setInput(0, s3b)
    return s3, s3b, sw, out, [s3, s3b, tubes, sw, out]
