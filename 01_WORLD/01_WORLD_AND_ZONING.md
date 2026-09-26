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

| District ID | Zone Name | Ring Tier | Radial Distance | Allowed Functions | Density Falloff |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `DIST_CORE` | Central Spire Hub | Tier 0 | 0 – 150m | Administration, Master Power, Emergency Bunker | Center-Peak (Gaussian) |
| `DIST_PETAL_BASE` | Hinge & Transit Interchange | Tier 1 | 150 – 350m | Heavy Maglev Stations, Transfer Plazas, Cargo Terminals | Linear High |
| `DIST_PETAL_MID` | High-Density Living / Domes | Tier 2 | 350 – 750m | Residential Domes, Hydroponics, Commercial Plazas | Uniform High |
| `DIST_PETAL_TIP` | Observation & Outpost | Tier 3 | 750 – 1100m | Harbors, Drone Launchpads, Defense Pylons | Edge-Peak |
| `DIST_STEM_COLUMN` | Engineering Subsurface | Tier -1 | 0 – 100m (Down) | Ballast Control, Geothermal Power, Submarine Docks | Axial Symmetrical |
| `DIST_ROOT_ANCHOR` | Abyssal Seabed Anchor | Tier -2 | Seabed Level | Hydraulic Claws, Deep Trench Mining, Anchor Cables | Ground Anchored |
