import requests

BASE_URL = "http://localhost/DVWA/"

common_dirs = [
    "admin",
    "login",
    "dashboard",
    "uploads",
    "config",
    "backup"
]

print(f"--- Checking for common directories on {BASE_URL} ---")

for directory in common_dirs:
    test_url = BASE_URL + directory
    
    try:
        response = requests.get(test_url, timeout=5)
        
        print(f"[{response.status_code}] - {test_url}")
        
    except requests.ConnectionError:
        print(f"[ERROR] - Could not connect to {test_url}. Is the server running?")
        break
    except requests.RequestException as e:
        print(f"[ERROR] - An error occurred for {test_url}: {e}")
