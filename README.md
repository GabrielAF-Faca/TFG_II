# Robô Quadrúpede Com 3 DOF Por Perna

## Componentes
Raspberry Pi Pico W <br>
12x Servomotores MG90S <br>
Conversor Step-Down <br>
Resistor 1k ohm <br>
Resistor 2k ohm <br>
Bateria Li-Ion 2s (7.4v) 2500 mAh <br>

## Circuito
Diagrama de circuito com as conexões dos componentes
![Circuito](./Imagens/circuito.png)

R1 = 2R2 | Neste caso, R1 = 2k ohm e R2 = 1k ohm 

Soldar em uma perfboard
![protoboard](./Imagens/protoboard.png)
(A) Raspberry Removido; (B) Raspberry Adicionado

## Montagem
Imprimir modelos 3D da pasta Modelos_3d

![Tibia](./Imagens/tibia.png)

Encaixar cabeçotes dos servos  
![Montagem dos servomotores na coxa](./Imagens/coxa.png)

Encaixar servomotores e parafusar (4x)<br>
![Perna](./Imagens/perna.png)

Encaixar Pernas nas bases e parafusar
![Robo](./Imagens/robo.png)

Conectar todos os motores e bateria
![Robo Montado](./Imagens/robo_montado.jpg)

## Programação
Conectar Raspberry no computador através de cabo usb <br>
Abrir o Thonny IDE <br>

Selecionar porta do Raspberry no canto inferior direito <br>
![selecionar](./Imagens/selecionar_porta.png)

Fazer Upload dos arquivos para o Raspberry <br>
Executar código <br>
Conectar na rede Wi-Fi do robô (através de smartphone)<br>
![wifi](./Imagens/wifi.png)

Acessar o endereço 192.168.4.1 no browser web (através de smartphone)<br>
![image](https://github.com/user-attachments/assets/0acc3c8c-86fd-4dee-921f-6949394c9387)
Controlar robô

## Vídeos do funcionamento
https://www.youtube.com/playlist?list=PLtiqwHhrwyDy4FeO3HXZ96Ta0Fswptasy
