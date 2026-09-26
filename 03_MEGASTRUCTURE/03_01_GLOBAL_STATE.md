# 03.01_FLOWER_GLOBAL_STATE - Istrorigan Global State Machine

## World Canon & Purpose (Era: 4205)
ศูนย์กลางสถานะสากลของมหานคร **ISTRORIGAN (อิสโตรริแกน)** มหานครแห่งการศึกษาและภูมิปัญญาหนึ่งเดียวของโลกหลังมหาอุทกภัย 17 รัฐ:
- **Council of Ten Governance**: การควบคุมสถานะเมืองตามมติของ **สภาสูง 10 คน**
- **Annual Submersion Cycle**: วัฏจักรการดำน้ำลงสู่ใต้ทะเลปีละ 2 ครั้งเพื่อการศึกษาและวิจัยใต้สมุทรลึก
- **Planetary Barrier Shield**: การกางม่านพลังงานโดมรังผึ้งเพื่อคุ้มกันความเป็นกลางและปกป้องเมืองจากพายุคลื่นยักษ์
- **Dynamic State Distributor**: ระบบกระจายสัญญาณคำสั่งสู่ทั้ง 8 กลีบวิทยาเขต และวงแหวนข้อปล้องใต้น้ำ

---

## 1. Parameter Tree

```text
03.01_FLOWER_GLOBAL_STATE

├─ FC_Istrorigan_Global_State
│  ├─ City_Epoch_Year [int: 4205]
│  ├─ Council_Ten_Quorum_Active [bool]
│  ├─ Council_Ten_Directive_ID [int]
│  ├─ Council_Ten_Emergency_Override [bool]
│  │
│  ├─ Open_State [bool]
│  ├─ Open_Amount [float 0–1]
│  ├─ Trade_Assembly_State [bool]
│  │
│  ├─ Barrier_Hex_Dome_Active [bool]
│  ├─ Barrier_Energy_Load [float 0–1]
│  ├─ Barrier_Neutral_Zone_Enforcement [bool]
│  │
│  ├─ Submerge_State [bool]
│  ├─ Submerge_Amount [float 0–1]
│  ├─ Deep_Sea_Mode [bool]
│  ├─ Emergency_State [bool]
│  │
│  ├─ Annual_Cycle_State [enum: 0=Surface_Spring, 1=Summer_Solstice_Dive, 2=Autumn_Diplomacy, 3=Winter_Equinox_Dive]
│  ├─ Current_Submersion_Depth_Meters [float]
│  │
│  ├─ Previous_Global_State
│  ├─ Current_Global_State
│  └─ Target_Global_State
│
└─ FC_Flower_State_Distributor
   ├─ Structure_State
   │  └─ Petal (8 Faculties) / Zone / Shore / Stem (Expanding Rings) / Root (Doomsday Vault) / Center (Council Spire)
   │
   ├─ Protection_State
   │  └─ Barrier Network / 70 Golden Pylons / Shield Emitter Core
   │
   ├─ Operation_State
   │  └─ 8-Petal Transit / Public Access / Academic Scheduling
   │
   ├─ Submerge_State
   │  └─ Ballast Chamber Pumping / Hydraulic Telescoping / Watertight Bulkhead Seals
   │
   └─ Emergency_State
      └─ Independent Petal Isolation / Evacuation Routing to Core Bunker
```

---

## 2. รายละเอียดสถานะหลัก (State Definitions)

### 2.1 วัฏจักรการดำน้ำปีละ 2 ครั้ง (`Annual_Cycle_State`)
| ค่า State | ชื่อโหมด | ช่วงเวลา | กิจกรรมหลัก | ระดับความลึก Z |
| :---: | :--- | :--- | :--- | :---: |
| `0` | `Surface_Spring_Semester` | เดือน 1–5 | ภาคการศึกษาผิวน้ำ, การเรียนการสอนทั่วไป, ท่าเรือเปิดรับเรือจาก 17 รัฐ | ผิวน้ำ ($Z = 0$) |
| `1` | `Summer_Solstice_Submersion` | เดือน 6 | **มหาฤดูกาลดำน้ำรอบที่ 1:** ศึกษาระบบนิเวศน์ทางทะเลลึก และแพลงก์ตอนเรืองแสง | $-500\text{ m}$ |
| `2` | `Autumn_Diplomatic_Assembly` | เดือน 7–11 | การประชุมสภา 17 รัฐ, มหกรรมวิชาการระดับโลก, และแลกเปลี่ยนเทคโนโลยี | ผิวน้ำ ($Z = 0$) |
| `3` | `Winter_Equinox_Abyssal_Submersion` | เดือน 12 | **มหาฤดูกาลดำน้ำรอบที่ 2:** ศึกษาธรณีฟิสิกส์ก้นสมุทร, ซ้อมรอดชีวิตใต้น้ำ 100% | $-1,000\text{ m}$ |

### 2.2 ม่านบาเรียพลังงานรังผึ้ง (`Barrier_Hex_Dome_Active`)
* **Normal Mode:** กางคลุมทั้งเมืองเพื่อกรองรังสี กั้นฝนกรด และปรับสภาพอากาศภายในให้เหมาะสมกับการเรียนรู้
* **Storm Shield Mode:** เมื่อคลื่นยักษ์สึนามิหรือมรสุมเข้าใกล้ บาเรียจะเร่งความเข้มข้นสูงสุดเพื่อสลายพลังงานคลื่น
* **Neutral Zone Enforcement:** สกัดกั้นอาวุธ เรือรบ หรือโดรนที่ไม่ได้รับอนุญาตจากสภา 10 คนโดยเด็ดขาด
* **Hydrostatic Mode (ตอนดำน้ำ):** แปรเปลี่ยนความถี่เป็นม่านปรับสมดุลแรงดันน้ำ ช่วยผ่อนแรงกดของมวลน้ำมหาศาลบนโดมกระจก

### 2.3 สิทธิอำนาจสภาสูง 10 คน (`Council_Ten_Quorum_Active`)
* การเปลี่ยนสถานะระดับเมือง (เช่น สั่งเริ่มดำน้ำ หรือเปิดโหมดฉุกเฉิน) ต้องได้รับคะแนนเสียงอย่างน้อย **7 ใน 10 เสียง**
* ในกรณีวิกฤติตัวเมืองถูกโจมตี ระบบจะตัดเข้าสู่ `Council_Ten_Emergency_Override = true` เพื่อผนึกกลีบและดำน้ำทันทีโดยอัตโนมัติ
