// Copyright (c) 2026 HopeLess / Istrorigan Sanctuary. All Rights Reserved.

#include "FlowerCityPCGModule.h"

DEFINE_LOG_CATEGORY(LogFlowerCityPCG);

#define LOCTEXT_NAMESPACE "FFlowerCityPCGModule"

void FFlowerCityPCGModule::StartupModule()
{
	UE_LOG(LogFlowerCityPCG, Log, TEXT("FlowerCityPCG Module (Istrorigan 4205) Initialized successfully."));
}

void FFlowerCityPCGModule::ShutdownModule()
{
	UE_LOG(LogFlowerCityPCG, Log, TEXT("FlowerCityPCG Module Shutdown."));
}

#undef LOCTEXT_NAMESPACE
	
IMPLEMENT_MODULE(FFlowerCityPCGModule, FlowerCityPCG)
