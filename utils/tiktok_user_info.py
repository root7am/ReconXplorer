from bs4 import BeautifulSoup

import requests
import json
from datetime import datetime


def get_tiktok_user_info(username) -> dict:
    """Fetch TikTok user information using requests and BeautifulSoup."""
    
    url = f'https://www.tiktok.com/@{username}'
    
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
        'accept-language': 'en-GB'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('tiktok2.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    
    script = soup.find('script', {'id': '__UNIVERSAL_DATA_FOR_REHYDRATION__'})
    data:dict = json.loads(script.text)['__DEFAULT_SCOPE__']['webapp.user-detail']
    
    return data.get('userInfo')

def main():
    """Main function to handle user input and display TikTok user information."""
    username = input("Enter the TikTok username: ").strip()
    print() # Add a new line
    
    if not username:
        print("Username cannot be empty.")
        return
    
    data = get_tiktok_user_info(username)
    
    if data is None:
        print(f"Error: No user found with the username '{username}'.")
    else:
        user_data:dict = data.get('user', {})
        stats:dict = data.get('stats', {})
        
        print("TikTok User Information:")
        print(f"Username: {user_data.get('uniqueId')}")
        print(f'Nickname: {user_data.get("nickname")}')
        print(f'User ID: {user_data.get("id")}')
        print(f'Description: {user_data.get("signature")}')
        print(f'Creation Date: {datetime.fromtimestamp(user_data.get("createTime")).strftime("%d-%m-%Y at %H:%M:%S")}')
        print(f'Region: {user_data.get("region")}')
        print(f'Language: {user_data.get("language")}')
        print(f'Friends: {stats.get("friendCount"):,}')
        print(f'Followers: {stats.get("followerCount"):,}')
        print(f'Following: {stats.get("followingCount"):,}')
        print(f'Hearts: {stats.get("heartCount"):,}')
        print(f'Videos: {stats.get("videoCount"):,}')
        print(f'Verified: {user_data.get("verified")}')
        print(f'Private Account: {user_data.get("secret")}')
        print(f'Open favorite: {user_data.get("openFavorite")}')


if __name__ == "__main__":
    main()
