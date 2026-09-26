// Copyright (c) 2026 HopeLess / Istrorigan Sanctuary. All Rights Reserved.

#include "FC_PCGMathLibrary.h"

#pragma region Petal Geometry & Waterway Clearance

float UFC_PCGMathLibrary::EvaluatePetalHalfWidth(float U, const FFC_PetalGeometrySettings& Settings)
{
	const float ClampedU = FMath::Clamp(U, 0.0f, 1.0f);
	
	// Distance from city center origin to this point along the petal spine
	const float RadialDistance = Settings.BaseInnerRadius + (ClampedU * Settings.PetalLength);
	
	// Available angular sector per petal in radians: for 8 petals, DeltaTheta = 2*PI / 8 = 45 degrees (PI/4)
	const float HalfSlotAngleRad = (2.0f * PI / FMath::Max(Settings.PetalCount, 1)) * 0.5f;
	
	// Maximum allowable physical half-width before encroaching on adjacent petal sector
	// We subtract half of the required safety waterway clearance (e.g. 45m / 2 = 22.5m)
	const float MaxPermittedHalfWidth = (RadialDistance * FMath::Sin(HalfSlotAngleRad)) - (Settings.MinWaterwayClearance * 0.5f);
	const float SafeMaxHalfWidth = FMath::Max(MaxPermittedHalfWidth, 500.0f); // Minimum structural spine width (5m)

	// Parametric profile curve based on Houdini reference VEX
	const float SkewedV = FMath::Pow(ClampedU, Settings.WidthSkew);
	const float ProfileSin = FMath::Sin(PI * SkewedV);
	const float ProfileCurve = FMath::Pow(FMath::Max(ProfileSin, 0.0f), Settings.WidthProfilePower);
	
	// Nominal unconstrained half-width
	const float NominalHalfWidth = (Settings.PetalWidthMax * 0.5f) * ProfileCurve;

	// Hard clamp to guarantee 45m waterway clearance is strictly never violated
	return FMath::Min(NominalHalfWidth, SafeMaxHalfWidth);
}

float UFC_PCGMathLibrary::EvaluatePetalSurfaceZ(float U, float V, const FFC_PetalGeometrySettings& Settings)
{
	const float ClampedU = FMath::Clamp(U, 0.0f, 1.0f);
	const float ClampedV = FMath::Clamp(V, -1.0f, 1.0f);

	// Longitudinal shape envelope
	const float LongitudinalArch = FMath::Sin(PI * ClampedU);

	// Central keel ridge along spine (elevated at V = 0, tapering to edges)
	const float KeelRidgeZ = Settings.KeelHeight * (1.0f - FMath::Abs(ClampedV)) * FMath::Pow(LongitudinalArch, 0.65f);

	// Transverse cup hollow (bowl depression, dipping down away from spine)
	const float CupHollowZ = -Settings.CupDepth * (ClampedV * ClampedV) * LongitudinalArch;

	// Base surface deck elevation before tip leveling
	float RawZ = KeelRidgeZ + CupHollowZ;

	// Canon Law: Outer petal tip (U -> 1.0) must rest flat at sea level (Z = 0) for harbor berths
	if (Settings.bForceOuterTipAtSeaLevel)
	{
		const float FlatTipBlend = FMath::SmoothStep(0.70f, 1.0f, ClampedU);
		RawZ = FMath::Lerp(RawZ, 0.0f, FlatTipBlend);
	}

	return RawZ;
}

void UFC_PCGMathLibrary::ComputePetalSurfaceTransform(
	int32 PetalIndex,
	float U,
	float V,
	const FFC_PetalGeometrySettings& Settings,
	float CurrentFoldPitchAngle_Deg,
	FVector& OutLocation,
	FVector& OutNormal,
	FVector& OutTangent)
{
	const float ClampedU = FMath::Clamp(U, 0.0f, 1.0f);
	const float ClampedV = FMath::Clamp(V, -1.0f, 1.0f);

	// Master azimuth angle for this petal's center spine
	const float PetalStepDeg = 360.0f / FMath::Max(Settings.PetalCount, 1);
	const float PetalCenterAngleDeg = PetalIndex * PetalStepDeg;
	const float CenterAngleRad = FMath::DegreesToRadians(PetalCenterAngleDeg);

	// Direction unit vectors in horizontal plane
	const FVector RadialForwardDir = FVector(FMath::Cos(CenterAngleRad), FMath::Sin(CenterAngleRad), 0.0f);
	const FVector TransverseDir = FVector(-FMath::Sin(CenterAngleRad), FMath::Cos(CenterAngleRad), 0.0f);

	// Radial spine distance & lateral offset
	const float RadialDistance = Settings.BaseInnerRadius + (ClampedU * Settings.PetalLength);
	const float HalfWidth = EvaluatePetalHalfWidth(ClampedU, Settings);
	const float LateralOffset = ClampedV * HalfWidth;

	// Base deck elevation
	const float LocalSurfaceZ = EvaluatePetalSurfaceZ(ClampedU, ClampedV, Settings);

	// Hydraulic folding pitch articulation: rotation around hinge at BaseInnerRadius
	const float PitchRad = FMath::DegreesToRadians(CurrentFoldPitchAngle_Deg);
	const float FoldedSpineDistance = (ClampedU * Settings.PetalLength) * FMath::Cos(PitchRad);
	
	float TipPitchBlend = 1.0f;
	if (Settings.bForceOuterTipAtSeaLevel && ClampedU > 0.70f)
	{
		TipPitchBlend = 1.0f - FMath::SmoothStep(0.70f, 1.0f, ClampedU);
	}
	const float FoldedElevationOffset = (ClampedU * Settings.PetalLength) * FMath::Sin(PitchRad) * TipPitchBlend;

	// Final 3D Cartesian position
	const FVector SpineHingeBase = RadialForwardDir * Settings.BaseInnerRadius;
	const FVector SpinePos = SpineHingeBase + (RadialForwardDir * FoldedSpineDistance);
	OutLocation = SpinePos + (TransverseDir * LateralOffset) + FVector(0.0f, 0.0f, LocalSurfaceZ + FoldedElevationOffset);

	// Longitudinal Tangent vector (along U direction)
	const FVector FoldedForwardDir = (RadialForwardDir * FMath::Cos(PitchRad) + FVector(0.0f, 0.0f, FMath::Sin(PitchRad))).GetSafeNormal();
	OutTangent = FoldedForwardDir;

	// Surface Normal calculation (Cross product of Tangent U and Transverse V)
	// Compute finite difference for transverse slope
	const float DeltaV = 0.01f;
	const float LeftZ = EvaluatePetalSurfaceZ(ClampedU, FMath::Clamp(ClampedV - DeltaV, -1.0f, 1.0f), Settings);
	const float RightZ = EvaluatePetalSurfaceZ(ClampedU, FMath::Clamp(ClampedV + DeltaV, -1.0f, 1.0f), Settings);
	const float dZdV = (RightZ - LeftZ) / (2.0f * DeltaV * FMath::Max(HalfWidth, 1.0f));

	const FVector TransverseSlopeVector = (TransverseDir + FVector(0.0f, 0.0f, dZdV)).GetSafeNormal();
	OutNormal = FVector::CrossProduct(OutTangent, TransverseSlopeVector).GetSafeNormal();

	// Ensure normal points upward into sky
	if (OutNormal.Z < 0.0f)
	{
		OutNormal = -OutNormal;
	}
}

bool UFC_PCGMathLibrary::VerifyWaterwayClearance(
	int32 PetalIndex,
	float U,
	const FFC_PetalGeometrySettings& Settings,
	float& OutActualClearanceDistance)
{
	const float RadialDistance = Settings.BaseInnerRadius + (U * Settings.PetalLength);
	const float PetalStepDeg = 360.0f / FMath::Max(Settings.PetalCount, 1);
	const float HalfSlotAngleRad = FMath::DegreesToRadians(PetalStepDeg * 0.5f);

	// Total sector width between adjacent petal centerlines at this radius
	const float SectorChordDistance = 2.0f * RadialDistance * FMath::Sin(HalfSlotAngleRad);
	
	// Combined width of adjacent petals at this radius
	const float PetalWidth = EvaluatePetalHalfWidth(U, Settings) * 2.0f;

	// Remaining physical clearance gap (the waterway)
	OutActualClearanceDistance = SectorChordDistance - PetalWidth;

	return OutActualClearanceDistance >= Settings.MinWaterwayClearance;
}

#pragma endregion Petal Geometry & Waterway Clearance

#pragma region Submerged Expanding Rings & Ballast

float UFC_PCGMathLibrary::CalculateSubmergedRingRadiusAtDepth(float Depth_Z, const FFC_SubmergedRingSettings& Settings)
{
	// Depth_Z is negative cm (0 at surface down to -100,000 cm = -1,000m)
	const float MaxAbsDepth = FMath::Max(FMath::Abs(Settings.TotalSubmergedDepth), 1000.0f);
	const float NormalizedDepth = FMath::Clamp(-Depth_Z / MaxAbsDepth, 0.0f, 1.0f);

	// Flare curve: Radius expands wider and wider as depth increases!
	const float FlareCurve = FMath::Pow(NormalizedDepth, Settings.ExpansionExponent);
	const float ExpandedRadius = Settings.SurfaceNeckRadius + ((Settings.SeabedAbyssalRadius - Settings.SurfaceNeckRadius) * FlareCurve);

	return ExpandedRadius;
}

void UFC_PCGMathLibrary::ComputeSubmergedRingPoint(
	int32 TierIndex,
	float Angle_Deg,
	const FFC_SubmergedRingSettings& Settings,
	FVector& OutLocation,
	FRotator& OutOrientation,
	float& OutRingRadius)
{
	const int32 SafeTierCount = FMath::Max(Settings.RingTierCount, 1);
	const float NormalizedTier = (float)FMath::Clamp(TierIndex, 0, SafeTierCount - 1) / (float)(SafeTierCount - 1);
	
	// Vertical depth for this tier
	const float TierDepth_Z = NormalizedTier * Settings.TotalSubmergedDepth; // negative Z
	OutRingRadius = CalculateSubmergedRingRadiusAtDepth(TierDepth_Z, Settings);

	const float Rad = FMath::DegreesToRadians(Angle_Deg);
	OutLocation = FVector(OutRingRadius * FMath::Cos(Rad), OutRingRadius * FMath::Sin(Rad), TierDepth_Z);

	// Orientation facing outwards from center axis
	OutOrientation = FRotator(0.0f, Angle_Deg, 0.0f);
}

float UFC_PCGMathLibrary::CalculateHydrostaticPressure_Bar(float Depth_Z_cm)
{
	// 1 Bar ~= 10 meters = 1,000 cm depth of salt water (1025 kg/m^3)
	const float DepthMeters = FMath::Abs(Depth_Z_cm) / 100.0f;
	return 1.0f + (DepthMeters * 0.10055f); // 1 atm surface + depth pressure
}

#pragma endregion Submerged Expanding Rings & Ballast

#pragma region Citadel & Golden Stamen Pylons

void UFC_PCGMathLibrary::ComputeStamenPylonTransform(
	int32 StamenIndex,
	int32 TotalStamens,
	float ReceptacleRadius,
	float PylonHeight,
	float InwardLean_Deg,
	FVector& OutBaseLocation,
	FRotator& OutPylonRotation)
{
	const int32 SafeCount = FMath::Max(TotalStamens, 1);
	const float AzimuthDeg = (360.0f / (float)SafeCount) * StamenIndex;
	const float AzimuthRad = FMath::DegreesToRadians(AzimuthDeg);

	// Placed exactly along the perimeter of the circular receptacle
	OutBaseLocation = FVector(
		ReceptacleRadius * FMath::Cos(AzimuthRad),
		ReceptacleRadius * FMath::Sin(AzimuthRad),
		1200.0f // Elevated rim deck (12m above sea level)
	);

	// Rotates to face center and leans inward to form the conical forcefield cage
	// Yaw faces inward (AzimuthDeg + 180), Pitch tilts inward
	OutPylonRotation = FRotator(InwardLean_Deg, AzimuthDeg + 180.0f, 0.0f);
}

EFC_DistrictZone UFC_PCGMathLibrary::EvaluateZoningAtLocation(
	const FVector& WorldLocation,
	float U,
	float V,
	const FFC_PetalGeometrySettings& PetalSettings,
	const FFC_SubmergedRingSettings& SubmergedSettings)
{
	// Submerged Stem or Abyssal Root
	if (WorldLocation.Z < -5000.0f)
	{
		if (WorldLocation.Z < SubmergedSettings.TotalSubmergedDepth * 0.85f)
		{
			return EFC_DistrictZone::Root_AbyssalAnchor;
		}
		return EFC_DistrictZone::Stem_ExpandingRings;
	}

	const float Distance2D = WorldLocation.Size2D();

	// Central Citadel & Stamen Ring
	if (Distance2D <= PetalSettings.BaseInnerRadius)
	{
		if (Distance2D > PetalSettings.BaseInnerRadius * 0.80f)
		{
			return EFC_DistrictZone::Core_StamenRing;
		}
		return EFC_DistrictZone::Core_Civic;
	}

	// Clearance Waterways: Lateral boundaries of petals where |V| approaches 1.0
	if (FMath::Abs(V) > 0.92f)
	{
		return EFC_DistrictZone::Clearance_Waterway;
	}

	// Petal Sectors divided longitudinally along spine
	if (U < 0.25f)
	{
		return EFC_DistrictZone::Petal_InnerTransit;
	}
	else if (U < 0.75f)
	{
		return EFC_DistrictZone::Petal_MidLiving;
	}
	else
	{
		return EFC_DistrictZone::Petal_OuterTip;
	}
}

#pragma endregion Citadel & Golden Stamen Pylons
