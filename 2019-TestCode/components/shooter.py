from ctre import WPI_TalonSRX
from magicbot import tunable
from enum import IntEnum
from constants import TALON_TIMEOUT

### prints for debugging
class ShooterSpeed(IntEnum):
    OFF = 0
    SLOW = 1
    FAST = 2

class HopperState(IntEnum):
    OFF = 0
    ON = 1

class Shooter:

    shooterMotor = WPI_TalonSRX
    hopperMotor = WPI_TalonSRX

    def setup(self):
        self.shooter_speed = ShooterSpeed.OFF
        self.hopper_state = HopperState.OFF

    def run_shooter_off(self):
        self.shooter_speed = ShooterSpeed.OFF
        #print("off1")
    def run_shooter_slow(self):
        self.shooter_speed = ShooterSpeed.SLOW
        #print("slow1")
    def run_shooter_fast(self):
        self.shooter_speed = ShooterSpeed.FAST  
        #print("fast1")      

    def hopper_on(self):
        self.hopper_state = HopperState.ON
        #print('hopperon1')
    def hopper_off(self):
        self.hopper_state = HopperState.OFF
        #print('hopperoff1')

    def execute(self):
        if self.shooter_speed == ShooterSpeed.OFF:
            self.shooterMotor.set(0)
            #print("off")
        elif self.shooter_speed == ShooterSpeed.SLOW:
            self.shooterMotor.set(0.5)
            #print("slow")
        elif self.shooter_speed == ShooterSpeed.FAST:
            self.shooterMotor.set(0.9)
            #print("fast")

        if self.hopper_state == HopperState.OFF:
            self.hopperMotor.set(0)
            #print('hopperoff')
        elif self.hopper_state == HopperState.ON:
            self.hopperMotor.set(0.5)
            #print('hopperon')