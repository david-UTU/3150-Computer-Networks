from http import client
from operator import mod
import socket

server_name = 'localhost'
server_port = 12000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_name, server_port))

while True:
    # Create a TCP/IP socket
    message = input('Text: ').encode('utf-8')
    client_socket.send(message)
    # Identify client port number
    # Port numbers from the client are similar to cookies
    # The server keeps track of the port numbers

    mod_message = client_socket.recv(1024)
    print('Received: ', mod_message.decode('utf-8'))

    if message == 'quit':
        break
client_socket.close()
