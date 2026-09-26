"""
================================================================================
 PROCEDURAL LOTUS FLOWER  -  SOP Digital Asset builder            Houdini 19-22
================================================================================
 Run:  Windows > Python Source Editor  ->  paste  ->  Run
 Or :  hython S:\\Houdini\\lotus_flower.py       ( arg "save" also writes .hip )

 Builds  /obj/lotus_flower/lotus  as a subnet that is HDA-ready:
   * all parameters promoted onto the subnet (tabs: Flower / Petal / Whorls /
     Center / Color), sectioned + separated, with Auto/Manual gates.
   * output 0  = the flower mesh
   * output 1  = GUIDE geometry (whorl rings + petal axes), also template-
     flagged so it shows as a viewport overlay right away.
   * "Fast Viewport" toggle drops resolution / subdiv / petal shell / stamens
     to points for fast interaction.
   * "Whorl Y-Lift" stacks the whorls vertically so petals stop interpenetrating.

 The script then tries  createDigitalAsset()  -> S:/Houdini/lotus_flower.hda .
 If that fails (licensing / path) it leaves the finished subnet in place;
 just RMB it -> "Create Digital Asset".

 To register the guide on the HDA:  Type Properties > Node > Guide  ->  set to
     op:`./guide_switch`     (or use output 1)
================================================================================
"""

import hou
import sys

OBJ = hou.node("/obj")
old = OBJ.node("lotus_flower")
if old:
    old.destroy()
old_ctrl = OBJ.node("lotus_CTRL")
if old_ctrl:
    old_ctrl.destroy()

GEO = OBJ.createNode("geo", "lotus_flower")
SUB = GEO.createNode("subnet", "lotus")
SUB.setComment("LOTUS FLOWER  -  select me, all controls are here.\n"
               "RMB -> Create Digital Asset when ready.")
SUB.setGenericFlag(hou.nodeFlag.DisplayComment, True)
SUB.setColor(hou.Color((0.10, 0.55, 0.85)))

COL_W, ROW_H = 2.4, 1.7
CREF = "../"                      # from a direct child of SUB -> the asset params


def mk(node_type, name, col, row, comment=""):
    try:
        n = SUB.createNode(node_type, name)
    except hou.OperationFailed:
        n = SUB.createNode(node_type.split("::")[0], name)
    n.setPosition(hou.Vector2(col * COL_W, -row * ROW_H))
    if comment:
        n.setComment(comment)
        n.setGenericFlag(hou.nodeFlag.DisplayComment, True)
    return n


def setp(node, name, value):
    p = node.parm(name)
    if p is not None:
        try:
            p.set(value)
        except Exception:
            pass


def sete(node, name, expr):
    p = node.parm(name)
    if p is not None:
        try:
            p.setExpression(expr)
        except Exception:
            pass


def wr(name, cls, code, col, row, *inputs, comment=""):
    n = mk("attribwrangle", name, col, row, comment)
    setp(n, "class", cls)
    setp(n, "snippet", code.replace("%C%", CREF))
    for i, s in enumerate(inputs):
        if s is not None:
            n.setInput(i, s)
    return n


def netbox(name, label, color, nodes):
    b = SUB.createNetworkBox(name)
    b.setComment(label)
    b.setColor(hou.Color(color))
    for n in nodes:
        if n is not None:
            b.addNode(n)
    try:
        b.fitAroundContents()
    except Exception:
        pass
    return b


# region PARAMETER INTERFACE  (promoted onto the subnet / future HDA)
# ==============================================================================
#  PARAMETER INTERFACE  (promoted onto the subnet / future HDA)
# ==============================================================================
ptg = hou.ParmTemplateGroup()


def F(n, l, d, lo, hi, dw=None, hidden=False, strict=False):
    kw = dict(default_value=(d,), min=lo, max=hi,
              min_is_strict=strict, max_is_strict=strict)
    if dw:
        kw["disable_when"] = dw
    if hidden:
        kw["is_hidden"] = True
    return hou.FloatParmTemplate(n, l, 1, **kw)


def I(n, l, d, lo, hi, dw=None, strict=False):
    kw = dict(default_value=(d,), min=lo, max=hi,
              min_is_strict=strict, max_is_strict=strict)
    if dw:
        kw["disable_when"] = dw
    return hou.IntParmTemplate(n, l, 1, **kw)


def B(n, l, d, dw=None):
    kw = dict(default_value=bool(d))
    if dw:
        kw["disable_when"] = dw
    return hou.ToggleParmTemplate(n, l, **kw)


def COL(n, l, rgb):
    kw = dict(default_value=rgb)
    look = getattr(hou, "parmLook", None)
    if look is not None:
        kw["look"] = look.ColorSquare
    scheme = None
    for a in ("parmNamingScheme", "parmNaming"):
        s = getattr(hou, a, None)
        if s is not None:
            scheme = s.RGBA
            break
    for key in ("naming_scheme", "naming"):
        if scheme is None:
            break
        try:
            return hou.FloatParmTemplate(n, l, 3, **dict(kw, **{key: scheme}))
        except TypeError:
            pass
    t = hou.FloatParmTemplate(n, l, 3, **kw)
    try:
        t.setNamingScheme(scheme)
    except Exception:
        pass
    return t


def SEP(n):
    return hou.SeparatorParmTemplate(n)


def STR(n, l, d=""):
    return hou.StringParmTemplate(n, l, 1, default_value=(d,))


def SIMPLE(name, label, items):
    f = hou.FolderParmTemplate(name, label, folder_type=hou.folderType.Simple)
    for it in items:
        f.addParmTemplate(it)
    return f


def TAB(name, label, items):
    f = hou.FolderParmTemplate(name, label, folder_type=hou.folderType.Tabs)
    for it in items:
        f.addParmTemplate(it)
    return f


D_TH_R = "{ autoPetalThickness == 0 }"
D_TH_M = "{ autoPetalThickness == 1 }"
D_RC_R = "{ autoReceptacleSize == 0 }"
D_RC_M = "{ autoReceptacleSize == 1 }"
D_ST_R = "{ autoStamenLength == 0 }"
D_ST_M = "{ autoStamenLength == 1 }"

ptg.append(TAB("tab_flower", "Flower", [
    SIMPLE("f_overall", "Overall", [
        F("flowerScale", "Flower Scale", 1.0, 0.05, 5.0),
        F("bloom", "Bloom   (bud 0  /  open 0.7  /  reflexed 1.3)", 0.70, 0.0, 1.3),
        I("seed", "Random Seed", 1, 0, 100),
    ]),
    SEP("s_fl1"),
    SIMPLE("f_output", "Output / Viewport", [
        B("fastViewport", "Fast Viewport   (low-res, no subdiv, stamens as points)", 0),
        B("showGuide", "Show Guides   (whorl rings + petal axes)", 1),
        SEP("s_fl2"),
        B("doSubdiv", "Subdivide", 1, dw="{ fastViewport == 1 }"),
        I("subdivIter", "Subdiv Iterations", 1, 0, 4, dw="{ fastViewport == 1 }"),
    ]),
]))

ptg.append(TAB("tab_petal", "Petal", [
    SIMPLE("f_psize", "Size", [
        F("petalLength", "Length", 0.60, 0.15, 1.5, strict=True),
        F("petalWidth", "Width   (real lotus tepals: length:width ~ 1.8:1, not needle-thin)",
          0.34, 0.05, 1.2, strict=True),
    ]),
    SEP("s_pe1"),
    SIMPLE("f_pthick", "Thickness", [
        B("petalSolid", "Solid Petals", 1),
        B("autoPetalThickness", "Auto Thickness   (fraction of length)", 1),
        F("petalThicknessRatio", "Thickness Ratio", 0.015, 0.0, 0.1, dw=D_TH_R),
        F("petalThicknessManual", "Manual Thickness", 0.008, 0.0, 0.08, dw=D_TH_M),
    ]),
    SEP("s_pe2"),
    SIMPLE("f_pprofile", "Outline Profile", [
        F("widthProfile", "Width Profile   (>1 = pointier)", 1.20, 0.6, 3.0, strict=True),
        F("widthSkew", "Widest-Point Bias", 0.92, 0.5, 1.6, strict=True),
        F("baseNarrow", "Base Narrow   (claw)", 0.30, 0.05, 1.0, strict=True),
        F("tipSharpness", "Tip Sharpness", 0.28, 0.0, 1.0, strict=True),
    ]),
    SEP("s_pe3"),
    SIMPLE("f_pcurve", "Curvature   (ranges locked - past these the petal folds through itself)", [
        F("cup", "Cup   (cross-section hollow)", 0.20, 0.0, 0.8, strict=True),
        F("midrib", "Midrib Keel", 0.12, 0.0, 0.5, strict=True),
        F("petalCurve", "Lengthwise Curve   (deg)", 15.0, 0.0, 80.0, strict=True),
        F("tipCurl", "Tip Curl   (deg)", 7.0, 0.0, 55.0, strict=True),
        F("wrinkle", "Edge Wrinkle", 0.15, 0.0, 1.0, strict=True),
    ]),
    SEP("s_pe4"),
    SIMPLE("f_pmesh", "Mesh", [
        I("petalRes", "Resolution", 18, 6, 90),
    ]),
]))

ptg.append(TAB("tab_whorls", "Whorls", [
    SIMPLE("f_wcount", "Count / Spacing", [
        I("whorlCount", "Whorls   (layers)", 4, 1, 8, strict=True),
        I("basePetalCount", "Petals in Inner Whorl", 5, 3, 20, strict=True),
        I("petalIncrement", "Extra Petals per Whorl", 3, 0, 8, strict=True),
        B("autoFitWidth", "Auto-Fit Width   (emergency-only clamp, floor 85% - real lotus "
          "petals OVERLAP, this must not fight that)", 1),
        F("petalGap", "Petal Gap   (extra spacing on top of Auto-Fit)",
          0.0, 0.0, 0.8, strict=True, dw="{ autoFitWidth == 0 }"),
        F("whorlTwist",
          "Whorl Twist   (0 = whorls stacked directly on top  /  1 = shingled -"
          " each petal centred in the gap of the whorl below, like a real lotus)",
          1.0, 0.0, 2.0, strict=True),
    ]),
    SEP("s_wh1"),
    SIMPLE("f_wradius", "Radius / Stacking", [
        B("autoInnerRadius", "Auto Inner Radius   (hug the receptacle - no gap at the base)", 1),
        F("innerRadiusRatio", "Inner Radius Ratio   (x Receptacle Radius)",
          1.05, 0.8, 2.0, strict=True, dw="{ autoInnerRadius == 0 }"),
        F("innerRadius", "Manual Inner Radius", 0.16, 0.02, 0.8, strict=True,
          dw="{ autoInnerRadius == 1 }"),
        F("radiusStep", "Radius Growth per Whorl   (min > 0 so whorls always separate)",
          0.15, 0.02, 0.4, strict=True),
        F("baseGather", "Base Gather   (0 = spread  ..  1 = tight to base)", 0.0, 0.0, 1.0, strict=True),
        F("whorlLift", "Whorl Step   (x petal length - outer whorl sits AT the receptacle "
          "base, each whorl inward steps UP toward the stamens; also spirals every single "
          "petal so no two ever share the exact same height)", 0.30, 0.0, 0.6, strict=True),
    ]),
    SEP("s_wh2"),
    SIMPLE("f_wpitch", "Open Pitch   (deg from vertical - locked to a sane cone)", [
        F("budPitch", "Bud", 8.0, 0.0, 30.0, strict=True),
        F("innerPitch", "Inner Whorl   (open)", 16.0, 0.0, 55.0, strict=True),
        F("outerPitch", "Outer Whorl   (open)", 66.0, 25.0, 115.0, strict=True),
    ]),
    SEP("s_wh3"),
    SIMPLE("f_wvar", "Per-Whorl / Per-Petal   (breaks the perfect symmetry)", [
        F("scaleStep", "Scale Growth per Whorl", 0.12, 0.0, 0.5, strict=True),
        F("pitchVariation", "Pitch Jitter   (deg)", 3.0, 0.0, 20.0, strict=True),
        F("scaleVariation", "Scale Jitter", 0.06, 0.0, 0.4, strict=True),
        F("azimuthJitter", "Azimuth Jitter   (deg - nudges each petal off its exact slot)",
          4.0, 0.0, 15.0, strict=True),
        F("radiusJitter", "Radius Jitter   (per-petal radial wobble)", 0.05, 0.0, 0.3, strict=True),
    ]),
]))

ptg.append(TAB("tab_center", "Center", [
    SIMPLE("f_recept", "Receptacle   (seed pod)", [
        B("showReceptacle", "Show Receptacle", 1),
        B("autoReceptacleSize", "Auto Size   (from flower scale)", 1),
        F("receptacleRadiusRatio", "Radius Ratio", 0.11, 0.0, 0.6, dw=D_RC_R),
        F("receptacleRadiusAdjust", "Radius Adjust", 0.0, -0.3, 0.3, dw=D_RC_R),
        F("receptacleHeightRatio", "Height Ratio", 0.09, 0.0, 0.6, dw=D_RC_R),
        F("receptacleHeightAdjust", "Height Adjust", 0.0, -0.3, 0.3, dw=D_RC_R),
        F("receptacleRadiusManual", "Manual Radius", 0.11, 0.0, 0.6, dw=D_RC_M),
        F("receptacleHeightManual", "Manual Height", 0.09, 0.0, 0.6, dw=D_RC_M),
        I("seedCount", "Seed Bumps", 22, 0, 80),
    ]),
    SEP("s_ce1"),
    SIMPLE("f_stamen", "Stamens", [
        B("showStamens", "Show Stamens", 1),
        I("stamenCount", "Count", 70, 0, 500),
        B("autoStamenLength", "Auto Length   (from receptacle radius)", 1),
        F("stamenLengthRatio", "Length Ratio", 0.90, 0.0, 4.0, dw=D_ST_R),
        F("stamenLengthAdjust", "Length Adjust", 0.0, -0.2, 0.2, dw=D_ST_R),
        F("stamenLengthManual", "Manual Length", 0.10, 0.0, 0.5, dw=D_ST_M),
    ]),
]))

ptg.append(TAB("tab_color", "Color", [
    SIMPLE("f_colpetal", "Petal", [
        COL("petalBaseColor", "Base", (0.99, 0.96, 0.88)),
        COL("petalTipColor", "Tip", (0.95, 0.52, 0.68)),
        F("colorFalloff", "Base -> Tip Falloff", 1.7, 0.2, 5.0),
    ]),
    SEP("s_co1"),
    SIMPLE("f_colcenter", "Center", [
        COL("receptacleColor", "Receptacle", (0.83, 0.80, 0.36)),
        COL("stamenColor", "Stamen", (0.98, 0.85, 0.22)),
    ]),
]))

ptg.append(TAB("tab_engine", "Engine", [
    SIMPLE("f_gr", "Game-Ready Output", [
        B("gameReady", "Game-Ready Output   (UV + triangulate + scale + material)", 0),
        F("exportScale", "Export Scale   (UE = 100, Unity = 1)", 1.0, 0.001, 1000.0),
        B("triangulate", "Triangulate", 1, dw="{ gameReady == 0 }"),
        B("doUV", "Auto UV Unwrap   (whole-flower atlas)", 1, dw="{ gameReady == 0 }"),
        STR("targetMaterial", "Material Path   (-> unreal_material / unity_material)"),
    ]),
    SEP("s_en1"),
    SIMPLE("f_inst", "Instancing   (output 2)", [
        STR("instanceAssetPath", "Instance Asset Path   (StaticMesh / prefab)"),
    ]),
]))

for _h in (F("petalThickness", "petalThickness", 0.008, 0.0, 1.0, hidden=True),
           F("receptacleRadius", "receptacleRadius", 0.11, 0.0, 2.0, hidden=True),
           F("receptacleHeight", "receptacleHeight", 0.09, 0.0, 2.0, hidden=True),
           F("stamenLength", "stamenLength", 0.10, 0.0, 2.0, hidden=True),
           F("effInnerRadius", "effInnerRadius", 0.16, 0.0, 2.0, hidden=True)):
    ptg.append(_h)

SUB.setParmTemplateGroup(ptg)

SUB.parm("petalThickness").setExpression(
    'if(ch("autoPetalThickness"),'
    ' ch("petalLength")*ch("petalThicknessRatio"), ch("petalThicknessManual"))')
SUB.parm("receptacleRadius").setExpression(
    'if(ch("autoReceptacleSize"),'
    ' ch("flowerScale")*ch("receptacleRadiusRatio")+ch("receptacleRadiusAdjust"),'
    ' ch("receptacleRadiusManual"))')
SUB.parm("receptacleHeight").setExpression(
    'if(ch("autoReceptacleSize"),'
    ' ch("flowerScale")*ch("receptacleHeightRatio")+ch("receptacleHeightAdjust"),'
    ' ch("receptacleHeightManual"))')
SUB.parm("stamenLength").setExpression(
    'if(ch("autoStamenLength"),'
    ' ch("receptacleRadius")*ch("stamenLengthRatio")+ch("stamenLengthAdjust"),'
    ' ch("stamenLengthManual"))')
SUB.parm("effInnerRadius").setExpression(
    'if(ch("autoInnerRadius"),'
    ' (ch("receptacleRadius")/max(ch("flowerScale"),0.001))*ch("innerRadiusRatio"),'
    ' ch("innerRadius"))')

# endregion

# region VEX   ( %C%  ->  "../" )
# ==============================================================================
#  VEX   ( %C%  ->  "../" )
# ==============================================================================
VEX_SHAPE = r'''
float u = clamp(@P.x + 0.5, 0.0, 1.0);
float v = clamp(@P.y + 0.5, 0.0, 1.0);
float L  = chf("%C%petalLength");
float W  = chf("%C%petalWidth");
float wp = chf("%C%widthProfile");
float sk = chf("%C%widthSkew");
float bn = chf("%C%baseNarrow");
float ts = chf("%C%tipSharpness");
float vs   = pow(v, sk);
float prof = pow(sin(M_PI * vs), wp);
prof *= lerp(bn, 1.0, smooth(0.0, 0.30, v));
prof *= lerp(1.0, 1.0 - ts, smooth(0.55, 1.0, v));
prof  = max(prof, 0.0);
@P = set((u - 0.5) * W * prof, v * L, 0.0);
f@pu = u;
f@pv = v;
'''

VEX_BEND = r'''
float u = f@pu, v = f@pv;
float cup    = chf("%C%cup");
float mr     = chf("%C%midrib");
float curveD = chf("%C%petalCurve");
float curlD  = chf("%C%tipCurl");
float wrk    = chf("%C%wrinkle");
float L      = max(chf("%C%petalLength"), 1e-4);
int   sd     = chi("%C%seed");
float cx = 2.0 * (u - 0.5);
float lp = sin(M_PI * v);
@P.z += cup * (cx * cx) * lp * 0.5;
@P.z -= mr  * (1.0 - abs(cx)) * pow(lp, 0.6) * 0.12;
if (wrk > 0.0) {
    vector np = set(u * 3.0, v * 7.0, sd * 1.37);
    @P.z += (noise(np)        - 0.5) * wrk * 0.10 * lp;
    @P.x += (noise(np + 19.3) - 0.5) * wrk * 0.04 * lp;
}
float k  = radians(curveD) / L;
float s  = @P.y;
float z0 = @P.z;
float a  = k * s + radians(curlD) * pow(smooth(0.55, 1.0, v), 2.0);
float Yc, Zc;
if (abs(k) > 1e-5) { Yc = sin(a) / k;  Zc = (1.0 - cos(a)) / k; }
else               { Yc = s;          Zc = 0.0; }
@P.y = Yc + z0 * -sin(a);
@P.z = Zc + z0 *  cos(a);
'''

VEX_COLOR = r'''
vector b  = chv("%C%petalBaseColor");
vector t  = chv("%C%petalTipColor");
float  fo = chf("%C%colorFalloff");
float  m  = pow(clamp(f@pv, 0.0, 1.0), fo);
@Cd  = lerp(b, t, m);
@Cd *= lerp(0.88, 1.0, abs(f@pu - 0.5) * 2.0);
'''

# shared whorl-loop macro text (kept identical in layout + guide so they match)
_LOOP_HEADER = r'''
int   whorls   = max(chi("%C%whorlCount"), 1);
int   baseCnt  = max(chi("%C%basePetalCount"), 1);
int   inc      = chi("%C%petalIncrement");
float innerR   = chf("%C%effInnerRadius");
float rStep    = chf("%C%radiusStep");
float lift     = chf("%C%whorlLift");
float pLen     = chf("%C%petalLength");
float bgather  = chf("%C%baseGather");
float pGap     = chf("%C%petalGap");
float pWidth   = chf("%C%petalWidth");
int   autoFit  = chi("%C%autoFitWidth");
float budPD    = chf("%C%budPitch");
float innPD    = chf("%C%innerPitch");
float outPD    = chf("%C%outerPitch");
float bloom    = chf("%C%bloom");
float sStep    = chf("%C%scaleStep");
float pTwist   = chf("%C%whorlTwist");
float pitchVar = chf("%C%pitchVariation");
float scaleVar = chf("%C%scaleVariation");
float azJit    = chf("%C%azimuthJitter");
float radJit   = chf("%C%radiusJitter");
int   sd       = chi("%C%seed");
float fs       = chf("%C%flowerScale");
vector up = set(0, 1, 0);
float runningPhase = 0.0;   // accumulated shingle offset, whorl by whorl
'''

VEX_LAYOUT = _LOOP_HEADER + r'''
int totalPetals = 0;
for (int w = 0; w < whorls; w++) {
    totalPetals += max(baseCnt + inc * w, 1);
}

int gid = 0;

for (int w = 0; w < whorls; w++) {
    float wt     = (whorls > 1) ? float(w) / float(whorls - 1) : 0.0;
    int   count  = max(baseCnt + inc * w, 1);

    float slotAngle =
        M_PI * 2.0 / float(count);

    float halfSlot =
        slotAngle * 0.5;

    float phase =
        (w % 2 == 0)
        ? 0.0
        : halfSlot * pTwist;

    float openP  = radians(lerp(innPD, outPD, wt));
    float pitch  = lerp(radians(budPD), openP, bloom);
    float bScale = (1.0 + sStep * w) * fs;

    // keep whorl as morphology group, not ring position
    float whorlBase =
        lift * float(whorls - 1 - w) * pLen * fs;

    for (int i = 0; i < count; i++) {

        float gt =
            (totalPetals > 1)
            ? float(gid) / float(totalPetals - 1)
            : 0.0;

        // ----------------------------------------------------
        // WHORL INTERLOCK POSITION
        // ----------------------------------------------------

        float az =
        phase
         + slotAngle * float(i);

        // radial variation inside each whorl
        float localT =
            (count > 1)
            ? float(i) / float(count - 1)
            : 0.5;

        float radialOffset =
            (localT - 0.5)
            * rStep
            * 0.35;

        float radius =
            (
                innerR
                + rStep * float(w)
                + radialOffset
            )
            * fs;

        // ----------------------------------------------------
        // VARIATION
        // ----------------------------------------------------

        float r1 =
            rand(float(gid) * 131.0 + float(sd) * 977.0) - 0.5;

        float r2 =
            rand(float(gid) * 57.0 + float(sd) * 331.0) - 0.5;

        float r3 =
            rand(float(gid) * 89.0 + float(sd) * 613.0) - 0.5;

        float r4 =
            rand(float(gid) * 211.0 + float(sd) * 157.0) - 0.5;

        float pit =
            pitch + radians(r1 * pitchVar);

        float sc =
            bScale * (1.0 + r2 * scaleVar);

        float azj =
            az + radians(r3 * azJit);

        vector radial =
            set(cos(azj), 0.0, sin(azj));

        float rg =
            lerp(1.0, 0.12, bgather);

        float eRad =
            radius
            * rg
            * (1.0 + r4 * radJit);

        // ----------------------------------------------------
        // HEIGHT
        // ----------------------------------------------------

        float spiralLift =
            (gt - 0.5)
            * lift
            * pLen
            * fs;

        float yLift =
            whorlBase * 0.55
            + spiralLift;

        int pt =
            addpoint(
                0,
                radial * eRad
                + set(0.0, yLift, 0.0)
            );

        // ----------------------------------------------------
        // WIDTH AUTO-FIT
        // ----------------------------------------------------

        float wfit = 1.0;

        if (autoFit) {

            // approximation using local radial spacing
            float approxCount =
                max(float(totalPetals), 1.0);

            float arcPer =
                (2.0 * M_PI * max(eRad, 1e-4))
                / float(max(count, 1));

            float worldW =
                max(pWidth * sc, 1e-5);

            wfit =
                clamp(
                    (arcPer * (1.0 - pGap)) / worldW,
                    0.85,
                    1.0
                );
        }

        // ----------------------------------------------------
        // ORIENTATION
        // ----------------------------------------------------

        vector ydir =
            normalize(
                cos(pit) * up
                + sin(pit) * radial
            );

        vector zdir =
            normalize(
                sin(pit) * up
                - cos(pit) * radial
            );

        vector xdir =
            normalize(
                cross(ydir, zdir)
            );

        matrix3 m =
            set(
                xdir.x, xdir.y, xdir.z,
                ydir.x, ydir.y, ydir.z,
                zdir.x, zdir.y, zdir.z
            );

        setpointattrib(
            0, "orient", pt,
            quaternion(m),
            "set"
        );

        setpointattrib(
            0, "pscale", pt,
            sc,
            "set"
        );

        setpointattrib(
            0, "scale", pt,
            set(wfit, 1.0, 1.0),
            "set"
        );

        setpointattrib(
            0, "whorl", pt,
            w,
            "set"
        );

        gid++;
    }
}
'''

VEX_PETALVAR = r'''
float n = fit01(noise(@P * 3.0 + chi("%C%seed") * 2.13), 0.93, 1.06);
@Cd *= n;
'''

VEX_RECEPT = r'''
@Cd = chv("%C%receptacleColor");
float n = noise(@P * 45.0 + chi("%C%seed") * 1.7);
@P += normalize(set(@P.x, 0.0, @P.z) + 1e-6) * (n - 0.5) * 0.003;
'''

VEX_SEED_PTS = r'''
int   n  = chi("%C%seedCount");
float fs = chf("%C%flowerScale");
float R  = chf("%C%receptacleRadius") * 0.78 * fs;
float H  = chf("%C%receptacleHeight") * fs;
float ga = radians(137.5);
for (int i = 0; i < n; i++) {
    float tt = (n > 1) ? float(i) / float(n - 1) : 0.0;
    float rr = sqrt(tt) * R;
    float a  = i * ga;
    int pt = addpoint(0, set(cos(a) * rr, H * 1.03, sin(a) * rr));
    setpointattrib(0, "pscale", pt, chf("%C%receptacleRadius") * 0.13 * fs, "set");
}
'''
VEX_SEED_COL = r'@Cd = chv("%C%receptacleColor") * 0.55;'

VEX_STAMEN_PTS = r'''
int   n  = max(chi("%C%stamenCount"), 0);
float fs = chf("%C%flowerScale");
float R  = chf("%C%receptacleRadius") * 1.08 * fs;
float H  = chf("%C%receptacleHeight") * 0.42 * fs;
float L  = chf("%C%stamenLength") * fs;
int   sd = chi("%C%seed");
for (int i = 0; i < n; i++) {
    float a  = M_PI * 2.0 * float(i) / float(max(n, 1)) + rand(i * 3 + sd * 7) * 0.35;
    float rr = R * (0.88 + rand(i * 5 + sd * 11) * 0.28);
    int pt = addpoint(0, set(cos(a) * rr, H, sin(a) * rr));
    float lean = radians(14.0 + rand(i * 7 + sd) * 16.0);
    matrix3 m = 1;
    rotate(m, lean, set(1, 0, 0));
    rotate(m, (M_PI * 0.5 - a), set(0, 1, 0));
    setpointattrib(0, "orient", pt, quaternion(m), "set");
    setpointattrib(0, "pscale", pt, L * (0.8 + rand(i * 9 + sd * 3) * 0.5), "set");
}
'''
VEX_STAMEN_LINE = r'''
float v = float(@ptnum) / 5.0;
@P.z += pow(v, 1.6) * 0.20;
@P.x += (noise(v * 4.0 + chi("%C%seed")) - 0.5) * 0.03 * v;
'''
VEX_STAMEN_COL = r'@Cd = chv("%C%stamenColor") * 0.75;'

VEX_ANTHER_PTS = r'''
int   n  = max(chi("%C%stamenCount"), 0);
float fs = chf("%C%flowerScale");
float R  = chf("%C%receptacleRadius") * 1.08 * fs;
float H  = chf("%C%receptacleHeight") * 0.42 * fs;
float L  = chf("%C%stamenLength") * fs;
int   sd = chi("%C%seed");
for (int i = 0; i < n; i++) {
    float a  = M_PI * 2.0 * float(i) / float(max(n, 1)) + rand(i * 3 + sd * 7) * 0.35;
    float rr = R * (0.88 + rand(i * 5 + sd * 11) * 0.28);
    vector base = set(cos(a) * rr, H, sin(a) * rr);
    float lean = radians(14.0 + rand(i * 7 + sd) * 16.0);
    matrix3 m = 1;
    rotate(m, lean, set(1, 0, 0));
    rotate(m, (M_PI * 0.5 - a), set(0, 1, 0));
    vector4 q = quaternion(m);
    float ln = L * (0.8 + rand(i * 9 + sd * 3) * 0.5);
    vector tip = base + qrotate(q, set(0.0, ln, 0.0)) + qrotate(q, set(0.0, 0.0, 0.20 * ln));
    int pt = addpoint(0, tip);
    setpointattrib(0, "orient", pt, q, "set");
    setpointattrib(0, "pscale", pt, ln * 0.9, "set");
}
'''
VEX_ANTHER_COL = r'@Cd = chv("%C%stamenColor");'

# endregion

# region GUIDE
# ---- GUIDE ---------------------------------------------------------------
VEX_GUIDE_RINGS = r'''
int   whorls = max(chi("%C%whorlCount"), 1);
float innerR = chf("%C%effInnerRadius");
float rStep  = chf("%C%radiusStep");
float lift   = chf("%C%whorlLift");
float pLen   = chf("%C%petalLength");
float bgather = chf("%C%baseGather");
float fs     = chf("%C%flowerScale");
int   seg    = 48;
for (int w = 0; w < whorls; w++) {
    float rad = (innerR + rStep * w) * fs * lerp(1.0, 0.12, bgather);
    float y   = lift * float(whorls - 1 - w) * pLen * fs;
    int prim = addprim(0, "poly");
    for (int i = 0; i < seg; i++) {
        float a = M_PI * 2.0 * float(i) / float(seg);
        int pt = addpoint(0, set(cos(a) * rad, y, sin(a) * rad));
        setpointattrib(0, "Cd", pt, {1.0, 0.82, 0.15});
        addvertex(0, prim, pt);
    }
}
'''

VEX_GUIDE_AXES = _LOOP_HEADER + r'''
float pL = chf("%C%petalLength");
for (int w = 0; w < whorls; w++) {
    float wt     = (whorls > 1) ? float(w) / float(whorls - 1) : 0.0;
    int   count  = max(baseCnt + inc * w, 1);
    float radius = (innerR + rStep * w) * fs;
    float whorlBase = lift * float(whorls - 1 - w) * pLen * fs;
    float openP  = radians(lerp(innPD, outPD, wt));
    float pitch  = lerp(radians(budPD), openP, bloom);
    float bScale = (1.0 + sStep * w) * fs;
    float halfSpace = M_PI / float(count);
    float phase      = runningPhase;
    runningPhase += halfSpace * pTwist;
    for (int i = 0; i < count; i++) {
        float az  = phase + M_PI * 2.0 * float(i) / float(count);
        float petalFrac = float(i) / float(max(count, 1));
        float yLift = whorlBase + (petalFrac - 0.5) * lift * pLen * fs * 0.6;
        vector radial = set(cos(az), 0.0, sin(az));
        vector base   = radial * radius * lerp(1.0, 0.12, bgather) + set(0.0, yLift, 0.0);
        vector ydir   = normalize(cos(pitch) * up + sin(pitch) * radial);
        int a = addpoint(0, base);
        int b = addpoint(0, base + ydir * pL * bScale);
        setpointattrib(0, "Cd", a, {0.20, 0.85, 1.0});
        setpointattrib(0, "Cd", b, {0.20, 0.85, 1.0});
        int pr = addprim(0, "polyline");
        addvertex(0, pr, a);
        addvertex(0, pr, b);
    }
}
'''

# endregion

# region NETWORK
# ==============================================================================
#  NETWORK
# ==============================================================================
ROOT = mk("null", "root", -3, 0, "empty root for the detail wrangles")

# endregion

# region PETAL
# ---- PETAL ------------------------------------------------------------------
petal_grid = mk("grid", "petal_grid", 0, 0, "flat sheet, res follows Fast Viewport")
for tok in ("polygon", "poly"):
    try:
        petal_grid.parm("type").set(tok); break
    except Exception:
        pass
setp(petal_grid, "orient", "xy")
try:
    petal_grid.parmTuple("size").set((1.0, 1.0))
except Exception:
    setp(petal_grid, "sizex", 1.0); setp(petal_grid, "sizey", 1.0)
sete(petal_grid, "rows", 'if(ch("../fastViewport"), 10, ch("../petalRes"))')
sete(petal_grid, "cols", 'max(5, int(if(ch("../fastViewport"), 10, ch("../petalRes")) * 0.5))')

petal_shape = wr("petal_shape", 2, VEX_SHAPE, 0, 1, petal_grid, comment="outline")
petal_bend = wr("petal_bend", 2, VEX_BEND, 0, 2, petal_shape, comment="cup + arc + curl + wrinkle")
petal_color = wr("petal_color", 2, VEX_COLOR, 0, 3, petal_bend, comment="base -> tip gradient")

petal_shell = mk("polyextrude::2.0", "petal_shell", 1, 3, "real thickness")
petal_shell.setInput(0, petal_color)
setp(petal_shell, "outputfront", 1)
setp(petal_shell, "outputback", 1)
setp(petal_shell, "outputside", 1)
sete(petal_shell, "dist", 'ch("../petalThickness")')

petal_solid_sw = mk("switch", "petal_solid_switch", 0, 4, "solid off when Fast Viewport")
petal_solid_sw.setInput(0, petal_color)
petal_solid_sw.setInput(1, petal_shell)
sete(petal_solid_sw, "input", 'if(ch("../fastViewport"), 0, ch("../petalSolid"))')

# endregion

# region LAYOUT + COPY
# ---- LAYOUT + COPY -------------------------------------------------------
petal_layout = wr("petal_layout", 0, VEX_LAYOUT, 4, 0, ROOT,
                  comment="1 point / petal : pos + orient + pscale")
petals_copy = mk("copytopoints::2.0", "petals_copy", 3, 6, "stamp petal onto points")
petals_copy.setInput(0, petal_solid_sw)
petals_copy.setInput(1, petal_layout)
setp(petals_copy, "useorient", 1)
petals_out = wr("petal_variation", 2, VEX_PETALVAR, 3, 7, petals_copy, comment="colour break-up")

PETAL_NODES = [petal_grid, petal_shape, petal_bend, petal_color, petal_shell,
               petal_solid_sw, petal_layout, petals_copy, petals_out]

# endregion

# region CENTER
# ---- CENTER ---------------------------------------------------------------
recept_tube = mk("tube", "receptacle_tube", 7, 0, "obconic seed pod")
for tok in ("polygon", "poly"):
    try:
        recept_tube.parm("type").set(tok); break
    except Exception:
        pass
setp(recept_tube, "cap", 1)
setp(recept_tube, "cols", 28)
setp(recept_tube, "rows", 6)
sete(recept_tube, "rad1", 'ch("../receptacleRadius") * ch("../flowerScale")')
sete(recept_tube, "rad2", 'ch("../receptacleRadius") * 0.45 * ch("../flowerScale")')
sete(recept_tube, "height", 'ch("../receptacleHeight") * ch("../flowerScale")')
sete(recept_tube, "ty", 'ch("../receptacleHeight") * 0.5 * ch("../flowerScale")')
if recept_tube.parm("rad1") is None:
    sete(recept_tube, "radx", 'ch("../receptacleRadius") * ch("../flowerScale")')
    sete(recept_tube, "rady", 'ch("../receptacleRadius") * ch("../flowerScale")')

recept_shape = wr("receptacle_shape", 2, VEX_RECEPT, 7, 1, recept_tube, comment="colour + texture")

seed_pts = wr("seed_points", 0, VEX_SEED_PTS, 9, 0, ROOT, comment="spiral of bump points")
seed_sphere = mk("sphere", "seed_sphere", 10, 0, "bump primitive")
for tok in ("polygon", "poly"):
    try:
        seed_sphere.parm("type").set(tok); break
    except Exception:
        pass
setp(seed_sphere, "rows", 6)
setp(seed_sphere, "cols", 8)
seed_copy = mk("copytopoints::2.0", "seed_copy", 9, 2, "bumps -> points")
seed_copy.setInput(0, seed_sphere)
seed_copy.setInput(1, seed_pts)
seed_color = wr("seed_color", 2, VEX_SEED_COL, 9, 3, seed_copy, comment="darker seed colour")

recept_merge = mk("merge", "receptacle_merge", 7, 4, "pod + seed bumps")
recept_merge.setInput(0, recept_shape)
recept_merge.setInput(1, seed_color)

recept_off = mk("null", "receptacle_off", 8, 5, "empty (OFF)")
recept_sw = mk("switch", "receptacle_switch", 7, 5, "showReceptacle")
recept_sw.setInput(0, recept_off)
recept_sw.setInput(1, recept_merge)
sete(recept_sw, "input", 'ch("../showReceptacle")')

CENTER_NODES = [recept_tube, recept_shape, seed_pts, seed_sphere, seed_copy,
                seed_color, recept_merge, recept_off, recept_sw]

# endregion

# region STAMENS
# ---- STAMENS ------------------------------------------------------------
stamen_pts = wr("stamen_points", 0, VEX_STAMEN_PTS, 13, 0, ROOT, comment="filament roots")
stamen_line = mk("line", "stamen_line", 15, 0, "6-pt template filament")
try:
    stamen_line.parmTuple("origin").set((0.0, 0.0, 0.0))
    stamen_line.parmTuple("dir").set((0.0, 1.0, 0.0))
except Exception:
    pass
setp(stamen_line, "dist", 1.0)
setp(stamen_line, "points", 6)
stamen_line_curve = wr("stamen_line_curve", 2, VEX_STAMEN_LINE, 15, 1, stamen_line, comment="bow")
stamen_copy = mk("copytopoints::2.0", "stamen_copy", 14, 3, "filament -> roots")
stamen_copy.setInput(0, stamen_line_curve)
stamen_copy.setInput(1, stamen_pts)
setp(stamen_copy, "useorient", 1)
stamen_wire = mk("polywire", "stamen_wire", 14, 4, "tube thickness")
stamen_wire.setInput(0, stamen_copy)
sete(stamen_wire, "radius", 'ch("../stamenLength") * 0.028 * ch("../flowerScale")')
stamen_color = wr("stamen_color", 2, VEX_STAMEN_COL, 14, 5, stamen_wire, comment="pale colour")

anther_pts = wr("anther_points", 0, VEX_ANTHER_PTS, 17, 0, ROOT, comment="tips")
anther_sphere = mk("sphere", "anther_sphere", 18, 0, "anther primitive")
for tok in ("polygon", "poly"):
    try:
        anther_sphere.parm("type").set(tok); break
    except Exception:
        pass
setp(anther_sphere, "rows", 6)
setp(anther_sphere, "cols", 8)
anther_squash = mk("xform", "anther_squash", 18, 1, "grain shape (+Y)")
anther_squash.setInput(0, anther_sphere)
try:
    anther_squash.parmTuple("s").set((0.09, 0.26, 0.09))
except Exception:
    anther_squash.parmTuple("scale").set((0.09, 0.26, 0.09))
anther_copy = mk("copytopoints::2.0", "anther_copy", 17, 3, "anthers -> tips")
anther_copy.setInput(0, anther_squash)
anther_copy.setInput(1, anther_pts)
setp(anther_copy, "useorient", 1)
anther_color = wr("anther_color", 2, VEX_ANTHER_COL, 17, 4, anther_copy, comment="bright colour")

stamen_full = mk("merge", "stamen_full", 15, 6, "filaments + anthers")
stamen_full.setInput(0, stamen_color)
stamen_full.setInput(1, anther_color)

stamen_off = mk("null", "stamen_off", 13, 8, "empty (OFF)")
stamen_sw = mk("switch", "stamen_switch", 15, 8,
               "0 off  /  1 points (Fast)  /  2 full")
stamen_sw.setInput(0, stamen_off)
stamen_sw.setInput(1, stamen_pts)
stamen_sw.setInput(2, stamen_full)
sete(stamen_sw, "input", 'if(ch("../showStamens"), if(ch("../fastViewport"), 1, 2), 0)')

STAMEN_NODES = [stamen_pts, stamen_line, stamen_line_curve, stamen_copy, stamen_wire,
                stamen_color, anther_pts, anther_sphere, anther_squash, anther_copy,
                anther_color, stamen_full, stamen_off, stamen_sw]

# endregion

# region ASSEMBLE
# ---- ASSEMBLE ---------------------------------------------------------------
flower_merge = mk("merge", "flower_merge", 6, 11, "petals + receptacle + stamens")
flower_merge.setInput(0, petals_out)
flower_merge.setInput(1, recept_sw)
flower_merge.setInput(2, stamen_sw)

flower_subdiv = mk("subdivide", "flower_subdiv", 8, 12, "OpenSubdiv")
flower_subdiv.setInput(0, flower_merge)
sete(flower_subdiv, "iterations", 'ch("../subdivIter")')

subdiv_sw = mk("switch", "subdiv_switch", 6, 12, "off when Fast Viewport")
subdiv_sw.setInput(0, flower_merge)
subdiv_sw.setInput(1, flower_subdiv)
sete(subdiv_sw, "input", 'if(ch("../fastViewport"), 0, ch("../doSubdiv"))')

flower_normal = mk("normal", "flower_normal", 6, 13, "shading normals")
flower_normal.setInput(0, subdiv_sw)
setp(flower_normal, "cuspangle", 40.0)

out_src = flower_normal
try:
    matnet = SUB.createNode("matnet", "materials")
    matnet.setPosition(hou.Vector2(20 * COL_W, -13 * ROW_H))
    shader = None
    for st in ("principledshader::2.0", "principledshader"):
        try:
            shader = matnet.createNode(st, "lotus_petal"); break
        except hou.OperationFailed:
            pass
    if shader:
        for pn, val in (("rough", 0.34), ("sss", 0.12),
                        ("ssscolorr", 0.98), ("ssscolorg", 0.55), ("ssscolorb", 0.62),
                        ("sheen", 0.35), ("sheentint", 0.5)):
            setp(shader, pn, val)
        for tgl in ("basecolor_useColorAttribute", "basecolor_usePointColor"):
            setp(shader, tgl, 1)
        assign = mk("material", "assign_material", 6, 14, "assign petal shader")
        assign.setInput(0, flower_normal)
        setp(assign, "shop_materialpath1", shader.path())
        out_src = assign
        ASSIGN_NODE = assign
    else:
        ASSIGN_NODE = None
except Exception:
    ASSIGN_NODE = None

# endregion

# region GAME-READY chain  (OUT 0 passes straight through when gameReady is off)
# ---- GAME-READY chain  (OUT 0 passes straight through when gameReady is off) --
gr_tri = mk("divide", "gr_triangulate", 9, 15, "triangulate: convex, 3 sides")
setp(gr_tri, "convex", 1)
setp(gr_tri, "numsides", 3)
setp(gr_tri, "brick", 0)
gr_tri.setInput(0, out_src)
gr_tri_sw = mk("switch", "gr_tri_switch", 7, 15, "triangulate gate")
gr_tri_sw.setInput(0, out_src)
gr_tri_sw.setInput(1, gr_tri)
sete(gr_tri_sw, "input", 'if(ch("../gameReady"), ch("../triangulate"), 0)')

gr_uv = mk("uvunwrap", "gr_uvunwrap", 9, 16, "auto UV atlas for the whole flower")
gr_uv.setInput(0, gr_tri_sw)
gr_uv_sw = mk("switch", "gr_uv_switch", 7, 16, "UV gate")
gr_uv_sw.setInput(0, gr_tri_sw)
gr_uv_sw.setInput(1, gr_uv)
sete(gr_uv_sw, "input", 'if(ch("../gameReady"), ch("../doUV"), 0)')

gr_mat = wr("gr_material_attribs", 0, r'''
string m = chs("%C%targetMaterial");
if (m != "") {
    s@shop_materialpath = m;
    s@unreal_material   = m;   // Houdini Engine -> UE material slot
    s@unity_material    = m;   // Houdini Engine -> Unity material
}
''', 9, 17, gr_uv_sw, comment="engine material-path attributes")

gr_scale = mk("xform", "gr_export_scale", 9, 18, "metres -> engine units (UE = x100)")
gr_scale.setInput(0, gr_mat)
sete(gr_scale, "scale", 'ch("../exportScale")')

gr_sw = mk("switch", "gameready_switch", 7, 18, "raw  vs  game-ready")
gr_sw.setInput(0, out_src)
gr_sw.setInput(1, gr_scale)
sete(gr_sw, "input", 'ch("../gameReady")')

OUT_MAIN = mk("output", "OUT", 7, 20, "output 0  ->  flower mesh")
OUT_MAIN.setInput(0, gr_sw)
setp(OUT_MAIN, "outputidx", 0)
OUT_MAIN.setDisplayFlag(True)
OUT_MAIN.setRenderFlag(True)

# ---- OUT 2 : one point for engine instancing (flower as set-dressing) --------
inst_pt = mk("add", "instance_point", 12, 20, "single point at the origin")
setp(inst_pt, "points", 1)
inst_w = wr("instance_attribs", 2, r'''
string a = chs("%C%instanceAssetPath");
s@unreal_instance = a;      // UE   : path to the Static Mesh uasset
s@unity_instance  = a;      // Unity: path to the prefab / mesh
p@orient  = set(0.0, 0.0, 0.0, 1.0);
f@pscale  = chf("%C%flowerScale");
v@N       = set(0, 0, 1);
v@up      = set(0, 1, 0);
''', 12, 21, inst_pt, comment="unreal_instance / unity_instance + transform")
OUT_INST = mk("output", "OUT_instance", 12, 22, "output 2  ->  instancing point")
OUT_INST.setInput(0, inst_w)
setp(OUT_INST, "outputidx", 2)

# endregion

# region disk export ROPs  (manual: hit 'Save to Disk')
# ---- disk export ROPs  (manual: hit 'Save to Disk') ------------------------
rop_fbx = mk("rop_fbx", "EXPORT_fbx", 7, 22, "Save to Disk  ->  FBX")
rop_fbx.setInput(0, OUT_MAIN)
setp(rop_fbx, "sopoutput", "S:/Houdini/export/lotus_flower.fbx")
ENGINE_EXTRA = []
try:
    rop_gltf = mk("rop_gltf", "EXPORT_gltf", 9, 22, "Save to Disk  ->  glTF / GLB")
    rop_gltf.setInput(0, OUT_MAIN)
    setp(rop_gltf, "file", "S:/Houdini/export/lotus_flower.glb")
    ENGINE_EXTRA.append(rop_gltf)
except Exception:
    pass

ASSEMBLE_NODES = [flower_merge, flower_subdiv, subdiv_sw, flower_normal, ASSIGN_NODE]
ENGINE_NODES = [gr_tri, gr_tri_sw, gr_uv, gr_uv_sw, gr_mat, gr_scale, gr_sw,
                OUT_MAIN, inst_pt, inst_w, OUT_INST, rop_fbx] + ENGINE_EXTRA

# endregion

# region GUIDE
# ---- GUIDE ----------------------------------------------------------------
guide_rings = wr("guide_rings", 0, VEX_GUIDE_RINGS, 21, 0, ROOT, comment="whorl radius rings")
guide_axes = wr("guide_axes", 0, VEX_GUIDE_AXES, 23, 0, ROOT, comment="per-petal length axis")
guide_merge = mk("merge", "guide_merge", 22, 2, "rings + axes")
guide_merge.setInput(0, guide_rings)
guide_merge.setInput(1, guide_axes)
guide_off = mk("null", "guide_off", 21, 3, "empty (OFF)")
guide_sw = mk("switch", "guide_switch", 22, 4, "showGuide  (also the HDA Guide node)")
guide_sw.setInput(0, guide_off)
guide_sw.setInput(1, guide_merge)
sete(guide_sw, "input", 'ch("../showGuide")')
try:
    guide_sw.setTemplateFlag(True)          # draw as viewport overlay immediately
except Exception:
    pass

OUT_GUIDE = mk("output", "OUT_guide", 22, 5, "output 1  ->  guide geometry")
OUT_GUIDE.setInput(0, guide_sw)
setp(OUT_GUIDE, "outputidx", 1)

GUIDE_NODES = [guide_rings, guide_axes, guide_merge, guide_off, guide_sw, OUT_GUIDE]

# endregion

# region network boxes
# ==============================================================================
#  network boxes
# ==============================================================================
netbox("box_petal", "PETAL + LAYOUT", (0.30, 0.34, 0.42), PETAL_NODES)
netbox("box_center", "CENTER", (0.42, 0.38, 0.28), CENTER_NODES)
netbox("box_stamens", "STAMENS", (0.40, 0.32, 0.40), STAMEN_NODES)
netbox("box_assemble", "ASSEMBLE  (merge / subdiv / material)", (0.28, 0.30, 0.44), ASSEMBLE_NODES)
netbox("box_guide", "GUIDE  ->  OUT 1  (template-flagged)", (0.46, 0.44, 0.20), GUIDE_NODES)
netbox("box_engine", "ENGINE  ->  OUT 0 game-ready  +  OUT 2 instance  +  export ROPs",
       (0.18, 0.42, 0.40), ENGINE_NODES)

SUB.setDisplayFlag(True)
SUB.setRenderFlag(True)

# endregion

# region turn the subnet into a SOP HDA  (best effort)
# ==============================================================================
#  turn the subnet into a SOP HDA  (best effort)
# ==============================================================================
ASSET = SUB
try:
    _ext = {hou.licenseCategoryType.Commercial: "hda",
            hou.licenseCategoryType.Indie: "hdalc",
            hou.licenseCategoryType.Apprentice: "hdanc"}.get(
                hou.licenseCategoryType(), "hda")
    HDA_PATH = "S:/Houdini/lotus_flower.%s" % _ext
    ASSET = SUB.createDigitalAsset(
        name="lotus_flower",
        hda_file_name=HDA_PATH,
        description="Lotus Flower",
        min_num_inputs=0,
        max_num_inputs=0,
    )
    try:
        ASSET.setName("lotus", unique_name=True)
    except Exception:
        pass
    print("HDA created  ->  %s" % HDA_PATH)
    print("The tabs are now the asset's real parameter interface (not 'spare').")
    print("Guide:  Type Properties > Node > Guide  ->  op:`./guide_switch`")
except Exception as e:
    print("=" * 64)
    print("createDigitalAsset FAILED - the 'lotus' subnet is left in place.")
    print("Its tabs are SPARE PARAMETERS on purpose: they turn INTO the real")
    print("HDA interface the moment you  RMB 'lotus' -> Create Digital Asset")
    print("(pick a save path, click Create).  Nothing is wrong with them.")
    print("reason:", repr(e))
    print("=" * 64)

try:
    GEO.layoutChildren()
except Exception:
    pass
ASSET.setCurrent(True, clear_all_selected=True)
print("Done  ->  %s" % ASSET.path())

if "save" in sys.argv:
    p = "S:/Houdini/lotus_flower.hip"
    hou.hipFile.save(p)
    print("saved", p)

# endregion
