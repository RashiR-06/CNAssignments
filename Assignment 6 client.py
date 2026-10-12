import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP CLIENT")

while True:
    message = input("Enter a string: ")

    client_socket.sendto(
        message.encode(),
        ("127.0.0.1", 6000)
    )

    if message.lower() == "exit":
        break

    data, address = client_socket.recvfrom(1024)

    print("Reversed string:", data.decode())

client_socket.close()

print("Client closed.")
