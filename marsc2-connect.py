import socket
from os import system

#connection variables
host = 'marsc2 ip'
port = 666 #commonly opened by mars c2

#socket creation to mars c2
mars_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mars_connection.connect((host, port))

while 1:
    #receive data from mars c2
    data_received = mars_connection.recv(16384)
    print(data_received.decode())

    #send data to mars c2
    data_to_send = str.encode(input('-> '))
    mars_connection.send(data_to_send)
