import os
import subprocess

print("--- Exercise 2.1 ---")
filename_to_check = "cyber_log.txt"
if os.path.exists(filename_to_check):
    print(f"File '{filename_to_check}' exists.")
else:
    print(f"File '{filename_to_check}' does not exist.")
print("-" * 30)

print("--- Exercise 2.2 ---")
print("Files in current directory:")
try:
    for item in os.listdir("."):
        print(f"- {item}")
except Exception as e:
    print(f"Could not list directory contents: {e}")
print("-" * 30)

print("--- Exercise 2.3 ---")
print("Fetching Network Information...")
try:
    result = subprocess.run(["ipconfig"], capture_output=True, text=True, check=True)
    print(result.stdout)
except FileNotFoundError:
    print("Error: 'ipconfig' command not found. Are you on Windows?")
except subprocess.CalledProcessError as e:
    print(f"Error running command: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
