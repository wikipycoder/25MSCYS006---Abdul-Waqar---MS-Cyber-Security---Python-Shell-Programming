import requests
from bs4 import BeautifulSoup
import argparse
import re
import csv
import sys

def scrape_ips(url):
    print(f"--- Scraping {url} for malicious IPs ---")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        page_text = response.text
        
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        ips = re.findall(ip_pattern, page_text)
        
        if not ips:
            print("[INFO] No IP addresses found on the page.")
            return

        unique_ips = sorted(list(set(ips)))
        
        csv_filename = 'malicious_ips.csv'
        with open(csv_filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Malicious IP'])
            for ip in unique_ips:
                writer.writerow([ip])
                
        print(f"\n[SUCCESS] Found {len(unique_ips)} unique IPs.")
        print(f"Saved to '{csv_filename}'. Showing first 10:")
        for ip in unique_ips[:10]:
            print(f"  - {ip}")
            
    except requests.exceptions.RequestException as e:
        print(f"\n[ERROR] Could not fetch the website: {e}")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    default_url = "https://lists.blocklist.de/lists/ssh.txt"
    
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        target_url = default_url
        print(f"No URL provided. Using default: {target_url}")
    
    scrape_ips(target_url)
