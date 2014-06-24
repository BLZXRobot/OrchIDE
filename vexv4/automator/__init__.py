__author__ = 'james'

# void Arcade2(unsigned char ucJoystick,
# unsigned char ucMoveChannel, unsigned char ucRotateChannel,
# unsigned char ucLeftMotor, unsigned char ucRightMotor,
#              unsigned char ucLeftInvert, unsigned char ucRightInvert);
# void Arcade4(unsigned char ucJoystick,
#              unsigned char ucMoveChannel, unsigned char ucRotateChannel,
#              unsigned char ucLeftfrontMotor, unsigned char ucRightfrontMotor,
#              unsigned char ucLeftrearMotor, unsigned char ucRightrearMotor,
#              unsigned char ucLeftfrontInvert, unsigned char ucRightfrontInvert,
#              unsigned char ucLeftrearInvert, unsigned char ucRightrearInvert);
# void Tank2(unsigned char ucJoystick,
#            unsigned char ucLeftChannel, unsigned char ucRightChannel,
#            unsigned char ucLeftMotor, unsigned char ucRightMotor,
#            unsigned char ucLeftInvert, unsigned char ucRightInvert);
# void Tank4(unsigned char ucJoystick,
#            unsigned char ucLeftChannel, unsigned char ucRightChannel,
#            unsigned char ucLeftfrontMotor, unsigned char ucRightfrontMotor,
#            unsigned char ucLeftrearMotor, unsigned char ucRightrearMotor,
#            unsigned char ucLeftfrontInvert, unsigned char ucRightfrontInvert,
#            unsigned char ucLeftrearInvert, unsigned char ucRightrearInvert);
# void Holonomic(unsigned char ucJoystick,
#                unsigned char ucMoveChannel1, unsigned char ucMoveChannel2, unsigned char ucRotateChannel,
#                unsigned char ucLeftfrontMotor, unsigned char ucRightfrontMotor,
#                unsigned char ucLeftrearMotor, unsigned char ucRightrearMotor,
#                unsigned char ucLeftfrontInvert, unsigned char ucRightfrontInvert,
#                unsigned char ucLeftrearInvert, unsigned char ucRightrearInvert);
# void JoystickToMotor(unsigned char ucJoystick, unsigned char ucChannel, unsigned char ucMotor, unsigned char ucInv);
# void JoystickToMotorAndLimit(unsigned char ucJoystick, unsigned char ucChannel, unsigned char ucMotor, unsigned char ucInv, unsigned char ucPositiveLimitSwitch, unsigned char ucNegativeLimitSwitch);
# void JoystickToServo(unsigned char ucJoystick, unsigned char ucChannel, unsigned char ucMotor, unsigned char ucInv);
# void JoystickDigitalToMotor(unsigned char ucJoystick, unsigned char ucChannel, unsigned char ucFirstButton, int nFirstButtonValue, unsigned char ucSecondButton, int nSecondButtonValue, unsigned char ucMotor);
# void JoystickDigitalToServo(unsigned char ucJoystick, unsigned char ucChannel, unsigned char ucFirstButton, int nFirstButtonValue, unsigned char ucSecondButton, int nSecondButtonValue, unsigned char ucMotor);
# void JoystickDigitalToMotorAndLimit(unsigned char ucJoystick, unsigned char ucChannel, unsigned char ucFirstButton, int nFirstButtonValue, unsigned char ucFirstLimitSwitch, unsigned char ucSecondButton, int nSecondButtonValue, unsigned char ucSecondLimitSwitch, unsigned char ucMotor);
# void JoystickToDigitalOutput(unsigned char ucJoystick, unsigned char ucChannel, unsigned char ucButton, unsigned char ucDout);
# void JoystickToDigitalLatch(unsigned char ucJoystick, unsigned char ucChannel, unsigned char ucButton, unsigned char ucDout);


# //---- SMART TASKS / WAIT UNTIL ----------------------------------------------------------
# void WaitUntilDigitalInput(unsigned char ucPort, unsigned char ucValue);
# void WaitUntilAnalogInput(unsigned char ucPort, unsigned int uiMin, unsigned int uiMax, unsigned char ucConditionType);
# void WaitUntilAnalogInputHR(unsigned char ucPort, unsigned int uiMin, unsigned int uiMax, unsigned char ucConditionType);
# void WaitUntilEncoder(unsigned char ucPort, long lPresetValue, long lMin, long lMax, unsigned char ucConditionType);
# void WaitUntilQuadEncoder(unsigned char channelA, unsigned char channelB, long lPresetValue, long lMin, long lMax, unsigned char ucConditionType);
# void WaitUntilUltrasonic(unsigned char ucEcho, unsigned char ucPing, unsigned char ucMin, unsigned char ucMax, unsigned char ucConditionType);
# void WaitUntilAccelerometer(unsigned char ucPort, int nMin, int nMax, unsigned char ucConditionType);
# void WaitUntilGyro(unsigned char ucPort, unsigned int uiType, char cDeadband, int nMin, int nMax, unsigned char ucConditionType);
# void WaitUntilIntegratedMotorEncoder(unsigned char ucMotor, long lPresetValue, long lMin, long lMax, unsigned char ucConditionType);
# void WaitUntilIntegratedMotorEncoderSpeed(unsigned char ucMotor, float fMin, float fMax, unsigned char ucConditionType);
#
# //---- SMART TASKS / MOTOR MODULE ----------------------------------------------------------
# void MotorTimeControl(unsigned char ucMotor, int nPower, long lTime);
# void MultiMotorTimeControl(unsigned char ucNumMotors, unsigned char ucMotor1, unsigned char ucMotor2, unsigned char ucMotor3, unsigned char ucMotor4, unsigned char ucInvert1, unsigned char ucInvert2 , unsigned char ucInvert3 , unsigned char ucInvert4 , int nPower, long lTime);
# void SmartMotorDegrees(unsigned char ucMotor, int nPower,  int nDegrees);
# void SmartMotorRotations(unsigned char ucMotor, int nPower,  float fRotations);
# void SmartMultiMotorDegrees(unsigned char ucNumMotors , unsigned char ucMasterMotor , unsigned char ucMotor1, unsigned char ucMotor2, unsigned char ucMotor3, unsigned char ucMotor4, unsigned char ucInvert1, unsigned char ucInvert2 , unsigned char ucInvert3 , unsigned char ucInvert4 , int nPower, int nDegrees);
# void SmartMultiMotorRotations(unsigned char ucNumMotors , unsigned char ucMasterMotor , unsigned char ucMotor1, unsigned char ucMotor2, unsigned char ucMotor3, unsigned char ucMotor4, unsigned char ucInvert1, unsigned char ucInvert2 , unsigned char ucInvert3 , unsigned char ucInvert4 , int nPower, float fRotations);
# //---- SMART TASKS / ROBOT DRIVING  --------------------------------------------------------
# void DefineRobotMotors(unsigned char ucGearing, unsigned char ucMasterMotor,
#                        unsigned char ucLeftfrontMotor, unsigned char ucRightfrontMotor,
#                        unsigned char ucLeftrearMotor, unsigned char ucRightrearMotor,
#                        unsigned char ucLeftfrontInvert, unsigned char ucRightfrontInvert,
#                        unsigned char ucLeftrearInvert, unsigned char ucRightrearInvert);
# void DriveRobot(int nPower);
# void TurnRobotCenter(int nPower);
# void TurnRobotSwing(int nPower);
# void StopRobot();
# void DriveRobotTimeControl(int nPower, long lTime);
# void TurnRobotCenterTimeControl(int nPower, long lTime);
# void TurnRobotSwingTimeControl(int nPower, long lTime);
# void DriveSmartMotorsDegrees(int nPower, int nDegrees);
# void DriveSmartMotorsRotations(int nPower,  float fRotations);
# void TurnSmartMotorsCenterDegrees(int nPower, int nDegrees);
# void TurnSmartMotorsCenterRotations(int nPower,  float fRotations);
# void DriveRobotCurve(int nPower, float fCurve);
# void DriveRobotCurveTimeControl(int nPower, float fCurve, long lTime);
# void DriveCurveSmartMotorsDegrees(int nPower, float fCurve, int nDegrees);
# void DriveCurveSmartMotorsRotations(int nPower, float fCurve, float fRotations);
