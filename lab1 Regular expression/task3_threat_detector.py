import re

sqli_pattern = re.compile(
    r"(?i)(\'|\")\s*(or|and)\s*(\'|\")\d(\'|\")\s*=\s*(\'|\")\d|union\s+select|select\s+.*\s+from",
    re.IGNORECASE
)

xss_pattern = re.compile(
    r"(?i)<script.*?>.*?</script>|alert\(.*?\)|onerror\s*=|onload\s*=",
    re.IGNORECASE
)

url_pattern = re.compile(
    r"(?i)https?://.*?(fake|evil|phish|malicious)\.",
    re.IGNORECASE
)

threat_patterns = {
    "SQL_INJECTION": sqli_pattern,
    "XSS_ATTACK": xss_pattern,
    "SUSPICIOUS_URL": url_pattern
}

def detect_threats(log_line):
    found_threats = False
    print(f"\nScanning log: \"{log_line}\"")

    for threat_name, pattern in threat_patterns.items():
        match = pattern.search(log_line)
        if match:
            print(f"  [!] ALERT: Potential {threat_name} detected!")
            print(f"      Trigger: \"{match.group(0)}\"")
            found_threats = True

    if not found_threats:
        print("  [+] Log appears clean.")

sample_logs = [
    "GET /index.php HTTP/1.1",
    "GET /login.php?user=' or '1'='1' --&pass=123",
    "GET /search?q=<script>alert('XSS');</script>",
    "User clicked on http://fakebank.com/login",
    "POST /comment data=Hello<img src=x onerror=alert(1)>",
    "GET /profile.php?user_id=105",
    "Received email from http://evil-domain.net/payload.zip",
    "GET /products.php?id=1' UNION SELECT user, pass FROM users--",
]

print("--- Starting Threat Detection Pipeline ---")
for log in sample_logs:
    detect_threats(log)
