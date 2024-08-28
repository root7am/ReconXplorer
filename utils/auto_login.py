import requests
import time
from pystyle import Colors
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def autologintitle():
    print(f"{Colors.purple}Auto Login - Discord{Colors.reset}")

def main():
    clear()
    
    entertoken = input(f"Enter the token: ")
    
    validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': entertoken, 'Content-Type': 'application/json'})
    if validityTest.status_code != 200:
        print(f"\nInvalid token")
        input(f"Press ENTER to exit")
        return
    
    try:
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        driver.get('https://discord.com/login')
        
        js = ('function login(token) {'
              'setInterval(() => {'
              'document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);'
              'setTimeout(() => {location.reload();}, 500);}')
        
        time.sleep(3)
        driver.execute_script(js + f'login("{entertoken}")')
        time.sleep(10)
        
        if driver.current_url == 'https://discord.com/login':
            clear()
            autologintitle()
            print(f"Connection Failed")
            driver.close()
        else:
            clear()
            autologintitle()
            print(f"Connection Established")
        
        input(f"Press ENTER to exit")
    
    except Exception as e:
        print(f"A problem occurred: {e}")
        time.sleep(2)
        clear()

if __name__ == "__main__":
    main()