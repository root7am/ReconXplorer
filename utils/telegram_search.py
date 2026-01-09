import requests
from bs4 import BeautifulSoup
from pystyle import Colors, Colorate

def telegram_lookup():
    username = input(f"{Colors.purple}Enter Telegram Username (without @): {Colors.reset}")
    print(f"{Colors.purple}Fetching public profile...{Colors.reset}")
    try:
        r = requests.get(f"https://t.me/{username}")
        soup = BeautifulSoup(r.text, 'html.parser')
        name = soup.find("div", {"class": "tgme_page_title"})
        bio = soup.find("div", {"class": "tgme_page_description"})
        
        if name:
            info = f"""
            Public Profile: t.me/{username}
            Name          : {name.text.strip()}
            Bio           : {bio.text.strip() if bio else 'No bio available'}
            """
            print(Colorate.Color(Colors.purple, info, True))
        else:
            print(f"{Colors.red}Username not found or profile is private.")
    except:
        print(f"{Colors.red}Error loading data.")

telegram_lookup()