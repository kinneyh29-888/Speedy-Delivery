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
claw_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
arm_motor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)


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
55, 63, 70
#Set up
# Set up
Claw_motor.spin(FORWARD)
Neck_motor.spin_for(FORWARD, 230, DEGREES)
# Drive to pick up
drivetrain.drive_for(FORWARD, 55, INCHES)
drivetrain.turn_for(RIGHT, 90, DEGREES)
drivetrain.drivefor(FORWARD, 1, INCHES)
#Drop off
drivetrain.drive_for(REVERSE, 5, INCHES)
drivetrain.turn_for(LEFT, 90, DEGREES)
drivetrain.drive_for(FORWARD, 37, INCHES)
drivetrain.turn_for(LEFT, 90, DEGREES)
drivetrain.drive_for(FORWARD, 90, INCHES)
drivetrain.turn_for(LEFT, 90, DEGREES)
drivetrain.drive_for(FORWARD, 15, INCHES)
#Set up
Claw_motor.spin(REVERSE)
Neck_motor.spin_for(FORWARD, 150, DEGREES)


