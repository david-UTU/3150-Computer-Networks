import socket

from torch import addr

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Listen on an address for incoming connections
# Tuple for datagrams (UDP)
# Leaving the second parameter empty will make the server listen on all interfaces
server.bind(('', 12000))

while True:
    # Receive data from the client
    message, address = server.recvfrom(4096)
    if message.decode() == "quit":
        print("Client has left the chat")
        break
    message = message.upper()
    # Print the message
    print(message.decode())

    server.sendto(message, address)

server.close()
