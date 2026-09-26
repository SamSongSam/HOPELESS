# 04_UE5_PCG_GRAPH_SETUP_GUIDE - Unreal Engine 5 Implementation

## Purpose & Prerequisites
คู่มือแนะนำการประกอบโหนดจริงใน **Unreal Engine 5 (UE 5.2 – 5.5)** โดยใช้ระบบ **PCG (Procedural Content Generation Framework)** พร้อมการเชื่อมต่อ C++ Data Tables และ Subgraphs

### Plugins ที่จำเป็น (Enable ใน `.uproject`):
1. **Procedural Content Generation Framework (PCG)**: Core PCG Graph system
2. **PCG Geometry Script Interop**: สำหรับสร้าง Splines และ Mesh Booleans แบบ Dynamic
3. **Gameplay Tags**: สำหรับ Socket & Compatibility Tag Queries

---

## 1. ผังโครงสร้าง Subgraph หลักใน PCG Graph

```
[Master PCG Graph: PCG_FlowerCity_Master]
  │
  ├─► [Subgraph: PCG_Sub_PolarLattice]
  │     └─ สร้าง Point Cloud ตามพิกัดกลีบดอกไม้ (u, v, r, theta, Z)
  │
  ├─► [Subgraph: PCG_Sub_DistrictZoning]
  │     └─ อ่าน DT_District_Zoning กรองแบ่งกลุ่ม Points ตาม RingTier และรัศมี
  │
  ├─► [Subgraph: PCG_Sub_SpineSplines]
  │     └─ ดึงจุดสันกลีบ (v = 0.0) แปลงเป็น Spline สำหรับวางราง Maglev และท่อหลัก
  │
  ├─► [Subgraph: PCG_Sub_ModulePlacement]
  │     └─ คำนวณ Socket Grammar, ตรวจสอบ Clearance Box, สุ่มเลือกโมดูลตาม Weight Curve
  │
  └─► [Subgraph: PCG_Sub_MeshSpawning]
        └─ Spawn ชิ้นส่วนลงใน Hierarchical Instanced Static Mesh (HISM)
```

---

## 2. ขั้นตอนการตั้งค่าในแต่ละ Subgraph

### 2.1 Subgraph 1: `PCG_Sub_PolarLattice`
1. เพิ่มโหนด **Custom Blueprint Element** ที่สืบทอดจาก `UPCGBlueprintElement` (ชื่อ `PCG_GeneratePetalLattice`)
2. ใส่ Input Parameters:
   - `PetalCount` (`int32` = 6)
   - `CoreRadius` (`float` = 15000.0)
   - `PetalLength` (`float` = 85000.0)
   - `MaxWidth` (`float` = 25000.0)
   - `OpenAmount` (`float` ดึงมาจาก Actor Blueprint)
3. รันสมการตามที่ระบุใน [02_RADIAL_GRID_MATH.md](../01_WORLD/02_RADIAL_GRID_MATH.md)
4. สั่ง **Add Attribute** ให้กับ Point Data:
   - `PetalIndex` (`int32`)
   - `PetalU` (`float`)
   - `PetalV` (`float`)
   - `Elevation_Z` (`float`)

### 2.2 Subgraph 2: `PCG_Sub_DistrictZoning`
1. ลากโหนด **Point Filter** หรือ **Attribute Filter**:
   - กรอง `PetalU <= 0.05` $\rightarrow$ ส่งต่อไปยังกลุ่ม `Zone.Core`
   - กรอง `0.05 < PetalU <= 0.25` $\rightarrow$ ส่งต่อไปยังกลุ่ม `Zone.Petal.Inner`
   - กรอง `0.25 < PetalU <= 0.70` $\rightarrow$ ส่งต่อไปยังกลุ่ม `Zone.Petal.Mid`
   - กรอง `0.70 < PetalU <= 1.00` $\rightarrow$ ส่งต่อไปยังกลุ่ม `Zone.Petal.Tip`
2. ใช้โหนด **Metadata Operation**:
   - เขียน GameplayTag ลงในแอตทริบิวต์ `@ZoneTag` ประจำจุด

### 2.3 Subgraph 3: `PCG_Sub_SpineSplines`
1. ใช้โหนด **Point Filter** คัดเลือกเฉพาะจุดที่ `abs(PetalV) < 0.05` (จุดที่อยู่บนสันกลางกลีบ)
2. เชื่อมเข้าโหนด **Create Spline from Points**:
   - เรียงลำดับจุดตามค่า `PetalU` จากน้อยไปมาก
   - จะได้ Spline เส้นทางหลัก 6 เส้นสำหรับ 6 กลีบ
3. เชื่อม Spline เข้ากับ **Spline Sampler**:
   - ระยะสุ่มตัวอย่าง $40\text{ m} = 4000\text{ cm}$
   - วางโมดูลราง `ARCH_TRANS_MAGLEV_TUBE` ตลอดเส้นทาง

### 2.4 Subgraph 4: `PCG_Sub_ModulePlacement`
1. ลากโหนด **Density Filter** ควบคู่กับโหนด **Random Seed Stream**:
   - กำหนด Seed แยกตาม `PetalIndex` โดยใช้สูตร: `MurmurHash3(MasterSeed, PetalIndex)`
2. อ่านข้อมูลจาก `DT_Asset_Archetypes`:
   - คำนวณ Weight สุทธิ: $\text{Weight} = \text{BaseWeight} \times \text{DepthWeightCurve}(Z) \times \text{RadialWeightCurve}(U)$
   - เลือกโมดูลด้วยโหนด **Weighted Random Sampler**
3. ป้องกันการชนกัน (Collision Clearance):
   - เพิ่มโหนด **Difference** หรือ **Self Pruning** โดยใช้ขนาด Clearance Box ของโมดูล

### 2.5 Subgraph 5: `PCG_Sub_MeshSpawning`
1. เชื่อมจุดสุดท้ายเข้าสู่โหนด **Static Mesh Spawner**
2. ภายใต้ Mesh Selector เลือก **PCG Mesh Selector Weighted**
3. กำหนดโหมดเป็น **Hierarchical Instanced Static Mesh (HISM)**:
   - ติ๊กถูกที่ `Enable Nanite`
   - ตั้งค่า `Cull Distance` = 300,000 cm (3 km) สำหรับโมดูลขนาดเล็ก
   - ตั้งค่า `Cull Distance` = 0 (No Culling) สำหรับแกนกลางและโครงสร้างหลัก

---

## 3. การเชื่อมต่อ Actor Blueprint กับ Runtime State

สร้าง Actor Blueprint ชื่อ `BP_FlowerCityMasterActor`:
1. Add Component: `PCGComponent`
2. Add Variables:
   - `Global_Master_Seed` (`int64`)
   - `Submerge_Amount` (`float` 0.0 – 1.0)
   - `Emergency_State` (`bool`)
3. ใน Event Graph:
   - เมื่อค่า `Submerge_Amount` เปลี่ยน $\rightarrow$ สั่ง **Update Material Parameter Collection** และสั่ง Event ไปยัง `FC_PCG_Runtime_State_Adapter` โดยตรง **โดยไม่ต้องเรียก `Generate()` ซ้ำ** เพื่อประสิทธิภาพสูงสุดในเกมจริง (60+ FPS)
