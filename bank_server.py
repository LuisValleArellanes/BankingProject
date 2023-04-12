#Client connection
import socket
import threading 

def handle_client(client_socket, client_address):
    #ATM REQUEST LOGIC
    pass

def main():
    server_address = ('127.0.0.1', 80)#choose IP and PORT
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print(f"[*]  Bank server listenting on {server_address}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[*]Accepted connection from {server_address}")

        client_handler = threading.Thread(target=handle_client, args = (client_socket, client_address))
        client_handler.start()
        
if __name__ == '__main__':
    main()
