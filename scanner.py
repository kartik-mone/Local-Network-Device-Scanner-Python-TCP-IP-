import socket
import time

class ScanResult:
    def __init__(self, ip, is_alive, response_time=None):
        self.ip = ip
        self.is_alive = is_alive
        self.response_time = response_time

class Scanner:
    def __init__(self, port=80, timeout=1):
        self.port = port
        self.timeout = timeout

    def scan_ip(self, ip):
        start = time.time()
        try:
            with socket.create_connection((ip, self.port), timeout=self.timeout):
                end = time.time()
                return ScanResult(ip, True, round((end - start) * 1000, 2))
        except:
            return ScanResult(ip, False)