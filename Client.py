"""
A simple Python script to send messages to a sever over Bluetooth using
Python sockets (with Python 3.3 or above).
"""

import socket

serverMACAddress = 'B8:27:EB:AC:C6:5D'
port = 3

print 'Starting the socket config ...'
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

while 1:
    message = input()
    text = message
    if text == "quit":
        break

    s.send(bytes(text))
s.close()
