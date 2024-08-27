import os
import socket
import requests
from json import JSONDecodeError
from pystyle import Colors

def handle_error(e):
    print(f"{Colors.red}Error: {e}{Colors.reset}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()

    try:
        print(f"{Colors.red}\nYour IP is not sent to anyone.{Colors.reset}")

        try:
            response = requests.get('https://api.ipify.org?format=json')
            ip_address_public = response.json().get('ip', 'None')
        except (requests.RequestException, JSONDecodeError) as e:
            ip_address_public = "None"
            handle_error(e)

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip_address_local = s.getsockname()[0]
            s.close()
        except Exception as e:
            ip_address_local = "None"
            handle_error(e)

        try:
            ip_address_ipv6 = []
            all_interfaces = socket.getaddrinfo(socket.gethostname(), None)
            for interface in all_interfaces:
                if interface[0] == socket.AF_INET6:
                    ip_address_ipv6.append(interface[4][0])
            ip_address_ipv6 = ' / '.join(ip_address_ipv6) if ip_address_ipv6 else "None"
        except Exception as e:
            ip_address_ipv6 = "None"
            handle_error(e)

        clear_screen()
        print(f"""
IP Public (IPv4) : {ip_address_public}
IP Local  (IPv4) : {ip_address_local}
IPv6 : {ip_address_ipv6}
        """)

    except Exception as e:
        handle_error(e)

if __name__ == "__main__":
    main()