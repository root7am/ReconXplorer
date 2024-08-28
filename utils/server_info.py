import requests
import os
from pystyle import Colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_error(message):
    print(f"Error: {message}")

def print_info(message):
    print(f"{message}")

def print_header(header):
    print(f"{header}")

def server_lookup():
    clear()
    invitelink = input(f"Insert end part of link of discord server link: ").strip()
    clear()

    try:
        if "discord.gg" in invitelink:
            code = invitelink.split('/')[-1]
        else:
            code = invitelink
        
        res = requests.get(f"https://discord.com/api/v9/invites/{code}")

        if res.status_code == 200:
            res_json = res.json()

            print_header("Invitation Information:")
            print_info(f"Invite Link: https://discord.gg/{res_json['code']}")
            print_info(f"Channel: {res_json['channel']['name']} ({res_json['channel']['id']})")
            print_info(f"Expiration Date: {res_json['expires_at']}\n")

            print_header("Inviter Information:")
            print_info(f"Username: {res_json['inviter']['username']}#{res_json['inviter']['discriminator']}")
            print_info(f"User ID: {res_json['inviter']['id']}\n")

            print_header("Server Information:")
            print_info(f"Name: {res_json['guild']['name']}")
            print_info(f"Server ID: {res_json['guild']['id']}")
            print_info(f"Banner: {res_json['guild']['banner']}")
            print_info(f"Description: {res_json['guild']['description']}")
            print_info(f"Custom Invite Link: {res_json['guild']['vanity_url_code']}")
            print_info(f"Verification Level: {res_json['guild']['verification_level']}")
            print_info(f"Splash: {res_json['guild']['splash']}")
            print_info(f"Features: {', '.join(res_json['guild']['features'])}")
        else:
            print_error(f"An error occurred while sending request (Status Code: {res.status_code})")
        
    except Exception as e:
        print_error(f"Error: {e}")

def main():
    clear()

    while True:
        server_lookup()
        input(f"\nPress ENTER to return to the main menu")
        clear()

if __name__ == "__main__":
    main()