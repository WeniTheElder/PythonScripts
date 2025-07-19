import socket

PORT = 2000

with socket.socket() as client:
    client.connect(('localhost', PORT))
    while True:
        message = input("enter a message to send:").encode()
        if message.lower() == 'q':
            break
        client.sendall(message)