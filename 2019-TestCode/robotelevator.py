import wpilib
import ctre
from components import manipulator, encodermotor
import magicbot

CONTROLLER_LEFT = wpilib.XboxController.Hand.kLeft
CONTROLLER_RIGHT = wpilib.XboxController.Hand.kRight


class SpartaBot(magicbot.MagicRobot):

    manipulator = manipulator.Manipulator
    encodermotor = encodermotor.EncoderMotor

    def robotInit(self):
        self.controller = wpilib.XboxController(0)

        self.motor_one = ctre.WPI_TalonSRX(5)
        self.motor_two = ctre.WPI_TalonSRX(1) #use this motor for encoder (motor_two)

        self.compressor = wpilib.Compressor()
        self.manipulator_one = wpilib.DoubleSolenoid(0, 2)
        


    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass    
        self.motor_test.set(0.1)
    
    def teleopPeriodic(self):
        #drivetrain
        self.motor_two.set(self.controller.getY(CONTROLLER_LEFT))
        self.motor_one.set(self.controller.getY(CONTROLLER_RIGHT))

        if self.controller.getBumperReleased(CONTROLLER_LEFT):
            self.manipulator.switch()

        if self.controller.getXButtonReleased():
            self.encodermotor.toggle()
        
        if self.controller.getYButtonReleased():
            self.encodermotor.move_incremental(80)

if __name__ == "__main__":
    wpilib.run(SpartaBot)
    