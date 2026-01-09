import webbrowser

class Colors:
    purple = '\033[95m'
    reset = '\033[0m'
    red = '\033[91m'
    white = '\033[97m'
    info = '\033[94m'

def ErrorModule(exception):
    print(f"Error importing module: {exception}")

def ErrorId():
    print(f"Invalid ID. Please enter a valid integer.")

def Error(exception):
    print(f"An error occurred: {exception}")

def Continue():
    input(f"Press Enter to continue...")

def Reset():
    print(f"")

def main():
    try:
        try:
            IdBot = int(input(f"\nID bot -> "))
        except ValueError:
            ErrorId()
            return

        URLBot = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'

        print(f"URL bot: \"{Colors.white}{URLBot}\"")

        choice = input(f"Open the Internet? (y/n) -> ")
        if choice.lower() in ['y', 'yes']:
            webbrowser.open_new_tab(URLBot)
            Continue()
            Reset()
        else:
            Continue()
            Reset()
    except Exception as e:
        Error(e)

if __name__ == "__main__":
    main()