from scanner import Scanner
from utils import generate_ip_range, log_result

# Change the base IP to your local network (like '192.168.1.')
BASE_IP = '192.168.1.'
START = 1
END = 10

scanner = Scanner(port=80)

print(f"Scanning {BASE_IP}{START} to {BASE_IP}{END} on port 80...\n")

for ip in generate_ip_range(BASE_IP, START, END):
    result = scanner.scan_ip(ip)
    log_result(result)