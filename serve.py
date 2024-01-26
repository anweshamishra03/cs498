from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_private_ip():
    # Get and return the private IP address
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

@app.route('/', methods=['POST'])
def run_stress_cpu():
    # Run stress_cpu.py in a separate process
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "CPU stress process started", 202

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

