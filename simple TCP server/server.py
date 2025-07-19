import socket
import threading

SERVER_PORT = 2000
counter = 0

def handle_client(client_socket, client_address):
    print(f"connection started with address {client_address}")
    with client_socket:
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    print(f"connection broke with address {client_address}")
                    break
                else:
                    print(f"message from address{client_address}:")
                    print(message)
            except Exception as e:
                print(f"error occured with address {client_address}:{e}")
                break
def server_program():
    with socket.socket() as server:
        print("to stop enter 'q' without the quotes")
        
        server.bind(('localhost',SERVER_PORT))
        server.listen()
        
        print(f"server is listening on port {SERVER_PORT}")
        
        while True:
            client_socket,client_address = server.accept()
            t = threading.Thread(target=handle_client, args = (client_socket,client_address))
            t.start()

if __name__ == "__main__":
    server_program()
            