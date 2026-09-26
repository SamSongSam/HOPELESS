"""
================================================================================
 ISTRORIGAN - COOK REPORT (evidence for AGENT_AUDIT_HANDOFF rule 6)
================================================================================
 Cooks every node under the city subnet and prints errors / warnings plus the
 key counts. Run after update_in_place.py:
   hython scripts/houdini/cook_report.py output/istrorigan_city.hip
================================================================================
"""
import sys
import hou

NODE_PATH = "/obj/istrorigan_city/istrorigan"

if len(sys.argv) > 1:
    hou.hipFile.load(sys.argv[1], suppress_save_prompt=True, ignore_load_warnings=True)

sub = hou.node(NODE_PATH)
bad = 0
for n in sub.children():
    if not isinstance(n, hou.SopNode):
        continue
    try:
        n.cook(force=False)
    except hou.OperationFailed:
        pass
    errs, warns = n.errors(), n.warnings()
    if errs or warns:
        bad += bool(errs)
        print("%-34s %s%s" % (n.name(), ("ERROR " + " | ".join(e.strip()[:160] for e in errs)) if errs else "",
                              ("WARN " + " | ".join(w.strip()[:160] for w in warns)) if warns else ""))


def count(name):
    n = sub.node(name)
    if n is None:
        return "missing"
    g = n.geometry()
    return "%d pts / %d prims" % (len(g.points()), len(g.prims())) if g else "no geometry"


print("-" * 80)
for name in ("sys03_petal_normals", "pcg_s1_polar_lattice", "pcg_s2_zoning", "pcg_s3_evac", "city_merge", "OUT"):
    print("%-24s %s" % (name, count(name)))
print("nodes with errors: %d" % bad)
