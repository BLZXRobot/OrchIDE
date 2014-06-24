__author__ = 'james'

# //---- INTEGRATED MOTOR ENCODERS -----------------------------------------------------
# #define MAX_IME 10
# typedef volatile struct
# {
# long counter;
# unsigned short speed;
# } ImeData;
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