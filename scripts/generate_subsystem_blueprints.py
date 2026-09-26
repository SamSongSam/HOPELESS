#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
 ISTRORIGAN MEGASTRUCTURE - COMPLETE SUBSYSTEM BLUEPRINT & SPECIFICATION PACK
================================================================================
 Generates discrete, high-resolution CAD blueprint schematics, visual renders,
 and exhaustive technical metrology cards for all 17 canonical subsystems:
   01. Apex Spire & Citadel of Ten
   02. Hexagonal Forcefield Barrier Dome
   03. 8 Academic Faculty Petals (45m Waterways)
   04. Botanical Bio-Domes & Living Habitats
   05. 70 Golden Stamen Forcefield Energy Pylons
   06. 45m Inter-Petal Canal Skybridges
   07. Outer Floating Marina Docks & Pontoon Jetties
   08. 12 Submerged Expanding Inverted Ballast Rings
   09. Abyssal Doomsday Vault & Bedrock Claws (-1,000m)
   10. 3D Maglev & Evacuation Multi-Layer Transit Network
   11. Core-to-Stem Ring 1 Structural Interface Collar
   12. Inter-Ring Hydraulic Expansion Dampers & Couplers
   13. Vertical Deep-Sea Transit Elevator Core (1.1 km)
   14. Emergency Watertight Bulkhead Isolation Gates
   15. 8 Faculty Sub-Council Assembly Halls
   16. Modular Civic & Academic Buildings (7,623 Floors)
   17. Modular Residential Housing & International Scholar Dormitories
================================================================================
"""

# region MODULE IMPORTS & PATH CONFIG
import os
import sys
import shutil
import math

try:
    from PIL import Image, ImageDraw, ImageFont  # type: ignore
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_BLUEPRINTS_DIR = os.path.join(WORKSPACE_DIR, "output", "blueprints")
os.makedirs(OUTPUT_BLUEPRINTS_DIR, exist_ok=True)

BRAIN_DIR = r"C:\Users\User\.gemini\antigravity-ide\brain\a80dddaf-f6d8-4967-a3ed-7b8237079c57"
# endregion


# region AI GENERATED IMAGE HARVESTER
AI_RENDER_MAPPING = [
    ("blueprint_apex_spire", "AI_RENDER_01_APEX_SPIRE.jpg", "08_PRESENTATION/parts/01_SYS_APEX_SPIRE.jpg"),
    ("blueprint_hex_barrier", "AI_RENDER_02_HEX_BARRIER.jpg", "08_PRESENTATION/parts/02_SYS_HEX_BARRIER.jpg"),
    ("blueprint_petal_structure", "AI_RENDER_03_ACADEMIC_PETAL.jpg", "08_PRESENTATION/parts/03_SYS_ACADEMIC_PETALS.jpg"),
    ("blueprint_biodomes_habitats", "AI_RENDER_04_BIO_DOMES.jpg", "08_PRESENTATION/parts/04_SYS_BIO_DOMES.jpg"),
    ("blueprint_stamen_pylons", "AI_RENDER_05_STAMEN_PYLONS.jpg", "08_PRESENTATION/parts/05_SYS_STAMEN_PYLONS.jpg"),
    ("blueprint_canal_skybridges", "AI_RENDER_06_CANAL_SKYBRIDGES.jpg", "08_PRESENTATION/parts/06_SYS_INTER_PETAL_CANAL.jpg"),
    ("blueprint_floating_marina", "AI_RENDER_07_FLOATING_MARINA_DOCKS.jpg", "08_PRESENTATION/parts/07_SYS_DEEP_SEA_BERTH.jpg"),
    ("blueprint_submerged_stem", "AI_RENDER_08_SUBMERGED_STEM.jpg", "08_PRESENTATION/parts/08_SYS_SUBMERGED_STEM_RINGS.jpg"),
    ("blueprint_abyssal_vault", "AI_RENDER_09_ABYSSAL_VAULT.jpg", "08_PRESENTATION/parts/09_SYS_SEABED_DOOMSDAY_VAULT.jpg"),
    ("blueprint_transit_transport", "AI_RENDER_10_TRANSIT_TRANSPORT.jpg", None),
    ("blueprint_stem_collar", "AI_RENDER_11_CORE_STEM_COLLAR.jpg", "08_PRESENTATION/parts/08_SYS_SUBMERGED_STEM_RINGS.jpg"),
    ("blueprint_hydraulic_dampers", "AI_RENDER_12_HYDRAULIC_DAMPERS.jpg", "08_PRESENTATION/parts/08_SYS_SUBMERGED_STEM_RINGS.jpg"),
    ("blueprint_elevator_core", "AI_RENDER_13_DEEPSEA_ELEVATOR_CORE.jpg", None),
    ("blueprint_bulkhead_gates", "AI_RENDER_14_BULKHEAD_GATES.jpg", None),
    ("blueprint_subcouncil_hall", "AI_RENDER_15_SUBCOUNCIL_HALL.jpg", None),
    ("blueprint_modular_buildings", "AI_RENDER_16_MODULAR_BUILDINGS.jpg", None),
    ("blueprint_residential_housing", "AI_RENDER_17_RESIDENTIAL_HOUSING_DORMS.jpg", None),
]


def harvest_ai_renders():
    """Copies high-res AI generated blueprints into output/blueprints/."""
    copied = 0
    brain_files = os.listdir(BRAIN_DIR) if os.path.exists(BRAIN_DIR) else []

    for prefix, dest_name, fallback_rel in AI_RENDER_MAPPING:
        dst = os.path.join(OUTPUT_BLUEPRINTS_DIR, dest_name)
        matched = False

        if brain_files:
            matching = [f for f in brain_files if f.startswith(prefix) and f.endswith(".jpg")]
            if matching:
                latest = sorted(matching)[-1]
                src = os.path.join(BRAIN_DIR, latest)
                shutil.copy2(src, dst)
                copied += 1
                matched = True
                print(f"  [+] Harvested AI Blueprint: {dest_name} ({os.path.getsize(dst):,} bytes)")

        if not matched and fallback_rel:
            fb_path = os.path.join(WORKSPACE_DIR, fallback_rel.replace("/", os.sep))
            if os.path.exists(fb_path):
                shutil.copy2(fb_path, dst)
                copied += 1
                print(f"  [+] Harvested Fallback Blueprint: {dest_name} from {fallback_rel} ({os.path.getsize(dst):,} bytes)")

    return copied
# endregion


# region CANON SUBSYSTEM DATA DICTIONARY
SUBSYSTEM_SPECS = [
    {
        "id": "SYS_01",
        "num": "01",
        "canon": "03.02_FLOWER_CENTER",
        "name": "APEX SPIRE & CITADEL OF TEN",
        "elevation": "+600.0m Apex / +120.0m Podium Plaza",
        "radius": "Base Podium R=150.0m / Twin Blade Span: 70.0m",
        "material": "Graphene Composite / Reinforced Titanium Ivory Ceramic",
        "mass": "1,450,000 Metric Tons",
        "archetype": "ARCH_CORE_COUNCIL_TEN_SPIRE, ARCH_CORE_PLAZA_PLATFORM",
        "extent": "8000 x 8000 x 18000 cm (80m x 80m x 180m Base Spire)",
        "buoyancy": "0 kN (Central Rigid Megastructure Anchor)",
        "pressure": "10.0 Bar (Atmospheric & Hurricane Pressurized)",
        "zoning": "Zone.Core, Core_Civic, Function.Academic.Citadel, System.BarrierGenerator",
        "transit": "12-Track Express Maglev Chute direct to Abyssal Vault (-1,000m) in 2.5 mins",
        "residential": "Council Chambers & Executive Quarters for the 10 Supreme Regents",
        "features": [
            "Sculptural Twin-Blade Split Apex (+600m) with central energy void aperture",
            "Suspended Crown Observatory Chamber at +520m elevation",
            "Splaying organic root buttresses transferring structural wind/wave shear into base",
            "Houses Council of Ten Supreme Executive Assembly & Core Power Distributor",
            "High-speed vertical maglev elevator chute linking apex to abyssal vault"
        ],
        "sockets": ["Petal Roots (8x)", "Stem Collar (1x)", "Barrier Apex Emitter (1x)"],
        "states": "Surface: Open Assembly | Dive: Pressurized Lockdown | Emergency: Quorum Isolation"
    },
    {
        "id": "SYS_02",
        "num": "02",
        "canon": "03.10_PROTECTION_NETWORK",
        "name": "HEXAGONAL FORCEFIELD BARRIER DOME",
        "elevation": "+650.0m Apex Crown / 0.0m Sea Level Perimeter",
        "radius": "Outer Deflection Radius R=1,500.0m (Diameter 3,000m)",
        "material": "Photonic Plasma Deflection Lattice / Coherent Hex Shield Field",
        "mass": "Field Energy Load: 850 MegaWatts (Continuous Baseline)",
        "archetype": "System.BarrierGenerator, ARCH_BARRIER_HEX_DOME",
        "extent": "300000 x 300000 x 65000 cm (3,000m x 3,000m x 650m Dome)",
        "buoyancy": "Zero Mass / 3,000m Pressurized Air Volume Enclosure",
        "pressure": "50.0 Bar External Deflection Capacity",
        "zoning": "Zone.Barrier, Planetary Defense Grid, System.Protection",
        "transit": "Airway Flight Corridors through 6 Automated Frequency Gates",
        "residential": "Protects all 8 Faculty Campuses and 125,000 Citizen Residents",
        "features": [
            "Geodesic honeycomb hexagonal energy cells deflecting storms and heavy waves",
            "Neutral Zone enforcement: automated atmospheric defense perimeter",
            "Hydrostatic pressure stabilization mode during deep-sea submersion (-1,000m)",
            "Solar radiation filtering & microclimate atmospheric conditioning inside dome",
            "Variable energy dissipation grid linked to 70 Golden Stamen Pylons"
        ],
        "sockets": ["Central Apex Emitter", "70 Stamen Harmonic Anchor Points", "Outer Rim Fairway Ring"],
        "states": "Normal: 60% Transparency | Storm: 100% Deflection | Submerged: Hydrostatic Shield"
    },
    {
        "id": "SYS_03",
        "num": "03",
        "canon": "03.03_PETAL_STRUCTURE",
        "name": "8 ACADEMIC FACULTY PETALS",
        "elevation": "+45.0m Flared Outer Rim / -18.0m Catamaran Hull Draft",
        "radius": "Length: 950.0m / Max Beam: 420.0m / Root: R=150.0m",
        "material": "Pre-stressed Marine Aerogel Concrete / Reinforced Kevlar Hull",
        "mass": "Total Buoyant Displacement: 32,000,000 Metric Tons",
        "archetype": "ARCH_CORE_HINGE_BRACKET, Petal_MidLiving",
        "extent": "42000 x 95000 x 6300 cm per Petal Blade",
        "buoyancy": "+35,000 kN per Sector (Total: +280,000 kN)",
        "pressure": "30.0 Bar (Submerged Hydrostatic Hull Shell)",
        "zoning": "Zone.Petal.0 through Zone.Petal.7 (8 Sovereign Academic Faculties)",
        "transit": "Central 40m Spines housing Dual-track Maglev & Subsurface Utility Trunks",
        "residential": "Base platforms for 1,280 Modular Buildings and Stepped Living Quarters",
        "features": [
            "Guaranteed >= 45.0m navigable inter-petal waterway seaway clearances",
            "Aerodynamic flared outer rim (+45m) with recessed pink luminescent accent strip",
            "Deep marine catamaran keel hull with internal floodable ballast and trim tanks",
            "Central 40m academic spine housing maglev corridors and faculty districts",
            "Socket platforms for Bio-Domes, amphitheaters, and faculty sub-council halls"
        ],
        "sockets": ["Central Citadel Hinge (8x)", "Canal Bridges (8x)", "Bulkhead Isolation Gates (8x)"],
        "states": "Surface: 0 deg Pitch (Flat) | Summer Dive: 25 deg Tuck | Winter Dive: 60 deg Sealed"
    },
    {
        "id": "SYS_04",
        "num": "04",
        "canon": "03.08_FLOWER_SCATTER",
        "name": "BOTANICAL BIO-DOMES & LIVING HABITATS",
        "elevation": "+38.0m Dome Apex / +10.0m Terrace Deck",
        "radius": "Bio-Dome Radius R=60.0m (4 Domes on Even Petals)",
        "material": "Hexagonal Double-Glazed Solar Glass / Carbon Fiber Space-Truss",
        "mass": "120,000 Metric Tons per Dome Complex",
        "archetype": "ARCH_HAB_DOMELUX_A, BioDome.Botanical",
        "extent": "3000 x 3000 x 1800 cm per Dome Enclosure",
        "buoyancy": "+28,000 kN per Biosphere Unit",
        "pressure": "3.0 Bar (Atmospheric Micro-climate Seal)",
        "zoning": "Zone.Petal.Mid, Faculty.Biosphere, BioDome.Botanical",
        "transit": "Direct subterranean pedestrian skywalk corridors and pneumatic chutes",
        "residential": "Living habitats for 800 botanical researchers and faculty scholars",
        "features": [
            "4 Geodesic glass biospheres housing endangered post-flood terrestrial flora",
            "4 Stepped open-air civic amphitheaters on odd petals for student assemblies",
            "Closed-loop atmospheric oxygenation and humidity recycling life support",
            "Direct subterranean connections to faculty botanical research laboratories",
            "Bioluminescent nocturnal illumination synchronized with city annual cycle"
        ],
        "sockets": ["Petal Mid-Spine Anchor (R=450m)", "O2 & Nutrient Feeder Trunks"],
        "states": "Surface: Open Solar Influx | Submerged: Internal Artificial Sun Array Active"
    },
    {
        "id": "SYS_05",
        "num": "05",
        "canon": "03.10_PROTECTION_NETWORK",
        "name": "70 GOLDEN STAMEN ENERGY PYLONS",
        "elevation": "+45.0m Emitter Mast / +12.0m Base Deck",
        "radius": "Perimeter Circular Array R=220.0m",
        "material": "Burnished Gold Nanocoating / Superconducting Ceramic Core",
        "mass": "8,500 Metric Tons per Pylon Unit (Total: 595,000 Metric Tons)",
        "archetype": "ARCH_BARRIER_PYLON_TOWER",
        "extent": "1000 x 1000 x 4500 cm (10m x 10m x 45m Tower)",
        "buoyancy": "+15,000 kN per Pylon Base Pod",
        "pressure": "25.0 Bar (High-Frequency Plasma Envelope)",
        "zoning": "Zone.Core, Zone.Petal.Inner, System.EnergyArray",
        "transit": "Underground power maintenance tunnels linking to Citadel Bus",
        "residential": "Uninhabited / Automated Plasma Power Defense Grid",
        "features": [
            "70 Conical defense array towers arranged in a concentric crown around Citadel",
            "Apex plasma arc emitters generating coherent energy envelope for Hex Barrier",
            "Harmonic frequency modulators neutralizing tsunami seismic wave energy",
            "Internal superconducting thermal dissipation radiators",
            "Direct microwave power beaming links to 8 Academic Faculty Petals"
        ],
        "sockets": ["Receptacle Colonnade Ring (70x Sockets)", "Citadel Central Power Grid"],
        "states": "Standby: 15% Glow | Shield Active: 85% Luminous Pulse | Dive: Hydro-Ionic Discharge"
    },
    {
        "id": "SYS_06",
        "num": "06",
        "canon": "03.06_FLOWER_ZONE & 03.18",
        "name": "INTER-PETAL CANAL SKYBRIDGES",
        "elevation": "+22.0m Bridge Deck (18m Overhead Clearance Above Water)",
        "radius": "Radial Orbit R=560.0m / Torus Ring R=15.0m",
        "material": "Aeronautical Titanium Alloy / Monolithic Curved Polycarbonate",
        "mass": "35,000 Metric Tons per Bridge Spoke (Total: 280,000 Metric Tons)",
        "archetype": "ARCH_TRANS_SKYWALK_CORRIDOR, Transit_Maglev",
        "extent": "1200 x 4500 x 600 cm (12m Deck Width x 45m Waterway Span)",
        "buoyancy": "+2,200 kN per Segment",
        "pressure": "5.0 Bar (Wind & Spray Impact Rating)",
        "zoning": "Zone.Canal, Transit.InterPetal, Transit_Pedestrian",
        "transit": "Dual-Track Maglev Ring Route + 6m Glazed Pedestrian Promenade",
        "residential": "Pedestrian transit artery linking adjacent faculty residential blocks",
        "features": [
            "8 Tubular skybridge transit corridors spanning the 45m navigable waterways",
            "Dual-track automated maglev train lines linking adjacent faculty campuses",
            "Elevated pedestrian promenades with panoramic transparent floor viewports",
            "Articulated hydraulic slip-joints accommodating independent petal pitch motion",
            "Emergency rapid disconnect seals that decouple in under 12 seconds"
        ],
        "sockets": ["Petal Flank Anchor Left/Right", "Maglev Ring Route Loop"],
        "states": "Surface: Connected Transit | Dive Preparation: Articulated Decouple & Retract"
    },
    {
        "id": "SYS_07",
        "num": "07",
        "canon": "03.09_FLOWER_SHORE",
        "name": "OUTER FLOATING MARINA JETTIES & DOCKS",
        "elevation": "0.0m Sea Level (Deck Height: +2.5m, Freeboard: 1.8m)",
        "radius": "Spine Length: 95.0m / Beam: 14.0m / Gangway: 65.0m",
        "material": "High-Density Polyethylene Marine Pontoon / Marine Aluminum Alloy",
        "mass": "12,000 Metric Tons per Berth Array (Total: 96,000 Metric Tons)",
        "archetype": "ARCH_HARBOR_DOCK_HEAVY, ARCH_HARBOR_DRONE_PAD",
        "extent": "3500 x 8000 x 1200 cm (Berth Basin & Spine)",
        "buoyancy": "+45,000 kN per Marina Complex",
        "pressure": "15.0 Bar (Submerged Wave Swell Resistance)",
        "zoning": "Zone.Petal.Tip, Zone.Shore, Dock.Research, Harbor.Ferry",
        "transit": "Deep-sea research vessel berths, civilian hydrofoils, drone launch ports",
        "residential": "Harbormaster Station & Maritime Quarantine Checkpoint",
        "features": [
            "Modular floating pontoon finger piers moored outside petal flanks (ZERO crowding)",
            "Berths research ships, deep-sea exploration subs, and civilian hydrofoil shuttles",
            "Articulated telescopic shore gangways adapting to tidal surges and wave swell",
            "Automated fuel, fresh water, and high-voltage shore charging pedestals",
            "Independent subsea acoustic tension tether anchors rooted into seabed"
        ],
        "sockets": ["Outer Petal Rim Docking Sockets (16x)", "Seabed Acoustic Tether Clustered Lines"],
        "states": "Surface: Open Berthing | Submerged: Detached & Ballasted to -30m Surface Buoy"
    },
    {
        "id": "SYS_08",
        "num": "08",
        "canon": "03.11_STEM_RING",
        "name": "12 SUBMERGED EXPANDING INVERTED BALLAST RINGS",
        "elevation": "0.0m Surface down to -900.0m Abyssal Depth",
        "radius": "Inverted Cone: R=80.0m at Neck -> R=350.0m at Seabed Tier 12",
        "material": "Titanium-Boron Reinforced Pressure Hull / Heavy Ballast Castings",
        "mass": "Total Dry Steel & Hull Mass: 48,000,000 Metric Tons",
        "archetype": "ARCH_STEM_BALLAST_CHAMBER, ARCH_STEM_HYDRAULIC_CRADLE",
        "extent": "5000 x 5000 x 4000 cm per Ring Collar Segment",
        "buoyancy": "-80,000 kN Ballast to +4,228,200 kN Variable Trim",
        "pressure": "180.0 Bar (Submerged Hydrostatic Rating)",
        "zoning": "Zone.Stem, Stem_Engineering, Submerged.HydraulicCradle",
        "transit": "Vertical Transit Shaft and 12-Level Ring Circumferential Tramways",
        "residential": "Deep-sea marine research laboratories and aquanaut pressure quarters",
        "features": [
            "12 Concentric cascading ring tiers forming the inverted underwater megastructure stem",
            "Cascading sea terraces with electric cyan bioluminescent exterior guidance steps",
            "High-capacity seawater ballast chambers for depth control (0 to -1,000m)",
            "Hydraulic Cradle Shelf at Ring 1 cradling the 8 petals during deep submersion",
            "Deep-sea marine biology labs, ocean current turbine generators, and pressure locks"
        ],
        "sockets": ["Core Interface Collar (Top)", "12 Inter-Ring Couplers", "Doomsday Vault (Bottom)"],
        "states": "Spring: 0m Float | Summer Dive: -500m Submerged | Winter Dive: -1,000m Abyssal"
    },
    {
        "id": "SYS_09",
        "num": "09",
        "canon": "03.16_ROOT_SYSTEM",
        "name": "ABYSSAL DOOMSDAY VAULT & BEDROCK ANCHOR CLAWS",
        "elevation": "-950.0m to -1,000.0m Oceanic Abyssal Seabed",
        "radius": "Central Vault Bunker Radius R=120.0m / Claw Span: 380.0m",
        "material": "Multi-layer Titanium Basalt Blast Armor / Cryogenic Alloy Shell",
        "mass": "Total Anchored Foundation Mass: 85,000,000 Metric Tons",
        "archetype": "ARCH_DOOMSDAY_VAULT_CHAMBER, ARCH_ROOT_SEABED_CLAW",
        "extent": "6000 x 9000 x 5000 cm (Claw) | 6000 x 6000 x 3500 cm (Vault)",
        "buoyancy": "-150,000 kN (Bedrock Gravitational Preload)",
        "pressure": "350.0 Bar (Abyssal Ocean Floor Extreme Pressure)",
        "zoning": "Zone.Root, Root_AbyssalAnchor, Abyssal.BedrockClaws",
        "transit": "Seabed Terminus Station with Decompression Locks and Submersible Bays",
        "residential": "Hermetic cryogenic seed vault, genome archives, and emergency bunker",
        "features": [
            "Central monolithic Doomsday Vault preserving genetic genome seeds of Earth's species",
            "Cryogenic knowledge repository containing complete archives of 17 Great States",
            "8 Giant articulated hydraulic bedrock claws drilled 150m into tectonic oceanic bedrock",
            "Tectonic seismic shock absorbers dampening Richter 9.0 deep-sea oceanic earthquakes",
            "Geothermal thermoelectric taps generating 2.4 GigaWatts of baseline power"
        ],
        "sockets": ["Vertical Transit Chute (Apex)", "8 Bedrock Hydraulic Struts", "Geothermal Wellheads"],
        "states": "Always Active: Continuous Autonomous Standalone Deep-Sea Bunker Operation"
    },
    {
        "id": "SYS_10",
        "num": "10",
        "canon": "03.20_TRANSIT_FLOW_NETWORK & 03_TRANSIT_AND_RESOURCE_GRAPH",
        "name": "3D MAGLEV & EVAC MULTI-LAYER TRANSIT NETWORK",
        "elevation": "+12.0m Surface Mainlines / -850m Deep-Sea Conduits",
        "radius": "Concentric Transit Rings at R=260m and R=520m / 8 Radial Trunks",
        "material": "Electromagnetic Superconducting Rails / Sealed Carbon Fiber Tubes",
        "mass": "Total Route Network: 136 Routes / 76 Stations (850,000 Metric Tons)",
        "archetype": "ARCH_TRANS_MAGLEV_STATION, ARCH_TRANS_MAGLEV_TUBE",
        "extent": "Station: 2400 x 6000 x 1200 cm | Tube: 600 x 4000 x 600 cm",
        "buoyancy": "+20,000 kN (Stations) / +6,000 kN (Tubes)",
        "pressure": "15.0 Bar (Stations) / 20.0 Bar (Submerged Tubes)",
        "zoning": "Zone.Core, Zone.Petal.Inner, Zone.Petal.Mid, Transit.Maglev",
        "transit": "Capacity: 150,000 Passengers/Hour | Headway: 30 Seconds | Top Speed: 350 km/h (Surface) / 180 km/h (Underwater)",
        "residential": "Connects all 8 Faculty Dormitory Hubs to Central Citadel in < 90 seconds",
        "features": [
            "Multi-layer 3D transit network with high-speed maglev passenger capsules and pneumatic cargo delivery",
            "Emergency pressurized evacuation tubes directing all citizens to Core Citadel Bunker in < 6 minutes",
            "Cryogenic cooling jackets maintaining 4K superconducting rail temperatures across all 8 petals",
            "Central 6-level Grand Interchange Terminal with automated platform screen doors and escalators",
            "Fail-safe magnetic induction regenerative braking feeding kinetic power back into city grid"
        ],
        "sockets": ["Citadel Central Grand Station", "76 Sub-Stations", "Petal Maglev Portals", "Inter-Petal Bridge Connectors"],
        "states": "Normal: High Throughput (120 trains/hr) | Emergency: Evac Capsule Priority Mode (Core Evacuation)"
    },
    {
        "id": "SYS_11",
        "num": "11",
        "canon": "03.15_FLOWER_STEM_CONNECTION",
        "name": "CORE-TO-STEM RING 1 STRUCTURAL INTERFACE COLLAR",
        "elevation": "0.0m Sea Surface to -50.0m Subsurface Collar",
        "radius": "Top Flange R=95.0m / Bottom Interface R=82.0m",
        "material": "Cast Nickel-Chromium Steel / Elastomeric Hydrostatic Gaskets",
        "mass": "3,200,000 Metric Tons",
        "archetype": "ARCH_STEM_COLLAR_COUPLER, System.InterfaceCollar",
        "extent": "9500 x 9500 x 5000 cm (95m Flange Diameter x 50m Depth)",
        "buoyancy": "-12,000 kN (Structural Deadweight)",
        "pressure": "40.0 Bar (Surface Shear & Subsurface Pressure)",
        "zoning": "Zone.Stem.Interface, Structural.Collar",
        "transit": "Subsurface Maglev Junction Station linking surface lines to vertical stem shaft",
        "residential": "Engineering Maintenance Crew Airlock Quarters",
        "features": [
            "Massive structural collar transferring shear and vertical loads between surface and stem",
            "8 Heavy radial load-bearing gussets aligned directly with the 8 academic petal axes",
            "Continuous circumferential triple-redundant hydrostatic pressure sealing gasket",
            "Heavy umbilical penetration sleeves routing primary electrical trunks and water lines",
            "Hydraulic preload tension jacks maintaining dynamic structural alignment"
        ],
        "sockets": ["Citadel Core Foundation (Top)", "Stem Ring 1 Bulkhead (Bottom)"],
        "states": "Continuous Dynamic Load Redistribution during All Submersion & Surface Cycles"
    },
    {
        "id": "SYS_12",
        "num": "12",
        "canon": "03.14_RING_CONNECTION & 03.12",
        "name": "INTER-RING HYDRAULIC EXPANSION DAMPERS & COUPLERS",
        "elevation": "Cascading along all 12 Ring Tiers (0m down to -900m)",
        "radius": "176 Hydraulic Damper Units (11 inter-ring levels x 8 sectors x 2 dual)",
        "material": "Hard Chrome-Plated Titanium-Vanadium Alloy Cylinders",
        "mass": "Total Hydraulic Array: 1,800,000 Metric Tons",
        "archetype": "ARCH_STEM_HYDRAULIC_CRADLE, System.HydraulicDamper",
        "extent": "300 x 1800 x 300 cm per Dual-Piston Actuator Assembly",
        "buoyancy": "Zero Mass Equilibrium in Seawater",
        "pressure": "250.0 Bar Internal Hydraulic Working Fluid Pressure",
        "zoning": "Zone.Stem.Hydraulics, Structural.Dampers",
        "transit": "Flexible articulated high-pressure utility jumper loops between ring levels",
        "residential": "Uninhabited / Automated Seismic Damping Array",
        "features": [
            "Dual-acting heavy hydraulic cylinders providing active damping against oceanic turbulence",
            "Telescopic expansion sleeves allowing controlled structural extension and collapse",
            "Fluidic shock dissipation chambers handling 50,000 kN impact forces per piston",
            "Flexible articulated high-pressure utility jumper loops connecting adjacent rings",
            "Fail-safe mechanical locking wedges holding position during prolonged depth hold"
        ],
        "sockets": ["Upper Ring Lug Mount", "Lower Ring Flange Mount", "Hydraulic Manifold Lines"],
        "states": "Extended at Surface | Actively Damped During Descent | Mechanically Locked at Bedrock"
    },
    {
        "id": "SYS_13",
        "num": "13",
        "canon": "03.13_STEM_TRANSPORT",
        "name": "VERTICAL DEEP-SEA TRANSIT ELEVATOR CORE",
        "elevation": "+120.0m Citadel Base down to -980.0m Seabed Terminal (1.1 km)",
        "radius": "Central Titanium Pressure Shaft Radius R=12.0m",
        "material": "Continuous Extruded Titanium-Composite Tube / Maglev Stators",
        "mass": "2,800,000 Metric Tons",
        "archetype": "ARCH_STEM_ELEVATOR_SHAFT",
        "extent": "2400 x 2400 x 110000 cm (24m Diameter x 1,100m Vertical Shaft)",
        "buoyancy": "-5,000 kN (Pressure Stabilized)",
        "pressure": "200.0 Bar (Submerged Titanium Alloy Pressure Shell)",
        "zoning": "Zone.Stem, Transit.VerticalElevator, Station.Airlock",
        "transit": "4 Maglev Elevator Cars (Speed: 25 m/s) + 5 Airlock Hubs (0m, -250m, -500m, -750m, -950m)",
        "residential": "Decompression Lounges & Abyssal Transition Living Pods",
        "features": [
            "Direct express vertical transit spine linking Citadel to Seabed Vault in 2.5 minutes",
            "4 External high-speed maglev elevator cab tracks with aerodynamic atmospheric seals",
            "5 Pressurized airlock transfer lobbies at Z=0m, -250m, -500m, -750m, -950m",
            "Atmospheric pressure staging decompression locks for abyssal researchers",
            "Central high-voltage superconducting bus duct and freshwater supply risers"
        ],
        "sockets": ["Citadel Core Transit Lobby", "5 Airlock Stations", "Doomsday Vault Apex"],
        "states": "Continuous 24/7 Vertical Transit with Automated Pressure-Stage Lockouts"
    },
    {
        "id": "SYS_14",
        "num": "14",
        "canon": "03.19_STATE_DEPENDENCY & 03.18",
        "name": "EMERGENCY WATERTIGHT BULKHEAD ISOLATION GATES",
        "elevation": "Sea Level Z=0m (Gantry Height: +38.0m / Keel Lock: -5.8m)",
        "radius": "Positioned at 8 Inner Seaways at R=165.0m",
        "material": "Reinforced Naval Steel Guillotine Armor / Concrete Pylon Towers",
        "mass": "450,000 Metric Tons (8 Gate Installations Total)",
        "archetype": "ARCH_BULKHEAD_ISOLATION_GATE, System.EmergencyGate",
        "extent": "1200 x 5500 x 4400 cm (45m Clear Spanning Gate Frame)",
        "buoyancy": "Zero (Rigid Pylon Foundation into Petal Keel)",
        "pressure": "20.0 Bar (Hydrostatic Tidal & Tsunami Barrier)",
        "zoning": "Zone.Canal.Gate, Security.Quarantine, Emergency.Bulkhead",
        "transit": "Canal fairways open during normal operations; sealed during quarantine",
        "residential": "Gatekeeper Watchtowers and Emergency Response Ready-Rooms",
        "features": [
            "Twin reinforced gantry towers straddling the 45m fairway channels at each petal root",
            "Movable multi-ton steel guillotine blast door descending from +24m to -5.8m keel lock",
            "Complete independent watertight isolation of any damaged or contaminated petal",
            "Triple-redundant inflatable rubber compression gaskets providing 100% hydrostatic seal",
            "Quarantine warning strobe beacons and automated canal traffic signal beacons"
        ],
        "sockets": ["Petal Flank Pier Mounts", "Canal Bedrock Keel Trench", "City Emergency Bus"],
        "states": "Normal: Raised (+24m Open) | Dive / Emergency: Sealed into Seabed Slot (-5.8m)"
    },
    {
        "id": "SYS_15",
        "num": "15",
        "canon": "03.06_FLOWER_ZONE & 03.03",
        "name": "8 FACULTY SUB-COUNCIL ASSEMBLY HALLS",
        "elevation": "+48.0m Canopy Apex / +10.0m Plaza Ground Level",
        "radius": "Podium Plaza Radius R=42.0m / Radial Distance R=380.0m on each petal",
        "material": "Honed Ivory Marine Limestone / Curved Structural Solar Glass",
        "mass": "280,000 Metric Tons per Assembly Hall Complex",
        "archetype": "ARCH_PETAL_SUBCOUNCIL_HALL, ARCH_ACADEMIC_AMPHITHEATER",
        "extent": "2400 x 3000 x 1200 cm per Assembly Hall",
        "buoyancy": "+14,000 kN per Complex",
        "pressure": "8.0 Bar (Storm & Pressure Shell)",
        "zoning": "Zone.Petal.Mid, Council.SubFaculty, Function.Academic",
        "transit": "Direct portal to Petal Central Spine Promenade and Maglev Station",
        "residential": "Faculty Offices, Dean Suites, and Scholar Symposia Lounges",
        "features": [
            "8 Distinct civic legislative assembly chambers for the 8 sovereign academic faculties",
            "Stepped circular limestone amphitheater seating 3,500 delegates and faculty scholars",
            "Sculptural aerodynamic cantilever clamshell canopy roof arching out over the plaza",
            "Faculty ceremonial beacon spire at apex illuminating with faculty-specific color tint",
            "Central holographic podium displaying global telemetry, academic votes, and city state"
        ],
        "sockets": ["Petal Civic Spine", "Faculty Transit Terminal", "Emergency Evac Chute"],
        "states": "Day: Academic Debates & Voting | Night: Public Cultural Symposia & Astronomical Observers"
    },
    {
        "id": "SYS_16",
        "num": "16",
        "canon": "03.07_CIVILIAN_MODULES & 02_MODULAR_ASSEMBLY",
        "name": "MODULAR CIVIC & ACADEMIC BUILDING SYSTEM",
        "elevation": "+12.0m Base Deck to +42.0m Rooftop Bio-Dome / Spire",
        "radius": "12.0m x 12.0m Footprint Grid / 1,280 Buildings / 7,623 Stacked Floors",
        "material": "Prefabricated Lightweight Aerogel Concrete / Curved Ivory Cladding",
        "mass": "Total Assembly Displacement: 3,043,040 Metric Tons | Buoyant Lift: 4,228,200 kN",
        "archetype": "FC_Building_Base, FC_Ground_Lobby, FC_Mid_Academic_Floors, FC_Roof_Dome",
        "extent": "1200 x 1200 x 400 to 600 cm per Modular Floor Unit",
        "buoyancy": "+600 to +1,200 kN per Module",
        "pressure": "6.0 Bar (Watertight Marine Aerogel Shell)",
        "zoning": "Zone.Petal.Mid, Function.Academic.Labs, Function.Classrooms",
        "transit": "Internal building service shafts linked to petal deck maglev and utility conduits",
        "residential": "Houses faculty research labs, lecture halls, and academic departments",
        "features": [
            "Modular kit-of-parts architecture stacked across 8 Academic Petal districts",
            "5 Standard functional tiers: Foundation, Ground Lobby, Academic Labs, Faculty Chambers, Rooftop Bio-Dome",
            "Parametric density distribution from high-density petal roots to low-density flaring tips",
            "Integrated maglev feeder tubes and pneumatic delivery chutes inside structural shafts",
            "Direct plug-and-play utility conduits connecting to petal deck umbilical manifolds"
        ],
        "sockets": ["Petal Deck Foundation Anchors (12x12m Grid)", "District Maglev Spine", "Utility Umbilical Ducts"],
        "states": "Surface: Full Academic Activity | Dive: Hermetically Pressurized & External Shutters Closed"
    },
    {
        "id": "SYS_17",
        "num": "17",
        "canon": "03.04_ZONES_AND_SCATTER & 01_DATA_TABLE_DISTRICT_ZONING",
        "name": "MODULAR RESIDENTIAL HOUSING & INTERNATIONAL SCHOLAR DORMITORIES",
        "elevation": "+12.0m Base Deck to +38.0m Stepped Terraces",
        "radius": "Footprint: 12.0m x 24.0m (1200 x 2400 cm) / Height: 9.0m to 24.0m",
        "material": "Prefabricated Aerogel Cellular Concrete / Self-Cleaning Hydrophobic Glass",
        "mass": "950 Metric Tons per Residential Block (Total District: 4,800,000 Metric Tons)",
        "archetype": "ARCH_HAB_MODULAR_APARTMENT, ARCH_HAB_DOME_COMPACT_B",
        "extent": "1200 x 2400 x 900 cm (Expandable to 4-8 Stories)",
        "buoyancy": "+14,000 kN per Block",
        "pressure": "5.0 Bar (Watertight Submerged Seals)",
        "zoning": "Zone.Petal.Mid, Petal_MidLiving, Campus.InternationalDorm",
        "transit": "Direct feeder connections to Petal Spine Maglev and Pneumatic Chutes",
        "residential": "Capacity: 350 Scholars / Faculty Units per Complex | Furnished Studio Suites, Hydroponic Balconies, Shared Living Lounges",
        "features": [
            "Cascading stepped-terrace architectural profile with cantilevered outdoor balconies",
            "Individual modular studio apartments with integrated climate-controlled living pods",
            "Hydroponic micro-farming balcony gardens providing localized fresh food production",
            "Inter-block pedestrian skybridge walkways and communal academic study lounges",
            "Slope-compensated foundation pilings anchoring securely into petal composite hull"
        ],
        "sockets": ["Petal Deck Structural Anchors", "Transit Feeder Portal", "Pneumatic Capsule Chute", "O2/Water Umbilicals"],
        "states": "Solstice: Open Balconies & Terraces | Dive / Storm: Hermetically Sealed External Blast Shutters"
    }
]
# endregion


# region PROCEDURAL CAD BLUEPRINT CARD RENDERER
def draw_blueprint_card(spec):
    """Draws a dedicated, ultra-crisp 1920x1080 sci-fi CAD technical blueprint card for one subsystem."""
    w, h = 1920, 1080
    im = Image.new("RGBA", (w, h), (6, 12, 22, 255))
    d = ImageDraw.Draw(im)

    # 1. Sci-Fi Technical Blueprint Grid
    grid_col_minor = (14, 28, 48, 140)
    grid_col_major = (24, 52, 88, 200)

    for x in range(0, w, 30):
        c = grid_col_major if x % 150 == 0 else grid_col_minor
        d.line([(x, 0), (x, h)], fill=c, width=1)
    for y in range(0, h, 30):
        c = grid_col_major if y % 150 == 0 else grid_col_minor
        d.line([(0, y), (w, y)], fill=c, width=1)

    # 2. Outer Technical Border & Calibration Marks
    d.rectangle([(25, 25), (w - 25, h - 25)], outline=(35, 85, 145, 255), width=2)
    d.rectangle([(32, 32), (w - 32, h - 32)], outline=(20, 55, 95, 255), width=1)

    bracket_len = 35
    for cx, cy in [(25, 25), (w - 25, 25), (25, h - 25), (w - 25, h - 25)]:
        dx = 1 if cx == 25 else -1
        dy = 1 if cy == 25 else -1
        d.line([(cx, cy), (cx + dx * bracket_len, cy)], fill=(0, 210, 255, 255), width=3)
        d.line([(cx, cy), (cx, cy + dy * bracket_len)], fill=(0, 210, 255, 255), width=3)

    # 3. Header Block
    d.rectangle([(45, 45), (w - 45, 145)], fill=(10, 22, 40, 220), outline=(0, 180, 255, 255), width=2)
    d.text((65, 55), "ISTRORIGAN MEGASTRUCTURE (YEAR 4205) - SYSTEM BREAKDOWN BLUEPRINT", fill=(0, 220, 255, 255))
    d.text((65, 80), f"COMPONENT: {spec['id']} // {spec['name']}", fill=(255, 255, 255, 255))
    d.text((65, 115), f"CANON ARCHITECTURE REF: {spec['canon']} | GOVERNANCE: COUNCIL OF TEN", fill=(160, 200, 240, 255))

    # Header Right Badges
    d.rectangle([(w - 340, 55), (w - 65, 135)], fill=(12, 30, 55, 255), outline=(0, 210, 255, 255), width=1)
    d.text((w - 325, 68), "SECURITY CLEARANCE: TIER 10", fill=(0, 230, 255, 255))
    d.text((w - 325, 90), "STATUS: ACTIVE CANONICAL", fill=(0, 255, 160, 255))
    d.text((w - 325, 112), "VERIFICATION: 100% GAME-READY", fill=(240, 240, 255, 255))

    # 4. Left Column: Engineering Telemetry & Physical Specs
    box_l_x = 45
    box_l_w = 520
    d.rectangle([(box_l_x, 165), (box_l_x + box_l_w, h - 45)], fill=(10, 20, 36, 210), outline=(30, 75, 125, 255), width=1)
    d.rectangle([(box_l_x, 165), (box_l_x + box_l_w, 205)], fill=(18, 42, 75, 255))
    d.text((box_l_x + 15, 175), "TECHNICAL SPECIFICATIONS & METROLOGY", fill=(0, 220, 255, 255))

    specs_list = [
        ("Subsystem ID", spec["id"]),
        ("Archetype Tag", spec.get("archetype", "ARCH_CANON_MODULE")),
        ("Footprint Extent", spec.get("extent", spec["radius"])),
        ("Elevation / Depth", spec["elevation"]),
        ("Structural Mass", spec["mass"]),
        ("Buoyancy Force", spec.get("buoyancy", "+35,000 kN")),
        ("Pressure Rating", spec.get("pressure", "15.0 Bar")),
        ("Zoning Permitted", spec.get("zoning", "Zone.Petal.Mid")),
    ]

    cur_y = 220
    for label, val in specs_list:
        d.text((box_l_x + 15, cur_y), label.upper() + ":", fill=(0, 180, 240, 255))
        cur_y += 20
        d.text((box_l_x + 25, cur_y), val[:55], fill=(245, 245, 250, 255))
        cur_y += 28
        d.line([(box_l_x + 15, cur_y - 6), (box_l_x + box_l_w - 15, cur_y - 6)], fill=(20, 45, 80, 255), width=1)

    # Operational States Box
    d.text((box_l_x + 15, cur_y + 4), "OPERATIONAL BEHAVIOR MODES:", fill=(255, 210, 0, 255))
    cur_y += 26
    d.text((box_l_x + 25, cur_y), spec["states"][:60], fill=(220, 230, 240, 255))

    # Sockets Box
    cur_y += 36
    d.text((box_l_x + 15, cur_y), "COUPLING & RIG SOCKETS:", fill=(0, 255, 180, 255))
    cur_y += 22
    for sock in spec["sockets"][:4]:
        d.text((box_l_x + 25, cur_y), f"* {sock}", fill=(200, 240, 255, 255))
        cur_y += 20

    # 5. Right Column: Architectural Schematic Diagram & Engineering Exploded Blueprint
    diag_x = box_l_x + box_l_w + 20
    diag_w = w - diag_x - 45
    d.rectangle([(diag_x, 165), (diag_x + diag_w, h - 45)], fill=(8, 16, 30, 230), outline=(0, 160, 240, 255), width=1)
    d.rectangle([(diag_x, 165), (diag_x + diag_w, 205)], fill=(16, 40, 70, 255))
    d.text((diag_x + 15, 175), f"ORTHOGRAPHIC CAD SCHEMATIC // ISOLATED SUBSYSTEM {spec['id']}", fill=(0, 220, 255, 255))

    cx = diag_x + diag_w // 2
    cy = 165 + (h - 210) // 2 - 40

    for r in [80, 160, 240, 320]:
        d.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=(18, 45, 80, 150), width=1)
    d.line([(cx - 360, cy), (cx + 360, cy)], fill=(18, 55, 95, 180), width=1)
    d.line([(cx, cy - 280), (cx, cy + 280)], fill=(18, 55, 95, 180), width=1)

    wire_col = (0, 220, 255, 255)
    accent_col = (255, 210, 0, 255)
    ghost_col = (30, 80, 140, 200)

    s_num = int(spec["num"])
    if s_num == 1:  # Apex Spire
        d.line([(cx - 140, cy + 180), (cx + 140, cy + 180)], fill=wire_col, width=3)
        for sign in [-1, 1]:
            d.line([(cx + sign * 140, cy + 180), (cx + sign * 60, cy + 80)], fill=wire_col, width=2)
            d.line([(cx + sign * 90, cy + 180), (cx + sign * 40, cy + 60)], fill=wire_col, width=2)
            d.line([(cx + sign * 40, cy + 180), (cx + sign * 20, cy + 40)], fill=wire_col, width=2)
        d.ellipse([(cx - 85, cy + 20), (cx + 85, cy + 50)], outline=accent_col, width=3)
        d.line([(cx - 40, cy + 35), (cx - 15, cy - 220)], fill=wire_col, width=3)
        d.line([(cx + 40, cy + 35), (cx + 15, cy - 220)], fill=wire_col, width=3)
        d.ellipse([(cx - 18, cy - 40), (cx + 18, cy + 10)], outline=(0, 255, 180, 255), width=2)

    elif s_num == 3:  # Petal Structure
        p_pts = []
        for a in range(0, 360, 5):
            rad = math.radians(a)
            px = cx + math.cos(rad) * 320
            py = cy + math.sin(rad) * 140
            p_pts.append((px, py))
        d.polygon(p_pts, outline=wire_col, fill=(10, 25, 45, 120))
        d.rectangle([(cx - 240, cy - 18), (cx + 140, cy + 18)], outline=(0, 255, 180, 255), width=2)
        d.ellipse([(cx + 160, cy - 45), (cx + 250, cy + 45)], outline=(0, 255, 140, 255), width=2)

    elif s_num in (8, 11, 12):  # Submerged Stem & Hydraulics
        for r_i in range(10):
            frac1 = r_i / 10.0
            frac2 = (r_i + 1) / 10.0
            w1 = 120 + (frac1 ** 1.3) * 220
            w2 = 120 + (frac2 ** 1.3) * 220
            y1 = cy - 140 + frac1 * 340
            y2 = cy - 140 + frac2 * 340
            d.polygon([(cx - w1, y1), (cx + w1, y1), (cx + w2, y2), (cx - w2, y2)], outline=wire_col, fill=(12, 30, 55, 80))
            d.line([(cx - w1 * 0.9, y1 + 5), (cx - w2 * 0.9, y2 - 5)], fill=accent_col, width=3)
            d.line([(cx + w1 * 0.9, y1 + 5), (cx + w2 * 0.9, y2 - 5)], fill=accent_col, width=3)

    elif s_num == 9:  # Abyssal Vault & Claws
        d.arc([(cx - 160, cy - 120), (cx + 160, cy + 80)], 180, 360, fill=wire_col, width=4)
        d.rectangle([(cx - 160, cy - 20), (cx + 160, cy + 40)], outline=wire_col, width=2)
        d.line([(cx - 280, cy + 120), (cx + 280, cy + 120)], fill=(120, 140, 160, 255), width=4)
        d.text((cx - 270, cy + 130), "OCEANIC TECTONIC BEDROCK (-1,000m)", fill=(160, 180, 200, 255))
        for c_x_off in [-140, -50, 50, 140]:
            d.line([(cx + c_x_off, cy + 40), (cx + c_x_off * 1.5, cy + 120)], fill=accent_col, width=4)
            d.line([(cx + c_x_off * 1.5, cy + 120), (cx + c_x_off * 1.8, cy + 190)], fill=wire_col, width=4)

    elif s_num == 10:  # 3D Maglev & Evac Transit Network
        # Multi-layer transit terminal diagram
        d.rectangle([(cx - 260, cy - 40), (cx + 260, cy + 40)], outline=wire_col, width=3)
        d.text((cx - 240, cy - 30), "CENTRAL MAGLEV INTERCHANGE TERMINAL (LEVEL 1-6)", fill=(0, 220, 255, 255))
        # Hyperloop tubes
        for ty in [cy - 120, cy - 70, cy + 80, cy + 130]:
            d.line([(cx - 300, ty), (cx + 300, ty)], fill=(0, 255, 180, 255), width=3)
            d.ellipse([(cx - 280, ty - 12), (cx - 250, ty + 12)], outline=accent_col, width=2)
            d.ellipse([(cx + 250, ty - 12), (cx + 280, ty + 12)], outline=accent_col, width=2)
        # Train pods on tracks
        d.rectangle([(cx - 80, cy - 130), (cx + 80, cy - 110)], fill=(0, 220, 255, 180), outline=accent_col, width=2)
        d.text((cx - 65, cy - 126), "MAGLEV CAR: 350 KM/H", fill=(10, 20, 40, 255))
        d.rectangle([(cx - 60, cy + 70), (cx + 60, cy + 90)], fill=(255, 210, 0, 180), outline=wire_col, width=2)
        d.text((cx - 50, cy + 74), "EVAC TUBE POD", fill=(10, 20, 40, 255))

    elif s_num == 14:  # Bulkhead Isolation Gates
        d.rectangle([(cx - 220, cy - 160), (cx - 160, cy + 140)], outline=wire_col, width=3)
        d.rectangle([(cx + 160, cy - 160), (cx + 220, cy + 140)], outline=wire_col, width=3)
        d.rectangle([(cx - 240, cy - 180), (cx + 240, cy - 140)], outline=accent_col, width=3)
        d.rectangle([(cx - 150, cy - 70), (cx + 150, cy + 70)], outline=(255, 90, 60, 255), width=4)
        d.line([(cx - 280, cy + 80), (cx + 280, cy + 80)], fill=(0, 180, 255, 255), width=2)

    elif s_num == 15:  # Sub-Council Halls
        for t in range(4):
            pw = 260 - t * 25
            ph = 70 - t * 7
            py = cy + 60 + t * 15
            d.ellipse([(cx - pw, py - ph), (cx + pw, py + ph)], outline=wire_col, width=2)
        d.arc([(cx - 200, cy - 160), (cx + 200, cy + 80)], 190, 350, fill=accent_col, width=4)
        d.line([(cx - 200, cy - 40), (cx + 200, cy - 40)], fill=wire_col, width=2)

    elif s_num == 16:  # Modular Civic & Academic Buildings
        floor_labels = [
            ("TIER 5: ROOF BIO-DOME (+26m)", 26, 8, accent_col),
            ("TIER 4: FACULTY CHAMBERS (+18m)", 18, 8, wire_col),
            ("TIER 3: ACADEMIC LABS (+10m)", 10, 8, wire_col),
            ("TIER 2: GROUND LOBBY (+4m)", 4, 6, wire_col),
            ("TIER 1: FOUNDATION (0m)", 0, 4, (120, 140, 160, 255)),
        ]
        iso_scale_x, iso_scale_y = 1.3, 0.7
        box_w, box_d = 90, 70
        base_y_screen = cy + 140

        for name, z_base, h_val, col in reversed(floor_labels):
            y_bot = base_y_screen - z_base * 7
            y_top = y_bot - h_val * 7
            pt_top_f = (cx, y_top + box_d * iso_scale_y * 0.5)
            pt_top_b = (cx, y_top - box_d * iso_scale_y * 0.5)
            pt_top_l = (cx - box_w * iso_scale_x * 0.5, y_top)
            pt_top_r = (cx + box_w * iso_scale_x * 0.5, y_top)
            pt_bot_f = (cx, y_bot + box_d * iso_scale_y * 0.5)
            pt_bot_l = (cx - box_w * iso_scale_x * 0.5, y_bot)
            pt_bot_r = (cx + box_w * iso_scale_x * 0.5, y_bot)

            d.polygon([pt_top_l, pt_top_f, pt_bot_f, pt_bot_l], outline=col, fill=(10, 24, 45, 160))
            d.polygon([pt_top_r, pt_top_f, pt_bot_f, pt_bot_r], outline=col, fill=(14, 32, 60, 160))
            d.polygon([pt_top_b, pt_top_r, pt_top_f, pt_top_l], outline=col, fill=(18, 42, 75, 200))
            d.line([(cx + box_w * iso_scale_x * 0.5 + 10, y_top), (cx + box_w * iso_scale_x * 0.5 + 90, y_top)], fill=col, width=1)
            d.text((cx + box_w * iso_scale_x * 0.5 + 100, y_top - 7), name, fill=col)

    elif s_num == 17:  # Modular Residential Housing & Scholar Dormitories
        # Stepped terrace residential facade diagram
        step_levels = 5
        base_y = cy + 150
        d.line([(cx - 250, base_y), (cx + 250, base_y)], fill=(0, 180, 255, 255), width=3)
        d.text((cx - 240, base_y + 10), "OCEAN WATER LEVEL Z=0m / PETAL DECK Z=+12m", fill=(0, 180, 255, 255))

        for st in range(step_levels):
            sw = 280 - st * 45
            sh = base_y - (st + 1) * 55
            # Terrace block
            d.rectangle([(cx - sw, sh), (cx + sw - 60, sh + 50)], outline=wire_col, fill=(12, 28, 50, 150), width=2)
            # Cantilever balcony
            d.rectangle([(cx + sw - 60, sh + 15), (cx + sw, sh + 50)], outline=accent_col, fill=(20, 45, 80, 180), width=2)
            d.text((cx - sw + 15, sh + 18), f"LEVEL {st + 1}: RESIDENTIAL LIVING UNITS", fill=(220, 235, 255, 255))
            # Hydroponic garden greenery line
            d.line([(cx + sw - 55, sh + 20), (cx + sw - 5, sh + 20)], fill=(0, 255, 140, 255), width=3)

    else:
        d.rectangle([(cx - 180, cy - 140), (cx + 180, cy + 140)], outline=wire_col, width=2)
        d.ellipse([(cx - 120, cy - 100), (cx + 120, cy + 100)], outline=accent_col, width=2)
        d.line([(cx - 180, cy - 140), (cx + 180, cy + 140)], fill=ghost_col, width=1)
        d.line([(cx - 180, cy + 140), (cx + 180, cy - 140)], fill=ghost_col, width=1)

    # 6. Lower Callout Feature Bullets
    bot_y = h - 210
    d.rectangle([(diag_x + 10, bot_y), (diag_x + diag_w - 10, h - 55)], fill=(12, 26, 46, 255), outline=(0, 180, 255, 255), width=1)
    d.text((diag_x + 25, bot_y + 10), "KEY CANONICAL ARCHITECTURAL FEATURES:", fill=(0, 255, 180, 255))
    feat_y = bot_y + 35
    for feat in spec["features"][:4]:
        d.text((diag_x + 35, feat_y), f">> {feat}", fill=(240, 245, 255, 255))
        feat_y += 24

    card_filename = f"{spec['num']}_BLUEPRINT_{spec['id']}.png"
    card_path = os.path.join(OUTPUT_BLUEPRINTS_DIR, card_filename)
    im.save(card_path, "PNG")
    print(f"  [+] Generated Blueprint Card: {card_filename} ({os.path.getsize(card_path):,} bytes)")
    return card_filename
# endregion


# region BLUEPRINT INDEX MARKDOWN GENERATOR
def generate_blueprint_index_md():
    """Writes an exhaustive Markdown Index documenting all generated blueprints for other AIs."""
    md_path = os.path.join(OUTPUT_BLUEPRINTS_DIR, "BLUEPRINT_INDEX.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# ISTRORIGAN MEGASTRUCTURE - COMPLETE SUBSYSTEM BLUEPRINT & METROLOGY CATALOG\n\n")
        f.write("**Era: Year 4205 | Sovereign Sanctuary of the 17 Great States**\n\n")
        f.write("> Exhaustive engineering blueprints, photorealistic visual CAD renders, and complete metrology specification tables\n")
        f.write("> for all 17 megastructure subsystems. Formatted for multi-agent AI inspection, 3D printing slicing, and UE5/Houdini compilation.\n\n")
        f.write("---\n\n")

        f.write("## 1. AI Visual Blueprint Renders (Photorealistic CAD Illustrations)\n\n")
        f.write("Visual CAD illustrations representing each individual component in high-resolution isolation:\n\n")

        render_titles = {
            "AI_RENDER_01_APEX_SPIRE.jpg": "SYS_01: Apex Spire & Citadel of Ten (+600m Twin-Blade Tower)",
            "AI_RENDER_02_HEX_BARRIER.jpg": "SYS_02: Hexagonal Forcefield Barrier Dome (3,000m Diameter Envelope)",
            "AI_RENDER_03_ACADEMIC_PETAL.jpg": "SYS_03: Academic Faculty Petals (45m Waterway Clearance & Hull)",
            "AI_RENDER_04_BIO_DOMES.jpg": "SYS_04: Botanical Bio-Domes & Living Habitats (Geodesic Biospheres)",
            "AI_RENDER_05_STAMEN_PYLONS.jpg": "SYS_05: 70 Golden Stamen Energy Pylons (45m Plasma Towers)",
            "AI_RENDER_06_CANAL_SKYBRIDGES.jpg": "SYS_06: 45m Inter-Petal Canal Skybridges (Maglev Transit Span)",
            "AI_RENDER_07_FLOATING_MARINA_DOCKS.jpg": "SYS_07: Outer Floating Marina Docks & Pontoon Jetties (Canon Berth)",
            "AI_RENDER_08_SUBMERGED_STEM.jpg": "SYS_08: 12 Submerged Expanding Stem Rings (0m to -900m Ballast)",
            "AI_RENDER_09_ABYSSAL_VAULT.jpg": "SYS_09: Abyssal Doomsday Vault & Bedrock Claws (-1,000m Seabed)",
            "AI_RENDER_10_TRANSIT_TRANSPORT.jpg": "SYS_10: 3D Maglev & Evac Multi-Layer Transit Network (Hyperloop Tubes)",
            "AI_RENDER_11_CORE_STEM_COLLAR.jpg": "SYS_11: Core-to-Stem Structural Interface Collar (Titanium Gussets)",
            "AI_RENDER_12_HYDRAULIC_DAMPERS.jpg": "SYS_12: Inter-Ring Hydraulic Expansion Dampers (Shock Absorbers)",
            "AI_RENDER_13_DEEPSEA_ELEVATOR_CORE.jpg": "SYS_13: Vertical Deep-Sea Transit Elevator Core (1.1km Pressure Shaft)",
            "AI_RENDER_14_BULKHEAD_GATES.jpg": "SYS_14: Emergency Bulkhead Isolation Gates (38m Floodgate Gantry)",
            "AI_RENDER_15_SUBCOUNCIL_HALL.jpg": "SYS_15: 8 Faculty Sub-Council Assembly Halls (Cantilever Clamshell)",
            "AI_RENDER_16_MODULAR_BUILDINGS.jpg": "SYS_16: Modular Civic & Academic Buildings (7,623 Stacked Floors)",
            "AI_RENDER_17_RESIDENTIAL_HOUSING_DORMS.jpg": "SYS_17: Modular Residential Housing & International Scholar Dorms",
        }

        for prefix, dest_name, fallback in AI_RENDER_MAPPING:
            dest_path = os.path.join(OUTPUT_BLUEPRINTS_DIR, dest_name)
            if os.path.exists(dest_path):
                title = render_titles.get(dest_name, dest_name.replace(".jpg", ""))
                f.write(f"### {title}\n")
                f.write(f"![{title}](./{dest_name})\n\n")

        f.write("---\n\n")
        f.write("## 2. Technical Orthographic CAD Blueprint Cards (1920x1080 Resolution)\n\n")
        f.write("Vector orthographic schematics and callout metrology diagrams for all 17 subsystems:\n\n")

        for spec in SUBSYSTEM_SPECS:
            card_file = f"{spec['num']}_BLUEPRINT_{spec['id']}.png"
            f.write(f"### {spec['id']}: {spec['name']}\n")
            f.write(f"![{card_file}](./{card_file})\n\n")

        f.write("---\n\n")
        f.write("## 3. Exhaustive Metrology & Engineering Specification Tables\n\n")
        f.write("Complete physical attributes, PCG archetypes, mass/buoyancy budgets, and zoning rules:\n\n")

        for spec in SUBSYSTEM_SPECS:
            f.write(f"### {spec['id']}: {spec['name']}\n\n")
            f.write(f"> **Canon Architecture Reference:** `{spec['canon']}`\n\n")

            f.write("| Specification Parameter | Canonical Engineering Value |\n")
            f.write("| :--- | :--- |\n")
            f.write(f"| **PCG Asset Archetype** | `{spec.get('archetype', 'N/A')}` |\n")
            f.write(f"| **Footprint Extent (W x L x H)** | `{spec.get('extent', spec['radius'])}` |\n")
            f.write(f"| **Elevation / Depth** | `{spec['elevation']}` |\n")
            f.write(f"| **Structural Mass** | `{spec['mass']}` |\n")
            f.write(f"| **Target Buoyancy Force** | `{spec.get('buoyancy', 'N/A')}` |\n")
            f.write(f"| **Pressure Resistance Rating** | `{spec.get('pressure', 'N/A')}` |\n")
            f.write(f"| **Zoning Allocation & Tags** | `{spec.get('zoning', 'N/A')}` |\n")
            f.write(f"| **Transit & Flow Integration** | {spec.get('transit', 'N/A')} |\n")
            f.write(f"| **Residential / Living Spec** | {spec.get('residential', 'N/A')} |\n")
            f.write(f"| **Operational Behavior States** | {spec['states']} |\n\n")

            f.write("**Coupling Sockets & Rig Interfaces:**\n")
            for sock in spec["sockets"]:
                f.write(f"- `{sock}`\n")
            f.write("\n")

            f.write("**Key Architectural Features:**\n")
            for feat in spec["features"]:
                f.write(f"- {feat}\n")
            f.write("\n---\n\n")

    print(f"  [+] Generated Master Blueprint Catalog: {md_path}")
# endregion


# region MAIN DISPATCHER
def main():
    print("================================================================================")
    print("ISTRORIGAN MEGASTRUCTURE - GENERATING ISOLATED SUBSYSTEM BLUEPRINT PACK")
    print("================================================================================")
    print("[1/3] Harvesting AI Generated Blueprint Renders (Parts 01 to 17)...")
    harvest_ai_renders()

    print("\n[2/3] Generating 1920x1080 High-Res Technical CAD Blueprint Cards (Parts 01 to 17)...")
    for spec in SUBSYSTEM_SPECS:
        draw_blueprint_card(spec)

    print("\n[3/3] Generating Master Blueprint Index Catalog...")
    generate_blueprint_index_md()

    print("================================================================================")
    print(f"[+] ALL BLUEPRINT ASSETS SUCCESSFULLY PRODUCED IN: {OUTPUT_BLUEPRINTS_DIR}")
    print("================================================================================")


if __name__ == "__main__":
    main()
# endregion
