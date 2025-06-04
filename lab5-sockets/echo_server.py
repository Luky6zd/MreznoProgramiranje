import selectors
import socket
import sys
import os
import datetime
print(datetime.datetime.now())

sys.path.append(os.path.abspath("../"))

from local_machine_info import print_machine_info
print_machine_info()

sel = selectors.DefaultSelector()

HOST = 'localhost'
PORT = 65432

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ)
print(f"[SERVER] listening on {HOST}:{PORT}")

connections = {}

while True:
    events = sel.select()
    for key, _ in events:
        if key.fileobj is lsock:
            conn, addr = lsock.accept()
            print(f"[NEW] Connection from {addr}")
            conn.setblocking(False)
            sel.register(conn, selectors.EVENT_READ)
            connections[conn] = addr
        else:
            conn = key.fileobj
            try:
                data = conn.recv(1024)
            except ConnectionResetError:
                data = None

            if data:
                message = data.decode().strip()
                client_ip = connections[conn][0]
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                print(f"\n[RECEIVED MESSAGE]")
                print(f"Vrijeme: {timestamp}")
                print(f"IP klijenta: {client_ip}")
                print(f"Poruka: {message}")

                # Odgovor klijentu
                if message.lower() == "vaše_ime_prezime":
                    response = "Unos nije podržan."
                else:
                    response = message
                conn.sendall(response.encode())
            else:
                print(f"[CLOSE] {connections[conn]}")
                sel.unregister(conn)
                conn.close()
                del connections[conn]

