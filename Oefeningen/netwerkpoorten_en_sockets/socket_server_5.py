import socket

port = 9000

correct_password = "secure123"
secret_message = "Dit is een geheim bericht."

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", port))
server_socket.listen(1)

print(f"Server luistert op poort {port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Verbinding van {client_address}")

    client_socket.sendall("Voer het password in.".encode())

    try:
        received_password = client_socket.recv(1024).decode().strip()
    except Exception as e:
        print(e)

    if received_password == correct_password:
        client_socket.sendall(secret_message.encode())
    else:
        client_socket.sendall("Fout wachtwoord.\n".encode())

    client_socket.close()
