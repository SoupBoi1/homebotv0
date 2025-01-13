import RPi.GPIO as GPIO

class L298NMoterDriver:
    PIN_enA = 12
    PIN_enB = 13
    pwm_frequncy = 1000
    pwm_duty = 100
    enA_pwm =None
    enB_pwm = None
    #enA_pwm= GPIO.PWM(PIN_enA,pwm_frequncy)
    #enB_pwm = GPIO.PWM(PIN_enB,pwm_frequncy)
    _pwm_d=[100,100] #index 0 is A suty cycle and index 1 is B cycle
    
    PIN_in1 = 24
    PIN_in2 = 23
    PIN_in3 =17
    PIN_in4 = 22
    pwm_enable = True


    
    def startA():
        L298NMoterDriver.enA_pwm.start(L298NMoterDriver._pwm_d[0])
    def startB():
        L298NMoterDriver.enB_pwm.start(L298NMoterDriver._pwm_d[1])
    def start():
        L298NMoterDriver.startA()
        L298NMoterDriver.startB()
    def stopA():
        L298NMoterDriver.enA_pwm.start(L298NMoterDriver._pwm_d[0])
    def stopB():
        L298NMoterDriver.enB_pwm.start(L298NMoterDriver._pwm_d[1])
    def stop():
        L298NMoterDriver.stopA()
        L298NMoterDriver.stopB()

    def edit_PWM_D(updated):
        _pwm_d = updated
        L298NMoterDriver.update_PWM_D()
    def update_PWM_D():
        L298NMoterDriver.enA_pwm.ChangeDutyCycle(L298NMoterDriver._pwm_d[0])
        L298NMoterDriver.enB_pwm.ChangeDutyCycle(L298NMoterDriver._pwm_d[1])
    
    def edit_PWM_F(updated):
        pwm_frequncy = updated
        update_PWM_F()

    def update_PWM_F():
        L298NMoterDriver.enA_pwm.ChangeFrequency(L298NMoterDriver.pwm_frequncy)
        L298NMoterDriver.enB_pwm.ChangeFrequency(L298NMoterDriver.pwm_frequncy)

    
    def init():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(L298NMoterDriver.PIN_in1,GPIO.OUT)
        GPIO.setup(L298NMoterDriver.PIN_in2,GPIO.OUT)
        GPIO.setup(L298NMoterDriver.PIN_in3,GPIO.OUT)
        GPIO.setup(L298NMoterDriver.PIN_in4,GPIO.OUT)
        

        if L298NMoterDriver.pwm_enable:
            GPIO.setup(L298NMoterDriver.PIN_enA,GPIO.OUT)
            GPIO.setup(L298NMoterDriver.PIN_enB,GPIO.OUT)
            L298NMoterDriver.enA_pwm= GPIO.PWM(L298NMoterDriver.PIN_enA,L298NMoterDriver.pwm_frequncy)
            L298NMoterDriver.enB_pwm= GPIO.PWM(L298NMoterDriver.PIN_enB,L298NMoterDriver.pwm_frequncy)
            L298NMoterDriver.start()
        else:
            L298NMoterDriver.stop()
        

        GPIO.setwarnings(False)

    def config_forwardA():
        GPIO.output(L298NMoterDriver.PIN_in1,False)
        GPIO.output(L298NMoterDriver.PIN_in2,True)

    def config_forwardB():
        GPIO.output(L298NMoterDriver.PIN_in3,False)
        GPIO.output(L298NMoterDriver.PIN_in4,True)

    def config_backwardA():
        GPIO.output(L298NMoterDriver.PIN_in1,True)
        GPIO.output(L298NMoterDriver.PIN_in2,False)

    def config_backwardB():
        GPIO.output(L298NMoterDriver.PIN_in3,True)
        GPIO.output(L298NMoterDriver.PIN_in4,False)

    def config_forward():
        GPIO.output(L298NMoterDriver.PIN_in1,True)
        GPIO.output(L298NMoterDriver.PIN_in1,True)

    def config_backward():
        L298NMoterDriver.config_backwardA()
        L298NMoterDriver.config_backwardB()

    def config_left():
        L298NMoterDriver.config_backwardA()
        L298NMoterDriver.config_forwardB()
        
    def config_right():
        L298NMoterDriver.config_forwardA()
        L298NMoterDriver.config_backwardB()
    
        
    
