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

# Contrary to what is written in internet, host here defines where app is running
# and not what it listens to (flask run --host=0.0.0.0 makes app listen to all IPs)
# if __name__ == "__main__":
#    app.run(host="0.0.0.0")

