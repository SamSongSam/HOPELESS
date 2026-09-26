# 02_RADIAL_GRID_MATH - Lotus Flower Morphology & Radial Mathematics

> **Reference Script:** ถอดรหัสอัลกอริทึมจาก [`lotus_flower_regioned.py`](file:///d:/2/OWN/HOPELESS/lotus_flower_regioned.py) สำหรับจำลองกายวิภาค **ดอกบัวหลวง (Sacred Lotus - Nelumbo nucifera)** ให้เป็นเมืองขนาดมหึมา (Megastructure)

---

# region LOTUS MORPHOLOGY & ANATOMY

กายวิภาคของดอกบัวหลวงในเชิงสถาปัตยกรรมประกอบด้วย 3 องค์ประกอบหลัก:

1. **Receptacle (ฝักบัวแกนกลาง)**: 
   - ฐานทรงกรวยคว่ำ (Inverted Cone) ปลายตัดแบน ด้านบนเป็นลานจอด/ศูนย์ควบคุม มีหลุมเมล็ดบัว (`seedCount` ~ 20-30 จุด) ทำหน้าที่เป็นโดมสังเกตการณ์
2. **Stamens (วงแหวนเกสรเรืองแสง)**: 
   - เสาพลังงานสูงเรียงล้อมรอบฝักบัวแกนกลาง 70-120 ต้น ทำหน้าที่ปล่อยม่านพลังงานและเป็นเสาเชื่อมต่อเครือข่าย
3. **Whorls of Petals (ชั้นกลีบดอกบัวซ้อนสลับ)**: 
   - กลีบดอกบัวไม่ได้แผ่เป็นระนาบชั้นเดียว แต่ซ้อนกันเป็น **Whorls (3-5 ชั้น)**
   - กลีบแต่ละชั้นจะสลับหว่างกัน (**Shingling / Interlocking**) โดยกลีบชั้นนอกจะอยู่ตรงช่องว่างระหว่างกลีบของชั้นในเสมอ
   - กลีบทรงท้องเรือ/ช้อน (Cupped & Keeled) โค้งโอบอุ้มพื้นที่อยู่อาศัยและโดมชีวภาพไว้ภายใน

# endregion LOTUS MORPHOLOGY & ANATOMY

---

# region WHORLS & SHINGLING INTERLOCK MATH

สูตรคำนวณการเรียงตัวของชั้นกลีบดอกบัว (Whorl Interlocking) จาก `lotus_flower_regioned.py`:

```c
// =========================================================================
// WHORL INTERLOCK & ROTATION CALCULATION (VEX / C++)
// =========================================================================
int whorls = 4;                 // จำนวนชั้นกลีบ (เช่น 4 ชั้น)
int baseCount = 5;              // จำนวนกลีบในชั้นในสุด
int increment = 3;              // กลีบที่เพิ่มขึ้นในแต่ละชั้นถัดไป (5, 8, 11, 14)
float whorlTwist = 1.0;         // 1.0 = สลับหว่างกึ่งกลางพอดี (Shingled)
float whorlLift = 0.30;         // อัตราการยกระดับความสูงชั้นในให้สูงกว่าชั้นนอก
float bloom = 0.70;             // 0.0 = ดอกตูม (Bud), 0.7 = บานสวยงาม (Open), 1.3 = บานสะพรั่ง

for (int w = 0; w < whorls; w++) 
{
    float wt = float(w) / float(whorls - 1); // 0.0 (ในสุด) ถึง 1.0 (นอกสุด)
    int count = baseCount + increment * w;
    float slotAngle = (2.0 * M_PI) / float(count);
    float halfSlot = slotAngle * 0.5;

    // สลับมุมของชั้นคู่/คี่ เพื่อให้กลีบเหลื่อมสลับช่องว่างกันเหมือนดอกบัวจริง
    float phase = (w % 2 == 0) ? 0.0 : (halfSlot * whorlTwist);

    // มุมกางของกลีบ: ชั้นนอกสุดจะบานกว้าง (66 องศา) ชั้นในสุดจะตั้งชัน (16 องศา)
    float innerPitch = radians(16.0);
    float outerPitch = radians(66.0);
    float openPitch = lerp(innerPitch, outerPitch, wt);
    float pitch = lerp(radians(8.0), openPitch, bloom);

    // ฐานชั้นในยกตัวสูงกว่าชั้นนอก (Whorl Step-up)
    float z_lift = whorlLift * float(whorls - 1 - w) * petalLength;

    for (int i = 0; i < count; i++) 
    {
        float azimuth = phase + slotAngle * float(i);
        // Transform Petal Module at (azimuth, pitch, z_lift)
    }
}
```

# endregion WHORLS & SHINGLING INTERLOCK MATH

---

# region PETAL MORPHOLOGY & BENDING VEX

การดัดรูปทรงกลีบดอกบัวให้เป็นทรงท้องเรือ (Cupped) และมีสันแกนกลาง (Midrib Keel):

```c
// =========================================================================
// PETAL SHAPE & CUPPED BENDING (VEX WRANGLE)
// =========================================================================
// u = [0, 1] ตามแนวขวาง, v = [0, 1] ตามแนวยาวจากโคนสู่ปลาย
float u = f@pu;
float v = f@pv;

float L = chf("petalLength");
float W = chf("petalWidth"); // สัดส่วนดอกบัวจริง ยาว:กว้าง ~ 1.8:1
float wp = 1.20;             // Width Profile (>1 = ปลายแหลมเรียว)
float sk = 0.92;             // จุดป่องกว้างสุดค่อนไปทางกลางค่อนปลาย
float bn = 0.30;             // โคนกลีบคอดเข้า (Base Narrow)
float ts = 0.28;             // ปลายกลีบเรียวหยดน้ำ

// 1. คำนวณความกว้างตามโครงสร้างจริงของกลีบบัว
float vs = pow(v, sk);
float prof = pow(sin(M_PI * vs), wp);
prof *= lerp(bn, 1.0, smooth(0.0, 0.30, v));
prof *= lerp(1.0, 1.0 - ts, smooth(0.55, 1.0, v));

// 2. การดัดโค้งเป็นทรงช้อน/เรือ (Cup & Keel)
float cx = 2.0 * (u - 0.5);  // -1 (ซ้าย) ถึง +1 (ขวา)
float lp = sin(M_PI * v);

float cup = 0.20;    // ความเว้าก้นช้อน
float midrib = 0.12; // สันคมแกนกลางกลีบ
@P.z += cup * (cx * cx) * lp * 0.5;
@P.z -= midrib * (1.0 - abs(cx)) * pow(lp, 0.6) * 0.12;

// 3. การดัดโค้งปลายกลีบ (Tip Curl)
float curveD = 15.0; // องศาโค้งตามยาว
float curlD = 7.0;   // ปลายงอนิดๆ
float k = radians(curveD) / L;
float a = k * @P.y + radians(curlD) * pow(smooth(0.55, 1.0, v), 2.0);
```

# endregion PETAL MORPHOLOGY & BENDING VEX

---

# region RECEPTACLE & STAMENS ARCHITECTURE

### 1. Receptacle (ฝักบัวแกนกลาง)
* ทรงกระบอกกรวยหงาย (Inverted Frustum Cone):
  * เส้นผ่านศูนย์กลางฐานล่าง: $150\text{ m}$
  * เส้นผ่านศูนย์กลางลานบน: $220\text{ m}$
  * ความสูง: $90\text{ m}$
* ด้านบนเจาะช่องรูปเบ้าเมล็ดบัว (Seed Pod Depressions) 22 จุด สำหรับเป็นสถานีเทียบอากาศยานและสกายโดม

### 2. Stamen Energy Towers (วงแหวนเกสรดอกบัว)
* เสาสนามพลังและท่อส่งประจุ 70 ต้น เรียงตัวเป็นวงกลมรัศมี $120\text{ m}$ ล้อมรอบฝักบัว
* ความสูงเสา: $45\text{ m}$ เรืองแสงสีทองอำพัน (`#FDB822` / `RGB: 0.98, 0.85, 0.22`)
* ทำหน้าที่ปล่อยสนามพลังกั้นคลื่นลมและเป็นสายส่งไฟฟ้าไร้สายสู่กลีบดอกบัว

# endregion RECEPTACLE & STAMENS ARCHITECTURE

---

# region COLOR GRADIENT & BIOLUMINESCENCE

การเกลี่ยสีของกลีบดอกบัวหลวง (Nelumbo nucifera Color Profile):

* **Petal Base (โคนกลีบ)**: ขาวนวล/ครีมงาช้าง (`RGB: 0.99, 0.96, 0.88` / `#FDFAF0`)
* **Petal Tip (ปลายกลีบและขอบใบ)**: ชมพูดอกบัวสะพรั่ง (`RGB: 0.95, 0.52, 0.68` / `#F284AD`)
* **Falloff Exponent**: $1.7$ (การไล่โทนสีชมพูจะเข้มขึ้นชัดเจนช่วง $40\%$ สุดท้ายสู่ปลายกลีบ)
* **Night Mode**: ขอบสีชมพูจะสลับเป็นเส้นใยนำแสงไฟเรืองแสงสีชมพู-ม่วง พร้อมไฟสีทองส่องขึ้นจากฝักบัวแกนกลาง

# endregion COLOR GRADIENT & BIOLUMINESCENCE
