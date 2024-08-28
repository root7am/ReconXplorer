import os
import base64
from pystyle import Colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def decrypt_token():
    clear()
    userid = input(f"Discord ID : ")
    encoded_bytes = base64.b64encode(userid.encode("utf-8"))
    encoded_str = str(encoded_bytes, "utf-8")
    print(f'\nFIRST PART : {encoded_str}')

if __name__ == "__main__":
    decrypt_token()