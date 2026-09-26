FLOWER\_CITY\_MASTER

&nbsp;

00\_CORE

├─ FC\_Global\_Settings

├─ FC\_Seed\_Control

├─ FC\_Scale\_Units

├─ FC\_Debug\_View

└─ FC\_Attribute\_Registry

&nbsp;

01\_WORLD

├─ FC\_Terrain

├─ FC\_Road

├─ FC\_Path

├─ FC\_District

└─ FC\_Plot

&nbsp;

02\_ARCHITECTURE

├─ FC\_Building\_Base

├─ FC\_Facade

├─ FC\_Roof

├─ FC\_Window

├─ FC\_Door

└─ FC\_Modular\_Assembly

&nbsp;

03\_FLOWER\_MEGASTRUCTURE  
│

├─ 03.01\_FLOWER\_GLOBAL\_STATE

│  │

│  ├─ FC\_Flower\_State

│  │  ├─ Open\_State \[bool\]

│  │  ├─ Open\_Amount \[float 0–1\]

│  │  ├─ Trade\_State \[bool\]

│  │  ├─ Protection\_State \[bool\]

│  │  ├─ Submerge\_State \[bool\]

│  │  ├─ Submerge\_Amount \[float 0–1\]

│  │  ├─ Deep\_Sea\_Mode \[bool\]

│  │  ├─ Emergency\_State \[bool\]

│  │  ├─ Annual\_Cycle\_State \[int / enum\]

│  │  ├─ Previous\_Global\_State

│  │  ├─ Current\_Global\_State

│  │  └─ Target\_Global\_State

│  │

│  └─ FC\_Flower\_State\_Distributor

│     │

│     ├─ Structure\_State

│     │  └─ Petal / Zone / Shore / Stem / Root / Center

│     │

│     ├─ Protection\_State

│     │  └─ Protection Network / Protection Pylon / Protection Control Center

│     │

│     ├─ Operation\_State

│     │  └─ Transport / Occupancy / Public Access / Service Access

│     │

│     ├─ Trade\_State

│     │  └─ Public Access / Shore Docking / Transport / Protection

│     │

│     ├─ Submerge\_State

│     │  └─ Pressure / Descent / Stem / Root / Shore / Transport

│     │

│     ├─ Deep\_Sea\_State

│     │  └─ Pressure / Hazard / Occupancy / Ring Access / Root Operation

│     │

│     └─ Emergency\_State

│        └─ Protection / Transport / Petal / Stem / Root / Shore / Evacuation

│

│

├─ 03.02\_FLOWER\_CENTER

│  │

│  ├─ FC\_Flower\_Center

│  │  ├─ Center\_ID

│  │  ├─ Center\_Radius

│  │  ├─ Center\_Height

│  │  ├─ Center\_Transform

│  │  ├─ Center\_Top\_Height

│  │  ├─ Center\_Base\_Height

│  │  ├─ Center\_Clearance

│  │  ├─ Center\_Profile

│  │  ├─ Center\_Thickness

│  │  ├─ Center\_Floor\_Count \[int\]

│  │  ├─ Center\_Floor\_Height

│  │  ├─ Center\_Core\_Radius

│  │  ├─ Center\_Inner\_Radius

│  │  ├─ Center\_Outer\_Radius

│  │  ├─ Center\_Orientation

│  │  ├─ Center\_Surface\_Normal

│  │  ├─ Center\_Load\_Class

│  │  ├─ Center\_State

│  │  └─ Center\_Enabled \[bool\]

│  │

│  ├─ FC\_Flower\_Cone

│  │  ├─ Cone\_ID

│  │  ├─ Cone\_Radius

│  │  ├─ Cone\_Base\_Radius

│  │  ├─ Cone\_Top\_Radius

│  │  ├─ Cone\_Height

│  │  ├─ Cone\_Profile

│  │  ├─ Cone\_Taper

│  │  ├─ Cone\_Thickness

│  │  ├─ Cone\_Base\_Height

│  │  ├─ Cone\_Top\_Height

│  │  ├─ Cone\_Transform

│  │  ├─ Cone\_Orientation

│  │  ├─ Cone\_Surface\_Normal

│  │  ├─ Cone\_Inner\_Clearance

│  │  ├─ Cone\_Outer\_Clearance

│  │  ├─ Cone\_Top\_Clearance

│  │  ├─ Cone\_Petal\_Clearance

│  │  ├─ Cone\_Building\_Clearance

│  │  ├─ Cone\_Load\_Class

│  │  ├─ Cone\_State

│  │  └─ Cone\_Enabled \[bool\]

│  │

│  ├─ FC\_Center\_Structure

│  │  ├─ Structural\_Core

│  │  ├─ Structural\_Ring

│  │  ├─ Upper\_Support

│  │  ├─ Lower\_Support

│  │  ├─ Load\_Transfer\_Point

│  │  ├─ Core\_Radius

│  │  ├─ Core\_Thickness

│  │  ├─ Ring\_Count \[int\]

│  │  ├─ Ring\_Radius

│  │  ├─ Ring\_Thickness

│  │  ├─ Support\_Count \[int\]

│  │  ├─ Support\_Spacing

│  │  ├─ Support\_Angle

│  │  ├─ Radial\_Support

│  │  ├─ Vertical\_Support

│  │  ├─ Petal\_Load\_Input

│  │  ├─ Center\_Load\_Input

│  │  ├─ Stem\_Load\_Output

│  │  ├─ Load\_Distribution

│  │  ├─ Load\_Balance

│  │  ├─ Structural\_Clearance

│  │  ├─ Structural\_State

│  │  └─ Structural\_Enabled \[bool\]

│  │

│  ├─ FC\_Center\_Petal\_Interface

│  │  ├─ Petal\_ID

│  │  ├─ Petal\_Attach\_Point

│  │  ├─ Petal\_Attach\_Transform

│  │  ├─ Petal\_Inner\_Pivot

│  │  ├─ Petal\_Left\_Rig\_Attach

│  │  ├─ Petal\_Right\_Rig\_Attach

│  │  ├─ Petal\_Rest\_Transform

│  │  ├─ Petal\_Open\_Transform

│  │  ├─ Petal\_Closed\_Transform

│  │  ├─ Petal\_Current\_Transform

│  │  ├─ Petal\_Local\_Space

│  │  ├─ Petal\_Rotation\_Axis

│  │  ├─ Petal\_Rotation\_Limit

│  │  ├─ Petal\_Raise\_Limit

│  │  ├─ Petal\_Lower\_Limit

│  │  ├─ Petal\_Twist\_Limit

│  │  ├─ Petal\_Clearance

│  │  ├─ Petal\_Center\_Clearance

│  │  ├─ Petal\_Neighbor\_Clearance

│  │  ├─ Petal\_Rig\_Clearance

│  │  ├─ Petal\_Load\_Interface

│  │  ├─ Petal\_Utility\_Interface

│  │  ├─ Petal\_Transport\_Interface

│  │  ├─ Petal\_State

│  │  ├─ Petal\_Connection\_State

│  │  └─ Petal\_Interface\_Enabled \[bool\]

│  │

│  ├─ FC\_Center\_Petal\_Distribution

│  │  ├─ Petal\_Count \[int\]

│  │  ├─ Petal\_Index \[int\]

│  │  ├─ Petal\_ID

│  │  ├─ Radial\_Angle

│  │  ├─ Angular\_Spacing

│  │  ├─ Rotation\_Offset

│  │  ├─ Distribution\_Radius

│  │  ├─ Distribution\_Center

│  │  ├─ Distribution\_Axis

│  │  ├─ Start\_Angle

│  │  ├─ End\_Angle

│  │  ├─ Closed\_Loop \[bool\]

│  │  ├─ Petal\_Radial\_Position

│  │  ├─ Petal\_Radial\_Direction

│  │  ├─ Petal\_Tangent\_Direction

│  │  ├─ Petal\_Local\_Transform

│  │  ├─ Petal\_World\_Transform

│  │  ├─ Petal\_Rotation

│  │  ├─ Petal\_Scale

│  │  ├─ Petal\_Spacing\_Override

│  │  ├─ Petal\_Rotation\_Override

│  │  ├─ Petal\_Radius\_Override

│  │  ├─ Neighbor\_Left\_ID

│  │  ├─ Neighbor\_Right\_ID

│  │  ├─ Neighbor\_Angle

│  │  ├─ Neighbor\_Clearance

│  │  ├─ Distribution\_Clearance

│  │  ├─ Distribution\_State

│  │  └─ Distribution\_Enabled \[bool\]

│  │

│  ├─ FC\_Center\_Petal\_Clearance

│  │  ├─ Inner\_Clearance

│  │  ├─ Closed\_State\_Clearance

│  │  ├─ Rig\_Clearance

│  │  ├─ Building\_Clearance

│  │  ├─ Center\_Collision\_Limit

│  │  ├─ Petal\_Inner\_Clearance

│  │  ├─ Petal\_Left\_Clearance

│  │  ├─ Petal\_Right\_Clearance

│  │  ├─ Petal\_Top\_Clearance

│  │  ├─ Petal\_Bottom\_Clearance

│  │  ├─ Neighbor\_Petal\_Clearance

│  │  ├─ Petal\_Rotation\_Clearance

│  │  ├─ Petal\_Raise\_Clearance

│  │  ├─ Petal\_Lower\_Clearance

│  │  ├─ Petal\_Twist\_Clearance

│  │  ├─ Rig\_Left\_Clearance

│  │  ├─ Rig\_Right\_Clearance

│  │  ├─ Rig\_Motion\_Clearance

│  │  ├─ Building\_Open\_State\_Clearance

│  │  ├─ Building\_Closed\_State\_Clearance

│  │  ├─ Building\_Roof\_Clearance

│  │  ├─ Center\_Cone\_Clearance

│  │  ├─ Center\_Structure\_Clearance

│  │  ├─ Transport\_Interface\_Clearance

│  │  ├─ Utility\_Interface\_Clearance

│  │  ├─ Open\_State\_Envelope

│  │  ├─ Closed\_State\_Envelope

│  │  ├─ Transition\_Envelope

│  │  ├─ Collision\_Margin

│  │  ├─ Safety\_Margin

│  │  ├─ Clearance\_Valid \[bool\]

│  │  └─ Clearance\_Debug

│  │

│  ├─ FC\_Center\_Building\_Restriction

│  │  ├─ Restricted\_Radius

│  │  ├─ Restriction\_Zone\_ID

│  │  ├─ Distance\_From\_Center

│  │  ├─ Distance\_From\_Cone

│  │  ├─ Max\_Building\_Height

│  │  ├─ Min\_Building\_Height

│  │  ├─ Max\_Building\_Floors \[int\]

│  │  ├─ Min\_Building\_Floors \[int\]

│  │  ├─ Max\_Roof\_Height

│  │  ├─ Flat\_Roof\_Required \[bool\]

│  │  ├─ Roof\_Profile\_Restriction

│  │  ├─ Building\_Orientation\_Mode

│  │  ├─ Follow\_Petal\_Surface \[bool\]

│  │  ├─ Upside\_Down\_Allowed \[bool\]

│  │  ├─ Petal\_Close\_Clearance

│  │  ├─ Petal\_Transition\_Clearance

│  │  ├─ Center\_Cone\_Clearance

│  │  ├─ Center\_Structure\_Clearance

│  │  ├─ Neighbor\_Building\_Clearance

│  │  ├─ Rig\_Motion\_Clearance

│  │  ├─ Protection\_Pylon\_Clearance

│  │  ├─ Transport\_Clearance

│  │  ├─ Emergency\_Access\_Clearance

│  │  ├─ Mass\_Class\_Limit

│  │  ├─ Load\_Budget

│  │  ├─ Public\_Space\_Required \[bool\]

│  │  ├─ Build\_Density\_Limit

│  │  ├─ Buildable\_Open\_State \[bool\]

│  │  ├─ Buildable\_Closed\_State \[bool\]

│  │  ├─ Buildable\_Transition\_State \[bool\]

│  │  ├─ Buildable \[bool\]

│  │  └─ Restriction\_Debug

│  │

│  ├─ FC\_Center\_Transport\_Hub

│  │  ├─ Center\_Transport\_Root

│  │  ├─ Transport\_State

│  │  ├─ Transport\_Mode

│  │  ├─ Active\_Route\_ID

│  │  ├─ Route\_Priority

│  │  ├─ Route\_Time\_Window

│  │  ├─ Current\_Petal\_State

│  │  ├─ Current\_Stem\_State

│  │  └─ Transport\_Enabled \[bool\]

│  │

│  ├─ FC\_Center\_Petal\_Transit

│  │  ├─ Petal\_ID

│  │  ├─ Petal\_Station\_ID

│  │  ├─ Petal\_Entry

│  │  ├─ Petal\_Exit

│  │  ├─ Center\_Connection

│  │  ├─ Route\_Transform

│  │  ├─ Route\_Orientation

│  │  ├─ Route\_Continuity

│  │  └─ Petal\_Transit\_State

│  │

│  ├─ FC\_Center\_Stem\_Transit

│  │  ├─ Stem\_Access

│  │  ├─ Stem\_Entry

│  │  ├─ Stem\_Exit

│  │  ├─ Stem\_Transfer\_Point

│  │  ├─ Vertical\_Transfer

│  │  ├─ Hyperlink\_Transfer

│  │  ├─ Lift\_Transfer

│  │  └─ Stem\_Transit\_State

│  │

│  ├─ FC\_Center\_Transfer\_Plaza

│  │  ├─ Civic\_Plaza

│  │  ├─ Education\_Access

│  │  ├─ Council\_Access

│  │  ├─ Public\_Transfer

│  │  ├─ Service\_Transfer

│  │  └─ Emergency\_Transfer

│  │

│  ├─ FC\_Center\_Transport\_Mode

│  │  ├─ Walk

│  │  ├─ Wheeled

│  │  ├─ Rail

│  │  ├─ Magnetic

│  │  ├─ Pod

│  │  ├─ Hyperlink

│  │  └─ Lift

│  │

│  ├─ FC\_Center\_Transport\_Adapter

│  │  ├─ Adapter\_ID

│  │  ├─ Source\_Mode

│  │  ├─ Target\_Mode

│  │  ├─ Wheel\_Mode

│  │  ├─ Rail\_Mode

│  │  ├─ Magnetic\_Mode

│  │  ├─ Connector\_Type

│  │  ├─ Conversion\_State

│  │  └─ Adapter\_Enabled \[bool\]

│  │

│  ├─ FC\_Center\_Transport\_Schedule

│  │  ├─ Route\_ID

│  │  ├─ Allowed\_State

│  │  ├─ Allowed\_Start\_Time

│  │  ├─ Allowed\_End\_Time

│  │  ├─ Priority\_Level

│  │  ├─ Public\_Allowed \[bool\]

│  │  ├─ Service\_Allowed \[bool\]

│  │  └─ Emergency\_Override \[bool\]

│  │

│  ├─ FC\_Center\_Articulated\_Connection

│  │  ├─ Connection\_ID

│  │  ├─ Petal\_ID

│  │  ├─ Pivot\_Point

│  │  ├─ Flexible\_Joint

│  │  ├─ Magnetic\_Joint

│  │  ├─ Rotation\_Axis

│  │  ├─ Rotation\_Limit

│  │  ├─ Translation\_Limit

│  │  ├─ Alignment\_State

│  │  └─ Connection\_State

│  │

│  ├─ FC\_Center\_Magnetic\_Transit

│  │  ├─ Magnetic\_Field\_State

│  │  ├─ Magnetic\_Assist

│  │  ├─ Magnetic\_Alignment

│  │  ├─ Magnetic\_Lock

│  │  ├─ Magnetic\_Release

│  │  └─ Magnetic\_Safety

│  │

│  ├─ FC\_Center\_Petal\_Fold\_Transit

│  │  ├─ Petal\_ID

│  │  ├─ Fold\_Progress \[float 0–1\]

│  │  ├─ Route\_Deformation

│  │  ├─ Route\_Orientation\_Update

│  │  ├─ Vehicle\_Orientation\_Update

│  │  ├─ Gravity\_Compensation

│  │  ├─ Magnetic\_Compensation

│  │  └─ Transit\_Continuity\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_Bridge\_State

│  │  ├─ Bridge\_ID

│  │  ├─ Required\_For\_Current\_State \[bool\]

│  │  ├─ Active \[bool\]

│  │  ├─ Folded \[bool\]

│  │  ├─ Locked \[bool\]

│  │  ├─ Retracted \[bool\]

│  │  └─ Bridge\_State

│  │

│  ├─ FC\_Center\_Route\_Consolidation

│  │  ├─ Source\_Route\_Count

│  │  ├─ Target\_Route\_Count

│  │  ├─ Merge\_State

│  │  ├─ Merge\_Point

│  │  ├─ Consolidated\_Route

│  │  └─ Unused\_Route\_Disable

│  │

│  ├─ FC\_Center\_Public\_Access

│  │  ├─ Public\_Entry

│  │  ├─ Public\_Exit

│  │  ├─ Civic\_Access

│  │  ├─ Education\_Access

│  │  └─ Council\_Access

│  │

│  ├─ FC\_Center\_Service\_Access

│  │  ├─ Service\_Entry

│  │  ├─ Service\_Exit

│  │  ├─ Maintenance\_Access

│  │  ├─ Utility\_Access

│  │  └─ Logistics\_Access

│  │

│  ├─ FC\_Center\_Emergency\_Access

│  │  ├─ Emergency\_Route

│  │  ├─ Emergency\_Entry

│  │  ├─ Emergency\_Exit

│  │  ├─ Evacuation\_Route

│  │  └─ Emergency\_Override

│  │

│  └─ FC\_Center\_Transport\_Debug

│     ├─ Show\_Active\_Route

│     ├─ Show\_Transport\_Mode

│     ├─ Show\_Route\_State

│     ├─ Show\_Articulated\_Joints

│     ├─ Show\_Magnetic\_Connections

│     ├─ Show\_Bridge\_State

│     └─ Show\_Route\_Continuity

│  │

│  ├─ FC\_Center\_Internal\_Circulation

│  │  ├─ Circulation\_Root

│  │  ├─ Circulation\_State

│  │  ├─ Current\_Center\_State

│  │  └─ Circulation\_Enabled \[bool\]

│  │

│  ├─ FC\_Center\_Ring\_Corridor

│  │  ├─ Ring\_ID

│  │  ├─ Corridor\_Radius

│  │  ├─ Corridor\_Width

│  │  ├─ Corridor\_Height

│  │  ├─ Corridor\_Level

│  │  ├─ Corridor\_Direction

│  │  ├─ One\_Way \[bool\]

│  │  ├─ Public\_Allowed \[bool\]

│  │  ├─ Service\_Allowed \[bool\]

│  │  └─ Corridor\_State

│  │

│  ├─ FC\_Center\_Radial\_Corridor

│  │  ├─ Corridor\_ID

│  │  ├─ Source\_Ring\_ID

│  │  ├─ Target\_Ring\_ID

│  │  ├─ Target\_Petal\_ID

│  │  ├─ Corridor\_Width

│  │  ├─ Corridor\_Height

│  │  ├─ Radial\_Angle

│  │  ├─ Corridor\_Length

│  │  ├─ Public\_Allowed \[bool\]

│  │  ├─ Service\_Allowed \[bool\]

│  │  └─ Corridor\_State

│  │

│  ├─ FC\_Center\_Vertical\_Transport

│  │  ├─ Vertical\_Route\_ID

│  │  ├─ Source\_Level

│  │  ├─ Target\_Level

│  │  ├─ Hyperlink\_Access \[bool\]

│  │  ├─ Lift\_Access \[bool\]

│  │  ├─ Vertical\_Shaft

│  │  ├─ Transfer\_Point

│  │  ├─ Capacity

│  │  ├─ Priority\_Level

│  │  └─ Vertical\_Transport\_State

│  │

│  ├─ FC\_Center\_Public\_Circulation

│  │  ├─ Public\_Route

│  │  ├─ Civic\_Plaza\_Route

│  │  ├─ Education\_Route

│  │  ├─ Council\_Route

│  │  ├─ Petal\_Transfer\_Route

│  │  └─ Stem\_Transfer\_Route

│  │

│  ├─ FC\_Center\_Service\_Path

│  │  ├─ Service\_Route\_ID

│  │  ├─ Utility\_Access

│  │  ├─ Maintenance\_Access

│  │  ├─ Cargo\_Access

│  │  ├─ Mechanical\_Access

│  │  ├─ Restricted\_Access \[bool\]

│  │  └─ Service\_Path\_State

│  │

│  ├─ FC\_Center\_Emergency\_Path

│  │  ├─ Emergency\_Route\_ID

│  │  ├─ Evacuation\_Path

│  │  ├─ Shelter\_Access

│  │  ├─ Emergency\_Stem\_Access

│  │  ├─ Emergency\_Petal\_Access

│  │  ├─ Route\_Redundancy

│  │  ├─ Blocked\_Route\_Bypass

│  │  └─ Emergency\_Path\_State

│  │

│  ├─ FC\_Center\_Access\_Control

│  │  ├─ Access\_Zone\_ID

│  │  ├─ Public\_Access \[bool\]

│  │  ├─ Staff\_Access \[bool\]

│  │  ├─ Service\_Access \[bool\]

│  │  ├─ Restricted\_Access \[bool\]

│  │  ├─ Emergency\_Override \[bool\]

│  │  └─ Access\_State

│  │

│  ├─ FC\_Center\_Circulation\_Connection

│  │  ├─ Connection\_ID

│  │  ├─ Source\_Route\_ID

│  │  ├─ Target\_Route\_ID

│  │  ├─ Connection\_Point

│  │  ├─ Transfer\_Type

│  │  ├─ Connection\_State

│  │  └─ Connection\_Enabled \[bool\]

│  │

│  ├─ FC\_Center\_Circulation\_Clearance

│  │  ├─ Minimum\_Walk\_Clearance

│  │  ├─ Vehicle\_Clearance

│  │  ├─ Vertical\_Clearance

│  │  ├─ Service\_Clearance

│  │  ├─ Emergency\_Clearance

│  │  └─ Clearance\_Valid \[bool\]

│  │

│  └─ FC\_Center\_Circulation\_Debug

│     ├─ Show\_Ring\_Corridor

│     ├─ Show\_Radial\_Corridor

│     ├─ Show\_Vertical\_Route

│     ├─ Show\_Public\_Route

│     ├─ Show\_Service\_Route

│     ├─ Show\_Emergency\_Route

│     └─ Show\_Access\_State

│&nbsp;&nbsp;

│  ├─ FC\_Center\_Service\_Core

│  │  ├─ Service\_Core\_ID

│  │  ├─ Service\_Core\_Root

│  │  ├─ Service\_Core\_State

│  │  ├─ Service\_Core\_Capacity

│  │  └─ Service\_Core\_Enabled \[bool\]

│  │

│  ├─ FC\_Center\_Utility\_Core

│  │  ├─ Utility\_Core

│  │  ├─ Utility\_Zone\_ID

│  │  ├─ Utility\_Route

│  │  ├─ Utility\_Capacity

│  │  ├─ Utility\_Load

│  │  ├─ Utility\_State

│  │  └─ Utility\_Enabled \[bool\]

│  │

│  ├─ FC\_Center\_Power\_Interface

│  │  ├─ Power\_Input

│  │  ├─ Power\_Output

│  │  ├─ Power\_Source\_ID

│  │  ├─ Power\_Target\_ID

│  │  ├─ Power\_Capacity

│  │  ├─ Power\_Load

│  │  ├─ Backup\_Power

│  │  ├─ Emergency\_Power

│  │  ├─ Power\_Isolation

│  │  └─ Power\_State

│  │

│  ├─ FC\_Center\_Data\_Interface

│  │  ├─ Data\_Input

│  │  ├─ Data\_Output

│  │  ├─ Network\_ID

│  │  ├─ Data\_Route

│  │  ├─ Control\_Link

│  │  ├─ Protection\_Network\_Link

│  │  ├─ Transport\_Network\_Link

│  │  ├─ Stem\_Network\_Link

│  │  ├─ Root\_Network\_Link

│  │  ├─ Backup\_Data\_Link

│  │  └─ Data\_State

│  │

│  ├─ FC\_Center\_Fluid\_Interface

│  │  ├─ Fluid\_Input

│  │  ├─ Fluid\_Output

│  │  ├─ Fluid\_Type

│  │  ├─ Fluid\_Route

│  │  ├─ Flow\_Rate

│  │  ├─ Pressure

│  │  ├─ Storage\_Link

│  │  ├─ Isolation\_Valve

│  │  ├─ Emergency\_Shutoff

│  │  └─ Fluid\_State

│  │

│  ├─ FC\_Center\_Maintenance\_Access

│  │  ├─ Maintenance\_Route

│  │  ├─ Maintenance\_Entry

│  │  ├─ Maintenance\_Exit

│  │  ├─ Inspection\_Point

│  │  ├─ Repair\_Point

│  │  ├─ Service\_Hatch

│  │  ├─ Restricted\_Access \[bool\]

│  │  └─ Maintenance\_State

│  │

│  ├─ FC\_Center\_Emergency\_Service

│  │  ├─ Emergency\_Power

│  │  ├─ Emergency\_Data

│  │  ├─ Emergency\_Fluid

│  │  ├─ Emergency\_Air

│  │  ├─ Emergency\_Water

│  │  ├─ Emergency\_Shutoff

│  │  ├─ Emergency\_Bypass

│  │  ├─ Emergency\_Service\_Route

│  │  └─ Emergency\_Service\_State

│  │

│  ├─ FC\_Center\_Service\_Clearance

│  │  ├─ Utility\_Clearance

│  │  ├─ Power\_Clearance

│  │  ├─ Data\_Clearance

│  │  ├─ Fluid\_Clearance

│  │  ├─ Maintenance\_Clearance

│  │  ├─ Emergency\_Clearance

│  │  └─ Clearance\_Valid \[bool\]

│  │

│  └─ FC\_Center\_Service\_Debug

│     ├─ Show\_Power\_Route

│     ├─ Show\_Data\_Route

│     ├─ Show\_Fluid\_Route

│     ├─ Show\_Service\_Route

│     ├─ Show\_Isolation\_Zone

│     └─ Show\_Service\_State  
│&nbsp;

│  ├─ FC\_Center\_Environmental\_Service

│  │  ├─ Environmental\_Service\_ID

│  │  ├─ Environmental\_Zone\_ID

│  │  ├─ Environmental\_State

│  │  ├─ Environmental\_Enabled \[bool\]

│  │  ├─ Air\_Supply

│  │  ├─ Air\_Return

│  │  ├─ Ventilation

│  │  ├─ Air\_Pressure

│  │  ├─ Pressure\_Compensation

│  │  ├─ Oxygen\_Level

│  │  ├─ Temperature\_Control

│  │  ├─ Humidity\_Control

│  │  ├─ Water\_Service

│  │  ├─ Water\_Recycling

│  │  ├─ Waste\_Service

│  │  ├─ Waste\_Isolation

│  │  ├─ Submerge\_Environmental\_Mode

│  │  ├─ Deep\_Sea\_Environmental\_Mode

│  │  ├─ Emergency\_Air\_Mode

│  │  ├─ Emergency\_Pressure\_Mode

│  │  ├─ Environmental\_Load

│  │  ├─ Environmental\_Capacity

│  │  └─ Environmental\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_Service\_Distribution

│  │  ├─ Service\_Distribution\_ID

│  │  ├─ Distribution\_Root

│  │  ├─ Distribution\_State

│  │  ├─ Distribution\_Enabled \[bool\]

│  │  ├─ Source\_Service\_ID

│  │  ├─ Target\_Service\_ID

│  │  ├─ Center\_Service\_Route

│  │  ├─ Petal\_Service\_Route

│  │  ├─ Stem\_Service\_Route

│  │  ├─ Protection\_Service\_Route

│  │  ├─ Transport\_Service\_Route

│  │  ├─ Public\_Service\_Route

│  │  ├─ Service\_Branch\_Point

│  │  ├─ Service\_Junction

│  │  ├─ Route\_Priority

│  │  ├─ Route\_Capacity

│  │  ├─ Route\_Load

│  │  ├─ Route\_State

│  │  ├─ Primary\_Route

│  │  ├─ Secondary\_Route

│  │  ├─ Redundant\_Route

│  │  ├─ Emergency\_Bypass\_Route

│  │  ├─ Distribution\_Balance

│  │  ├─ Distribution\_Override

│  │  └─ Distribution\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_Service\_Isolation

│  │  ├─ Isolation\_ID

│  │  ├─ Isolation\_Zone\_ID

│  │  ├─ Isolation\_State

│  │  ├─ Isolation\_Enabled \[bool\]

│  │  ├─ Isolation\_Source\_ID

│  │  ├─ Isolation\_Target\_ID

│  │  ├─ Power\_Isolated \[bool\]

│  │  ├─ Data\_Isolated \[bool\]

│  │  ├─ Fluid\_Isolated \[bool\]

│  │  ├─ Environmental\_Isolated \[bool\]

│  │  ├─ Transport\_Service\_Isolated \[bool\]

│  │  ├─ Petal\_Service\_Isolated \[bool\]

│  │  ├─ Stem\_Service\_Isolated \[bool\]

│  │  ├─ Protection\_Service\_Isolated \[bool\]

│  │  ├─ Automatic\_Isolation \[bool\]

│  │  ├─ Manual\_Isolation \[bool\]

│  │  ├─ Emergency\_Isolation \[bool\]

│  │  ├─ Pressure\_Isolation

│  │  ├─ Flood\_Isolation

│  │  ├─ Fire\_Isolation

│  │  ├─ Structural\_Failure\_Isolation

│  │  ├─ Isolation\_Boundary

│  │  ├─ Isolation\_Seal

│  │  ├─ Isolation\_Bypass

│  │  ├─ Reconnect\_Allowed \[bool\]

│  │  ├─ Reconnect\_State

│  │  └─ Isolation\_Valid \[bool\]

│

│  ├─ FC\_Center\_Protection\_Interface

│  │  ├─ Protection\_Interface\_ID

│  │  ├─ Protection\_Control\_Link

│  │  ├─ Protection\_Network\_ID

│  │  ├─ Pylon\_Network\_Link

│  │  ├─ Field\_State\_Input

│  │  ├─ Field\_State\_Output

│  │  ├─ Protection\_Mode

│  │  ├─ Protection\_Priority

│  │  ├─ Protection\_Enabled \[bool\]

│  │  ├─ Emergency\_Protection\_Link

│  │  └─ Protection\_Interface\_State

│  │

│  ├─ FC\_Center\_Protection\_Control

│  │  ├─ Control\_Center\_ID

│  │  ├─ Control\_Source\_ID

│  │  ├─ Control\_Target\_ID

│  │  ├─ Enable\_Command

│  │  ├─ Disable\_Command

│  │  ├─ Strength\_Command

│  │  ├─ Coverage\_Command

│  │  ├─ Emergency\_Command

│  │  ├─ Manual\_Override

│  │  └─ Control\_State

│  │

│  ├─ FC\_Center\_Pylon\_Network\_Interface

│  │  ├─ Pylon\_ID

│  │  ├─ Pylon\_Group\_ID

│  │  ├─ Pylon\_Zone\_ID

│  │  ├─ Pylon\_Active \[bool\]

│  │  ├─ Pylon\_Health\_State

│  │  ├─ Pylon\_Field\_Strength

│  │  ├─ Pylon\_Coverage\_Radius

│  │  ├─ Pylon\_Network\_State

│  │  └─ Pylon\_Connection\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_Field\_State\_Interface

│  │  ├─ Field\_ID

│  │  ├─ Field\_Active \[bool\]

│  │  ├─ Field\_Strength

│  │  ├─ Field\_Coverage

│  │  ├─ Field\_Overlap

│  │  ├─ Field\_Gap

│  │  ├─ Field\_Stability

│  │  ├─ Field\_Load

│  │  ├─ Field\_Failure\_State

│  │  └─ Field\_State

│  │

│  ├─ FC\_Center\_Protection\_Zone\_Interface

│  │  ├─ Protection\_Zone\_ID

│  │  ├─ Petal\_ID

│  │  ├─ Zone\_ID

│  │  ├─ Required\_Coverage

│  │  ├─ Current\_Coverage

│  │  ├─ Protection\_Level

│  │  ├─ Priority\_Level

│  │  └─ Zone\_Protected \[bool\]

│  │

│  ├─ FC\_Center\_Protection\_State

│  │  ├─ Normal\_Protection

│  │  ├─ Trade\_Protection

│  │  ├─ Closed\_State\_Protection

│  │  ├─ Submerge\_Protection

│  │  ├─ Deep\_Sea\_Protection

│  │  └─ Emergency\_Protection

│  │

│  ├─ FC\_Center\_Protection\_Failure\_Interface

│  │  ├─ Failed\_Pylon\_ID

│  │  ├─ Failed\_Zone\_ID

│  │  ├─ Coverage\_Lost

│  │  ├─ Field\_Instability

│  │  ├─ Reroute\_Protection

│  │  ├─ Increase\_Neighbor\_Strength

│  │  ├─ Isolate\_Failed\_Pylon

│  │  └─ Failure\_State

│  │

│  ├─ FC\_Center\_Emergency\_Protection

│  │  ├─ Emergency\_Trigger

│  │  ├─ Emergency\_Coverage

│  │  ├─ Emergency\_Strength

│  │  ├─ Emergency\_Priority

│  │  ├─ Emergency\_Power\_Request

│  │  ├─ Emergency\_Network\_Override

│  │  └─ Emergency\_Protection\_State

│  │

│  ├─ FC\_Center\_Protection\_Service\_Interface

│  │  ├─ Power\_Link

│  │  ├─ Data\_Link

│  │  ├─ Service\_Link

│  │  ├─ Maintenance\_Link

│  │  ├─ Backup\_Power\_Link

│  │  └─ Service\_State

│  │

│  └─ FC\_Center\_Protection\_Debug

│     ├─ Show\_Pylon\_ID

│     ├─ Show\_Protection\_Zone

│     ├─ Show\_Field\_Coverage

│     ├─ Show\_Field\_Overlap

│     ├─ Show\_Field\_Gap

│     ├─ Show\_Failed\_Pylon

│     └─ Show\_Protection\_State

│

│  ├─ FC\_Center\_State

│  │  ├─ Normal\_State

│  │  ├─ Trade\_State

│  │  ├─ Close\_State

│  │  ├─ Submerge\_State

│  │  ├─ Deep\_Sea\_State

│  │  ├─ Emergency\_State

│  │  ├─ Previous\_State

│  │  ├─ Current\_State

│  │  ├─ Target\_State

│  │  ├─ State\_Transition\_Progress \[float 0–1\]

│  │  ├─ Center\_Operational \[bool\]

│  │  ├─ Public\_Access\_Enabled \[bool\]

│  │  ├─ Service\_Access\_Enabled \[bool\]

│  │  ├─ Transport\_Enabled \[bool\]

│  │  ├─ Protection\_Enabled \[bool\]

│  │  ├─ Utility\_Enabled \[bool\]

│  │  ├─ Environmental\_Service\_Enabled \[bool\]

│  │  ├─ Emergency\_Service\_Enabled \[bool\]

│  │  └─ State\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_Normal\_State

│  │  ├─ Public\_Access

│  │  ├─ Civic\_Access

│  │  ├─ Education\_Access

│  │  ├─ Council\_Access

│  │  ├─ Standard\_Transport

│  │  ├─ Standard\_Protection

│  │  └─ Standard\_Service

│  │

│  ├─ FC\_Center\_Trade\_State

│  │  ├─ Trade\_Access\_Enabled \[bool\]

│  │  ├─ External\_Visitor\_Access

│  │  ├─ Public\_Transport\_Priority

│  │  ├─ Petal\_Access\_Priority

│  │  ├─ Shore\_Access\_State

│  │  ├─ Protection\_Trade\_Mode

│  │  ├─ Service\_Load\_Mode

│  │  └─ Trade\_State\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_Close\_State

│  │  ├─ Petal\_Close\_Active \[bool\]

│  │  ├─ Center\_Clearance\_Lock

│  │  ├─ Building\_Clearance\_Lock

│  │  ├─ Transport\_Reconfiguration

│  │  ├─ Bridge\_State\_Update

│  │  ├─ Service\_Route\_Update

│  │  ├─ Protection\_State\_Update

│  │  └─ Close\_State\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_Submerge\_State

│  │  ├─ Submerge\_Active \[bool\]

│  │  ├─ Submerge\_Progress \[float 0–1\]

│  │  ├─ Pressure\_Mode

│  │  ├─ Environmental\_Mode

│  │  ├─ Transport\_Submerge\_Mode

│  │  ├─ Service\_Isolation\_Mode

│  │  ├─ Protection\_Submerge\_Mode

│  │  └─ Submerge\_State\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_Deep\_Sea\_State

│  │  ├─ Deep\_Sea\_Mode \[bool\]

│  │  ├─ Pressure\_Level

│  │  ├─ Hazard\_Level

│  │  ├─ Occupancy\_Mode

│  │  ├─ Restricted\_Access\_Mode

│  │  ├─ Environmental\_Deep\_Sea\_Mode

│  │  ├─ Protection\_Deep\_Sea\_Mode

│  │  ├─ Service\_Deep\_Sea\_Mode

│  │  ├─ Transport\_Deep\_Sea\_Mode

│  │  └─ Deep\_Sea\_State\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_Emergency\_State

│  │  ├─ Emergency\_Active \[bool\]

│  │  ├─ Emergency\_Type

│  │  ├─ Emergency\_Priority

│  │  ├─ Emergency\_Transport

│  │  ├─ Emergency\_Protection

│  │  ├─ Emergency\_Service

│  │  ├─ Emergency\_Isolation

│  │  ├─ Emergency\_Evacuation

│  │  ├─ Manual\_Override

│  │  └─ Emergency\_State\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_State\_Transition

│  │  ├─ Source\_State

│  │  ├─ Target\_State

│  │  ├─ Transition\_Progress \[float 0–1\]

│  │  ├─ Transition\_Delay

│  │  ├─ Transition\_Limit

│  │  ├─ Transition\_Override

│  │  └─ Transition\_Valid \[bool\]

│  │

│  └─ FC\_Center\_State\_Debug

│     ├─ Show\_Current\_State

│     ├─ Show\_Target\_State

│     ├─ Show\_Access\_State

│     ├─ Show\_Transport\_State

│     ├─ Show\_Protection\_State

│     ├─ Show\_Service\_State

│     └─ Show\_State\_Validation

│&nbsp;&nbsp;

│  ├─ FC\_Center\_Socket

│  │  ├─ Socket\_ID

│  │  ├─ Socket\_Type

│  │  ├─ Socket\_Name

│  │  ├─ Socket\_Group\_ID

│  │  ├─ Parent\_ID

│  │  ├─ Target\_ID

│  │  ├─ Socket\_Transform

│  │  ├─ Socket\_Local\_Transform

│  │  ├─ Socket\_World\_Transform

│  │  ├─ Socket\_Position

│  │  ├─ Socket\_Rotation

│  │  ├─ Socket\_Scale

│  │  ├─ Socket\_Normal

│  │  ├─ Socket\_Tangent

│  │  ├─ Socket\_Axis

│  │  ├─ Socket\_Clearance

│  │  ├─ Socket\_Radius

│  │  ├─ Socket\_Orientation\_Mode

│  │  ├─ Socket\_Connection\_Type

│  │  ├─ Socket\_Connection\_State

│  │  ├─ Socket\_Lock\_State

│  │  ├─ Socket\_Seal\_State

│  │  ├─ Socket\_Active \[bool\]

│  │  ├─ Socket\_Occupied \[bool\]

│  │  ├─ Socket\_Enabled \[bool\]

│  │  └─ Socket\_State

│  │

│  ├─ FC\_Center\_Socket\_Petal

│  │  ├─ Petal\_ID

│  │  ├─ Petal\_Attach\_Socket

│  │  ├─ Petal\_Rig\_Left\_Socket

│  │  ├─ Petal\_Rig\_Right\_Socket

│  │  ├─ Petal\_Transport\_Socket

│  │  ├─ Petal\_Utility\_Socket

│  │  └─ Petal\_Socket\_State

│  │

│  ├─ FC\_Center\_Socket\_Stem

│  │  ├─ Stem\_ID

│  │  ├─ Stem\_Structural\_Socket

│  │  ├─ Stem\_Transport\_Socket

│  │  ├─ Stem\_Utility\_Socket

│  │  ├─ Stem\_Service\_Socket

│  │  └─ Stem\_Socket\_State

│  │

│  ├─ FC\_Center\_Socket\_Transport

│  │  ├─ Transport\_Socket\_ID

│  │  ├─ Route\_ID

│  │  ├─ Transport\_Mode

│  │  ├─ Entry\_Socket

│  │  ├─ Exit\_Socket

│  │  ├─ Transfer\_Socket

│  │  └─ Transport\_Socket\_State

│  │

│  ├─ FC\_Center\_Socket\_Service

│  │  ├─ Service\_Socket\_ID

│  │  ├─ Power\_Socket

│  │  ├─ Data\_Socket

│  │  ├─ Fluid\_Socket

│  │  ├─ Environmental\_Socket

│  │  ├─ Maintenance\_Socket

│  │  └─ Service\_Socket\_State

│  │

│  ├─ FC\_Center\_Socket\_Protection

│  │  ├─ Protection\_Socket\_ID

│  │  ├─ Pylon\_Link\_Socket

│  │  ├─ Control\_Link\_Socket

│  │  ├─ Power\_Link\_Socket

│  │  ├─ Data\_Link\_Socket

│  │  └─ Protection\_Socket\_State

│  │

│  ├─ FC\_Center\_Socket\_Rig

│  │  ├─ Rig\_Socket\_ID

│  │  ├─ Rig\_Part\_ID

│  │  ├─ Rig\_Pivot

│  │  ├─ Rig\_Parent\_ID

│  │  ├─ Rig\_Control\_Link

│  │  └─ Rig\_Socket\_State

│  │

│  ├─ FC\_Center\_Socket\_Validation

│  │  ├─ Validate\_Parent

│  │  ├─ Validate\_Target

│  │  ├─ Validate\_Transform

│  │  ├─ Validate\_Orientation

│  │  ├─ Validate\_Clearance

│  │  ├─ Validate\_Occupancy

│  │  └─ Socket\_Valid \[bool\]

│  │

│  └─ FC\_Center\_Socket\_Debug

│     ├─ Show\_Socket\_ID

│     ├─ Show\_Socket\_Type

│     ├─ Show\_Socket\_Axis

│     ├─ Show\_Socket\_Normal

│     ├─ Show\_Socket\_Clearance

│     ├─ Show\_Connection\_State

│     └─ Show\_Occupancy

│&nbsp;&nbsp;

│  ├─ FC\_Center\_To\_Petal

│  │  ├─ Petal\_ID

│  │  ├─ Connection\_ID

│  │  ├─ Connection\_Point

│  │  ├─ Connection\_Transform

│  │  ├─ Connection\_Local\_Space

│  │  ├─ Connection\_State

│  │  ├─ Connection\_Enabled \[bool\]

│  │  ├─ Connection\_Clearance

│  │  ├─ Structural\_Interface

│  │  ├─ Rig\_Interface

│  │  ├─ Transport\_Interface

│  │  ├─ Utility\_Interface

│  │  ├─ Service\_Interface

│  │  ├─ Data\_Interface

│  │  ├─ Power\_Interface

│  │  └─ Emergency\_Interface

│  │

│  ├─ FC\_Center\_To\_Petal\_Structure

│  │  ├─ Structural\_Attach\_Point

│  │  ├─ Structural\_Load\_Input

│  │  ├─ Structural\_Load\_Output

│  │  ├─ Load\_Transfer

│  │  ├─ Load\_Limit

│  │  ├─ Support\_State

│  │  └─ Structural\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_To\_Petal\_Rig

│  │  ├─ Petal\_Root

│  │  ├─ Inner\_Pivot

│  │  ├─ Left\_Rig\_Link

│  │  ├─ Right\_Rig\_Link

│  │  ├─ Rest\_Transform

│  │  ├─ Open\_Transform

│  │  ├─ Closed\_Transform

│  │  ├─ Current\_Transform

│  │  ├─ Rig\_State

│  │  └─ Rig\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_To\_Petal\_Transport

│  │  ├─ Transport\_Connection\_ID

│  │  ├─ Petal\_Route\_ID

│  │  ├─ Center\_Route\_ID

│  │  ├─ Entry\_Point

│  │  ├─ Exit\_Point

│  │  ├─ Transfer\_Point

│  │  ├─ Transport\_Mode

│  │  ├─ Articulated\_Joint

│  │  ├─ Magnetic\_Connection

│  │  ├─ Route\_Continuity

│  │  ├─ Transport\_State

│  │  └─ Transport\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_To\_Petal\_Utility

│  │  ├─ Utility\_Connection\_ID

│  │  ├─ Power\_Link

│  │  ├─ Data\_Link

│  │  ├─ Fluid\_Link

│  │  ├─ Environmental\_Link

│  │  ├─ Service\_Link

│  │  ├─ Utility\_Capacity

│  │  ├─ Utility\_Load

│  │  ├─ Utility\_Isolation

│  │  ├─ Utility\_State

│  │  └─ Utility\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_To\_Petal\_State

│  │  ├─ Petal\_State

│  │  ├─ Center\_State

│  │  ├─ Open\_State

│  │  ├─ Close\_State

│  │  ├─ Submerge\_State

│  │  ├─ Emergency\_State

│  │  ├─ Transition\_Progress \[float 0–1\]

│  │  └─ Interface\_State\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_To\_Petal\_Clearance

│  │  ├─ Structural\_Clearance

│  │  ├─ Rig\_Clearance

│  │  ├─ Transport\_Clearance

│  │  ├─ Utility\_Clearance

│  │  ├─ Open\_State\_Clearance

│  │  ├─ Transition\_Clearance

│  │  ├─ Closed\_State\_Clearance

│  │  └─ Clearance\_Valid \[bool\]

│  │

│  ├─ FC\_Center\_To\_Petal\_Isolation

│  │  ├─ Isolate\_Power \[bool\]

│  │  ├─ Isolate\_Data \[bool\]

│  │  ├─ Isolate\_Fluid \[bool\]

│  │  ├─ Isolate\_Transport \[bool\]

│  │  ├─ Isolate\_Service \[bool\]

│  │  ├─ Emergency\_Isolation \[bool\]

│  │  ├─ Reconnect\_Allowed \[bool\]

│  │  └─ Isolation\_State

│  │

│  └─ FC\_Center\_To\_Petal\_Debug

│     ├─ Show\_Connection\_Point

│     ├─ Show\_Load\_Path

│     ├─ Show\_Rig\_Link

│     ├─ Show\_Transport\_Link

│     ├─ Show\_Utility\_Link

│     ├─ Show\_Clearance

│     └─ Show\_Interface\_State

│&nbsp;&nbsp;

│  └─ FC\_Center\_To\_Stem

│     ├─ Stem\_ID

│     ├─ Stem\_Root

│     ├─ Connection\_ID

│     ├─ Connection\_Point

│     ├─ Connection\_Transform

│     ├─ Connection\_Local\_Space

│     ├─ Connection\_State

│     ├─ Connection\_Enabled \[bool\]

│     ├─ Structural\_Interface

│     ├─ Transport\_Interface

│     ├─ Utility\_Interface

│     ├─ Service\_Interface

│     ├─ Data\_Interface

│     ├─ Power\_Interface

│     ├─ Load\_Transfer\_Interface

│     ├─ Pressure\_Interface

│     └─ Emergency\_Interface

│

│     ├─ FC\_Center\_To\_Stem\_Structure

│     │  ├─ Structural\_Attach\_Point

│     │  ├─ Center\_Load\_Input

│     │  ├─ Stem\_Load\_Output

│     │  ├─ Load\_Transfer

│     │  ├─ Load\_Distribution

│     │  ├─ Load\_Balance

│     │  ├─ Load\_Limit

│     │  ├─ Structural\_Alignment

│     │  ├─ Structural\_State

│     │  └─ Structural\_Valid \[bool\]

│

│     ├─ FC\_Center\_To\_Stem\_Transport

│     │  ├─ Transport\_Connection\_ID

│     │  ├─ Center\_Route\_ID

│     │  ├─ Stem\_Route\_ID

│     │  ├─ Entry\_Point

│     │  ├─ Exit\_Point

│     │  ├─ Transfer\_Point

│     │  ├─ Hyperlink\_Link

│     │  ├─ Lift\_Link

│     │  ├─ Vertical\_Transfer

│     │  ├─ Route\_Continuity

│     │  ├─ Transport\_State

│     │  └─ Transport\_Valid \[bool\]

│

│     ├─ FC\_Center\_To\_Stem\_Utility

│     │  ├─ Utility\_Connection\_ID

│     │  ├─ Power\_Link

│     │  ├─ Data\_Link

│     │  ├─ Fluid\_Link

│     │  ├─ Environmental\_Link

│     │  ├─ Service\_Link

│     │  ├─ Utility\_Capacity

│     │  ├─ Utility\_Load

│     │  ├─ Utility\_Isolation

│     │  ├─ Utility\_State

│     │  └─ Utility\_Valid \[bool\]

│

│     ├─ FC\_Center\_To\_Stem\_Load\_Transfer

│     │  ├─ Load\_Source\_ID

│     │  ├─ Load\_Target\_ID

│     │  ├─ Vertical\_Load

│     │  ├─ Radial\_Load

│     │  ├─ Torsion\_Load

│     │  ├─ Dynamic\_Load

│     │  ├─ Shock\_Load

│     │  ├─ Current\_Load

│     │  ├─ Load\_Capacity

│     │  ├─ Load\_Margin

│     │  ├─ Load\_Transfer\_State

│     │  └─ Load\_Valid \[bool\]

│

│     ├─ FC\_Center\_To\_Stem\_Pressure

│     │  ├─ Pressure\_Interface\_ID

│     │  ├─ Center\_Pressure

│     │  ├─ Stem\_Pressure

│     │  ├─ Pressure\_Difference

│     │  ├─ Pressure\_Transition

│     │  ├─ Pressure\_Lock

│     │  ├─ Pressure\_Seal

│     │  ├─ Pressure\_Isolation

│     │  ├─ Pressure\_State

│     │  └─ Pressure\_Valid \[bool\]

│

│     ├─ FC\_Center\_To\_Stem\_Telescopic\_Interface

│     │  ├─ Stem\_Deploy\_Value

│     │  ├─ Stem\_Collapse\_Value

│     │  ├─ Stem\_Current\_Height

│     │  ├─ Stem\_Extended\_Height

│     │  ├─ Stem\_Collapsed\_Height

│     │  ├─ Collapse\_Rate

│     │  ├─ Shock\_Damping\_Value

│     │  ├─ Descent\_State

│     │  └─ Telescopic\_State\_Valid \[bool\]

│

│     ├─ FC\_Center\_To\_Stem\_State

│     │  ├─ Center\_State

│     │  ├─ Stem\_State

│     │  ├─ Normal\_State

│     │  ├─ Close\_State

│     │  ├─ Submerge\_State

│     │  ├─ Deep\_Sea\_State

│     │  ├─ Emergency\_State

│     │  ├─ Transition\_Progress \[float 0–1\]

│     │  └─ Interface\_State\_Valid \[bool\]

│

│     ├─ FC\_Center\_To\_Stem\_Clearance

│     │  ├─ Structural\_Clearance

│     │  ├─ Transport\_Clearance

│     │  ├─ Utility\_Clearance

│     │  ├─ Pressure\_Lock\_Clearance

│     │  ├─ Telescopic\_Clearance

│     │  ├─ Service\_Clearance

│     │  ├─ Emergency\_Clearance

│     │  └─ Clearance\_Valid \[bool\]

│

│     ├─ FC\_Center\_To\_Stem\_Isolation

│     │  ├─ Isolate\_Power \[bool\]

│     │  ├─ Isolate\_Data \[bool\]

│     │  ├─ Isolate\_Fluid \[bool\]

│     │  ├─ Isolate\_Transport \[bool\]

│     │  ├─ Isolate\_Pressure \[bool\]

│     │  ├─ Isolate\_Service \[bool\]

│     │  ├─ Emergency\_Isolation \[bool\]

│     │  ├─ Reconnect\_Allowed \[bool\]

│     │  └─ Isolation\_State

│

│     ├─ FC\_Center\_To\_Stem\_Emergency

│     │  ├─ Emergency\_Trigger

│     │  ├─ Emergency\_Transport\_Link

│     │  ├─ Emergency\_Power\_Link

│     │  ├─ Emergency\_Data\_Link

│     │  ├─ Emergency\_Pressure\_Seal

│     │  ├─ Emergency\_Isolation

│     │  ├─ Emergency\_Bypass

│     │  └─ Emergency\_State

│

│     └─ FC\_Center\_To\_Stem\_Debug

│        ├─ Show\_Connection\_Point

│        ├─ Show\_Load\_Path

│        ├─ Show\_Transport\_Link

│        ├─ Show\_Utility\_Link

│        ├─ Show\_Pressure\_Interface

│        ├─ Show\_Telescopic\_State

│        ├─ Show\_Clearance

│        └─ Show\_Interface\_State

│

│

├─ 03.03\_PETAL\_STRUCTURE

│  ├─ FC\_Flower\_Petal

│  │  ├─ Petal\_ID \[int\]

│  │  ├─ Petal\_Count \[int\]

│  │  ├─ Petal\_Length

│  │  ├─ Petal\_Width

│  │  ├─ Petal\_Thickness

│  │  ├─ Petal\_Profile

│  │  └─ Petal\_Rotation

│  │

│  ├─ FC\_Petal\_Inner\_Attach

│  ├─ FC\_Petal\_Outer\_Edge

│  ├─ FC\_Petal\_Left\_Edge

│  ├─ FC\_Petal\_Right\_Edge

│  ├─ FC\_Petal\_Shore\_Attach

│  └─ FC\_Petal\_Center\_Clearance

│

│

├─ 03.04\_PETAL\_STATE

│  ├─ FC\_Petal\_State

│  │  ├─ Petal\_ID

│  │  ├─ Open \[bool\]

│  │  ├─ Open\_Amount \[float\]

│  │  ├─ Target\_Height

│  │  └─ Transition\_Progress

│  │

│  ├─ FC\_Petal\_Open

│  ├─ FC\_Petal\_Close

│  └─ FC\_Petal\_State\_Transition

│

│

├─ 03.05\_PETAL\_RIG

│  │

│  ├─ FC\_Petal\_Rig

│  │  ├─ Petal\_ID

│  │  ├─ Rig\_Left

│  │  ├─ Rig\_Right

│  │  ├─ Inner\_Pivot

│  │  ├─ Left\_Pivot

│  │  ├─ Right\_Pivot

│  │  ├─ Raise\_Amount

│  │  ├─ Lower\_Amount

│  │  ├─ Twist\_Amount

│  │  └─ Rig\_State

│  │

│  ├─ FC\_Petal\_Rig\_Left

│  ├─ FC\_Petal\_Rig\_Right

│  ├─ FC\_Petal\_Rig\_Balance

│  ├─ FC\_Petal\_Rig\_Limit

│  └─ FC\_Petal\_Rig\_Debug

│

│

├─ 03.06\_FLOWER\_ZONE

│  │

│  ├─ FC\_Flower\_Zone

│  │  ├─ Petal\_ID \[int\]

│  │  ├─ Zone\_ID \[int\]

│  │  ├─ Distance\_From\_Center

│  │  ├─ Distance\_From\_Cone

│  │  ├─ Distance\_From\_Petal\_Edge

│  │  ├─ Current\_Height

│  │  └─ Current\_Petal\_State

│  │

│  ├─ FC\_Zone\_Petal

│  ├─ FC\_Zone\_Inner

│  ├─ FC\_Zone\_Middle

│  ├─ FC\_Zone\_Outer

│  ├─ FC\_Zone\_Shore

│  └─ FC\_Zone\_Transition

│

│

├─ 03.07\_FLOWER\_HEIGHT

│  ├─ FC\_Flower\_Height

│  │  ├─ Base\_Height

│  │  ├─ Petal\_ID

│  │  ├─ Zone\_ID

│  │  ├─ Distance\_Factor

│  │  ├─ Open\_Height

│  │  ├─ Closed\_Height

│  │  └─ Height\_Offset

│  │

│  └─ FC\_Flower\_Height\_State

│

│

├─ 03.08\_FLOWER\_SCATTER

│  ├─ FC\_Flower\_Scatter

│  │  ├─ Petal\_ID

│  │  ├─ Zone\_ID

│  │  ├─ Density

│  │  ├─ Seed

│  │  ├─ Scale\_Range

│  │  ├─ Height\_Range

│  │  ├─ Center\_Distance

│  │  └─ Petal\_State

│  │

│  ├─ FC\_Scatter\_By\_Petal

│  ├─ FC\_Scatter\_By\_Zone

│  ├─ FC\_Scatter\_Exclusion

│  └─ FC\_Scatter\_State\_Update

│

│

├─ 03.09\_FLOWER\_SHORE

│  │

│  ├─ FC\_Flower\_Shore

│  │  ├─ Shore\_ID

│  │  ├─ Petal\_ID

│  │  ├─ Connected \[bool\]

│  │  ├─ Connection\_Amount

│  │  ├─ Shore\_Width

│  │  └─ Shore\_Offset

│  │

│  ├─ FC\_Shore\_Petal\_Connector

│  ├─ FC\_Shore\_Detach

│  ├─ FC\_Shore\_Attach

│  ├─ FC\_Shore\_Edge

│  ├─ FC\_Shore\_Transition

│  └─ FC\_Shore\_Clearance

│

│

├─ 03.10\_PROTECTION\_NETWORK

│

│  ├─ FC\_Protection\_Network

│  │  ├─ Protection\_State

│  │  ├─ Coverage

│  │  ├─ Strength

│  │  ├─ Network\_ID

│  │  └─ Emergency\_Mode

│

│  ├─ FC\_Protection\_Pylon

│  │  ├─ Pylon\_ID

│  │  ├─ Zone\_ID

│  │  ├─ Position

│  │  ├─ Radius

│  │  ├─ Strength

│  │  └─ Active \[bool\]

│

│  ├─ FC\_Protection\_Field

│  ├─ FC\_Field\_Coverage

│  ├─ FC\_Field\_Overlap

│  ├─ FC\_Field\_Gap\_Detection

│  ├─ FC\_Protection\_Control\_Center

│  ├─ FC\_Protection\_State

│  ├─ FC\_Protection\_Failure

│  └─ FC\_Protection\_Debug

│

│

│

├─ 03.11\_STEM\_RING

│  │

│  ├─ FC\_STEM\_Ring

│  │  ├─ Ring\_ID \[int\]

│  │  ├─ Ring\_Count \[int\]

│  │  ├─ Ring\_Radius

│  │  ├─ Ring\_Height \[\>= 3m\]

│  │  ├─ Ring\_Thickness

│  │  ├─ Extended\_Z

│  │  ├─ Collapsed\_Z

│  │  ├─ Collapse\_Amount

│  │  ├─ Current\_Depth

│  │  ├─ Pressure\_Level

│  │  ├─ Hazard\_Level

│  │  ├─ Occupancy\_Allowed \[bool\]

│  │  ├─ Pressure\_Rating

│  │  ├─ Emergency\_Seal\_State

│  │  ├─ Transport\_Status

│  │  └─ City\_Submerged\_Mode \[bool\]

│  │

│  ├─ FC\_STEM\_Ring\_Shell

│  ├─ FC\_STEM\_Ring\_Floor

│  ├─ FC\_STEM\_Ring\_Interior

│  ├─ FC\_STEM\_Ring\_Service

│  └─ FC\_STEM\_Ring\_Clearance

│

│

├─ 03.12\_STEM\_TELESCOPIC\_SYSTEM

│  │

│  ├─ FC\_STEM\_Telescope

│  │  ├─ Deploy\_Amount \[0–1\]

│  │  ├─ Ring\_ID

│  │  ├─ Extended\_Z

│  │  ├─ Collapsed\_Z

│  │  ├─ Overlap

│  │  ├─ Clearance

│  │

│  ├─ FC\_STEM\_Ring\_Order

│  ├─ FC\_STEM\_Ring\_Nesting

│  ├─ FC\_STEM\_Ring\_Stop

│  ├─ FC\_STEM\_Collapse\_Limit

│  ├─ FC\_STEM\_Deploy\_Limit

│  ├─ FC\_STEM\_Staged\_Collapse

│  ├─ FC\_STEM\_Shock\_Absorption

│  ├─ FC\_STEM\_Load\_Distribution

│  ├─ FC\_STEM\_Descent\_Control

│  └─ FC\_STEM\_Emergency\_Stop

│

├─ 03.13\_STEM\_TRANSPORT

│  │

│  ├─ FC\_STEM\_Transport

│  ├─ FC\_STEM\_Walkway

│  ├─ FC\_STEM\_Vertical\_Transport

│  ├─ FC\_STEM\_Service\_Path

│  ├─ FC\_STEM\_Flower\_Access

│  ├─ FC\_STEM\_Root\_Access

│  ├─ FC\_STEM\_Pressure\_Transition

│  ├─ FC\_STEM\_Pressure\_Lock

│  ├─ FC\_STEM\_Emergency\_Access

│  ├─ FC\_STEM\_Occupancy\_Control

│  └─ FC\_STEM\_Depth\_Restriction

│

│

├─ 03.14\_RING\_CONNECTION

│  │

│  ├─ FC\_STEM\_Ring\_Connection

│  │  ├─ Connection\_ID

│  │  ├─ Source\_Ring\_ID

│  │  ├─ Target\_Ring\_ID

│  │  ├─ Connected \[bool\]

│  │  ├─ Extend\_Amount

│  │  └─ Lock\_State

│  │

│  ├─ FC\_Ring\_Port

│  ├─ FC\_Ring\_Bridge

│  ├─ FC\_Ring\_Bridge\_Extend

│  ├─ FC\_Ring\_Bridge\_Retract

│  ├─ FC\_Ring\_Port\_Align

│  ├─ FC\_Ring\_Port\_Lock

│  ├─ FC\_Ring\_Port\_Seal

│  └─ FC\_Ring\_Emergency\_Disconnect

│

│

├─ 03.15\_FLOWER\_STEM\_CONNECTION

│  ├─ FC\_Flower\_Stem\_Port

│  ├─ FC\_Flower\_Stem\_Transition

│  ├─ FC\_Flower\_Stem\_Transport

│  ├─ FC\_Flower\_Stem\_Structure

│  └─ FC\_Flower\_Stem\_Seal

│

│

├─ 03.16\_ROOT\_SYSTEM

│  │

│  ├─ FC\_Root

│  ├─ FC\_Root\_Core

│  ├─ FC\_Root\_Branch

│  ├─ FC\_Root\_Anchor

│  ├─ FC\_Root\_Energy\_Storage

│  ├─ FC\_Root\_Power\_Distribution

│  ├─ FC\_Root\_Logistics\_Hub

│  ├─ FC\_Root\_Cargo\_Transfer

│  ├─ FC\_Root\_Transport

│  ├─ FC\_Root\_Service

│  ├─ FC\_Root\_Maintenance

│  ├─ FC\_Root\_Emergency

│  ├─ FC\_Root\_Transition

│  └─ FC\_Root\_To\_Stem

│

│

├─ 03.17\_STRUCTURE\_DEBUG

│  │

│  ├─ FC\_Debug\_Petal\_ID

│  ├─ FC\_Debug\_Zone

│  ├─ FC\_Debug\_Rig

│  ├─ FC\_Debug\_Shore\_Connection

│  ├─ FC\_Debug\_Ring\_ID

│  ├─ FC\_Debug\_Ring\_Clearance

│  ├─ FC\_Debug\_Port

│  └─ FC\_Debug\_State

│

├─ 03.18\_STRUCTURE\_CLEARANCE

│  │

│  ├─ FC\_Petal\_Rig\_Clearance

│  ├─ FC\_Petal\_To\_Petal\_Clearance

│  ├─ FC\_Petal\_To\_Center\_Clearance

│  ├─ FC\_Protection\_Field\_Clearance

│  ├─ FC\_Shore\_Clearance

│  ├─ FC\_Ring\_Nesting\_Clearance

│  ├─ FC\_Ring\_Port\_Clearance

│  ├─ FC\_Transport\_Clearance

│  ├─ FC\_Building\_To\_Center\_Clearance

│  ├─ FC\_Building\_Petal\_Close\_Clearance

│  ├─ FC\_Shore\_Docking\_Clearance

│  ├─ FC\_Protection\_Pylon\_Clearance

│  ├─ FC\_STEM\_Pressure\_Lock\_Clearance

│  └─ FC\_Root\_Stem\_Clearance

│

│

├─ 03.19\_STATE\_DEPENDENCY

│  │

│  ├─ FC\_State\_Dependency\_Controller

│  │  ├─ Global\_State

│  │  ├─ Transition\_Progress \[float 0–1\]

│  │  ├─ Previous\_State

│  │  ├─ Current\_State

│  │  └─ Target\_State

│  │

│  ├─ FC\_State\_Normal

│  ├─ FC\_State\_Open\_For\_Trade

│  ├─ FC\_State\_Prepare\_Close

│  ├─ FC\_State\_Close

│  ├─ FC\_State\_Protected

│  ├─ FC\_State\_Prepare\_Annual\_Submerge

│  ├─ FC\_State\_Prepare\_Submerge

│  ├─ FC\_State\_Submerge

│  ├─ FC\_State\_Submerged

│  ├─ FC\_State\_Deep\_Sea\_Operation

│  ├─ FC\_State\_Prepare\_Surface\_Return

│  ├─ FC\_State\_Prepare\_Deploy

│  ├─ FC\_State\_Deploy

│  └─ FC\_State\_Emergency

│

│  ├─ FC\_Dependency\_Transport

│  │  ├─ Stop\_Public\_Transport

│  │  ├─ Clear\_Transport\_Path

│  │  ├─ Lock\_Internal\_Transport

│  │  └─ Confirm\_Transport\_Clear

│  │

│  ├─ FC\_Dependency\_Ring\_Connection

│  │  ├─ Retract\_Bridge

│  │  ├─ Disconnect\_Port

│  │  ├─ Seal\_Port

│  │  └─ Confirm\_Disconnected

│  │

│  ├─ FC\_Dependency\_Shore

│  │  ├─ Shore\_Prepare

│  │  ├─ Shore\_Detach

│  │  ├─ Shore\_Secure

│  │  └─ Confirm\_Shore\_Clear

│  │

│  ├─ FC\_Dependency\_Petal

│  │  ├─ Petal\_Prepare

│  │  ├─ Petal\_Raise

│  │  ├─ Petal\_Close

│  │  ├─ Petal\_Open

│  │  └─ Confirm\_Petal\_State

│  │

│  ├─ FC\_Dependency\_Zone

│  │  ├─ Update\_Zone\_Height

│  │  ├─ Update\_Zone\_Clearance

│  │  ├─ Update\_Scatter\_Position

│  │  └─ Update\_Buildable\_Area

│  │

│  ├─ FC\_Dependency\_Protection

│  │  ├─ Protection\_Prepare

│  │  ├─ Protection\_Enable

│  │  ├─ Protection\_Disable

│  │  ├─ Check\_Field\_Coverage

│  │  └─ Confirm\_Protection\_State

│  │

│  ├─ FC\_Dependency\_Stem

│  │  ├─ Stem\_Prepare\_Collapse

│  │  ├─ Ring\_Disconnect

│  │  ├─ Ring\_Collapse

│  │  ├─ Ring\_Deploy

│  │  └─ Confirm\_Stem\_State

│  │

│  ├─ FC\_Dependency\_Pressure

│  │  ├─ Update\_Ring\_Depth

│  │  ├─ Update\_Pressure\_Level

│  │  ├─ Update\_Hazard\_Level

│  │  ├─ Update\_Occupancy

│  │  └─ Update\_Transport\_Restriction

│  │

│  ├─ FC\_Dependency\_Descent

│  │  ├─ Calculate\_Descent

│  │  ├─ Stage\_Stem\_Collapse

│  │  ├─ Apply\_Shock\_Damping

│  │  ├─ Monitor\_Load

│  │  └─ Confirm\_Stable\_Descent

│  │

│  ├─ FC\_Dependency\_Root

│  │  ├─ Root\_Prepare

│  │  ├─ Root\_Transition

│  │  ├─ Root\_Anchor\_State

│  │  └─ Confirm\_Root\_State

│  │

│  ├─ FC\_State\_Transition\_Order

│  ├─ FC\_State\_Transition\_Delay

│  ├─ FC\_State\_Transition\_Limit

│  ├─ FC\_State\_Transition\_Override

│  └─ FC\_State\_Transition\_Debug

││

│  \[03.20 reserved for top-level GAME\_READY system\]  
│

└─ 03.21\_RIG\_EXPORT\_INTERFACE

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Export\_Interface

&nbsp;&nbsp;&nbsp;│  ├─ Rig\_System\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Part\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Parent\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Root\_Transform

&nbsp;&nbsp;&nbsp;│  ├─ Local\_Transform

&nbsp;&nbsp;&nbsp;│  ├─ Pivot\_Transform

&nbsp;&nbsp;&nbsp;│  ├─ Rest\_Transform

&nbsp;&nbsp;&nbsp;│  └─ Export\_Enabled \[bool\]

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Part\_Classification

&nbsp;&nbsp;&nbsp;│  ├─ Static

&nbsp;&nbsp;&nbsp;│  ├─ Rigid\_Movable

&nbsp;&nbsp;&nbsp;│  ├─ Deformable

&nbsp;&nbsp;&nbsp;│  ├─ Telescopic

&nbsp;&nbsp;&nbsp;│  ├─ Connector

&nbsp;&nbsp;&nbsp;│  └─ Socket

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Petal\_Interface

&nbsp;&nbsp;&nbsp;│  ├─ Petal\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Petal\_Root

&nbsp;&nbsp;&nbsp;│  ├─ Rig\_Left

&nbsp;&nbsp;&nbsp;│  ├─ Rig\_Right

&nbsp;&nbsp;&nbsp;│  ├─ Inner\_Pivot

&nbsp;&nbsp;&nbsp;│  ├─ Left\_Pivot

&nbsp;&nbsp;&nbsp;│  ├─ Right\_Pivot

&nbsp;&nbsp;&nbsp;│  ├─ Open\_Value

&nbsp;&nbsp;&nbsp;│  ├─ Raise\_Value

&nbsp;&nbsp;&nbsp;│  ├─ Lower\_Value

&nbsp;&nbsp;&nbsp;│  └─ Twist\_Value

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Protection\_Interface

&nbsp;&nbsp;&nbsp;│  ├─ Pylon\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Pylon\_Root

&nbsp;&nbsp;&nbsp;│  ├─ Pylon\_Pivot

&nbsp;&nbsp;&nbsp;│  ├─ Active\_Value

&nbsp;&nbsp;&nbsp;│  └─ Field\_State

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Stem\_Interface

&nbsp;&nbsp;&nbsp;│  ├─ Ring\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Parent\_Ring\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Ring\_Pivot

&nbsp;&nbsp;&nbsp;│  ├─ Extended\_Transform

&nbsp;&nbsp;&nbsp;│  ├─ Collapsed\_Transform

&nbsp;&nbsp;&nbsp;│  ├─ Deploy\_Value

&nbsp;&nbsp;&nbsp;│  ├─ Collapse\_Value

&nbsp;&nbsp;&nbsp;│  ├─ Collapse\_Rate

&nbsp;&nbsp;&nbsp;│  ├─ Shock\_Damping\_Value

&nbsp;&nbsp;&nbsp;│  ├─ Current\_Depth

&nbsp;&nbsp;&nbsp;│  └─ Descent\_State

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Ring\_Connection\_Interface

&nbsp;&nbsp;&nbsp;│  ├─ Connection\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Source\_Ring\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Target\_Ring\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Port\_A\_Transform

&nbsp;&nbsp;&nbsp;│  ├─ Port\_B\_Transform

&nbsp;&nbsp;&nbsp;│  ├─ Bridge\_Root

&nbsp;&nbsp;&nbsp;│  ├─ Extend\_Value

&nbsp;&nbsp;&nbsp;│  ├─ Lock\_State

&nbsp;&nbsp;&nbsp;│  ├─ Seal\_State

&nbsp;&nbsp;&nbsp;│  └─ Connection\_State

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Shore\_Interface

&nbsp;&nbsp;&nbsp;│  ├─ Shore\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Petal\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Shore\_Root

&nbsp;&nbsp;&nbsp;│  ├─ Attach\_Point

&nbsp;&nbsp;&nbsp;│  ├─ Detach\_Transform

&nbsp;&nbsp;&nbsp;│  ├─ Dock\_Transform

&nbsp;&nbsp;&nbsp;│  ├─ Free\_Float\_State

&nbsp;&nbsp;&nbsp;│  ├─ Navigation\_Root

&nbsp;&nbsp;&nbsp;│  ├─ Stabilization\_State

&nbsp;&nbsp;&nbsp;│  └─ Connection\_State

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Root\_Interface

&nbsp;&nbsp;&nbsp;│  ├─ Root\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Root\_Root

&nbsp;&nbsp;&nbsp;│  ├─ Root\_Anchor

&nbsp;&nbsp;&nbsp;│  ├─ Root\_To\_Stem

&nbsp;&nbsp;&nbsp;│  ├─ Anchor\_State

&nbsp;&nbsp;&nbsp;│  └─ Root\_Transition\_State

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Socket\_Interface

&nbsp;&nbsp;&nbsp;│  ├─ Socket\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Socket\_Type

&nbsp;&nbsp;&nbsp;│  ├─ Parent\_Part\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Socket\_Transform

&nbsp;&nbsp;&nbsp;│  ├─ Socket\_State

&nbsp;&nbsp;&nbsp;│  └─ Connection\_Target\_ID

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Bone\_Mapping

&nbsp;&nbsp;&nbsp;│  ├─ Part\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Bone\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Bone\_Name

&nbsp;&nbsp;&nbsp;│  └─ Parent\_Bone\_ID

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Control\_Mapping

&nbsp;&nbsp;&nbsp;│  ├─ Control\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Target\_Part\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Control\_Type

&nbsp;&nbsp;&nbsp;│  └─ Control\_Value

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Pivot\_Mapping

&nbsp;&nbsp;&nbsp;│  ├─ Part\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Pivot\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Pivot\_Transform

&nbsp;&nbsp;&nbsp;│  └─ Pivot\_Space

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Socket\_Mapping

&nbsp;&nbsp;&nbsp;│  ├─ Socket\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Parent\_Part\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Target\_ID

&nbsp;&nbsp;&nbsp;│  └─ Connection\_Type

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Transform\_Space

&nbsp;&nbsp;&nbsp;│  ├─ World\_Space

&nbsp;&nbsp;&nbsp;│  ├─ Root\_Space

&nbsp;&nbsp;&nbsp;│  ├─ Parent\_Space

&nbsp;&nbsp;&nbsp;│  └─ Local\_Space

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Hierarchy\_Validation

&nbsp;&nbsp;&nbsp;│  ├─ Validate\_Parent\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Validate\_Pivot

&nbsp;&nbsp;&nbsp;│  ├─ Validate\_Root

&nbsp;&nbsp;&nbsp;│  ├─ Validate\_Socket

&nbsp;&nbsp;&nbsp;│  └─ Validate\_Movable\_Hierarchy

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;├─ FC\_Rig\_Export\_Validation

&nbsp;&nbsp;&nbsp;│  ├─ Missing\_ID

&nbsp;&nbsp;&nbsp;│  ├─ Missing\_Pivot

&nbsp;&nbsp;&nbsp;│  ├─ Missing\_Parent

&nbsp;&nbsp;&nbsp;│  ├─ Invalid\_Transform

&nbsp;&nbsp;&nbsp;│  ├─ Invalid\_Hierarchy

&nbsp;&nbsp;&nbsp;│  └─ Export\_Ready \[bool\]

&nbsp;&nbsp;&nbsp;│

&nbsp;&nbsp;&nbsp;└─ FC\_Rig\_Export\_Debug

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ Show\_Pivots

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ Show\_Roots

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ Show\_Sockets

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ Show\_Parent\_Links

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ Show\_Rig\_ID

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ Show\_Export\_Status

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

04\_SCIFI

├─ FC\_Pipe

├─ FC\_Cable

├─ FC\_Light

├─ FC\_Mechanical\_Detail

└─ FC\_Energy\_Element

&nbsp;

05\_PROPS

├─ FC\_Street\_Prop

├─ FC\_Sign

├─ FC\_Bench

└─ FC\_Utility

&nbsp;

06\_RIG

├─ FC\_Rig\_Pivot

├─ FC\_Rig\_MovablePart

├─ FC\_Rig\_Socket

├─ FC\_Rig\_BoneData

└─ FC\_Rig\_Debug

&nbsp;

07\_GAME\_READY

├─ FC\_Collision

├─ FC\_LOD

├─ FC\_Material\_ID

├─ FC\_UV\_Prep

├─ FC\_Instance\_Policy

└─ FC\_Export\_Prep

&nbsp;

08\_PRESENTATION

├─ FC\_Hero\_Setup

├─ FC\_Breakdown\_View

└─ FC\_Portfolio\_Debug

&nbsp;