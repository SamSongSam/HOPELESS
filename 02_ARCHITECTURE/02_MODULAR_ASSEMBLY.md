# 02_ARCHITECTURE - Modular Building Assemblies

## Purpose & PCG Implementation
ระบบสถาปัตยกรรมแบบแยกส่วน (Kit-of-Parts Modular System) สำหรับการประกอบอาคารบนกลีบดอกไม้และแกนกลาง:
- **FC_Building_Base**: โครงสร้างฐานรากรับน้ำหนักและปรับระดับระนาบตามความเอียงของกลีบ
- **FC_Facade**: ชิ้นส่วนผนังภายนอก รองรับรูปแบบปกติและแบบกันแรงดันน้ำ (Pressure-Proof)
- **FC_Roof**: หลังคาแบบแบน, โดมชีวภาพ (Bio-Dome), และจุดลงจอดโดรน
- **FC_Window & FC_Door**: บานหน้าต่าง/ประตู รวมถึงประตูผนึกกันน้ำเข้า (Watertight Air-lock Doors)
- **FC_Modular_Assembly**: กฎการนำชิ้นส่วนมาประกอบเข้าด้วยกัน (Wave Function Collapse / Socket Grammar)

---

## Parameter Tree

```text
02_ARCHITECTURE

├─ FC_Building_Base

├─ FC_Facade

├─ FC_Roof

├─ FC_Window

├─ FC_Door

└─ FC_Modular_Assembly

03_FLOWER_MEGASTRUCTURE
│
```

---

## Modular Snapping Guidelines
1. **Grid Unit Dimensions**: กำหนดโมดูลมาตรฐานที่ $400 	imes 400 	imes 300	ext{ cm}$ (กว้าง $	imes$ ยาว $	imes$ สูง)
2. **Floor Height Step**: แต่ละชั้นสูง $300	ext{ cm}$ หรือ $600	ext{ cm}$ (Double-height Lobby)
3. **Curved Petal Compensation**: โมดูลฐานราก (`FC_Building_Base`) ต้องมี Slope Compensation Parameter ($pm 15^circ$) เพื่อให้พื้นอาคารภายในได้ระดับระนาบแนวนอนเสมอแม้กลีบจะเอียง
