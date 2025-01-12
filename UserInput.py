import pygame

class UserInput:

    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        turn =[0.0,0.0]
    def getRawInputs(self):
        #ls X, ls Y, rs X, rs Y, LT,RT,
        #RawInput =[0.0,0.0,0.0,0.0,0.0,0.0]
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                print(f"Axis {event.axis} value: {event.value}")
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")
            #print(f"[{round(turn[0],1)},{round(turn[1],1)}]") 
