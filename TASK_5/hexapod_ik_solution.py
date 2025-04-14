#Part_A
import math

def inverse_kinematics(x, y, z, L1, L2, L3):
    """
    Computes the joint angles (alpha, beta, gamma) for a 3DOF robotic leg.
    Parameters:

        x, y, z : float
            Target foot position in 3D space (relative to coxa base)
        L1 : float
            Length of coxa
        L2 : float
            Length of femur
        L3 : float
            Length of tibia

    Returns:
        (alpha, beta, gamma) in degrees
    """
    # Angle alpha (coxa) in horizontal plane
    alpha = math.atan2(y, x)  # Radians

    # Projected distance from coxa to foot in horizontal plane
    horizontal_dist = math.hypot(x, y)
    
    #Planar distance from femur joint to foot
    r = horizontal_dist - L1
    s = z  # As Vertical component remains the same
    
    # Distance from femur joint to foot position (hypotenuse)
    D = math.hypot(r, s)

    # Check reachability
    if D > (L2 + L3):
        raise ValueError("Target is out of reach for the leg.")
    
    # Law of cosines for angle at femur (beta)
    a = math.acos((L2**2 + D**2 - L3**2) / (2 * L2 * D))
    b = math.atan2(s, r)
    beta = b + a

    # Law of cosines for angle at tibia (gamma)
    gamma = math.acos((L2**2 + L3**2 - D**2) / (2 * L2 * L3))

    # Convert radians to degrees
    alpha_deg = math.degrees(alpha)
    beta_deg = math.degrees(beta)
    gamma_deg = math.degrees(gamma)

    return alpha_deg, beta_deg, gamma_deg

#Part_B
import math

def inverse_kinematics(x, y, z, L1, L2, L3):
    """
    Computes the joint angles (alpha, beta, gamma) for a 3DOF robotic leg.
    Returns angles in degrees.
    """
    # Angle alpha (coxa) in horizontal plane
    alpha = math.atan2(y, x)

    # Projected distance from coxa to foot in horizontal plane
    horizontal_dist = math.hypot(x, y)

    # Effective planar distance from femur joint to foot
    r = horizontal_dist - L1
    s = z

    # Distance from femur joint to foot position
    D = math.hypot(r, s)

    # Check reachability
    if D > (L2 + L3):
        raise ValueError("Unreachable: Target is beyond leg's reach.")

    # Law of cosines
    a = math.acos((L2**2 + D**2 - L3**2) / (2 * L2 * D))
    b = math.atan2(s, r)
    beta = b + a

    gamma = math.acos((L2**2 + L3**2 - D**2) / (2 * L2 * L3))

    # Convert to degrees
    alpha_deg = math.degrees(alpha)
    beta_deg = math.degrees(beta)
    gamma_deg = math.degrees(gamma)

    return alpha_deg, beta_deg, gamma_deg


# Link lengths
L1 = 5.0   # Coxa
L2 = 10.0  # Femur
L3 = 15.0  # Tibia

# Test cases
test_positions = [
    {"name": "Test 1 (Typical reachable)",         "coords": (15.0, 10.0, -5.0)},
    {"name": "Test 2 (Near base)",                 "coords": (2.0, 1.0, -1.0)},
    {"name": "Test 3 (Near max reach)",            "coords": (25.0, 0.0, 0.0)},  # L1+L2+L3 = 30, total reach
    {"name": "Test 4 (Unreachable point)",         "coords": (40.0, 0.0, 0.0)},  # Out of reach
    {"name": "Test 5 (Deep Z position)",           "coords": (10.0, 0.0, -20.0)},
]

# Run tests
for test in test_positions:
    name = test["name"]
    x, y, z = test["coords"]
    print(f"\n{name}")
    print(f"Target Coordinates: x={x}, y={y}, z={z}")
    try:
        alpha, beta, gamma = inverse_kinematics(x, y, z, L1, L2, L3)
        print(f"Joint Angles: α = {alpha:.2f}°, β = {beta:.2f}°, γ = {gamma:.2f}°")
        print("Status: Reachable")
    except ValueError as e:
        print("Status: Unreachable -", e)

