# 03.03 - Petal Structure, State & Rigging

## Purpose & PCG Implementation
ระบบกลีบดอกไม้ (Petals) ของเมือง:
- **FC_Flower_Petal**: โครงสร้างทางกายภาพของกลีบ ความยาว ความกว้าง สันกลาง (Spine) ขอบใบ (Blade)
- **FC_Petal_State**: สถานะของกลีบ (กางออก, หุบเข้า, โหมดป้องกัน, โหมดลอยตัว)
- **FC_Petal_Rig**: กระดูกข้อต่อ (Bones/Joints), ค่าขีดจำกัดมุมการหมุน (Angular Limits), และตัวหน่วงการสั่นไหว (Dampers)

---

## Parameter Tree

```text
├─ 03.03_PETAL_STRUCTURE

│  ├─ FC_Flower_Petal

│  │  ├─ Petal_ID \[int\]

│  │  ├─ Petal_Count \[int\]

│  │  ├─ Petal_Length

│  │  ├─ Petal_Width

│  │  ├─ Petal_Thickness

│  │  ├─ Petal_Profile

│  │  └─ Petal_Rotation

│  │

│  ├─ FC_Petal_Inner_Attach

│  ├─ FC_Petal_Outer_Edge

│  ├─ FC_Petal_Left_Edge

│  ├─ FC_Petal_Right_Edge

│  ├─ FC_Petal_Shore_Attach

│  └─ FC_Petal_Center_Clearance

│

│

├─ 03.04_PETAL_STATE

│  ├─ FC_Petal_State

│  │  ├─ Petal_ID

│  │  ├─ Open \[bool\]

│  │  ├─ Open_Amount \[float\]

│  │  ├─ Target_Height

│  │  └─ Transition_Progress

│  │

│  ├─ FC_Petal_Open

│  ├─ FC_Petal_Close

│  └─ FC_Petal_State_Transition

│

│

├─ 03.05_PETAL_RIG

│  │

│  ├─ FC_Petal_Rig

│  │  ├─ Petal_ID

│  │  ├─ Rig_Left

│  │  ├─ Rig_Right

│  │  ├─ Inner_Pivot

│  │  ├─ Left_Pivot

│  │  ├─ Right_Pivot

│  │  ├─ Raise_Amount

│  │  ├─ Lower_Amount

│  │  ├─ Twist_Amount

│  │  └─ Rig_State

│  │

│  ├─ FC_Petal_Rig_Left

│  ├─ FC_Petal_Rig_Right

│  ├─ FC_Petal_Rig_Balance

│  ├─ FC_Petal_Rig_Limit

│  └─ FC_Petal_Rig_Debug

│

│
```
