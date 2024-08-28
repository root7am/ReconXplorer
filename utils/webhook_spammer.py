import requests
import time
import threading
from pystyle import Colors

def clear():
    print("\033c", end="")

def webhookspam():
    clear()
    webhook = input(f"WebHook Link: ")
    try:
        requests.post(webhook, json={'content': "Initial test message"})
    except:
        print(f"Your WebHook is invalid!")
        time.sleep(2)
        clear()
        return

    message = input(f"\nEnter the message to spam: ")
    amount = int(input(f"\nAmount of messages to send: "))
    
    def spam():
        try:
            requests.post(webhook, json={'content': message})
        except Exception as e:
            print(f"Error: {e}")

    for x in range(amount):
        threading.Thread(target=spam).start()
        time.sleep(0.1)
    
    print(f"Webhook has been correctly spammed")
    input(f"\nPress ENTER to exit")
    clear()

def main():
    webhookspam()

if __name__ == "__main__":
    main()