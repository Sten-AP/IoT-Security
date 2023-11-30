from http.server import SimpleHTTPRequestHandler
import socketserver
import os


BASE_DIR = os.path.dirname(__file__)
PORT = 8000

os.chdir(BASE_DIR)

handler = SimpleHTTPRequestHandler

with socketserver.TCPServer(("localhost", PORT), handler) as httpd:
    print("Server open op poort: ", PORT)
    httpd.serve_forever()