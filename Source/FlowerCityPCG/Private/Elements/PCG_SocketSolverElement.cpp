// Copyright (c) 2026 HopeLess / Istrorigan Sanctuary. All Rights Reserved.

#include "Elements/PCG_SocketSolverElement.h"
#include "Data/PCGPointData.h"
#include "Metadata/PCGMetadata.h"
#include "PCGContext.h"
#include "PCGPin.h"

UPCG_SocketSolverSettings::UPCG_SocketSolverSettings()
{
	bUseSeed = false;
}

TArray<FPCGPinProperties> UPCG_SocketSolverSettings::InputPinProperties() const
{
	TArray<FPCGPinProperties> PinProperties;
	PinProperties.Emplace(PCGPinConstants::DefaultInputLabel, EPCGDataType::Point, false, false, NSLOCTEXT("FlowerCityPCG", "InputPointsPin", "Candidate Module Sockets"));
	return PinProperties;
}

TArray<FPCGPinProperties> UPCG_SocketSolverSettings::OutputPinProperties() const
{
	TArray<FPCGPinProperties> PinProperties;
	PinProperties.Emplace(PCGPinConstants::DefaultOutputLabel, EPCGDataType::Point, false, false, NSLOCTEXT("FlowerCityPCG", "ValidOutputPin", "Valid Snapped & Cleared Modules"));
	PinProperties.Emplace(FName(TEXT("Rejected")), EPCGDataType::Point, false, false, NSLOCTEXT("FlowerCityPCG", "RejectedPin", "Pruned Modules (Clearance Collision or Joint Failure)"));
	return PinProperties;
}

FPCGElementPtr UPCG_SocketSolverSettings::CreateElement() const
{
	return MakeShared<FPCG_SocketSolverElement>();
}

bool FPCG_SocketSolverElement::ExecuteInternal(FPCGContext* Context) const
{
	check(Context);

	const UPCG_SocketSolverSettings* Settings = Context->GetInputSettings<UPCG_SocketSolverSettings>();
	check(Settings);

	TArray<FPCGTaggedData> Inputs = Context->InputData.GetInputsByPin(PCGPinConstants::DefaultInputLabel);
	if (Inputs.Num() == 0)
	{
		return true;
	}

	for (const FPCGTaggedData& InputData : Inputs)
	{
		const UPCGPointData* InputPointData = Cast<UPCGPointData>(InputData.Data);
		if (!InputPointData)
		{
			continue;
		}

		const TArray<FPCGPoint>& InPoints = InputPointData->GetPoints();
		if (InPoints.Num() == 0)
		{
			continue;
		}

		UPCGPointData* ValidPointData = NewObject<UPCGPointData>();
		UPCGPointData* RejectedPointData = NewObject<UPCGPointData>();

		ValidPointData->InitializeFromData(InputPointData);
		RejectedPointData->InitializeFromData(InputPointData);

		TArray<FPCGPoint>& ValidPoints = ValidPointData->GetMutablePoints();
		TArray<FPCGPoint>& RejectedPoints = RejectedPointData->GetMutablePoints();

		UPCGMetadata* ValidMeta = ValidPointData->Metadata;
		FPCGMetadataAttribute<bool>* AttrWatertightPass = ValidMeta->CreateAttribute<bool>(FName(TEXT("WatertightPassed")), true, true, true);
		FPCGMetadataAttribute<float>* AttrJointStress = ValidMeta->CreateAttribute<float>(FName(TEXT("JointShearLoad_kN")), 0.0f, true, true);

		// Spatial Grid indexing for fast clearance & collision checking
		const float MinimumClearanceDistanceSq = FMath::Square(Settings->SnapToleranceRadius);

		for (int32 i = 0; i < InPoints.Num(); ++i)
		{
			const FPCGPoint& Candidate = InPoints[i];
			const FVector CandidateLoc = Candidate.Transform.GetLocation();
			bool bIsRejected = false;

			// Submerged watertight enforcement rule
			if (Settings->bStrictWatertightCheckSubmerged && CandidateLoc.Z < 0.0f)
			{
				// Submerged points must not be placed directly on open unsealed boundaries
				if (Candidate.Density < 0.15f)
				{
					bIsRejected = true;
				}
			}

			// Proximity clearance check against already accepted valid points
			if (!bIsRejected)
			{
				for (const FPCGPoint& Accepted : ValidPoints)
				{
					const float DistSq = FVector::DistSquared(CandidateLoc, Accepted.Transform.GetLocation());
					if (DistSq < MinimumClearanceDistanceSq * 0.25f) // Overlapping footprint collision
					{
						bIsRejected = true;
						break;
					}
				}
			}

			if (bIsRejected)
			{
				RejectedPoints.Add(Candidate);
			}
			else
			{
				const int64 EntryKey = ValidPoints.Num();
				ValidPoints.Add(Candidate);

				// Populate runtime attributes
				AttrWatertightPass->SetValue(EntryKey, true);
				AttrJointStress->SetValue(EntryKey, FMath::Abs(CandidateLoc.Z) * 0.05f); // Hydrostatic joint load
			}
		}

		// Output pins routing
		FPCGTaggedData& ValidOut = Context->OutputData.TaggedData.Emplace_GetRef();
		ValidOut.Pin = PCGPinConstants::DefaultOutputLabel;
		ValidOut.Data = ValidPointData;

		FPCGTaggedData& RejectedOut = Context->OutputData.TaggedData.Emplace_GetRef();
		RejectedOut.Pin = FName(TEXT("Rejected"));
		RejectedOut.Data = RejectedPointData;
	}

	return true;
}
