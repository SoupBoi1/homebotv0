from mpu6050 import mpu6050 
import time 
import pygame
from L298NMoterDriver import L298NMoterDriver as motor
import ControlerTranslator
import sonar 

mpu = mpu6050(0x68)

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

motor.init()
sonar.init()


contols_turn =[0.0,0.0]
contols_acc =[0.0,0.0]
contols_t = False

accel_data = mpu.get_accel_data()

gyro_data = mpu.get_gyro_data()
try: 
		
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.JOYAXISMOTION:
				if event.axis <= 1:
					contols_turn[event.axis] =event.value
				if event.axis == 4:
					contols_acc[0] = (round(event.value,1)+1.0)/2.0
					motor.config_forward()
				if event.axis == 5:
					contols_acc[1] = (round(event.value,1)+1.0)/2.0
					motor.config_backward()
			elif event.type == pygame.JOYBUTTONUP:
				if event.button ==4:
						contols_t = not contols_t
				print(f"Button {event.button} released")
		print(f"[{round(contols_turn[0],1)},{round(contols_turn[1],1)}] speed: {contols_acc_1D}") 
		motor._pwm_d = ControlerTranslator.get(contols_turn,contols_acc[0]+contols_acc[1],100)
		#motor.edit_PWM_D([contols_acc[1]*100.0,contols_acc[0]*100.0])motor._pwm_d()
		print(motor._pwm_d)
		motor.update_PWM_D()
		#if contols_t:
		#        motor.config_backward()
		#else:
		#    motor.config_forward()
		sonar.getDistance()
		accel_data = mpu.get_accel_data()
		gyro_data = mpu.get_gyro_data()
		print(mpu.get_temp())
		print(f" acc: {accel_data['x']}, {accel_data['y']}, {accel_data['z']}")
		print(f" gyro: {gyro_data['x']}, {gyro_data['y']}, {gyro_data['z']}")
		time.sleep(.1)
except KeyboardInterrupt:
        GPIO.cleanup()