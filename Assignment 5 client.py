import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 5001))

print("TCP CLIENT")
print("Connected to server.")

while True:
    message = input("Client: ")
    client_socket.send(message.encode())

    if message.lower() == "exit":
        break

    reply = client_socket.recv(1024).decode()
    print("Server:", reply)

    if reply.lower() == "exit":
        break

client_socket.close()

print("Connection closed.")
