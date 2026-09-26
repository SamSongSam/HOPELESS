// Copyright (c) 2026 HopeLess / Istrorigan Sanctuary. All Rights Reserved.

#include "Runtime/FC_PCGRuntimeStateAdapter.h"
#include "FC_PCGMathLibrary.h"
#include "Materials/MaterialParameterCollectionInstance.h"
#include "Kismet/KismetMaterialLibrary.h"

UFC_PCGRuntimeStateAdapterComponent::UFC_PCGRuntimeStateAdapterComponent()
{
	PrimaryComponentTick.bCanEverTick = true;
	PrimaryComponentTick.bStartWithTickEnabled = true;
}

void UFC_PCGRuntimeStateAdapterComponent::BeginPlay()
{
	Super::BeginPlay();
	UpdateMaterialParameters();
}

void UFC_PCGRuntimeStateAdapterComponent::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

	if (bIsTransitioning)
	{
		TransitionTimer += DeltaTime;
		const float Alpha = FMath::Clamp(TransitionTimer / FMath::Max(TotalTransitionDuration, 0.001f), 0.0f, 1.0f);
		const float SmoothAlpha = FMath::SmoothStep(0.0f, 1.0f, Alpha);

		// Interpolate Depth and Petal Pitch Angle
		CurrentDepth_Meters = FMath::Lerp(CurrentDepth_Meters, TargetDepth_Meters, SmoothAlpha);
		CurrentPitchAngle_Deg = FMath::Lerp(CurrentPitchAngle_Deg, TargetPitchAngle_Deg, SmoothAlpha);

		// Calculate Current Pressure in Bar
		const float CurrentPressure = UFC_PCGMathLibrary::CalculateHydrostaticPressure_Bar(CurrentDepth_Meters * 100.0f);
		OnSubmersionDepthUpdated.Broadcast(CurrentDepth_Meters, CurrentPressure);

		UpdateMaterialParameters();

		if (Alpha >= 1.0f)
		{
			bIsTransitioning = false;
			CurrentCycleState = TargetCycleState;
			CurrentDepth_Meters = TargetDepth_Meters;
			CurrentPitchAngle_Deg = TargetPitchAngle_Deg;
		}
	}
}

void UFC_PCGRuntimeStateAdapterComponent::SetAnnualCycleState(EFC_AnnualCycleState NewState, float TransitionDurationSeconds)
{
	if (NewState == CurrentCycleState && !bIsTransitioning)
	{
		return;
	}

	const EFC_AnnualCycleState OldState = CurrentCycleState;
	TargetCycleState = NewState;
	TotalTransitionDuration = FMath::Max(TransitionDurationSeconds, 1.0f);
	TransitionTimer = 0.0f;
	bIsTransitioning = true;

	switch (NewState)
	{
	case EFC_AnnualCycleState::Surface_Default:
		TargetDepth_Meters = 0.0f;
		TargetPitchAngle_Deg = 2.5f; // Flat tip rest mode
		SetBulkheadsEmergencySealed(false);
		break;

	case EFC_AnnualCycleState::Summer_Solstice_Dive_500m:
		TargetDepth_Meters = SummerDiveTargetDepth_M;
		TargetPitchAngle_Deg = 16.0f; // Protective folded angle
		SetBulkheadsEmergencySealed(true);
		break;

	case EFC_AnnualCycleState::Winter_Solstice_Dive_1000m:
		TargetDepth_Meters = WinterDiveTargetDepth_M;
		TargetPitchAngle_Deg = 18.0f; // Maximum hydrodynamic dive pitch
		SetBulkheadsEmergencySealed(true);
		break;

	case EFC_AnnualCycleState::Ascending_Surface:
		TargetDepth_Meters = 0.0f;
		TargetPitchAngle_Deg = 8.0f; // Intermediate ascent pitch
		break;
	}

	OnAnnualCycleStateChanged.Broadcast(OldState, NewState);
}

void UFC_PCGRuntimeStateAdapterComponent::SetBulkheadsEmergencySealed(bool bSeal)
{
	if (bBulkheadsSealed != bSeal)
	{
		bBulkheadsSealed = bSeal;
		OnBulkheadsToggled.Broadcast(bBulkheadsSealed);
	}
}

void UFC_PCGRuntimeStateAdapterComponent::UpdateMaterialParameters()
{
	UWorld* World = GetWorld();
	if (!World)
	{
		return;
	}

	UMaterialParameterCollection* MPC = BarrierMaterialParameterCollection.LoadSynchronous();
	if (!MPC)
	{
		return;
	}

	// Calculate barrier intensity: 0.25 on surface standby, ramp up to 1.0 when submerged deeper than -50m
	const float NormalizedSubmersion = FMath::Clamp(-CurrentDepth_Meters / 100.0f, 0.0f, 1.0f);
	const float BarrierIntensity = FMath::Lerp(0.25f, 1.0f, NormalizedSubmersion);

	UKismetMaterialLibrary::SetScalarParameterValue(World, MPC, BarrierActivationParamName, BarrierIntensity);
	UKismetMaterialLibrary::SetScalarParameterValue(World, MPC, DepthParamName, CurrentDepth_Meters);
}
