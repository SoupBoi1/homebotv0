from mpu6050 import mpu6050 
import time 
import pygame

mpu = mpu6050(0x68)

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
turn =[0.0,0.0]

accel_data = mpu.get_accel_data()

gyro_data = mpu.get_gyro_data()

while(True):
	for event in pygame.event.get():
		if event.type == pygame.JOYAXISMOTION:
			if event.axis <= 1:
				turn[event.axis] =event.value
	print(f"[{round(turn[0],1)},{round(turn[1],1)}]") 
	
	accel_data = mpu.get_accel_data()
	gyro_data = mpu.get_gyro_data()
	print(mpu.get_temp())
	print(f" acc: {accel_data['x']}, {accel_data['y']}, {accel_data['z']}")
	print(f" gyro: {gyro_data['x']}, {gyro_data['y']}, {gyro_data['z']}")
	time.sleep(.1)
	
