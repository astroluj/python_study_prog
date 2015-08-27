#-*- coding: utf-8 -*-
# TCP server example
from socket import socket, AF_INET, SOCK_STREAM

# init Set
PORT = 2000
BUF_SIZE = 2048
server_socket = socket(AF_INET,
                       SOCK_STREAM)
server_socket.bind(("", PORT))
# max 5
server_socket.listen(5)

print ("TCPServer Waiting for client on port 2000")

# blocking
while True:
        # Get Connector info
        client_socket, address = server_socket.accept()
        print('I got a connection from {0}'.format(address))
        while True:
                data = input ('SEND( TYPE q or Q to Quit):')
                if data == 'Q' or data == 'q':
                        client_socket.send (bytes(data, 'UTF-8'))
                        client_socket.close()

                        break
                else:
                        client_socket.send(bytes(data, 'UTF-8'))

                 # Get Client Data
                data = client_socket.recv(BUF_SIZE)
                if data == 'q' or data == 'Q':
                        client_socket.close()

                        break
                else:
                        print ('Recv Data : '.format(data))
	
