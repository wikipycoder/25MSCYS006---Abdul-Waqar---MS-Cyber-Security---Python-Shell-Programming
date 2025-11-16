from scapy.all import sniff, IP, TCP

def packet_handler(packet):
    if IP in packet:
        source_ip = packet[IP].src
        dest_ip = packet[IP].dst
        
        print(f"IP Packet: {source_ip} -> {dest_ip}")
        
        if TCP in packet and packet[TCP].dport == 4444:
            print(f"  [!] ALERT: Suspicious traffic detected to port 4444 from {source_ip}!")

if __name__ == "__main__":
    print("--- Starting Packet Sniffer (Press Ctrl+C to stop) ---")
    
    try:
        sniff(prn=packet_handler, count=20)
        
    except PermissionError:
        print("\n[ERROR] Permission denied. You may need to run this script as an administrator (or with 'sudo' on Linux/macOS).")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        
    print("\n--- Sniffer has stopped ---")
