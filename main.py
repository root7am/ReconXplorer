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
from tiktok_user_info import main as tiktok_user_info_main 

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
    print(f"{Colors.purple}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Colors.reset}")
    print(f"{Colors.purple}[1]{Colors.reset} - IP Info{Colors.reset} {Colors.purple}(Osint){Colors.reset}                                     {Colors.purple}[11]{Colors.reset} - Scrapper Proxy {Colors.purple}(Scrapper){Colors.reset}                                     {Colors.purple}[21]{Colors.reset} - Server Info FiveM {Colors.purple}(Osint){Colors.reset}")         
    print(f"{Colors.purple}[2]{Colors.reset} - Get IP{Colors.reset} {Colors.purple}(Other){Colors.reset}                                      {Colors.purple}[12]{Colors.reset} - Email Info {Colors.purple}(Osint){Colors.reset}                                            {Colors.purple}[22]{Colors.reset} - Steam User Info {Colors.purple}(Osint){Colors.reset}")
    print(f"{Colors.purple}[3]{Colors.reset} - Token Decrypt{Colors.reset} {Colors.purple}(Discord){Colors.reset}                             {Colors.purple}[13]{Colors.reset} - Instagram User Info {Colors.purple}(Osint){Colors.reset}                                   {Colors.purple}[23]{Colors.reset} - TikTok User Info (Indisponible) {Colors.purple}(Osint){Colors.reset}")
    print(f"{Colors.purple}[4]{Colors.reset} - Token Checker{Colors.reset} {Colors.purple}(Discord){Colors.reset}                             {Colors.purple}[14]{Colors.reset} - Number Info {Colors.purple}(Osint){Colors.reset}                                           {Colors.purple}[24]{Colors.reset} - Invite Bot To Id {Colors.purple}(Discord){Colors.reset}")                           
    print(f"{Colors.purple}[5]{Colors.reset} - Token Info{Colors.reset} {Colors.purple}(Discord){Colors.reset}                                {Colors.purple}[15]{Colors.reset} - Auto Login {Colors.purple}(Discord){Colors.reset}                                          {Colors.purple}[25]{Colors.reset} - Ip Scanner {Colors.purple}(Osint){Colors.reset}")                              
    print(f"{Colors.purple}[6]{Colors.reset} - Badge Changer{Colors.reset} {Colors.purple}(Discord){Colors.reset}                             {Colors.purple}[16]{Colors.reset} - Token Generator {Colors.purple}(Generator){Colors.reset}")
    print(f"{Colors.purple}[7]{Colors.reset} - Status Rotator{Colors.reset} {Colors.purple}(Discord){Colors.reset}                            {Colors.purple}[17]{Colors.reset} - Discord Massreport {Colors.purple}(Discord){Colors.reset}")
    print(f"{Colors.purple}[8]{Colors.reset} - Server Info{Colors.reset} {Colors.purple}(Discord){Colors.reset}                               {Colors.purple}[18]{Colors.reset} - Website Info {Colors.purple}(Osint){Colors.reset}")
    print(f"{Colors.purple}[9]{Colors.reset} - Webhook Info{Colors.reset} {Colors.purple}(Discord){Colors.reset}                              {Colors.purple}[19]{Colors.reset} - Token Massdm {Colors.purple}(Discord){Colors.reset}")
    print(f"{Colors.purple}[10]{Colors.reset} - Webhook Spammer{Colors.reset} {Colors.purple}(Discord){Colors.reset}                          {Colors.purple}[20]{Colors.reset} - Snapchat User Info{Colors.reset} {Colors.purple}(Osint){Colors.reset}")
    print(f"{Colors.purple}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Colors.reset}")
    print(f"{Colors.purple}[quit]{Colors.reset} - Quit{Colors.reset}")
    print("")

def get_pc_name():
    """Retourne le nom de l'ordinateur"""
    return socket.gethostname()

def prompt_input(prompt_message):
    pc_name = get_pc_name()
    return input(f"╭─── {pc_name}@ReconXplorer\n│\n╰─$ {prompt_message}")

handles = [
    None,
    get_ip_info,
    get_ip_main,
    decrypt_token,
    token_checker_main,
    display_discord_info,
    badge_changer_main,
    status_changer,
    server_lookup,
    info_webhook,
    webhookspam,
    get_proxies,
    email_info_main,
    instagram_user_info_main,
    number_info_main,
    auto_login_main,
    token_generator_main,
    lambda: os.system('python utils/discord_massreport.py'),
    website_info_main,
    execute_mass_dm,
    lambda: os.system('python utils/snapchat_user_info.py'),
    lambda: os.system('python utils/server_info_fivem.py'),
    lambda: os.system('python utils/steam_user_info.py'),
    tiktok_user_info_main,
    lambda: os.system('python utils/invite_bot_to_id.py'),
    lambda: os.system('python utils/ip_scanner.py')
]

def main():
    while True:
        display_menu()
        choice = prompt_input("")

        if choice.lower() == 'quit':
            print("Exiting...")
            break

        try:
            choice = int(choice)
            if 1 <= choice <= len(handles) - 1:
                handle = handles[choice]
                handle()
            else:
                print("Invalid option, please select again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to a menu option.")

        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()