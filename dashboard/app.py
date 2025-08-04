from flask import Flask, render_template, jsonify

# Fix import path to access scanner.py and utils.py from parent directory
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scanner import Scanner
from utils import generate_ip_range

app = Flask(__name__)

BASE_IP = '192.168.1.'
START = 1
END = 10
scanner = Scanner(port=80)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan')
def scan():
    results = []
    for ip in generate_ip_range(BASE_IP, START, END):
        result = scanner.scan_ip(ip)
        results.append({
            'ip': result.ip,
            'status': 'alive' if result.is_alive else 'unreachable',
            'response_time': result.response_time
        })
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
