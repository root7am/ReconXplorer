import requests
from pystyle import Colors, Colorate

def roblox_lookup():
    user_id = input(f"{Colors.purple}Enter Roblox User ID: {Colors.reset}")
    try:
        r = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        if r.status_code == 200:
            data = r.json()
            info = f"""
            Username    : {data.get('name')}
            Display Name: {data.get('displayName')}
            Description : {data.get('description') if data.get('description') else 'None'}
            Created At  : {data.get('created')}
            Is Banned   : {'Yes' if data.get('isBanned') else 'No'}
            """
            print(Colorate.Color(Colors.purple, info, True))
        else:
            print(f"{Colors.red}User not found.")
    except:
        print(f"{Colors.red}Network error.")

roblox_lookup()