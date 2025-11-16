import requests
import time
import re
import csv

def scrape_iocs(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        return set(re.findall(ip_pattern, response.text))
    except requests.exceptions.RequestException as e:
        print(f"[WARNING] Could not fetch IOCs: {e}")
        return set()

def monitor_threat_feed(url, interval_seconds=60):
    print("--- Starting Threat Feed Monitor (Press Ctrl+C to stop) ---")
    
    known_iocs = set()
    csv_filename = 'newly_discovered_iocs.csv'
    
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'New IOC'])

    try:
        while True:
            print(f"\nChecking for new IOCs at {time.ctime()}...")
            
            latest_iocs = scrape_iocs(url)
            
            if latest_iocs:
                new_iocs = latest_iocs - known_iocs
                
                if new_iocs:
                    print(f"[!] Found {len(new_iocs)} new IOC(s)!")
                    with open(csv_filename, 'a', newline='') as f:
                        writer = csv.writer(f)
                        for ioc in new_iocs:
                            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                            writer.writerow([timestamp, ioc])
                            print(f"    -> Logged: {ioc}")
                    
                    known_iocs.update(new_iocs)
                else:
                    print("[+] No new IOCs found.")
            
            print(f"Waiting for {interval_seconds} seconds...")
            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\n--- Monitor stopped by user. ---")

if __name__ == "__main__":
    threat_feed_url = "https://lists.blocklist.de/lists/ssh.txt"
    monitor_threat_feed(threat_feed_url)
