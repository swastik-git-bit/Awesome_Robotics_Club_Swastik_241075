part A:
Design Approach
The robot is a 3RPS parallel manipulator. This is essentially a 3DOF platform with 3 legs each having a rotational joint and a spherical joint. Extending or contracting each leg will result in the platform being angled in a different way. This is done by each stepper motor. My biggest considerations when designing the balancer was to have sleekness and simplicity. For sleekness, I ensured that the electronics and most of the wires were well hidden. For simplicity, I decided to use 3 motors (3DOF) rather than the 6 motors (6DOF) used in version 1. Weighing the cost-benefits, I also chose not to use position encoders with the stepper motors. Using encoders would only eliminate the need to have the machine start at a common position. Without them, you simply just have to push the platform down every time.

Electronics 

 digital servo (x6)
Teensy 4.1
6 channel Maestro servo controller
Pixy2 Camera
3.3 to 5v logic level converter
half proto board + screw terminal
SPST switch
18 AWG wire
XT60H connector pair
2S (7.4v) 6200mah lipo battery

#Stepper Motor Control – Key Points
Initial Problem
The ball-balancing bot experienced jittery motion during early testing.
Dynamic Speed & Acceleration Control:
The speed and acceleration of each stepper motor were made proportional to the distance between:
The motor's current position, an
Its target position.
This means:
Far from target → High speed and acceleration.
Close to target → Low speed and acceleration.
Result: Smoother transitions and reduced jitter.
Microstepping Upgrade:
Switched stepper drivers to 1/16th microstepping mode.
Instead of standard 200 steps/revolution, now using 3200 steps/revolution.
This results in:
Finer control of motor position.
Smoother and more precise motion.

Use of teensy:
 The teensy is the brain of the robot. All of the other electronic components are connected to the teensy. We will be programming the teensy using the Arduino IDE. If you have never used a teensy before, you will need to do one of two things to allow the Arduino software to support the teensy.
use of paolulu maestro:
The first thing we will need to do to the polulu maestro is to get it set up. You will need to download the maestro control center software to verify/change two settings. Once you have downloaded the software and connected the maestro, plug in one of the servos and move it around from the software to verify that the board works. Here is a good tutorial on how to get set up with the maestro.
The Camera:
The pixy2 camera is what we will use for object detection. Nothing on the pixy needs to be modified, but you will need to download Pixymon v2 in order to view the camera footage and set up an object to be detected. For now, all you need to do with the pixy is to plug it into your computer and ensure that it works by viewing the footage on Pixymon. I would also suggest testing the object recognition by setting up a random object to be detected.

![image](https://github.com/user-attachments/assets/d7e527ae-b786-4c30-8b7c-c5d743a2334a)
Benefits of Additional DOF
1. Improved Stability (Z-axis control or platform damping)
Adding Z-axis movement (vertical motion) or compliant mechanisms helps:
Absorb sudden forces (like ball drops or impacts).
Minimize vibrations from motors or environmental sources.
Stabilize the platform like a suspension system.
2. Enhanced Responsiveness (Faster reaction times)
Extra DOF (e.g., using a Stewart platform or extra actuators) enables:
Faster direction changes by shifting the platform more efficiently.
Simultaneous control of multiple motion axes for agile corrections.
Preemptive shaping of platform motion based on ball trajectory prediction.
3. Higher Control Precision
More actuators or finer microstepping (like in the video) allow:
Sub-millimeter movement resolution.
Smooth transitions in tilt and rotation angles.
Less overshoot and more accurate PID or model-based control.
4. Compensation for External Disturbances
With more DOF, the system can:
React to wind, uneven weight distribution, or moving bases.
Maintain control even if one actuator underperforms or lags.
Distribute load more evenly, improving balance during rapid shifts.
5. Advanced Control Tasks
Extra DOF opens doors for:
Ball trajectory control (e.g., follow a path or play a game).
Platform yaw rotation, to steer the ball with spin.
Research in nonlinear or predictive control systems.

Screenshot of the 3D model: ![image](https://github.com/user-attachments/assets/cdb4b2d1-174b-4117-8a66-eea6893c4e48)
Pros and Cons

Aspect                               	Pros	                                                               Cons
Performance	      Ultra-precise control in all 6 DOF; fast response; adaptive	             Might be overkill for simple balancing task
Stability       	High stability due to multi-axis corrections	                           Requires complex control algorithms (e.g., inverse kinematics)
Reliability	      Redundant actuators can provide backup	                                 More points of failure due to actuator count
Complexity	      Can run advanced experiments, simulate terrain, handle disturbances	     Mechanically and electronically complex
Cost	            Great for research, teaching, or demo purposes	                         Expensive: actuators, controller, power supply

Part B:
Method 1: Capacitive Touch Sensor Grid (2D Touch Surface)
1. Sensor Selection
Sensor Type: Capacitive touch sensor matrix/grid
Example: Mutual-capacitance 2D touch grid using ITO (Indium Tin Oxide) film or Flex PCB with intersecting electrodes.

KeySpecs:
High spatial resolution (e.g., 1 mm or better)
Fast sampling rate (≥100 Hz)
Multitouch support (if extended)

3. Tracking Mechanism
A conductive or semi-conductive ball (like coated with a conductive layer or containing a metal core) will alter the local capacitance where it touches or is close to the surface.
The grid detects the X-Y coordinates of the ball’s position in real time by identifying which row and column exhibit a capacitance change.
Algorithms smooth out the noisy readings to get continuous position tracking.

5. Pros and Cons
Aspect	                                     Pros	                                                                Cons
Accuracy	                High (sub-mm precision possible with fine grids)	              Sensitive to interference and requires a conductive ball
Latency	                  Low latency (<10 ms typical)	                                  Sampling rate might need optimization for fast ball movement
Cost	                    Moderate; depends on grid size and electronics	                Higher than simple sensors, but cheaper than high-end vision
Complexity	              Medium; needs signal processing, shielding from noise	          PCB layout and calibration can be tricky

Method 2: Infrared (IR) Distance Sensor Array Under Platform
1. Sensor Selection
Sensor Type: Infrared proximity/distance sensors (e.g., VL53L0X, GP2Y0A21YK0F)
Arrangement: Array of sensors mounted beneath a semi-transparent or mesh platform, looking up.
Specs:
Range: 2–30 cm
Update rate: ≥50 Hz
Narrow beam angle (for better resolution)
2. Tracking Mechanism
The ball interrupts or reflects IR light depending on the sensor type:
If using Time-of-Flight (ToF) sensors, they detect changes in height when the ball passes over.
By triagulating distances from multiple sensors, the 2D position of the ball can be inferred.
Interpolation techniques improve position resolution between sensors.
3. Pros and Cons
Aspect	                       Pros                                                            	Cons
Accuracy	        Moderate (~1–5 mm with interpolation)         	             Depends on sensor density and surface reflectivity
Latency         	Moderate; low-latency but needs interpolation	                Slight delay from sensor polling and fusion
Cost	            Moderate to high (more sensors = better coverage)            	Cost scales with desired resolution
Complexity	      Higher; requires sensor fusion, calibration, and filtering	  Beam overlap and cross-talk must be managed



