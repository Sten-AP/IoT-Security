from socket import socket, AF_INET, SOCK_STREAM

host = '0.0.0.0'
port = 8001

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f"Server luistert op {host}:{port}")
    
    conn, addr = s.accept()
    with conn:
        print(f"Verbonden met {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)