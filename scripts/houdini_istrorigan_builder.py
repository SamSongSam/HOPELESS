"""
================================================================================
 ISTRORIGAN MEGASTRUCTURE (YEAR 4205) - HOUDINI SOP ASSET BUILDER
================================================================================
 Run in Houdini: Windows > Python Source Editor -> Paste -> Run
 Or via CLI:     hython scripts/houdini_istrorigan_builder.py

 Builds /obj/istrorigan_city/istrorigan as an HDA-ready subnet:
   - 8 Discrete, Articulated Petals (No overlapping, 45m Waterway Clearance)
   - Level Outer Petal Tips (Z = 0m) for Ocean Research Berths & Ferries
   - Central Citadel Receptacle & Council of Ten Apex Spire (600m)
   - 70 Golden Stamen Forcefield Pylons (Conical Defense Perimeter)
   - 12 Telescopic Expanding Underwater Ballast Rings (Down to -1,000m)
================================================================================
"""

import sys
import math

try:
    import hou  # type: ignore
    HOUDINI_AVAILABLE = True
except ImportError:
    HOUDINI_AVAILABLE = False


def build_istrorigan_houdini_network():
    if not HOUDINI_AVAILABLE:
        print("[!] Houdini 'hou' module is not available in standalone Python environment.")
        print("[!] Run this script inside Houdini (Python Source Editor) or via 'hython'.")
        return False

    obj = hou.node("/obj")
    old_geo = obj.node("istrorigan_city")
    if old_geo:
        old_geo.destroy()

    geo = obj.createNode("geo", "istrorigan_city")
    sub = geo.createNode("subnet", "istrorigan")
    sub.setComment("ISTRORIGAN MEGASTRUCTURE (Year 4205)\n"
                   "Sovereign Sanctuary of the 17 Great States.\n"
                   "8 Discrete Petals | 45m Waterways | Expanding Abyssal Rings.")
    sub.setGenericFlag(hou.nodeFlag.DisplayComment, True)
    sub.setColor(hou.Color((0.15, 0.65, 0.95)))

    col_w, row_h = 2.5, 1.8

    def mk(node_type, name, col, row, comment=""):
        try:
            n = sub.createNode(node_type, name)
        except hou.OperationFailed:
            n = sub.createNode(node_type.split("::")[0], name)
        n.setPosition(hou.Vector2(col * col_w, -row * row_h))
        if comment:
            n.setComment(comment)
            n.setGenericFlag(hou.nodeFlag.DisplayComment, True)
        return n

    # region PROMOTED PARAMETERS
    ptg = hou.ParmTemplateGroup()

    def F(n, l, d, lo, hi):
        return hou.FloatParmTemplate(n, l, 1, default_value=(d,), min=lo, max=hi)

    def I(n, l, d, lo, hi):
        return hou.IntParmTemplate(n, l, 1, default_value=(d,), min=lo, max=hi)

    def B(n, l, d):
        return hou.ToggleParmTemplate(n, l, default_value=bool(d))

    def TAB(name, label, items):
        f = hou.FolderParmTemplate(name, label, folder_type=hou.folderType.Tabs)
        for it in items:
            f.addParmTemplate(it)
        return f

    def SIMPLE(name, label, items):
        f = hou.FolderParmTemplate(name, label, folder_type=hou.folderType.Simple)
        for it in items:
            f.addParmTemplate(it)
        return f

    ptg.append(TAB("tab_city", "Megastructure", [
        SIMPLE("f_scale", "Dimensions", [
            F("cityScale", "City Scale", 1.0, 0.1, 5.0),
            F("baseRadius", "Base Inner Radius (m)", 350.0, 100.0, 1000.0),
            F("petalLength", "Petal Length (m)", 1200.0, 400.0, 3000.0),
            F("petalWidthMax", "Petal Max Width (m)", 680.0, 200.0, 1500.0),
            F("waterwayClearance", "Min Waterway Clearance (m)", 45.0, 20.0, 150.0),
        ]),
        SIMPLE("f_articulation", "Hydraulic Articulation", [
            F("operatingPitch", "Operating Pitch (deg)", 2.5, 0.0, 25.0),
            F("diveShieldPitch", "Dive Shield Pitch (deg)", 18.0, 5.0, 45.0),
            B("submersionActive", "Submersion Mode Active", 0),
        ])
    ]))

    ptg.append(TAB("tab_submerged", "Submerged Rings", [
        SIMPLE("f_subrings", "Ballast Rings", [
            I("ringTierCount", "Ring Tiers", 12, 3, 24),
            F("neckRadius", "Surface Neck Radius (m)", 300.0, 100.0, 800.0),
            F("abyssalRadius", "Seabed Abyssal Radius (m)", 950.0, 400.0, 2500.0),
            F("submergedDepth", "Total Depth (m)", -1000.0, -2500.0, -200.0),
            F("expansionExponent", "Expansion Flare Exponent", 1.65, 1.0, 3.0),
        ])
    ]))

    ptg.append(TAB("tab_citadel", "Citadel & Barrier", [
        SIMPLE("f_citadel", "Council & Pylons", [
            F("receptacleRadius", "Receptacle Radius (m)", 320.0, 100.0, 800.0),
            I("stamenCount", "Golden Stamen Pylons", 70, 10, 120),
            F("stamenHeight", "Stamen Height (m)", 85.0, 20.0, 200.0),
            F("stamenInwardLean", "Stamen Inward Lean (deg)", 14.0, 0.0, 35.0),
            F("apexSpireHeight", "Council of Ten Spire (m)", 600.0, 150.0, 1500.0),
        ])
    ]))

    sub.setParmTemplateGroup(ptg)
    # endregion

    # region VEX WRANGLE FOR PETAL LATTICE
    VEX_PETALS = r'''
    int petalCount = 8;
    float baseR = chf("../baseRadius");
    float pLen  = chf("../petalLength");
    float pWMax = chf("../petalWidthMax");
    float clearMin = chf("../waterwayClearance");
    float pitchDeg = ch("../submersionActive") ? chf("../diveShieldPitch") : chf("../operatingPitch");
    float pitchRad = radians(pitchDeg);

    int uSteps = 30;
    int vSteps = 16;
    float halfSlotRad = M_PI / float(petalCount);

    for (int p = 0; p < petalCount; p++) {
        float centerAngDeg = float(p) * (360.0 / float(petalCount));
        float centerRad = radians(centerAngDeg);
        vector forward = set(cos(centerRad), 0.0, sin(centerRad));
        vector transverse = set(-sin(centerRad), 0.0, cos(centerRad));

        for (int ui = 0; ui <= uSteps; ui++) {
            float u = float(ui) / float(uSteps);
            float rDist = baseR + u * pLen;

            // Clearance enforcement math
            float maxHalfW = (rDist * sin(halfSlotRad)) - (clearMin * 0.5);
            maxHalfW = max(maxHalfW, 5.0);

            float vs = pow(u, 0.52);
            float prof = pow(max(sin(M_PI * vs), 0.0), 1.20);
            float halfW = min((pWMax * 0.5) * prof, maxHalfW);

            float sectorChord = 2.0 * rDist * sin(halfSlotRad);
            float actualClear = sectorChord - (halfW * 2.0);

            // Z profile: keel & cup with flat tip blend at sea level
            float arch = sin(M_PI * u);
            float foldZ = u * pLen * sin(pitchRad);
            if (u > 0.70) {
                float t = (u - 0.70) / 0.30;
                float blend = 1.0 - (t * t * (3.0 - 2.0 * t));
                foldZ *= blend;
            }

            for (int vi = 0; vi <= vSteps; vi++) {
                float v = -1.0 + 2.0 * (float(vi) / float(vSteps));
                float keelZ = 25.0 * (1.0 - abs(v)) * pow(arch, 0.65);
                float cupZ  = -42.0 * (v * v) * arch;
                float deckZ = keelZ + cupZ;

                if (u > 0.70) {
                    float t = (u - 0.70) / 0.30;
                    deckZ *= (1.0 - (t * t * (3.0 - 2.0 * t)));
                }

                float latOffset = v * halfW;
                float foldDist = u * pLen * cos(pitchRad);
                vector spinePos = forward * (baseR + foldDist);
                vector pos = spinePos + (transverse * latOffset) + set(0.0, deckZ + foldZ, 0.0);

                int pt = addpoint(0, pos);
                setpointattrib(0, "petal_index", pt, p, "set");
                setpointattrib(0, "u", pt, u, "set");
                setpointattrib(0, "v", pt, v, "set");
                setpointattrib(0, "clearance_m", pt, actualClear, "set");

                string ztag = "Petal_MidLiving";
                if (abs(v) > 0.92) ztag = "Clearance_Waterway";
                else if (u < 0.25) ztag = "Petal_InnerTransit";
                else if (u > 0.75) ztag = "Petal_OuterTip";
                setpointattrib(0, "zone", pt, ztag, "set");
            }
        }
    }
    '''
    # endregion

    # region VEX WRANGLE FOR EXPANDING UNDERWATER RINGS
    VEX_RINGS = r'''
    int tiers = chi("../ringTierCount");
    float neckR = chf("../neckRadius");
    float abyssR = chf("../abyssalRadius");
    float maxDepth = chf("../submergedDepth");
    float expP = chf("../expansionExponent");
    int angRes = 48;

    for (int t = 0; t < tiers; t++) {
        float normT = float(t) / float(max(tiers - 1, 1));
        float depthZ = normT * maxDepth;
        float flare = pow(normT, expP);
        float radius = neckR + (abyssR - neckR) * flare;
        float pressure = 1.0 + (abs(depthZ) * 0.10055);

        for (int a = 0; a < angRes; a++) {
            float rad = radians(float(a) * (360.0 / float(angRes)));
            vector pos = set(radius * cos(rad), depthZ, radius * sin(rad));

            int pt = addpoint(0, pos);
            setpointattrib(0, "tier", pt, t, "set");
            setpointattrib(0, "radius_m", pt, radius, "set");
            setpointattrib(0, "pressure_bar", pt, pressure, "set");
            setpointattrib(0, "zone", pt, (normT > 0.85 ? "Root_AbyssalAnchor" : "Stem_ExpandingRings"), "set");
        }
    }
    '''
    # endregion

    # region VEX WRANGLE FOR STAMENS & APEX SPIRE
    VEX_CITADEL = r'''
    int stamens = chi("../stamenCount");
    float recR = chf("../receptacleRadius");
    float stamH = chf("../stamenHeight");
    float lean = radians(chf("../stamenInwardLean"));
    float spireH = chf("../apexSpireHeight");

    // 70 Golden Stamen Pylons
    for (int s = 0; s < stamens; s++) {
        float ang = radians(float(s) * (360.0 / float(stamens)));
        vector base = set(recR * cos(ang), 12.0, recR * sin(ang));
        int pt = addpoint(0, base);
        setpointattrib(0, "type", pt, "StamenBase", "set");

        vector tip = base + set(-sin(lean) * cos(ang) * stamH, stamH * cos(lean), -sin(lean) * sin(ang) * stamH);
        int ptTip = addpoint(0, tip);
        setpointattrib(0, "type", ptTip, "StamenTip", "set");
        addprim(0, "polyline", pt, ptTip);
    }

    // Council Apex Spire Point
    int apexPt = addpoint(0, set(0.0, spireH, 0.0));
    setpointattrib(0, "type", apexPt, "ApexCouncilChamber", "set");
    setpointattrib(0, "zone", apexPt, "Core_Civic", "set");
    '''
    # endregion

    # Create Wrangle Nodes
    wr_petals = mk("attribwrangle", "gen_8_petals", 0, 0, "8 Articulated Discrete Petals")
    wr_petals.parm("class").set(0) # Detail / once
    wr_petals.parm("snippet").set(VEX_PETALS)

    wr_rings = mk("attribwrangle", "gen_submerged_rings", 1, 0, "12 Telescopic Expanding Ballast Rings")
    wr_rings.parm("class").set(0)
    wr_rings.parm("snippet").set(VEX_RINGS)

    wr_citadel = mk("attribwrangle", "gen_citadel_stamens", 2, 0, "Citadel, 70 Stamens & 600m Spire")
    wr_citadel.parm("class").set(0)
    wr_citadel.parm("snippet").set(VEX_CITADEL)

    merge = mk("merge", "merge_all_components", 1, 2, "merge components")
    merge.setInput(0, wr_petals)
    merge.setInput(1, wr_rings)
    merge.setInput(2, wr_citadel)

    output = mk("output", "OUT_Istrorigan_Mesh", 1, 3, "final mesh output")
    output.setInput(0, merge)
    output.setDisplayFlag(True)
    output.setRenderFlag(True)

    # region NETWORK BOXES & STICKY NOTES
    try:
        box_gen = sub.createNetworkBox("box_generators")
        box_gen.setComment("01. VEX PROCEDURAL GENERATORS")
        box_gen.setColor(hou.Color((0.2, 0.35, 0.45)))
        for n in [wr_petals, wr_rings, wr_citadel]:
            box_gen.addNode(n)
        box_gen.fitAroundContents()

        box_out = sub.createNetworkBox("box_output")
        box_out.setComment("02. MERGE & OUTPUT")
        box_out.setColor(hou.Color((0.35, 0.28, 0.15)))
        for n in [merge, output]:
            box_out.addNode(n)
        box_out.fitAroundContents()

        note = sub.createStickyNote("note_istrorigan_specs")
        note.setPosition(hou.Vector2(-5.5, 0.0))
        note.setSize(hou.Vector2(4.5, 4.0))
        note.setText("========================================\n"
                      "ISTRORIGAN SOP ASSET (YEAR 4205)\n"
                      "========================================\n"
                      "* 8 Articulated Discrete Petals (45m Waterways)\n"
                      "* 12 Expanding Submerged Ballast Rings (-1000m)\n"
                      "* Citadel of Ten & 600m Apex Spire\n"
                      "* 70 Golden Stamen Energy Pylons\n"
                      "========================================")
        note.setColor(hou.Color((0.10, 0.14, 0.22)))
    except Exception:
        pass
    # endregion

    print("[+] Houdini Megastructure Network /obj/istrorigan_city/istrorigan created successfully!")
    return True


if __name__ == "__main__":
    build_istrorigan_houdini_network()
