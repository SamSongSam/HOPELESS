#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN MEGASTRUCTURE - MASTER PIPELINE RUNNER (YEAR 4205)
================================================================================
One-click master pipeline execution:
1. Procedural Point Lattice Generator (istrorigan_pcg_generator.py)
2. Transit & Resource Flow Graph Solver (transit_resource_graph_solver.py)
3. Modular Kit-of-Parts Building Assembler (modular_building_assembler.py)
4. Zone Micro-Scatter & Prop Generator (zone_scatter_generator.py)
5. Skeletal Joint Rig & Hydraulic Animator (istrorigan_rig_animator.py)
6. 3D Hexagonal Barrier Dome Generator (hex_barrier_dome_generator.py)
7. Game-Ready Nanite & Draw Call Performance Auditor (game_ready_budget_auditor.py)
8. Unreal Engine 5 PCG Graph Automation Setup (unreal_setup_pcg_graphs.py)
9. Automated Codebase & Region Verification Suite (verify_codebase.py)
================================================================================
Usage:
    py scripts/run_all_pipelines.py
================================================================================
"""

# region MODULE IMPORTS & STAGES CONFIG
import os
import sys
import subprocess
import time

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

PIPELINE = [
    ("Point Lattice Generator", "istrorigan_pcg_generator.py"),
    ("Transit & Resource Graph Solver", "transit_resource_graph_solver.py"),
    ("Modular Building Assembler", "modular_building_assembler.py"),
    ("Zone Micro-Scatter Generator", "zone_scatter_generator.py"),
    ("Modular Parts 3D OBJ Exporter", "export_modular_parts_obj.py"),
    ("3D Flower City OBJ Exporter", "export_istrorigan_obj.py"),
    ("Skeletal Rig & Hydraulic Animator", "istrorigan_rig_animator.py"),
    ("3D Hex Barrier Dome Generator", "hex_barrier_dome_generator.py"),
    ("Performance & Budget Auditor", "game_ready_budget_auditor.py"),
    ("UE5 PCG Graph Automation", "unreal_setup_pcg_graphs.py"),
    ("Houdini Master Megastructure Compiler", "run_houdini_istrorigan.py"),
    ("Subsystem Blueprints & CAD Generator", "generate_subsystem_blueprints.py"),
    ("Master Anatomy Infographic Generator", "generate_infographic_breakdown.py"),
    ("Codebase Verification Suite", "verify_codebase.py")
]
# endregion


# region PIPELINE EXECUTION ENGINE
def run_pipeline():
    start_time = time.time()
    print("================================================================================")
    print(" EXECUTING ISTRORIGAN COMPLETE MEGASTRUCTURE PIPELINE (YEAR 4205)")
    print("================================================================================")
    
    success_count = 0
    python_cmd = "py"
    hython_cmd = r"D:\HODUINI\Houdini 22.0.429\bin\hython.exe"

    for step_num, (name, script_file) in enumerate(PIPELINE, 1):
        script_path = os.path.join(SCRIPTS_DIR, script_file)
        print(f"\n[{step_num}/{len(PIPELINE)}] >>> Running {name} ({script_file})...")
        if script_file == "run_houdini_istrorigan.py":
            if os.path.exists(hython_cmd):
                cmd = [hython_cmd, script_path, "save"]
            else:
                print("      [SKIP] Hython executable not found, skipping Houdini compilation.")
                success_count += 1
                continue
        else:
            cmd = [python_cmd, script_path]

        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(SCRIPTS_DIR))
        
        if result.returncode == 0:
            print(f"      [OK] {name} completed successfully.")
            for line in result.stdout.strip().split("\n")[-4:]:
                print(f"           {line}")
            success_count += 1
        else:
            print(f"      [ERROR] {name} failed with code {result.returncode}!")
            print(result.stderr)
            break

    elapsed = time.time() - start_time
    print("\n================================================================================")
    if success_count == len(PIPELINE):
        print(f"[+] ALL {len(PIPELINE)} PIPELINE STAGES EXECUTED PERFECTLY in {elapsed:.2f}s!")
        print("[+] Generated Outputs in output/:")
        out_dir = os.path.join(os.path.dirname(SCRIPTS_DIR), "output")
        for f in os.listdir(out_dir):
            size = os.path.getsize(os.path.join(out_dir, f))
            print(f"    - {f:<38} ({size:,.0f} bytes)")
    else:
        print(f"[!] Pipeline terminated with failures ({success_count}/{len(PIPELINE)} passed).")
    print("================================================================================")
    return 0 if success_count == len(PIPELINE) else 1
# endregion


# region MAIN ENTRY
if __name__ == "__main__":
    sys.exit(run_pipeline())
# endregion
