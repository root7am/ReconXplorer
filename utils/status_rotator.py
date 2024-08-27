import requests
import time
import threading
from pystyle import Colors

def get_headers(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }
    return headers

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def read_status_texts():
    print(f"\nEnter the statuses you want to set and type FIN when you're done:")
    status_texts = []
    index = 1
    
    while True:
        line = input(f'Status {index}: ')
        
        if line.upper() == "FIN":
            break
        
        status_texts.append(line)
        index += 1
    
    return status_texts

def get_user_id(token):
    headers = get_headers(token)
    try:
        r = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
        if r.status_code == 200:
            return r.json()['id']
        else:
            return None
    except Exception as e:
        print(f"Error getting user ID: {e}")
        return None

def change_status(token, text):
    headers = get_headers(token)
    setting = {
        'custom_status': {
            'text': text,
        },
    }
    try:
        r = requests.patch("https://discord.com/api/v10/users/@me/settings", headers=headers, json=setting)
        if r.status_code == 200:
            print(f'Token={token[:20]}... [SUCCESS]')
        else:
            print(f"Token={token[:20]}... [ERROR] ({r.status_code})")
    except Exception as e:
        print(f"Error changing status: {e}")

def status_changer():
    clear()
    
    token = input(f'Enter your token: ')
    
    status_texts = read_status_texts()
    
    while True:
        try:
            time_frequency = int(input(f'Time between each status change (in seconds): '))
            break
        except ValueError:
            print(f'Please enter an integer for the time.')
    
    user_id = get_user_id(token)
    if not user_id:
        print("Unable to retrieve user ID. Exiting.")
        return
        
    try:
        while True:
            for text in status_texts:
                change_status(token, text)
                time.sleep(time_frequency)
    except KeyboardInterrupt:
        print(f"\nStatus rotation interrupted.")

if __name__ == "__main__":
    status_changer()