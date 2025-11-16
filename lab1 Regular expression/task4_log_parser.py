import re

def parse_and_clean_logs(log_data):
    log_pattern = re.compile(
        r'(?P<ip>\S+) \S+ \S+ \[(?P<time>.*?)\] "(?P<request>.*?)" (?P<status>\d{3}) \S+ ".*?" "(?P<user_agent>.*?)"'
    )
    
    bot_pattern = re.compile(r'bot', re.IGNORECASE)

    print("--- Starting Log Analysis ---")
    parsed_data = []

    for line in log_data.strip().split('\n'):
        match = log_pattern.match(line)
        if not match:
            continue

        log_entry = match.groupdict()
        status_code = int(log_entry['status'])
        user_agent = log_entry['user_agent']

        if status_code >= 400:
            print(f"[!] Client Error Found: IP={log_entry['ip']}, Status={status_code}, Request=\"{log_entry['request']}\"")

        if bot_pattern.search(user_agent):
            user_agent = 'SUSPICIOUS_BOT'

        parsed_data.append({
            'ip': log_entry['ip'],
            'status': status_code,
            'normalized_ua': user_agent
        })

    print("\n--- Parsed Data Table ---")
    print(f"{'IP Address':<16} {'Status':<8} {'Normalized User-Agent'}")
    print("-" * 60)
    for item in parsed_data:
        print(f"{item['ip']:<16} {item['status']:<8} {item['normalized_ua']}")

sample_log_file_content = """
127.0.0.1 - - [11/Sep/2025:10:00:00 +0000] "GET /admin HTTP/1.1" 404 1234 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
192.168.1.5 - - [11/Sep/2025:10:01:15 +0000] "GET /index.html HTTP/1.1" 200 5678 "-" "Googlebot/2.1 (+http://www.google.com/bot.html)"
10.0.0.23 - - [11/Sep/2025:10:02:30 +0000] "POST /login HTTP/1.1" 401 500 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
8.8.8.8 - - [11/Sep/2025:10:03:45 +0000] "GET /images/logo.png HTTP/1.1" 200 9101 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
192.168.1.5 - - [11/Sep/2025:10:04:00 +0000] "GET /hidden-page HTTP/1.1" 403 450 "-" "AhrefsBot/7.0; +http://ahrefs.com/robot/"
"""

parse_and_clean_logs(sample_log_file_content)
