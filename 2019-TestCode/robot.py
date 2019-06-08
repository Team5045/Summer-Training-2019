import wpilib
import ctre
import magicbot
from components import manipulator, encodermotor

CONTROLLER_LEFT = wpilib.XboxController.Hand.kLeft
CONTROLLER_RIGHT = wpilib.XboxController.Hand.kRight


class SpartaBot(magicbot.MagicRobot):

    manipulator = manipulator.Manipulator
    encodermotor = encodermotor.EncoderMotor

    def createObjects(self):
        self.controller = wpilib.XboxController(0)

        self.motor_one = ctre.WPI_TalonSRX(1)
        self.encodermotor_motor = ctre.WPI_TalonSRX(5)

        self.compressor = wpilib.Compressor()
        self.manipulator_solenoid = wpilib.DoubleSolenoid(1, 3)
        


    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass    
        self.motor_test.set(0.1)
    
    def teleopPeriodic(self):
        #drivetrain
        self.motor_one.set(self.controller.getY(CONTROLLER_RIGHT))

        if self.controller.getBumperReleased(CONTROLLER_LEFT):
            self.manipulator.switch()
        
        if self.controller.getYButtonReleased():
            self.encodermotor.move_incremental(1000)

        if self.controller.getBButtonReleased():
            self.encodermotor.true_toggle(True)

        if self.controller.getAButtonReleased():
            self.encodermotor.true_toggle(False)

        if self.controller.getXButtonReleased():
            self.encodermotor.toggle()
            

if __name__ == "__main__":
    wpilib.run(SpartaBot)
    