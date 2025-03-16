#Mbaeyi Chibuikem VUG/CSC/22/6952
import socket

# Server settings
HOST = '127.0.0.1'  # Server address
PORT = 65432        # Port to connect to

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Connected to the server. Type 'exit' to disconnect.")

while True:
    # Get user input
    message = input("Client: ")
    
    # Send message to the server
    client_socket.sendall(message.encode())

    if message.lower() == "exit":
        print("Disconnected from the server.")
        break

    # Receive response from the server
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")

# Close connection
client_socket.close()
