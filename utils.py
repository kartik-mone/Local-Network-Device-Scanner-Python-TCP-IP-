from scanner import ScanResult

def generate_ip_range(base_ip, start, end):
    return [f"{base_ip}{i}" for i in range(start, end + 1)]

def log_result(result: ScanResult):
    if result.is_alive:
        print(f"[✔] {result.ip} is alive ({result.response_time} ms)")
    else:
        print(f"[✖] {result.ip} is unreachable")