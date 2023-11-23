import socket

port = 9000

correct_password = "geheim"
secret_message = "Dit is de geheime boodschap!"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("localhost", port))

server_socket.listen(1)

print(f"Server luistert op poort {port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Verbinding van {client_address}")

    client_socket.sendall("Welkom! Voer het wachtwoord in:\n".encode())

    received_password = client_socket.recv(1024).decode().strip()

    if received_password == correct_password:
        client_socket.sendall(secret_message.encode())
    else:
        client_socket.sendall("Onjuist wachtwoord. Verbinding gesloten.\n".encode())

    client_socket.close()
