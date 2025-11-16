import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_dynamic_page(url):
    print(f"--- Dynamically scraping {url} with Selenium ---")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")
    
    driver = None
    try:
        service = Service()
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("Driver initialized. Navigating to page...")
        driver.get(url)
        
        print("Waiting for 5 seconds for page to load...")
        time.sleep(5)
        
        page_source = driver.page_source
        
        soup = BeautifulSoup(page_source, 'html.parser')
        
        links = soup.find_all('a', href=True)
        
        print(f"\n[SUCCESS] Page parsed. Found {len(links)} links.")
        print("Showing first 10 unique links:")
        
        unique_links = set()
        for link in links:
            href = link['href']
            if href.startswith('http'):
                unique_links.add(href)
        
        for link in list(unique_links)[:10]:
            print(f"  - {link}")

    except Exception as e:
        print(f"\n[ERROR] An error occurred: {e}")
        print("          If this is a 'chromedriver' error, you may need to install it manually.")
    finally:
        if driver:
            driver.quit()
            print("\nBrowser driver closed.")

if __name__ == "__main__":
    target_url = "https://otx.alienvault.com/"
    scrape_dynamic_page(target_url)
