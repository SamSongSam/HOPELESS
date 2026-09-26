# 00_PCG_DATA_CONTRACTS - Spatial, Sockets & Rule Schemas

## Purpose
ไฟล์นี้เป็น **Data Layer / Data Contracts** ที่จำเป็นสำหรับการนำไปเขียน C++, Unreal Engine 5 PCG Graph, หรือ Houdini VEX โดยรวบรวม Structs, Enums, และตารางข้อมูลที่โครงสร้างเดิมขาดไป

---

## 1. Radial & Polar Coordinate Math (`FFC_RadialCoordinates`)

พิกัดเฉพาะสำหรับเมืองทรงดอกไม้ (Megastructure) ใช้แทน Cartesian Grid ทั่วไป:

```cpp
USTRUCT(BlueprintType)
struct FFC_RadialCoordinates
{
    GENERATED_BODY()

    // ลำดับกลีบ (0 ถึง N-1 ตามเข็มนาฬิกา)
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|PCG")
    int32 PetalIndex = 0;

    // ลำดับวงแหวนจากแกนกลาง (0 = Core, 1 = Inner Petal, 2 = Mid Blade, 3 = Tip, 4 = Outer Rim)
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|PCG")
    int32 RingTier = 0;

    // ระยะห่างจากจุดศูนย์กลางเมือง (cm หรือ meters)
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|PCG")
    float RadialDistance = 0.0f;

    // มุมระนาบเชิงขั้ว (0.0 - 360.0 องศา)
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|PCG")
    float Angle_Degrees = 0.0f;

    // Normalised Petal UV: U = 0.0 (โคนกลีบติด Center) ถึง 1.0 (ปลายกลีบ Tip)
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|PCG")
    float PetalU_Normalized = 0.0f;

    // Normalised Petal UV: V = -1.0 (ขอบกลีบซ้าย), 0.0 (สันแกนกลาง Spine), +1.0 (ขอบกลีบขวา)
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|PCG")
    float PetalV_Normalized = 0.0f;

    // ระดับความสูงเทียบกับระดับน้ำทะเล (Sea Level Z = 0)
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|PCG")
    float Elevation_Z = 0.0f;

    // Tier ความลึกแนวดิ่ง (-2: Abyssal Trench, -1: Submerged Stem, 0: Sea Level, 1: Surface, 2: Spire)
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|PCG")
    int32 VerticalTier = 0;
};
```

---

## 2. Slot & Socket Snapping System (`FFC_PCG_Socket`)

```cpp
UENUM(BlueprintType)
enum class EFC_SocketType : uint8
{
    Structural_Hinge      UMETA(DisplayName = "Structural Hinge (Center to Petal)"),
    Structural_Girder     UMETA(DisplayName = "Rigid Structural Girder"),
    Transit_Pedestrian    UMETA(DisplayName = "Pedestrian Corridor/Walkway"),
    Transit_Maglev        UMETA(DisplayName = "High-speed Maglev Rail"),
    Transit_Submersible   UMETA(DisplayName = "Submersible Dock/Tunnel"),
    Utility_PowerGrid     UMETA(DisplayName = "High-Voltage Power Trunk"),
    Utility_LifeSupport   UMETA(DisplayName = "Oxygen / Fluid Pipeline"),
    Facade_Mount          UMETA(DisplayName = "Surface Panel / Defense Mount")
};

UENUM(BlueprintType)
enum class EFC_SocketGender : uint8
{
    Male,
    Female,
    Bilateral
};

USTRUCT(BlueprintType)
struct FFC_PCG_Socket
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Socket")
    FName SocketName;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Socket")
    EFC_SocketType SocketType = EFC_SocketType::Structural_Girder;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Socket")
    EFC_SocketGender Gender = EFC_SocketGender::Bilateral;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Socket")
    FTransform LocalTransform = FTransform::Identity;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Socket")
    FVector ClearanceExtent = FVector(200.f, 200.f, 300.f);

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Socket")
    FGameplayTagContainer CompatibilityTags;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "FlowerCity|Socket")
    bool bIsOccupied = false;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "FlowerCity|Socket")
    int32 ConnectedModuleUID = -1;
};
```

---

## 3. Module Weight & Probability Table (`FFC_ModuleSpawnRule`)

```cpp
USTRUCT(BlueprintType)
struct FFC_ModuleSpawnRule
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Spawn")
    FName ArchetypeID;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Spawn")
    TSoftObjectPtr<UStaticMesh> MeshAsset;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Spawn")
    float BaseWeight = 100.0f;

    // Weight Multiplier เทียบกับระดับความลึก (Depth 0m ถึง -500m)
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Spawn")
    FRuntimeFloatCurve DepthWeightCurve;

    // Weight Multiplier เทียบกับระยะห่างจาก Center
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Spawn")
    FRuntimeFloatCurve RadialWeightCurve;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Spawn")
    int32 MinCountPerPetal = 1;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Spawn")
    int32 MaxCountPerPetal = 8;

    // แรงดันน้ำสูงสุดที่รับได้ (Bar)
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Spawn")
    float PressureRating_Bar = 50.0f;

    // แรงลอยตัวสุทธิ (kN)
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Spawn")
    float BuoyancyForce_kN = 100.0f;
};
```

---

## 4. Gameplay Transit & Flow Graph (`FFC_CityGraphNode`, `FFC_CityGraphEdge`)

```cpp
USTRUCT(BlueprintType)
struct FFC_CityGraphNode
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Graph")
    int32 NodeID = 0;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Graph")
    FVector WorldLocation = FVector::ZeroVector;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Graph")
    FGameplayTag NodeTypeTag; // เช่น "Graph.Node.TransitHub", "Graph.Node.O2Substation"

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Graph")
    int32 PetalIndex = -1; // -1 = Core

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Graph")
    TArray<int32> ConnectedEdgeIDs;
};

USTRUCT(BlueprintType)
struct FFC_CityGraphEdge
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Graph")
    int32 EdgeID = 0;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Graph")
    int32 StartNodeID = 0;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Graph")
    int32 EndNodeID = 0;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Graph")
    FGameplayTag EdgeTypeTag; // เช่น "Graph.Edge.MaglevTrack", "Graph.Edge.OxygenPipe"

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "FlowerCity|Graph")
    float Capacity = 1000.0f;
};
```
