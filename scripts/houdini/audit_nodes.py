import hou
import sys

hou.hipFile.load("d:/2/OWN/HOPELESS/output/istrorigan_city.hip")
sub = hou.node("/obj/istrorigan_city/istrorigan")

all_nodes = sub.children()
print("=" * 90)
print(" HOUDINI MEGASTRUCTURE COMPLETE NODE AUDIT REPORT")
print("=" * 90)
print("Subnet Path:", sub.path())
print("Total Nodes:", len(all_nodes))

errors_found = []
warnings_found = []
node_stats = []

for n in sorted(all_nodes, key=lambda x: x.name()):
    errs = n.errors()
    warns = n.warnings()
    if errs:
        errors_found.append((n.name(), errs))
    if warns:
        warnings_found.append((n.name(), warns))
    
    g = n.geometry() if hasattr(n, "geometry") else None
    n_pts = len(g.points()) if g else 0
    n_prims = len(g.prims()) if g else 0
    pos = n.position()
    comment = n.comment()
    node_stats.append({
        "name": n.name(),
        "type": n.type().name(),
        "pos": (round(pos.x(), 2), round(pos.y(), 2)),
        "pts": n_pts,
        "prims": n_prims,
        "inputs": [inp.name() if inp else None for inp in n.inputs()],
        "comment": comment
    })

print("\n" + "-" * 90)
print("1. ERROR & INTEGRITY AUDIT")
print("-" * 90)
if not errors_found:
    print("  [PASS] 0 ERRORS - All %d nodes cook successfully without any errors!" % len(all_nodes))
else:
    for name, err in errors_found:
        print("  [FAIL] %s: %s" % (name, err))

if not warnings_found:
    print("  [PASS] 0 WARNINGS across all nodes!")
else:
    for name, warn in warnings_found:
        print("  [WARN] %s: %s" % (name, warn))

print("\n" + "-" * 90)
print("2. COMPLETE NODE-BY-NODE INVENTORY (%d NODES)" % len(node_stats))
print("-" * 90)
print("%-24s | %-15s | %-14s | %-8s | %-8s | %s" % ("Node Name", "Type", "Position", "Points", "Prims", "Inputs"))
print("-" * 90)
for s in node_stats:
    inps_str = ", ".join([str(i) for i in s["inputs"]]) if s["inputs"] else "None"
    print("%-24s | %-15s | %-14s | %-8d | %-8d | %s" % (
        s["name"], s["type"], str(s["pos"]), s["pts"], s["prims"], inps_str
    ))

print("\n" + "-" * 90)
print("3. NETWORK BOX AUDIT")
print("-" * 90)
boxes = sub.networkBoxes()
print("Total Network Boxes: %d" % len(boxes))
boxed_nodes = set()
for b in sorted(boxes, key=lambda x: x.comment()):
    b_nodes = b.nodes()
    boxed_nodes.update(b_nodes)
    print("  * [%-35s] (%s) - %d nodes" % (b.comment(), b.name(), len(b_nodes)))
    print("    Nodes: %s" % ", ".join(sorted([n.name() for n in b_nodes])))

unboxed = [n for n in all_nodes if n not in boxed_nodes and n.name() != "root"]
if not unboxed:
    print("  [PASS] 100% of functional nodes are categorized in Network Boxes!")
else:
    print("  Unboxed nodes: %s" % ", ".join([n.name() for n in unboxed]))

print("\n" + "-" * 90)
print("4. STICKY NOTE DOCUMENTATION AUDIT")
print("-" * 90)
notes = sub.stickyNotes()
print("Total Sticky Notes: %d" % len(notes))
for nt in notes:
    print("  * [%-25s] pos=(%.1f, %.1f), size=(%.1f, %.1f)" % (
        nt.name(), nt.position().x(), nt.position().y(), nt.size().x(), nt.size().y()
    ))
    first_line = nt.text().strip().split("\n")[0]
    print("    Header: %s" % first_line)

print("\n" + "=" * 90)
