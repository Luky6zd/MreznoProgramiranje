import socket

import sys
import os

sys.path.append(os.path.abspath("../.."))

from local_machine_info import print_machine_info
print_machine_info()

# client_udp.py - UDP klijent koji šalje poruke serveru i prima odgovore

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print("[CLIENT] Connected to server.")
    while True:
        message = input("Unesi poruku (ili 'exit'): ")
        if message.lower() == 'exit':
            break
        s.sendto(message.encode(), (HOST, PORT))
        data, addr = s.recvfrom(1024)
        print(f"[CLIENT] Received: {data.decode()}")