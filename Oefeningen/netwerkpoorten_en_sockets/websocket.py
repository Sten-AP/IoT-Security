import socket

host = "localhost"
port = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

request = "GET / HTTP/1.1\r\nHost: localhost:8000\r\n\r\n"
client_socket.sendall(request.encode())

response = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data

print(response.decode())
client_socket.close()
