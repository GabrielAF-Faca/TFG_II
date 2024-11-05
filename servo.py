from machine import Pin, PWM
'''
class Servo:
    
    # Construtor
    def __init__(self, reverse=False):
        self.reverse = reverse
        self.FREQ = 50
        self.pulse_min = 2000 # 0º ~ 0.61 ms
        self.pulse_max = 7800 # 180º ~ 2.38 ms
        self.duty = self.pulse_min + (self.pulse_max - self.pulse_min) #90º
    
    # Configura o pino e inicia o PWM a 90º
    def attach(self, pino):
        self.pin = Pin(pino)
        self.pwm = PWM(self.pin)
        self.pwm.freq(self.FREQ)
        self.pwm.duty_u16(self.duty)
    
    # Converte o angulo em pulso
    def convert(self, angulo):
        if angulo <= 0:
            return self.pulse_min
        if angulo >= 180:
            return self.pulse_max
        
        pulso = self.pulse_min + int( (angulo / 180) * (self.pulse_max - self.pulse_min) )
        return pulso
    
    # Recebe o angulo e controla o servo
    def write(self, angulo):
        self.duty = self.convert(angulo)
        
        if self.reverse:
            self.duty = self.convert(180-angulo)
        self.pwm.duty_u16(self.duty)

''' 
class Servo:
 
    def __init__(self, pin: int or Pin or PWM, freq=50, minVal=2500, maxVal=7500, reverse=False):

        if isinstance(pin, int):
            pin = Pin(pin, Pin.OUT)
            
        if isinstance(pin, Pin):
            self.__pwm = PWM(pin)
            
        if isinstance(pin, PWM):
            self.__pwm = pin
            
        self.__pwm.freq(freq)
        self.minVal = minVal
        self.maxVal = maxVal
        
        self.reverse = reverse
        
        self.angle = None
        
    def read(self):
        return self.angle
    
    def write(self, angle):
          
        if self.reverse:
            angle = 180 - angle
        
        if angle <= 0:
            angle = 1
            
        if angle > 180:
            angle = 180
        
        self.angle = angle
        
        value = (angle) * (1024) / (180)
        
        self.goto(round(value)) # Convert range value to angle value
        
        return angle
    
    def goto(self, value: int):

        if value < 0:
            value = 0
            
        elif value > 1024:
            value = 1024
            
        delta = self.maxVal - self.minVal
        
        target = int(self.minVal + ((value / 1024) * delta))
        
        self.__pwm.duty_u16(target)
        
        
    def min_pos(self):
        self.__pwm.duty_u16(self.minVal)
    
    def max_pos(self):
        self.__pwm.duty_u16(self.maxVal)
    
 
