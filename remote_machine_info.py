import subprocess
import platform
import socket

def check_network_availability(host):
    args = ["ping", "-n", "2", "-w", "1000", host] if platform.system().lower() == "windows" else ["ping", "-c", "2", "-W", "1", host]
    
    try:
        output = subprocess.run(
            args,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5
        )
        return output.returncode == 0
    except:
        return False

def get_ip_address(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None

def main():
    host = input("Enter domain name: ").strip() or "google.com"
    
    print(f"\n Checking availability for: {host}")
    
    if check_network_availability(host):
        print("Ping successfull")
        
        ip = get_ip_address(host)
        if ip:
            print(f" IP address for {host}: {ip}")
        else:
            print(f" Can't find IP address for {host}")
    else:
        print("Host is not available!")

if __name__ == "__main__":
    main()