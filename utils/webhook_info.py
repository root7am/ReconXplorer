import requests
import os
from pystyle import Colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def info_webhook():
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        webhook_url = input("Enter Webhook URL: ")
        response = requests.get(webhook_url, headers=headers)
        response.raise_for_status()
        webhook_info = response.json()
        clear()
        print("\nInformation Webhook:")

        print(f"ID : {webhook_info['id']}")
        print(f"Token : {webhook_info['token']}")
        print(f"Name : {webhook_info['name']}")
        print(f"Avatar : {webhook_info['avatar']}")
        print(f"Type  : {'bot' if webhook_info['type'] == 1 else 'webhook utilisateur'}")
        print(f"Channel ID : {webhook_info['channel_id']}")
        print(f"Server ID  : {webhook_info['guild_id']}")

        print("\nUser information associated with the Webhook:")
        if 'user' in webhook_info and webhook_info['user']:
            user_info = webhook_info['user']
            print(f"ID : {user_info['id']}")
            print(f"Name : {user_info['username']}")
            print(f"DisplayName : {user_info.get('global_name', 'N/A')}")
            print(f"Number : {user_info['discriminator']}")
            print(f"Avatar : {user_info['avatar']}")
            print(f"Flags : {user_info['flags']} Publique: {user_info['public_flags']}")
            print(f"Color : {user_info.get('accent_color', 'N/A')}")
            print(f"Decoration : {user_info.get('avatar_decoration_data', 'N/A')}")
            print(f"Banner : {user_info.get('banner_color', 'N/A')}")
            print("")
        else:
            print("\nNo user information associated with the Webhook.")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    clear()
    info_webhook()
