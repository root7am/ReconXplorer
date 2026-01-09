import requests
from datetime import datetime, timezone
from pystyle import Colors, Center, Colorate

def display_discord_info(token_discord=None):
    if not token_discord:
        token_discord = input("Enter Discord token: ").strip()

    try:
        headers = {'Authorization': token_discord, 'Content-Type': 'application/json'}

        r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
        user = r.json()

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
            created_at_discord = datetime.fromtimestamp(
                ((int(user['id']) >> 22) + 1420070400000) / 1000, timezone.utc
            ).strftime('%Y-%m-%d %H:%M:%S')

        nitro_discord = {0: 'False', 1: 'Nitro Classic', 2: 'Nitro Boosts', 3: 'Nitro Basic'}.get(user.get('premium_type'), 'None')

        output = f"""
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
MFA : {mfa_discord}
        """

        print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(output)))
        input("Press Enter to return to the main menu...")

    except Exception as e:
        print(f"[!] Error retrieving Discord info: {e}")


if __name__ == "__main__":
    display_discord_info()
