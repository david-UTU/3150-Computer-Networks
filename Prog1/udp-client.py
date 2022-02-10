import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input()

    client.sendto(bytes(message, "utf-8"), ("localhost", 12000))
    if message == "quit":
        break

    new_message, server_address = client.recvfrom(4096)

    print("Received: {}".format(new_message.decode()))

client.close()
