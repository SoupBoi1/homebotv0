from mpu6050 import mpu6050 
import time 
mpu = mpu6050(0x68)

accel_data = mpu.get_accel_data()

gyro_data = mpu.get_gyro_data()

while(True):
	accel_data = mpu.get_accel_data()
	gyro_data = mpu.get_gyro_data()
	print(mpu.get_temp())
	print(f" acc: {accel_data['x']}, {accel_data['y']}, {accel_data['z']}")
	print(f" gyro: {gyro_data['x']}, {gyro_data['y']}, {gyro_data['z']}")
	time.sleep(.1)
