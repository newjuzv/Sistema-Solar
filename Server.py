#!/usr/bin/python
# coding=utf-8

import numpy as np
import RPi.GPIO as GPIO #importamos la libreria y cambiamos su nombre por "GPIO"
import time #necesario para los delays
#import socket
import bluetooth


#definimos la clase sistema solar

class SistemaSolar(object):

#ApagarSalidas=0
#Sol=1
#Mercurio=2
#Venus=3
#Tierra=4
#Marte=5
#Jupiter=6
#Saturno=7
#Urano=8
#Neptuno=9


    def numbers_to_methods_to_strings(self, argument):

        #establecemos el sistema de numeracion que queramos
        GPIO.setmode(GPIO.BCM)
 
        #configuramos los pines como una salida
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(21, GPIO.OUT)

        method_name = 'number_' + str(argument)
        method = getattr(self, method_name, lambda: "nothing")
        return method()


    def number_0(self):

        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        
        return "Apagado"

    def number_1(self):

        GPIO.output(5, GPIO.HIGH)
        
        return "Sol"


    def number_2(self):

        GPIO.output(6, GPIO.HIGH)
        
        return "Mercurio"


    def number_3(self):

        GPIO.output(13, GPIO.HIGH)
        
        return "Venus"


    def number_4(self):

        GPIO.output(19, GPIO.HIGH)
        
        return "Tierra"


    def number_5(self):

        GPIO.output(26, GPIO.HIGH)
        
        return "Marte"


    def number_6(self):

        GPIO.output(12, GPIO.HIGH)
        
        return "Jupiter"


    def number_7(self):

        GPIO.output(16, GPIO.HIGH)
        
        return "Saturno"


    def number_8(self):

        GPIO.output(20, GPIO.HIGH)
        
        return "Urano"


    def number_9(self):

        GPIO.output(21, GPIO.HIGH)
        
        return "Neptuno"



#Inicia el programa

if __name__ == "__main__":

    sis = SistemaSolar()

#Inicializa el bluetooth

    hostMACAddress = 'B8:27:EB:AC:C6:5D' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
    port = 3
    backlog = 1
    size = 1024
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.bind((hostMACAddress, port))
    s.listen(backlog)
    try:
        client, clientInfo = s.accept()
        while 1:
            data = client.recv(size)
            if data:
                print(data)
                sis.numbers_to_methods_to_strings(data)
                client.send(data) # Echo back to client
    except:	
        print("Closing socket")
        client.close()
        s.close()


    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)




    
