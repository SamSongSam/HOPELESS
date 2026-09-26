# DT_Asset_Archetypes - Istrorigan Module Catalog (Year 4205)

## World Canon & Purpose
แคตตาล็อกโมดูลสถาปัตยกรรมและโครงสร้างสำหรับมหานคร **ISTRORIGAN** ศูนย์รวมวิทยาลัยและภูมิปัญญาหนึ่งเดียวของโลกหลังมหาอุทกภัย 17 รัฐ:
- **Central Governance & Barrier**: หอคอยสภาสูง 10 คน และเสากำเนิดม่านบาเรียพลังงานรังผึ้ง 70 ต้น
- **8-Petal Academic Quads**: อัฒจันทร์บรรยายกลางแจ้ง (Tiered Amphitheaters), อาคารสภาย่อย 8 คณะ, โดมชีววิทยา, และหอสมุดสากล
- **Submerged Expanding Cradle**: วงแหวนข้อปล้องไฮดรอลิกถ่วงน้ำหนักสำหรับการดำน้ำปีละ 2 ครั้ง
- **Abyssal Doomsday Vault**: คลังเซิร์ฟเวอร์สำรองข้อมูลมนุษยชาติและธนาคารดีเอ็นเอชีวภาพก้นสมุทร

---

## 1. Master Archetype Catalog Table

| Archetype ID | Display Name | Size Class | Footprint Extent (W x L x H cm) | Mass (Tons) | Buoyancy (kN) | Pressure (Bar) | Base Weight | Permitted Zones |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `ARCH_CORE_COUNCIL_TEN_SPIRE` | Central Spire Citadel of Council of Ten | MegaStructure | 8000 x 8000 x 18000 | 85,000 | 0 | 10 | 100 | `Zone.Core` |
| `ARCH_CORE_HINGE_BRACKET` | Petal Articulation Hydraulic Hinge | Large | 2400 x 3600 x 1500 | 12,000 | +5,000 | 30 | 100 | `Zone.Core, Zone.Petal.Inner` |
| `ARCH_CORE_PLAZA_PLATFORM`| Grand Central Faculty Assembly Plaza | Large | 4000 x 4000 x 800 | 4,500 | +12,000 | 5 | 150 | `Zone.Core` |
| `ARCH_ACADEMIC_AMPHITHEATER`| Tiered Open-Air Lecture Amphitheater | Large | 3500 x 3500 x 800 | 3,800 | +18,000 | 5 | 120 | `Zone.Petal.Mid` |
| `ARCH_PETAL_SUBCOUNCIL_HALL`| Faculty Sub-Council Administration Hall | Medium | 2400 x 3000 x 1200 | 2,200 | +14,000 | 8 | 100 | `Zone.Petal.Mid` |
| `ARCH_HAB_DOMELUX_A` | Botanical Research & Living Bio-Dome | Large | 3000 x 3000 x 1800 | 1,800 | +28,000 | 3 | 80 | `Zone.Petal.Mid` |
| `ARCH_HAB_DOME_COMPACT_B` | High-Density International Scholar Dome | Medium | 1800 x 1800 x 1200 | 1,200 | +18,000 | 8 | 120 | `Zone.Petal.Mid` |
| `ARCH_HAB_MODULAR_APARTMENT`| Stepped Terrace Faculty Living Block | Medium | 1200 x 2400 x 900 | 950 | +14,000 | 5 | 200 | `Zone.Petal.Mid` |
| `ARCH_HYDRO_BIOFARM_A` | Vertical Oceanic Hydroponics Facility | Medium | 1500 x 3000 x 1200 | 800 | +16,000 | 2 | 100 | `Zone.Petal.Mid` |
| `ARCH_COMM_MARKET_POD` | 17-State Public Exchange & Commons Pod | Small | 600 x 1200 x 450 | 250 | +4,500 | 3 | 160 | `Zone.Petal.Mid, Zone.Shore` |
| `ARCH_TRANS_MAGLEV_STATION` | Petal Spine Maglev Interchange Terminal | Large | 2400 x 6000 x 1200 | 3,200 | +20,000 | 15 | 90 | `Zone.Petal.Inner, Zone.Petal.Mid` |
| `ARCH_TRANS_MAGLEV_TUBE` | Spine Maglev Enclosed Tube Segment | Medium | 600 x 4000 x 600 | 450 | +6,000 | 20 | 300 | `Zone.Petal.Inner, Zone.Petal.Mid` |
| `ARCH_TRANS_SKYWALK_CORRIDOR`| Glazed Campus Promenade Skywalk | Small | 400 x 2000 x 350 | 120 | +2,200 | 5 | 250 | `Zone.Petal.Mid` |
| `ARCH_HARBOR_DOCK_HEAVY` | Public Ferry & Research Vessel Sea Berth | Large | 3500 x 8000 x 1200 | 8,500 | +45,000 | 15 | 80 | `Zone.Petal.Tip, Zone.Shore` |
| `ARCH_HARBOR_DRONE_PAD` | Meteorological & Academic Drone Port | Small | 800 x 800 x 400 | 180 | +3,000 | 5 | 140 | `Zone.Petal.Tip` |
| `ARCH_BARRIER_PYLON_TOWER` | Golden Stamen Forcefield Barrier Pylon | Medium | 1000 x 1000 x 4500 | 2,800 | +15,000 | 25 | 100 | `Zone.Core, Zone.Petal.Inner` |
| `ARCH_SUB_RESEARCH_DOME` | Reinforced Abyssal Marine Research Dome | Medium | 2000 x 2000 x 1600 | 6,500 | +8,000 | 120 | 90 | `Zone.Stem, Zone.Petal.Mid` |
| `ARCH_SUB_DOCKING_AIRLOCK` | Submersible Research Submarine Airlock | Large | 2500 x 4500 x 1800 | 9,000 | +12,000 | 150 | 70 | `Zone.Stem` |
| `ARCH_STEM_BALLAST_CHAMBER`| Hydraulic Trim Ballast Pod (Bi-Annual Dive)| Large | 5000 x 5000 x 4000 | 45,000 | -25,000 | 180 | 100 | `Zone.Stem` |
| `ARCH_STEM_ELEVATOR_SHAFT` | Deep-Sea Vertical Academic Lift Column | Large | 2000 x 2000 x 10000| 18,000 | -5,000 | 200 | 150 | `Zone.Stem` |
| `ARCH_STEM_GEOTHERMAL_CORE`| Abyssal Siphon Geothermal Thermal Core | Large | 3500 x 3500 x 3000 | 22,000 | -15,000 | 250 | 60 | `Zone.Stem` |
| `ARCH_DOOMSDAY_VAULT_CHAMBER`| Doomsday Knowledge Vault & Gene Bank | MegaStructure | 6000 x 6000 x 3500 | 65,000 | -45,000 | 350 | 100 | `Zone.Root` |
| `ARCH_ROOT_SEABED_CLAW` | Hydraulic Bedrock Claw Ridge Anchor | MegaStructure | 6000 x 9000 x 5000 | 110,000| -85,000 | 350 | 100 | `Zone.Root` |

---

## 2. Unreal Engine 5 Import JSON (`DT_Asset_Archetypes.json`)

```json
[
  {
    "Name": "ARCH_CORE_COUNCIL_TEN_SPIRE",
    "ArchetypeID": "ARCH_CORE_COUNCIL_TEN_SPIRE",
    "DisplayName": "Central Spire Citadel of Council of Ten",
    "SizeClass": "EFC_ModuleSizeClass::MegaStructure",
    "FootprintExtent": { "X": 8000.0, "Y": 8000.0, "Z": 18000.0 },
    "StructuralMass_Tons": 85000.0,
    "BuoyancyForce_kN": 0.0,
    "PressureRating_Bar": 10.0,
    "BaseSpawnWeight": 100.0,
    "MinInstancesPerPetal": 0,
    "MaxInstancesPerPetal": 1,
    "MaterialProfileTag": { "TagName": "Material.Surface.TitaniumCeramic" }
  },
  {
    "Name": "ARCH_ACADEMIC_AMPHITHEATER",
    "ArchetypeID": "ARCH_ACADEMIC_AMPHITHEATER",
    "DisplayName": "Tiered Open-Air Lecture Amphitheater",
    "SizeClass": "EFC_ModuleSizeClass::Large",
    "FootprintExtent": { "X": 3500.0, "Y": 3500.0, "Z": 800.0 },
    "StructuralMass_Tons": 3800.0,
    "BuoyancyForce_kN": 18000.0,
    "PressureRating_Bar": 5.0,
    "BaseSpawnWeight": 120.0,
    "MinInstancesPerPetal": 1,
    "MaxInstancesPerPetal": 2,
    "MaterialProfileTag": { "TagName": "Material.Surface.CompositeShell" }
  },
  {
    "Name": "ARCH_PETAL_SUBCOUNCIL_HALL",
    "ArchetypeID": "ARCH_PETAL_SUBCOUNCIL_HALL",
    "DisplayName": "Faculty Sub-Council Administration Hall",
    "SizeClass": "EFC_ModuleSizeClass::Medium",
    "FootprintExtent": { "X": 2400.0, "Y": 3000.0, "Z": 1200.0 },
    "StructuralMass_Tons": 2200.0,
    "BuoyancyForce_kN": 14000.0,
    "PressureRating_Bar": 8.0,
    "BaseSpawnWeight": 100.0,
    "MinInstancesPerPetal": 1,
    "MaxInstancesPerPetal": 1,
    "MaterialProfileTag": { "TagName": "Material.Surface.CivicMarble" }
  },
  {
    "Name": "ARCH_BARRIER_PYLON_TOWER",
    "ArchetypeID": "ARCH_BARRIER_PYLON_TOWER",
    "DisplayName": "Golden Stamen Forcefield Barrier Pylon",
    "SizeClass": "EFC_ModuleSizeClass::Medium",
    "FootprintExtent": { "X": 1000.0, "Y": 1000.0, "Z": 4500.0 },
    "StructuralMass_Tons": 2800.0,
    "BuoyancyForce_kN": 15000.0,
    "PressureRating_Bar": 25.0,
    "BaseSpawnWeight": 100.0,
    "MinInstancesPerPetal": 2,
    "MaxInstancesPerPetal": 8,
    "MaterialProfileTag": { "TagName": "Material.Surface.GoldenEnergyConduit" }
  },
  {
    "Name": "ARCH_HAB_DOMELUX_A",
    "ArchetypeID": "ARCH_HAB_DOMELUX_A",
    "DisplayName": "Botanical Research & Living Bio-Dome",
    "SizeClass": "EFC_ModuleSizeClass::Large",
    "FootprintExtent": { "X": 3000.0, "Y": 3000.0, "Z": 1800.0 },
    "StructuralMass_Tons": 1800.0,
    "BuoyancyForce_kN": 28000.0,
    "PressureRating_Bar": 3.0,
    "BaseSpawnWeight": 80.0,
    "MinInstancesPerPetal": 1,
    "MaxInstancesPerPetal": 4,
    "MaterialProfileTag": { "TagName": "Material.Surface.SmartGlass" }
  },
  {
    "Name": "ARCH_TRANS_MAGLEV_STATION",
    "ArchetypeID": "ARCH_TRANS_MAGLEV_STATION",
    "DisplayName": "Petal Spine Maglev Interchange Terminal",
    "SizeClass": "EFC_ModuleSizeClass::Large",
    "FootprintExtent": { "X": 2400.0, "Y": 6000.0, "Z": 1200.0 },
    "StructuralMass_Tons": 3200.0,
    "BuoyancyForce_kN": 20000.0,
    "PressureRating_Bar": 15.0,
    "BaseSpawnWeight": 90.0,
    "MinInstancesPerPetal": 1,
    "MaxInstancesPerPetal": 2,
    "MaterialProfileTag": { "TagName": "Material.Surface.CarbonWeave" }
  },
  {
    "Name": "ARCH_HARBOR_DOCK_HEAVY",
    "ArchetypeID": "ARCH_HARBOR_DOCK_HEAVY",
    "DisplayName": "Public Ferry & Research Vessel Sea Berth",
    "SizeClass": "EFC_ModuleSizeClass::Large",
    "FootprintExtent": { "X": 3500.0, "Y": 8000.0, "Z": 1200.0 },
    "StructuralMass_Tons": 8500.0,
    "BuoyancyForce_kN": 45000.0,
    "PressureRating_Bar": 15.0,
    "BaseSpawnWeight": 80.0,
    "MinInstancesPerPetal": 1,
    "MaxInstancesPerPetal": 2,
    "MaterialProfileTag": { "TagName": "Material.Shore.AntiFouling" }
  },
  {
    "Name": "ARCH_STEM_BALLAST_CHAMBER",
    "ArchetypeID": "ARCH_STEM_BALLAST_CHAMBER",
    "DisplayName": "Hydraulic Trim Ballast Pod (Bi-Annual Dive)",
    "SizeClass": "EFC_ModuleSizeClass::Large",
    "FootprintExtent": { "X": 5000.0, "Y": 5000.0, "Z": 4000.0 },
    "StructuralMass_Tons": 45000.0,
    "BuoyancyForce_kN": -25000.0,
    "PressureRating_Bar": 180.0,
    "BaseSpawnWeight": 100.0,
    "MinInstancesPerPetal": 0,
    "MaxInstancesPerPetal": 4,
    "MaterialProfileTag": { "TagName": "Material.Submerged.CorrodedAlloy" }
  },
  {
    "Name": "ARCH_DOOMSDAY_VAULT_CHAMBER",
    "ArchetypeID": "ARCH_DOOMSDAY_VAULT_CHAMBER",
    "DisplayName": "Doomsday Knowledge Vault & Gene Bank",
    "SizeClass": "EFC_ModuleSizeClass::MegaStructure",
    "FootprintExtent": { "X": 6000.0, "Y": 6000.0, "Z": 3500.0 },
    "StructuralMass_Tons": 65000.0,
    "BuoyancyForce_kN": -45000.0,
    "PressureRating_Bar": 350.0,
    "BaseSpawnWeight": 100.0,
    "MinInstancesPerPetal": 0,
    "MaxInstancesPerPetal": 1,
    "MaterialProfileTag": { "TagName": "Material.Abyssal.CathodicArmored" }
  },
  {
    "Name": "ARCH_ROOT_SEABED_CLAW",
    "ArchetypeID": "ARCH_ROOT_SEABED_CLAW",
    "DisplayName": "Hydraulic Bedrock Claw Ridge Anchor",
    "SizeClass": "EFC_ModuleSizeClass::MegaStructure",
    "FootprintExtent": { "X": 6000.0, "Y": 9000.0, "Z": 5000.0 },
    "StructuralMass_Tons": 110000.0,
    "BuoyancyForce_kN": -85000.0,
    "PressureRating_Bar": 350.0,
    "BaseSpawnWeight": 100.0,
    "MinInstancesPerPetal": 0,
    "MaxInstancesPerPetal": 1,
    "MaterialProfileTag": { "TagName": "Material.Abyssal.CathodicArmored" }
  }
]
```
