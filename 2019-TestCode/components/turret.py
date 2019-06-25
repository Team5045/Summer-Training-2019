import math
from magicbot import tunable
from ctre import WPI_TalonSRX
from enum import IntEnum
from constants import TALON_TIMEOUT

class Turret:
    USE_MOTIONMAGIC = True

    turretMotor = WPI_TalonSRX
    
    kFreeSpeed = tunable(0.3)
    kZeroingSpeed = tunable(0.1)
    kP = tunable(0.3)
    kI = tunable(0.0)
    kD = tunable(0.0)
    kF = tunable(0.0)

    kCruiseVelocity = 30000
    kAcceleration = 12000

    setpoint = tunable(0)
    value = tunable(0)
    error = tunable(0)

    def setup(self):
        self.pending_position = None
        self.pending_drive = None
        self._temp_hold = None

        #self.has_zeroed = True
        self.has_zeroed = False
        self.needs_brake = False
        self.braking_direction = None

        self.index = 0

        self.turretMotor.setInverted(False)
        self.turretMotor.configSelectedFeedbackSensor(
            WPI_TalonSRX.FeedbackDevice.CTRE_MagEncoder_Relative, 0, 0)
        self.turretMotor.selectProfileSlot(0, 0)
        self.turretMotor.setSensorPhase(True)

        self.turretMotor.config_kP(0, self.kP, 0)
        self.turretMotor.config_kI(0, self.kI, 0)
        self.turretMotor.config_kD(0, self.kD, 0)
        self.turretMotor.config_kF(0, self.kF, 0)

        self.turretMotor.configPeakOutputReverse(-0.1, TALON_TIMEOUT)

        try:
            self.turretMotor.configMotionCruiseVelocity(self.kCruiseVelocity, 0)
            self.turretMotor.configMotionAcceleration(self.kAcceleration, 0)
        except NotImplementedError:
            # Simulator - no motion profiling support
            self.USE_MOTIONMAGIC = False


    def is_encoder_connected(self):
        return self.turretMotor.getPulseWidthRiseToRiseUs() != 0

    def get_encoder_position(self):
        return self.turretMotor.getSelectedSensorPosition(0)

    def move_to(self, amount):
        '''
        Move `amount` inches.
        '''
        self.pending_position = amount

    def raise_freely(self):
        self.pending_drive = self.kFreeSpeed

    def lower_freely(self):
        self.pending_drive = -self.kFreeSpeed

    def move_incremental_right(self,x):
        x=x*500
        self.move_to(self.setpoint+x)
    
    def move_incremental_left(self,x):
        x=x*100
        self.move_to(self.setpoint-x)

    def execute(self):
        # For debugging
        #print('elevator', 'drive', self.pending_drive, 'lim', self.reverse_limit.get(),
        #      'pending_pos', self.pending_position,
        #      'setpoint', self.setpoint,
        #      'val', self.value,
        #      'err', self.error,
        #      'curr_pos', self.turretMotor.getQuadraturePosition(),
        #      'curr_velo', self.turretMotor.getQuadratureVelocity())

        # Brake - apply the brake either when we reach peak of movement
        # (for upwards motion), and thus ds/dt = v = 0, or else immediately
        # if we're traveling downwards (since no e.z. way to sense gravity vs
        # intertial movement).
        if self.needs_brake:
            if self.pending_drive:
                self.needs_brake = False
            else:
                velocity = self.turretMotor.getQuadratureVelocity()
                if velocity == 0 or \
                        self.braking_direction == -1 or \
                        velocity / abs(velocity) != self.braking_direction:
                    self.pending_position = self.turretMotor.getQuadraturePosition()
                    self.needs_brake = False
                    self.braking_direction = None

        # Elevator turretMotor
        if self.pending_drive:
            self.turretMotor.set(WPI_TalonSRX.ControlMode.PercentOutput,
                           self.pending_drive)
            self.pending_drive = None
            self.pending_position = None  # Clear old pending position
            self._temp_hold = None

        # Update dashboard PID values
        if self.pending_position:
            try:
                self.setpoint = self.turretMotor.getClosedLoopTarget(0)
                self.value = self.turretMotor.getSelectedSensorPosition(0)
                self.error = self.turretMotor.getClosedLoopError(0)
            except NotImplementedError:
                # Simulator doesn't implement getError
                pass

    def get_state(self):
        return {
            'pending_position': self.pending_position
        }

    def put_state(self, state):
        self.pending_position = state['pending_position']