from scapy.all import IP, ICMP, send

def craft_and_send_ping(destination_ip):
    print(f"--- Crafting and sending ICMP packet to {destination_ip} ---")
    
    try:
        packet = IP(dst=destination_ip, ttl=64) / ICMP()
        
        send(packet, verbose=1)
        
        print(f"\n[SUCCESS] Packet sent to {destination_ip}.")
        
    except PermissionError:
        print("\n[ERROR] Permission denied. You may need to run this script as an administrator.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    target = "8.8.8.8"
    craft_and_send_ping(target)
