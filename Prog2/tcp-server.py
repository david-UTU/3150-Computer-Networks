import socket

# Create a TCP/IP socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12000))
# Listen to accept a connection
server.listen(1)

while True:
    client_server, addr = server.accept()
    print('Connection accepted')
    # Receive the data in small chunks and retransmit it
    while True:
        # Receive data from the client
        # use .recv(n) to receive n bytes without an address associated
        data = client_server.recv(4096)
        if data.decode() == 'quit':
            break
        data = data.decode()
        data = data.upper()
        print('Received data:', data)
        data = data.encode()
        client_server.sendall(data)
