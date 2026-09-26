# คู่มือการเตรียมโปรเจกต์สถาปัตยกรรม ISTRORIGAN ใน HOUDINI (Houdini Production Pipeline)

> **Era: 4205 | World of 17 Great States**  
> มหานครดอกบัว **ISTRORIGAN (อิสโตรริแกน)** — เอกสารแนวทางการขึ้นงานสถาปัตยกรรม Procedural และการประกอบ 9 ชิ้นส่วนหลักในโปรแกรม **SideFX Houdini** (SOPs, VEX & Solaris/USD)

---

## 1. ไฟล์ 3D OBJ โมดูลาร์แต่ละพาร์ท (Baked 3D Parts Directory)

ระบบได้ทำการสร้างและ Export โมเดล 3D แยกชิ้นส่วนอิสระทั้ง 9 พาร์ท พร้อมสเกลมาตรฐาน **DCC Meters (1 unit = 1m)** ไว้ในโฟลเดอร์ [output/parts/](../output/parts):

| No. | รหัสระบบ (System ID) | ชื่อไฟล์ 3D Geometry | จำนวนโพลีกอน | รายละเอียดสถาปัตยกรรมใน Houdini |
| :---: | :--- | :--- | :---: | :--- |
| **01** | `SYS_01_APEX_SPIRE` | [01_SYS_APEX_SPIRE.obj](../output/parts/01_SYS_APEX_SPIRE.obj) | 832 polys | หอคอยสภาสิบ (+600m), โครงสร้างยอดแหลม Fluted Spine และลาน Citadel Plaza (+120m) |
| **02** | `SYS_02_HEX_BARRIER` | [02_SYS_HEX_BARRIER.obj](../output/parts/02_SYS_HEX_BARRIER.obj) | 648 polys | โดมม่านพลังงานเรขาคณิตรังผึ้ง 6 เหลี่ยม (Hexagonal Grid), รัศมี 1,500m, สูง +650m |
| **03** | `SYS_03_ACADEMIC_PETALS` | [03_SYS_ACADEMIC_PETALS_8X.obj](../output/parts/03_SYS_ACADEMIC_PETALS_8X.obj)<br>[03_SYS_ACADEMIC_PETAL_SINGLE.obj](../output/parts/03_SYS_ACADEMIC_PETAL_SINGLE.obj) | 5,760 polys<br>(720/กลีบ) | 8 กลีบดอกบัวแยกเดี่ยว ทรงช้อน (Cupped Hull) พร้อมสันกระดูกงู (Keel), ร่องน้ำกว้าง 45m และปลายกลีบ Z=0m |
| **04** | `SYS_04_BIO_DOMES` | [04_SYS_BIO_DOMES.obj](../output/parts/04_SYS_BIO_DOMES.obj) | 1,024 polys | โดมชีววิทยา Geodesic 8 โดมประจำ 8 กลีบ (R=55m บนระนาบผิวกลีบ r=650m) |
| **05** | `SYS_05_STAMEN_PYLONS` | [05_SYS_STAMEN_PYLONS.obj](../output/parts/05_SYS_STAMEN_PYLONS.obj) | 3,360 polys | เสากระโดงพลังงานสีทอง 70 ต้นรอบ Citadel Plaza (ความสูงเสา 45m, รัศมี 180m-260m) |
| **06** | `SYS_06_CANAL_BRIDGES` | [06_SYS_CANAL_BRIDGES.obj](../output/parts/06_SYS_CANAL_BRIDGES.obj) | 80 polys | สะพานกระจกทรงโค้ง (Inter-Petal Skybridges) 8 จุด พาดข้ามร่องน้ำ 45m ระหว่างขอบกลีบ |
| **07** | `SYS_07_OUTER_DOCKS` | [07_SYS_OUTER_FLOATING_DOCK.obj](../output/parts/07_SYS_OUTER_FLOATING_DOCK.obj) | 240 polys | **ท่าเรือทุ่นลอยขนาดเล็ก นอกขอบกลีบ (ตาม Canon LOTUS_ACADEMY_CITY.jpg)** พร้อมทางลาดพับเก็บได้ |
| **08** | `SYS_08_STEM_RINGS` | [08_SYS_STEM_RINGS.obj](../output/parts/08_SYS_STEM_RINGS.obj) | 384 polys | วงแหวนถังอับเฉายืดหด 12 ชั้นใต้น้ำ ขยายรัศมีจาก 80m สู่ 350m (ระดับความลึก -50m ถึง -900m) |
| **09** | `SYS_09_SEABED_VAULT` | [09_SYS_SEABED_VAULT.obj](../output/parts/09_SYS_SEABED_VAULT.obj) | 24 polys | บังเกอร์คลังความรู้ Doomsday Vault ก้นสมุทร (-1,000m) และก้ามปูไททาเนียมยึดตรึงพื้นหิน 4 ทิศ |

---

## 2. วิธีการรันตัวสร้างเครือข่ายโหนดใน Houdini อัตโนมัติ (Automated Houdini Network Builder)

สคริปต์ [scripts/houdini_modular_parts_builder.py](../scripts/houdini_modular_parts_builder.py) จะสร้างโครงสร้างเครือข่าย `/obj/ISTRORIGAN_MASTER` ภายใน Houdini ให้โดยอัตโนมัติ

### วิธีใช้งานใน Houdini:
1. เปิดโปรแกรม Houdini (Houdini 19.5, 20.0, 20.5 หรือสูงกว่า)
2. ไปที่เมนูด้านบน: **Windows > Python Source Editor** (หรือเปิดแท็บ **Python Shell**)
3. คัดลอกโค้ดจาก [scripts/houdini_modular_parts_builder.py](../scripts/houdini_modular_parts_builder.py) ไปวาง แล้วกด **Apply / Run**
4. หรือรันผ่าน Terminal/Command Prompt ด้วยคำสั่ง:
   ```bash
   hython <project>/scripts/houdini_modular_parts_builder.py
   ```

### สิ่งที่ถูกสร้างขึ้นใน `/obj`:
```
/obj/ISTRORIGAN_MASTER/
├── [Subnet] PART_01_APEX_SPIRE       (หอคอยสภาสิบ +600m)
├── [Subnet] PART_02_HEX_BARRIER      (ม่านบาเรียรังผึ้ง)
├── [Subnet] PART_03_ACADEMIC_PETALS  (8 กลีบดอกบัว)
├── [Subnet] PART_04_BIO_DOMES        (โดมชีววิจัย)
├── [Subnet] PART_05_STAMEN_PYLONS    (เสาสนามพลัง 70 ต้น)
├── [Subnet] PART_06_CANAL_BRIDGES    (สะพานลอยข้ามร่องน้ำ)
├── [Subnet] PART_07_OUTER_DOCKS      (ท่าเรือทุ่นลอยนอกกลีบ)
├── [Subnet] PART_08_STEM_RINGS       (วงแหวนยืดหด 12 ชั้น)
├── [Subnet] PART_09_SEABED_VAULT     (คลังความรู้ก้นสมุทร)
├── [Merge]  MERGE_ALL_PARTS
├── [Xform]  MASTER_SCALE_XFORM
└── [Null]   OUT_ISTRORIGAN_FINAL     <-- โหนดปลายทางสำหรับแสดงผลหรือ Render
```

---

## 3. แผงควบคุมมาสเตอร์บน Houdini UI (Master Controls)

โหนด `/obj/ISTRORIGAN_MASTER` มีพารามิเตอร์ที่ Promoted ออกมาให้ปรับแต่งได้ทันที:

- **Master Transforms**:
  - `Global Scale`: สเกลรวมของเมือง (Default: `1.0`)
  - `Petal Pitch Angle (deg)`: องศายกของกลีบดอกบัว (`0.0° - 45.0°`)
  - `Submerged Dive Mode`: เปิด/ปิดโหมดดำน้ำหนีพายุ
  - `Hex Barrier Energy`: ควบคุมความสว่าง/ความทึบของม่านบาเรีย (`0.30 - 1.00`)
- **Parts Visibility (Solo / Hide)**:
  - สวิตช์ Checkbox เปิด/ปิดการแสดงผลของแต่ละพาร์ทแยกกันได้ทั้ง 9 พาร์ท

---

## 4. คลังโค้ด VEX สำหรับการสร้างแบบ Procedural ใน Houdini (VEX Library)

สำหรับงานที่ต้องการดัดแปลงรูปทรงหรือ Scatter จุดบนพื้นผิวแบบ Real-time:

- **สูตรคณิตศาสตร์กลีบดอกบัวและช่องว่าง 45m**: [scripts/vex/petal_polar_lattice.vfl](../scripts/vex/petal_polar_lattice.vfl)
  - นำไปวางในโหนด **Attribute Wrangle (Points)**
  - มีการคำนวณระยะ Clear ร่องน้ำ 45m อัตโนมัติ:
    ```c
    float max_permitted_half_w = (r_dist * sin(M_PI / 8.0)) - (min_clearance * 0.5);
    ```
- **สูตรจัดวางเสาพลังงาน 70 ต้น, ท่าเรือทุ่นลอย และวงแหวน 12 ชั้น**: [scripts/vex/stamen_and_dock_generators.vfl](../scripts/vex/stamen_and_dock_generators.vfl)

---

## 5. การส่งต่อเข้าสู่ Solaris (USD / Karma) & Unreal Engine 5

- **Solaris / Karma LOPs**: 
  - ใช้โหนด `SOP Import` หรือ `Sublayer` ชี้ตรงไปยังไฟล์ `.obj` ใน `output/parts/`
  - แต่ละชิ้นส่วนมีแอตทริบิวต์ `s@part_id` ฝังไว้ในตัว geometry เพื่อนำไปแมป MaterialX (เช่น Glass สำหรับ Bio-Dome, Gold Brushed Metal สำหรับ Stamen, White Carbon Composite สำหรับ Petal Hull)
- **Unreal Engine 5 LiveLink / FBX**:
  - หากต้องการส่งออกเข้า UE5 เป็น Nanite Meshes ให้ต่อโหนด `ROP FBX Output` จากแต่ละ Subnet เข้าสู่ Content Browser ของ Unreal Engine
