# 03.05 - Stem Rings, Telescopic Columns & Abyssal Roots (Expanding Cradle)

## World Canon & Hydrodynamic Physics (Era: 4205)
โครงสร้างลำต้นใต้น้ำและรากยึดสมุทรของมหานคร **ISTRORIGAN**:
- **Expanding Inverted Telescopic Rings (วงแหวนข้อปล้องบนเล็ก ขยายใหญ่ลงลึกสู่ก้นสมุทร)**:
  - วงแหวนปล้องชั้นบนสุดใต้แกนกลางมีขนาดแคบ ($R = 80\text{ m}$) และจะ **ขยายเส้นผ่านศูนย์กลางกว้างขึ้นเรื่อยๆ ตามความลึก** จนถึงฐานล่างสุด ($R = 350\text{ m}$)
  - **ฟิสิกส์ทางทะเล (Naval Engineering):** การออกแบบให้ฐานล่างกว้างและหนัก ทำให้จุดศูนย์ถ่วง ($KG$) อยู่ต่ำกว่าจุดศูนย์กลางแรงลอยตัว ($KB$) อย่างมหาศาล กลายเป็นโครงสร้างแบบ **Self-Righting** ที่ไม่มีวันพลิกคว่ำเด็ดขาด
  - **Hydraulic Cradle Shelf:** เมื่อเมืองเข้าสู่โหมดดำน้ำ วงแหวนที่กว้างออกจะทำหน้าที่เป็น **"เปลรองรับไฮดรอลิก"** อุ้มและกระจายแรงดันน้ำของกลีบเมืองทั้ง 8 ไม่ให้แรงกดไปกระจุกที่แกนกลาง
- **Bi-Annual Submersion Ballast Control**: ถังอัดและสูบน้ำทะเลขนาดมหึมา ควบคุมการดำน้ำปีละ 2 ครั้งเพื่อการศึกษาใต้สมุทรลึก
- **Doomsday Knowledge Vault & Bedrock Anchor**: ปล้องล่างสุดที่ฝังลงในแนวสันหินก้นทะเล บรรจุ **เซิร์ฟเวอร์สำรองข้อมูลอารยธรรมมนุษย์ก่อนน้ำท่วมและธนาคารดีเอ็นเอชีวภาพ** ที่ปลอดภัยที่สุดในโลก ยึดด้วยกรงเล็บไฮดรอลิก (`ARCH_ROOT_SEABED_CLAW`)

---

## Parameter Tree

```text
├─ 03.11_STEM_RING

│  │

│  ├─ FC_STEM_Ring

│  │  ├─ Ring_ID \[int\]

│  │  ├─ Ring_Count \[int\]

│  │  ├─ Ring_Radius

│  │  ├─ Ring_Height \[\>= 3m\]

│  │  ├─ Ring_Thickness

│  │  ├─ Extended_Z

│  │  ├─ Collapsed_Z

│  │  ├─ Collapse_Amount

│  │  ├─ Current_Depth

│  │  ├─ Pressure_Level

│  │  ├─ Hazard_Level

│  │  ├─ Occupancy_Allowed \[bool\]

│  │  ├─ Pressure_Rating

│  │  ├─ Emergency_Seal_State

│  │  ├─ Transport_Status

│  │  └─ City_Submerged_Mode \[bool\]

│  │

│  ├─ FC_STEM_Ring_Shell

│  ├─ FC_STEM_Ring_Floor

│  ├─ FC_STEM_Ring_Interior

│  ├─ FC_STEM_Ring_Service

│  └─ FC_STEM_Ring_Clearance

│

│

├─ 03.12_STEM_TELESCOPIC_SYSTEM

│  │

│  ├─ FC_STEM_Telescope

│  │  ├─ Deploy_Amount \[0–1\]

│  │  ├─ Ring_ID

│  │  ├─ Extended_Z

│  │  ├─ Collapsed_Z

│  │  ├─ Overlap

│  │  ├─ Clearance

│  │

│  ├─ FC_STEM_Ring_Order

│  ├─ FC_STEM_Ring_Nesting

│  ├─ FC_STEM_Ring_Stop

│  ├─ FC_STEM_Collapse_Limit

│  ├─ FC_STEM_Deploy_Limit

│  ├─ FC_STEM_Staged_Collapse

│  ├─ FC_STEM_Shock_Absorption

│  ├─ FC_STEM_Load_Distribution

│  ├─ FC_STEM_Descent_Control

│  └─ FC_STEM_Emergency_Stop

│

├─ 03.13_STEM_TRANSPORT

│  │

│  ├─ FC_STEM_Transport

│  ├─ FC_STEM_Walkway

│  ├─ FC_STEM_Vertical_Transport

│  ├─ FC_STEM_Service_Path

│  ├─ FC_STEM_Flower_Access

│  ├─ FC_STEM_Root_Access

│  ├─ FC_STEM_Pressure_Transition

│  ├─ FC_STEM_Pressure_Lock

│  ├─ FC_STEM_Emergency_Access

│  ├─ FC_STEM_Occupancy_Control

│  └─ FC_STEM_Depth_Restriction

│

│

├─ 03.14_RING_CONNECTION

│  │

│  ├─ FC_STEM_Ring_Connection

│  │  ├─ Connection_ID

│  │  ├─ Source_Ring_ID

│  │  ├─ Target_Ring_ID

│  │  ├─ Connected \[bool\]

│  │  ├─ Extend_Amount

│  │  └─ Lock_State

│  │

│  ├─ FC_Ring_Port

│  ├─ FC_Ring_Bridge

│  ├─ FC_Ring_Bridge_Extend

│  ├─ FC_Ring_Bridge_Retract

│  ├─ FC_Ring_Port_Align

│  ├─ FC_Ring_Port_Lock

│  ├─ FC_Ring_Port_Seal

│  └─ FC_Ring_Emergency_Disconnect

│

│

├─ 03.15_FLOWER_STEM_CONNECTION

│  ├─ FC_Flower_Stem_Port

│  ├─ FC_Flower_Stem_Transition

│  ├─ FC_Flower_Stem_Transport

│  ├─ FC_Flower_Stem_Structure

│  └─ FC_Flower_Stem_Seal

│

│

├─ 03.16_ROOT_SYSTEM

│  │

│  ├─ FC_Root

│  ├─ FC_Root_Core

│  ├─ FC_Root_Branch

│  ├─ FC_Root_Anchor

│  ├─ FC_Root_Energy_Storage

│  ├─ FC_Root_Power_Distribution

│  ├─ FC_Root_Logistics_Hub

│  ├─ FC_Root_Cargo_Transfer

│  ├─ FC_Root_Transport

│  ├─ FC_Root_Service

│  ├─ FC_Root_Maintenance

│  ├─ FC_Root_Emergency

│  ├─ FC_Root_Transition

│  └─ FC_Root_To_Stem

│

│
```
