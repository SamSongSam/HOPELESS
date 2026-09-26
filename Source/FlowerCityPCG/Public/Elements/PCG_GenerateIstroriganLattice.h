// Copyright (c) 2026 HopeLess / Istrorigan Sanctuary. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "PCGSettings.h"
#include "PCGElement.h"
#include "FC_PCG_Types.h"
#include "PCG_GenerateIstroriganLattice.generated.h"

/**
 * ============================================================================
 * PCG NODE: GENERATE ISTRORIGAN LATTICE
 * ============================================================================
 * Generates the master structural point cloud for the Istrorigan Megastructure:
 * - 8 discrete non-overlapping petals with 45m waterway clearance
 * - Central Receptacle & Council of Ten Citadel
 * - 70 Golden Stamen Forcefield Pylon Anchors
 * - 12 Telescopic Expanding Underwater Ballast Rings down to -1,000m
 * ============================================================================
 */
UCLASS(BlueprintType, ClassGroup = (Procedural))
class FLOWERCITYPCG_API UPCG_GenerateIstroriganLatticeSettings : public UPCGSettings
{
	GENERATED_BODY()

public:
	UPCG_GenerateIstroriganLatticeSettings();

#pragma region UPCGSettings Interface
	virtual FName GetDefaultNodeName() const override { return FName(TEXT("GenerateIstroriganLattice")); }
	virtual FText GetDefaultNodeTitle() const override { return NSLOCTEXT("FlowerCityPCG", "GenerateIstroriganLatticeTitle", "Generate Istrorigan Lattice (4205)"); }
	virtual FText GetNodeTooltipText() const override { return NSLOCTEXT("FlowerCityPCG", "GenerateIstroriganLatticeTooltip", "Generates the complete 8-petal and expanding underwater ballast lattice for Istrorigan."); }
	virtual EPCGSettingsType GetType() const override { return EPCGSettingsType::Spatial; }

protected:
	virtual TArray<FPCGPinProperties> InputPinProperties() const override;
	virtual TArray<FPCGPinProperties> OutputPinProperties() const override;
	virtual FPCGElementPtr CreateElement() const override;
#pragma endregion UPCGSettings Interface

public:
#pragma region Petal Generation Parameters

	/** Master settings for petal geometry and clearance */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Petals")
	FFC_PetalGeometrySettings PetalSettings;

	/** Resolution along petal length (U axis) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Petals|Resolution", meta = (ClampMin = "5", ClampMax = "120"))
	int32 PetalUSteps = 36;

	/** Resolution across petal width (V axis) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Petals|Resolution", meta = (ClampMin = "3", ClampMax = "60"))
	int32 PetalVSteps = 19;

	/** Current fold pitch angle for runtime articulation preview (Degrees) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Petals|Articulation", meta = (ClampMin = "0.0", ClampMax = "45.0"))
	float RuntimePitchAngle_Deg = 2.5f;

#pragma endregion Petal Generation Parameters

#pragma region Submerged Rings Parameters

	/** Master settings for expanding underwater ballast rings */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Submerged Rings")
	FFC_SubmergedRingSettings SubmergedSettings;

	/** Radial point resolution per ring tier */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Submerged Rings|Resolution", meta = (ClampMin = "12", ClampMax = "128"))
	int32 RingAngularResolution = 48;

#pragma endregion Submerged Rings Parameters

#pragma region Central Citadel & Stamens

	/** Radius of the central circular receptacle platform (Centimeters: default 150m = 15,000 cm) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Citadel")
	float ReceptacleRadius = 15000.0f;

	/** Total stamen forcefield pylons around perimeter (Canon: exactly 70) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Citadel")
	int32 StamenCount = 70;

	/** Height of each golden stamen pylon (Centimeters: default 45m = 4,500 cm, matching ARCH_BARRIER_PYLON_TOWER) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Citadel")
	float StamenHeight = 4500.0f;

	/** Inward lean angle for stamens (Degrees) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Citadel")
	float StamenInwardLean_Deg = 14.0f;

	/** Height of the Council of Ten Apex Spire (Centimeters: default 350m = 35,000 cm, matching ZONE_CORE_CITADEL) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Citadel")
	float ApexSpireHeight = 35000.0f;

#pragma endregion Central Citadel & Stamens
};

/**
 * Execution element for generating the Istrorigan point cloud
 */
class FPCG_GenerateIstroriganLatticeElement : public IPCGElement
{
protected:
	virtual bool ExecuteInternal(FPCGContext* Context) const override;
};
