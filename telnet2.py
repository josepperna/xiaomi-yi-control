# -*- coding: utf-8 -*-
#importem llibreries
import telnetlib
import RPi.GPIO as GPIO

#Inicialitzem els pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(7, GPIO.IN)

#Ens connectem a la càmera i demanem accés
tn = telnetlib.Telnet("192.168.42.1", 7878)
tn.write("{'msg_id':257,'token':1}"+"\r")
tn.read_until("param")

#Llegim el output de la càmera per a saber 
#quin és el token a utilitzar
output = tn.read_some()
token = output[3]

#Afegim interrupccions 
GPIO.add_event_detect(3, GPIO.RISING)
GPIO.add_event_detect(5, GPIO.RISING)
GPIO.add_event_detect(7, GPIO.FALLING)

#Bucle infinit que envia els comandaments per a fer cada acció
while True:
    if GPIO.event_detected(3):#Foto
        tn.write("{'msg_id':769,'token':"+ token +"}"+"\r")
        
    if GPIO.event_detected(5):#Inici vídeo
        tn.write("{'msg_id':513,'token':"+ token +"}"+"\r")

    if GPIO.event_detected(7):#Final vídeo
        tn.write("{'msg_id':514,'token':"+ token +"}"+"\r") 
    
