import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 5001))
server_socket.listen(1)

print("TCP SERVER")
print("Server started...")
print("Waiting for client connection...")

conn, address = server_socket.accept()

print("Client connected:", address)

while True:
    message = conn.recv(1024).decode()

    if not message or message.lower() == "exit":
        break

    print("Client:", message)

    reply = input("Server: ")
    conn.send(reply.encode())

    if reply.lower() == "exit":
        break

conn.close()
server_socket.close()

print("Connection closed.")
