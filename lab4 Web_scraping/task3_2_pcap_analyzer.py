from scapy.all import rdpcap, wrpcap, IP, TCP, Ether, Raw

pcap_filename = 'sample.pcap'

def create_sample_pcap():
    print(f"=== Creating a sample packet capture file: '{pcap_filename}' ===")
    
    http_get_request = (
        Ether() / 
        IP(src="192.168.1.10", dst="1.1.1.1") / 
        TCP(sport=12345, dport=80) / 
        Raw(load="GET /index.html HTTP/1.1\r\nHost: example.com\r\n\r\n")
    )
    
    dns_request = (
        Ether() / 
        IP(dst="8.8.8.8") / 
        TCP(dport=53)
    )
    
    another_http_request = (
        Ether() / 
        IP(src="192.168.1.15", dst="2.2.2.2") / 
        TCP(sport=54321, dport=80) / 
        Raw(load="GET /login.php HTTP/1.1\r\nHost: another-site.org\r\n\r\n")
    )

    wrpcap(pcap_filename, [http_get_request, dns_request, another_http_request])
    print("Sample file created successfully.")

def analyze_pcap(filename):
    print(f"\n=== Analyzing '{filename}' for HTTP requests ===")
    
    try:
        packets = rdpcap(filename)
        
        http_requests_found = 0
        
        for packet in packets:
            if packet.haslayer(TCP) and packet[TCP].dport == 80:
                http_requests_found += 1
                if packet.haslayer(IP):
                    source_ip = packet[IP].src
                    dest_ip = packet[IP].dst
                    print(f"\n[+] Found HTTP Request from {source_ip} to {dest_ip}")
                    
                    if packet.haslayer(Raw):
                        payload = packet[Raw].load.decode('utf-8', errors='ignore')
                        print("    Payload (Request Data):")
                        print(f"    ===================\n{payload.strip()}\n    ===================")

        if http_requests_found == 0:
            print("[INFO] No HTTP requests found in the capture file.")

    except FileNotFoundError:
        print(f"\n[ERROR] The file '{filename}' was not found.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    create_sample_pcap()
    analyze_pcap(pcap_filename)
