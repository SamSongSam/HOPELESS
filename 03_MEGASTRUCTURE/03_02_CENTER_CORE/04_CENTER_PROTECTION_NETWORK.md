# 03.02.04 - Center Protection Network & Defense Pylons

## Purpose & PCG Implementation
ระบบป้องกันภัยระดับมหานครรอบแกนกลาง:
- จุดเชื่อมต่อโครงข่ายป้องกัน (`FC_Center_Protection_Interface`) และศูนย์ควบคุมม่านพลัง (`FC_Center_Protection_Control`)
- โครงข่ายเสาส่งสนามพลัง (`FC_Center_Pylon_Network_Interface`, `FC_Center_Field_State_Interface`)
- โซนและระดับการป้องกัน (`FC_Center_Protection_Zone_Interface`, `FC_Center_Protection_State`)
- ระบบรับมือความล้มเหลวและม่านพลังฉุกเฉิน (`FC_Center_Protection_Failure_Interface`, `FC_Center_Emergency_Protection`)

---

## Parameter Tree

```text
│  ├─ FC_Center_Protection_Interface

│  │  ├─ Protection_Interface_ID

│  │  ├─ Protection_Control_Link

│  │  ├─ Protection_Network_ID

│  │  ├─ Pylon_Network_Link

│  │  ├─ Field_State_Input

│  │  ├─ Field_State_Output

│  │  ├─ Protection_Mode

│  │  ├─ Protection_Priority

│  │  ├─ Protection_Enabled \[bool\]

│  │  ├─ Emergency_Protection_Link

│  │  └─ Protection_Interface_State

│  │

│  ├─ FC_Center_Protection_Control

│  │  ├─ Control_Center_ID

│  │  ├─ Control_Source_ID

│  │  ├─ Control_Target_ID

│  │  ├─ Enable_Command

│  │  ├─ Disable_Command

│  │  ├─ Strength_Command

│  │  ├─ Coverage_Command

│  │  ├─ Emergency_Command

│  │  ├─ Manual_Override

│  │  └─ Control_State

│  │

│  ├─ FC_Center_Pylon_Network_Interface

│  │  ├─ Pylon_ID

│  │  ├─ Pylon_Group_ID

│  │  ├─ Pylon_Zone_ID

│  │  ├─ Pylon_Active \[bool\]

│  │  ├─ Pylon_Health_State

│  │  ├─ Pylon_Field_Strength

│  │  ├─ Pylon_Coverage_Radius

│  │  ├─ Pylon_Network_State

│  │  └─ Pylon_Connection_Valid \[bool\]

│  │

│  ├─ FC_Center_Field_State_Interface

│  │  ├─ Field_ID

│  │  ├─ Field_Active \[bool\]

│  │  ├─ Field_Strength

│  │  ├─ Field_Coverage

│  │  ├─ Field_Overlap

│  │  ├─ Field_Gap

│  │  ├─ Field_Stability

│  │  ├─ Field_Load

│  │  ├─ Field_Failure_State

│  │  └─ Field_State

│  │

│  ├─ FC_Center_Protection_Zone_Interface

│  │  ├─ Protection_Zone_ID

│  │  ├─ Petal_ID

│  │  ├─ Zone_ID

│  │  ├─ Required_Coverage

│  │  ├─ Current_Coverage

│  │  ├─ Protection_Level

│  │  ├─ Priority_Level

│  │  └─ Zone_Protected \[bool\]

│  │

│  ├─ FC_Center_Protection_State

│  │  ├─ Normal_Protection

│  │  ├─ Trade_Protection

│  │  ├─ Closed_State_Protection

│  │  ├─ Submerge_Protection

│  │  ├─ Deep_Sea_Protection

│  │  └─ Emergency_Protection

│  │

│  ├─ FC_Center_Protection_Failure_Interface

│  │  ├─ Failed_Pylon_ID

│  │  ├─ Failed_Zone_ID

│  │  ├─ Coverage_Lost

│  │  ├─ Field_Instability

│  │  ├─ Reroute_Protection

│  │  ├─ Increase_Neighbor_Strength

│  │  ├─ Isolate_Failed_Pylon

│  │  └─ Failure_State

│  │

│  ├─ FC_Center_Emergency_Protection

│  │  ├─ Emergency_Trigger

│  │  ├─ Emergency_Coverage

│  │  ├─ Emergency_Strength

│  │  ├─ Emergency_Priority

│  │  ├─ Emergency_Power_Request

│  │  ├─ Emergency_Network_Override

│  │  └─ Emergency_Protection_State

│  │

│  ├─ FC_Center_Protection_Service_Interface

│  │  ├─ Power_Link

│  │  ├─ Data_Link

│  │  ├─ Service_Link

│  │  ├─ Maintenance_Link

│  │  ├─ Backup_Power_Link

│  │  └─ Service_State

│  │

│  └─ FC_Center_Protection_Debug

│     ├─ Show_Pylon_ID

│     ├─ Show_Protection_Zone

│     ├─ Show_Field_Coverage

│     ├─ Show_Field_Overlap

│     ├─ Show_Field_Gap

│     ├─ Show_Failed_Pylon

│     └─ Show_Protection_State

│
```
