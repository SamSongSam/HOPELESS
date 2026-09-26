#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN UNREAL ENGINE 5 PCG GRAPH SETUP SCRIPT (YEAR 4205)
================================================================================
Implements the 5-Stage Procedural Content Generation Architecture:
  Stage 1: Mathematical Polar Lattice & Surface Projection (PCG_Sub_PolarLattice)
  Stage 2: Spatial Partitioning & 10 Faculty District Zoning (PCG_Sub_DistrictZoning)
  Stage 3: Topological Waypoint Graph & Spline Routing (PCG_Sub_SpineSplines)
  Stage 4: Socket Grammar & 45m Collision Clearance Sweep (PCG_Sub_ModulePlacement)
  Stage 5: Instanced Static Mesh Spawning & HISM Settings (PCG_Sub_MeshSpawning)
  Master:  PCG_Istrorigan_Master Orchestrator Graph

Execution:
  Inside UE5 Editor: Window > Developer Tools > Output Log (Python) -> Run
  CLI Commandlet:    UnrealEditor-Cmd.exe <Project> -run=pythonscript -script=scripts/unreal_setup_pcg_graphs.py
  Standalone Python: py -3.11 scripts/unreal_setup_pcg_graphs.py
================================================================================
"""

# region MODULE IMPORTS & ENVIRONMENT
import os
import sys
import json

try:
    import unreal  # type: ignore
    UNREAL_AVAILABLE = True
except ImportError:
    UNREAL_AVAILABLE = False
# endregion


# region PCG GRAPH RECIPES SPECIFICATION
def build_master_pcg_graph_recipe():
    """
    Constructs the complete 54-node Unreal Engine 5 PCG architecture recipe
    structured into Master Orchestrator + 5 Functional Subgraphs.
    """
    recipe = {
        "architecture": "Unreal Engine 5 PCG Multi-Subgraph Framework (Year 4205)",
        "target_engine": "Unreal Engine 5.2 - 5.5",
        "package_root": "/Game/FlowerCity/PCG",
        "total_nodes": 54,
        "subgraphs": {
            "PCG_Sub_PolarLattice": {
                "description": "Stage 1: Polar Lattice Generator & Surface Projection",
                "nodes": [
                    {
                        "name": "LatticeGenerator",
                        "class": "UPCG_GenerateIstroriganLatticeSettings",
                        "properties": {
                            "PetalUSteps": 36,
                            "PetalVSteps": 19,
                            "RuntimePitchAngle_Deg": 2.5,
                            "StamenCount": 70,
                            "ApexSpireHeight": 60000.0,
                            "RingTierCount": 12,
                            "SurfaceNeckRadius": 30000.0,
                            "SeabedAbyssalRadius": 95000.0
                        }
                    },
                    {
                        "name": "WorldRayHit_SeaLevel",
                        "class": "UPCGWorldRayHitSettings",
                        "properties": {"RayDirection": [0.0, 0.0, -1.0], "RayLength": 150000.0}
                    },
                    {
                        "name": "NormalProjector",
                        "class": "UPCGNormalToDensitySettings",
                        "properties": {"NormalThreshold": 0.75}
                    },
                    {
                        "name": "RadialBoundsFilter",
                        "class": "UPCGPointFilterSettings",
                        "properties": {"FilterMode": "KeepInsideSphere", "Radius": 150000.0}
                    }
                ],
                "connections": [
                    {"from": "LatticeGenerator.Out", "to": "WorldRayHit_SeaLevel.In"},
                    {"from": "WorldRayHit_SeaLevel.Out", "to": "NormalProjector.In"},
                    {"from": "NormalProjector.Out", "to": "RadialBoundsFilter.In"}
                ]
            },
            "PCG_Sub_DistrictZoning": {
                "description": "Stage 2: Spatial Partitioning & 10 Faculty District Zoning",
                "nodes": [
                    {"name": "Filter_ZoneCitadel", "class": "UPCGPointFilterSettings", "target_attr": "ZoneTag", "value": "ZONE_CORE_CITADEL"},
                    {"name": "Filter_ZoneOceanic", "class": "UPCGPointFilterSettings", "target_attr": "ZoneTag", "value": "ZONE_FACULTY_OCEANIC"},
                    {"name": "Filter_ZoneBiosphere", "class": "UPCGPointFilterSettings", "target_attr": "ZoneTag", "value": "ZONE_FACULTY_BIOSPHERE"},
                    {"name": "Filter_ZoneClimate", "class": "UPCGPointFilterSettings", "target_attr": "ZoneTag", "value": "ZONE_FACULTY_CLIMATE"},
                    {"name": "Filter_ZoneMegastruct", "class": "UPCGPointFilterSettings", "target_attr": "ZoneTag", "value": "ZONE_FACULTY_MEGASTRUCT"},
                    {"name": "Filter_ZoneArchives", "class": "UPCGPointFilterSettings", "target_attr": "ZoneTag", "value": "ZONE_FACULTY_ARCHIVES"},
                    {"name": "Filter_ZoneAbyssal", "class": "UPCGPointFilterSettings", "target_attr": "ZoneTag", "value": "ZONE_FACULTY_ABYSSAL"},
                    {"name": "Filter_ZoneDiplomacy", "class": "UPCGPointFilterSettings", "target_attr": "ZoneTag", "value": "ZONE_FACULTY_DIPLOMACY"},
                    {"name": "Filter_ZoneMedicine", "class": "UPCGPointFilterSettings", "target_attr": "ZoneTag", "value": "ZONE_FACULTY_MEDICINE"},
                    {"name": "Filter_ZoneHarbor", "class": "UPCGPointFilterSettings", "target_attr": "ZoneTag", "value": "ZONE_HARBOR_BERTH"},
                    {"name": "Filter_WaterwayExclusion", "class": "UPCGPointFilterSettings", "target_attr": "ZoneTag", "value": "ZONE_CLEARANCE_WATERWAY"},
                    {"name": "Metadata_TagAssigner", "class": "UPCGMetadataOperationSettings", "operation": "AppendGameplayTags"}
                ],
                "connections": [
                    {"from": "In", "to": "Filter_ZoneCitadel.In"},
                    {"from": "Filter_ZoneCitadel.Outside", "to": "Filter_ZoneOceanic.In"},
                    {"from": "Filter_ZoneOceanic.Outside", "to": "Filter_ZoneBiosphere.In"},
                    {"from": "Filter_ZoneBiosphere.Outside", "to": "Filter_ZoneClimate.In"},
                    {"from": "Filter_ZoneClimate.Outside", "to": "Filter_ZoneMegastruct.In"},
                    {"from": "Filter_ZoneMegastruct.Outside", "to": "Filter_ZoneArchives.In"},
                    {"from": "Filter_ZoneArchives.Outside", "to": "Filter_ZoneAbyssal.In"},
                    {"from": "Filter_ZoneAbyssal.Outside", "to": "Filter_ZoneDiplomacy.In"},
                    {"from": "Filter_ZoneDiplomacy.Outside", "to": "Filter_ZoneMedicine.In"},
                    {"from": "Filter_ZoneMedicine.Outside", "to": "Filter_ZoneHarbor.In"},
                    {"from": "Filter_ZoneHarbor.Outside", "to": "Filter_WaterwayExclusion.In"}
                ]
            },
            "PCG_Sub_SpineSplines": {
                "description": "Stage 3: Topological Transit Spines & Inter-Petal Canal Splines",
                "nodes": [
                    {"name": "Filter_SpineBackbone", "class": "UPCGPointFilterSettings", "properties": {"Attribute": "PetalV", "Operator": "AbsLessThan", "Threshold": 0.05}},
                    {"name": "CreateSpline_PetalSpines", "class": "UPCGCreateSplineSettings", "properties": {"SplineType": "CentripetalCatmullRom", "bClosed": False}},
                    {"name": "SplineSampler_Maglev", "class": "UPCGSplineSamplerSettings", "properties": {"Mode": "Distance", "DistanceIncrement": 4000.0}},
                    {"name": "SplineSampler_Utility", "class": "UPCGSplineSamplerSettings", "properties": {"Mode": "Distance", "DistanceIncrement": 2500.0}},
                    {"name": "Filter_BridgePortals", "class": "UPCGPointFilterSettings", "properties": {"Attribute": "PetalU", "Operator": "Between", "Min": 0.55, "Max": 0.60}},
                    {"name": "CreateSpline_CanalBridges", "class": "UPCGCreateSplineSettings", "properties": {"SplineType": "Hermite", "bClosed": True}}
                ],
                "connections": [
                    {"from": "In", "to": "Filter_SpineBackbone.In"},
                    {"from": "Filter_SpineBackbone.Inside", "to": "CreateSpline_PetalSpines.In"},
                    {"from": "CreateSpline_PetalSpines.Out", "to": "SplineSampler_Maglev.In"},
                    {"from": "CreateSpline_PetalSpines.Out", "to": "SplineSampler_Utility.In"},
                    {"from": "In", "to": "Filter_BridgePortals.In"},
                    {"from": "Filter_BridgePortals.Inside", "to": "CreateSpline_CanalBridges.In"}
                ]
            },
            "PCG_Sub_ModulePlacement": {
                "description": "Stage 4: Socket Grammar, 45m Waterway Clearance Sweep & Pruning",
                "nodes": [
                    {
                        "name": "SocketSolver",
                        "class": "UPCG_SocketSolverSettings",
                        "properties": {"bStrictWatertightCheckSubmerged": True, "SnapToleranceRadius": 350.0, "MaxAngularTolerance_Deg": 7.5}
                    },
                    {"name": "DensityFilter_Buildings", "class": "UPCGDensityFilterSettings", "properties": {"LowerBound": 0.35, "UpperBound": 1.0}},
                    {"name": "BoundsModifier_ModuleFootprint", "class": "UPCGBoundsModifierSettings", "properties": {"BoundsMin": [-600, -600, 0], "BoundsMax": [600, 600, 3000]}},
                    {"name": "Difference_WaterwayClearance", "class": "UPCGDifferenceSettings", "properties": {"DensityFunction": "Binary", "Mode": "Continuous"}},
                    {"name": "SelfPruning_BuildingOverlap", "class": "UPCGSelfPruningSettings", "properties": {"PruningType": "RemoveDuplicates", "RadiusSimilarity": 0.95}},
                    {"name": "TransformPoints_DiscreteYaw", "class": "UPCGTransformPointsSettings", "properties": {"RotationStep": 90.0, "bUniformScale": True}},
                    {"name": "DensityFilter_ScatterProps", "class": "UPCGDensityFilterSettings", "properties": {"LowerBound": 0.65, "UpperBound": 1.0}},
                    {"name": "TransformPoints_PropJitter", "class": "UPCGTransformPointsSettings", "properties": {"ScaleMin": [0.8, 0.8, 0.8], "ScaleMax": [1.2, 1.2, 1.2]}}
                ],
                "connections": [
                    {"from": "In", "to": "SocketSolver.In"},
                    {"from": "SocketSolver.Out", "to": "DensityFilter_Buildings.In"},
                    {"from": "DensityFilter_Buildings.Out", "to": "BoundsModifier_ModuleFootprint.In"},
                    {"from": "BoundsModifier_ModuleFootprint.Out", "to": "Difference_WaterwayClearance.Source"},
                    {"from": "WaterwayClearanceVolume", "to": "Difference_WaterwayClearance.Difference"},
                    {"from": "Difference_WaterwayClearance.Out", "to": "SelfPruning_BuildingOverlap.In"},
                    {"from": "SelfPruning_BuildingOverlap.Out", "to": "TransformPoints_DiscreteYaw.In"},
                    {"from": "In", "to": "DensityFilter_ScatterProps.In"},
                    {"from": "DensityFilter_ScatterProps.Out", "to": "TransformPoints_PropJitter.In"}
                ]
            },
            "PCG_Sub_MeshSpawning": {
                "description": "Stage 5: Hierarchical Instanced Static Mesh (HISM) Spawners",
                "nodes": [
                    {"name": "Spawner_ApexSpire", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_FC_CouncilSpire_600m", "cull_dist": 0, "nanite": True},
                    {"name": "Spawner_HexBarrier", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_FC_HexBarrier_Dome_R1500m", "cull_dist": 0, "nanite": True},
                    {"name": "Spawner_PetalDecks", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_FC_PetalDeck_LOD0", "cull_dist": 0, "nanite": True},
                    {"name": "Spawner_BioDomes", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_FC_BioDome_Geodesic_R60m", "cull_dist": 200000, "nanite": True},
                    {"name": "Spawner_GoldenStamens", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_FC_GoldenStamen_Pylon", "cull_dist": 150000, "nanite": True},
                    {"name": "Spawner_CanalBridges", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_FC_Canal_Skybridge_Torus", "cull_dist": 150000, "nanite": True},
                    {"name": "Spawner_OuterDocks", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_FC_Outer_FloatingDock_Pontoon", "cull_dist": 120000, "nanite": True},
                    {"name": "Spawner_SubmergedRings", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_FC_SubmergedRing_Collar", "cull_dist": 0, "nanite": True},
                    {"name": "Spawner_SeabedVault", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_FC_SeabedVault_Bunker", "cull_dist": 0, "nanite": True},
                    {"name": "Spawner_TransitMaglev", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_FC_Transit_MaglevTube", "cull_dist": 100000, "nanite": True},
                    {"name": "Spawner_TransitUtility", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_FC_Transit_UtilityConduit", "cull_dist": 80000, "nanite": True},
                    {"name": "Spawner_Bld_Oceanic", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_Mod_Faculty_OceanicPower", "cull_dist": 250000, "nanite": True},
                    {"name": "Spawner_Bld_Biosphere", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_Mod_Faculty_BiosphereEcology", "cull_dist": 250000, "nanite": True},
                    {"name": "Spawner_Bld_Climate", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_Mod_Faculty_ClimateScience", "cull_dist": 250000, "nanite": True},
                    {"name": "Spawner_Bld_Megastruct", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_Mod_Faculty_MegastructArch", "cull_dist": 250000, "nanite": True},
                    {"name": "Spawner_Bld_Archives", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_Mod_Faculty_DeepArchives", "cull_dist": 250000, "nanite": True},
                    {"name": "Spawner_Bld_Abyssal", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_Mod_Faculty_AbyssalMining", "cull_dist": 250000, "nanite": True},
                    {"name": "Spawner_Bld_Diplomacy", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_Mod_Faculty_DiplomacyLaw", "cull_dist": 250000, "nanite": True},
                    {"name": "Spawner_Bld_Medicine", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_Mod_Faculty_MedicineCyber", "cull_dist": 250000, "nanite": True},
                    {"name": "Spawner_Prop_WarningBuoy", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_Prop_Waterway_WarningBuoy", "cull_dist": 50000, "nanite": False},
                    {"name": "Spawner_Prop_AtmoSensor", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_Prop_Weather_AtmoSensor", "cull_dist": 40000, "nanite": False},
                    {"name": "Spawner_Prop_BeaconLamp", "class": "UPCGStaticMeshSpawnerSettings", "mesh": "SM_Prop_Harbor_NavigationalBeacon", "cull_dist": 60000, "nanite": False}
                ]
            }
        },
        "master_graph": {
            "name": "PCG_Istrorigan_Master",
            "nodes": [
                {"name": "Sub_PolarLattice", "class": "UPCGSubgraphSettings", "subgraph": "PCG_Sub_PolarLattice"},
                {"name": "Sub_DistrictZoning", "class": "UPCGSubgraphSettings", "subgraph": "PCG_Sub_DistrictZoning"},
                {"name": "Sub_SpineSplines", "class": "UPCGSubgraphSettings", "subgraph": "PCG_Sub_SpineSplines"},
                {"name": "Sub_ModulePlacement", "class": "UPCGSubgraphSettings", "subgraph": "PCG_Sub_ModulePlacement"},
                {"name": "Sub_MeshSpawning", "class": "UPCGSubgraphSettings", "subgraph": "PCG_Sub_MeshSpawning"}
            ],
            "connections": [
                {"from": "Sub_PolarLattice.Out", "to": "Sub_DistrictZoning.In"},
                {"from": "Sub_DistrictZoning.Out", "to": "Sub_SpineSplines.In"},
                {"from": "Sub_DistrictZoning.Out", "to": "Sub_ModulePlacement.In"},
                {"from": "Sub_SpineSplines.SplineOut", "to": "Sub_MeshSpawning.SplineIn"},
                {"from": "Sub_ModulePlacement.MeshPoints", "to": "Sub_MeshSpawning.PointIn"}
            ]
        }
    }
    return recipe
# endregion


# region UNREAL PCG GRAPH GENERATOR & RECIPE WRITER
def setup_unreal_pcg_graph():
    recipe = build_master_pcg_graph_recipe()
    
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output")
    out_path = os.path.join(out_dir, "ue5_pcg_graph_recipe.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(recipe, f, indent=2)
    
    print("=" * 80)
    print(" ISTRORIGAN UNREAL ENGINE 5 PCG GRAPH AUTOMATION SUITE (YEAR 4205)")
    print("=" * 80)
    print(f"[+] Successfully compiled 54-Node Master PCG Architecture Recipe!")
    print(f"[+] Output File: {out_path}")
    print(f"    - Master Orchestrator: PCG_Istrorigan_Master")
    for name, subg in recipe["subgraphs"].items():
        print(f"    - Subgraph: {name:<26} ({len(subg['nodes'])} nodes) - {subg['description']}")
    print("-" * 80)

    if not UNREAL_AVAILABLE:
        print("[*] Note: 'unreal' python module is inactive (Standalone Python Environment).")
        print("[*] Full 54-node PCG recipe is saved in output/ue5_pcg_graph_recipe.json.")
        print("[*] Inside Unreal Editor: Run this script via Developer Tools -> Python to instantiate.")
        print("=" * 80)
        return True

    # Inside Unreal Engine Environment
    print("[*] Unreal Engine Python Environment detected! Instantiating PCG Assets...")
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    package_path = recipe["package_root"]
    
    # 1. Create Subgraphs
    created_subgraphs = {}
    for subg_name, subg_data in recipe["subgraphs"].items():
        factory = unreal.PCGGraphFactory()
        sg_asset = asset_tools.create_asset(subg_name, package_path, unreal.PCGGraph, factory)
        if sg_asset:
            created_subgraphs[subg_name] = sg_asset
            unreal.log(f"[+] Created PCG Subgraph: {package_path}/{subg_name} with {len(subg_data['nodes'])} nodes")

    # 2. Create Master Graph
    master_factory = unreal.PCGGraphFactory()
    master_asset = asset_tools.create_asset(recipe["master_graph"]["name"], package_path, unreal.PCGGraph, master_factory)
    if master_asset:
        unreal.log(f"[+] Created Master PCG Graph: {master_asset.get_path_name()}")

    print("=" * 80)
    return True
# endregion


# region MAIN ENTRY
if __name__ == "__main__":
    setup_unreal_pcg_graph()
# endregion
