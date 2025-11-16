from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

def monitor_cisco_device():
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': '192.168.1.1',
        'username': 'admin',
        'password': 'cisco',
    }
    
    print(f"--- Attempting to connect to {cisco_device['host']} via SSH... ---")
    
    try:
        with ConnectHandler(**cisco_device) as conn:
            conn.enable()
            output = conn.send_command("show interfaces")
            
            print("\n--- Received output from device ---")
            print(output)
            
            if "CRC" in output and output.count("CRC") > 5:
                print("\n[!] ALERT: High number of CRC errors detected on an interface!")
            else:
                print("\n[+] No significant errors found.")
                
    except (NetmikoTimeoutException, ConnectionRefusedError):
        print(f"\n[ERROR] Connection failed: Could not connect to {cisco_device['host']}.")
        print("          This is expected if the device is not on your network.")
    except NetmikoAuthenticationException:
        print(f"\n[ERROR] Authentication failed for user '{cisco_device['username']}'.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    monitor_cisco_device()
