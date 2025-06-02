import socket

HOST = 'localhost'
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

name = input("Unesite korisničko ime: ")
sock.sendall(name.encode())

print("Chat zapocet. Koristite Ctrl+c za izlaz")

while True:
    msg = input("> ")
    sock.sendall(msg.encode())