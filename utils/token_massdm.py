import json
import requests
import os
import threading
from pystyle import Colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title(title):
    print(f"{'=' * 60}\n{title}\n{'=' * 60}")

def print_error(message):
    print(f"Error: {message}")

def print_info(message):
    print(f"{message}")

def get_dm_channel_ids(token_discord):
    try:
        response = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token_discord})
        
        if response.status_code == 200:
            channels = response.json()
            dm_channel_ids = [channel['id'] for channel in channels if channel['type'] == 1]
            return dm_channel_ids
        else:
            print_error(f"Status code {response.status_code}: Unable to fetch DM channels.")
            return []

    except Exception as e:
        print_error(f"Error fetching DM channel IDs: {e}")
        return []

def save_ids_to_json(dm_channel_ids, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(dm_channel_ids, f, indent=4)
        print_info(f"Saved all DM channel IDs to {filename}.")
    except Exception as e:
        print_error(f"Error saving IDs to JSON: {e}")

def MassDM(token_discord, dm_channel_ids, message):
    try:
        for channel_id in dm_channel_ids:
            response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",
                                     headers={'Authorization': token_discord, 'Content-Type': 'application/json'},
                                     json={"content": message})
            if response.status_code == 200:
                print_info(f"Message sent to channel ID: {channel_id}")
            else:
                print_error(f"Status code {response.status_code}: Unable to send message to channel ID: {channel_id}")

    except Exception as e:
        print_error(f"Error sending message: {e}")

def execute_mass_dm():
    try:
        clear()
        token_discord = input(f"Enter your Discord token: ").strip()
        message = input(f"Enter the message to send: ").strip()
        output_file = "dm_channel_ids.json"

        dm_channel_ids = get_dm_channel_ids(token_discord)

        if not dm_channel_ids:
            print_error("No DM channel IDs collected. Exiting.")
            return

        save_ids_to_json(dm_channel_ids, output_file)
        print_info(f"Total DM channel IDs collected: {len(dm_channel_ids)}")

        proceed = input(f"Do you want to send the message to all collected DM channels? (y/n): ").strip().lower()

        if proceed == 'y':
            for channel_id in dm_channel_ids:
                t = threading.Thread(target=MassDM, args=(token_discord, [channel_id], message))
                t.start()
                t.join()
                print_info(f"Finished sending messages to channel {channel_id}.")
        else:
            print_info("Exiting without sending messages.")

        input(f"Press Enter to return to the main menu...")

    except Exception as e:
        print_error(f"Error: {e}")

def display_menu():
    clear()
    menu = f"""
1. Mass DM to Discord Channels
2. Exit
    """
    print(menu)

def handle_menu_choice(choice):
    if choice == '1':
        execute_mass_dm()
    elif choice == '2':
        print_info("Exiting program.")
        exit(0)
    else:
        print_error("Invalid choice. Please enter a valid option.")

def run_menu():
    while True:
        display_menu()
        choice = input(f"Enter your choice: ").strip()

        handle_menu_choice(choice)

if __name__ == "__main__":
    run_menu()