import socket
# Define the server address (Raspberry Pi's IP address and port)
SERVER_IP = 'YOUR IP ADRESS'
SERVER_PORT = 9880

def send_message(message):
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address
    server_socket.bind((SERVER_IP, SERVER_PORT))

    # Listen for incoming connections (max 1 connection in this example)
    server_socket.listen(1)
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

    # Accept a connection from the client
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    data = client_socket.recv(1024)
    if not data:
        return 'Noe data'
    try:
        result = message
        client_socket.send(result.encode('utf-8'))
        print(result)
    finally:
        client_socket.close()
        server_socket.close()
