import utime

from servo import Servo

from perna import Perna

params = {
        'junta1':{
            'pin':18,
            'inv':True,
            'ini_angle':90,
            'offset':90
        },
        'junta2':{
            'pin':17,
            'inv':False,
            'ini_angle':90,
            'offset':0
        },
        'junta3':{
            'pin':16,
            'inv':True,
            'ini_angle':90,
            'offset':-90
        },
        'coxa_length':61.3,
        'tibia_length':63.75,
        'y_rest': 5,
        'z_rest': 0,
    }

params2 = {
        'junta1':{
            'pin':21,
            'inv':True,
            'ini_angle':90,
            'offset':45
        },
        'junta2':{
            'pin':26,
            'inv':False,
            'ini_angle':0,
            'offset':0
        },
        'junta3':{
            'pin':27,
            'inv':True,
            'ini_angle':90,
            'offset':-90
        },
        'coxa_length':61.3,
        'tibia_length':63.75,
        'y_rest': 5,
        'z_rest': 0,
    }

params3 = {
        'junta1':{
            'pin':5,
            'inv':False,
            'ini_angle':90,
            'offset':90
        },
        'junta2':{
            'pin':6,
            'inv':False,
            'ini_angle':0,
            'offset':0
        },
        'junta3':{
            'pin':7,
            'inv':True,
            'ini_angle':90,
            'offset':-90
        },
        'coxa_length':61.3,
        'tibia_length':63.75,
        'y_rest': 5,
        'z_rest': 0,
    }

params4 = {
        'junta1':{
            'pin':13,
            'inv':False,
            'ini_angle':90,
            'offset':90
        },
        'junta2':{
            'pin':14,
            'inv':False,
            'ini_angle':0,
            'offset':0
        },
        'junta3':{
            'pin':15,
            'inv':True,
            'ini_angle':90,
            'offset':-90
        },
        'coxa_length':61.3,
        'tibia_length':63.75,
        'y_rest': 5,
        'z_rest': 0,
    }

class Robo:
    
    def __init__(self):

        self.perna1 = Perna(params)
        self.perna2 = Perna(params2)
        self.perna3 = Perna(params3)
        self.perna4 = Perna(params4)

    def levantar(self):
        self.perna1.move_to_point(0, 80, 50)
        self.perna4.move_to_point(0, 80, 50)
        self.perna2.move_to_point(0, 80, 50)
        self.perna3.move_to_point(0, 80, 50)
    
    def abaixar(self):
        self.perna1.move_to_point(0, 80, 20)
        self.perna4.move_to_point(0, 80, 20)
        self.perna2.move_to_point(0, 80, 20)
        self.perna3.move_to_point(0, 80, 20)

    def dancar(self):
        self.perna1.move_to_point(0, 60, 30)
        self.perna4.move_to_point(0, 60, 30)
        self.perna2.move_to_point(0, -60, -50)
        self.perna3.move_to_point(0, 60, 30)
        utime.sleep(1)
        self.perna1.move_to_point(0, 60, 30)
        self.perna4.move_to_point(0, 60, 30)
        self.perna2.move_to_point(0, 60, 30)
        self.perna3.move_to_point(0, -60, -50)
        utime.sleep(1)
        self.perna1.move_to_point(0, -60, -50)
        self.perna4.move_to_point(0, 60, 30)
        self.perna2.move_to_point(0, 60, 30)
        self.perna3.move_to_point(0, 60, 30)
        utime.sleep(1)
        self.perna1.move_to_point(0, 60, 30)
        self.perna4.move_to_point(0, -60, -50)
        self.perna2.move_to_point(0, 60, 30)
        self.perna3.move_to_point(0, 60, 30)
        utime.sleep(1)
        self.perna1.move_to_point(0, 60, 30)
        self.perna4.move_to_point(0, 60, 30)
        self.perna2.move_to_point(0, 60, 30)
        self.perna3.move_to_point(0, 60, 30)
        utime.sleep(1)
        self.perna1.move_to_point(0, -30, 10)
        self.perna4.move_to_point(0, -30, 10)
        self.perna2.move_to_point(0, -30, 10)
        self.perna3.move_to_point(0, -30, 10)
        utime.sleep(1)
        self.perna1.move_to_point(0, 60, 30)
        self.perna4.move_to_point(0, 60, 30)
        self.perna2.move_to_point(0, 60, 30)
        self.perna3.move_to_point(0, 60, 30)
        utime.sleep(1)
        self.perna1.move_to_point(0, -30, 10)
        self.perna4.move_to_point(0, -30, 10)
        self.perna2.move_to_point(0, -30, 10)
        self.perna3.move_to_point(0, -30, 10)
        utime.sleep(1)
        self.perna1.move_to_point(0, 60, 30)
        self.perna4.move_to_point(0, 60, 30)
        self.perna2.move_to_point(0, 60, 30)
        self.perna3.move_to_point(0, 60, 30)
        utime.sleep(1)
        self.perna1.move_to_point(0, -30, 10)
        self.perna4.move_to_point(0, -30, 10)
        self.perna2.move_to_point(0, -30, 10)
        self.perna3.move_to_point(0, -30, 10)
        utime.sleep(1)
        self.perna1.move_to_point(0, 60, 30)
        self.perna4.move_to_point(0, 60, 30)
        self.perna2.move_to_point(0, 60, 30)
        self.perna3.move_to_point(0, 60, 30)
        utime.sleep(1)
    
    def frente(self):
        self.perna2.move_to_point(90, 20, 0)
        self.perna4.move_to_point(90, 20, 0)
        self.perna3.move_to_point(-40, 80, 50)
        self.perna1.move_to_point(0, 80, 50)
        utime.sleep(0.25)
        self.perna2.move_to_point(90, 20, 50)
        self.perna4.move_to_point(90, 20, 50)
        utime.sleep(0.25)
        self.perna4.move_to_point(0, 80, 50)
        self.perna2.move_to_point(-40, 80, 50)
        self.perna1.move_to_point(90, 20, 0)
        self.perna3.move_to_point(90, 20, 0)
        utime.sleep(0.25)
        self.perna1.move_to_point(90, 20, 50)
        self.perna3.move_to_point(90, 20, 50)
        utime.sleep(0.25)

    def tras(self):
        self.perna1.move_to_point(-90, 20, 0)
        self.perna3.move_to_point(-90, 20, 0)
        self.perna2.move_to_point(40, 80, 50)
        self.perna4.move_to_point(0, 80, 50)
        utime.sleep(0.25)
        self.perna1.move_to_point(-90, 20, 50)
        self.perna3.move_to_point(-90, 20, 50)
        utime.sleep(0.25)
        self.perna1.move_to_point(0, 80, 50)
        self.perna3.move_to_point(40, 80, 50)
        self.perna2.move_to_point(-90, 20, 0)
        self.perna4.move_to_point(-90, 20, 0)
        utime.sleep(0.25)
        self.perna2.move_to_point(-90, 20, 50)
        self.perna4.move_to_point(-90, 20, 50)
        utime.sleep(0.25)
    
    def direita(self):
        self.perna2.move_to_point(-90, 20, 0)
        self.perna4.move_to_point(-90, 20, 50)
        utime.sleep(0.25)
        self.perna3.move_to_point(90, 20, 50)
        self.perna1.move_to_point(90, 20, 0)
        utime.sleep(0.25)
        self.levantar()
        utime.sleep(0.5)
    
    def esquerda(self):
        self.perna2.move_to_point(90, 20, 50)
        self.perna4.move_to_point(90, 20, 0)
        utime.sleep(0.25)
        self.perna3.move_to_point(-90, 20, 0)
        self.perna1.move_to_point(-90, 20, 50)
        utime.sleep(0.25)
        self.levantar()
        utime.sleep(0.5)
    
    def gira_direita(self):
        self.perna2.move_to_point(-90, 20, 0)
        self.perna4.move_to_point(90, 20, 0)
        utime.sleep(0.25)
        self.perna2.move_to_point(-90, 20, 50)
        self.perna4.move_to_point(90, 20, 50)
        self.perna1.move_to_point(-90, 20, 0)
        self.perna3.move_to_point(90, 20, 0)
        utime.sleep(0.25)
        self.perna1.move_to_point(-90, 20, 50)
        self.perna3.move_to_point(90, 20, 50)
        utime.sleep(0.25)
        self.levantar()
        utime.sleep(0.25)
    
    def gira_esquerda(self):
        self.perna2.move_to_point(90, 20, 0)
        self.perna4.move_to_point(-90, 20, 0)
        utime.sleep(0.25)
        self.perna2.move_to_point(90, 20, 50)
        self.perna4.move_to_point(-90, 20, 50)
        self.perna1.move_to_point(90, 20, 0)
        self.perna3.move_to_point(-90, 20, 0)
        utime.sleep(0.25)
        self.perna1.move_to_point(90, 20, 50)
        self.perna3.move_to_point(-90, 20, 50)
        utime.sleep(0.25)
        self.levantar()
        utime.sleep(0.25)
    
    def testar_perna(self):
        
        for i in range(90):
            try:
                self.perna2.move_to_point(i, 0, 0)
                utime.sleep(0.1)
            except:
                continue
        
        for i in range(90, 0, -1):
            try:
                self.perna2.move_to_point(i, 0, 0)
                utime.sleep(0.1)
            except:
                continue
        
        for i in range(180):
            try:
                self.perna2.move_to_point(0, i, 0)
                utime.sleep(0.1)
            except:
                continue
        
        for i in range(180, 0, -1):
            try:
                self.perna2.move_to_point(0, i, 0)
                utime.sleep(0.1)
            except:
                continue

#robo = Robo()
#robo.perna2.j3.write(90)
#utime.sleep(1)
#robo.levantar()