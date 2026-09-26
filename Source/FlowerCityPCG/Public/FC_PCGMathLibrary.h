// Copyright (c) 2026 HopeLess / Istrorigan Sanctuary. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "FC_PCG_Types.h"
#include "FC_PCGMathLibrary.generated.h"

/**
 * ============================================================================
 * ISTRORIGAN PROCEDURAL MATH LIBRARY
 * ============================================================================
 * Mathematical foundations for:
 * 1. 8-Petal Parametric Geometry with 45m Waterway Clearance Enforcement
 * 2. Flat Tip Deck Alignment at Sea Level (Z = 0)
 * 3. Telescopic Submerged Ballast Rings with Non-Linear Abyssal Expansion Flare
 * 4. 70 Golden Stamen Forcefield Pylon Vector Transforms
 * ============================================================================
 */
UCLASS()
class FLOWERCITYPCG_API UFC_PCGMathLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

public:

#pragma region Petal Geometry & Waterway Clearance

	/**
	 * Calculates the half-width of a petal at normalized longitudinal parameter U [0.0 = Base, 1.0 = Tip].
	 * Clamps automatically to guarantee the 45m waterway clearance between adjacent petals.
	 */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Math|Petals")
	static float EvaluatePetalHalfWidth(float U, const FFC_PetalGeometrySettings& Settings);

	/**
	 * Calculates the local elevation Z on the petal surface taking into account:
	 * - Keel rib ridge along center spine (V = 0.0)
	 * - Transverse cup bowl hollow towards lateral edges (V = -1.0 or +1.0)
	 * - Forced leveling to Sea Level (Z = 0.0) at the outer tip (U = 1.0)
	 */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Math|Petals")
	static float EvaluatePetalSurfaceZ(float U, float V, const FFC_PetalGeometrySettings& Settings);

	/**
	 * Computes full 3D World Cartesian position, Surface Normal, and Longitudinal Tangent
	 * for a point on Petal[PetalIndex] at normalized coordinates (U, V).
	 */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Math|Petals")
	static void ComputePetalSurfaceTransform(
		int32 PetalIndex,
		float U,
		float V,
		const FFC_PetalGeometrySettings& Settings,
		float CurrentFoldPitchAngle_Deg,
		FVector& OutLocation,
		FVector& OutNormal,
		FVector& OutTangent
	);

	/**
	 * Calculates the physical clearance distance between the left edge of Petal[N] and right edge of Petal[N-1].
	 * Returns true if clearance meets or exceeds the required safety threshold (e.g. 45m).
	 */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Math|Petals")
	static bool VerifyWaterwayClearance(
		int32 PetalIndex,
		float U,
		const FFC_PetalGeometrySettings& Settings,
		float& OutActualClearanceDistance
	);

#pragma endregion Petal Geometry & Waterway Clearance

#pragma region Submerged Expanding Rings & Ballast

	/**
	 * Calculates the radius of the submerged structure at given depth Z (negative cm).
	 * Expanding flare formula: R(z) = NeckRadius + (AbyssalRadius - NeckRadius) * ((-Z) / MaxDepth)^Exponent.
	 */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Math|Submerged")
	static float CalculateSubmergedRingRadiusAtDepth(float Depth_Z, const FFC_SubmergedRingSettings& Settings);

	/**
	 * Computes the 3D world coordinate and orientation of a ring segment at given tier and polar angle.
	 */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Math|Submerged")
	static void ComputeSubmergedRingPoint(
		int32 TierIndex,
		float Angle_Deg,
		const FFC_SubmergedRingSettings& Settings,
		FVector& OutLocation,
		FRotator& OutOrientation,
		float& OutRingRadius
	);

	/**
	 * Calculates hydrostatic water pressure at given depth in Bar (1 Bar ~= 1,000 cm = 10m sea water).
	 */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Math|Physics")
	static float CalculateHydrostaticPressure_Bar(float Depth_Z_cm);

#pragma endregion Submerged Expanding Rings & Ballast

#pragma region Citadel & Golden Stamen Pylons

	/**
	 * Computes the world transform and inward lean for one of the 70 Golden Stamen Forcefield Pylons.
	 */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Math|Citadel")
	static void ComputeStamenPylonTransform(
		int32 StamenIndex,
		int32 TotalStamens,
		float ReceptacleRadius,
		float PylonHeight,
		float InwardLean_Deg,
		FVector& OutBaseLocation,
		FRotator& OutPylonRotation
	);

	/**
	 * Determines the district zoning type based on radial distance, depth, and normalized petal position.
	 */
	UFUNCTION(BlueprintPure, Category = "Istrorigan|Math|Zoning")
	static EFC_DistrictZone EvaluateZoningAtLocation(
		const FVector& WorldLocation,
		float U,
		float V,
		const FFC_PetalGeometrySettings& PetalSettings,
		const FFC_SubmergedRingSettings& SubmergedSettings
	);

#pragma endregion Citadel & Golden Stamen Pylons

};
