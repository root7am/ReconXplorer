import requests
import subprocess
import socket
import sys
import ssl
import concurrent.futures
from requests.exceptions import RequestException
from datetime import datetime

class Colors:
    purple = '\033[95m'
    reset = '\033[0m'
    white = '\033[97m'
    red = '\033[91m'

def current_time_hour():
    """Returns the current time in a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def handle_error(error_message):
    """Prints error messages."""
    print(f"Error: {error_message}")

def ip_type(ip):
    """Determines if the IP address is IPv4 or IPv6."""
    if ':' in ip:
        ip_type = "IPv6"
    elif '.' in ip:
        ip_type = "IPv4"
    else:
        ip_type = "Unknown"
    print(f" IP Type: {ip_type}")

def ip_ping(ip):
    """Pings the IP address to check if it's reachable."""
    try:
        if sys.platform.startswith("win"):
            result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=1)
        else:
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=1)
        ping = "Succeed" if result.returncode == 0 else "Fail"
    except Exception:
        ping = "Fail"
    print(f" Ping: {ping}")

def ip_port(ip):
    """Scans common ports to check if they are open."""
    port_protocol_map = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
        80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
        443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
        1521: "Oracle DB", 3389: "RDP"
    }
    port_list = port_protocol_map.keys()

    def scan_port(ip, port):
        """Checks if a specific port on the IP address is open."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    protocol = port_protocol_map.get(port, "Unknown")
                    print(f" Port: {port} Status: Open Protocol: {protocol}")
        except Exception:
            pass

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(scan_port, ip, port) for port in port_list]
        concurrent.futures.wait(futures)

def ip_dns(ip):
    """Attempts to resolve the DNS name for the IP address."""
    try:
        dns, _, _ = socket.gethostbyaddr(ip)
    except Exception:
        dns = "None"
    if dns != "None":
        print(f" DNS: {dns}")

def ip_host_info(ip):
    """Fetches and displays information about the IP address from ipinfo.io."""
    api_url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(api_url)
        api = response.json()
    except RequestException:
        api = {}

    host_country = api.get('country', 'None')
    host_name = api.get('hostname', 'None')
    host_isp = api.get('org', 'None')
    host_as = api.get('asn', 'None')

    if host_country != "None":
        print(f" Host Country: {host_country}")
    if host_name != "None":
        print(f" Host Name: {host_name}")
    if host_isp != "None":
        print(f" Host ISP: {host_isp}")
    if host_as != "None":
        print(f" Host AS: {host_as}")

def ssl_certificate_check(ip):
    """Checks the SSL certificate for the IP address."""
    port = 443
    try:
        with socket.create_connection((ip, port), timeout=1) as sock:
            context = ssl.create_default_context()
            with context.wrap_socket(sock, server_hostname=ip) as ssock:
                cert = ssock.getpeercert()
                print(f" SSL Certificate: {cert}")
    except Exception as e:
        print(f" SSL Certificate Check Failed: {e}")

def main():
    """Main function to execute IP scanning operations."""
    try:
        ip = input(f" IP -> ").strip()
        if not ip:
            handle_error("IP address cannot be empty.")
            return

        print(f" Information Recovery...")
        print(f" IP: {ip}")

        ip_type(ip)
        ip_ping(ip)
        ip_dns(ip)
        ip_port(ip)
        ip_host_info(ip)
        ssl_certificate_check(ip)

    except Exception as e:
        handle_error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()