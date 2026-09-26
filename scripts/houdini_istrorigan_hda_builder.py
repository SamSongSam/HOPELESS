"""
================================================================================
 ISTRORIGAN MEGASTRUCTURE (YEAR 4205) - MODULAR ARCHITECTURE RUNNER
================================================================================
 ระบบได้ถูกแยกส่วน (Decoupled & Separated) ออกเป็นโมดูลเดี่ยวอย่างสมบูรณ์:
 
 1. ส่วนโมดูล Python แต่ละระบบ (Modular Python Subsystems):
    ├── scripts/houdini/part01_apex_spire.py       (Citadel & Spire)
    ├── scripts/houdini/part02_hex_barrier.py      (Hex Forcefield Dome)
    ├── scripts/houdini/part03_academic_petals.py  (8 Academic Petals)
    ├── scripts/houdini/part04_bio_domes.py        (Bio-Domes & Habitats)
    ├── scripts/houdini/part05_stamen_pylons.py    (70 Golden Stamens)
    ├── scripts/houdini/part06_canal_bridges.py    (Canal Skybridges)
    ├── scripts/houdini/part07_outer_docks.py      (Floating Marinas & Yachts)
    ├── scripts/houdini/part08_submerged_rings.py  (12 Deep Sea Rings & Tiers)
    └── scripts/houdini/part09_seabed_vault.py     (Doomsday Bedrock Vault)

 2. ไฟล์โค้ดคำนวณเรขาคณิต VEX แยกเฉพาะ (.vfl files with syntax highlighting):
    └── scripts/houdini/vex/*.vfl

 3. ตัวประสานระบบหลัก (Master Orchestrator):
    └── scripts/houdini/build_istrorigan_master.py

 รันไฟล์นี้จะเรียกใช้งานระบบแยกโมดูลทั้งหมดอัตโนมัติ โดยไม่เกิดความสับสนซ้ำซ้อน
================================================================================
"""

# region ENVIRONMENT & MODULE RESOLUTION
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HOUDINI_MODULES_DIR = os.path.join(SCRIPT_DIR, "houdini")

for p in (SCRIPT_DIR, HOUDINI_MODULES_DIR):
    if p not in sys.path:
        sys.path.insert(0, p)

from houdini.build_istrorigan_master import build_master_istrorigan_system
# endregion


# region RUNNER ENTRY POINT
def main():
    save_hip = "save" in sys.argv
    build_master_istrorigan_system(save_hip=save_hip)


if __name__ == "__main__":
    main()
# endregion

