"""
================================================================================
 ISTRORIGAN PROCEDURAL SYSTEM - ROOT LAUNCHER
================================================================================
 Quick launcher for the Houdini Master Pipeline.
 Run:
   hython scripts/run_houdini_istrorigan.py [save]
 Or inside Houdini Python Source Editor:
   exec(open(r"<project>/scripts/run_houdini_istrorigan.py").read())
================================================================================
"""

# region ENVIRONMENT SETUP & MODULE RESOLUTION
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HOUDINI_MODULES_DIR = os.path.join(SCRIPT_DIR, "houdini")

for p in (SCRIPT_DIR, HOUDINI_MODULES_DIR):
    if p not in sys.path:
        sys.path.insert(0, p)

from houdini.build_istrorigan_master import build_master_istrorigan_system
# endregion


# region LAUNCHER EXECUTION
if __name__ == "__main__":
    save_hip = "save" in sys.argv
    build_master_istrorigan_system(save_hip=save_hip)
# endregion

