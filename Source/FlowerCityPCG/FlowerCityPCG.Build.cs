// Copyright (c) 2026 HopeLess / Istrorigan Sanctuary. All Rights Reserved.

using UnrealBuildTool;

public class FlowerCityPCG : ModuleRules
{
	public FlowerCityPCG(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = ModuleRules.PCHUsageMode.UseExplicitOrSharedPCHs;
		
		PublicIncludePaths.AddRange(
			new string[] {
				// Module public headers
			}
		);
				
		PrivateIncludePaths.AddRange(
			new string[] {
				// Module private headers
			}
		);
			
		PublicDependencyModuleNames.AddRange(
			new string[]
			{
				"Core",
				"CoreUObject",
				"Engine",
				"PCG",
				"GameplayTags",
				"StructUtils"
			}
		);
			
		PrivateDependencyModuleNames.AddRange(
			new string[]
			{
				"RenderCore",
				"RHI"
			}
		);
	}
}
