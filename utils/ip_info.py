import requests
import ipaddress
from pystyle import Colors, Center, Colorate

def get_ip_info():
    ip = input("Enter IP address: ").strip()

    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private:
            print(f"\n[!] Private or local IP address: {ip}")
            return

        url = f"https://ipwhois.app/json/{ip}"
        response = requests.get(
            url,
            timeout=5,
            headers={"User-Agent": "ReconXplorer/1.0"}
        )
        response.raise_for_status()
        data = response.json()

        if data.get("success") is False:
            print(f"\n[!] Lookup failed: {data.get('message', 'Unknown error')}")
            return

        output = f"""
IP        : {data.get('ip')}
Country   : {data.get('country')}
Region    : {data.get('region')}
City      : {data.get('city')}
ZIP       : {data.get('postal')}
ISP       : {data.get('isp')}
Org       : {data.get('org')}
Timezone  : {data.get('timezone')}
Coords    : {data.get('latitude')}, {data.get('longitude')}
"""
        print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(output)))

    except ipaddress.AddressValueError:
        print(f"\n[!] Invalid IP format: {ip}")
    except requests.RequestException as e:
        print(f"\n[!] Network error: {e}")
if __name__ == "__main__":
    get_ip_info()
