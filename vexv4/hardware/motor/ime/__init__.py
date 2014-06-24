__author__ = 'james'

# //---- INTEGRATED MOTOR ENCODERS -----------------------------------------------------
# #define MAX_IME 10
# typedef volatile struct
# {
# long counter;
# unsigned short speed;
# } ImeData;

# void DefineImeTable(unsigned char ucMotor1I2C, unsigned char ucucIme2I2C, unsigned char ucMotor3I2C, unsigned char ucMotor4I2C, unsigned char ucMotor5I2C,
# unsigned char ucMotor6I2C, unsigned char ucMotor7I2C, unsigned char ucMotor8I2C, unsigned char ucMotor9I2C, unsigned char ucMotor10I2C);
# void DefineMotorTypes(unsigned char ucMotorType1, unsigned char ucMotorType2, unsigned char ucMotorType3, unsigned char ucMotorType4, unsigned char ucMotorType5,
# unsigned char ucMotorType6, unsigned char ucMotorType7, unsigned char ucMotorType8, unsigned char ucMotorType9, unsigned char ucMotorType10);


# unsigned char InitIntegratedMotorEncoders(void);
# void PresetIntegratedMotorEncoder(unsigned char ucMotor, long lPresetValue);
# long GetIntegratedMotorEncoder(unsigned char ucMotor);
# float GetIntegratedMotorEncoderSpeed(unsigned char ucMotor);
# void GetIntegratedMotorEncodersData(ImeData ime[MAX_IME]);
# void SetSaveCompetitionIme(unsigned char ucSave);
# long GetSavedCompetitionIme(unsigned char ucMotor);
# //---- PID ------------------------------------------------------------------------------
# void DefineIntegratedMotorEncoderPID(unsigned char ucMotor, float fKc, float fTi  , float fTd, long lTolerance);
# void StartIntegratedMotorEncoderPID(unsigned char ucMotor, long lSetpoint);
# void UpdateSetpointIntegratedMotorEncoderPID(unsigned char ucMotor, long lSetpoint);
# unsigned char OnTargetIntegratedMotorEncoderPID(unsigned char ucMotor);
# void StopIntegratedMotorEncoderPID(unsigned char ucMotor);
# void IME_GetPIDControlData(unsigned char ucMotor, unsigned char *pucEnabled, long *plSetPoint, int *pnPower, long *plError, long *plChangeError, long *plAccumError);