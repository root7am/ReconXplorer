import requests

def get_fivem_server_info(cfx_id):
    url = f"https://servers-frontend.fivem.net/api/servers/single/{cfx_id}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        server_info = response.json()

        data = {
            "Server Name": server_info.get('Data', {}).get('hostname', 'Unavailable'),
            "IP": server_info.get('Data', {}).get('connectEndPoints', ['Unavailable'])[0].split(':')[0],
            "Port": server_info.get('Data', {}).get('connectEndPoints', ['Unavailable'])[0].split(':')[1],
        }

        return data
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def main():
    cfx_id = input("Enter the CFX ID of the server: ")
    server_data = get_fivem_server_info(cfx_id)
    
    if "Error" in server_data:
        print(f"Error: {server_data['Error']}")
    else:
        print("Server Information:")
        for key, value in server_data.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
