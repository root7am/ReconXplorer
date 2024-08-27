import subprocess
from emailrep import EmailRep
import re
from pystyle import Colors

def handle_error(error_message):
    print(f"Error: {error_message}")

def check_email_with_holehe(email):
    try:
        result = subprocess.run(['holehe', email, '--only-used'], capture_output=True, text=True)
        if result.returncode != 0:
            handle_error("An error occurred while running holehe")
            return

        output_lines = result.stdout.split('\n')

        print(f"\nResults from Holehe for email: {email}\n")
        for line in output_lines:
            match = re.match(r"\[\+\] Email used: .* on (.*)", line)
            if match:
                print(match.group(1))

    except Exception as e:
        handle_error(f"Error executing holehe: {str(e)}")

def get_email_information_with_emailrep(email):
    api = EmailRep()
    try:
        response = api.query(email)
        if response:
            print(f"\nResults from :")
            print(f"Email: {email}")
            if 'reputation' in response:
                print(f"Reputation: {response['reputation']}")
            else:
                print(f"Reputation: N/A")
                
            if 'details' in response:
                print(f"Details: {response['details']}")
                if 'sources' in response['details']:
                    print(f"Sources: {response['details']['sources']}")
                else:
                    print(f"Sources: N/A")
                print(f"Account creation date: {response['details'].get('date_creation', 'N/A')}")
                print(f"Last seen: {response['details'].get('last_seen', 'N/A')}")
                print(f"Days since last seen: {response['details'].get('days_since_last_seen', 'N/A')}")
                print(f"Blacklist status: {response['details'].get('blacklisted', 'N/A')}")
                print(f"Malicious status: {response['details'].get('malicious_activity', 'N/A')}")
            else:
                print(f"Details: N/A")
        else:
            print(f"No information found for {email}")
    except Exception as e:
        handle_error(f"Error querying : {str(e)}")

def main():
    email = input(f"Enter the email address: ")
    check_email_with_holehe(email)
    get_email_information_with_emailrep(email)

if __name__ == "__main__":
    main()