import socket
import sys

socket.setdefaulttimeout(0.5)
# skripta za provjeru dostupnosti porta na određenoj IP adresi
# skripta provjerava je li određeni port na IP adresi otvoren ili zatvoren

import socket
import sys

def provjeri_raspon(start_port, end_port):
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        print("[GREŠKA] Portovi moraju biti između 1 i 65535.")
        return False
    if start_port > end_port:
        print("[GREŠKA] Početni port mora biti manji ili jednak krajnjem.")
        return False
    return True

def skeniraj_portove(host, start_port, end_port):
    print(f"\n[INFO] Skeniram host: {host} | Portovi: {start_port}–{end_port}")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                s.connect((host, port))
                try:
                    servis = socket.getservbyport(port)
                except OSError:
                    servis = "Nepoznat"
                print(f"Port {port} OTVOREN ({servis})")
            except (socket.timeout, ConnectionRefusedError, OSError):
                pass  # Port zatvoren ili nedostupan

def main():
    if len(sys.argv) != 4:
        print("Upotreba: python port_scanner.py <host> <pocetni_port> <zavrsni_port>")
        sys.exit(1)

    host = sys.argv[1]

    try:
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
    except ValueError:
        print("[GREŠKA] Portovi moraju biti cijeli brojevi.")
        sys.exit(1)

    if not provjeri_raspon(start_port, end_port):
        sys.exit(1)

    skeniraj_portove(host, start_port, end_port)

if __name__ == "__main__":
    main()

