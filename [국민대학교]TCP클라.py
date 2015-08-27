#-*- codingL utf-8 -*-
#client program
from socket import socket, AF_INET, SOCK_STREAM


# Init Set
HOST = 'localhost'
PORT = 2000
BUF_SIZE = 2048
ADDR = (HOST, PORT)

# Connection
tcpCliSock = socket(AF_INET,
                    SOCK_STREAM)
tcpCliSock.connect(ADDR)

# Blocking  
while True:
        # q or Q is define Quit
        # Get Server Data
        data = tcpCliSock.recv(BUF_SIZE)
        if  data == 'q' or data == 'Q':
                tcpCliSock.close()
                
                break
        else:
                print('Recv Data : {0}'.format(data))   
                data = input('> ')
                if data != 'Q' and data != 'q':
                        tcpCliSock.send(bytes(data,
                                              'UTF-8'))
                else:
                        tcpCliSock.send(bytes(data,
                                              'UTF-8'))
                        tcpCliSock.close()
                        
                        break


