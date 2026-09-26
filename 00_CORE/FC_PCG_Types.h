#pragma once

#if __has_include("CoreMinimal.h")
#include "CoreMinimal.h"
#include "Engine/DataTable.h"
#include "GameplayTagContainer.h"
#include "Curves/CurveFloat.h"
#include "FC_PCG_Types.generated.h"
#else
// Fallback declarations for IDE standalone mode / code browsing outside Unreal Build Tool
#ifndef UENUM
#define UENUM(...)
#endif
#ifndef UMETA
#define UMETA(...)
#endif
#ifndef USTRUCT
#define USTRUCT(...)
#endif
#ifndef UPROPERTY
#define UPROPERTY(...)
#endif
#ifndef GENERATED_BODY
#define GENERATED_BODY(...)
#endif
#include <cstdint>
#include <string>
#include <vector>
using uint8 = std::uint8_t;
using int32 = std::int32_t;
struct FVector { float X = 0, Y = 0, Z = 0; static FVector ZeroVector; };
struct FGameplayTag { std::string Tag; };
struct FRuntimeFloatCurve {};
struct FTableRowBase {};
template<typename T> struct TArray : public std::vector<T> {};
template<typename T> struct TSoftObjectPtr { T* Ptr = nullptr; };
class UStaticMesh {};
#endif


/**
 * ============================================================================
 * FLOWER CITY PCG - CORE DATA CONTRACTS & TYPE DEFINITIONS
 * ============================================================================
 * Provides standardized USTRUCTs, UENUMs, and Data Table Schemas for:
 * 1. Radial/Polar Coordinate Mapping
 * 2. District Zoning & Spatial Allocations
 * 3. Module Archetypes, Mass & Buoyancy Properties
 * 4. Hardware Sockets & Snapping Compatibility Matrix
 * 5. Topological Gameplay Transit & Life Support Flow Graphs
 * ============================================================================
 */

#pragma region Enums

UENUM(BlueprintType)
enum class EFC_DistrictZone : uint8
{
    Core_Civic           UMETA(DisplayName = "Core: Civic & Master Control"),
    Petal_InnerTransit   UMETA(DisplayName = "Petal: Inner Transit Interchange"),
    Petal_MidLiving      UMETA(DisplayName = "Petal: Mid Habitation & Bio-Domes"),
    Petal_OuterTip       UMETA(DisplayName = "Petal: Outer Tip & Sea Harbor"),
    Stem_Engineering     UMETA(DisplayName = "Stem: Submerged Engineering & Ballast"),
    Root_AbyssalAnchor   UMETA(DisplayName = "Root: Abyssal Seabed Anchor Claws"),
    Shore_Perimeter      UMETA(DisplayName = "Shore: Perimeter Flotilla & Docks")
};

UENUM(BlueprintType)
enum class EFC_SocketType : uint8
{
    Structural_Hinge     UMETA(DisplayName = "Structural Hinge (Center-to-Petal)"),
    Structural_Girder    UMETA(DisplayName = "Rigid Structural Frame Girder"),
    Transit_Pedestrian   UMETA(DisplayName = "Pedestrian Corridor Walkway"),
    Transit_Maglev       UMETA(DisplayName = "High-Speed Maglev Rail Tube"),
    Transit_Submersible  UMETA(DisplayName = "Underwater Submersible Dock/Tube"),
    Utility_PowerGrid    UMETA(DisplayName = "High-Voltage Power Trunk Conduit"),
    Utility_LifeSupport  UMETA(DisplayName = "Oxygen & Freshwater Pipeline"),
    Facade_Mount         UMETA(DisplayName = "Surface Panel & Defense Mount"),
    Pylon_ForceField     UMETA(DisplayName = "Perimeter Force Field Pylon Joint")
};

UENUM(BlueprintType)
enum class EFC_SocketGender : uint8
{
    Male                 UMETA(DisplayName = "Male (Outward Insertion)"),
    Female               UMETA(DisplayName = "Female (Inward Receptor)"),
    Bilateral            UMETA(DisplayName = "Bilateral (Symmetric Coupling)")
};

UENUM(BlueprintType)
enum class EFC_ModuleSizeClass : uint8
{
    Small                UMETA(DisplayName = "Small (400 x 400 x 300 cm)"),
    Medium               UMETA(DisplayName = "Medium (1200 x 1200 x 600 cm)"),
    Large                UMETA(DisplayName = "Large (3000 x 3000 x 1800 cm)"),
    MegaStructure        UMETA(DisplayName = "MegaStructure (6000+ cm)")
};

UENUM(BlueprintType)
enum class EFC_CityGraphNodeType : uint8
{
    TransitHub           UMETA(DisplayName = "Transit Hub / Station"),
    PowerSubstation      UMETA(DisplayName = "Power Grid Substation"),
    LifeSupportTerminal  UMETA(DisplayName = "Oxygen & Water Terminal"),
    EvacuationShelter    UMETA(DisplayName = "Emergency Evacuation Bunker"),
    MaintenanceJunction  UMETA(DisplayName = "Engineering Maintenance Hub")
};

#pragma endregion Enums

#pragma region Spatial & Radial Coordinates

USTRUCT(BlueprintType)
struct FFC_RadialCoordinates
{
    GENERATED_BODY()

    /** Index of the petal (0 to TotalPetals - 1, clockwise from North) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Coordinates")
    int32 PetalIndex = 0;

    /** Radial concentric ring tier: 0 = Core, 1 = Inner, 2 = Mid, 3 = Tip, 4 = Outer */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Coordinates")
    int32 RingTier = 0;

    /** Distance from city master origin (0,0) in Centimeters (Unreal Units) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Coordinates")
    float RadialDistance = 0.0f;

    /** World polar angle (theta) in degrees [0.0, 360.0) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Coordinates")
    float Angle_Degrees = 0.0f;

    /** Normalized coordinate along petal longitudinal spine [0.0 = Base, 1.0 = Tip] */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Coordinates")
    float PetalU_Normalized = 0.0f;

    /** Normalized coordinate across petal lateral width [-1.0 = Left, 0.0 = Spine, +1.0 = Right] */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Coordinates")
    float PetalV_Normalized = 0.0f;

    /** Elevation offset relative to Sea Level (Z = 0.0 cm) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Coordinates")
    float Elevation_Z = 0.0f;

    /** Vertical layer tier: -2 = Abyssal, -1 = Submerged Stem, 0 = Water Surface, 1 = Surface Deck, 2 = Spire */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Coordinates")
    int32 VerticalTier = 0;

    /** Convert Radial Coordinates to World Cartesian Vector */
    FVector ToWorldCartesian(float PetalFoldPitchAngle = 0.0f) const
    {
        const float Rad = FMath::DegreesToRadians(Angle_Degrees);
        const float EffectiveRadius = RadialDistance * FMath::Cos(FMath::DegreesToRadians(PetalFoldPitchAngle));
        const float X = EffectiveRadius * FMath::Cos(Rad);
        const float Y = EffectiveRadius * FMath::Sin(Rad);
        const float Z = Elevation_Z + (RadialDistance * FMath::Sin(FMath::DegreesToRadians(PetalFoldPitchAngle)));
        return FVector(X, Y, Z);
    }
};

#pragma endregion Spatial & Radial Coordinates

#pragma region District Zoning Table Row

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

    /** Minimum distance from city center (cm) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
    float MinRadius = 0.0f;

    /** Maximum distance from city center (cm) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
    float MaxRadius = 100000.0f;

    /** Minimum allowable depth relative to sea level (cm) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
    float MinDepth_Z = -50000.0f;

    /** Maximum allowable elevation relative to sea level (cm) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
    float MaxElevation_Z = 20000.0f;

    /** Target buoyancy balance required for this district (kN, positive = floats, negative = ballasted) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
    float TargetBuoyancy_kN = 0.0f;

    /** Maximum allowable building height above deck (cm) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
    float MaxBuildingHeight = 4000.0f;

    /** Density falloff exponent: 1.0 = linear, 2.0 = exponential decay toward edges */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
    float DensityFalloffExponent = 1.0f;

    /** Gameplay tags of modules permitted to spawn in this zone */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Zoning")
    FGameplayTagContainer AllowedModuleTags;
};

#pragma endregion District Zoning Table Row

#pragma region Sockets & Snapping Matrix

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

    /** Local transform relative to parent module origin (X axis points forward along connection normal) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Socket")
    FTransform LocalTransform = FTransform::Identity;

    /** Sweep clearance bounding box (cm) centered around the connection port */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Socket")
    FVector ClearanceExtent = FVector(200.f, 200.f, 300.f);

    /** Compatibility tag requirements (e.g. "Socket.Watertight", "Socket.HighVoltage") */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Socket")
    FGameplayTagContainer CompatibilityTags;

    /** Runtime status tracking */
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

    /** Maximum angular deflection tolerated across the joint in degrees */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Compatibility")
    float MaxAngularTolerance_Deg = 5.0f;

    /** Maximum shear load tolerated by this joint in Kilo-Newtons (kN) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Compatibility")
    float MaxShearTolerance_kN = 1000.0f;

    /** Does this joint require a hermetic watertight seal? */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Compatibility")
    bool bRequiresWatertightSeal = false;
};

#pragma endregion Sockets & Snapping Matrix

#pragma region Asset Archetype Catalog

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

    /** Bounding dimensions in cm (Width, Length, Height) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    FVector FootprintExtent = FVector(1200.f, 1200.f, 600.f);

    /** Structural mass in Metric Tons */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    float StructuralMass_Tons = 1500.0f;

    /** Net buoyant lift force generated in sea water (kN) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    float BuoyancyForce_kN = 1800.0f;

    /** Maximum hydrodynamic pressure rating before hull breach (Bar) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    float PressureRating_Bar = 25.0f;

    /** Base PCG spawn weight before curve modulation */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    float BaseSpawnWeight = 100.0f;

    /** Modulates spawn weight based on depth (Z axis): 0m surface down to -500m abyssal */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    FRuntimeFloatCurve DepthWeightCurve;

    /** Modulates spawn weight based on normalized distance from center (U coordinate) */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    FRuntimeFloatCurve RadialWeightCurve;

    /** Minimum modules required per petal */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    int32 MinInstancesPerPetal = 1;

    /** Maximum modules permitted per petal */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    int32 MaxInstancesPerPetal = 10;

    /** Pre-defined sockets configured on this archetype */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    TArray<FFC_PCG_Socket> Sockets;

    /** Material variant tag: "Material.Surface.Clean", "Material.Submerged.Corroded", etc. */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    FGameplayTag MaterialProfileTag;

    /** LOD screen size thresholds [LOD0, LOD1, LOD2, LOD3] */
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Archetype")
    TArray<float> LODScreenSizes = { 0.6f, 0.3f, 0.15f, 0.05f };
};

#pragma endregion Asset Archetype Catalog

#pragma region Gameplay & Flow Networks

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
