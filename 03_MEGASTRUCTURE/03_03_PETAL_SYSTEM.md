# 03.03 - Istrorigan 8-Petal Academic System & Mechanics

## World Canon & Purpose (Era: 4205)
ระบบกลีบเมืองทั้ง 8 ของมหานคร **ISTRORIGAN** ถูกออกแบบให้เป็น **8 วิทยาเขตมหาวิทยาลัยชั้นนำ (8 Grand Academic Faculties)** สำหรับ 17 มหารัฐ:
- **8 Distinct Independent Petals**: กลีบทั้ง 8 แยกขาดจากกันโดยสิ้นเชิง ไม่มีส่วนใดเกยหรือซ้อนทับกัน (Non-overlapping) คั่นด้วยร่องน้ำทะเลสีฟ้าใส (Canal Clearance กว้าง 45 เมตร) เพื่อให้แต่ละกลีบสามารถยกตัว พับเก็บ หรือบิดองศาได้อิสระโดยไม่เกิดการชนปะทะกัน (No Edge Collision)
- **Sub-Council Governance**: แต่ละกลีบมี **อาคารสภาย่อย (Faculty Sub-Council Hall)** คอยกำกับดูแลวิชาการและการจัดการทรัพยากรภายในกลีบ
- **Public & Academic Benefits**: พื้นที่ทั้งหมดอุทิศเพื่อสาธารณประโยชน์ ประกอบด้วยอัฒจันทร์บรรยายกลางแจ้ง (Open-Air Tiered Amphitheaters), โดมวิจัยพฤกษศาสตร์และชีววิทยาทางทะเล, หอสมุดสากล, และทางเดินศึกษาธรรมชาติ
- **Flat Surface Docks**: ปลายกลีบทอดราบแนบระดับผิวน้ำ ($Z = 0$) เป็นท่าเทียบเรือวิจัย เรือโดยสารสาธารณะ และแนวกั้นคลื่น

---

## 1. Parameter Tree

```text
03.03_PETAL_STRUCTURE

├─ FC_Istrorigan_8_Petals
│  ├─ Petal_Index [int: 0 to 7]
│  ├─ Petal_Count [int: 8 (Fixed Canon)]
│  ├─ Petal_Length [float: 85,000 cm]
│  ├─ Petal_Width [float: 25,000 cm]
│  ├─ Petal_Profile [Lotus Spoon-Curve (Cup & Keel)]
│  │
│  ├─ Petal_Clearance_Canal_Width [float: 4,500 cm (45m)]
│  ├─ Inter_Petal_Collision_Guard [bool: true]
│  ├─ Independent_Pitch_Angle [float: 0 to 60 deg]
│  │
│  ├─ FC_Petal_SubCouncil_Hall
│  │  ├─ SubCouncil_ID [int: 0 to 7]
│  │  ├─ Faculty_Specialization [string]
│  │  └─ Quorum_Status [bool]
│  │
│  ├─ FC_Petal_Public_Facilities
│  │  ├─ Academic_Amphitheater_Count [int: 1 per petal]
│  │  ├─ BioDome_Research_Clusters [int: 2 to 4 per petal]
│  │  ├─ Public_Campus_Promenade [bool: true]
│  │  └─ Spine_Maglev_Transit_Tube [bool: true]
│  │
│  ├─ FC_Petal_Inner_Attach (Heavy Hydraulic Hinge)
│  ├─ FC_Petal_Outer_Edge (Flat Sea Dock Berth)
│  ├─ FC_Petal_Left_Edge (Canal Margin)
│  └─ FC_Petal_Right_Edge (Canal Margin)

03.04_PETAL_STATE
├─ FC_Petal_State
│  ├─ Petal_ID [0 to 7]
│  ├─ Open_State [bool]
│  ├─ Open_Amount [float 0–1]
│  ├─ Submerge_Tuck_Pitch [float: 8.0 deg]
│  ├─ Emergency_Quarantine_Sealed [bool]
│  └─ Watertight_Bulkhead_Status [enum: Open, Warning, Hermetic_Sealed]

03.05_PETAL_RIG
├─ FC_Petal_Rig
│  ├─ Master_Hinge_Bone (Root Anchor to Center)
│  ├─ Spine_Deformation_Spline (Curvature Control)
│  ├─ Hydraulic_Piston_Dampers (Shock Absorption)
│  └─ Angular_Limit_Pitch_Max [65 deg]
```

---

## 2. แผนผังคณะของทั้ง 8 กลีบ (Faculty Allocation Matrix)

| Petal Index | ชื่อคณะประจำกลีบ (Faculty Name) | ฟังก์ชันหลักเพื่อสาธารณประโยชน์ | สิ่งปลูกสร้างเด่น |
| :---: | :--- | :--- | :--- |
| **Petal 0** | **Faculty of Oceanic & Geothermal Engineering** | วิจัยพลังงานสะอาดใต้สมุทรและวิศวกรรมโครงสร้าง | หอแปลงพลังงาน, สถาบันทดสอบไฮดรอลิก |
| **Petal 1** | **Faculty of Biosphere & Marine Biology** | ฟื้นฟูระบบนิเวศน์ทางทะเลและเกษตรไฮโดรโปนิกส์ | เมกะไบโอโดมกระจกใส, สถาบันเพาะเลี้ยงปะการัง |
| **Petal 2** | **Faculty of Geo-Atmospheric Science** | ควบคุมและพยากรณ์มรสุมโลกยุคหลังน้ำท่วม | หอดูดาวและสถานีตรวจวัดบรรยากาศเรดาร์ |
| **Petal 3** | **Faculty of Floating Megastructures** | วิจัยการสร้างและขยายเมืองลอยน้ำสำหรับมนุษยชาติ | สถาบันทดสอบการไหลวนของของไหล (Hydrodynamics Lab) |
| **Petal 4** | **Grand Universal Library & Pre-Deluge Archives** | หอจดหมายเหตุรวบรวมประวัติศาสตร์มนุษย์ก่อนน้ำท่วม | หอสมุดโดมกระจกยักษ์, อัฒจันทร์บรรยาย 5,000 ที่นั่ง |
| **Petal 5** | **Faculty of Deep-Sea Mining & Abyssal Exploration**| สำรวจร่องสมุทรมาเรียนาและทรัพยากรแร่ก้นทะเล | อู่ต่อเรือดำน้ำลึก, แท่นทดสอบแรงดันน้ำ 500 Bar |
| **Petal 6** | **17-State Parliamentary Assembly & Global Campus** | ศูนย์กลางการทูต การแลกเปลี่ยนวัฒนธรรม และหอพักนานาชาติ| สภาความร่วมมือ 17 รัฐ, ลานประชุมนานาชาติ |
| **Petal 7** | **Faculty of Oceanic Medicine & Genetics** | แพทยศาสตร์ทางทะเล การบำบัดรังสี และการปรับพันธุศาสตร์ | โรงพยาบาลกลางมหาสมุทร, สถาบันพันธุวิศวกรรม |
