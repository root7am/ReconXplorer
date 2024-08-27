import requests
import threading
import os
from pystyle import Colors

DEFAULT_REPORT_REASON = "Inappropriate content" 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def MassReport(token, guild_id, channel_id, message_id, reason):
    for _ in range(500):
        threading.Thread(target=Report, args=(token, guild_id, channel_id, message_id, reason)).start()

def Report(token, guild_id, channel_id, message_id, reason):
    url = 'https://discordapp.com/api/v8/report'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Content-Type': 'application/json',
        'Authorization': token
    }
    payload = {
        'channel_id': channel_id,
        'message_id': message_id,
        'guild_id': guild_id,
        'reason': reason
    }

    response = requests.post(url, json=payload, headers=headers)
    
    status = response.status_code
    response_message = response.json().get('message', 'Unknown error')

    if status == 201:
        print("Report successfully sent!\n")
    elif status in (401, 403):
        print(f"{response_message}\n")
    else:
        print(f"Error: {response_message} | Status Code: {status}\n")

if __name__ == "__main__":
    clear()
    token = input(f"Enter your Discord token: ")
    guild_id = input(f"Enter the server ID: ")
    channel_id = input(f"Enter the channel ID: ")
    message_id = input(f"Enter the message ID: ")
    
    reason = input(f"Enter the report reason (default: {DEFAULT_REPORT_REASON}): ").strip()
    if not reason:
        reason = DEFAULT_REPORT_REASON

    MassReport(token, guild_id, channel_id, message_id, reason)