# 03.05 - Stem Rings, Telescopic Columns & Abyssal Roots

## Purpose & PCG Implementation
โครงสร้างส่วนล่างใต้ผิวน้ำของ Megastructure:
- **FC_Stem_Ring**: วงแหวนเสริมความแข็งแรงของลำต้นแกนดิ่ง
- **FC_Stem_Telescopic_System**: เสายืด-หดไฮดรอลิกสำหรับปรับระดับความสูงของเมืองเหนือน้ำ
- **FC_Stem_Transport**: ลิฟต์ดิ่งความเร็วสูงและท่อลำเลียงสู่ชั้นใต้ทะเล
- **FC_Ring_Connection & FC_Flower_Stem_Connection**: จุดถ่ายแรงและข้อต่อวงแหวน
- **FC_Root_System**: รากยึดพื้นสมุทร (Seabed Anchor Claws), ท่อดูดความร้อนใต้พิภพ, และระบบถ่วงน้ำหนัก (Ballast)

---

## Parameter Tree

```text
├─ 03.11_STEM_RING

│  │

│  ├─ FC_STEM_Ring

│  │  ├─ Ring_ID \[int\]

│  │  ├─ Ring_Count \[int\]

│  │  ├─ Ring_Radius

│  │  ├─ Ring_Height \[\>= 3m\]

│  │  ├─ Ring_Thickness

│  │  ├─ Extended_Z

│  │  ├─ Collapsed_Z

│  │  ├─ Collapse_Amount

│  │  ├─ Current_Depth

│  │  ├─ Pressure_Level

│  │  ├─ Hazard_Level

│  │  ├─ Occupancy_Allowed \[bool\]

│  │  ├─ Pressure_Rating

│  │  ├─ Emergency_Seal_State

│  │  ├─ Transport_Status

│  │  └─ City_Submerged_Mode \[bool\]

│  │

│  ├─ FC_STEM_Ring_Shell

│  ├─ FC_STEM_Ring_Floor

│  ├─ FC_STEM_Ring_Interior

│  ├─ FC_STEM_Ring_Service

│  └─ FC_STEM_Ring_Clearance

│

│

├─ 03.12_STEM_TELESCOPIC_SYSTEM

│  │

│  ├─ FC_STEM_Telescope

│  │  ├─ Deploy_Amount \[0–1\]

│  │  ├─ Ring_ID

│  │  ├─ Extended_Z

│  │  ├─ Collapsed_Z

│  │  ├─ Overlap

│  │  ├─ Clearance

│  │

│  ├─ FC_STEM_Ring_Order

│  ├─ FC_STEM_Ring_Nesting

│  ├─ FC_STEM_Ring_Stop

│  ├─ FC_STEM_Collapse_Limit

│  ├─ FC_STEM_Deploy_Limit

│  ├─ FC_STEM_Staged_Collapse

│  ├─ FC_STEM_Shock_Absorption

│  ├─ FC_STEM_Load_Distribution

│  ├─ FC_STEM_Descent_Control

│  └─ FC_STEM_Emergency_Stop

│

├─ 03.13_STEM_TRANSPORT

│  │

│  ├─ FC_STEM_Transport

│  ├─ FC_STEM_Walkway

│  ├─ FC_STEM_Vertical_Transport

│  ├─ FC_STEM_Service_Path

│  ├─ FC_STEM_Flower_Access

│  ├─ FC_STEM_Root_Access

│  ├─ FC_STEM_Pressure_Transition

│  ├─ FC_STEM_Pressure_Lock

│  ├─ FC_STEM_Emergency_Access

│  ├─ FC_STEM_Occupancy_Control

│  └─ FC_STEM_Depth_Restriction

│

│

├─ 03.14_RING_CONNECTION

│  │

│  ├─ FC_STEM_Ring_Connection

│  │  ├─ Connection_ID

│  │  ├─ Source_Ring_ID

│  │  ├─ Target_Ring_ID

│  │  ├─ Connected \[bool\]

│  │  ├─ Extend_Amount

│  │  └─ Lock_State

│  │

│  ├─ FC_Ring_Port

│  ├─ FC_Ring_Bridge

│  ├─ FC_Ring_Bridge_Extend

│  ├─ FC_Ring_Bridge_Retract

│  ├─ FC_Ring_Port_Align

│  ├─ FC_Ring_Port_Lock

│  ├─ FC_Ring_Port_Seal

│  └─ FC_Ring_Emergency_Disconnect

│

│

├─ 03.15_FLOWER_STEM_CONNECTION

│  ├─ FC_Flower_Stem_Port

│  ├─ FC_Flower_Stem_Transition

│  ├─ FC_Flower_Stem_Transport

│  ├─ FC_Flower_Stem_Structure

│  └─ FC_Flower_Stem_Seal

│

│

├─ 03.16_ROOT_SYSTEM

│  │

│  ├─ FC_Root

│  ├─ FC_Root_Core

│  ├─ FC_Root_Branch

│  ├─ FC_Root_Anchor

│  ├─ FC_Root_Energy_Storage

│  ├─ FC_Root_Power_Distribution

│  ├─ FC_Root_Logistics_Hub

│  ├─ FC_Root_Cargo_Transfer

│  ├─ FC_Root_Transport

│  ├─ FC_Root_Service

│  ├─ FC_Root_Maintenance

│  ├─ FC_Root_Emergency

│  ├─ FC_Root_Transition

│  └─ FC_Root_To_Stem

│

│
```
