# 03.08 - Megastructure Rig Export Interface

## Purpose & PCG Implementation
ส่วนต่อประสานสำหรับส่งออกโครงสร้าง Rig และแอนิเมชันไปยัง Game Engine:
- รายชื่อกระดูกหลัก (Master Bone Hierarchy)
- Curve Parameters สำหรับ Blend Shapes / Procedural Animation
- ซ็อกเก็ตสำหรับผูกโมดูลเข้ากับกระดูก Rig ตอน Runtime

---

## Parameter Tree

```text
└─ 03.21_RIG_EXPORT_INTERFACE

│

├─ FC_Rig_Export_Interface

│  ├─ Rig_System_ID

│  ├─ Part_ID

│  ├─ Parent_ID

│  ├─ Root_Transform

│  ├─ Local_Transform

│  ├─ Pivot_Transform

│  ├─ Rest_Transform

│  └─ Export_Enabled \[bool\]

│

├─ FC_Rig_Part_Classification

│  ├─ Static

│  ├─ Rigid_Movable

│  ├─ Deformable

│  ├─ Telescopic

│  ├─ Connector

│  └─ Socket

│

├─ FC_Rig_Petal_Interface

│  ├─ Petal_ID

│  ├─ Petal_Root

│  ├─ Rig_Left

│  ├─ Rig_Right

│  ├─ Inner_Pivot

│  ├─ Left_Pivot

│  ├─ Right_Pivot

│  ├─ Open_Value

│  ├─ Raise_Value

│  ├─ Lower_Value

│  └─ Twist_Value

│

├─ FC_Rig_Protection_Interface

│  ├─ Pylon_ID

│  ├─ Pylon_Root

│  ├─ Pylon_Pivot

│  ├─ Active_Value

│  └─ Field_State

│

├─ FC_Rig_Stem_Interface

│  ├─ Ring_ID

│  ├─ Parent_Ring_ID

│  ├─ Ring_Pivot

│  ├─ Extended_Transform

│  ├─ Collapsed_Transform

│  ├─ Deploy_Value

│  ├─ Collapse_Value

│  ├─ Collapse_Rate

│  ├─ Shock_Damping_Value

│  ├─ Current_Depth

│  └─ Descent_State

│

├─ FC_Rig_Ring_Connection_Interface

│  ├─ Connection_ID

│  ├─ Source_Ring_ID

│  ├─ Target_Ring_ID

│  ├─ Port_A_Transform

│  ├─ Port_B_Transform

│  ├─ Bridge_Root

│  ├─ Extend_Value

│  ├─ Lock_State

│  ├─ Seal_State

│  └─ Connection_State

│

├─ FC_Rig_Shore_Interface

│  ├─ Shore_ID

│  ├─ Petal_ID

│  ├─ Shore_Root

│  ├─ Attach_Point

│  ├─ Detach_Transform

│  ├─ Dock_Transform

│  ├─ Free_Float_State

│  ├─ Navigation_Root

│  ├─ Stabilization_State

│  └─ Connection_State

│

├─ FC_Rig_Root_Interface

│  ├─ Root_ID

│  ├─ Root_Root

│  ├─ Root_Anchor

│  ├─ Root_To_Stem

│  ├─ Anchor_State

│  └─ Root_Transition_State

│

├─ FC_Rig_Socket_Interface

│  ├─ Socket_ID

│  ├─ Socket_Type

│  ├─ Parent_Part_ID

│  ├─ Socket_Transform

│  ├─ Socket_State

│  └─ Connection_Target_ID

│

├─ FC_Rig_Bone_Mapping

│  ├─ Part_ID

│  ├─ Bone_ID

│  ├─ Bone_Name

│  └─ Parent_Bone_ID

│

├─ FC_Rig_Control_Mapping

│  ├─ Control_ID

│  ├─ Target_Part_ID

│  ├─ Control_Type

│  └─ Control_Value

│

├─ FC_Rig_Pivot_Mapping

│  ├─ Part_ID

│  ├─ Pivot_ID

│  ├─ Pivot_Transform

│  └─ Pivot_Space

│

├─ FC_Rig_Socket_Mapping

│  ├─ Socket_ID

│  ├─ Parent_Part_ID

│  ├─ Target_ID

│  └─ Connection_Type

│

├─ FC_Rig_Transform_Space

│  ├─ World_Space

│  ├─ Root_Space

│  ├─ Parent_Space

│  └─ Local_Space

│

├─ FC_Rig_Hierarchy_Validation

│  ├─ Validate_Parent_ID

│  ├─ Validate_Pivot

│  ├─ Validate_Root

│  ├─ Validate_Socket

│  └─ Validate_Movable_Hierarchy

│

├─ FC_Rig_Export_Validation

│  ├─ Missing_ID

│  ├─ Missing_Pivot

│  ├─ Missing_Parent

│  ├─ Invalid_Transform

│  ├─ Invalid_Hierarchy

│  └─ Export_Ready \[bool\]

│

└─ FC_Rig_Export_Debug

├─ Show_Pivots

├─ Show_Roots

├─ Show_Sockets

├─ Show_Parent_Links

├─ Show_Rig_ID

└─ Show_Export_Status
```
