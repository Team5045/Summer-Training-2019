from enum import IntEnum
from wpilib import DoubleSolenoid
import magicbot


#print statements for debugging
class SolenoidState(IntEnum):
    EXTENDED = 0
    RETRACTED = 1

class Manipulator:

    solenoid = DoubleSolenoid
    
    def setup(self):
        self.state = SolenoidState.RETRACTED

    def switch(self):
        if self.state == SolenoidState.EXTENDED:
            self.state = SolenoidState.RETRACTED
        elif self.state == SolenoidState.RETRACTED:
            self.state = SolenoidState.EXTENDED

    def extend(self):
        self.state = SolenoidState.EXTENDED
        #self.solenoid.set(1)
        #print("runningextend")


    def retract(self):
        self.state = SolenoidState.RETRACTED
        #self.solenoid.set()
        #print("runningretract")

    def get_state(self):
        return {
            'claw_state': self.state,
        }

    def put_state(self, state):
        self.state = state['claw_state']

    def execute(self):
        if self.state == SolenoidState.RETRACTED:
            self.solenoid.set(DoubleSolenoid.Value.kForward)
            #print("runningexecuteforward")
        elif self.state == SolenoidState.EXTENDED:
            self.solenoid.set(DoubleSolenoid.Value.kReverse)
            #print("runningexecutereverse")

