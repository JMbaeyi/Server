#Mbaeyi Chibuikem VUG/CSC/22/6952
import socket

# Server settings
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}...")

# Accept client connections
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    # Receive message from client
    data = conn.recv(1024).decode()
    if not data or data.lower() == "exit":
        print("Client disconnected.")
        break
    print(f"Client: {data}")

    # Send response back to client
    response = input("Server: ")
    conn.sendall(response.encode())

# Close connection
conn.close()
server_socket.close()
