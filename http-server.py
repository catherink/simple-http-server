import http.server
import socketserver
# import socket
from flask import Flask
from healthcheck import HealthCheck

PORT = 8080
# Handler that just serves a static file from the current directory and any of its subdirectories
# SimpleHTTPRequestHandler will look for an index.html
Handler = http.server.SimpleHTTPRequestHandler

# TCP address is passed as a tuple of IP (listening to all IPs) and port (which is 8080)
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    httpd.serve_forever()

app = Flask(__name__)

health = HealthCheck()

def server_up():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect_ex will return the error indicator 0 if the operation succeeded
    result = sock.connect_ex(('', PORT))
    if result == 0:
        return True, "200"

health.add_check(server_up())

app.add_url_rule("/health", "healthcheck", view_func=lambda: health.run())
