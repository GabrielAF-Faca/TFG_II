import utime
import math
from servo import Servo


def cosine_law(a, b, c):
    
    nom = ((a**2) + (b**2) - (c**2))
    dem = (2 * a * b)
    res = nom/dem
    
    return math.acos(res)


class Perna:
    
    def __init__(self, params, path = './config.txt'):
        
        self.path = path
        
        j1 = params['junta1']
        j2 = params['junta2']
        j3 = params['junta3']
        
        
        self.j1 = Servo(j1['pin'], reverse=j1['inv'])
        self.j2 = Servo(j2['pin'], reverse=j2['inv'])
        self.j3 = Servo(j3['pin'], reverse=j3['inv'])

        self.j1.write(j1['ini_angle'])
        self.j2.write(j2['ini_angle'])
        self.j3.write(j3['ini_angle'])
        
        self.j1_offset = j1['offset']
        self.j2_offset = j2['offset']
        self.j3_offset = j3['offset']
        
        self.coxa_length = params['coxa_length']
        self.tibia_length = params['tibia_length']
        
        self.y_rest = params['y_rest']
        self.z_rest = params['z_rest']
        
        self.min_x = None
        self.max_x = None
        
        self.min_y = None
        self.max_y = None
        
        self.min_z = None
        self.max_z = None
        
        try:
            with open(self.path, 'r') as file:
                linha = file.readline().rstrip()
                
                self.min_x, self.max_x = [int(i) for i in linha.split(',')]
                
                linha = file.readline().rstrip()
                
                self.min_y, self.max_y = [int(i) for i in linha.split(',')]
                
                linha = file.readline().rstrip()
                
                self.min_z, self.max_z = [int(i) for i in linha.split(',')]
            
            print(f"x = ({self.min_x}, {self.max_x}) | y = ({self.min_y}, {self.max_y}) | z = ({self.min_z}, {self.max_z})")
                          
        except Exception as e:
            print(e)
            self.calibrar_eixos()
           
        
        self.move_to_point()
        
    def move_to_point(self, x=0, y=0, z=0):
        
        j2l = self.coxa_length
        j3l = self.tibia_length
        
        y += self.y_rest
        z += self.z_rest
        
        aj1 = math.degrees(math.atan(x/y))
        
        h = math.sqrt((y**2) + (x**2))
        
        l = math.sqrt((h**2) + (z**2))
        
        print(f'l = {l}')
        
        aj3 = math.degrees(cosine_law(j2l, j3l, l))
        b = math.degrees(cosine_law(l, j2l, j3l))
        a = math.degrees(math.atan(z/h))
        aj2 = b + (-a)
        
                
        self.j1.write(self.j1_offset - aj1)
        self.j2.write(aj2 + self.j2_offset)
        self.j3.write(aj3 + self.j3_offset)
            
        print(f'j1 = {aj1} | j2 = {aj2} | j3 = {aj3}')
        
    
    
    def calibrar_eixo_x(self, delay=0.01, min_b = -360, max_b = 360):
        
        self.min_x = min_b
        self.max_x = max_b
        
        for i in range(min_b, max_b):
            try:
                self.move_to_point(i, 0, 0)
                utime.sleep(delay)
            except:
                print(i)
                if i < 0:
                    if i > self.min_x:
                        self.min_x = i
                else:
                    self.max_x = i
                    break
                    
                continue
    
    
    def calibrar_eixo_y(self, delay=0.01, min_b = -360, max_b = 360):
        
        self.min_y = min_b
        self.max_y = max_b
        
        for i in range(min_b, max_b):
            try:
                self.move_to_point(0, i, 0)
                utime.sleep(delay)
            except:
                if i < 0:
                    if i > self.min_y:
                        self.min_y = i
                else:
                    self.max_y = i
                    break
                continue

    
    
    def calibrar_eixo_z(self, delay=0.01, min_b = -360, max_b = 360):
        
        self.min_z = min_b
        self.max_z = max_b
        
        for i in range(min_b, max_b):
            try:
                self.move_to_point(0, 0, i)
                utime.sleep(delay)
            except:
                if i < 0:
                    if i > self.min_z:
                        self.min_z = i
                else:
                    self.max_z = i
                    break
                continue
    
    def calibrar_eixos(self):
        print("Calibrando eixo x")
        utime.sleep(2)
        
        self.calibrar_eixo_x()
        
        print("Calibrando eixo y")
        utime.sleep(2)
        
        self.calibrar_eixo_y()
        
        print("Calibrando eixo z")
        utime.sleep(2)
        
        self.calibrar_eixo_z()
        
        print(f"x = ({self.min_x}, {self.max_x}) | y = ({self.min_y}, {self.max_y}) | z = ({self.min_z}, {self.max_z})")
        
        with open(self.path, 'w') as file:
            file.write(f'{self.min_x},{self.max_x}\n{self.min_y},{self.max_y}\n{self.min_z},{self.max_z}')
            
    
    def posicao_off(self):
        self.j1.write(90)
        self.j2.write(180)
        self.j3.write(1)
        
