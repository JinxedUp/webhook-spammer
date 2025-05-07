import requests
import time
import os
from colorama import Fore, Back, Style, init

os.system("cls")
print(Fore.RED + """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                            """)


spam = True
webhook_url = input("Webhook url:")

message = input("message: ")
username = input("username: ")
delay = float(input("delay: "))

data = {
    "content": message,
    "username": username
}



while spam == True:
    response = requests.post(webhook_url, json=data)
    time.sleep(delay)

    if response.status_code == 200:
        print("message sent")
    elif response.status_code == 429:
        print("ratelimited, waiting 5 seconds")
    elif response.status_code == 204:
        print("message sent")
    else:
        print(f"failed to send message due to unknown error {response.status_code}")

