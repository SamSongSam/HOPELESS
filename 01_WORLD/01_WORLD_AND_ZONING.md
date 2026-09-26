# 01_WORLD - World & District Spatial Zoning

## Purpose & PCG Implementation
นิยามการแบ่งสรรพื้นที่โลก (World Partitioning), สภาพภูมิประเทศเทียม (Megastructure Deck Terrain), โครงข่ายถนนหลัก (Road/Path Network), และแปลงที่ดินสำหรับสิ่งปลูกสร้าง (Districts & Plots)

---

## Parameter Tree

```text
01_WORLD

├─ FC_Terrain

├─ FC_Road

├─ FC_Path

├─ FC_District

└─ FC_Plot
```

---

## PCG District Zoning Rules

| District ID | Zone Name | Ring Tier | Radial Distance | Allowed Functions & Urban Programming | Density Falloff |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `DIST_CORE` | Central Spire Hub & Solar Agora | Tier 0 | 0 – 150m | • **ลานกิจกรรม**: Grand Solar Agora, เวทีสภาสิบ, ลานพิธีการอธิการบดี<br>• **พื้นที่สาธารณะ**: Colonnade ทางเดินหินอ่อน, จัตุรัสพบปะสากล<br>• **การบริหาร**: บัญชาการกลาง, ชุมทางลิฟต์ดิ่ง 12 ราง, บังเกอร์นิรภัย | Center-Peak (Gaussian 2.5) |
| `DIST_PETAL_BASE` | Hinge, Transit & Proving Gate | Tier 1 | 150 – 350m | • **พื้นที่ทดลอง**: ศูนย์ทดสอบระบบขับเคลื่อนแม่เหล็ก, แล็บวิเคราะห์แรงเฉือนบานพับ<br>• **พื้นที่สาธารณะ**: ชานชาลาสถานี Maglev Interchange, จุดชมวิวร่องน้ำ 45m<br>• **โครงสร้างพื้นฐาน**: ประตูกั้นน้ำ 38m, เสาสนามพลังงาน 70 ต้น, ชุมทางขนส่งตู้คอนเทนเนอร์ | Linear High (1.8) |
| `DIST_PETAL_MID` | High-Density Living & Research Commons | Tier 2 | 350 – 750m | • **ที่อยู่อาศัย**: หอพักนักศึกษา Stepped Terraces 125,000 คน, แฟลตคณาจารย์, วิลล่าคณะทูต<br>• **ลานกิจกรรม**: อัฒจันทร์บรรยายกลางแจ้ง (3,500 ที่นั่ง/คณะ), ลานเวทีน้ำกลางแจ้ง<br>• **พื้นที่ทดลอง**: ห้องแล็บวิจัย 7,623 ชั้น, โรงเพาะพันธุ์พืชโดมชีวภาพ, แปลงวิจัยพันธุศาสตร์<br>• **พื้นที่สาธารณะ**: สวนพฤกษศาสตร์ Bio-Domes, ตลาดกลาง 17 รัฐ, สกายวอล์กทางเดินลอยฟ้า | Uniform High (1.2) |
| `DIST_PETAL_TIP` | Marine Testing, Harbors & Esplanades | Tier 3 | 750 – 1100m | • **พื้นที่ทดลอง**: แอ่งทดสอบคลื่นไฮโดรไดนามิกส์ในทะเลเปิด, แท่นทดสอบยานดำน้ำลึก, ลานทดสอบโดรนสภาพอากาศ<br>• **พื้นที่สาธารณะ**: ทางเดินเลียบสมุทร Esplanade 12 km, จุดชมพระอาทิตย์ตก 360 องศา, ลานกีฬาทางน้ำ<br>• **ลานกิจกรรม**: ท่าเรือเปิดลานคนเดินริมทะเล, เวทีประกวดเรือนวัตกรรม 17 รัฐ<br>• **ท่าเรือ**: ท่าเรือทุ่นลอย Canon Pontoon Docks, สถานีรับเรือวิจัยนานาชาติ | Edge-Peak (1.0) |
| `DIST_STEM_COLUMN` | Engineering Subsurface & Hyperbaric Labs | Tier -1 | 0 – 100m (Down) | • **พื้นที่ทดลอง**: แท็งก์จำลองแรงดันสมุทรลึก Hyperbaric Chamber (ทน 1,500 Bar), โรงไฟฟ้าความร้อนใต้พิภพต้นแบบ<br>• **ที่อยู่อาศัย**: แคปซูลพักผ่อนเจ้าหน้าที่กะดึกใต้น้ำ (Subsurface Engineering Bunks)<br>• **วิศวกรรม**: วงแหวนยืดหด 12 ชั้น, ถังอับเฉาปรับแรงลอยตัว 4.2M kN, กระบอกไฮดรอลิก 176 ชุด | Axial Symmetrical (1.5) |
| `DIST_ROOT_ANCHOR` | Abyssal Seabed Anchor & Deep Vault | Tier -2 | Seabed Level (-1000m) | • **พื้นที่ทดลอง**: แท่นขุดเจาะร่องสมุทรมาเรียนา, สถานีตรวจวัดแผ่นดินไหวใต้พิภพ, ปล่องเก็บความร้อนภูเขาไฟ<br>• **พื้นที่สาธารณะ**: หอจดหมายเหตุอารยธรรมมนุษย์ (Doomsday Vault Reading Room สำหรับนักวิจัยระดับสูง)<br>• **วิศวกรรม**: ก้ามปูหินไททาเนียม 8 ทิศ, คลังเก็บตัวอย่างพันธุกรรม DNA | Ground Anchored (2.0) |

---

## 4 ฟังก์ชันหลักในการจัดผังเมือง (4 Core Urban Typologies)

### 1. ลานกิจกรรม (Activity Plazas & Event Grounds)
- **Grand Solar Agora (Citadel Plaza)**: ลานพิธีการกลางรัศมี 150m จุคนได้ 60,000 คน ใช้ในพิธีวันครีษมายันและเปิดภาคเรียนสากล
- **Faculty Open-Air Amphitheaters**: อัฒจันทร์หินอ่อนรูปเกือกม้าประจำกลีบทั้ง 8 คณะ จุคณะละ 3,500 ที่นั่ง
- **Inter-Petal Water Stages**: เวทีลอยน้ำในร่องน้ำ 45 เมตร สำหรับการแสดงแสงสีเสียงและเทศกาลเรือนานาชาติ
- **Campus Maker Quads**: ลานแสดงผลงานสิ่งประดิษฐ์และนวัตกรรมหุ่นยนต์กลางแจ้ง

### 2. ที่อยู่อาศัย (Residential Housing & Living Quarters)
- **Stepped-Terrace Scholar Blocks (`ARCH_HAB_MODULAR_APARTMENT`)**: อาคารพักอาศัยบันไดขั้น 4-8 ชั้น พร้อมระเบียงปลูกผักไฮโดรโปนิกส์ส่วนตัว
- **Geodesic Biosphere Living Pods (`ARCH_HAB_DOME_COMPACT_B`)**: โดมพักอาศัยชีวภาพรวมระบบปิด ออกซิเจนหมุนเวียน 100%
- **Diplomatic Enclave Residences**: ที่พักตัวแทนทูตานุทูตและคณาจารย์ผู้ทรงคุณวุฒิจาก 17 มหารัฐ
- **Subsurface Quiet Bunks**: แคปซูลพักผ่อนเก็บเสียงสมบูรณ์แบบสำหรับทีมวิศวกรใต้น้ำในปล้อง Stem

### 3. พื้นที่ทดลอง (Experimental Proving Grounds & Living Labs)
- **Hyperbaric Trench Testing Tanks**: แท็งก์ทดสอบแรงดันน้ำลึก 1,500 Bar สำหรับทดสอบวัสดุและยานสำรวจใต้ทะเล
- **Open-Ocean Hydrodynamic Flumes**: แอ่งทดสอบคลื่นธรรมชาติและใบพัดขับเคลื่อนเรือไฮโดรฟอยล์ที่ปลายกลีบ
- **Extreme Weather Simulation Domes**: โดมจำลองพายุหมุนและฟ้าผ่าควบคุมเพื่อพัฒนาม่านบาเรีย
- **Abyssal Drill Rig Sites**: แท่นทดสอบการขุดเจาะแร่หายากบนพื้นผิวภูเขาไฟใต้ทะเลลึก -1,000m

### 4. พื้นที่สาธารณะ (Public Spaces, Waterfront Promenades & Parks)
- **Waterfront Esplanades**: ทางเดินเลียบขอบทะเลความยาวรวมกว่า 12 กิโลเมตร รอบขอบกลีบทั้ง 8 กลีบ
- **Botanical Bio-Parks**: สวนป่าดงดิบและพื้นที่ชุ่มน้ำชายเลนเทียมภายในโดมแก้วเพื่อการพักผ่อนของพลเมือง
- **Glazed Skywalk Network**: ทางเดินกระจกลอยฟ้าเชื่อมระหว่างอาคารและข้ามกลีบโดยไม่ต้องกลัวฝนหรือลมแรง
- **17-State Cultural Bazaar**: ลานตลาดแลกเปลี่ยนวัฒนธรรม สินค้าหัตถกรรม และอาหารพื้นเมืองจาก 17 มหารัฐ
