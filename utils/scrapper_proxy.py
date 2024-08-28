import random
import time
import os
import httpx

def main():
    pass

def save_proxies(proxies):
    with open("proxies.txt", "w") as file:
        file.write("\n".join(proxies))

def get_proxies():
    if os.path.exists('proxies.txt'):
        os.remove('proxies.txt')
    open('proxies.txt', 'a+').close()
    
    with open('proxies.txt', 'r', encoding='utf-8') as f:
        proxies = f.read().splitlines()
    
    if not proxies:
        proxy_log = {}
    else:
        proxy = random.choice(proxies)
        proxy_log = {
            "http://": f"http://{proxy}", 
            "https://": f"http://{proxy}"
        }
    
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"

    try:
        response = httpx.get(url, timeout=60)
        
        if response.status_code == 200:
            proxies = response.text.splitlines()
            save_proxies(proxies)
        else:
            time.sleep(1)
            get_proxies()
    except (httpx.HTTPStatusError, httpx.RequestError, httpx.NetworkError):
        time.sleep(1)
        get_proxies()

if __name__ == "__main__":
    main()
    get_proxies()