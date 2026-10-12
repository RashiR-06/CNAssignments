import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(("127.0.0.1", 6000))

print("UDP SERVER")
print("Server started...")
print("Waiting for client message...")

while True:
    data, address = server_socket.recvfrom(1024)

    message = data.decode()

    print("Client:", message)

    if message.lower() == "exit":
        break

    result = message[::-1]

    server_socket.sendto(result.encode(), address)

server_socket.close()

print("Server closed.")
