# 04.01 - PCG Generation Pipeline Architecture

## Purpose
พิมพ์เขียวลำดับการประมวลผลของ PCG Graph (5-Stage Generation Workflow) สำหรับ Unreal Engine 5 PCG Framework หรือ Houdini Engine

---

## ลำดับการ Generate 5 ขั้นตอน (5-Stage Pipeline)

```mermaid
flowchart LR
    S1[Stage 1: Polar Lattice] --> S2[Stage 2: Zoning & Filtering]
    S2 --> S3[Stage 3: Graph & Splines]
    S3 --> S4[Stage 4: Socket Grammar]
    S4 --> S5[Stage 5: Instancing & Culling]
```

### Stage 1: Mathematical Lattice & Polar Grid
1. อ่านค่าจาก `00_CORE/00_CORE_SETTINGS.md` (`Global_Master_Seed`, `Max_Petal_Count`, `World_Scale_Factor`)
2. สร้างจุด Point Cloud ในพิกัดโพลาร์ $(r, 	heta, z)$ ตามสมการของกลีบดอกไม้
3. บันทึก Attributes ลงใน Point:
   - `PetalIndex` $(0 dots N-1)$
   - `RingTier` $(0 dots 4)$
   - `PetalU_Normalized` $(0.0 dots 1.0)$
   - `PetalV_Normalized` $(-1.0 dots +1.0)$
   - `Elevation_Z`

### Stage 2: Spatial Partitioning & District Zoning
1. กรองจุดด้วยตาราง Zoning Rules จาก `00_CORE/00_PCG_DATA_CONTRACTS.md`
2. กำหนด Tag ให้แต่ละ Point: เช่น `Zone.Core`, `Zone.Petal.Mid`, `Zone.Stem`
3. ลบจุดที่อยู่ในเขตห้ามสร้าง (`FC_Center_Building_Restriction` จาก `03.02.01`)

### Stage 3: Topological Waypoint Graph & Spline Routing
1. สร้างโครงข่ายการเดินทาง (Petal Transit Graph) เชื่อมต่อจาก Core สู่ Petal Tips
2. วาง Spline ทางเดินหลัก, รางรถไฟ Maglev, และท่อลำเลียง Utility บนสันกลีบ (`PetalV == 0.0`)
3. วาง Spline วงแหวนเชื่อมระหว่างกลีบ (Inter-Petal Connecting Bridges)

### Stage 4: Socket Grammar & Prefab Fitting
1. วางโมดูลโครงสร้างหลัก (Anchor Structures / Primary Girders)
2. ค้นหา Socket ที่เปิดอยู่ (`bIsOccupied == false`)
3. คำนวณความเข้ากันได้ตาม `FFC_SocketCompatibilityMatrix`
4. สุ่มเลือก Module Archetype ตาม `FFC_ModuleSpawnRule` (คำนวณตามความลึกและระยะรัศมี)
5. ทำ Clearance Sweep Box เพื่อป้องกันการวางทับซ้อน

### Stage 5: Instanced Static Mesh Spawning & Performance
1. ยุบรวมโมดูลที่เป็น Static Mesh ซ้ำๆ ลงใน **HISM (Hierarchical Instanced Static Mesh)**
2. ตั้งค่า Nanite Enable, Distance Culling และ LOD Bias ตามระดับความสำคัญของโมดูล
3. ผูก Metadata กลับไปยัง `FC_PCG_Runtime_State_Adapter`
