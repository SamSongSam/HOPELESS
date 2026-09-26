# 03.02.07 - Center Coupling: To Petal & To Stem

## Purpose & PCG Implementation
ส่วนต่อประสานเชิงกล, งานโครงสร้าง, และระบบขนส่งข้ามรอยต่อระหว่าง:
1. **Center to Petal**: โครงสร้างข้อต่อบานพับ, การถ่ายน้ำหนัก, ท่อสาธารณูปโภคยืดหยุ่น, Clearance การบิดงอ, และระบบตัดตอนแยกกลีบ (`FC_Center_To_Petal`)
2. **Center to Stem**: เสารับน้ำหนักแกนดิ่ง, ระบบ Telescopic ยืด-หด, ปลอกผนึกแรงดันน้ำลึก, ท่อลิฟต์ดิ่งสู่ก้นทะเล, และการตัดตอนฉุกเฉิน (`FC_Center_To_Stem`)

---

## Parameter Tree

```text
│  ├─ FC_Center_To_Petal

│  │  ├─ Petal_ID

│  │  ├─ Connection_ID

│  │  ├─ Connection_Point

│  │  ├─ Connection_Transform

│  │  ├─ Connection_Local_Space

│  │  ├─ Connection_State

│  │  ├─ Connection_Enabled \[bool\]

│  │  ├─ Connection_Clearance

│  │  ├─ Structural_Interface

│  │  ├─ Rig_Interface

│  │  ├─ Transport_Interface

│  │  ├─ Utility_Interface

│  │  ├─ Service_Interface

│  │  ├─ Data_Interface

│  │  ├─ Power_Interface

│  │  └─ Emergency_Interface

│  │

│  ├─ FC_Center_To_Petal_Structure

│  │  ├─ Structural_Attach_Point

│  │  ├─ Structural_Load_Input

│  │  ├─ Structural_Load_Output

│  │  ├─ Load_Transfer

│  │  ├─ Load_Limit

│  │  ├─ Support_State

│  │  └─ Structural_Valid \[bool\]

│  │

│  ├─ FC_Center_To_Petal_Rig

│  │  ├─ Petal_Root

│  │  ├─ Inner_Pivot

│  │  ├─ Left_Rig_Link

│  │  ├─ Right_Rig_Link

│  │  ├─ Rest_Transform

│  │  ├─ Open_Transform

│  │  ├─ Closed_Transform

│  │  ├─ Current_Transform

│  │  ├─ Rig_State

│  │  └─ Rig_Valid \[bool\]

│  │

│  ├─ FC_Center_To_Petal_Transport

│  │  ├─ Transport_Connection_ID

│  │  ├─ Petal_Route_ID

│  │  ├─ Center_Route_ID

│  │  ├─ Entry_Point

│  │  ├─ Exit_Point

│  │  ├─ Transfer_Point

│  │  ├─ Transport_Mode

│  │  ├─ Articulated_Joint

│  │  ├─ Magnetic_Connection

│  │  ├─ Route_Continuity

│  │  ├─ Transport_State

│  │  └─ Transport_Valid \[bool\]

│  │

│  ├─ FC_Center_To_Petal_Utility

│  │  ├─ Utility_Connection_ID

│  │  ├─ Power_Link

│  │  ├─ Data_Link

│  │  ├─ Fluid_Link

│  │  ├─ Environmental_Link

│  │  ├─ Service_Link

│  │  ├─ Utility_Capacity

│  │  ├─ Utility_Load

│  │  ├─ Utility_Isolation

│  │  ├─ Utility_State

│  │  └─ Utility_Valid \[bool\]

│  │

│  ├─ FC_Center_To_Petal_State

│  │  ├─ Petal_State

│  │  ├─ Center_State

│  │  ├─ Open_State

│  │  ├─ Close_State

│  │  ├─ Submerge_State

│  │  ├─ Emergency_State

│  │  ├─ Transition_Progress \[float 0–1\]

│  │  └─ Interface_State_Valid \[bool\]

│  │

│  ├─ FC_Center_To_Petal_Clearance

│  │  ├─ Structural_Clearance

│  │  ├─ Rig_Clearance

│  │  ├─ Transport_Clearance

│  │  ├─ Utility_Clearance

│  │  ├─ Open_State_Clearance

│  │  ├─ Transition_Clearance

│  │  ├─ Closed_State_Clearance

│  │  └─ Clearance_Valid \[bool\]

│  │

│  ├─ FC_Center_To_Petal_Isolation

│  │  ├─ Isolate_Power \[bool\]

│  │  ├─ Isolate_Data \[bool\]

│  │  ├─ Isolate_Fluid \[bool\]

│  │  ├─ Isolate_Transport \[bool\]

│  │  ├─ Isolate_Service \[bool\]

│  │  ├─ Emergency_Isolation \[bool\]

│  │  ├─ Reconnect_Allowed \[bool\]

│  │  └─ Isolation_State

│  │

│  └─ FC_Center_To_Petal_Debug

│     ├─ Show_Connection_Point

│     ├─ Show_Load_Path

│     ├─ Show_Rig_Link

│     ├─ Show_Transport_Link

│     ├─ Show_Utility_Link

│     ├─ Show_Clearance

│     └─ Show_Interface_State

│

│  └─ FC_Center_To_Stem

│     ├─ Stem_ID

│     ├─ Stem_Root

│     ├─ Connection_ID

│     ├─ Connection_Point

│     ├─ Connection_Transform

│     ├─ Connection_Local_Space

│     ├─ Connection_State

│     ├─ Connection_Enabled \[bool\]

│     ├─ Structural_Interface

│     ├─ Transport_Interface

│     ├─ Utility_Interface

│     ├─ Service_Interface

│     ├─ Data_Interface

│     ├─ Power_Interface

│     ├─ Load_Transfer_Interface

│     ├─ Pressure_Interface

│     └─ Emergency_Interface

│

│     ├─ FC_Center_To_Stem_Structure

│     │  ├─ Structural_Attach_Point

│     │  ├─ Center_Load_Input

│     │  ├─ Stem_Load_Output

│     │  ├─ Load_Transfer

│     │  ├─ Load_Distribution

│     │  ├─ Load_Balance

│     │  ├─ Load_Limit

│     │  ├─ Structural_Alignment

│     │  ├─ Structural_State

│     │  └─ Structural_Valid \[bool\]

│

│     ├─ FC_Center_To_Stem_Transport

│     │  ├─ Transport_Connection_ID

│     │  ├─ Center_Route_ID

│     │  ├─ Stem_Route_ID

│     │  ├─ Entry_Point

│     │  ├─ Exit_Point

│     │  ├─ Transfer_Point

│     │  ├─ Hyperlink_Link

│     │  ├─ Lift_Link

│     │  ├─ Vertical_Transfer

│     │  ├─ Route_Continuity

│     │  ├─ Transport_State

│     │  └─ Transport_Valid \[bool\]

│

│     ├─ FC_Center_To_Stem_Utility

│     │  ├─ Utility_Connection_ID

│     │  ├─ Power_Link

│     │  ├─ Data_Link

│     │  ├─ Fluid_Link

│     │  ├─ Environmental_Link

│     │  ├─ Service_Link

│     │  ├─ Utility_Capacity

│     │  ├─ Utility_Load

│     │  ├─ Utility_Isolation

│     │  ├─ Utility_State

│     │  └─ Utility_Valid \[bool\]

│

│     ├─ FC_Center_To_Stem_Load_Transfer

│     │  ├─ Load_Source_ID

│     │  ├─ Load_Target_ID

│     │  ├─ Vertical_Load

│     │  ├─ Radial_Load

│     │  ├─ Torsion_Load

│     │  ├─ Dynamic_Load

│     │  ├─ Shock_Load

│     │  ├─ Current_Load

│     │  ├─ Load_Capacity

│     │  ├─ Load_Margin

│     │  ├─ Load_Transfer_State

│     │  └─ Load_Valid \[bool\]

│

│     ├─ FC_Center_To_Stem_Pressure

│     │  ├─ Pressure_Interface_ID

│     │  ├─ Center_Pressure

│     │  ├─ Stem_Pressure

│     │  ├─ Pressure_Difference

│     │  ├─ Pressure_Transition

│     │  ├─ Pressure_Lock

│     │  ├─ Pressure_Seal

│     │  ├─ Pressure_Isolation

│     │  ├─ Pressure_State

│     │  └─ Pressure_Valid \[bool\]

│

│     ├─ FC_Center_To_Stem_Telescopic_Interface

│     │  ├─ Stem_Deploy_Value

│     │  ├─ Stem_Collapse_Value

│     │  ├─ Stem_Current_Height

│     │  ├─ Stem_Extended_Height

│     │  ├─ Stem_Collapsed_Height

│     │  ├─ Collapse_Rate

│     │  ├─ Shock_Damping_Value

│     │  ├─ Descent_State

│     │  └─ Telescopic_State_Valid \[bool\]

│

│     ├─ FC_Center_To_Stem_State

│     │  ├─ Center_State

│     │  ├─ Stem_State

│     │  ├─ Normal_State

│     │  ├─ Close_State

│     │  ├─ Submerge_State

│     │  ├─ Deep_Sea_State

│     │  ├─ Emergency_State

│     │  ├─ Transition_Progress \[float 0–1\]

│     │  └─ Interface_State_Valid \[bool\]

│

│     ├─ FC_Center_To_Stem_Clearance

│     │  ├─ Structural_Clearance

│     │  ├─ Transport_Clearance

│     │  ├─ Utility_Clearance

│     │  ├─ Pressure_Lock_Clearance

│     │  ├─ Telescopic_Clearance

│     │  ├─ Service_Clearance

│     │  ├─ Emergency_Clearance

│     │  └─ Clearance_Valid \[bool\]

│

│     ├─ FC_Center_To_Stem_Isolation

│     │  ├─ Isolate_Power \[bool\]

│     │  ├─ Isolate_Data \[bool\]

│     │  ├─ Isolate_Fluid \[bool\]

│     │  ├─ Isolate_Transport \[bool\]

│     │  ├─ Isolate_Pressure \[bool\]

│     │  ├─ Isolate_Service \[bool\]

│     │  ├─ Emergency_Isolation \[bool\]

│     │  ├─ Reconnect_Allowed \[bool\]

│     │  └─ Isolation_State

│

│     ├─ FC_Center_To_Stem_Emergency

│     │  ├─ Emergency_Trigger

│     │  ├─ Emergency_Transport_Link

│     │  ├─ Emergency_Power_Link

│     │  ├─ Emergency_Data_Link

│     │  ├─ Emergency_Pressure_Seal

│     │  ├─ Emergency_Isolation

│     │  ├─ Emergency_Bypass

│     │  └─ Emergency_State

│

│     └─ FC_Center_To_Stem_Debug

│        ├─ Show_Connection_Point

│        ├─ Show_Load_Path

│        ├─ Show_Transport_Link

│        ├─ Show_Utility_Link

│        ├─ Show_Pressure_Interface

│        ├─ Show_Telescopic_State

│        ├─ Show_Clearance

│        └─ Show_Interface_State

│

│
```
