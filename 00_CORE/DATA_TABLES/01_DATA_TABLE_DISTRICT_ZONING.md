# DT_District_Zoning - 17-State Global Academy Zoning Table

## World-Building Context
> **Setting:** โลกหลังมหาอุทกภัยน้ำท่วมใหญ่จนเหลือเพียง **17 มหารัฐ (17 Great States)** มหานครแห่งนี้จึงถูกสถาปนาขึ้นกลางมหาสมุทรสากลในฐานะ **"ศูนย์กลางการศึกษาและภูมิปัญญาเดียวของมนุษยชาติ"** ปกป้องด้วยม่านพลังงานบาเรียทรงโดม (Forcefield Barrier Dome) และมีกำหนดการดำน้ำลงสู่ใต้ทะเลปีละ 2 ครั้งเพื่อการศึกษาและวิจัยใต้สมุทรลึก

---

## 1. Zoning Allocation Table (8 Faculties + Core & Abyssal Base)

| Row Name | DistrictType | Zone Display Name | Petal / Sector | Radius (cm) | MinDepth / MaxElevation (cm) | Target Buoyancy (kN) | Allowed Modules & Purpose |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `ZONE_CORE_CITADEL` | `Core_Civic` | Grand Academic Citadel & Barrier Generator | Center Core | 0 – 15,000 | -10,000 to +35,000 | 0 (Anchor) | `Function.Academic.Citadel, System.BarrierGenerator` |
| `ZONE_FACULTY_OCEANIC` | `Petal_MidLiving` | Faculty of Oceanic Engineering & Power | Petal 0 | 15,000 – 110,000 | -5,000 to +6,000 | +35,000 | `Faculty.Engineering, Lab.Geothermal, Dock.Research` |
| `ZONE_FACULTY_BIOSPHERE`| `Petal_MidLiving` | Faculty of Biosphere & Marine Biology | Petal 1 | 15,000 – 110,000 | -5,000 to +6,000 | +35,000 | `Faculty.Biosphere, BioDome.Botanical, Lab.Hydroponic` |
| `ZONE_FACULTY_CLIMATE` | `Petal_MidLiving` | Faculty of Geo-Atmospheric Stabilization | Petal 2 | 15,000 – 110,000 | -5,000 to +6,000 | +35,000 | `Faculty.Atmospheric, Dome.WeatherObservation` |
| `ZONE_FACULTY_MEGASTRUCT`|`Petal_MidLiving`| Faculty of Floating Megastructure Civil Eng | Petal 3 | 15,000 – 110,000 | -5,000 to +6,000 | +35,000 | `Faculty.Architecture, Lab.Hydrodynamics` |
| `ZONE_FACULTY_ARCHIVES` | `Petal_MidLiving` | Grand Universal Library & Pre-Deluge Archives | Petal 4 | 15,000 – 110,000 | -5,000 to +6,000 | +35,000 | `Faculty.Humanities, Vault.Library, Amphitheater.Public` |
| `ZONE_FACULTY_ABYSSAL` | `Petal_MidLiving` | Faculty of Deep-Sea Mining & Trench Exploration| Petal 5 | 15,000 – 110,000 | -5,000 to +6,000 | +35,000 | `Faculty.AbyssalMining, Lab.PressureTesting` |
| `ZONE_FACULTY_DIPLOMACY`| `Petal_MidLiving` | 17-State Parliamentary Assembly & Living Campus| Petal 6 | 15,000 – 110,000 | -5,000 to +6,000 | +35,000 | `Council.17States, Campus.InternationalDorm` |
| `ZONE_FACULTY_MEDICINE` | `Petal_MidLiving` | Faculty of Oceanic Medicine & Genetics | Petal 7 | 15,000 – 110,000 | -5,000 to +6,000 | +35,000 | `Faculty.Medical, Lab.Genetics, Hospital.Public` |
| `ZONE_STEM_TELESCOPIC` | `Stem_Engineering`| Submerged Expanding Telescopic Rings Cradle | Stem (Down) | 8,000 – 35,000 | -90,000 to -1,000 | -80,000 (Ballast) | `Submerged.HydraulicCradle, Ballast.PumpingChamber` |
| `ZONE_ROOT_VAULT` | `Root_AbyssalAnchor`| Bedrock Anchor & Doomsday Knowledge Vault | Seabed | 0 – 50,000 | -250,000 to -90,000 | -150,000 (Anchor) | `Abyssal.BedrockClaws, Vault.DeepServerCores` |

---

## 2. Unreal Engine 5 Import JSON (`DT_District_Zoning.json`)

```json
[
  {
    "Name": "ZONE_CORE_CITADEL",
    "DistrictType": "EFC_DistrictZone::Core_Civic",
    "ZoneDisplayName": "Grand Academic Citadel & Barrier Generator",
    "RingTier": 0,
    "MinRadius": 0.0,
    "MaxRadius": 15000.0,
    "MinDepth_Z": -10000.0,
    "MaxElevation_Z": 35000.0,
    "TargetBuoyancy_kN": 0.0,
    "MaxBuildingHeight": 12000.0,
    "DensityFalloffExponent": 2.5,
    "AllowedModuleTags": {
      "GameplayTags": [
        { "TagName": "Zone.Core" },
        { "TagName": "Function.Academic.Citadel" },
        { "TagName": "System.BarrierGenerator" }
      ]
    }
  },
  {
    "Name": "ZONE_FACULTY_OCEANIC",
    "DistrictType": "EFC_DistrictZone::Petal_MidLiving",
    "ZoneDisplayName": "Faculty of Oceanic Engineering & Power",
    "RingTier": 2,
    "MinRadius": 15000.0,
    "MaxRadius": 110000.0,
    "MinDepth_Z": -5000.0,
    "MaxElevation_Z": 6000.0,
    "TargetBuoyancy_kN": 35000.0,
    "MaxBuildingHeight": 4500.0,
    "DensityFalloffExponent": 1.2,
    "AllowedModuleTags": {
      "GameplayTags": [
        { "TagName": "Zone.Petal.0" },
        { "TagName": "Faculty.Engineering" },
        { "TagName": "Lab.Geothermal" }
      ]
    }
  },
  {
    "Name": "ZONE_FACULTY_BIOSPHERE",
    "DistrictType": "EFC_DistrictZone::Petal_MidLiving",
    "ZoneDisplayName": "Faculty of Biosphere & Marine Biology",
    "RingTier": 2,
    "MinRadius": 15000.0,
    "MaxRadius": 110000.0,
    "MinDepth_Z": -5000.0,
    "MaxElevation_Z": 6000.0,
    "TargetBuoyancy_kN": 35000.0,
    "MaxBuildingHeight": 4500.0,
    "DensityFalloffExponent": 1.0,
    "AllowedModuleTags": {
      "GameplayTags": [
        { "TagName": "Zone.Petal.1" },
        { "TagName": "Faculty.Biosphere" },
        { "TagName": "BioDome.Botanical" }
      ]
    }
  },
  {
    "Name": "ZONE_FACULTY_ARCHIVES",
    "DistrictType": "EFC_DistrictZone::Petal_MidLiving",
    "ZoneDisplayName": "Grand Universal Library & Pre-Deluge Archives",
    "RingTier": 2,
    "MinRadius": 15000.0,
    "MaxRadius": 110000.0,
    "MinDepth_Z": -5000.0,
    "MaxElevation_Z": 6000.0,
    "TargetBuoyancy_kN": 35000.0,
    "MaxBuildingHeight": 5000.0,
    "DensityFalloffExponent": 1.1,
    "AllowedModuleTags": {
      "GameplayTags": [
        { "TagName": "Zone.Petal.4" },
        { "TagName": "Faculty.Humanities" },
        { "TagName": "Vault.Library" },
        { "TagName": "Amphitheater.Public" }
      ]
    }
  },
  {
    "Name": "ZONE_FACULTY_DIPLOMACY",
    "DistrictType": "EFC_DistrictZone::Petal_MidLiving",
    "ZoneDisplayName": "17-State Parliamentary Assembly & Living Campus",
    "RingTier": 2,
    "MinRadius": 15000.0,
    "MaxRadius": 110000.0,
    "MinDepth_Z": -5000.0,
    "MaxElevation_Z": 6000.0,
    "TargetBuoyancy_kN": 35000.0,
    "MaxBuildingHeight": 4000.0,
    "DensityFalloffExponent": 1.0,
    "AllowedModuleTags": {
      "GameplayTags": [
        { "TagName": "Zone.Petal.6" },
        { "TagName": "Council.17States" },
        { "TagName": "Campus.InternationalDorm" }
      ]
    }
  },
  {
    "Name": "ZONE_STEM_TELESCOPIC",
    "DistrictType": "EFC_DistrictZone::Stem_Engineering",
    "ZoneDisplayName": "Submerged Expanding Telescopic Rings Cradle",
    "RingTier": -1,
    "MinRadius": 8000.0,
    "MaxRadius": 35000.0,
    "MinDepth_Z": -90000.0,
    "MaxElevation_Z": -1000.0,
    "TargetBuoyancy_kN": -80000.0,
    "MaxBuildingHeight": 3000.0,
    "DensityFalloffExponent": 1.5,
    "AllowedModuleTags": {
      "GameplayTags": [
        { "TagName": "Zone.Stem" },
        { "TagName": "Submerged.HydraulicCradle" },
        { "TagName": "Ballast.PumpingChamber" }
      ]
    }
  },
  {
    "Name": "ZONE_ROOT_VAULT",
    "DistrictType": "EFC_DistrictZone::Root_AbyssalAnchor",
    "ZoneDisplayName": "Bedrock Anchor & Doomsday Knowledge Vault",
    "RingTier": -2,
    "MinRadius": 0.0,
    "MaxRadius": 50000.0,
    "MinDepth_Z": -250000.0,
    "MaxElevation_Z": -90000.0,
    "TargetBuoyancy_kN": -150000.0,
    "MaxBuildingHeight": 8000.0,
    "DensityFalloffExponent": 2.0,
    "AllowedModuleTags": {
      "GameplayTags": [
        { "TagName": "Zone.Root" },
        { "TagName": "Abyssal.BedrockClaws" },
        { "TagName": "Vault.DeepServerCores" }
      ]
    }
  }
]
```
