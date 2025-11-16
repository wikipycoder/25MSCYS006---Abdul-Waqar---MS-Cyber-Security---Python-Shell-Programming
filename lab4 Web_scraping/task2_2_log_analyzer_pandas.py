import pandas as pd
import os

csv_filename = 'network_logs.csv'

log_data = {
    'timestamp': ['2025-10-31 12:00', '2025-10-31 12:01', '2025-10-31 12:02', '2025-10-31 12:03', '2025-10-31 12:04'],
    'src_ip': ['192.168.1.10', '10.0.0.5', '192.168.1.10', '8.8.8.8', '10.0.0.5'],
    'dst_ip': ['8.8.8.8', '192.168.1.100', '1.1.1.1', '192.168.1.10', '192.168.1.101'],
    'protocol': ['DNS', 'HTTP', 'HTTPS', 'DNS', 'HTTP']
}
try:
    df_to_save = pd.DataFrame(log_data)
    df_to_save.to_csv(csv_filename, index=False)
    print(f"Created sample log file: '{csv_filename}'")
except Exception as e:
    print(f"Error creating CSV file: {e}")

print(f"\n--- Analyzing '{csv_filename}' with pandas ---")
try:
    df = pd.read_csv(csv_filename)
    
    suspicious_traffic = df[df['protocol'] == 'HTTP']
    
    print("\n[INFO] Found Suspicious HTTP Traffic:")
    print(suspicious_traffic.head(5))
    
    print("\n[INFO] Top Source IPs in Suspicious Traffic:")
    top_source_ips = suspicious_traffic['src_ip'].value_counts()
    print(top_source_ips.head(5))

except FileNotFoundError:
    print(f"\n[ERROR] The file '{csv_filename}' was not found.")
except Exception as e:
    print(f"\nAn error occurred during analysis: {e}")
