import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Lokalno ime računala: {hostname}")
print(f"IP adresa: {ip_address}")