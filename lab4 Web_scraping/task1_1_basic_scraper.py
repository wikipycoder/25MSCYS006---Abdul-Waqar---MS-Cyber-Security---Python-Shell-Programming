import requests
from bs4 import BeautifulSoup

URL = "https://krebsonsecurity.com/"
print(f"--- Scraping {URL} ---")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

try:
    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.title.string
    print(f"\nPage Title: {title.strip()}")
    
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    print(f"\nFound {len(links)} total links. Showing the first 10:")
    for link in links[:10]:
        print(f"  - {link}")
        
    print("\nFiltering for external links (starting with 'http'):")
    external_links = [link for link in links if link.startswith('http')]
    for ext_link in external_links[:10]:
        print(f"  - {ext_link}")

except requests.exceptions.RequestException as e:
    print(f"\n[ERROR] Could not fetch the website: {e}")
except Exception as e:
    print(f"\nAn error occurred during parsing: {e}")
