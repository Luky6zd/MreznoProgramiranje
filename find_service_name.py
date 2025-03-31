import socket

def get_service_info(port):
    services = []
    for protocol in ['tcp', 'udp']:
        try:
            service = socket.getservbyport(port, protocol)
            services.append((protocol.upper(), service))
        except OSError:
            continue
    return services

def main():
    ports_input = input("Enter ports (divide by coma or white space): ").strip()
    ports = []
    
    for p in ports_input.replace(',', ' ').split():
        try:
            port = int(p)
            if 1 <= port <= 65535:
                ports.append(port)
            else:
                print(f"Illegal port: {p} (it must be in range 1-65535)")
        except ValueError:
            print(f"Invalid: '{p}' nije broj")

    if not ports:
        print("\n No valid ports")
        return

    print("\n{:^8} | {:^8} | {}".format("PORT", "PROTOKOL", "SERVIS"))
    print("-" * 35)
    
    for port in ports:
        services = get_service_info(port)
        if services:
            for protocol, service in services:
                print(f"{port:^8} | {protocol:^8} | {service}")
        else:
            print(f"{port:^8} | {'-':^8} | Service not found")

if __name__ == "__main__":
    main()