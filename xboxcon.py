import pygame
import numpy as np 

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()


while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            print(f"Axis {event.axis} value: {event.value}")
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")
        elif event.type == pygame.JOYBUTTONUP:
            print(f"Button {event.button} released")

