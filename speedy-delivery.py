#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_drive_smart = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
Claw_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
Neck_motor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ----------------------------------------------------------------------------
#                                                                            
#    Project:        
#    Description:    
#    Configuration:  V5 Clawbot or Advanced TrainingBot (Drivetrain 2-motor, No Gyro)
#                    Claw Motor in Port 3
#                    Arm Motor in Port 8          
#                                                                            
# ----------------------------------------------------------------------------

# Library imports
from vex import *
import urandom
import math


wait(2, SECONDS)


Neck_motor.set_max_torque(1000, PERCENT)


# CLAW SETUP
Claw_motor.spin(FORWARD)
Neck_motor.spin_for(FORWARD, 360, DEGREES)

# MOVEMENT

drivetrain.drive_for(FORWARD, 36, INCHES)
drivetrain.turn_for(LEFT, 90, DEGREES)

drivetrain.drive_for(FORWARD, 7, INCHES)


# CLAW PICKUP
wait(1, SECONDS)

Neck_motor.spin_for(REVERSE, 125,DEGREES)
wait(1, SECONDS)

Claw_motor.spin(REVERSE)
wait(1, SECONDS)

Neck_motor.spin_for(FORWARD, 125, DEGREES)
wait(1, SECONDS)


# REACH DELIVERY POINT

drivetrain.drive_for(REVERSE, 3, INCHES)
drivetrain.turn_for(RIGHT, 87, DEGREES)

drivetrain.drive_for(FORWARD, 45, INCHES)

drivetrain.turn_for(LEFT, 94, DEGREES)

drivetrain.drive_for(FORWARD, 67, INCHES)

#LEAVE BALL ON DESTINATION POINT

Neck_motor.spin_for(REVERSE, 125, DEGREES)
wait(2, SECONDS)
Claw_motor.spin(FORWARD)
wait(2, SECONDS)
Neck_motor.spin_for(FORWARD, 125, DEGREES)
wait(2, SECONDS)
Claw_motor.spin(REVERSE)

#RETURN TO PICKUP

drivetrain.drive_for(REVERSE, 65, INCHES)
drivetrain.turn_for(LEFT, 92, DEGREES)
drivetrain.drive_for(FORWARD, 45, INCHES)
drivetrain.turn_for(RIGHT, 90, DEGREES)
drivetrain.drive_for(FORWARD, 5, INCHES)
Claw_motor.spin(FORWARD)

#PICK UP 2
wait(1, SECONDS)

Neck_motor.spin_for(REVERSE, 125,DEGREES)
wait(1, SECONDS)

Claw_motor.spin(REVERSE)
wait(1, SECONDS)

Neck_motor.spin_for(FORWARD, 125, DEGREES)
wait(1, SECONDS)

drivetrain.drive_for(REVERSE, 3, INCHES)
drivetrain.turn_for(RIGHT, 90, DEGREES)

drivetrain.drive_for(FORWARD, 45, INCHES)

drivetrain.turn_for(LEFT, 90, DEGREES)

drivetrain.drive_for(FORWARD, 65, INCHES)

#LEAVE BALL ON DESTINATION POINT 2

Neck_motor.spin_for(REVERSE, 125, DEGREES)
wait(2, SECONDS)
Claw_motor.spin(FORWARD)
wait(2, SECONDS)
Neck_motor.spin_for(FORWARD, 125, DEGREES)
wait(2, SECONDS)
Claw_motor.spin(REVERSE)

#RETURN TO PICKUP 2

drivetrain.drive_for(REVERSE, 65, INCHES)
drivetrain.turn_for(LEFT, 90, DEGREES)
drivetrain.drive_for(FORWARD, 45, INCHES)
drivetrain.turn_for(RIGHT, 90, DEGREES)
drivetrain.drive_for(FORWARD, 3, INCHES)

#PICK UP 3
wait(1, SECONDS)

Neck_motor.spin_for(REVERSE, 125,DEGREES)
wait(1, SECONDS)

Claw_motor.spin(REVERSE)
wait(1, SECONDS)

Neck_motor.spin_for(FORWARD, 125, DEGREES)
wait(1, SECONDS)

drivetrain.drive_for(REVERSE, 3, INCHES)
drivetrain.turn_for(RIGHT, 90, DEGREES)

drivetrain.drive_for(FORWARD, 45, INCHES)

drivetrain.turn_for(LEFT, 90, DEGREES)

drivetrain.drive_for(FORWARD, 65, INCHES)

#LEAVE BALL ON DESTINATION POINT 3

Neck_motor.spin_for(REVERSE, 125, DEGREES)
wait(2, SECONDS)
Claw_motor.spin(FORWARD)
wait(2, SECONDS)
Neck_motor.spin_for(FORWARD, 125, DEGREES)
wait(2, SECONDS)
Claw_motor.spin(REVERSE)

#RETURN TO PICKUP 3

drivetrain.drive_for(REVERSE, 80, INCHES)
