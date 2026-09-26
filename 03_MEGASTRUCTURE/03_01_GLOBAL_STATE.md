# 03.01_FLOWER_GLOBAL_STATE - Global City State Machine

## Purpose & PCG Implementation
ศูนย์กลางสถานะสากลของ Flower Megastructure ที่ส่งผลกระทบต่อทั้งเมือง:
- สถานะการบาน/หุบ (`Open_State`, `Open_Amount 0-1`)
- สถานะการค้าเปิดรับเรือภายนอก (`Trade_State`)
- สถานะกางม่านพลังป้องกัน (`Protection_State`)
- สถานะดำน้ำ/จมน้ำ (`Submerge_State`, `Submerge_Amount 0-1`)
- โหมดทะเลลึก (`Deep_Sea_Mode`)
- โหมดฉุกเฉินระดับวิกฤต (`Emergency_State`)
- ระบบกระจายสถานะ (`FC_Flower_State_Distributor`)

---

## Parameter Tree

```text
├─ 03.01_FLOWER_GLOBAL_STATE

│  │

│  ├─ FC_Flower_State

│  │  ├─ Open_State \[bool\]

│  │  ├─ Open_Amount \[float 0–1\]

│  │  ├─ Trade_State \[bool\]

│  │  ├─ Protection_State \[bool\]

│  │  ├─ Submerge_State \[bool\]

│  │  ├─ Submerge_Amount \[float 0–1\]

│  │  ├─ Deep_Sea_Mode \[bool\]

│  │  ├─ Emergency_State \[bool\]

│  │  ├─ Annual_Cycle_State \[int / enum\]

│  │  ├─ Previous_Global_State

│  │  ├─ Current_Global_State

│  │  └─ Target_Global_State

│  │

│  └─ FC_Flower_State_Distributor

│     │

│     ├─ Structure_State

│     │  └─ Petal / Zone / Shore / Stem / Root / Center

│     │

│     ├─ Protection_State

│     │  └─ Protection Network / Protection Pylon / Protection Control Center

│     │

│     ├─ Operation_State

│     │  └─ Transport / Occupancy / Public Access / Service Access

│     │

│     ├─ Trade_State

│     │  └─ Public Access / Shore Docking / Transport / Protection

│     │

│     ├─ Submerge_State

│     │  └─ Pressure / Descent / Stem / Root / Shore / Transport

│     │

│     ├─ Deep_Sea_State

│     │  └─ Pressure / Hazard / Occupancy / Ring Access / Root Operation

│     │

│     └─ Emergency_State

│        └─ Protection / Transport / Petal / Stem / Root / Shore / Evacuation

│

│
```

---

## PCG Runtime Adapter Mapping
สถานะเหล่านี้จะถูกส่งต่อเข้าสู่ `FC_PCG_Runtime_State_Adapter` เพื่อควบคุม:
1. การเปิด/ปิด Watertight Bulkheads ในท่อทางเดิน
2. การปรับ Material Parameter Collection (เช่น คราบน้ำ, ตะไคร่, แสงไฟเตือนภัยสีแดง)
3. การสลับโหมด Collision และ Spline Pathfinding
