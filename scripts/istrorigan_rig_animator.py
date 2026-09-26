#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN PROCEDURAL RIGGING & SKELETAL ANIMATOR (YEAR 4205)
================================================================================
Implements 03_MEGASTRUCTURE/03_08_RIG_EXPORT_INTERFACE.md:
- Generates 3D Skeletal Bone Hierarchy for Istrorigan Megastructure:
    * Root_Master (0,0,0)
    * Citadel_Spire_Bone (Council of 10)
    * 8 Petal Hinge & Articulation Chains (Hinge -> Mid -> Tip)
    * 12 Submerged Telescopic Ring Piston Bones (Tier 1 -> Tier 12)
- Solves Keyframe Animation States:
    1. Surface Operations (Pitch = 2.5 deg, Rings Buoyant at Z=0m)
    2. Summer Solstice Dive (Pitch = 16.0 deg, Rings Flooded to -500m)
    3. Winter Solstice Dive (Pitch = 18.0 deg, Rings Telescoped to -1000m)
    4. Emergency Storm Shield (Pitch = 22.0 deg, Protective Cocoon)
- Exports Bone Hierarchy & Animation Track in JSON (compatible with Unreal Control Rig)
================================================================================
Usage:
    py scripts/istrorigan_rig_animator.py
Outputs:
    output/istrorigan_skeletal_rig.json
================================================================================
"""

import os
import sys
import math
import json

# region SKELETAL RIG DATA STRUCTURES
class Bone:
    def __init__(self, name, parent_name=None, bind_pos=(0.0, 0.0, 0.0), bind_rot=(0.0, 0.0, 0.0)):
        self.name = name
        self.parent_name = parent_name
        self.bind_pos = bind_pos # (x, y, z)
        self.bind_rot = bind_rot # (pitch, yaw, roll) in degrees
        self.keyframes = {}      # time_sec -> {"pos": (x,y,z), "rot": (pitch, yaw, roll)}

    def to_dict(self):
        return {
            "name": self.name,
            "parent": self.parent_name,
            "bind_pos": [round(v, 2) for v in self.bind_pos],
            "bind_rot": [round(v, 2) for v in self.bind_rot],
            "keyframes": {
                str(t): {
                    "pos": [round(v, 2) for v in kf["pos"]],
                    "rot": [round(v, 2) for v in kf["rot"]]
                }
                for t, kf in self.keyframes.items()
            }
        }
# endregion


# region BONE HIERARCHY & KEYFRAME SOLVER
def build_megastructure_rig():
    print("[*] Generating Megastructure Bone Hierarchy & Articulation Rig...")
    bones = {}

    # 1. Master Root & Citadel Spire
    bones["Root_Master"] = Bone("Root_Master", None, (0.0, 0.0, 0.0))
    bones["Citadel_Apex_Spire"] = Bone("Citadel_Apex_Spire", "Root_Master", (0.0, 0.0, 35000.0))

    # 2. 8 Petal Bone Chains (Centimeters: Base 15,000 cm, Mid 62,500 cm, Tip 110,000 cm)
    petal_count = 8
    base_r = 15000.0
    mid_r = 62500.0
    tip_r = 110000.0

    for p in range(petal_count):
        az_deg = p * (360.0 / petal_count)
        az_rad = math.radians(az_deg)
        cos_a, sin_a = math.cos(az_rad), math.sin(az_rad)

        hinge_name = f"Bone_Petal_Hinge_{p+1:02d}"
        mid_name = f"Bone_Petal_Mid_{p+1:02d}"
        tip_name = f"Bone_Petal_Tip_{p+1:02d}"

        # Bind poses (cm)
        bones[hinge_name] = Bone(hinge_name, "Root_Master", (base_r * cos_a, base_r * sin_a, 0.0), (0.0, az_deg, 0.0))
        bones[mid_name] = Bone(mid_name, hinge_name, ((mid_r - base_r) * cos_a, (mid_r - base_r) * sin_a, 2000.0), (0.0, az_deg, 0.0))
        bones[tip_name] = Bone(tip_name, mid_name, ((tip_r - mid_r) * cos_a, (tip_r - mid_r) * sin_a, -2000.0), (0.0, az_deg, 0.0))

    # 3. 12 Submerged Telescopic Ring Piston Bones (Down to -90,000 cm)
    bones["Stem_Collar"] = Bone("Stem_Collar", "Root_Master", (0.0, 0.0, -1000.0))
    parent_tier = "Stem_Collar"
    for tier in range(1, 13):
        tier_name = f"Bone_Submerged_Ring_Tier_{tier:02d}"
        bind_z = -7500.0 # Step down to -90,000 cm
        bones[tier_name] = Bone(tier_name, parent_tier, (0.0, 0.0, bind_z))
        parent_tier = tier_name

    # -------------------------------------------------------------------------
    # ANIMATION KEYFRAME GENERATION (Centimeters)
    # -------------------------------------------------------------------------
    print("[*] Generating Keyframe Animation Tracks (Surface -> Summer -> Winter -> Storm)...")
    anim_states = [
        {"time": 0.0, "desc": "Surface Operations", "pitch": 2.5, "depth_cm": 0.0},
        {"time": 5.0, "desc": "Summer Solstice Dive", "pitch": 16.0, "depth_cm": -50000.0},
        {"time": 10.0, "desc": "Winter Solstice Dive", "pitch": 18.0, "depth_cm": -90000.0},
        {"time": 15.0, "desc": "Emergency Storm Shield", "pitch": 22.0, "depth_cm": -10000.0},
    ]

    for state in anim_states:
        t = state["time"]
        pitch = state["pitch"]
        depth = state["depth_cm"]

        # Root vertical translation for dive
        bones["Root_Master"].keyframes[t] = {
            "pos": (0.0, 0.0, depth),
            "rot": (0.0, 0.0, 0.0)
        }
        bones["Citadel_Apex_Spire"].keyframes[t] = {
            "pos": (0.0, 0.0, 35000.0),
            "rot": (0.0, 0.0, 0.0)
        }

        # Petal hydraulic pitch
        for p in range(petal_count):
            az_deg = p * (360.0 / petal_count)
            hinge_name = f"Bone_Petal_Hinge_{p+1:02d}"
            mid_name = f"Bone_Petal_Mid_{p+1:02d}"
            tip_name = f"Bone_Petal_Tip_{p+1:02d}"

            bones[hinge_name].keyframes[t] = {
                "pos": bones[hinge_name].bind_pos,
                "rot": (pitch, az_deg, 0.0)
            }
            bones[mid_name].keyframes[t] = {
                "pos": bones[mid_name].bind_pos,
                "rot": (pitch * 0.85, az_deg, 0.0)
            }
            tip_pitch_mod = 0.0 if depth > -5000.0 else pitch * 0.70
            bones[tip_name].keyframes[t] = {
                "pos": bones[tip_name].bind_pos,
                "rot": (tip_pitch_mod, az_deg, 0.0)
            }

        # Telescopic rings extending
        for tier in range(1, 13):
            tier_name = f"Bone_Submerged_Ring_Tier_{tier:02d}"
            telescope_z = -7500.0 * (abs(depth) / 90000.0) if depth < 0.0 else -7500.0
            bones[tier_name].keyframes[t] = {
                "pos": (0.0, 0.0, telescope_z),
                "rot": (0.0, 0.0, 0.0)
            }

    print(f"[+] Skeletal Rig generated: {len(bones)} Bones with 4 Articulation States.")
    return bones
# endregion


# region RIG EXPORTER (JSON)
def export_rig(bones, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    json_path = os.path.join(output_dir, "istrorigan_skeletal_rig.json")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "rig_name": "Rig_Istrorigan_Megastructure_4205",
            "total_bones": len(bones),
            "bones": [b.to_dict() for b in bones.values()]
        }, f, indent=2)

    print(f"[+] Exported Skeletal Rig JSON: {json_path}")
# endregion


# region MAIN PIPELINE ENTRY POINT
def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root_dir, "output")
    bones = build_megastructure_rig()
    export_rig(bones, out_dir)


if __name__ == "__main__":
    main()
# endregion

