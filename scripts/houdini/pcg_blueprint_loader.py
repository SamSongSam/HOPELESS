"""
================================================================================
 ISTRORIGAN PCG - STAGE 0: BLUEPRINT LOADER (Python SOP)
================================================================================
 Reads the blueprint data tables straight from the project .md files at cook
 time, so the .md blueprint stays the single source of truth:

   00_CORE/DATA_TABLES/01_DATA_TABLE_DISTRICT_ZONING.md
     - the markdown "Zoning Allocation Table" is authoritative (all rows)
     - the embedded JSON adds MaxBuildingHeight / DensityFalloffExponent / tags;
       rows missing from the JSON inherit from the first JSON row with the same
       DistrictType and are flagged zone_from_json = 0

 Output: one point, detail arrays zone_* (metres, not cm).
 Edit the .md, then press 'Reload Blueprint' on the HDA (or change blueprintRoot).
================================================================================
"""

LOADER_CODE = r'''
import os, re, json, hou
# no literal backtick anywhere in this code: Houdini expands backticks in the
# Python SOP's code parm as hscript expressions
BT = chr(96)

node = hou.pwd()
geo = node.geometry()
geo.clear()
root = node.parent().parm("blueprintRoot").evalAsString()
zon_path = os.path.join(root, "00_CORE", "DATA_TABLES", "01_DATA_TABLE_DISTRICT_ZONING.md")

def num(s):
    s = s.replace(",", "").replace("+", "").strip()
    return float(s)

def span(cell):
    # "15,000 - 110,000" / "-5,000 to +6,000" (en dash or 'to')
    parts = re.split(r"\s*(?:–|—|to)\s*", cell.strip())
    return num(parts[0]), num(parts[-1])

rows = []
if not os.path.exists(zon_path):
    raise hou.NodeError("Blueprint zoning table not found: %s  (check blueprintRoot)" % zon_path)
text = open(zon_path, encoding="utf-8").read()
for line in text.splitlines():
    m = re.match(r"\s*\|\s*" + BT + r"(ZONE_[A-Z_]+)" + BT + r"\s*\|(.*)", line)
    if not m:
        continue
    cells = [c.strip() for c in m.group(2).split("|")]
    if len(cells) < 7:
        continue
    dtype = cells[0].strip(BT + " ")
    sector = cells[2]
    pm = re.search(r"Petal\s+(\d+)", sector)
    if pm:
        petal = int(pm.group(1))
    elif "Core" in sector:
        petal = -1
    elif "Stem" in sector:
        petal = -2
    else:
        petal = -3                      # seabed / root
    rmin, rmax = span(cells[3])
    zmin, zmax = span(cells[4])
    buoy = num(re.sub(r"\(.*?\)", "", cells[5]))
    tags = [t.strip() for t in cells[6].strip(BT + " ").replace(BT, "").split(",") if t.strip()]
    rows.append(dict(name=m.group(1), dtype=dtype, display=cells[1], petal=petal,
                     rmin=rmin, rmax=rmax, zmin=zmin, zmax=zmax, buoy=buoy, tags=tags))

js = {}
for b in re.findall(BT * 3 + r"json\s*(.*?)" + BT * 3, text, re.S):
    try:
        for r in json.loads(b):
            js[r["Name"]] = r
    except Exception:
        pass
by_type = {}
for r in js.values():
    by_type.setdefault(r.get("DistrictType", "").split("::")[-1], r)

missing = []
out = {k: [] for k in ("zone_name", "zone_type", "zone_display", "zone_tags")}
nums = {k: [] for k in ("zone_petal", "zone_tier", "zone_from_json")}
flts = {k: [] for k in ("zone_minR", "zone_maxR", "zone_minZ", "zone_maxZ", "zone_buoyancy_kn",
                        "zone_maxBldH", "zone_falloff")}
tier_by_type = {"Core_Civic": 0, "Petal_MidLiving": 2, "Stem_Engineering": -1, "Root_AbyssalAnchor": -2}
for r in rows:
    j = js.get(r["name"])
    src = j if j is not None else by_type.get(r["dtype"])
    if j is None:
        missing.append(r["name"])
    tags = list(r["tags"])
    if j is not None:
        tags = [t["TagName"] for t in j.get("AllowedModuleTags", {}).get("GameplayTags", [])] or tags
    if r["petal"] >= 0 and not any(t.startswith("Zone.") for t in tags):
        tags.insert(0, "Zone.Petal.%d" % r["petal"])
    out["zone_name"].append(r["name"]); out["zone_type"].append(r["dtype"])
    out["zone_display"].append(r["display"]); out["zone_tags"].append(",".join(tags))
    nums["zone_petal"].append(r["petal"])
    nums["zone_tier"].append(int(src["RingTier"]) if src else tier_by_type.get(r["dtype"], 0))
    nums["zone_from_json"].append(1 if j is not None else 0)
    flts["zone_minR"].append(r["rmin"] * 0.01); flts["zone_maxR"].append(r["rmax"] * 0.01)
    flts["zone_minZ"].append(r["zmin"] * 0.01); flts["zone_maxZ"].append(r["zmax"] * 0.01)
    flts["zone_buoyancy_kn"].append(r["buoy"])
    flts["zone_maxBldH"].append((src["MaxBuildingHeight"] if src else 4500.0) * 0.01)
    flts["zone_falloff"].append(src["DensityFalloffExponent"] if src else 1.0)

geo.createPoint()
for k, v in out.items():
    geo.addArrayAttrib(hou.attribType.Global, k, hou.attribData.String)
    geo.setGlobalAttribValue(k, v)
for k, v in nums.items():
    geo.addArrayAttrib(hou.attribType.Global, k, hou.attribData.Int)
    geo.setGlobalAttribValue(k, v)
for k, v in flts.items():
    geo.addArrayAttrib(hou.attribType.Global, k, hou.attribData.Float)
    geo.setGlobalAttribValue(k, v)
geo.addAttrib(hou.attribType.Global, "blueprint_zoning_path", "")
geo.setGlobalAttribValue("blueprint_zoning_path", zon_path)
geo.addAttrib(hou.attribType.Global, "blueprint_json_missing", "")
geo.setGlobalAttribValue("blueprint_json_missing", ",".join(missing))

'''
