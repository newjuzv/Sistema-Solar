"""
A simple Python script to send messages to a sever over Bluetooth using
Python sockets (with Python 3.3 or above).
"""

import socket

serverMACAddress = 'D0:7E:35:F8:D7:06'
port = 3
message = 'Hola Mae'

print 'Starting the socket config ...'
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

while 1:
    text = message
    if text == "quit":
        break

    s.send(bytes(text))
s.close()
