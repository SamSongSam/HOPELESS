# 03.02.05 - Center State Machine & Mode Transitions

## Purpose & PCG Implementation
เครื่องจักรสถิต (Finite State Machine) ควบคุมพฤติกรรมของแกนกลางเมือง:
- สถานะการทำงานปกติ (`FC_Center_Normal_State`)
- สถานะเปิดการค้า (`FC_Center_Trade_State`)
- สถานะปิดผนึก/หุบ (`FC_Center_Close_State`)
- สถานะจมน้ำ (`FC_Center_Submerge_State`)
- สถานะทะเลลึก (`FC_Center_Deep_Sea_State`)
- สถานะฉุกเฉิน (`FC_Center_Emergency_State`)
- การเปลี่ยนผ่านสถานะและการตรวจสอบ (`FC_Center_State_Transition`, `FC_Center_State_Debug`)

---

## Parameter Tree

```text
│  ├─ FC_Center_State

│  │  ├─ Normal_State

│  │  ├─ Trade_State

│  │  ├─ Close_State

│  │  ├─ Submerge_State

│  │  ├─ Deep_Sea_State

│  │  ├─ Emergency_State

│  │  ├─ Previous_State

│  │  ├─ Current_State

│  │  ├─ Target_State

│  │  ├─ State_Transition_Progress \[float 0–1\]

│  │  ├─ Center_Operational \[bool\]

│  │  ├─ Public_Access_Enabled \[bool\]

│  │  ├─ Service_Access_Enabled \[bool\]

│  │  ├─ Transport_Enabled \[bool\]

│  │  ├─ Protection_Enabled \[bool\]

│  │  ├─ Utility_Enabled \[bool\]

│  │  ├─ Environmental_Service_Enabled \[bool\]

│  │  ├─ Emergency_Service_Enabled \[bool\]

│  │  └─ State_Valid \[bool\]

│  │

│  ├─ FC_Center_Normal_State

│  │  ├─ Public_Access

│  │  ├─ Civic_Access

│  │  ├─ Education_Access

│  │  ├─ Council_Access

│  │  ├─ Standard_Transport

│  │  ├─ Standard_Protection

│  │  └─ Standard_Service

│  │

│  ├─ FC_Center_Trade_State

│  │  ├─ Trade_Access_Enabled \[bool\]

│  │  ├─ External_Visitor_Access

│  │  ├─ Public_Transport_Priority

│  │  ├─ Petal_Access_Priority

│  │  ├─ Shore_Access_State

│  │  ├─ Protection_Trade_Mode

│  │  ├─ Service_Load_Mode

│  │  └─ Trade_State_Valid \[bool\]

│  │

│  ├─ FC_Center_Close_State

│  │  ├─ Petal_Close_Active \[bool\]

│  │  ├─ Center_Clearance_Lock

│  │  ├─ Building_Clearance_Lock

│  │  ├─ Transport_Reconfiguration

│  │  ├─ Bridge_State_Update

│  │  ├─ Service_Route_Update

│  │  ├─ Protection_State_Update

│  │  └─ Close_State_Valid \[bool\]

│  │

│  ├─ FC_Center_Submerge_State

│  │  ├─ Submerge_Active \[bool\]

│  │  ├─ Submerge_Progress \[float 0–1\]

│  │  ├─ Pressure_Mode

│  │  ├─ Environmental_Mode

│  │  ├─ Transport_Submerge_Mode

│  │  ├─ Service_Isolation_Mode

│  │  ├─ Protection_Submerge_Mode

│  │  └─ Submerge_State_Valid \[bool\]

│  │

│  ├─ FC_Center_Deep_Sea_State

│  │  ├─ Deep_Sea_Mode \[bool\]

│  │  ├─ Pressure_Level

│  │  ├─ Hazard_Level

│  │  ├─ Occupancy_Mode

│  │  ├─ Restricted_Access_Mode

│  │  ├─ Environmental_Deep_Sea_Mode

│  │  ├─ Protection_Deep_Sea_Mode

│  │  ├─ Service_Deep_Sea_Mode

│  │  ├─ Transport_Deep_Sea_Mode

│  │  └─ Deep_Sea_State_Valid \[bool\]

│  │

│  ├─ FC_Center_Emergency_State

│  │  ├─ Emergency_Active \[bool\]

│  │  ├─ Emergency_Type

│  │  ├─ Emergency_Priority

│  │  ├─ Emergency_Transport

│  │  ├─ Emergency_Protection

│  │  ├─ Emergency_Service

│  │  ├─ Emergency_Isolation

│  │  ├─ Emergency_Evacuation

│  │  ├─ Manual_Override

│  │  └─ Emergency_State_Valid \[bool\]

│  │

│  ├─ FC_Center_State_Transition

│  │  ├─ Source_State

│  │  ├─ Target_State

│  │  ├─ Transition_Progress \[float 0–1\]

│  │  ├─ Transition_Delay

│  │  ├─ Transition_Limit

│  │  ├─ Transition_Override

│  │  └─ Transition_Valid \[bool\]

│  │

│  └─ FC_Center_State_Debug

│     ├─ Show_Current_State

│     ├─ Show_Target_State

│     ├─ Show_Access_State

│     ├─ Show_Transport_State

│     ├─ Show_Protection_State

│     ├─ Show_Service_State

│     └─ Show_State_Validation

│
```
