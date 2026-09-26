# 03.02.02 - Center Transport, Transit & Internal Circulation

## Purpose & PCG Implementation
ระบบโครงข่ายการเดินทางและสัญจรหลักภายในแกนกลางเมือง:
- ศูนย์กลางการคมนาคม (`FC_Center_Transport_Hub`)
- ทางเชื่อมขนส่งสู่กลีบ (`FC_Center_Petal_Transit`) และสู่ลำต้น (`FC_Center_Stem_Transit`)
- ลานเปลี่ยนถ่ายการเดินทาง (`FC_Center_Transfer_Plaza`)
- ข้อต่อยืดหยุ่นปรับตามการหุบกลีบ (`FC_Center_Articulated_Connection`, `FC_Center_Petal_Fold_Transit`)
- ระบบทางเดินภายในวงแหวน (`FC_Center_Ring_Corridor`), ทางเดินตามแนวรัศมี (`FC_Center_Radial_Corridor`), และลิฟต์แนวดิ่ง (`FC_Center_Vertical_Transport`)
- เส้นทางฉุกเฉินและควบคุมการเข้าถึง (`FC_Center_Access_Control`, `FC_Center_Emergency_Path`)

---

## Parameter Tree

```text
│  ├─ FC_Center_Transport_Hub

│  │  ├─ Center_Transport_Root

│  │  ├─ Transport_State

│  │  ├─ Transport_Mode

│  │  ├─ Active_Route_ID

│  │  ├─ Route_Priority

│  │  ├─ Route_Time_Window

│  │  ├─ Current_Petal_State

│  │  ├─ Current_Stem_State

│  │  └─ Transport_Enabled \[bool\]

│  │

│  ├─ FC_Center_Petal_Transit

│  │  ├─ Petal_ID

│  │  ├─ Petal_Station_ID

│  │  ├─ Petal_Entry

│  │  ├─ Petal_Exit

│  │  ├─ Center_Connection

│  │  ├─ Route_Transform

│  │  ├─ Route_Orientation

│  │  ├─ Route_Continuity

│  │  └─ Petal_Transit_State

│  │

│  ├─ FC_Center_Stem_Transit

│  │  ├─ Stem_Access

│  │  ├─ Stem_Entry

│  │  ├─ Stem_Exit

│  │  ├─ Stem_Transfer_Point

│  │  ├─ Vertical_Transfer

│  │  ├─ Hyperlink_Transfer

│  │  ├─ Lift_Transfer

│  │  └─ Stem_Transit_State

│  │

│  ├─ FC_Center_Transfer_Plaza

│  │  ├─ Civic_Plaza

│  │  ├─ Education_Access

│  │  ├─ Council_Access

│  │  ├─ Public_Transfer

│  │  ├─ Service_Transfer

│  │  └─ Emergency_Transfer

│  │

│  ├─ FC_Center_Transport_Mode

│  │  ├─ Walk

│  │  ├─ Wheeled

│  │  ├─ Rail

│  │  ├─ Magnetic

│  │  ├─ Pod

│  │  ├─ Hyperlink

│  │  └─ Lift

│  │

│  ├─ FC_Center_Transport_Adapter

│  │  ├─ Adapter_ID

│  │  ├─ Source_Mode

│  │  ├─ Target_Mode

│  │  ├─ Wheel_Mode

│  │  ├─ Rail_Mode

│  │  ├─ Magnetic_Mode

│  │  ├─ Connector_Type

│  │  ├─ Conversion_State

│  │  └─ Adapter_Enabled \[bool\]

│  │

│  ├─ FC_Center_Transport_Schedule

│  │  ├─ Route_ID

│  │  ├─ Allowed_State

│  │  ├─ Allowed_Start_Time

│  │  ├─ Allowed_End_Time

│  │  ├─ Priority_Level

│  │  ├─ Public_Allowed \[bool\]

│  │  ├─ Service_Allowed \[bool\]

│  │  └─ Emergency_Override \[bool\]

│  │

│  ├─ FC_Center_Articulated_Connection

│  │  ├─ Connection_ID

│  │  ├─ Petal_ID

│  │  ├─ Pivot_Point

│  │  ├─ Flexible_Joint

│  │  ├─ Magnetic_Joint

│  │  ├─ Rotation_Axis

│  │  ├─ Rotation_Limit

│  │  ├─ Translation_Limit

│  │  ├─ Alignment_State

│  │  └─ Connection_State

│  │

│  ├─ FC_Center_Magnetic_Transit

│  │  ├─ Magnetic_Field_State

│  │  ├─ Magnetic_Assist

│  │  ├─ Magnetic_Alignment

│  │  ├─ Magnetic_Lock

│  │  ├─ Magnetic_Release

│  │  └─ Magnetic_Safety

│  │

│  ├─ FC_Center_Petal_Fold_Transit

│  │  ├─ Petal_ID

│  │  ├─ Fold_Progress \[float 0–1\]

│  │  ├─ Route_Deformation

│  │  ├─ Route_Orientation_Update

│  │  ├─ Vehicle_Orientation_Update

│  │  ├─ Gravity_Compensation

│  │  ├─ Magnetic_Compensation

│  │  └─ Transit_Continuity_Valid \[bool\]

│  │

│  ├─ FC_Center_Bridge_State

│  │  ├─ Bridge_ID

│  │  ├─ Required_For_Current_State \[bool\]

│  │  ├─ Active \[bool\]

│  │  ├─ Folded \[bool\]

│  │  ├─ Locked \[bool\]

│  │  ├─ Retracted \[bool\]

│  │  └─ Bridge_State

│  │

│  ├─ FC_Center_Route_Consolidation

│  │  ├─ Source_Route_Count

│  │  ├─ Target_Route_Count

│  │  ├─ Merge_State

│  │  ├─ Merge_Point

│  │  ├─ Consolidated_Route

│  │  └─ Unused_Route_Disable

│  │

│  ├─ FC_Center_Public_Access

│  │  ├─ Public_Entry

│  │  ├─ Public_Exit

│  │  ├─ Civic_Access

│  │  ├─ Education_Access

│  │  └─ Council_Access

│  │

│  ├─ FC_Center_Service_Access

│  │  ├─ Service_Entry

│  │  ├─ Service_Exit

│  │  ├─ Maintenance_Access

│  │  ├─ Utility_Access

│  │  └─ Logistics_Access

│  │

│  ├─ FC_Center_Emergency_Access

│  │  ├─ Emergency_Route

│  │  ├─ Emergency_Entry

│  │  ├─ Emergency_Exit

│  │  ├─ Evacuation_Route

│  │  └─ Emergency_Override

│  │

│  └─ FC_Center_Transport_Debug

│     ├─ Show_Active_Route

│     ├─ Show_Transport_Mode

│     ├─ Show_Route_State

│     ├─ Show_Articulated_Joints

│     ├─ Show_Magnetic_Connections

│     ├─ Show_Bridge_State

│     └─ Show_Route_Continuity

│  │

│  ├─ FC_Center_Internal_Circulation

│  │  ├─ Circulation_Root

│  │  ├─ Circulation_State

│  │  ├─ Current_Center_State

│  │  └─ Circulation_Enabled \[bool\]

│  │

│  ├─ FC_Center_Ring_Corridor

│  │  ├─ Ring_ID

│  │  ├─ Corridor_Radius

│  │  ├─ Corridor_Width

│  │  ├─ Corridor_Height

│  │  ├─ Corridor_Level

│  │  ├─ Corridor_Direction

│  │  ├─ One_Way \[bool\]

│  │  ├─ Public_Allowed \[bool\]

│  │  ├─ Service_Allowed \[bool\]

│  │  └─ Corridor_State

│  │

│  ├─ FC_Center_Radial_Corridor

│  │  ├─ Corridor_ID

│  │  ├─ Source_Ring_ID

│  │  ├─ Target_Ring_ID

│  │  ├─ Target_Petal_ID

│  │  ├─ Corridor_Width

│  │  ├─ Corridor_Height

│  │  ├─ Radial_Angle

│  │  ├─ Corridor_Length

│  │  ├─ Public_Allowed \[bool\]

│  │  ├─ Service_Allowed \[bool\]

│  │  └─ Corridor_State

│  │

│  ├─ FC_Center_Vertical_Transport

│  │  ├─ Vertical_Route_ID

│  │  ├─ Source_Level

│  │  ├─ Target_Level

│  │  ├─ Hyperlink_Access \[bool\]

│  │  ├─ Lift_Access \[bool\]

│  │  ├─ Vertical_Shaft

│  │  ├─ Transfer_Point

│  │  ├─ Capacity

│  │  ├─ Priority_Level

│  │  └─ Vertical_Transport_State

│  │

│  ├─ FC_Center_Public_Circulation

│  │  ├─ Public_Route

│  │  ├─ Civic_Plaza_Route

│  │  ├─ Education_Route

│  │  ├─ Council_Route

│  │  ├─ Petal_Transfer_Route

│  │  └─ Stem_Transfer_Route

│  │

│  ├─ FC_Center_Service_Path

│  │  ├─ Service_Route_ID

│  │  ├─ Utility_Access

│  │  ├─ Maintenance_Access

│  │  ├─ Cargo_Access

│  │  ├─ Mechanical_Access

│  │  ├─ Restricted_Access \[bool\]

│  │  └─ Service_Path_State

│  │

│  ├─ FC_Center_Emergency_Path

│  │  ├─ Emergency_Route_ID

│  │  ├─ Evacuation_Path

│  │  ├─ Shelter_Access

│  │  ├─ Emergency_Stem_Access

│  │  ├─ Emergency_Petal_Access

│  │  ├─ Route_Redundancy

│  │  ├─ Blocked_Route_Bypass

│  │  └─ Emergency_Path_State

│  │

│  ├─ FC_Center_Access_Control

│  │  ├─ Access_Zone_ID

│  │  ├─ Public_Access \[bool\]

│  │  ├─ Staff_Access \[bool\]

│  │  ├─ Service_Access \[bool\]

│  │  ├─ Restricted_Access \[bool\]

│  │  ├─ Emergency_Override \[bool\]

│  │  └─ Access_State

│  │

│  ├─ FC_Center_Circulation_Connection

│  │  ├─ Connection_ID

│  │  ├─ Source_Route_ID

│  │  ├─ Target_Route_ID

│  │  ├─ Connection_Point

│  │  ├─ Transfer_Type

│  │  ├─ Connection_State

│  │  └─ Connection_Enabled \[bool\]

│  │

│  ├─ FC_Center_Circulation_Clearance

│  │  ├─ Minimum_Walk_Clearance

│  │  ├─ Vehicle_Clearance

│  │  ├─ Vertical_Clearance

│  │  ├─ Service_Clearance

│  │  ├─ Emergency_Clearance

│  │  └─ Clearance_Valid \[bool\]

│  │

│  └─ FC_Center_Circulation_Debug

│     ├─ Show_Ring_Corridor

│     ├─ Show_Radial_Corridor

│     ├─ Show_Vertical_Route

│     ├─ Show_Public_Route

│     ├─ Show_Service_Route

│     ├─ Show_Emergency_Route

│     └─ Show_Access_State

│
```
