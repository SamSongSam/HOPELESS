// Copyright (c) 2026 HopeLess / Istrorigan Sanctuary. All Rights Reserved.

#include "Elements/PCG_GenerateIstroriganLattice.h"
#include "FC_PCGMathLibrary.h"
#include "Data/PCGPointData.h"
#include "Metadata/PCGMetadata.h"
#include "Metadata/PCGMetadataAccessor.h"
#include "PCGContext.h"
#include "PCGPin.h"

UPCG_GenerateIstroriganLatticeSettings::UPCG_GenerateIstroriganLatticeSettings()
{
	bUseSeed = true;
}

TArray<FPCGPinProperties> UPCG_GenerateIstroriganLatticeSettings::InputPinProperties() const
{
	// Self-generating generator node - no input pins required
	return TArray<FPCGPinProperties>();
}

TArray<FPCGPinProperties> UPCG_GenerateIstroriganLatticeSettings::OutputPinProperties() const
{
	TArray<FPCGPinProperties> PinProperties;
	
	// Default master combined output pin
	PinProperties.Emplace(PCGPinConstants::DefaultOutputLabel, EPCGDataType::Point);

	// Dedicated component output pins for isolated subgraph routing
	PinProperties.Emplace(FName(TEXT("Petals")), EPCGDataType::Point, false, false, NSLOCTEXT("FlowerCityPCG", "PetalsPinTooltip", "8 Discrete Articulated Petals Point Cloud"));
	PinProperties.Emplace(FName(TEXT("Citadel")), EPCGDataType::Point, false, false, NSLOCTEXT("FlowerCityPCG", "CitadelPinTooltip", "Council of Ten Central Citadel Spire Points"));
	PinProperties.Emplace(FName(TEXT("Stamens")), EPCGDataType::Point, false, false, NSLOCTEXT("FlowerCityPCG", "StamensPinTooltip", "70 Golden Stamen Forcefield Pylons"));
	PinProperties.Emplace(FName(TEXT("SubmergedRings")), EPCGDataType::Point, false, false, NSLOCTEXT("FlowerCityPCG", "SubmergedRingsPinTooltip", "12 Telescopic Expanding Ballast Rings"));

	return PinProperties;
}

FPCGElementPtr UPCG_GenerateIstroriganLatticeSettings::CreateElement() const
{
	return MakeShared<FPCG_GenerateIstroriganLatticeElement>();
}

bool FPCG_GenerateIstroriganLatticeElement::ExecuteInternal(FPCGContext* Context) const
{
	check(Context);

	const UPCG_GenerateIstroriganLatticeSettings* Settings = Context->GetInputSettings<UPCG_GenerateIstroriganLatticeSettings>();
	check(Settings);

	// Allocate point datasets for each pin
	UPCGPointData* MasterPointData = NewObject<UPCGPointData>();
	UPCGPointData* PetalsPointData = NewObject<UPCGPointData>();
	UPCGPointData* CitadelPointData = NewObject<UPCGPointData>();
	UPCGPointData* StamensPointData = NewObject<UPCGPointData>();
	UPCGPointData* SubmergedPointData = NewObject<UPCGPointData>();

	TArray<FPCGPoint>& MasterPoints = MasterPointData->GetMutablePoints();
	TArray<FPCGPoint>& PetalPoints = PetalsPointData->GetMutablePoints();
	TArray<FPCGPoint>& CitadelPoints = CitadelPointData->GetMutablePoints();
	TArray<FPCGPoint>& StamenPoints = StamensPointData->GetMutablePoints();
	TArray<FPCGPoint>& SubmergedPoints = SubmergedPointData->GetMutablePoints();

	// Initialize Metadata Attributes on Petals Point Data
	UPCGMetadata* PetalMeta = PetalsPointData->Metadata;
	FPCGMetadataAttribute<int32>* AttrPetalIndex = PetalMeta->CreateAttribute<int32>(FName(TEXT("PetalIndex")), 0, true, true);
	FPCGMetadataAttribute<float>* AttrPetalU = PetalMeta->CreateAttribute<float>(FName(TEXT("PetalU")), 0.0f, true, true);
	FPCGMetadataAttribute<float>* AttrPetalV = PetalMeta->CreateAttribute<float>(FName(TEXT("PetalV")), 0.0f, true, true);
	FPCGMetadataAttribute<FString>* AttrZoneTag = PetalMeta->CreateAttribute<FString>(FName(TEXT("ZoneTag")), TEXT("Petal_MidLiving"), true, true);
	FPCGMetadataAttribute<float>* AttrClearanceGap = PetalMeta->CreateAttribute<float>(FName(TEXT("ClearanceGap_cm")), 4500.0f, true, true);
	FPCGMetadataAttribute<int32>* AttrSubCouncil = PetalMeta->CreateAttribute<int32>(FName(TEXT("SubCouncilIndex")), 1, true, true);

	// Initialize Metadata Attributes on Submerged Rings Point Data
	UPCGMetadata* SubmergedMeta = SubmergedPointData->Metadata;
	FPCGMetadataAttribute<int32>* AttrRingTier = SubmergedMeta->CreateAttribute<int32>(FName(TEXT("RingTier")), 0, true, true);
	FPCGMetadataAttribute<float>* AttrRingRadius = SubmergedMeta->CreateAttribute<float>(FName(TEXT("RingRadius_cm")), 30000.0f, true, true);
	FPCGMetadataAttribute<float>* AttrPressureBar = SubmergedMeta->CreateAttribute<float>(FName(TEXT("HydrostaticPressure_Bar")), 1.0f, true, true);

#pragma region 1. Generate 8 Discrete Non-Overlapping Petals

	const int32 NumPetals = FMath::Max(Settings->PetalSettings.PetalCount, 1);
	const int32 USteps = FMath::Max(Settings->PetalUSteps, 2);
	const int32 VSteps = FMath::Max(Settings->PetalVSteps, 2);

	for (int32 PetalIdx = 0; PetalIdx < NumPetals; ++PetalIdx)
	{
		for (int32 uIdx = 0; uIdx <= USteps; ++uIdx)
		{
			const float NormalizedU = (float)uIdx / (float)USteps;
			
			float ClearanceDistance = 0.0f;
			UFC_PCGMathLibrary::VerifyWaterwayClearance(PetalIdx, NormalizedU, Settings->PetalSettings, ClearanceDistance);

			for (int32 vIdx = 0; vIdx <= VSteps; ++vIdx)
			{
				// Map v from [-1.0 (Left edge) to +1.0 (Right edge)]
				const float NormalizedV = -1.0f + (2.0f * ((float)vIdx / (float)VSteps));

				FVector WorldPos, WorldNormal, WorldTangent;
				UFC_PCGMathLibrary::ComputePetalSurfaceTransform(
					PetalIdx,
					NormalizedU,
					NormalizedV,
					Settings->PetalSettings,
					Settings->RuntimePitchAngle_Deg,
					WorldPos,
					WorldNormal,
					WorldTangent
				);

				FPCGPoint Point;
				Point.Transform = FTransform(WorldTangent.Rotation(), WorldPos, FVector(1.0f));
				Point.Density = 1.0f;
				Point.BoundsMin = FVector(-600.f, -600.f, -300.f);
				Point.BoundsMax = FVector(600.f, 600.f, 300.f);
				Point.Seed = Context->GetSeed() + (PetalIdx * 10000) + (uIdx * 100) + vIdx;

				// Map to exact DT_District_Zoning row names
				static const FString FacultyRowNames[8] = {
					TEXT("ZONE_FACULTY_OCEANIC"),
					TEXT("ZONE_FACULTY_BIOSPHERE"),
					TEXT("ZONE_FACULTY_CLIMATE"),
					TEXT("ZONE_FACULTY_MEGASTRUCT"),
					TEXT("ZONE_FACULTY_ARCHIVES"),
					TEXT("ZONE_FACULTY_ABYSSAL"),
					TEXT("ZONE_FACULTY_DIPLOMACY"),
					TEXT("ZONE_FACULTY_MEDICINE")
				};

				FString ZoneName = FacultyRowNames[FMath::Clamp(PetalIdx, 0, 7)];
				if (FMath::Abs(NormalizedV) > 0.92f)
				{
					ZoneName = TEXT("ZONE_CLEARANCE_WATERWAY");
				}
				else if (NormalizedU > 0.85f)
				{
					ZoneName = TEXT("ZONE_HARBOR_BERTH");
				}

				const int64 EntryKey = PetalPoints.Num();
				PetalPoints.Add(Point);
				MasterPoints.Add(Point);

				// Write Metadata
				AttrPetalIndex->SetValue(EntryKey, PetalIdx);
				AttrPetalU->SetValue(EntryKey, NormalizedU);
				AttrPetalV->SetValue(EntryKey, NormalizedV);
				AttrZoneTag->SetValue(EntryKey, ZoneName);
				AttrClearanceGap->SetValue(EntryKey, ClearanceDistance);
				AttrSubCouncil->SetValue(EntryKey, PetalIdx + 1);
			}
		}
	}

#pragma endregion 1. Generate 8 Discrete Non-Overlapping Petals

#pragma region 2. Generate 70 Golden Stamen Forcefield Pylons

	const int32 TotalStamens = FMath::Max(Settings->StamenCount, 1);
	for (int32 StamenIdx = 0; StamenIdx < TotalStamens; ++StamenIdx)
	{
		FVector BasePos;
		FRotator PylonRot;
		UFC_PCGMathLibrary::ComputeStamenPylonTransform(
			StamenIdx,
			TotalStamens,
			Settings->ReceptacleRadius,
			Settings->StamenHeight,
			Settings->StamenInwardLean_Deg,
			BasePos,
			PylonRot
		);

		FPCGPoint Point;
		Point.Transform = FTransform(PylonRot, BasePos, FVector(1.0f));
		Point.Density = 1.0f;
		Point.BoundsMin = FVector(-300.f, -300.f, 0.f);
		Point.BoundsMax = FVector(300.f, 300.f, Settings->StamenHeight);
		Point.Seed = Context->GetSeed() + 500000 + StamenIdx;

		StamenPoints.Add(Point);
		MasterPoints.Add(Point);
	}

#pragma endregion 2. Generate 70 Golden Stamen Forcefield Pylons

#pragma region 3. Generate Central Citadel & Council of Ten Apex Spire

	// Base Receptacle Deck Hubs (Concentric radial rings)
	const int32 CitadelRings = 5;
	for (int32 RingIdx = 0; RingIdx < CitadelRings; ++RingIdx)
	{
		const float RingFraction = (float)(RingIdx + 1) / (float)CitadelRings;
		const float RingRadius = RingFraction * (Settings->ReceptacleRadius * 0.75f);
		const int32 PointsInRing = 8 * (RingIdx + 1);

		for (int32 PtIdx = 0; PtIdx < PointsInRing; ++PtIdx)
		{
			const float AngleDeg = (360.0f / (float)PointsInRing) * PtIdx;
			const float AngleRad = FMath::DegreesToRadians(AngleDeg);

			FVector Pos(RingRadius * FMath::Cos(AngleRad), RingRadius * FMath::Sin(AngleRad), 1500.0f);
			FRotator Rot(0.0f, AngleDeg, 0.0f);

			FPCGPoint Point;
			Point.Transform = FTransform(Rot, Pos, FVector(1.0f));
			Point.Density = 1.0f;
			Point.BoundsMin = FVector(-800.f, -800.f, 0.f);
			Point.BoundsMax = FVector(800.f, 800.f, 1500.f);
			Point.Seed = Context->GetSeed() + 600000 + (RingIdx * 100) + PtIdx;

			CitadelPoints.Add(Point);
			MasterPoints.Add(Point);
		}
	}

	// Council of Ten Chamber Point at Apex
	{
		FPCGPoint ApexPoint;
		ApexPoint.Transform = FTransform(FRotator::ZeroRotator, FVector(0.f, 0.f, Settings->ApexSpireHeight), FVector(1.0f));
		ApexPoint.Density = 1.0f;
		ApexPoint.BoundsMin = FVector(-2500.f, -2500.f, -2000.f);
		ApexPoint.BoundsMax = FVector(2500.f, 2500.f, 2000.f);
		ApexPoint.Seed = Context->GetSeed() + 777777;

		CitadelPoints.Add(ApexPoint);
		MasterPoints.Add(ApexPoint);
	}

#pragma endregion 3. Generate Central Citadel & Council of Ten Apex Spire

#pragma region 4. Generate 12 Telescopic Expanding Underwater Ballast Rings

	const int32 TierCount = FMath::Max(Settings->SubmergedSettings.RingTierCount, 1);
	const int32 RingResolution = FMath::Max(Settings->RingAngularResolution, 8);

	for (int32 TierIdx = 0; TierIdx < TierCount; ++TierIdx)
	{
		for (int32 AngleIdx = 0; AngleIdx < RingResolution; ++AngleIdx)
		{
			const float AngleDeg = (360.0f / (float)RingResolution) * AngleIdx;
			
			FVector RingLocation;
			FRotator RingOrientation;
			float CalculatedRadius = 0.0f;

			UFC_PCGMathLibrary::ComputeSubmergedRingPoint(
				TierIdx,
				AngleDeg,
				Settings->SubmergedSettings,
				RingLocation,
				RingOrientation,
				CalculatedRadius
			);

			const float HydrostaticPressure = UFC_PCGMathLibrary::CalculateHydrostaticPressure_Bar(RingLocation.Z);

			FPCGPoint Point;
			Point.Transform = FTransform(RingOrientation, RingLocation, FVector(1.0f));
			Point.Density = 1.0f;
			Point.BoundsMin = FVector(-1000.f, -1000.f, -500.f);
			Point.BoundsMax = FVector(1000.f, 1000.f, 500.f);
			Point.Seed = Context->GetSeed() + 800000 + (TierIdx * 1000) + AngleIdx;

			const int64 EntryKey = SubmergedPoints.Num();
			SubmergedPoints.Add(Point);
			MasterPoints.Add(Point);

			AttrRingTier->SetValue(EntryKey, TierIdx);
			AttrRingRadius->SetValue(EntryKey, CalculatedRadius);
			AttrPressureBar->SetValue(EntryKey, HydrostaticPressure);
		}
	}

#pragma endregion 4. Generate 12 Telescopic Expanding Underwater Ballast Rings

	// Route outputs to PCG Output Pins
	FPCGTaggedData& MasterOut = Context->OutputData.TaggedData.Emplace_GetRef();
	MasterOut.Pin = PCGPinConstants::DefaultOutputLabel;
	MasterOut.Data = MasterPointData;

	FPCGTaggedData& PetalsOut = Context->OutputData.TaggedData.Emplace_GetRef();
	PetalsOut.Pin = FName(TEXT("Petals"));
	PetalsOut.Data = PetalsPointData;

	FPCGTaggedData& CitadelOut = Context->OutputData.TaggedData.Emplace_GetRef();
	CitadelOut.Pin = FName(TEXT("Citadel"));
	CitadelOut.Data = CitadelPointData;

	FPCGTaggedData& StamensOut = Context->OutputData.TaggedData.Emplace_GetRef();
	StamensOut.Pin = FName(TEXT("Stamens"));
	StamensOut.Data = StamensPointData;

	FPCGTaggedData& SubmergedOut = Context->OutputData.TaggedData.Emplace_GetRef();
	SubmergedOut.Pin = FName(TEXT("SubmergedRings"));
	SubmergedOut.Data = SubmergedPointData;

	return true;
}
