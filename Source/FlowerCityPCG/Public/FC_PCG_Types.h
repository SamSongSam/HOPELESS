// Copyright (c) 2026 HopeLess / Istrorigan Sanctuary. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Engine/DataTable.h"
#include "GameplayTagContainer.h"
#include "Curves/CurveFloat.h"
#include "FC_PCG_Types.generated.h"

/**
 * ============================================================================
 * ISTRORIGAN MEGASTRUCTURE (YEAR 4205) - PROCEDURAL CONTENT GENERATION TYPES
 * ============================================================================
 * Central Sovereign Sanctuary of the 17 Post-Deluge Great States.
 * Ruled by the Council of Ten at the Central Spire, with 8 Specialized Petals.
 * Features 8 discrete non-overlapping petals, expanding underwater ballast rings,
 * and a bi-annual deep submersion cycle (-500m / -1,000m).
 * ============================================================================
 */

#pragma region Enums - World & Governance

UENUM(BlueprintType)
enum class EFC_AnnualCycleState : uint8
{
	Surface_Default              UMETA(DisplayName = "Surface Default (Z = 0m, Harbors Active, Hex Shield Standby)"),
	Summer_Solstice_Dive_500m    UMETA(DisplayName = "Summer Solstice Dive (-500m, Marine Biology Research, Hex Shield 100%)"),
	Winter_Solstice_Dive_1000m   UMETA(DisplayName = "Winter Solstice Dive (-1,000m, Abyssal Physics Test, Bulkheads Sealed)"),
	Ascending_Surface            UMETA(DisplayName = "Ascending to Surface (Ballast Purge, Pressure Equalization)")
};

UENUM(BlueprintType)
enum class EFC_PetalAffiliation : uint8
{
	Petal_1_MarineBiosphere      UMETA(DisplayName = "Petal 1: Marine Biosphere & Oceanic Botany"),
	Petal_2_HighEnergyPhysics    UMETA(DisplayName = "Petal 2: High-Energy Plasma & Fusion Core"),
	Petal_3_HydraulicCybernetics UMETA(DisplayName = "Petal 3: Hydraulic Cybernetics & Robotics"),
	Petal_4_DeepGeologyMining    UMETA(DisplayName = "Petal 4: Abyssal Geology & Tectonic Claws"),
	Petal_5_AtmosphereMeteorology UMETA(DisplayName = "Petal 5: Atmospheric Control & Weather Spire"),
	Petal_6_GlobalArchivalData   UMETA(DisplayName = "Petal 6: Quantum Archives & Knowledge Vaults"),
	Petal_7_DiplomaticAssembly   UMETA(DisplayName = "Petal 7: Diplomatic Assembly of 17 Great States"),
	Petal_8_MedicalCryogenics    UMETA(DisplayName = "Petal 8: Pan-Pathology & Cryogenic Sanctuaries"),
	CenterCore_Citadel           UMETA(DisplayName = "Citadel: Apex Spire & Council of Ten Seat")
};

UENUM(BlueprintType)
enum class EFC_DistrictZone : uint8
{
	Core_Civic                   UMETA(DisplayName = "Core: Council of 10 Citadel & Central Receptacle"),
	Core_StamenRing              UMETA(DisplayName = "Core: 70 Golden Stamen Forcefield Ring"),
	Petal_InnerTransit           UMETA(DisplayName = "Petal: Inner Arterial Interchange & Monorail Terminal"),
	Petal_MidLiving              UMETA(DisplayName = "Petal: University Campuses, Biospheres & Dwellings"),
	Petal_OuterTip               UMETA(DisplayName = "Petal: Outer Tip Ocean-Level Harbor & Research Berths"),
	Stem_ExpandingRings          UMETA(DisplayName = "Stem: Telescopic Expanding Underwater Ballast Rings"),
	Root_AbyssalAnchor           UMETA(DisplayName = "Root: Abyssal Knowledge Vault & Trench Anchors"),
	Clearance_Waterway           UMETA(DisplayName = "Safety: 45m Hydraulic Articulation Waterway")
};

#pragma endregion Enums - World & Governance

#pragma region Enums - Modular Hardware & Sockets

UENUM(BlueprintType)
enum class EFC_SocketType : uint8
{
	Structural_Hinge             UMETA(DisplayName = "Structural Hinge (Citadel-to-Petal Joint)"),
	Structural_Girder            UMETA(DisplayName = "Rigid Structural Frame Girder"),
	Transit_Pedestrian           UMETA(DisplayName = "Pedestrian Pressurized Walkway"),
	Transit_Maglev               UMETA(DisplayName = "High-Speed Maglev Evacuation Rail"),
	Transit_Submersible          UMETA(DisplayName = "Submersible Docking Collar"),
	Utility_PowerGrid            UMETA(DisplayName = "High-Voltage Superconducting Conduit"),
	Utility_LifeSupport          UMETA(DisplayName = "Freshwater & Oxygen Mainline"),
	Facade_Mount                 UMETA(DisplayName = "Hexagonal Armor / Absorber Mount"),
	Pylon_ForceField             UMETA(DisplayName = "Golden Stamen Forcefield Emitter Coupling")
};

UENUM(BlueprintType)
enum class EFC_SocketGender : uint8
{
	Male                         UMETA(DisplayName = "Male (Outward Coupling)"),
	Female                       UMETA(DisplayName = "Female (Inward Receptor)"),
	Bilateral                    UMETA(DisplayName = "Bilateral (Hermetic Symmetric Latch)")
};

UENUM(BlueprintType)
enum class EFC_ModuleSizeClass : uint8
{
	Small                        UMETA(DisplayName = "Small (400 x 400 x 300 cm)"),
	Medium                       UMETA(DisplayName = "Medium (1200 x 1200 x 600 cm)"),
	Large                        UMETA(DisplayName = "Large (3000 x 3000 x 1800 cm)"),
	MegaStructure                UMETA(DisplayName = "MegaStructure (6000+ cm)")
};

#pragma endregion Enums - Modular Hardware & Sockets

#pragma region Structs - Parametric Geometry & Math Settings

USTRUCT(BlueprintType)
struct FFC_PetalGeometrySettings
{
	GENERATED_BODY()

	/** Total distinct petals around city perimeter (Canon: exactly 8) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals", meta = (ClampMin = "3", ClampMax = "16"))
	int32 PetalCount = 8;

	/** Radial distance from city origin to inner hinge base of petals (Centimeters: default 150m = 15,000 cm) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals")
	float BaseInnerRadius = 15000.0f;

	/** Length along petal longitudinal spine from base to tip (Centimeters: default 950m = 95,000 cm, tip at 110,000 cm) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals")
	float PetalLength = 95000.0f;

	/** Maximum width of petal at its widest bulge (Centimeters: default 420m = 42,000 cm) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals")
	float PetalWidthMax = 42000.0f;

	/** Minimum safety clearance between adjacent petals to prevent collision during hydraulic pitch (Centimeters: default 45m = 4,500 cm) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals")
	float MinWaterwayClearance = 4500.0f;

	/** Outward width profile power (>1 = pointier, <1 = blockier) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals Profile")
	float WidthProfilePower = 1.20f;

	/** Widest point bias along spine (0.0 = base, 0.5 = mid, 1.0 = tip) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals Profile")
	float WidthSkew = 0.52f;

	/** Transverse cross-section hollow bowl curvature (Cup factor in cm) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals Curvature")
	float CupDepth = 3500.0f;

	/** Central keel rib vertical elevation offset (Centimeters) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals Curvature")
	float KeelHeight = 2200.0f;

	/** Pitch angle in degrees for petals during normal surface operations (Degrees) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals Articulation")
	float OperatingPitchAngle_Deg = 2.5f;

	/** Pitch angle in degrees when folded upward in storm / dive shield mode (Degrees) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals Articulation")
	float DiveShieldPitchAngle_Deg = 18.0f;

	/** Ensures outer tip deck is completely flat and level with sea level (Z = 0) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Petals Alignment")
	bool bForceOuterTipAtSeaLevel = true;
};

USTRUCT(BlueprintType)
struct FFC_SubmergedRingSettings
{
	GENERATED_BODY()

	/** Total number of expanding telescopic ring tiers descending into the deep (Canon: 12 tiers) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|SubmergedRings", meta = (ClampMin = "3", ClampMax = "24"))
	int32 RingTierCount = 12;

	/** Radius of the uppermost submerged collar at the neck of the citadel (Centimeters: default 80m = 8,000 cm) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|SubmergedRings")
	float SurfaceNeckRadius = 8000.0f;

	/** Radius of the lowermost ring anchored into the seabed (Centimeters: default 350m = 35,000 cm - expanding flare!) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|SubmergedRings")
	float SeabedAbyssalRadius = 35000.0f;

	/** Total depth span of submerged rings (Centimeters: default -900m = -90,000 cm) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|SubmergedRings")
	float TotalSubmergedDepth = -90000.0f;

	/** Radial expansion flare exponent: 1.0 = cone, >1.0 = bell curve flare out near base for extreme low center-of-gravity */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|SubmergedRings")
	float ExpansionExponent = 1.65f;

	/** Wall thickness of each ring section (Centimeters) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|SubmergedRings")
	float RingWallThickness = 2800.0f;

	/** Total ballast water intake capacity across all ring tanks (Cubic Meters) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|SubmergedRings")
	float TotalBallastCapacity_m3 = 18500000.0f;
};

USTRUCT(BlueprintType)
struct FFC_RadialCoordinates
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Coordinates")
	int32 PetalIndex = 0;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Coordinates")
	int32 RingTier = 0;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Coordinates")
	float RadialDistance = 0.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Coordinates")
	float Angle_Degrees = 0.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Coordinates")
	float PetalU_Normalized = 0.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Coordinates")
	float PetalV_Normalized = 0.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Coordinates")
	float Elevation_Z = 0.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Coordinates")
	int32 VerticalTier = 0;

	FVector ToWorldCartesian(float PetalFoldPitchAngle = 0.0f) const
	{
		const float Rad = FMath::DegreesToRadians(Angle_Degrees);
		const float PitchRad = FMath::DegreesToRadians(PetalFoldPitchAngle);
		const float EffectiveRadius = RadialDistance * FMath::Cos(PitchRad);
		const float X = EffectiveRadius * FMath::Cos(Rad);
		const float Y = EffectiveRadius * FMath::Sin(Rad);
		const float Z = Elevation_Z + (RadialDistance * FMath::Sin(PitchRad));
		return FVector(X, Y, Z);
	}
};

#pragma endregion Structs - Parametric Geometry & Math Settings

#pragma region Structs - Data Table Rows

USTRUCT(BlueprintType)
struct FFC_DistrictZoningRule : public FTableRowBase
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
	EFC_DistrictZone DistrictType = EFC_DistrictZone::Petal_MidLiving;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
	FString ZoneDisplayName;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
	int32 RingTier = 0;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
	float MinRadius = 0.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
	float MaxRadius = 150000.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
	float MinDepth_Z = -100000.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
	float MaxElevation_Z = 65000.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
	float TargetBuoyancy_kN = 0.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
	float MaxBuildingHeight = 4000.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
	float DensityFalloffExponent = 1.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
	FGameplayTagContainer AllowedModuleTags;
};

USTRUCT(BlueprintType)
struct FFC_PCG_Socket
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Socket")
	FName SocketName;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Socket")
	EFC_SocketType SocketType = EFC_SocketType::Structural_Girder;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Socket")
	EFC_SocketGender Gender = EFC_SocketGender::Bilateral;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Socket")
	FTransform LocalTransform = FTransform::Identity;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Socket")
	FVector ClearanceExtent = FVector(200.f, 200.f, 300.f);

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Socket")
	FGameplayTagContainer CompatibilityTags;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Socket")
	bool bIsOccupied = false;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Socket")
	int32 ConnectedModuleUID = -1;
};

USTRUCT(BlueprintType)
struct FFC_SocketCompatibilityRule : public FTableRowBase
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Compatibility")
	EFC_SocketType SourceSocketType = EFC_SocketType::Transit_Pedestrian;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Compatibility")
	EFC_SocketType TargetSocketType = EFC_SocketType::Transit_Pedestrian;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Compatibility")
	bool bAllowSameGender = false;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Compatibility")
	float MaxAngularTolerance_Deg = 5.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Compatibility")
	float MaxShearTolerance_kN = 1000.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Compatibility")
	bool bRequiresWatertightSeal = false;
};

USTRUCT(BlueprintType)
struct FFC_AssetArchetype : public FTableRowBase
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	FName ArchetypeID;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	FString DisplayName;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	EFC_ModuleSizeClass SizeClass = EFC_ModuleSizeClass::Medium;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	TSoftObjectPtr<UStaticMesh> MeshAsset;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	FVector FootprintExtent = FVector(1200.f, 1200.f, 600.f);

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	float StructuralMass_Tons = 1500.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	float BuoyancyForce_kN = 1800.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	float PressureRating_Bar = 25.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	float BaseSpawnWeight = 100.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	FRuntimeFloatCurve DepthWeightCurve;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	FRuntimeFloatCurve RadialWeightCurve;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	int32 MinInstancesPerPetal = 1;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	int32 MaxInstancesPerPetal = 10;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	TArray<FFC_PCG_Socket> Sockets;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	FGameplayTag MaterialProfileTag;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
	TArray<float> LODScreenSizes = { 0.6f, 0.3f, 0.15f, 0.05f };
};

#pragma endregion Structs - Data Table Rows

#pragma region Gameplay & Flow Networks

UENUM(BlueprintType)
enum class EFC_CityGraphNodeType : uint8
{
	TransitHub           UMETA(DisplayName = "Transit Hub / Station"),
	PowerSubstation      UMETA(DisplayName = "Power Grid Substation"),
	LifeSupportTerminal  UMETA(DisplayName = "Oxygen & Water Terminal"),
	EvacuationShelter    UMETA(DisplayName = "Emergency Evacuation Bunker"),
	MaintenanceJunction  UMETA(DisplayName = "Engineering Maintenance Hub")
};

USTRUCT(BlueprintType)
struct FFC_CityGraphNode
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	int32 NodeID = 0;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	FVector WorldLocation = FVector::ZeroVector;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	EFC_CityGraphNodeType NodeType = EFC_CityGraphNodeType::TransitHub;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	int32 PetalIndex = -1; // -1 = Core Center

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	TArray<int32> ConnectedEdgeIDs;

	/** Maximum passenger or resource capacity */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	float Capacity = 5000.0f;

	/** Current throughput or occupancy */
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Graph")
	float CurrentFlowRate = 0.0f;

	/** Is node functioning normally or flooded/quarantined? */
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Graph")
	bool bIsOperational = true;
};

USTRUCT(BlueprintType)
struct FFC_CityGraphEdge
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	int32 EdgeID = 0;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	int32 StartNodeID = 0;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	int32 EndNodeID = 0;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	FGameplayTag EdgeTypeTag; // e.g. "Graph.Edge.MaglevSpine", "Graph.Edge.OxygenMainTrunk"

	/** Spline control points representing physical path */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	TArray<FVector> SplinePoints;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	float Length_Meters = 0.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Graph")
	float MaxThroughput = 1000.0f;

	/** Sealed watertight bulkhead status */
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Graph")
	bool bIsBulkheadSealed = false;
};

#pragma endregion Gameplay & Flow Networks

