# 06 - Game-Ready Tech, LODs & Presentation

## Purpose & PCG Implementation
ข้อกำหนดทางเทคนิคสำหรับการนำไป Render และรันใน Game Engine:
- **FC_Collision**: ขอบเขตการชน (Simple Primitives vs Complex Convex)
- **FC_LOD**: ระยะการแสดงผลและ Nanite Settings
- **FC_Material_ID**: การจัดกลุ่ม Material เพื่อลด Draw Calls
- **FC_UV_Prep**: การเตรียม UV สำหรับ Lightmaps และ Detail Textures
- **FC_Instance_Policy**: นโยบายการ Instance (HISM / ISM / Packed Level Actors)
- **FC_Export_Prep**: การเตรียมข้อมูลสำหรับ Export สู่ Unreal / Unity
- **Rig & Presentation**: กล้อง Hero Setup, Breakdown View, และ Portfolio Debug

---

## Parameter Tree

### Rigging Data (06_RIG)
```text
06_RIG

├─ FC_Rig_Pivot

├─ FC_Rig_MovablePart

├─ FC_Rig_Socket

├─ FC_Rig_BoneData

└─ FC_Rig_Debug
```

### Game-Ready Technical Setup (07_GAME_READY)
```text
07_GAME_READY

├─ FC_Collision

├─ FC_LOD

├─ FC_Material_ID

├─ FC_UV_Prep

├─ FC_Instance_Policy

└─ FC_Export_Prep
```

### Presentation & Portfolio View (08_PRESENTATION)
```text
08_PRESENTATION

├─ FC_Hero_Setup

├─ FC_Breakdown_View

└─ FC_Portfolio_Debug
```
