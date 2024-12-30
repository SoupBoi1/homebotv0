import RPi.GPIO as GPIO

class L298NMoterDriver():

    PIN_enA = 12
    PIN_enB = 13
    pwm_frequncy = 1000
    pwm_duty = 100
    pwm_enA= GPIO.PWM(PIN_enA,pwm_frequncy)
    pwm_enB = GPIO.PWM(PIN_enB,pwm_frequncy)
    _pwm_d=[100,100] #index 0 is A suty cycle and index 1 is B cycle
    
    PIN_in1 = 24
    PIN_in2 = 23
    PIN_in3 =17
    PIN_in4 = 22
    pwm_enable = True


    
    def startA():
        enA_pwm.start(_pwm_d[0])
    def startB():
        enB_pwm.start(_pwm_d[1])
    def start():
        startA()
        startB()
    def stopA():
        enA_pwm.start(_pwm_d[0])
    def stopB():
        enB_pwm.start(_pwm_d[1])
    def stop():
        stopA()
        stopB()

    def edit_PWM_D(updated):
        _pwm_d = updated
        update_PWM_D()
    def update_PWM_D():
        enA_pwm.ChangeDutyCycle(_pwm_d[0])
        enB_pwm.ChangeDutyCycle(_pwm_d[1])
    
    def edit_PWM_F(updated):
        pwm_frequncy = updated
        update_PWM_F()

    def update_PWM_F():
        enA_pwm.ChangeFrequency(pwm_frequncy)
        enB_pwm.ChangeFrequency(pwm_frequncy)

    
    def init():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN_in1,GPIO.OUT)
        GPIO.setup(PIN_in2,GPIO.OUT)
        GPIO.setup(PIN_in3,GPIO.OUT)
        GPIO.setup(PIN_in4,GPIO.OUT)
        

        if PWM_enable:
            GPIO.setup(PIN_enA,GPIO.OUT)
            GPIO.setup(PIN_enB,GPIO.OUT)
            start()
        else:
            stop()
        

        GPIO.setwarnings(False)

    def config_forwardA():
        GPIO.output(PIN_in1,False)
        GPIO.output(PIN_in2,True)

    def config_forwardB():
        GPIO.output(PIN_in3,False)
        GPIO.output(PIN_in4,True)

    def config_backwardA():
        GPIO.output(PIN_in1,True)
        GPIO.output(PIN_in2,False)

    def config_backwardB():
        GPIO.output(PIN_in3,True)
        GPIO.output(PIN_in4,False)

    def config_forward():
        config_forwardA()
        config_forwardB()

    def config_backward():
        config_backwardA()
        config_backwardB()

    def config_left():
        config_backwardA()
        config_forwardB()
        
    def config_right():
        config_forwardA()
        config_backwardB()
    
        
    