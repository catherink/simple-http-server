from flask import Flask
from healthcheck import HealthCheck
import socket

app = Flask(__name__)

@app.route('/')
def hello_python():
    return 'Hello, Python!'

health = HealthCheck()

@app.route('/health')
def server_up():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect_ex will return the error indicator 0 if the operation succeeded
    result = sock.connect_ex(('', 5000))
    if result == 0:
        return "200"
    else:
        return "Something is broken"

health.add_check(server_up())

app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
