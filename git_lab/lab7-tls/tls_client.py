import socket
import ssl

def http_get(host, port, use_ssl=False):
    request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    
    # TCP konekcija
    with socket.create_connection((host, port)) as sock:
        if use_ssl:
            context = ssl.create_default_context()
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                ssock.sendall(request.encode())
                response = ssock.recv(4096)
        else:
            sock.sendall(request.encode())
            response = sock.recv(4096)

    return response.decode(errors='ignore')  # ignoriraj ne-dekodabilne bajtove

def prikazi_odgovor(labela, odgovor):
    print(f"\n--- Odgovor preko {labela} ---\n")
    linije = odgovor.split('\r\n')
    for i, linija in enumerate(linije[:15]):
        print(linija)
    if len(linije) > 15:
        print("...")

if __name__ == "__main__":
    host = 'www.google.com'

    # HTTP (port 80)
    odgovor_http = http_get(host, 80, use_ssl=False)

    # HTTPS (port 443)
    odgovor_https = http_get(host, 443, use_ssl=True)

    # Prikaz u konzoli
    print(f"Provjera dostupnosti {host} preko HTTP i HTTPS protokola:\n")
    prikazi_odgovor("HTTP (port 80)", odgovor_http)
    prikazi_odgovor("HTTPS (port 443)", odgovor_https)
