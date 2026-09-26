# 03.06 - Megastructure Protection, Clearance & Collision Limits

## Purpose & PCG Implementation
การกำหนดระยะความปลอดภัยและโครงข่ายป้องกันภัยภาพรวม:
- **FC_Protection_Network**: วงแหวนเสาป้องกันรอบนอกและโดมสนามพลัง
- **FC_Structure_Debug**: ระบบ Visualize ตรวจสอบการทับซ้อนของโครงสร้าง
- **FC_Structure_Clearance**: ปริมาตรระยะปลอดภัยขั้นต่ำ (Safety Margin Volumes) ระหว่างชิ้นส่วนที่เคลื่อนไหวได้

---

## Parameter Tree

### Protection Network (03.10)
```text
├─ 03.10_PROTECTION_NETWORK

│

│  ├─ FC_Protection_Network

│  │  ├─ Protection_State

│  │  ├─ Coverage

│  │  ├─ Strength

│  │  ├─ Network_ID

│  │  └─ Emergency_Mode

│

│  ├─ FC_Protection_Pylon

│  │  ├─ Pylon_ID

│  │  ├─ Zone_ID

│  │  ├─ Position

│  │  ├─ Radius

│  │  ├─ Strength

│  │  └─ Active \[bool\]

│

│  ├─ FC_Protection_Field

│  ├─ FC_Field_Coverage

│  ├─ FC_Field_Overlap

│  ├─ FC_Field_Gap_Detection

│  ├─ FC_Protection_Control_Center

│  ├─ FC_Protection_State

│  ├─ FC_Protection_Failure

│  └─ FC_Protection_Debug

│

│

│
```

### Structure Debug & Clearance (03.17 - 03.18)
```text
├─ 03.17_STRUCTURE_DEBUG

│  │

│  ├─ FC_Debug_Petal_ID

│  ├─ FC_Debug_Zone

│  ├─ FC_Debug_Rig

│  ├─ FC_Debug_Shore_Connection

│  ├─ FC_Debug_Ring_ID

│  ├─ FC_Debug_Ring_Clearance

│  ├─ FC_Debug_Port

│  └─ FC_Debug_State

│

├─ 03.18_STRUCTURE_CLEARANCE

│  │

│  ├─ FC_Petal_Rig_Clearance

│  ├─ FC_Petal_To_Petal_Clearance

│  ├─ FC_Petal_To_Center_Clearance

│  ├─ FC_Protection_Field_Clearance

│  ├─ FC_Shore_Clearance

│  ├─ FC_Ring_Nesting_Clearance

│  ├─ FC_Ring_Port_Clearance

│  ├─ FC_Transport_Clearance

│  ├─ FC_Building_To_Center_Clearance

│  ├─ FC_Building_Petal_Close_Clearance

│  ├─ FC_Shore_Docking_Clearance

│  ├─ FC_Protection_Pylon_Clearance

│  ├─ FC_STEM_Pressure_Lock_Clearance

│  └─ FC_Root_Stem_Clearance

│

│
```
