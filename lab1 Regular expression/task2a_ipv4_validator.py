import re

def is_valid_ipv4(ip_address):
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    if re.match(pattern, ip_address):
        print(f"'{ip_address}' is a VALID IPv4 address.")
        return True
    else:
        print(f"'{ip_address}' is an INVALID IPv4 address.")
        return False

print("--- Testing IPv4 Addresses ---")
is_valid_ipv4("192.168.1.1")
is_valid_ipv4("0.0.0.0")
is_valid_ipv4("255.255.255.255")
is_valid_ipv4("10.0.5.20")

print("\n--- Testing Invalid Addresses from the Lab ---")
is_valid_ipv4("256.1.2.3")
is_valid_ipv4("192.168.1.256")
is_valid_ipv4("192.168..1")
is_valid_ipv4("192.168.1")
is_valid_ipv4("Is this an invalid IP address")
