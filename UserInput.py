import pygame
import numpy as np 

class UserInput:

    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    def getRawInputs(self):
        #ls X, ls Y, rs X, rs Y, LT,RT,
        RawInput =[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                RawInput[event.axis] = event.value
                #print(f"Axis {event.axis} value: {event.value}")
            elif event.type == pygame.JOYBUTTONDOWN: #up is 1
                print(f"Button {event.button} pressed")
            elif event.type == pygame.JOYBUTTONUP: # down is -1
                print(f"Button {event.button} released")
        return RawInput
