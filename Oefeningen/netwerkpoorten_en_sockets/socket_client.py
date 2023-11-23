import socket

server_address = ("localhost", 9000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(server_address)
except Exception as e:
    print(f"Fout bij verbinden met de server: {e}")
    exit()

welcome_message = client_socket.recv(1024).decode()
print(welcome_message)

password = input("Voer het wachtwoord in: ")

client_socket.sendall(password.encode())

response = client_socket.recv(1024).decode()
print(response)

client_socket.close()
