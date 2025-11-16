import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            return port
    except socket.error as e:
        print(f"Socket error on port {port}: {e}")
    finally:
        sock.close()
    return None

def port_scan(target_ip, port_list):
    print(f"--- Scanning {target_ip} for open ports... ---")
    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(target_ip, p), port_list)
        
        open_ports = [port for port in results if port is not None]

    if open_ports:
        print(f"\n[SUCCESS] Found {len(open_ports)} open port(s):")
        for port in sorted(open_ports):
            print(f"  - Port {port} is open")
    else:
        print("\n[INFO] No open ports found in the specified list.")

if __name__ == "__main__":
    target = "127.0.0.1"
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389, 8080]
    port_scan(target, common_ports)
