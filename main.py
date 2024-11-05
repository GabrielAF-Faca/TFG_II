from machine import ADC 
from picozero import pico_led
from robo import Robo
from time import sleep

import machine
import math
import network
import socket
import utime


#bateria = ADC(29)
#print(bateria.read_u16())

pin = machine.ADC(28)

def webpage(ligado, bateria):
    #Template HTML
    
    if ligado:
        cor_ligar = 'green'
        cor_hover = 'rgb(0, 93, 0)'
        disabled = ''
    else:
        cor_ligar = 'red'
        cor_hover = 'rgb(181, 0, 0)'
        disabled = 'disabled'
        
    html = ""
    
    with open("./index.html") as file:
        html = file.read()
    
    bateria_string = ""
    
    for i in range(bateria):
        bateria_string += "<span>&#128994</span>"
    
    for i in range(10-bateria):
        bateria_string += "<span>&#128308</span>"
    
    html = html.replace("#DISABLED#", '#DISABLED#' + disabled)
    html = html.replace("#COR_BOTAO_LIGAR#", cor_ligar)
    html = html.replace("#COR_BOTAO_HOVER#", cor_hover)
    html = html.replace("#INDICADOR_BATERIA#", bateria_string)
    
     
    return str(html)
    #return u"".join(html).encode("utf-8")
        
def ap_mode(ssid, password):
    # Just making our internet connection
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)

    while ap.active() == False:
        pico_led.toggle()
        pass
    print('AP Mode Is Active, You can Now Connect')
    print('IP Address To Connect to:: ' + ap.ifconfig()[0])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
    s.bind(('', 80))
    s.listen(5)
    
    robo = None
    
    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        pico_led.on()
        request = conn.recv(1024)
        print('Content = %s' % str(request))
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request.startswith('/ligar?'):
            if robo == None:
                robo = Robo()
            else:
                robo.perna1.posicao_off()
                robo.perna2.posicao_off()
                robo.perna3.posicao_off()
                robo.perna4.posicao_off()
                del robo
                robo = None
        elif request.startswith('/levantar'):
            robo.levantar()
        elif request.startswith('/dancar?'):
            robo.dancar()
        elif request.startswith('/frente'):
            robo.frente()
        elif request.startswith('/deitar'):
            robo.abaixar()
        elif request.startswith('/esquerda'):
            robo.esquerda()
        elif request.startswith('/direita'):
            robo.direita()
        elif request.startswith('/tras'):
            robo.tras()
        elif request.startswith('/girarEsq'):
            robo.gira_esquerda()
        elif request.startswith('/girarDir'):
            robo.gira_direita()
        elif request.startswith('/trajeto'):
            tipo_trajeto = str(request).split("?trajeto=")[1].rstrip("'")
            print(tipo_trajeto)
            # TODO COISAS MAGICAS DEPOIS DE SELECIONAR O TRAJETO
        print(request)
        
        adc_reading  = pin.read_u16()
        adc_voltage  = (adc_reading * 2.6) / 51633
        
        porcentagem = math.floor((adc_voltage * 10)/2.6)
        
        print(porcentagem)
        
        response = webpage(robo != None, porcentagem)
        conn.send(response)
        conn.close()


ssid = 'Robo_Aranha'
password = '12345678'

ap_mode(ssid, password)


#robo.dancar()
#robo.perna1.move_to_point(90, -15, 10)
#robo.testar_perna()

#for i in range(10):
#    robo.andar()




