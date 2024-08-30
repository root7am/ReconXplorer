import requests

def get_ip_info(ip):
    api_token = '66819ffdf72438' 
    url = f"https://ipinfo.io/{ip}?token={api_token}"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des informations de l'IP: {e}")
        return None
