# DT_Socket_Compatibility_Matrix - Hardware Snapping Rules

## Purpose
ตารางกฎเกณฑ์ความเข้ากันได้ของจุดเชื่อมต่อ (Socket Compatibility Matrix) สำหรับโมดูล PCG ทำหน้าที่ป้องกันไม่ให้โมดูลสุ่มวางข้ามประเภท เช่น ป้องกันไม่ให้นำท่อ Maglev ไปเชื่อมกับท่อสายไฟ หรือป้องกันไม่ให้ข้อต่อบานพับรับแรงบิดเกินกว่าที่คำนวณไว้

---

## 1. Compatibility Matrix Table

| Source Socket Type | Target Socket Type | Gender Requirement | Max Angular Deflection | Max Shear Tolerance (kN) | Watertight Seal Required | Default Clearance Extent (cm) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `Structural_Hinge` | `Structural_Hinge` | Male ↔ Female | $\pm 18^\circ$ (Pitch along Bloom axis) | 85,000 | No (Mechanical Hinge) | 400 x 400 x 600 |
| `Structural_Girder`| `Structural_Girder`| Bilateral ↔ Bilateral | $0^\circ$ (Strict Rigid) | 25,000 | No (Dry Lattice) | 250 x 250 x 300 |
| `Transit_Pedestrian`|`Transit_Pedestrian`| Bilateral ↔ Bilateral | $\pm 5^\circ$ (Flexible Accordion Seal)| 800 | Yes (Telescopic Gasket)| 200 x 200 x 300 |
| `Transit_Maglev` | `Transit_Maglev` | Bilateral ↔ Bilateral | $0^\circ$ (Strict Straight Line) | 6,500 | Yes (Vacuum Hermetic) | 300 x 300 x 400 |
| `Transit_Submersible`|`Transit_Submersible`| Male ↔ Female | $0^\circ$ (Double Ring Airlock) | 12,000 | Yes (Rated to 200 Bar) | 350 x 350 x 500 |
| `Utility_PowerGrid`| `Utility_PowerGrid`| Male ↔ Female | $\pm 45^\circ$ (Flexible Cable Loop) | 200 | Yes (Oil Insulated) | 150 x 150 x 150 |
| `Utility_LifeSupport`|`Utility_LifeSupport`| Male ↔ Female | $\pm 15^\circ$ (Bellows Joint) | 500 | Yes (Food-grade/O2 Seal)| 150 x 150 x 200 |
| `Facade_Mount` | `Facade_Mount` | Male ↔ Female | $0^\circ$ (Flush Mount) | 150 | No | 100 x 100 x 50 |
| `Pylon_ForceField` | `Pylon_ForceField` | Bilateral ↔ Bilateral | Line-of-Sight ($\pm 90^\circ$ Sector) | N/A (Projected Emitter)| N/A | 500 x 500 x 1000 |

---

## 2. Unreal Engine 5 Import JSON (`DT_Socket_Compatibility_Matrix.json`)

```json
[
  {
    "Name": "RULE_STRUCT_HINGE",
    "SourceSocketType": "EFC_SocketType::Structural_Hinge",
    "TargetSocketType": "EFC_SocketType::Structural_Hinge",
    "bAllowSameGender": false,
    "MaxAngularTolerance_Deg": 18.0,
    "MaxShearTolerance_kN": 85000.0,
    "bRequiresWatertightSeal": false
  },
  {
    "Name": "RULE_STRUCT_GIRDER",
    "SourceSocketType": "EFC_SocketType::Structural_Girder",
    "TargetSocketType": "EFC_SocketType::Structural_Girder",
    "bAllowSameGender": true,
    "MaxAngularTolerance_Deg": 0.0,
    "MaxShearTolerance_kN": 25000.0,
    "bRequiresWatertightSeal": false
  },
  {
    "Name": "RULE_TRANSIT_PEDESTRIAN",
    "SourceSocketType": "EFC_SocketType::Transit_Pedestrian",
    "TargetSocketType": "EFC_SocketType::Transit_Pedestrian",
    "bAllowSameGender": true,
    "MaxAngularTolerance_Deg": 5.0,
    "MaxShearTolerance_kN": 800.0,
    "bRequiresWatertightSeal": true
  },
  {
    "Name": "RULE_TRANSIT_MAGLEV",
    "SourceSocketType": "EFC_SocketType::Transit_Maglev",
    "TargetSocketType": "EFC_SocketType::Transit_Maglev",
    "bAllowSameGender": true,
    "MaxAngularTolerance_Deg": 0.0,
    "MaxShearTolerance_kN": 6500.0,
    "bRequiresWatertightSeal": true
  },
  {
    "Name": "RULE_TRANSIT_SUBMERSIBLE",
    "SourceSocketType": "EFC_SocketType::Transit_Submersible",
    "TargetSocketType": "EFC_SocketType::Transit_Submersible",
    "bAllowSameGender": false,
    "MaxAngularTolerance_Deg": 0.0,
    "MaxShearTolerance_kN": 12000.0,
    "bRequiresWatertightSeal": true
  },
  {
    "Name": "RULE_UTILITY_POWER",
    "SourceSocketType": "EFC_SocketType::Utility_PowerGrid",
    "TargetSocketType": "EFC_SocketType::Utility_PowerGrid",
    "bAllowSameGender": false,
    "MaxAngularTolerance_Deg": 45.0,
    "MaxShearTolerance_kN": 200.0,
    "bRequiresWatertightSeal": true
  },
  {
    "Name": "RULE_UTILITY_LIFESUPPORT",
    "SourceSocketType": "EFC_SocketType::Utility_LifeSupport",
    "TargetSocketType": "EFC_SocketType::Utility_LifeSupport",
    "bAllowSameGender": false,
    "MaxAngularTolerance_Deg": 15.0,
    "MaxShearTolerance_kN": 500.0,
    "bRequiresWatertightSeal": true
  }
]
```
