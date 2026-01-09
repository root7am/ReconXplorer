import socket
import requests
from pystyle import Colors

IPINFO_API_KEY = '66819ffdf72438'

def resolve_ip_from_url(url):
    try:
        ip = socket.gethostbyname(url)
        return ip
    except socket.error as e:
        print(f"Error resolving IP address for {url}: {e}")
        return None

def get_ipinfo(ip):
    url = f'https://ipinfo.io/{ip}/json?token={IPINFO_API_KEY}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data from IPinfo for IP: {ip}")
        return None

def display_website_info(ip):
    data = get_ipinfo(ip)
    
    if data:
        print(f"IP Address: {data.get('ip', 'Unknown')}")
        print(f"Organization: {data.get('org', 'Unknown')}")
        print(f"Hostname: {data.get('hostname', 'Unknown')}")
        print(f"Location: {data.get('city', 'Unknown')}, {data.get('region', 'Unknown')}, {data.get('country', 'Unknown')}")
        print(f"ISP: {data.get('isp', 'Unknown')}")
        print(f"Location Coordinates: {data.get('loc', 'Unknown')}")
    else:
        print("No information found or failed to retrieve data.")

def main():
    url = input("Enter website URL to get info: ").strip()
    ip = resolve_ip_from_url(url)
    
    if ip:
        print(f"Fetching information for IP: {ip}...")
        display_website_info(ip)
    else:
        print("Failed to resolve IP address for the given URL.")

if __name__ == "__main__":
    main()