# 03.02.03 - Center Service, Utility Core & Environmental Networks

## Purpose & PCG Implementation
ระบบสาธารณูปโภคและระบบสนับสนุนชีวิต (Life Support / Engineering Core) ของแกนกลาง:
- แกนงานระบบบริการ (`FC_Center_Service_Core`) และแกนสาธารณูปโภค (`FC_Center_Utility_Core`)
- ข้อต่อจ่ายพลังงาน (`FC_Center_Power_Interface`), ระบบส่งข้อมูล (`FC_Center_Data_Interface`), และท่อของเหลว/ออกซิเจน (`FC_Center_Fluid_Interface`)
- ช่องทางซ่อมบำรุงและระบบบริการฉุกเฉิน (`FC_Center_Maintenance_Access`, `FC_Center_Emergency_Service`)
- ระบบควบคุมสิ่งแวดล้อมและการแยกส่วนตัดตอน (`FC_Center_Environmental_Service`, `FC_Center_Service_Isolation`)

---

## Parameter Tree

```text
│  ├─ FC_Center_Service_Core

│  │  ├─ Service_Core_ID

│  │  ├─ Service_Core_Root

│  │  ├─ Service_Core_State

│  │  ├─ Service_Core_Capacity

│  │  └─ Service_Core_Enabled \[bool\]

│  │

│  ├─ FC_Center_Utility_Core

│  │  ├─ Utility_Core

│  │  ├─ Utility_Zone_ID

│  │  ├─ Utility_Route

│  │  ├─ Utility_Capacity

│  │  ├─ Utility_Load

│  │  ├─ Utility_State

│  │  └─ Utility_Enabled \[bool\]

│  │

│  ├─ FC_Center_Power_Interface

│  │  ├─ Power_Input

│  │  ├─ Power_Output

│  │  ├─ Power_Source_ID

│  │  ├─ Power_Target_ID

│  │  ├─ Power_Capacity

│  │  ├─ Power_Load

│  │  ├─ Backup_Power

│  │  ├─ Emergency_Power

│  │  ├─ Power_Isolation

│  │  └─ Power_State

│  │

│  ├─ FC_Center_Data_Interface

│  │  ├─ Data_Input

│  │  ├─ Data_Output

│  │  ├─ Network_ID

│  │  ├─ Data_Route

│  │  ├─ Control_Link

│  │  ├─ Protection_Network_Link

│  │  ├─ Transport_Network_Link

│  │  ├─ Stem_Network_Link

│  │  ├─ Root_Network_Link

│  │  ├─ Backup_Data_Link

│  │  └─ Data_State

│  │

│  ├─ FC_Center_Fluid_Interface

│  │  ├─ Fluid_Input

│  │  ├─ Fluid_Output

│  │  ├─ Fluid_Type

│  │  ├─ Fluid_Route

│  │  ├─ Flow_Rate

│  │  ├─ Pressure

│  │  ├─ Storage_Link

│  │  ├─ Isolation_Valve

│  │  ├─ Emergency_Shutoff

│  │  └─ Fluid_State

│  │

│  ├─ FC_Center_Maintenance_Access

│  │  ├─ Maintenance_Route

│  │  ├─ Maintenance_Entry

│  │  ├─ Maintenance_Exit

│  │  ├─ Inspection_Point

│  │  ├─ Repair_Point

│  │  ├─ Service_Hatch

│  │  ├─ Restricted_Access \[bool\]

│  │  └─ Maintenance_State

│  │

│  ├─ FC_Center_Emergency_Service

│  │  ├─ Emergency_Power

│  │  ├─ Emergency_Data

│  │  ├─ Emergency_Fluid

│  │  ├─ Emergency_Air

│  │  ├─ Emergency_Water

│  │  ├─ Emergency_Shutoff

│  │  ├─ Emergency_Bypass

│  │  ├─ Emergency_Service_Route

│  │  └─ Emergency_Service_State

│  │

│  ├─ FC_Center_Service_Clearance

│  │  ├─ Utility_Clearance

│  │  ├─ Power_Clearance

│  │  ├─ Data_Clearance

│  │  ├─ Fluid_Clearance

│  │  ├─ Maintenance_Clearance

│  │  ├─ Emergency_Clearance

│  │  └─ Clearance_Valid \[bool\]

│  │

│  └─ FC_Center_Service_Debug

│     ├─ Show_Power_Route

│     ├─ Show_Data_Route

│     ├─ Show_Fluid_Route

│     ├─ Show_Service_Route

│     ├─ Show_Isolation_Zone

│     └─ Show_Service_State
│

│  ├─ FC_Center_Environmental_Service

│  │  ├─ Environmental_Service_ID

│  │  ├─ Environmental_Zone_ID

│  │  ├─ Environmental_State

│  │  ├─ Environmental_Enabled \[bool\]

│  │  ├─ Air_Supply

│  │  ├─ Air_Return

│  │  ├─ Ventilation

│  │  ├─ Air_Pressure

│  │  ├─ Pressure_Compensation

│  │  ├─ Oxygen_Level

│  │  ├─ Temperature_Control

│  │  ├─ Humidity_Control

│  │  ├─ Water_Service

│  │  ├─ Water_Recycling

│  │  ├─ Waste_Service

│  │  ├─ Waste_Isolation

│  │  ├─ Submerge_Environmental_Mode

│  │  ├─ Deep_Sea_Environmental_Mode

│  │  ├─ Emergency_Air_Mode

│  │  ├─ Emergency_Pressure_Mode

│  │  ├─ Environmental_Load

│  │  ├─ Environmental_Capacity

│  │  └─ Environmental_Valid \[bool\]

│  │

│  ├─ FC_Center_Service_Distribution

│  │  ├─ Service_Distribution_ID

│  │  ├─ Distribution_Root

│  │  ├─ Distribution_State

│  │  ├─ Distribution_Enabled \[bool\]

│  │  ├─ Source_Service_ID

│  │  ├─ Target_Service_ID

│  │  ├─ Center_Service_Route

│  │  ├─ Petal_Service_Route

│  │  ├─ Stem_Service_Route

│  │  ├─ Protection_Service_Route

│  │  ├─ Transport_Service_Route

│  │  ├─ Public_Service_Route

│  │  ├─ Service_Branch_Point

│  │  ├─ Service_Junction

│  │  ├─ Route_Priority

│  │  ├─ Route_Capacity

│  │  ├─ Route_Load

│  │  ├─ Route_State

│  │  ├─ Primary_Route

│  │  ├─ Secondary_Route

│  │  ├─ Redundant_Route

│  │  ├─ Emergency_Bypass_Route

│  │  ├─ Distribution_Balance

│  │  ├─ Distribution_Override

│  │  └─ Distribution_Valid \[bool\]

│  │

│  ├─ FC_Center_Service_Isolation

│  │  ├─ Isolation_ID

│  │  ├─ Isolation_Zone_ID

│  │  ├─ Isolation_State

│  │  ├─ Isolation_Enabled \[bool\]

│  │  ├─ Isolation_Source_ID

│  │  ├─ Isolation_Target_ID

│  │  ├─ Power_Isolated \[bool\]

│  │  ├─ Data_Isolated \[bool\]

│  │  ├─ Fluid_Isolated \[bool\]

│  │  ├─ Environmental_Isolated \[bool\]

│  │  ├─ Transport_Service_Isolated \[bool\]

│  │  ├─ Petal_Service_Isolated \[bool\]

│  │  ├─ Stem_Service_Isolated \[bool\]

│  │  ├─ Protection_Service_Isolated \[bool\]

│  │  ├─ Automatic_Isolation \[bool\]

│  │  ├─ Manual_Isolation \[bool\]

│  │  ├─ Emergency_Isolation \[bool\]

│  │  ├─ Pressure_Isolation

│  │  ├─ Flood_Isolation

│  │  ├─ Fire_Isolation

│  │  ├─ Structural_Failure_Isolation

│  │  ├─ Isolation_Boundary

│  │  ├─ Isolation_Seal

│  │  ├─ Isolation_Bypass

│  │  ├─ Reconnect_Allowed \[bool\]

│  │  ├─ Reconnect_State

│  │  └─ Isolation_Valid \[bool\]

│
```
