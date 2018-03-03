#!/usr/bin/python
# coding=utf-8

import numpy as np
#import RPi.GPIO as GPIO #importamos la libreria y cambiamos su nombre por "GPIO"
import time #necesario para los delays
#import socket
import bluetooth


#definimos la clase sistema solar

class SistemaSolar(object):

#Sol=0
#Mercurio=1
#Venus=2
#Tierra=3
#Marte=4
#Jupiter=5
#Saturno=6
#Urano=7
#Neptuno=8


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

        GPIO.output(5, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(5, GPIO.LOW)
        
        return "Sol"


    def number_1(self):

        GPIO.output(6, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(6, GPIO.LOW)
        
        return "Mercurio"


    def number_2(self):

        GPIO.output(13, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(13, GPIO.LOW)
        
        return "Venus"


    def number_3(self):

        GPIO.output(19, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(19, GPIO.LOW)
        
        return "Tierra"


    def number_4(self):

        GPIO.output(26, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(26, GPIO.LOW)
        
        return "Marte"


    def number_5(self):

        GPIO.output(12, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(12, GPIO.LOW)
        
        return "Jupiter"


    def number_6(self):

        GPIO.output(16, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(16, GPIO.LOW)
        
        return "Saturno"


    def number_7(self):

        GPIO.output(20, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(20, GPIO.LOW)
        
        return "Urano"


    def number_8(self):

        GPIO.output(21, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(21, GPIO.LOW)
        
        return "Neptuno"





#Inicia el programa

if __name__ == "__main__":

    sis = SistemaSolar()

#Inicializa el bluetooth

    hostMACAddress = 'D0:7E:35:F8:D7:06' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
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


    GPIO.cleanup()  #devuelve los pines a su estado inicial




    
