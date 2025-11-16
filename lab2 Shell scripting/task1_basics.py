import datetime

print("--- Exercise 1.1 ---")
print("Hello, Cybersecurity World!")
print("-" * 30)

print("--- Exercise 1.2 ---")
name = input("Enter your name: ")
print(f"Hello, {name}!")
print("-" * 30)

print("--- Exercise 1.3 ---")
log_filename = "cyber_log.txt"
timestamp = datetime.datetime.now().isoformat()

#opening file by with block in order to close file automatically, no need for separate file opening.
try:
    with open(log_filename, "w") as file:
        file.write(f"Log entry: Script executed at {timestamp}.\n")
    print(f"Log entry written to {log_filename}")
except Exception as e:
    print(f"An error occurred: {e}")
