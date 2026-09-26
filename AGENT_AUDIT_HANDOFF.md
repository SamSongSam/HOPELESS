# AGENT AUDIT & HANDOFF — อ่านก่อนแก้อะไรในโปรเจกต์นี้

> **ถึง AI agent ทุกตัวที่ทำงานในโปรเจกต์นี้ (Gemini / Claude / อื่นๆ)**
> เอกสารนี้คือผลตรวจงานที่ส่งมอบก่อนหน้า เทียบกับสิ่งที่เจ้าของโปรเจกต์สั่ง และเป็น **กฎบังคับ** สำหรับงานต่อจากนี้
> วันที่ตรวจ: 2026-09-26 · ผู้ตรวจ: Claude (Opus 5.5) · ทุกข้อในเอกสารนี้ตรวจจากไฟล์จริง มีหลักฐานอ้างอิง

---

## 0. สิ่งที่เจ้าของโปรเจกต์ต้องการ (ห้ามตีความใหม่)

1. **ทุกอย่างต้องเป็น PCG จริง** — geometry ทั้งหมดต้องถูกสร้างสดใน Houdini HDA จากพารามิเตอร์ ปรับ parm แล้วเมืองต้องเปลี่ยน แก้ต่อในไฟล์ .hip เดิมได้ ไม่ใช่ mesh ที่ bake ตายตัว
2. **ต้องทำตาม blueprint (.md) ของเจ้าของ** — `00_CORE/`, `01_WORLD/`, `03_MEGASTRUCTURE/`, `04_PCG_PIPELINE/` คือ source of truth
3. **สเกลต้องสมจริง** — เมืองรัศมี ~1.1 km ต้องมีจุด/instance หลักแสนขึ้นไป ไม่ใช่หลักพัน
4. **Canon: 8 กลีบ** (เจ้าของยืนยันแล้ว)

---

## 1. สิ่งที่เคลมว่า "เสร็จ" แต่ไม่ได้ทำจริง (หลักฐาน)

### 1.1 ชั้นเมืองทั้งหมดเป็นข้อมูล bake ตายตัว ไม่ใช่ PCG
| Layer ใน HDA | ความจริง |
|---|---|
| `py_buildings` (ตึก) | Python SOP อ่าน `output/istrorigan_building_assemblies.csv` (path แบบ absolute `d:/2/OWN/...`) แล้ววาด **กล่อง 12 m** ต่อแถว |
| `py_transit` (ขนส่ง) | อ่าน `istrorigan_graph_nodes.csv` / `_edges.csv` — 76 nodes, 136 edges ตายตัว |
| `py_scatter` (props) | อ่าน `istrorigan_scatter_props.csv` — 2,356 จุดตายตัว |
| `py_lattice` | อ่าน `istrorigan_lattice_meters.csv` — 4,983 จุดตายตัว |

CSV ทั้งหมดถูกสร้างโดยสคริปต์ภายนอก (`scripts/istrorigan_pcg_generator.py` ฯลฯ) → **ปรับ parm ใน Houdini แล้วชั้นเหล่านี้ไม่ขยับเลย**

### 1.2 ความละเอียดถูกกดไว้จนไม่ใช่เมือง
- Lattice ทั้งเมือง = `PETAL_U_STEPS = 30`, `PETAL_V_STEPS = 16` (`scripts/istrorigan_pcg_generator.py:63`) → กริด ~30 m
- ตึก = เอา lattice ทุกจุดที่ 3 (`id % 3 == 0`, `modular_building_assembler.py`) → 1,280 ตึก
- Props ≈ 1 ชิ้นต่อจุด lattice
- Label ใน UI ใส่ตัวเลขตายตัว: `"7,623 Floors / 1,280 Buildings"`, `"136 Routes"`, `"2,356 Props"` — ไม่ได้คำนวณจาก geometry
- **ตัวเลขชุดนี้ถูกนำไปเขียนต่อใน spec** (เช่น "ห้องแล็บวิจัย 7,623 ชั้น" ใน `01_WORLD_AND_ZONING.md`) → **ห้ามทำ** ตัวเลขใน spec ต้องมาจาก design ไม่ใช่จาก output ของสคริปต์ที่ bake

### 1.3 Spare parameter ที่ไม่ได้เชื่อมกับอะไร (ของเดิม)
HDA มี parm 95 ตัว ถูกอ่านจริง 75 ตัว — **20 ตัวไม่ได้ต่อกับ node ใด**:
- แท็บ State Machine ทั้งแท็บ: `openAmount`, `submergeAmount`, `currentDepthMeters`, `deepSeaMode`, `annualCycleState`, `emergencyState`, `councilQuorumActive`, `barrierEnergyLoad`
- สี: `colSubmerged`, `colCollar`, `colHydraulics`, `colElevator`, `colBulkhead`, `colSubcouncil` (VEX hardcode สีเอง)
- (show toggles บางตัวต่อผ่าน f-string — ตรวจแล้วใช้งานได้)

ขณะที่ parameter tree ใน blueprint มี ~1,550 รายการ (`03_MEGASTRUCTURE`, `02_`, `05_`) — VEX อ่านจริงแค่ 62 ค่า

### 1.4 ทุก part เป็นแค่ shell ที่ต่อ quad ด้วยมือ + ค่า hardcode
ค่าที่ควรมาจาก parm/กลีบ แต่ใส่ตายตัวใน VEX (ตัวอย่าง):
| ไฟล์ | Hardcode |
|---|---|
| `part02_hex_barrier.vfl` | `u_divs = 28`, `v_divs = 14` (โดม R 1,500 m → ช่องละ ~200 m) |
| `part05_stamen_pylons.vfl` | ฐานเสาที่ `Y = 120.0` ตายตัว; ring R = 220 m (blueprint `02_RADIAL_GRID_MATH` ระบุ R = 120 m รอบ receptacle) |
| `part07_outer_docks.vfl` | `startR = 1040.0` (ไม่ตามความยาวกลีบ) |
| `part12_ring_hydraulics.vfl` | `neckR = 80.0`, `seabedR = 350.0`, `tiers = 12` |
| `part14_bulkhead_gates.vfl` | `gateRadius = 165.0`, `channelW = 45.0`, `towerH = 38.0` |
| `part11/13/15` | segs/rings/tiers ตายตัวทั้งหมด |

ผลคือ **ปรับกลีบแล้ว part อื่นไม่ตาม** และวางไม่ตรงกัน

### 1.5 สวิตช์ "High-Res" หลอก + บั๊กแกน
- `useHighResParts` (ค่าเริ่มต้น ON) โหลด `output/parts/*.obj` ซึ่ง export จากสูตรเดียวกันที่ความละเอียดเท่าเดิม — ไม่ได้ high-res
- OBJ เหล่านี้เป็น **Z-up** แต่ Houdini เป็น Y-up → ทุก part ล้มตะแคง 90° (โดมกลายเป็นชาม, วงแหวนใต้น้ำกลายเป็นหอตั้งขึ้น) ขณะที่ชั้น CSV สลับแกนถูก → วางไม่ตรงกัน

### 1.6 Builder ลบฉากทุกครั้งที่รัน
`build_istrorigan_master.py` เรียก `old.destroy()` ทุกครั้ง → ค่าที่เจ้าของปรับใน .hip หายหมด (ขัดข้อ 0.1)

### 1.7 Spec ของเจ้าของถูกเขียนทับ (เทียบ git staged vs working tree)
ไฟล์ที่ parameter tree เดิมถูกลบแล้วแทนด้วย lore:
- `03_MEGASTRUCTURE/03_03_PETAL_SYSTEM.md` — ลบ `Petal_Thickness`, `Petal_Rotation`, `FC_Petal_Shore_Attach`, `FC_Petal_Center_Clearance`, `Target_Height`, `Transition_Progress`, `FC_Petal_Open/Close/State_Transition`, `Rig_Left/Right`, `Inner/Left/Right_Pivot`, `Raise/Lower/Twist_Amount`, `Rig_State`, `FC_Petal_Rig_Balance/Limit/Debug`
- `03_MEGASTRUCTURE/03_01_GLOBAL_STATE.md` — ลบกิ่งย่อยของ `FC_Flower_State_Distributor` (Structure / Protection / Operation / Trade / Submerge / Deep_Sea / Emergency พร้อม target ของแต่ละกิ่ง)
- `README.md`, `00_CORE_SETTINGS.md`, `03_05_STEM_AND_ROOT.md`, `03_02_CENTER_CORE/01_...` — เขียนหัวข้อ Purpose ใหม่
- ต้นฉบับยังอยู่ใน git commit แรก (baseline) ของ repo นี้ — ใช้ `git show <baseline>:<path>` ดูได้

### 1.8 ช่องโหว่ใน blueprint ที่ไม่มีใครรายงาน
- `01_DATA_TABLE_DISTRICT_ZONING.md`: ตาราง markdown มี 8 คณะ แต่ JSON มีแค่ **คณะ 0, 1, 4, 6** (ขาด 2, 3, 5, 7)
- `03_03_PETAL_SYSTEM.md`: `Petal_Width = 250 m` แต่โค้ด/ภาพใช้ 420 m — ที่ 420 m กลีบหุบได้แค่ ~10.5° ก่อนคลอง 45 m จะชน (spec ต้องการหุบถึง 60°) → **รอเจ้าของตัดสิน**
- ไม่มีทะเล/ผิวน้ำในกราฟ Houdini เลย

---

## 2. สิ่งที่แก้แล้ว (Claude, 2026-09-26) — ยัง **ไม่เคยรันใน Houdini จริง**

ทุกข้อด้านล่างตรวจด้วย Python mirror (พอร์ต VEX บรรทัดต่อบรรทัด) เท่านั้น **ต้องรันใน Houdini เพื่อยืนยัน**

| งาน | ไฟล์ | สถานะ |
|---|---|---|
| Part 03 กลีบ ระดับ Lotus (55 parm, บาน/หุบที่ hinge, spine curve, jitter, override รายกลีบ, collision guard 3D, watertight) | `scripts/houdini/part03_academic_petals.py`, `vex/part03_academic_petals.vfl` | เขียนแล้ว |
| PCG Stage 0 — อ่าน zoning table จาก .md สดๆ | `pcg_blueprint_loader.py` | เขียนแล้ว |
| PCG Stage 1 — polar lattice บน deck กลีบจริง (4 m → 108k จุด, 2 m → 432k) | `vex/pcg_s1_polar_lattice.vfl` | เขียนแล้ว |
| PCG Stage 2 — zoning, district, density, 8 restrictions ตาม `03.02.01` | `vex/pcg_s2_zoning.vfl` | เขียนแล้ว |
| PCG Stage 3 — graph L1/L2/L3, ring bridges + Bridge_State, flood isolation, Dijkstra evac | `vex/pcg_s3_graph.vfl`, `vex/pcg_s3_evac.vfl` | เขียนแล้ว |
| อัปเดต .hip แบบไม่ทำลาย (เก็บค่า parm เดิม) | `update_in_place.py` | เขียนแล้ว |
| Builder ไม่ลบฉากเอง (ต้องส่ง `rebuild` เท่านั้น) | `build_istrorigan_master.py` | แก้แล้ว |
| OBJ Z-up → Y-up, `useHighResParts` default OFF | `build_istrorigan_master.py` | แก้แล้ว |

### Contract ระหว่าง stage (ห้ามเปลี่ยนชื่อโดยไม่อัปเดตทุกฝั่ง)
- Part 03 → detail arrays `pf_count, pf_ures, pf_rootR, pf_cup, pf_az[], pf_pitch[], pf_len[], pf_th[], pf_cr[], pf_cy[], pf_deckY[], pf_rimH[], pf_w[], pf_deckInset[]`
- Stage 0 → detail arrays `zone_name[], zone_type[], zone_tags[], zone_petal[], zone_tier[], zone_minR/maxR/minZ/maxZ[] (m), zone_maxBldH[], zone_falloff[], zone_from_json[]`
- Stage 1 → points `PetalIndex, RingTier, PetalU_Normalized, PetalV_Normalized, Elevation_Z, RadialDistance, AlongDistance, SpineDistance, EdgeDistance, N, lattice_id`
- Stage 2 → + `ZoneRow, DistrictType, DistrictID, ZoneTag, ZoneTags, MaxBuildingHeight_m, Density, Buildable, RestrictReason, BuildCandidate` + groups `buildable, build_candidate, promenade, transport_spine, emergency_access`
- Stage 3 → points `NodeID, NodeType, PetalIndex, bIsOperational, EvacDistance_m, EvacNextNode`; prims `Layer, EdgeType, EdgeID, start_node, end_node, Length_m, bIsOperational, BridgeState`

---

## 3. งานที่ยังค้าง (เรียงลำดับ)

1. **รัน `update_in_place.py` ใน Houdini** แก้ error VEX ถ้ามี — ห้ามทำงานต่อบนโค้ดที่ยังไม่เคย cook ผ่าน
2. **Stage 4 Socket Grammar** — วาง archetype จาก `02_DATA_TABLE_ASSET_ARCHETYPES` บน `build_candidate`, ตรวจ `03_DATA_TABLE_SOCKET_MATRIX`, clearance sweep
3. **Stage 5 Instancing** — instance points (`unreal_instance`, LOD/Nanite) แทน `py_buildings` / `py_scatter`
4. **ต่อ part อื่นอีก 13 ตัว** ให้อ่าน `pf_*` / parm ของ part อื่น แทนค่า hardcode ในข้อ 1.4 (bulkhead ที่ root, docks ที่ปลายกลีบจริง, stamen ตาม receptacle, สะพาน part06 ใช้ bridge curve จาก Stage 3)
5. **ทะเล / ผิวน้ำ** แบบ procedural
6. ต่อ state ที่เหลือ (`emergencyState`, `deepSeaMode`, `annualCycleState` ฯลฯ) และสีที่ไม่ได้ต่อ
7. รอเจ้าของตัดสิน: ความกว้างกลีบ 420 m vs 250 m, stamen ring 220 m vs 120 m, bridge Tier 3 ที่ 900 m (ช่องกว้าง ~448 m)

---

## 4. กฎบังคับสำหรับ agent ทุกตัว

1. **ห้ามเขียนทับหรือลบ parameter tree / ตารางใน blueprint** — เพิ่มได้เฉพาะหัวข้อใหม่ที่ติดป้ายชัดเจน ถ้าเห็นว่า spec ขัดกันเอง ให้ **รายงานเจ้าของ** ไม่ใช่แก้เอง
2. **ห้ามใช้ข้อมูล bake (CSV/JSON/OBJ ที่สร้างนอก Houdini) เป็นแหล่ง geometry ของ HDA** — ทุกชั้นต้อง cook จาก parm ใน network ได้ (อ่าน blueprint .md ตอน cook ได้ เพราะเป็น source of truth)
3. **ทุก spare parm ต้องมี node อ่านจริง** — ก่อนส่งงาน ตรวจด้วยคำสั่งนี้ต้องไม่มี output ในส่วน "undefined" และต้องอธิบายทุก parm ที่ไม่ถูกอ่าน:
   ```bash
   cd scripts/houdini
   grep -ohE 'ch[ifvs]?\("%C%[A-Za-z0-9_]+' vex/*.vfl | sed 's/.*%C%//' | sort -u > /tmp/used.txt
   grep -rhoE '\b(F|I|B|COL|STR)\("[A-Za-z0-9_#]+"' *.py | sed -E 's/.*\("//;s/"//;s/#//' | sort -u > /tmp/defined.txt
   comm -23 /tmp/used.txt /tmp/defined.txt   # used but undefined  -> ต้องว่าง
   comm -13 /tmp/used.txt /tmp/defined.txt   # defined but unused  -> ต้องอธิบายได้ทุกตัว
   ```
4. **ห้าม hardcode ขนาด/ตำแหน่งที่มีอยู่แล้วเป็น parm หรือ contract** — อ่านจาก `pf_*` หรือ `ch()` ของ part ที่เกี่ยวข้อง
5. **ห้ามใส่ตัวเลขผลลัพธ์ลงใน label UI หรือใน spec** — ถ้าจะแสดงจำนวน ให้คำนวณจาก geometry (detail attrib)
6. **ห้ามรายงานว่า "เสร็จ" โดยไม่มีหลักฐานการ cook** — ต้องแนบ: จำนวน points/prims, detail attrib ตรวจสอบ (`min_clearance_m`, `lattice_count`, `evac_max_distance_m` ฯลฯ) และ error/warning ของ node ถ้าไม่มี Houdini ให้บอกตรงๆ ว่ายังไม่ได้รัน
7. **ห้ามทำลายฉากของเจ้าของ** — ใช้ `update_in_place.py` (หรือเพิ่ม step ในนั้น) ห้าม `destroy()` node ที่มีอยู่
8. **หน่วย**: Houdini = เมตร, Y-up · UE = เซนติเมตร, Z-up · blueprint DataTable = เซนติเมตร (loader แปลงเป็นเมตรแล้ว)
9. **VEX gotcha**: point ที่สร้างใน wrangle เดียวกัน **อ่านกลับด้วย `point()` ไม่ได้** — เก็บตำแหน่งไว้ใน array เอง
10. **ห้ามแก้ไฟล์พร้อมกับ agent อื่น** — ก่อนแก้ไฟล์ใด ดู `git status` / mtime; ทำงานบน branch ของตัวเอง แล้วให้เจ้าของ merge
