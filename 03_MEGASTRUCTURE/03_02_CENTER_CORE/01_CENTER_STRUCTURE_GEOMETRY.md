# 03.02.01 - Center Structure, Cone & Restrictions

## Purpose & PCG Implementation
นิยามรูปทรงเรขาคณิตหลักของแกนกลางเมือง (`FC_Flower_Center`), โคนศูนย์กลาง (`FC_Flower_Cone`), โครงสร้างรับแรงหลัก (`FC_Center_Structure`), จุดเชื่อมต่อกลีบ (`FC_Center_Petal_Interface`), การกระจายกลีบ (`FC_Center_Petal_Distribution`), ระยะปลอดภัย (`FC_Center_Petal_Clearance`), และข้อจำกัดความสูง/โซนห้ามสร้างอาคาร (`FC_Center_Building_Restriction`)

---

## Parameter Tree

```text
├─ 03.02_FLOWER_CENTER

│  │

│  ├─ FC_Flower_Center

│  │  ├─ Center_ID

│  │  ├─ Center_Radius

│  │  ├─ Center_Height

│  │  ├─ Center_Transform

│  │  ├─ Center_Top_Height

│  │  ├─ Center_Base_Height

│  │  ├─ Center_Clearance

│  │  ├─ Center_Profile

│  │  ├─ Center_Thickness

│  │  ├─ Center_Floor_Count \[int\]

│  │  ├─ Center_Floor_Height

│  │  ├─ Center_Core_Radius

│  │  ├─ Center_Inner_Radius

│  │  ├─ Center_Outer_Radius

│  │  ├─ Center_Orientation

│  │  ├─ Center_Surface_Normal

│  │  ├─ Center_Load_Class

│  │  ├─ Center_State

│  │  └─ Center_Enabled \[bool\]

│  │

│  ├─ FC_Flower_Cone

│  │  ├─ Cone_ID

│  │  ├─ Cone_Radius

│  │  ├─ Cone_Base_Radius

│  │  ├─ Cone_Top_Radius

│  │  ├─ Cone_Height

│  │  ├─ Cone_Profile

│  │  ├─ Cone_Taper

│  │  ├─ Cone_Thickness

│  │  ├─ Cone_Base_Height

│  │  ├─ Cone_Top_Height

│  │  ├─ Cone_Transform

│  │  ├─ Cone_Orientation

│  │  ├─ Cone_Surface_Normal

│  │  ├─ Cone_Inner_Clearance

│  │  ├─ Cone_Outer_Clearance

│  │  ├─ Cone_Top_Clearance

│  │  ├─ Cone_Petal_Clearance

│  │  ├─ Cone_Building_Clearance

│  │  ├─ Cone_Load_Class

│  │  ├─ Cone_State

│  │  └─ Cone_Enabled \[bool\]

│  │

│  ├─ FC_Center_Structure

│  │  ├─ Structural_Core

│  │  ├─ Structural_Ring

│  │  ├─ Upper_Support

│  │  ├─ Lower_Support

│  │  ├─ Load_Transfer_Point

│  │  ├─ Core_Radius

│  │  ├─ Core_Thickness

│  │  ├─ Ring_Count \[int\]

│  │  ├─ Ring_Radius

│  │  ├─ Ring_Thickness

│  │  ├─ Support_Count \[int\]

│  │  ├─ Support_Spacing

│  │  ├─ Support_Angle

│  │  ├─ Radial_Support

│  │  ├─ Vertical_Support

│  │  ├─ Petal_Load_Input

│  │  ├─ Center_Load_Input

│  │  ├─ Stem_Load_Output

│  │  ├─ Load_Distribution

│  │  ├─ Load_Balance

│  │  ├─ Structural_Clearance

│  │  ├─ Structural_State

│  │  └─ Structural_Enabled \[bool\]

│  │

│  ├─ FC_Center_Petal_Interface

│  │  ├─ Petal_ID

│  │  ├─ Petal_Attach_Point

│  │  ├─ Petal_Attach_Transform

│  │  ├─ Petal_Inner_Pivot

│  │  ├─ Petal_Left_Rig_Attach

│  │  ├─ Petal_Right_Rig_Attach

│  │  ├─ Petal_Rest_Transform

│  │  ├─ Petal_Open_Transform

│  │  ├─ Petal_Closed_Transform

│  │  ├─ Petal_Current_Transform

│  │  ├─ Petal_Local_Space

│  │  ├─ Petal_Rotation_Axis

│  │  ├─ Petal_Rotation_Limit

│  │  ├─ Petal_Raise_Limit

│  │  ├─ Petal_Lower_Limit

│  │  ├─ Petal_Twist_Limit

│  │  ├─ Petal_Clearance

│  │  ├─ Petal_Center_Clearance

│  │  ├─ Petal_Neighbor_Clearance

│  │  ├─ Petal_Rig_Clearance

│  │  ├─ Petal_Load_Interface

│  │  ├─ Petal_Utility_Interface

│  │  ├─ Petal_Transport_Interface

│  │  ├─ Petal_State

│  │  ├─ Petal_Connection_State

│  │  └─ Petal_Interface_Enabled \[bool\]

│  │

│  ├─ FC_Center_Petal_Distribution

│  │  ├─ Petal_Count \[int\]

│  │  ├─ Petal_Index \[int\]

│  │  ├─ Petal_ID

│  │  ├─ Radial_Angle

│  │  ├─ Angular_Spacing

│  │  ├─ Rotation_Offset

│  │  ├─ Distribution_Radius

│  │  ├─ Distribution_Center

│  │  ├─ Distribution_Axis

│  │  ├─ Start_Angle

│  │  ├─ End_Angle

│  │  ├─ Closed_Loop \[bool\]

│  │  ├─ Petal_Radial_Position

│  │  ├─ Petal_Radial_Direction

│  │  ├─ Petal_Tangent_Direction

│  │  ├─ Petal_Local_Transform

│  │  ├─ Petal_World_Transform

│  │  ├─ Petal_Rotation

│  │  ├─ Petal_Scale

│  │  ├─ Petal_Spacing_Override

│  │  ├─ Petal_Rotation_Override

│  │  ├─ Petal_Radius_Override

│  │  ├─ Neighbor_Left_ID

│  │  ├─ Neighbor_Right_ID

│  │  ├─ Neighbor_Angle

│  │  ├─ Neighbor_Clearance

│  │  ├─ Distribution_Clearance

│  │  ├─ Distribution_State

│  │  └─ Distribution_Enabled \[bool\]

│  │

│  ├─ FC_Center_Petal_Clearance

│  │  ├─ Inner_Clearance

│  │  ├─ Closed_State_Clearance

│  │  ├─ Rig_Clearance

│  │  ├─ Building_Clearance

│  │  ├─ Center_Collision_Limit

│  │  ├─ Petal_Inner_Clearance

│  │  ├─ Petal_Left_Clearance

│  │  ├─ Petal_Right_Clearance

│  │  ├─ Petal_Top_Clearance

│  │  ├─ Petal_Bottom_Clearance

│  │  ├─ Neighbor_Petal_Clearance

│  │  ├─ Petal_Rotation_Clearance

│  │  ├─ Petal_Raise_Clearance

│  │  ├─ Petal_Lower_Clearance

│  │  ├─ Petal_Twist_Clearance

│  │  ├─ Rig_Left_Clearance

│  │  ├─ Rig_Right_Clearance

│  │  ├─ Rig_Motion_Clearance

│  │  ├─ Building_Open_State_Clearance

│  │  ├─ Building_Closed_State_Clearance

│  │  ├─ Building_Roof_Clearance

│  │  ├─ Center_Cone_Clearance

│  │  ├─ Center_Structure_Clearance

│  │  ├─ Transport_Interface_Clearance

│  │  ├─ Utility_Interface_Clearance

│  │  ├─ Open_State_Envelope

│  │  ├─ Closed_State_Envelope

│  │  ├─ Transition_Envelope

│  │  ├─ Collision_Margin

│  │  ├─ Safety_Margin

│  │  ├─ Clearance_Valid \[bool\]

│  │  └─ Clearance_Debug

│  │

│  ├─ FC_Center_Building_Restriction

│  │  ├─ Restricted_Radius

│  │  ├─ Restriction_Zone_ID

│  │  ├─ Distance_From_Center

│  │  ├─ Distance_From_Cone

│  │  ├─ Max_Building_Height

│  │  ├─ Min_Building_Height

│  │  ├─ Max_Building_Floors \[int\]

│  │  ├─ Min_Building_Floors \[int\]

│  │  ├─ Max_Roof_Height

│  │  ├─ Flat_Roof_Required \[bool\]

│  │  ├─ Roof_Profile_Restriction

│  │  ├─ Building_Orientation_Mode

│  │  ├─ Follow_Petal_Surface \[bool\]

│  │  ├─ Upside_Down_Allowed \[bool\]

│  │  ├─ Petal_Close_Clearance

│  │  ├─ Petal_Transition_Clearance

│  │  ├─ Center_Cone_Clearance

│  │  ├─ Center_Structure_Clearance

│  │  ├─ Neighbor_Building_Clearance

│  │  ├─ Rig_Motion_Clearance

│  │  ├─ Protection_Pylon_Clearance

│  │  ├─ Transport_Clearance

│  │  ├─ Emergency_Access_Clearance

│  │  ├─ Mass_Class_Limit

│  │  ├─ Load_Budget

│  │  ├─ Public_Space_Required \[bool\]

│  │  ├─ Build_Density_Limit

│  │  ├─ Buildable_Open_State \[bool\]

│  │  ├─ Buildable_Closed_State \[bool\]

│  │  ├─ Buildable_Transition_State \[bool\]

│  │  ├─ Buildable \[bool\]

│  │  └─ Restriction_Debug

│  │
```
