import subprocess
import platform
import sys

def ping_host(host):
    print(f"--- Pinging {host} ---")

    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', host]

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            print(f"[SUCCESS] Host {host} is reachable.")
            print("\n--- Ping Output ---")
            print(result.stdout)
            return True
        else:
            print(f"[FAILURE] Host {host} is unreachable.")
            print("\n--- Error Output ---")
            print(result.stderr)
            return False

    except FileNotFoundError:
        print("Error: 'ping' command not found. Is it installed and in your PATH?")
        return False
    except subprocess.TimeoutExpired:
        print(f"Error: Ping command for {host} timed out.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    target_host = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"
    ping_host(target_host)
