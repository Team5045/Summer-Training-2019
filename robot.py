import wpilib
import ctre
import magicbot
from components import manipulator, encodermotor, turret, shooter

CONTROLLER_LEFT = wpilib.XboxController.Hand.kLeft
CONTROLLER_RIGHT = wpilib.XboxController.Hand.kRight


class SpartaBot(magicbot.MagicRobot):

    manipulator = manipulator.Manipulator
    encodermotor = encodermotor.EncoderMotor
    turret = turret.Turret
    shooter = shooter.Shooter

    def createObjects(self):
        self.controller = wpilib.XboxController(0)

        self.motor_one = ctre.WPI_TalonSRX(1)

        self.encodermotor_motor = ctre.WPI_TalonSRX(5)

        self.compressor = wpilib.Compressor()
        self.manipulator_solenoid = wpilib.DoubleSolenoid(1, 3)

        self.turret_turretMotor = ctre.WPI_TalonSRX(2)

        self.shooter_shooterMotor = ctre.WPI_TalonSRX(3)
        self.shooter_hopperMotor = ctre.WPI_TalonSRX(4)
        
    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass    
        #self.motor_test.set(0.1)
    
    def teleopPeriodic(self):
        #one motor on right stick (axis 5)
        self.motor_one.set(self.controller.getY(CONTROLLER_RIGHT))

        #one double solenoid
        if self.controller.getBumperReleased(CONTROLLER_LEFT):
            self.manipulator.switch()

        #turret encoder
        '''if self.controller.getX(CONTROLLER_LEFT)>0.05:
            self.turret.move_incremental_right(self.controller.getX(CONTROLLER_LEFT))
        elif self.controller.getX(CONTROLLER_LEFT)<0.05:
            self.turret.move_incremental_left(self.controller.getX(CONTROLLER_LEFT))'''

        #turret from left stick x axis (X)
        self.turret_turretMotor.set(0.3*self.controller.getX(CONTROLLER_LEFT))

        #trigger axis is Z in simulator
        #ball shooter and hopper
        if self.controller.getTriggerAxis(CONTROLLER_LEFT)>0.75:
            #self.shooter_shooterMotor.set(0.9)
            self.shooter.run_shooter_fast()
            self.shooter.hopper_on()
        elif self.controller.getTriggerAxis(CONTROLLER_LEFT)>0.25:
            self.shooter.run_shooter_slow() 
            self.shooter.hopper_on()
        else:
            self.shooter.run_shooter_off()
            self.shooter.hopper_off()

        #single motor on encoder
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
    