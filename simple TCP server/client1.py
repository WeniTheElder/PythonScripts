import socket

PORT = 2000

with socket.socket() as client:
    client.connect(('localhost', PORT))
    while True:
        message = input("enter a message to send('quit' to exit):").encode()
        if message.lower() == 'quit':
            break
        client.sendall(message)