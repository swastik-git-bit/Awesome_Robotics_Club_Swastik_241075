#Part A
This function calculates the joint angles (α, β, γ) of a 3DOF robotic leg given a 3D foot position (x, y, z) and the leg segment lengths (L1, L2, L3):
Steps:
Coxa Angle (α):
alpha = atan2(y, x)
This calculates the angle of rotation in the XY (horizontal) plane from the base to the foot.
Horizontal Distance:
horizontal_dist = hypot(x, y) gives the distance from the origin to the foot in the XY plane.
Planar Distances r and s:
r = horizontal_dist - L1: Subtracts the coxa length (L1) to get the horizontal offset from the femur joint.
s = z: The vertical (Z) component stays the same.
Effective Distance D:
D = hypot(r, s): Straight-line distance from femur joint to foot position.
Reachability Check:
If D > (L2 + L3), the point is unreachable — leg can’t stretch that far.
Femur Angle (β):
Uses law of cosines and angle math to compute β.
a = acos(...): Angle between femur and the line to foot.
b = atan2(s, r): Base angle from femur to foot in the plane.
beta = b + a
Tibia Angle (γ):
Another law of cosines: angle between femur and tibia.
Convert to Degrees:
All angles are converted from radians to degrees before returning.

Part B
This section tests the inverse_kinematics function with 5 predefined 3D target positions to verify correct behavior under different conditions:
 Test Cases:
 Test 1: A typical reachable point within the workspace.
 Test 2: A point very close to the base.
 Test 3: A point at the edge of the maximum reach (L1 + L2 + L3 = 30).
 Test 4: An unreachable point beyond max reach (40 units away).
 Test 5: A reachable point with a large negative Z (foot way below).
 What It Does:
Iterates through each test position.
Calls inverse_kinematics() for the given coordinates.
If reachable, prints the joint angles.
If unreachable, catches the ValueError and prints a clean error message.
