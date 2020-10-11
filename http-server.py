import http.server
import socketserver

PORT = 8080
# Handler that just serves a static file from the current directory and any of its subdirectories
# SimpleHTTPRequestHAndler will look for an index.html
Handler = http.server.SimpleHTTPRequestHandler

# TCP address is passed as a tuple of IP (listening to all IPs) and port (which is 8080)
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()