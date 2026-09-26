// Copyright (c) 2026 HopeLess / Istrorigan Sanctuary. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "FC_PCG_Types.h"
#include "Materials/MaterialParameterCollection.h"
#include "FC_PCGRuntimeStateAdapter.generated.h"

DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FFC_OnAnnualCycleChanged, EFC_AnnualCycleState, PreviousState, EFC_AnnualCycleState, NewState);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FFC_OnSubmersionDepthUpdated, float, CurrentDepth_Meters, float, CurrentPressure_Bar);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FFC_OnBulkheadsToggled, bool, bIsWatertightSealed);

/**
 * ============================================================================
 * ISTRORIGAN RUNTIME STATE ADAPTER COMPONENT
 * ============================================================================
 * Coordinates megastructure transitions between Surface and Bi-Annual Submersion cycles:
 * - Updates Material Parameter Collection (MPC_IstroriganBarrier)
 * - Controls Hexagonal Energy Dome opacity and frequency
 * - Regulates Hydraulic Petal Pitch Angle (Normal 2.5 deg -> Dive Shield 18 deg)
 * - Simulates expanding ring ballast intake and hydrostatic pressure changes
 * ============================================================================
 */
UCLASS(ClassGroup = (FlowerCity), meta = (BlueprintSpawnableComponent))
class FLOWERCITYPCG_API UFC_PCGRuntimeStateAdapterComponent : public UActorComponent
{
	GENERATED_BODY()

public:
	UFC_PCGRuntimeStateAdapterComponent();

	virtual void BeginPlay() override;
	virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

#pragma region State Control Interface

	/** Transitions the city into a new annual cycle state (e.g. Summer Dive -500m or Winter Dive -1,000m) */
	UFUNCTION(BlueprintCallable, Category = "Istrorigan|Runtime")
	void SetAnnualCycleState(EFC_AnnualCycleState NewState, float TransitionDurationSeconds = 10.0f);

	/** Returns current active state */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Runtime")
	EFC_AnnualCycleState GetCurrentState() const { return CurrentCycleState; }

	/** Returns current depth in meters (negative when submerged) */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Runtime")
	float GetCurrentDepthMeters() const { return CurrentDepth_Meters; }

	/** Returns current hydraulic pitch angle of the 8 petals (Degrees) */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Runtime")
	float GetCurrentPetalPitchAngle() const { return CurrentPitchAngle_Deg; }

	/** Manually triggers emergency watertight bulkheads across all 8 petals and transit tubes */
	UFUNCTION(BlueprintCallable, Category = "Istrorigan|Runtime")
	void SetBulkheadsEmergencySealed(bool bSeal);

#pragma endregion State Control Interface

#pragma region Parameters & Configuration

	/** Material Parameter Collection for global visual synchronization (MPC_IstroriganBarrier) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Rendering")
	TSoftObjectPtr<UMaterialParameterCollection> BarrierMaterialParameterCollection;

	/** Name of scalar parameter for barrier shield activation (0.0 = off, 1.0 = fully energized) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Rendering")
	FName BarrierActivationParamName = FName(TEXT("Barrier_Hex_Dome_Active"));

	/** Name of scalar parameter for depth in meters */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Rendering")
	FName DepthParamName = FName(TEXT("Submersion_Depth_Meters"));

	/** Target depth for Summer Solstice Dive (Default -500.0m) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Cycle Config")
	float SummerDiveTargetDepth_M = -500.0f;

	/** Target depth for Winter Solstice Dive (Default -1000.0m) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Istrorigan|Cycle Config")
	float WinterDiveTargetDepth_M = -1000.0f;

#pragma endregion Parameters & Configuration

#pragma region Events & Delegates

	UPROPERTY(BlueprintAssignable, Category = "Istrorigan|Events")
	FFC_OnAnnualCycleChanged OnAnnualCycleStateChanged;

	UPROPERTY(BlueprintAssignable, Category = "Istrorigan|Events")
	FFC_OnSubmersionDepthUpdated OnSubmersionDepthUpdated;

	UPROPERTY(BlueprintAssignable, Category = "Istrorigan|Events")
	FFC_OnBulkheadsToggled OnBulkheadsToggled;

#pragma endregion Events & Delegates

protected:
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Istrorigan|State")
	EFC_AnnualCycleState CurrentCycleState = EFC_AnnualCycleState::Surface_Default;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Istrorigan|State")
	EFC_AnnualCycleState TargetCycleState = EFC_AnnualCycleState::Surface_Default;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Istrorigan|State")
	float CurrentDepth_Meters = 0.0f;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Istrorigan|State")
	float TargetDepth_Meters = 0.0f;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Istrorigan|State")
	float CurrentPitchAngle_Deg = 2.5f;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Istrorigan|State")
	float TargetPitchAngle_Deg = 2.5f;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Istrorigan|State")
	bool bBulkheadsSealed = false;

	float TransitionTimer = 0.0f;
	float TotalTransitionDuration = 1.0f;
	bool bIsTransitioning = false;

	void UpdateMaterialParameters();
};
