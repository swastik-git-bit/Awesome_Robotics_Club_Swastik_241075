#Part_A
import math

def inverse_kinematics(x, y, z, L1, L2, L3):
   
    alpha = math.atan2(y, x)  

    horizontal_dist = math.hypot(x, y)
    
    r = horizontal_dist - L1
    s = z  
    
    D = math.hypot(r, s)

    if D > (L2 + L3):
        raise ValueError("Target is out of reach for the leg.")
    
    a = math.acos((L2**2 + D**2 - L3**2) / (2 * L2 * D))
    b = math.atan2(s, r)
    beta = b + a

    gamma = math.acos((L2**2 + L3**2 - D**2) / (2 * L2 * L3))

    alpha_deg = math.degrees(alpha)
    beta_deg = math.degrees(beta)
    gamma_deg = math.degrees(gamma)

    return alpha_deg, beta_deg, gamma_deg

#Part_B
import math

def inverse_kinematics(x, y, z, L1, L2, L3):
    
    alpha = math.atan2(y, x)

    horizontal_dist = math.hypot(x, y)

    r = horizontal_dist - L1
    s = z

    D = math.hypot(r, s)

    if D > (L2 + L3):
        raise ValueError("Unreachable: Target is beyond leg's reach.")

    a = math.acos((L2**2 + D**2 - L3**2) / (2 * L2 * D))
    b = math.atan2(s, r)
    beta = b + a

    gamma = math.acos((L2**2 + L3**2 - D**2) / (2 * L2 * L3))

    alpha_deg = math.degrees(alpha)
    beta_deg = math.degrees(beta)
    gamma_deg = math.degrees(gamma)

    return alpha_deg, beta_deg, gamma_deg


L1 = 5.0   
L2 = 10.0  
L3 = 15.0  

test_positions = [
    {"name": "Test 1 (Typical reachable)",         "coords": (15.0, 10.0, -5.0)},
    {"name": "Test 2 (Near base)",                 "coords": (2.0, 1.0, -1.0)},
    {"name": "Test 3 (Near max reach)",            "coords": (25.0, 0.0, 0.0)}, 
    {"name": "Test 4 (Unreachable point)",         "coords": (40.0, 0.0, 0.0)},  
    {"name": "Test 5 (Deep Z position)",           "coords": (10.0, 0.0, -20.0)},
]


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

