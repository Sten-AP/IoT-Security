from http.server import BaseHTTPRequestHandler, HTTPServer
import os

BASE_DIR = os.path.dirname(__file__)

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        with open(f'{BASE_DIR}/index.html', 'r') as file:
            self.wfile.write(file.read().encode())

    def do_POST(self):
        self.do_GET()

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()
