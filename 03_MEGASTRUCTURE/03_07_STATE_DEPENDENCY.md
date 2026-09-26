# 03.07 - Global & Sector State Dependency Matrix

## Purpose & PCG Implementation
ตารางความสัมพันธ์เชิงตรรกะ (Dependency Logic): เมื่อสถานะหลักของเมืองเปลี่ยน (เช่น จาก Open เป็น Submerge หรือ Emergency) ระบบย่อยแต่ละส่วน (Petal, Stem, Root, Shore, Transport, Protection) จะต้องปรับสถานะตามอย่างไร

---

## Parameter Tree

```text
├─ 03.19_STATE_DEPENDENCY

│  │

│  ├─ FC_State_Dependency_Controller

│  │  ├─ Global_State

│  │  ├─ Transition_Progress \[float 0–1\]

│  │  ├─ Previous_State

│  │  ├─ Current_State

│  │  └─ Target_State

│  │

│  ├─ FC_State_Normal

│  ├─ FC_State_Open_For_Trade

│  ├─ FC_State_Prepare_Close

│  ├─ FC_State_Close

│  ├─ FC_State_Protected

│  ├─ FC_State_Prepare_Annual_Submerge

│  ├─ FC_State_Prepare_Submerge

│  ├─ FC_State_Submerge

│  ├─ FC_State_Submerged

│  ├─ FC_State_Deep_Sea_Operation

│  ├─ FC_State_Prepare_Surface_Return

│  ├─ FC_State_Prepare_Deploy

│  ├─ FC_State_Deploy

│  └─ FC_State_Emergency

│

│  ├─ FC_Dependency_Transport

│  │  ├─ Stop_Public_Transport

│  │  ├─ Clear_Transport_Path

│  │  ├─ Lock_Internal_Transport

│  │  └─ Confirm_Transport_Clear

│  │

│  ├─ FC_Dependency_Ring_Connection

│  │  ├─ Retract_Bridge

│  │  ├─ Disconnect_Port

│  │  ├─ Seal_Port

│  │  └─ Confirm_Disconnected

│  │

│  ├─ FC_Dependency_Shore

│  │  ├─ Shore_Prepare

│  │  ├─ Shore_Detach

│  │  ├─ Shore_Secure

│  │  └─ Confirm_Shore_Clear

│  │

│  ├─ FC_Dependency_Petal

│  │  ├─ Petal_Prepare

│  │  ├─ Petal_Raise

│  │  ├─ Petal_Close

│  │  ├─ Petal_Open

│  │  └─ Confirm_Petal_State

│  │

│  ├─ FC_Dependency_Zone

│  │  ├─ Update_Zone_Height

│  │  ├─ Update_Zone_Clearance

│  │  ├─ Update_Scatter_Position

│  │  └─ Update_Buildable_Area

│  │

│  ├─ FC_Dependency_Protection

│  │  ├─ Protection_Prepare

│  │  ├─ Protection_Enable

│  │  ├─ Protection_Disable

│  │  ├─ Check_Field_Coverage

│  │  └─ Confirm_Protection_State

│  │

│  ├─ FC_Dependency_Stem

│  │  ├─ Stem_Prepare_Collapse

│  │  ├─ Ring_Disconnect

│  │  ├─ Ring_Collapse

│  │  ├─ Ring_Deploy

│  │  └─ Confirm_Stem_State

│  │

│  ├─ FC_Dependency_Pressure

│  │  ├─ Update_Ring_Depth

│  │  ├─ Update_Pressure_Level

│  │  ├─ Update_Hazard_Level

│  │  ├─ Update_Occupancy

│  │  └─ Update_Transport_Restriction

│  │

│  ├─ FC_Dependency_Descent

│  │  ├─ Calculate_Descent

│  │  ├─ Stage_Stem_Collapse

│  │  ├─ Apply_Shock_Damping

│  │  ├─ Monitor_Load

│  │  └─ Confirm_Stable_Descent

│  │

│  ├─ FC_Dependency_Root

│  │  ├─ Root_Prepare

│  │  ├─ Root_Transition

│  │  ├─ Root_Anchor_State

│  │  └─ Confirm_Root_State

│  │

│  ├─ FC_State_Transition_Order

│  ├─ FC_State_Transition_Delay

│  ├─ FC_State_Transition_Limit

│  ├─ FC_State_Transition_Override

│  └─ FC_State_Transition_Debug

││

│  \[03.20 reserved for top-level GAME_READY system\]
│
```
