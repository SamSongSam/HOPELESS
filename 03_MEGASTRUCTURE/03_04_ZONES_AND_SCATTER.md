# 03.04 - Flower Zones, Elevation, Scatter & Shoreline

## Purpose & PCG Implementation
การกระจายตัวของวัตถุและโซนบนพื้นผิวกลีบเมือง:
- **FC_Flower_Zone**: การจัดโซนตามระยะรัศมีและความหนาแน่น
- **FC_Flower_Height**: เส้นโค้งระดับความสูงตามสันกลีบและขอบกลีบ
- **FC_Flower_Scatter**: กฎการ Scatter จุด PCG Points (Poisson Disk / Jittered Grid)
- **FC_Flower_Shore**: ชายฝั่งรอบนอก ท่าเรือเทียบเรือผิวน้ำ และจุดเชื่อมต่อแนวน้ำ

---

## Parameter Tree

```text
├─ 03.06_FLOWER_ZONE

│  │

│  ├─ FC_Flower_Zone

│  │  ├─ Petal_ID \[int\]

│  │  ├─ Zone_ID \[int\]

│  │  ├─ Distance_From_Center

│  │  ├─ Distance_From_Cone

│  │  ├─ Distance_From_Petal_Edge

│  │  ├─ Current_Height

│  │  └─ Current_Petal_State

│  │

│  ├─ FC_Zone_Petal

│  ├─ FC_Zone_Inner

│  ├─ FC_Zone_Middle

│  ├─ FC_Zone_Outer

│  ├─ FC_Zone_Shore

│  └─ FC_Zone_Transition

│

│

├─ 03.07_FLOWER_HEIGHT

│  ├─ FC_Flower_Height

│  │  ├─ Base_Height

│  │  ├─ Petal_ID

│  │  ├─ Zone_ID

│  │  ├─ Distance_Factor

│  │  ├─ Open_Height

│  │  ├─ Closed_Height

│  │  └─ Height_Offset

│  │

│  └─ FC_Flower_Height_State

│

│

├─ 03.08_FLOWER_SCATTER

│  ├─ FC_Flower_Scatter

│  │  ├─ Petal_ID

│  │  ├─ Zone_ID

│  │  ├─ Density

│  │  ├─ Seed

│  │  ├─ Scale_Range

│  │  ├─ Height_Range

│  │  ├─ Center_Distance

│  │  └─ Petal_State

│  │

│  ├─ FC_Scatter_By_Petal

│  ├─ FC_Scatter_By_Zone

│  ├─ FC_Scatter_Exclusion

│  └─ FC_Scatter_State_Update

│

│

├─ 03.09_FLOWER_SHORE

│  │

│  ├─ FC_Flower_Shore

│  │  ├─ Shore_ID

│  │  ├─ Petal_ID

│  │  ├─ Connected \[bool\]

│  │  ├─ Connection_Amount

│  │  ├─ Shore_Width

│  │  └─ Shore_Offset

│  │

│  ├─ FC_Shore_Petal_Connector

│  ├─ FC_Shore_Detach

│  ├─ FC_Shore_Attach

│  ├─ FC_Shore_Edge

│  ├─ FC_Shore_Transition

│  └─ FC_Shore_Clearance

│

│
```
