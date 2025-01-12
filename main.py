from mpu6050 import mpu6050 
import time 
import pygame
import L298NMoterDriver as motor

mpu = mpu6050(0x68)

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

motor.init()


contols_turn =[0.0,0.0]
contols_acc =[0.0,0.0]


accel_data = mpu.get_accel_data()

gyro_data = mpu.get_gyro_data()

while(True):
	for event in pygame.event.get():
		if event.type == pygame.JOYAXISMOTION:
			if event.axis <= 1:
				contols_turn[event.axis] =event.value
			if event.axis == 4:
				contols_acc[0] = (round(event.value,1)+1.0)/2.0
			if event.axis == 5:
				contols_acc[1] = (round(event.value,1)+1.0)/2.0
	print(f"[{round(contols_turn[0],1)},{round(contols_turn[1],1)}] speed: {contols_acc}") 
	
	motor._pwm_d=contols_acc*100.0
	motor.edit_PWM_D(contols_acc*100.0)
	motor.update_PWM_D()
	motor.config_forwardA()
	accel_data = mpu.get_accel_data()
	gyro_data = mpu.get_gyro_data()
	print(mpu.get_temp())
	print(f" acc: {accel_data['x']}, {accel_data['y']}, {accel_data['z']}")
	print(f" gyro: {gyro_data['x']}, {gyro_data['y']}, {gyro_data['z']}")
	time.sleep(.1)
	
