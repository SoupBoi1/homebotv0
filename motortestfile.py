import RPi.GPIO as GPIO
import time
import tty, sys, termios
import keyboard  # using module keyboard
enA = 12
enB = 13
in1 = 24
in2 = 23
in3 =17
in4 = 22
pwd_fre = 500
GPIO.setmode(GPIO.BCM)
pwd_dA = 0
pwd_dB = 0 
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.setwarnings(False)

enA_pwm = GPIO.PWM(enA,pwd_fre)
enB_pwm = GPIO.PWM(enB,pwd_fre)

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(enA,GPIO.OUT)
    GPIO.setup(enB,GPIO.OUT)
    GPIO.setwarnings(False)
def config_forward():
    GPIO.output(in1,False)
    GPIO.output(in2,True)
    GPIO.output(in3,False)
    GPIO.output(in4,True)
    
def config_backward():
    GPIO.output(in1,True)
    GPIO.output(in2,False)
    GPIO.output(in3,True)
    GPIO.output(in4,False)
    
def forward(tf):
    init()
    enA_pwm.start(pwd_dA)
    enB_pwm.start(pwd_dB)
    config_forward()
    #time.sleep(tf)
    #GPIO.cleanup()
    
def backward(tf):
    init()
    GPIO.output(in1,True)
    GPIO.output(in2,False)
    GPIO.output(in3,True)
    GPIO.output(in4,False)
    time.sleep(tf)
    GPIO.cleanup()

def left(tf):
    init()
    GPIO.output(in1,False)
    GPIO.output(in2,True)
    GPIO.output(in3,True)
    GPIO.output(in4,False)
    time.sleep(tf)
    GPIO.cleanup()
def right(tf):
    init()
    GPIO.output(in1,True)
    GPIO.output(in2,False)
    GPIO.output(in3,False)
    GPIO.output(in4,True)
    time.sleep(tf)
    GPIO.cleanup()

#forward(4)
#backward(4)
filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x = 0

#GPIO.setup(enA,GPIO.OUT)
#pi_pwm = GPIO.PWM(enA,1000)
w_t= False
s_t=False
while 1:
  x=sys.stdin.read(1)[0]
  print("You pressed", x)
  if x == "w":
    print("forward")
    forward(1)
  if x == "s":
    backward(1)
  if x =="d":
    left(.1)
    print("left")
  if x =="a":    
    right(.1)
    print("right")
  if x[0] == "t":
    init()
    dutyC = int(x.split()[1])
    pwd_fre =int(x.split()[2])*100  
    enA_pwm.ChangeFrequency(pwd_fre)
    enB_pwm.ChangeFrequency(pwd_fre)
    enA_pwm.start(0)
    enB_pwm.start(0)
    print("test")
    config_forward()
    print("motor pwd: ",dutyC," and" ,pwd_fre )
    enA_pwm.ChangeDutyCycle(dutyC) #provide duty cycle in the range 0-100
    enB_pwm.ChangeDutyCycle(100-dutyC)
    time.sleep(3)
    enA_pwm.stop()
    enB_pwm.stop()
    GPIO.cleanup()

  if x[0] == "f":
    init()
    pwd_fre =int(x.split()[1])*100
    enA_pwm.ChangeFrequency(pwd_fre)
    enB_pwm.ChangeFrequency(pwd_fre)
    enA_pwm.start(0)
    enB_pwm.start(0)
    print("test")
    config_forward()
    for duty in range(0,100,10):
        print("motor pwd: ",duty," and" ,(100-duty))
        enA_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        enB_pwm.ChangeDutyCycle(100-duty)
        time.sleep(3)
    time.sleep(0.5)
    enA_pwm.stop()
    enB_pwm.stop()
    GPIO.cleanup()

#termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)
