# 03.02.06 - Center Sockets & Snapping Interface

## Purpose & PCG Implementation
จุดเชื่อมต่อกายภาพ (Hardware Sockets) ของแกนกลางสำหรับให้โมดูลอื่นมาประกอบ:
- ซ็อกเก็ตหลัก (`FC_Center_Socket`)
- ซ็อกเก็ตเชื่อมกลีบ (`FC_Center_Socket_Petal`) และเชื่อมลำต้น (`FC_Center_Socket_Stem`)
- ซ็อกเก็ตระบบขนส่ง (`FC_Center_Socket_Transport`) และงานระบบ (`FC_Center_Socket_Service`)
- ซ็อกเก็ตเสาป้องกัน (`FC_Center_Socket_Protection`) และข้อต่อ Rig (`FC_Center_Socket_Rig`)
- กฎการตรวจสอบความถูกต้องของซ็อกเก็ต (`FC_Center_Socket_Validation`, `FC_Center_Socket_Debug`)

---

## Parameter Tree

```text
│  ├─ FC_Center_Socket

│  │  ├─ Socket_ID

│  │  ├─ Socket_Type

│  │  ├─ Socket_Name

│  │  ├─ Socket_Group_ID

│  │  ├─ Parent_ID

│  │  ├─ Target_ID

│  │  ├─ Socket_Transform

│  │  ├─ Socket_Local_Transform

│  │  ├─ Socket_World_Transform

│  │  ├─ Socket_Position

│  │  ├─ Socket_Rotation

│  │  ├─ Socket_Scale

│  │  ├─ Socket_Normal

│  │  ├─ Socket_Tangent

│  │  ├─ Socket_Axis

│  │  ├─ Socket_Clearance

│  │  ├─ Socket_Radius

│  │  ├─ Socket_Orientation_Mode

│  │  ├─ Socket_Connection_Type

│  │  ├─ Socket_Connection_State

│  │  ├─ Socket_Lock_State

│  │  ├─ Socket_Seal_State

│  │  ├─ Socket_Active \[bool\]

│  │  ├─ Socket_Occupied \[bool\]

│  │  ├─ Socket_Enabled \[bool\]

│  │  └─ Socket_State

│  │

│  ├─ FC_Center_Socket_Petal

│  │  ├─ Petal_ID

│  │  ├─ Petal_Attach_Socket

│  │  ├─ Petal_Rig_Left_Socket

│  │  ├─ Petal_Rig_Right_Socket

│  │  ├─ Petal_Transport_Socket

│  │  ├─ Petal_Utility_Socket

│  │  └─ Petal_Socket_State

│  │

│  ├─ FC_Center_Socket_Stem

│  │  ├─ Stem_ID

│  │  ├─ Stem_Structural_Socket

│  │  ├─ Stem_Transport_Socket

│  │  ├─ Stem_Utility_Socket

│  │  ├─ Stem_Service_Socket

│  │  └─ Stem_Socket_State

│  │

│  ├─ FC_Center_Socket_Transport

│  │  ├─ Transport_Socket_ID

│  │  ├─ Route_ID

│  │  ├─ Transport_Mode

│  │  ├─ Entry_Socket

│  │  ├─ Exit_Socket

│  │  ├─ Transfer_Socket

│  │  └─ Transport_Socket_State

│  │

│  ├─ FC_Center_Socket_Service

│  │  ├─ Service_Socket_ID

│  │  ├─ Power_Socket

│  │  ├─ Data_Socket

│  │  ├─ Fluid_Socket

│  │  ├─ Environmental_Socket

│  │  ├─ Maintenance_Socket

│  │  └─ Service_Socket_State

│  │

│  ├─ FC_Center_Socket_Protection

│  │  ├─ Protection_Socket_ID

│  │  ├─ Pylon_Link_Socket

│  │  ├─ Control_Link_Socket

│  │  ├─ Power_Link_Socket

│  │  ├─ Data_Link_Socket

│  │  └─ Protection_Socket_State

│  │

│  ├─ FC_Center_Socket_Rig

│  │  ├─ Rig_Socket_ID

│  │  ├─ Rig_Part_ID

│  │  ├─ Rig_Pivot

│  │  ├─ Rig_Parent_ID

│  │  ├─ Rig_Control_Link

│  │  └─ Rig_Socket_State

│  │

│  ├─ FC_Center_Socket_Validation

│  │  ├─ Validate_Parent

│  │  ├─ Validate_Target

│  │  ├─ Validate_Transform

│  │  ├─ Validate_Orientation

│  │  ├─ Validate_Clearance

│  │  ├─ Validate_Occupancy

│  │  └─ Socket_Valid \[bool\]

│  │

│  └─ FC_Center_Socket_Debug

│     ├─ Show_Socket_ID

│     ├─ Show_Socket_Type

│     ├─ Show_Socket_Axis

│     ├─ Show_Socket_Normal

│     ├─ Show_Socket_Clearance

│     ├─ Show_Connection_State

│     └─ Show_Occupancy

│
```
