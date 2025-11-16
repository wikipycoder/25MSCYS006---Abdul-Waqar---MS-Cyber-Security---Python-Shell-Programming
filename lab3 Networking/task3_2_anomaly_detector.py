import time
from statistics import mean, stdev
import nmap
import psutil

def find_active_hosts(network_prefix='192.168.1.0/24'):
    print(f"--- Scanning network {network_prefix} for active hosts... ---")
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=network_prefix, arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        print("[SUCCESS] Active hosts found:")
        for host, status in hosts_list:
            print(f"  - Host: {host}  Status: {status}")
    except nmap.PortScannerError:
        print("\n[ERROR] Nmap not found. Please install it on your system.")
        print("          (Download from nmap.org)")
    except Exception as e:
        print(f"\nAn error occurred during the scan: {e}")

def monitor_traffic_spike(duration=30, threshold=2.5):
    print(f"\n--- Monitoring network traffic for {duration} seconds... ---")
    stats = []
    try:
        interfaces = psutil.net_io_counters(pernic=True).keys()
        if not interfaces:
            print("[ERROR] No network interfaces found.")
            return
            
        interface_to_monitor = list(interfaces)[0]
        print(f"(Monitoring on interface: {interface_to_monitor})")

        for _ in range(duration // 5):
            net_io = psutil.net_io_counters(pernic=True)[interface_to_monitor]
            stats.append(net_io.bytes_recv)
            time.sleep(5)

        rates = [(stats[i] - stats[i - 1]) / 5 for i in range(1, len(stats))]
        
        if len(rates) > 1:
            average_rate = mean(rates)
            std_deviation = stdev(rates)
            current_rate = rates[-1]
            
            print(f"Average traffic rate: {average_rate:.2f} bytes/sec")
            print(f"Current traffic rate: {current_rate:.2f} bytes/sec")

            if current_rate > average_rate + (std_deviation * threshold):
                print("\n[!] ALERT: Significant traffic spike detected!")
            else:
                print("\n[+] Network traffic appears normal.")
        else:
            print("\n[INFO] Not enough data to analyze for spikes.")
            
    except KeyError:
        print(f"[ERROR] Could not find interface. Please check its name.")
    except Exception as e:
        print(f"\nAn error occurred during traffic monitoring: {e}")

if __name__ == "__main__":
    my_network = "192.168.100.0/24"
    
    find_active_hosts(my_network)
    monitor_traffic_spike()
