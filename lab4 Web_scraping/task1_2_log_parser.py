import re

log_filename = "dummy_access.log"

log_content = """
192.168.1.1 - - [01/Oct/2025:12:00:00] "GET /login" 200
10.0.0.5 - - [01/Oct/2025:12:01:00] "POST /admin" 403
192.168.1.1 - - [01/Oct/2025:12:02:00] "GET /home" 200
8.8.8.8 - - [01/Oct/2025:12:03:00] "GET /" 200
10.0.0.5 - - [01/Oct/2025:12:04:00] "POST /admin" 403
"""
try:
    with open(log_filename, "w") as f:
        f.write(log_content)
    print(f"Created '{log_filename}' for parsing.")
except Exception as e:
    print(f"Error creating log file: {e}")

print(f"--- Parsing '{log_filename}' for unique IPs ---")
ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
unique_ips = set()

try:
    with open(log_filename, 'r') as f:
        for line in f:
            match = re.search(ip_pattern, line)
            if match:
                unique_ips.add(match.group(1))

    print("Found the following unique IPs:")
    for ip in unique_ips:
        print(f"  - {ip}")

except FileNotFoundError:
    print(f"Error: Log file '{log_filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
