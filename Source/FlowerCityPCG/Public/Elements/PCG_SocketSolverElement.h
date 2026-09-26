// Copyright (c) 2026 HopeLess / Istrorigan Sanctuary. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "PCGSettings.h"
#include "PCGElement.h"
#include "FC_PCG_Types.h"
#include "PCG_SocketSolverElement.generated.h"

/**
 * ============================================================================
 * PCG NODE: SOCKET SOLVER & CLEARANCE ENFORCER
 * ============================================================================
 * Solves modular snap connections against DT_Socket_Compatibility_Matrix:
 * - Enforces Male-to-Female or Bilateral pairing
 * - Validates Watertight Seal requirement for submerged Z < 0 modules
 * - Discards overlapping module bounding boxes
 * - Outputs Validated Connected Points and Rejected/Pruned Points
 * ============================================================================
 */
UCLASS(BlueprintType, ClassGroup = (Procedural))
class FLOWERCITYPCG_API UPCG_SocketSolverSettings : public UPCGSettings
{
	GENERATED_BODY()

public:
	UPCG_SocketSolverSettings();

#pragma region UPCGSettings Interface
	virtual FName GetDefaultNodeName() const override { return FName(TEXT("SolveSocketsAndClearance")); }
	virtual FText GetDefaultNodeTitle() const override { return NSLOCTEXT("FlowerCityPCG", "SocketSolverTitle", "Solve Sockets & Clearance"); }
	virtual FText GetNodeTooltipText() const override { return NSLOCTEXT("FlowerCityPCG", "SocketSolverTooltip", "Validates socket pairing, angular deflection, watertight requirements, and spatial clearance."); }
	virtual EPCGSettingsType GetType() const override { return EPCGSettingsType::Spatial; }

protected:
	virtual TArray<FPCGPinProperties> InputPinProperties() const override;
	virtual TArray<FPCGPinProperties> OutputPinProperties() const override;
	virtual FPCGElementPtr CreateElement() const override;
#pragma endregion UPCGSettings Interface

public:
#pragma region Solver Parameters

	/** Reference to DT_Socket_Compatibility_Matrix data table */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Sockets|Rules")
	TSoftObjectPtr<UDataTable> SocketCompatibilityTable;

	/** Enforces watertight integrity on all sockets with negative elevation (Z < 0 cm) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Sockets|Rules")
	bool bStrictWatertightCheckSubmerged = true;

	/** Maximum search radius to discover matching counterpart sockets (Centimeters) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Sockets|Search")
	float SnapToleranceRadius = 350.0f;

	/** Maximum angular misalignment tolerated between opposing sockets (Degrees) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Sockets|Search")
	float MaxAngularTolerance_Deg = 7.5f;

#pragma endregion Solver Parameters
};

class FPCG_SocketSolverElement : public IPCGElement
{
protected:
	virtual bool ExecuteInternal(FPCGContext* Context) const override;
};
