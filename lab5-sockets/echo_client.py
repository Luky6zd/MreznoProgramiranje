import socket
import sys
import os

sys.path.append(os.path.abspath("../"))

from local_machine_info import print_machine_info
print_machine_info()

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[CLIENT] Connected to server.")
    
    while True:
        message = input("Unesi poruku (ili 'exit'): ")
        if message.lower() == 'exit':
            print("[CLIENT] Closing connection.")
            break
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"[SERVER RESPONSE] {data.decode()}")
