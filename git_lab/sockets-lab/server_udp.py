import socket
import sys
import os

sys.path.append(os.path.abspath("../.."))

# server_udp.py - UDP server koji prima poruke od klijenta i šalje ih natrag
from local_machine_info import print_machine_info
print_machine_info()

HOST = '0.0.0.0'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"[SERVER] Listening UDP on {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"[SERVER] Received from {addr}: {data.decode()}")
        s.sendto(data, addr)
