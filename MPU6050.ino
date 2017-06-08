// MPU-6050 per progetto Sismoduino
#include<Wire.h>
#define LED12 12
#define LED11 11

const int MPU=0x68; // I2C address of the MPU-6050

int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;

void setup(){
 pinMode(LED12, OUTPUT);
 pinMode(LED11, OUTPUT);
 Wire.begin();
 Wire.beginTransmission(MPU);
 Wire.write(0x6B); // PWR_MGMT_1 register
 Wire.write(0); // set to zero (wakes up the MPU-6050)
 Wire.endTransmission(true);
 Serial.begin(9600);
}

void loop(){
 Wire.beginTransmission(MPU);
 Wire.write(0x3B); // starting with register 0x3B (ACCEL_XOUT_H)
 Wire.endTransmission(false);
 Wire.requestFrom(MPU,14,true); // request a total of 14 registers
 AcX=Wire.read()<<8|Wire.read(); // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
 AcY=Wire.read()<<8|Wire.read(); // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)

 AcZ=Wire.read()<<8|Wire.read(); // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)

 Tmp=Wire.read()<<8|Wire.read(); // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
 GyX=Wire.read()<<8|Wire.read(); // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
 GyY=Wire.read()<<8|Wire.read(); // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
 GyZ=Wire.read()<<8|Wire.read(); // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)

 if (abs(AcZ) <= 5500)
 {
   digitalWrite(LED11, HIGH);
   digitalWrite(LED12, LOW);
 }
 else
 {
   digitalWrite(LED12, HIGH);
   digitalWrite(LED11, LOW);
 }

 Serial.println(AcZ);
 delay(50);
}
