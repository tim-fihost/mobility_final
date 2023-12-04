import socket

SERVER_IP = 'YOUR IP SERVER IP'
SERVER_PORT = 9880

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_IP,SERVER_PORT)
print(f"Connected to {SERVER_IP}:{SERVER_PORT}")

def get_data():
    result = client_socket.recv(1024)
    print(f"Result from SERVER: {result.decode('utf-8')}")
    return result.decode('utf-8')

client_socket.close()