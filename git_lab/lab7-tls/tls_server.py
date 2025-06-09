import socket
import ssl

hostname = 'www.google.com'
port = 443

# kreiranje SSL konteksta
context = ssl.create_default_context()

# kreiranje TCP socketa i wrepanje u SSL
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert = ssock.getpeercert()

        print("\nCertifikat uspješno dohvaćen.\n")

        # ispis informacija o certifikatu
        subject = dict(x[0] for x in cert['subject'])
        issuer = dict(x[0] for x in cert['issuer'])

        print("Subject (za koga vrijedi):")
        for key, value in subject.items():
            print(f"   {key}: {value}")

        print("\nIssuer (tko je izdao):")
        for key, value in issuer.items():
            print(f"   {key}: {value}")

        print("\nVrijedi od:", cert['notBefore'])
        print("Vrijedi do:", cert['notAfter'])
