# 00_CORE - Global Settings, Seeds & Registry

## Purpose & PCG Implementation
ชุดการตั้งค่าระดับ Master Control สำหรับการควบคุมการ Generate เมืองทั้งหมด ทำหน้าที่เป็น Root Node ใน PCG Graph:
- **FC_Global_Settings**: กำหนดขอบเขตสเกลรวม (World Bounds), ระดับน้ำทะเลอ้างอิง (Sea Level Z = 0), และจำนวนกลีบเมืองหลัก
- **FC_Seed_Control**: Root Random Stream สำหรับการสุ่มแบบ Deterministic (ใส่ Seed เดิม โลกต้อง Gen ออกมาเหมือนเดิม 100%)
- **FC_Scale_Units**: มาตรฐานสเกลเรขาคณิต (1 Unreal Unit = 1 cm) เพื่อให้ทุก Prefab สอดคล้องกัน
- **FC_Debug_View**: สวิตช์เปิด-ปิด Visualizer แสดงขอบเขต Grid, Sockets, และเส้นทาง Splines
- **FC_Attribute_Registry**: คลังรายชื่อ PCG Point Attributes ทั้งหมดที่ส่งต่อใน Graph Pipeline

---

## Parameter Tree

```text
00_CORE

├─ FC_Global_Settings

├─ FC_Seed_Control

├─ FC_Scale_Units

├─ FC_Debug_View

└─ FC_Attribute_Registry
```

---

## PCG Attribute Specification

| Attribute Name | Data Type | Default Value | PCG Scope | Description |
| :--- | :--- | :--- | :--- | :--- |
| `City_ID` | `FName` | `ISTRORIGAN` | Global | ชื่อมหานครต้นแบบแห่งการศึกษา Year 4205 |
| `World_Era_Year` | `int32` | `4205` | Global | ยุคสมัยหลังมหาอุทกภัย 17 รัฐ |
| `Council_Count` | `int32` | `10` | Global | จำนวนสมาชิกสภาสูงผู้ปกครองเมือง (Council of Ten) |
| `Global_Master_Seed` | `int64` | `133742` | Global | เมล็ดพันธุ์หลักในการสุ่มทั้งโลก |
| `World_Scale_Factor` | `float` | `1.0` | Global | ตัวคูณขนาดสัดส่วนภาพรวมของเมือง |
| `Sea_Level_Z` | `float` | `0.0` | Global | ระดับความสูงผิวน้ำทะเลอ้างอิง (cm) |
| `Max_Petal_Count` | `int32` | `8` | Global | จำนวน 8 กลีบวิทยาเขตอิสระ |
| `Submersion_Cycle_Per_Year` | `int32` | `2` | Global | ความถี่การดำน้ำเพื่อการศึกษาใต้สมุทร (ปีละ 2 ครั้ง) |
| `Debug_Draw_Lattice` | `bool` | `false` | Debug | แสดงเส้น Grid เชิงขั้ว (Polar Lattice) |
