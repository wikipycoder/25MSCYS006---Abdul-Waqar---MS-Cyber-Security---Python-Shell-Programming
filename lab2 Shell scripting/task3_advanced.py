import sys
import hashlib
import re
import psutil
from cryptography.fernet import Fernet

print("--- Exercise 3.1: Argument Parser & Hasher ---")
if len(sys.argv) > 1:
    input_string = sys.argv[1]
    hash_object = hashlib.sha256(input_string.encode())
    print(f"Argument provided: '{input_string}'")
    print(f"SHA256 Hash: {hash_object.hexdigest()}")
else:
    print("No argument provided. Usage: python task3_advanced.py <string_to_hash>")
print("-" * 50)

print("--- Exercise 3.2: Process Monitor ---")
print("Listing top 10 running processes:")
try:
    processes = sorted(psutil.process_iter(['pid', 'name', 'memory_percent']),
                       key=lambda p: p.info['memory_percent'],
                       reverse=True)
    for proc in processes[:10]:
        print(f"  PID: {proc.info['pid']:<6} Name: {proc.info['name']:<30} Memory: {proc.info['memory_percent']:.2f}%")
except psutil.Error as e:
    print(f"Could not list processes. Error: {e}")
    print("Please try running 'pip install psutil' in your terminal.")
print("-" * 50)

print("--- Exercise 3.3: Log Analyzer ---")
def analyze_log(filename, keyword="error"):
    print(f"Searching for keyword '{keyword}' in '{filename}'...")
    try:
        with open(filename, "r") as file:
            matches = []
            for line_num, line in enumerate(file, 1):
                if re.search(keyword, line, re.IGNORECASE):
                    matches.append((line_num, line.strip()))
            
            if matches:
                print(f"Found {len(matches)} match(es) for '{keyword}':")
                for num, l in matches:
                    print(f"  Line {num}: {l}")
            else:
                print(f"No lines containing '{keyword}' were found.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

with open("sample_system.log", "w") as f:
    f.write("INFO: System startup successful.\n")
    f.write("WARNING: CPU temperature high.\n")
    f.write("ERROR: Failed to connect to database server.\n")
    f.write("INFO: User 'admin' logged in.\n")
    f.write("Error: Critical service [auth-service] failed to start.\n")

analyze_log("sample_system.log", keyword="error")
print("-" * 50)

print("--- Exercise 3.4: File Encryptor ---")
file_to_encrypt = "secret_data.txt"
encrypted_file = file_to_encrypt + ".enc"

with open(file_to_encrypt, "w") as f:
    f.write("This is a top secret message for the cybersecurity lab.")

try:
    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(file_to_encrypt, "rb") as f:
        file_data = f.read()

    encrypted_data = cipher.encrypt(file_data)

    with open(encrypted_file, "wb") as f:
        f.write(encrypted_data)

    print(f"File '{file_to_encrypt}' has been encrypted.")
    print(f"Encrypted data saved to '{encrypted_file}'.")
    print(f"Encryption Key (save this!): {key.decode()}")

except ImportError:
    print("Could not encrypt file. Please run 'pip install cryptography'.")
except Exception as e:
    print(f"An error occurred during encryption: {e}")
