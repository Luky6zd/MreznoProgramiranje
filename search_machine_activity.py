import socket
import subprocess
import platform
from typing import List, Tuple

def get_hostname_from_ip(ip: str) -> None:
    """Dobiva hostname za određenu IP adresu"""
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        print(f"🔎 Hostname za {ip}: {hostname}")
    except (socket.herror, socket.gaierror) as e:
        print(f"❌ Greška pri dobivanju hostname-a: {e}")
    except Exception as e:
        print(f"⚡ Neočekivana greška: {e}")

def run_network_scan() -> None:
    """Pokreće mrežni sken ovisno o OS-u"""
    print("\n🛰️  Mrežni sken - aktivni servisi i portovi")
    
    # Odabir naredbe ovisno o OS-u
    if platform.system().lower() == 'windows':
        cmd = ['netstat', '-an']
    else:
        cmd = ['ss', '-tulnp']  # Moderna alternativa za netstat na Linuxu

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        print("📡 Rezultati mrežnog skena:")
        print(result.stdout)
        
        # Parsiranje portova za dodatnu analizu (pojednostavljeno)
        open_ports = parse_ports(result.stdout)
        if open_ports:
            print("\n🔍 Analiza pronađenih portova:")
            analyze_ports(open_ports)
            
    except subprocess.CalledProcessError as e:
        print(f"🚨 Greška pri izvršavanju {cmd[0]}: {e.stderr}")
    except FileNotFoundError:
        print(f"❌ Naredba {cmd[0]} nije pronađena!")

def parse_ports(output: str) -> List[int]:
    """Pojednostavljeno parsiranje portova iz izlaza"""
    ports = set()
    for line in output.split('\n'):
        if 'LISTEN' in line or 'ESTAB' in line:  # Filtrira zanimljive linije
            parts = line.split()
            for part in parts:
                if ':' in part and part.count(':') == 1:
                    _, port = part.rsplit(':', 1)
                    if port.isdigit():
                        ports.add(int(port))
    return list(ports)

def analyze_ports(ports: List[int]) -> None:
    """Analizira portove koristeći socket modul"""
    for port in sorted(ports):
        try:
            service = socket.getservbyport(port, 'tcp')
            print(f"• Port {port}: TCP/{service}")
        except OSError:
            pass
        try:
            service = socket.getservbyport(port, 'udp')
            print(f"• Port {port}: UDP/{service}")
        except OSError:
            pass

def main():
    # 1. Dio: Dobivanje hostname za 8.8.8.8
    get_hostname_from_ip('8.8.8.8')
    
    # 2. Dio: Mrežni sken i analiza
    run_network_scan()

if __name__ == "__main__":
    main() 