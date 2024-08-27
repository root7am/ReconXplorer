import requests
from pystyle import Colors

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def housechangertitle():
    print(f"{Colors.purple}HypeSquad House Changer{Colors.reset}")

def setTitle(title):
    print(f"{Colors.purple}{title}{Colors.reset}")

def main():
    clear()
    housechangertitle()
    setTitle("HypeSquad Changer")

    print(f"Which house do you want to be part of:\n\n01 Bravery\n02 Brilliance\n03 Balance\n\n")
    house = input(f"Enter your House choice: ")
    token = input(f"Enter the token: ")

    validityTest = requests.get('https://discord.com/api/v10/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if validityTest.status_code != 200:
        print(f"\nInvalid token")
        input(f"\nPress ENTER to exit...")
        return  
    
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    
    if house == "1":
        payload = {'house_id': 1}
    elif house == "2":
        payload = {'house_id': 2}
    elif house == "3":
        payload = {'house_id': 3}
    else:
        print(f"Invalid Choice")
        input(f"\nPress ENTER to exit...")
        return 

    r = requests.post('https://discord.com/api/v10/hypesquad/online', headers=headers, json=payload, timeout=10)
    if r.status_code == 204:
        print(f"\nHypesquad House changed")
    else:
        print(f"\nAn error occurred, please retry")
    
    input(f"\nPress ENTER to exit")

if __name__ == "__main__":
    main()