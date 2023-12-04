import socket

# Define the server address (Raspberry Pi's IP address and port)
SERVER_IP = '192.168.200.103' #YOUR_RASPBERRY_PI_IP'
SERVER_PORT = 9879

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f"Connected to {SERVER_IP}:{SERVER_PORT}")

# Send data to the server for computing
data_to_send = "Hello, Raspberry Pi!"
client_socket.send(data_to_send.encode('utf-8'))

# Receive the result from the server
result = client_socket.recv(1024)
print(f"Result from Raspberry Pi: {result.decode('utf-8')}")

# Close the socket
client_socket.close()
