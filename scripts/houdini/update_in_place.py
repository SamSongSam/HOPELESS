"""
================================================================================
 ISTRORIGAN - IN-PLACE UPGRADE (non-destructive)
================================================================================
 Upgrades an EXISTING scene without rebuilding it:
   Part 03 petals -> lotus-grade generator
   Absolute paths -> re-pointed at blueprintRoot ($HIP/..) so the project can move
   PCG Stages 0-2 -> blueprint loader, polar lattice, zoning (replaces the
                     baked-CSV 'py_lattice' layer)
 Details:
   * keeps /obj/istrorigan_city/istrorigan and every other node as-is
   * keeps every parameter value you already set (same-name parms survive)
   * swaps the Academic Petals tab for the lotus-grade one (new parms get defaults)
   * migrates old hand-set rim/keel values into Manual mode so the look holds
   * replaces the petal wrangle snippet, inserts weld/clean/normal if missing
   * works on a plain subnet or on an HDA instance (definition is updated too)

 Run inside Houdini (Python Source Editor) with the project hip open,
 or:  hython scripts/houdini/update_in_place.py <file.hip> [save]
================================================================================
"""

import sys
import os
import re

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
if PACKAGE_DIR not in sys.path:
    sys.path.insert(0, PACKAGE_DIR)

from helpers import mk, setp, sete, get_hou, load_vex
import part03_academic_petals as p03
import pcg_stages

NODE_PATH = "/obj/istrorigan_city/istrorigan"
CREF = "../"

# parms the old petal tab exposed directly and that are now Auto/Manual resolved
LEGACY_TO_MANUAL = {
    "petalRimHeight": ("rimHeightManual", 45.0),   # (manual parm, old default)
    "keelDepth": ("keelDraftManual", 18.0),
}

# parms still sitting on the OLD default get the new default; hand-set values stay
OLD_DEFAULT_BUMPS = {
    "petalURes": (32, 160),   # 32 rings was the coarse shell resolution
}


def _read_legacy(node):
    """Capture hand-set legacy values before the tab is swapped."""
    kept = {}
    for name, (manual, old_default) in LEGACY_TO_MANUAL.items():
        p = node.parm(name)
        if p is None:
            continue
        try:
            has_expr = bool(p.expression())
        except Exception:
            has_expr = False
        if not has_expr and abs(p.eval() - old_default) > 1e-6:
            kept[manual] = p.eval()
    return kept


def _tab_of(ptg, member_parm):
    """Tab folder that holds member_parm. Houdini renames tab folders on save
    (tab_petals -> tab_master_3 ...), so tabs are located by a parm inside them."""
    hou = get_hou()
    if ptg.find(member_parm) is None:
        return None
    f = ptg.containingFolder(member_parm)
    while f is not None and f.folderType() != hou.folderType.Tabs:
        try:
            f = ptg.containingFolder(f)
        except hou.OperationFailed:
            return None
    return f


def _swap_petal_tab(node):
    ptg = node.parmTemplateGroup()
    new_tab = p03.get_parm_templates()
    old_tab = _tab_of(ptg, "petalCount")
    if old_tab is not None:
        ptg.replace(old_tab, new_tab)
    else:
        ptg.append(new_tab)
    # parms the petal VEX needs from other tabs, in case this scene predates them
    from helpers import F, COL
    for tmpl in (F("openAmount", "Academic Petals Open / Tuck Amount", 1.0, 0.0, 1.0),
                 F("submergeAmount", "Global Submersion Amount", 0.0, 0.0, 1.0),
                 COL("colPetalHull", "Petal Hull (Pure White)", (0.94, 0.95, 0.98)),
                 F("stamenRingRadius", "Ring Radius (m)", 220.0, 20.0, 1000.0),
                 F("barrierRadius", "Dome Radius (m)", 1500.0, 500.0, 5000.0),
                 F("barrierHeight", "Dome Height (m)", 650.0, 50.0, 3000.0)):
        if ptg.find(tmpl.name()) is None:
            ptg.append(tmpl)
    pcg_tab = pcg_stages.get_parm_templates()
    old_pcg = _tab_of(ptg, "blueprintRoot")
    if old_pcg is not None:
        ptg.replace(old_pcg, pcg_tab)
    else:
        ptg.append(pcg_tab)
    node.setParmTemplateGroup(ptg)          # same-name parms keep their values
    p03.setup_expressions(node)


def _refresh_part_snippets(node):
    """Push the current vex/*.vfl code into every existing part wrangle, so fixes to
    any part (not only petals / PCG) reach the scene. partNN_name.vfl -> sysNN_name."""
    vex_dir = os.path.join(PACKAGE_DIR, "vex")
    extra = {"guide_network.vfl": "guide_network_gen", "gr_material.vfl": "gr_material_attribs",
             "instance_attribs.vfl": "instance_attribs"}
    n_done = 0
    for fn in sorted(os.listdir(vex_dir)):
        m = re.match(r"part(\d\d)_(\w+)\.vfl$", fn)
        target = ("sys%s_%s" % (m.group(1), m.group(2))) if m else extra.get(fn)
        w = node.node(target) if target else None
        if w is None or w.parm("snippet") is None:
            continue
        code = load_vex(fn).replace("%C%", CREF)
        if w.parm("snippet").unexpandedString() != code:
            w.parm("snippet").set(code)
            n_done += 1
    if n_done:
        print("[*] refreshed VEX in %d part wrangles from vex/*.vfl" % n_done)


def _upgrade_network(node):
    w = node.node("sys03_academic_petals")
    if w is None:
        raise RuntimeError("sys03_academic_petals not found under %s" % node.path())
    w.parm("snippet").set(load_vex("part03_academic_petals.vfl").replace("%C%", CREF))
    w.setComment("Lotus-grade petal hulls + hinge pose + 45m collision guard")

    downstream = [(c.outputNode(), c.inputIndex()) for c in w.outputConnections()]
    pos = w.position()

    fuse = node.node("sys03_petal_weld") or mk(node, "fuse", "sys03_petal_weld", 0, 0, "weld coincident points")
    clean = node.node("sys03_petal_clean") or mk(node, "clean", "sys03_petal_clean", 0, 0, "drop degenerate prims")
    nrm = node.node("sys03_petal_normals") or mk(node, "normal", "sys03_petal_normals", 0, 0, "hard edges at rim/light reveal")
    hou = get_hou()
    fuse.setPosition(pos + hou.Vector2(0, -1.0))
    clean.setPosition(pos + hou.Vector2(0, -2.0))
    nrm.setPosition(pos + hou.Vector2(0, -3.0))
    fuse.setInput(0, w)
    clean.setInput(0, fuse)
    nrm.setInput(0, clean)
    sete(fuse, "dist", 'ch("%spetalFuseDist")' % CREF)
    setp(nrm, "cuspangle", 35.0)

    chain = {fuse, clean, nrm}
    for out_node, idx in downstream:
        if out_node not in chain:
            out_node.setInput(idx, nrm)

    box = node.findNetworkBox("box_petals")
    if box is not None:
        for n in (fuse, clean, nrm):
            box.addNode(n)
        box.fitAroundContents()


def _install_pcg(node):
    """Create or refresh PCG Stages 0-2 and feed them into the lattice switch."""
    hou = get_hou()
    petals = node.node("sys03_petal_normals")
    root = node.node("root")
    s0 = node.node("pcg_s0_blueprint")
    if s0 is None:
        anchor = node.node("py_lattice") or node.node("sw_lattice") or petals
        pos = anchor.position()
        res = pcg_stages.build_nodes(node, root, petals, col=0, row=0, cref=CREF)
        view, nodes = res["lattice_view"], res["nodes"]
        for i, n in enumerate(nodes):
            n.setPosition(pos + hou.Vector2(3.0 + (i % 3) * 2.6, -1.4 * (i // 3)))
    else:
        from pcg_blueprint_loader import LOADER_CODE
        s0.parm("python").set(LOADER_CODE)
        node.node("pcg_s1_polar_lattice").parm("snippet").set(
            load_vex("pcg_s1_polar_lattice.vfl").replace("%C%", CREF))
        node.node("pcg_s2_zoning").parm("snippet").set(
            load_vex("pcg_s2_zoning.vfl").replace("%C%", CREF))
        node.node("pcg_s1_polar_lattice").setInput(1, petals)
        view = node.node("pcg_s2_view_switch")
        if node.node("pcg_s3_graph") is None:
            pos = node.node("pcg_s2_zoning").position()
            g = pcg_stages.build_stage3(node, root, petals, 0, 0, CREF)
            for i, n in enumerate(g[4]):
                n.setPosition(pos + hou.Vector2(8.0 + (i % 2) * 2.6, -1.4 * (i // 2)))
        else:
            node.node("pcg_s3_graph").parm("snippet").set(load_vex("pcg_s3_graph.vfl").replace("%C%", CREF))
            node.node("pcg_s3_evac").parm("snippet").set(load_vex("pcg_s3_evac.vfl").replace("%C%", CREF))
            node.node("pcg_s3_graph").setInput(1, petals)

    sw = node.node("sw_lattice")
    if sw is not None:
        sw.setInput(1, view)
    swt = node.node("sw_transit")
    if swt is not None:
        swt.setInput(1, node.node("pcg_s3_view_switch"))
    for legacy, stage in (("py_lattice", "1-2"), ("lattice_clearance_validator", "1-2"),
                          ("py_transit", "3"), ("transit_conduits_3d", "3")):
        n = node.node(legacy)
        if n is not None:
            n.setComment("LEGACY baked CSV - disconnected, replaced by PCG Stage %s" % stage)
    for toggle in ("showLattice", "showTransit"):
        p = node.parm(toggle)
        if p is not None and not p.eval():
            p.set(1)
            print("[*] %s switched ON so the live PCG layer is visible" % toggle)


ABS_OUTPUT = re.compile(r'"[A-Za-z]:[/\\][^"]*?[/\\]output[/\\]')


def _repath(node):
    """Replace absolute project paths baked into existing nodes (old d:/2/OWN/HOPELESS
    checkout) with paths relative to the HDA's blueprintRoot parm ($HIP/..)."""
    n_fixed = 0
    bp = '`chs("../blueprintRoot")`/output/'
    for child in node.children():
        tname = child.type().name()
        for parm_name in ("file", "sopoutput"):
            parm = child.parm(parm_name)
            if parm is None or parm.parmTemplate().type().name() != "String":
                continue
            raw = parm.unexpandedString()
            m = re.search(r"[/\\]output[/\\](.*)$", raw.replace("\\", "/"))
            if m and re.match(r"^[A-Za-z]:[/\\]", raw):
                parm.set(bp + m.group(1))
                n_fixed += 1
        if tname == "python":
            code = child.parm("python").eval()
            if ABS_OUTPUT.search(code):
                code = ABS_OUTPUT.sub('ROOT + "/output/', code)
                if "ROOT = " not in code:
                    code = code.replace("import csv, os, hou\n",
                                        "import csv, os, hou\n"
                                        "ROOT = hou.pwd().parent().evalParm(\"blueprintRoot\")   # project root ($HIP/..)\n", 1)
                child.parm("python").set(code)
                n_fixed += 1
    if n_fixed:
        print("[*] re-pathed %d node parms to blueprintRoot ($HIP/..)" % n_fixed)


def upgrade(node_path=NODE_PATH, save_path=None):
    hou = get_hou()
    node = hou.node(node_path)
    if node is None:
        raise RuntimeError("%s not found - open the project hip first" % node_path)

    definition = node.type().definition()
    if definition is not None:
        node.allowEditingOfContents()

    kept = _read_legacy(node)
    bumps = [name for name, (old, _new) in OLD_DEFAULT_BUMPS.items()
             if node.parm(name) is not None and node.parm(name).eval() == old]
    _swap_petal_tab(node)
    for name in bumps:
        node.parm(name).set(OLD_DEFAULT_BUMPS[name][1])
        print("[*] %s was on the old default -> %s" % (name, OLD_DEFAULT_BUMPS[name][1]))
    if kept:
        node.parm("autoPetalSection").set(0)
        for manual, value in kept.items():
            node.parm(manual).set(value)

    _refresh_part_snippets(node)
    _upgrade_network(node)
    _install_pcg(node)
    _repath(node)

    # baked OBJs are not procedural and would hide the new petals
    hr = node.parm("useHighResParts")
    if hr is not None and hr.eval():
        hr.set(0)
        print("[*] useHighResParts was ON (baked OBJ) -> switched OFF so the procedural petals show")

    if definition is not None:
        definition.updateFromNode(node)
        definition.save(definition.libraryFilePath(), node)
        print("[+] HDA definition updated -> %s" % definition.libraryFilePath())

    geo = node.node("sys03_petal_normals").geometry()
    try:
        gap = geo.attribValue("min_clearance_m")
        sc = geo.attribValue("guard_pitch_scale")
        print("[+] petals cooked: %d points, min clearance %.1f m, guard pitch scale %.3f"
              % (len(geo.points()), gap, sc))
    except Exception as e:
        print("[!] petals did not cook cleanly: %s" % e)
        errs = node.node("sys03_academic_petals").errors()
        if errs:
            print("\n".join(errs))

    if kept:
        print("[*] kept your hand-set values in Manual mode: %s" % kept)
    if save_path:
        hou.hipFile.save(save_path)
        print("[+] saved -> %s" % save_path)
    s2 = node.node("pcg_s2_zoning").geometry()
    try:
        cand = len([pt for pt in s2.points() if pt.attribValue("BuildCandidate")])
        print("[+] PCG Stage 1-2: %d lattice points, %d build candidates, JSON gaps: %s"
              % (len(s2.points()), cand,
                 node.node("pcg_s0_blueprint").geometry().attribValue("blueprint_json_missing") or "none"))
    except Exception as e:
        print("[!] PCG stages did not cook cleanly: %s" % e)
        for nm in ("pcg_s0_blueprint", "pcg_s1_polar_lattice", "pcg_s2_zoning"):
            errs = node.node(nm).errors()
            if errs:
                print("  %s: %s" % (nm, "; ".join(errs)))
    try:
        g = node.node("pcg_s3_evac").geometry()
        print("[+] PCG Stage 3: %d graph nodes, %d edges, %d bridges (%d retracted), max evac %.0f m"
              % (len(g.points()), len(g.prims()), g.attribValue("graph_bridges") if g.findGlobalAttrib("graph_bridges") else 0,
                 g.attribValue("graph_bridges_retracted") if g.findGlobalAttrib("graph_bridges_retracted") else 0,
                 g.attribValue("evac_max_distance_m")))
    except Exception as e:
        print("[!] PCG Stage 3 did not cook cleanly: %s" % e)
        for nm in ("pcg_s3_graph", "pcg_s3_evac"):
            n = node.node(nm)
            if n is not None and n.errors():
                print("  %s: %s" % (nm, "; ".join(n.errors())))
    print("[+] Upgraded in place at %s" % node.path())
    return node


if __name__ == "__main__":
    hou = get_hou()
    args = [a for a in sys.argv[1:] if a != "save"]
    if args:
        hou.hipFile.load(args[0], suppress_save_prompt=True)
    upgrade(save_path=(hou.hipFile.path() if "save" in sys.argv else None))
