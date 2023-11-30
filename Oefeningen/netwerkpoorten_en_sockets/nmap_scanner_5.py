from nmap import PortScanner
import os
import socket


correct_password = "secure123"

BASE_DIR = os.path.dirname(__file__)

nm = PortScanner()
nm.scan('localhost', '8500-9500')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hosts = []
for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        lport = sorted(lport)
        
        ports = {}
        for port in lport:
            if nm[host][proto][port]['state'] =="open":
                server_address = ("localhost", port)
                client_socket.connect(server_address)
                welcome_message = client_socket.recv(1024).decode()
                if welcome_message:
                    print(f"Poort {port}: {welcome_message}")
                    client_socket.sendall(correct_password.encode())

                    response = client_socket.recv(1024).decode()
                    print(response)
                    break
        