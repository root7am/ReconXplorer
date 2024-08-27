import os
import sys
import socket
from pystyle import Colors, Cursor, System, Anime, Center, Colorate

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from ip_info import get_ip_info
from get_ip import main as get_ip_main
from token_decrypt import decrypt_token
from token_checker import main as token_checker_main
from token_info import display_discord_info
from badge_changer import main as badge_changer_main
from status_rotator import status_changer
from server_info import server_lookup
from webhook_info import info_webhook
from webhook_spammer import webhookspam
from scrapper_proxy import get_proxies  
from email_info import main as email_info_main
from instagram_user_info import main as instagram_user_info_main  
from number_info import main as number_info_main 
from auto_login import main as auto_login_main
from token_generator import main as token_generator_main 
from website_info import main as website_info_main
from token_massdm import execute_mass_dm 

class colors:
    red = '[38;2;255;0;0m'
    orange = '[38;2;255;165;0m'
    green = '[38;2;100;255;100m'
    black = '[38;2;0;0;0m'
    pink = '[38;2;255;0;255m'
    purple = '[38;2;113;41;255m'
    blue = '[38;2;92;120;255m'
    white = '[38;2;255;255;255m'
    gray = '[38;2;200;200;200m'
    light_gray = '[38;2;150;150;150m'

watermark = '''
 ____                     __  __      _                     
|  _ \ ___  ___ ___  _ __ \ \/ /_ __ | | ___  _ __ ___ _ __ 
| |_) / _ \/ __/ _ \| '_ \ \  /| '_ \| |/ _ \| '__/ _ \ '__|
|  _ <  __/ (_| (_) | | | |/  \| |_) | | (_) | | |  __/ |   
|_| \_\___|\___\___/|_| |_/_/\_\ .__/|_|\___/|_|  \___|_|   
                               |_|                          
                    Press ENTER to continue  
                            '''

Cursor.HideCursor()
System.Title('Press ENTER to continue')
Anime.Fade(Center.Center(watermark), Colors.purple_to_blue, Colorate.Vertical, interval=0.100, enter=True)

Cursor.ShowCursor()

print(watermark
      .replace('█', colors.purple + '█')
      .replace('╗', colors.blue + '╗')
      .replace('║', colors.blue + '║')
      .replace('╝', colors.blue + '╝')
      .replace('═', colors.blue + '═')
      .replace('╔', colors.blue + '╔')
      + '\n' + colors.white)

def display_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{Colors.purple} ____                     __  __      _                     ")
    print(f"|  _ \\ ___  ___ ___  _ __ \\ \\/ /_ __ | | ___  _ __ ___ _ __ ")
    print(f"| |_) / _ \\/ __/ _ \\| '_ \\ \\  /| '_ \\| |/ _ \\| '__/ _ \\ '__|")
    print(f"|  _ <  __/ (_| (_) | | | |/  \\| |_) | | (_) | | |  __/ |   ")
    print(f"|_| \\_\\___|\\___\\___/|_| |_/_/\\_\\ .__/|_|\___/|_|  \\___|_|   ")
    print(f"                               |_|                           ")
    print("            Developers : @6AM & @7AM | discord.gg/brifr")
    print("")
    print(f"{Colors.purple}─────────────────────────────────────────────────────────────────────────────────────────────────────{Colors.reset}")
    print(f"{Colors.purple}[1]{Colors.reset} - IP Info{Colors.reset} {Colors.purple}(Osint){Colors.reset}                                     {Colors.purple}[11]{Colors.reset} - Scrapper Proxy {Colors.purple}(Scrapper){Colors.reset}")         
    print(f"{Colors.purple}[2]{Colors.reset} - Get IP{Colors.reset} {Colors.purple}(Other){Colors.reset}                                      {Colors.purple}[12]{Colors.reset} - Email Info {Colors.purple}(Osint){Colors.reset}")
    print(f"{Colors.purple}[3]{Colors.reset} - Token Decrypt{Colors.reset} {Colors.purple}(Discord){Colors.reset}                             {Colors.purple}[13]{Colors.reset} - Instagram User Info {Colors.purple}(Osint){Colors.reset}")
    print(f"{Colors.purple}[4]{Colors.reset} - Token Checker{Colors.reset} {Colors.purple}(Discord){Colors.reset}                             {Colors.purple}[14]{Colors.reset} - Number Info {Colors.purple}(Osint){Colors.reset}")                           
    print(f"{Colors.purple}[5]{Colors.reset} - Token Info{Colors.reset} {Colors.purple}(Discord){Colors.reset}                                {Colors.purple}[15]{Colors.reset} - Auto Login {Colors.purple}(Discord){Colors.reset}")                              
    print(f"{Colors.purple}[6]{Colors.reset} - Badge Changer{Colors.reset} {Colors.purple}(Discord){Colors.reset}                             {Colors.purple}[16]{Colors.reset} - Token Generator {Colors.purple}(Generator){Colors.reset}")
    print(f"{Colors.purple}[7]{Colors.reset} - Status Rotator{Colors.reset} {Colors.purple}(Discord){Colors.reset}                            {Colors.purple}[17]{Colors.reset} - Discord Massreport {Colors.purple}(Discord){Colors.reset}")
    print(f"{Colors.purple}[8]{Colors.reset} - Server Info{Colors.reset} {Colors.purple}(Discord){Colors.reset}                               {Colors.purple}[18]{Colors.reset} - Website Info {Colors.purple}(Osint){Colors.reset}")
    print(f"{Colors.purple}[9]{Colors.reset} - Webhook Info{Colors.reset} {Colors.purple}(Discord){Colors.reset}                              {Colors.purple}[19]{Colors.reset} - Token Massdm {Colors.purple}(Discord){Colors.reset}")
    print(f"{Colors.purple}[10]{Colors.reset} - Webhook Spammer{Colors.reset} {Colors.purple}(Discord){Colors.reset}")
    print(f"{Colors.purple}─────────────────────────────────────────────────────────────────────────────────────────────────────{Colors.reset}")
    print(f"{Colors.purple}[quit]{Colors.reset} - Quit{Colors.reset}")
    print("")

def get_pc_name():
    """Retourne le nom de l'ordinateur"""
    return socket.gethostname()

def prompt_input(prompt_message):
    pc_name = get_pc_name()
    return input(f"╭─── {pc_name}@ReconXplorer\n│\n╰─$ {prompt_message}")

def ip_info():
    ip = prompt_input("Enter IP address: ")
    print(f"Fetching information for IP: {ip}...")
    data = get_ip_info(ip)
    
    if data:
        print(f"IP Address: {data.get('ip')}")
        print(f"City: {data.get('city')}")
        print(f"Region: {data.get('region')}")
        print(f"Country: {data.get('country')}")
        print(f"Location: {data.get('loc')}")
        print(f"Organization: {data.get('org')}")
        print(f"Timezone: {data.get('timezone')}")
    else:
        print("No information found.")

def token_decrypt():
    import base64
    from pystyle import Colors
    
    clear()
    userid = prompt_input("Enter Discord ID: ")
    encoded_bytes = base64.b64encode(userid.encode("utf-8"))
    encoded_str = str(encoded_bytes, "utf-8")
    print(f'\nFIRST PART : {encoded_str}')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def token_info():
    clear()
    try:
        print("Token Info Fetcher")
        token_discord = prompt_input("Enter Discord token: ")
        display_discord_info(token_discord)
        clear()
    except Exception as e:
        print(f"Error: {e}")

def badge_changer():
    clear()
    badge_changer_main()

def status_rotator():
    clear()
    status_changer()

def server_info():
    clear()
    server_lookup()

def webhook_info():
    clear()
    webhook_url = prompt_input("Enter Webhook URL: ")
    info_webhook(webhook_url)

def webhook_spammer():
    clear()
    webhookspam() 

def scrapper_proxy():
    clear()
    print("Starting proxy scrapper...")
    get_proxies()
    print("Proxies have been scraped and saved to proxies.txt.")
    input("\nPress Enter to return to the menu...")

def email_info():
    clear()
    email_info_main()  
    input("\nPress Enter to return to the menu...")

def instagram_user_info():
    clear()
    instagram_user_info_main()
    input("\nPress Enter to return to the menu...")

def number_info():
    clear()
    number_info_main()  
    input("\nPress Enter to return to the menu...")

def auto_login():
    clear()
    auto_login_main()  
    input("\nPress Enter to return to the menu...")

def token_generator():
    clear()
    token_generator_main()  
    input("\nPress Enter to return to the menu...")

def website_info():
    clear()
    website_info_main()  
    input("\nPress Enter to return to the menu...")

def main():
    while True:
        display_menu()
        choice = prompt_input("")
        
        if choice == '1':
            ip_info()
        elif choice == '2':
            get_ip_main()
        elif choice == '3':
            token_decrypt()
        elif choice == '4':
            token_checker_main()
        elif choice == '5':
            token_info()
        elif choice == '6':
            badge_changer()
        elif choice == '7':
            status_rotator()
        elif choice == '8':
            server_info()
        elif choice == '9':
            webhook_info()
        elif choice == '10':
            webhook_spammer() 
        elif choice == '11':
            scrapper_proxy()  
        elif choice == '12':
            email_info() 
        elif choice == '13':
            instagram_user_info()  
        elif choice == '14':
            number_info()  
        elif choice == '15':
            auto_login()  
        elif choice == '16':
            token_generator() 
        elif choice == '17':
            os.system('python utils/discord_massreport.py')
        elif choice == '18':
            website_info()
        elif choice == '19':
            execute_mass_dm() 
        elif choice == 'quit':
            print("Exiting...")
            break
        else:
            print("Invalid option, please select again.")
        
        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()