import requests
from pystyle import Colors, Colorate

def discord_id_lookup():
    print(Colorate.Color(Colors.purple, "\n --- Discord ID Lookup (Multi-Source) ---", True))
    user_id = input(f"{Colors.purple} Enter Discord User ID: {Colors.reset}").strip()
    
    if not user_id.isdigit():
        print(f"{Colors.red} Error: Numerical ID required.")
        return

    
    endpoints = [
        f"https://discordlookup.mesalytic.moe/v1/user/{user_id}",
        f"https://discordid.pro/lookup/{user_id}",
    ]

    success = False
    for url in endpoints:
        try:
            print(f"{Colors.purple} Trying source: {url.split('/')[2]}...{Colors.reset}")
            
            
            if r.status_code == 200:
                data = r.json()
                
                user = data.get('username') or data.get('tag')
                info = f"""
 [!] Success!
 --------------------------------------
 Username    : {user}
 Global Name : {data.get('global_name', 'N/A')}
 ID          : {user_id}
 Created At  : {data.get('created_at', 'N/A')}
 --------------------------------------
                """
                print(Colorate.Color(Colors.purple, info, True))
                success = True
                break
        except Exception:
            continue

    if not success:
        print(f"{Colors.red} [!] All sources failed. Your network is blocking the requests.")
        print(f"{Colors.white} Solution: Use a VPN or change your DNS to 8.8.8.8.")

if __name__ == "__main__":
    discord_id_lookup()