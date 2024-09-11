import requests
import json
import time
import os
import http.server
import socketserver
import threading
from platform import system
import random

# Server handler for GET request
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"RAFAY XD HERE")

# Function to execute the server
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
        
# Clear the terminal based on OS
def cls():
    if system() == 'Linux' or system() == 'Darwin':
        os.system('clear')
    elif system() == 'Windows':
        os.system('cls')

# Constants for colors and formatting
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;31m'
RESET = '\033[0m'
BLUE = "\033[1;34m"
WHITE = "\033[1;37m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
GREEN = "\033[1;32m"
BOLD = '\033[1;1m'

# Function to display logo
def logo():
    clear = "\x1b[0m"
    colors = [31, 34, 36]

    x = """
.------..------..------..------..------..------.
|R.--. ||A.--. ||F.--. ||F.--. ||A.--. ||Y.--. |
| :/\: || :/\: || (\/) || :(): || :/\: || (\/) |
| :\/: || (__) || :\/: || ()() || :\/: || :\/: |
| '--'R|| '--'A|| '--'F|| '--'F|| '--'A|| '--'Y|
`------'`------'`------'`------'`------'`------'
"""
    for N, line in enumerate(x.split("\n")):
        print(f"\x1b[1;{random.choice(colors)}m{line}{clear}")
        time.sleep(0.05)

logo()

# Function to display venom banner
def venom():
    clear = "\x1b[0m"
    colors = [32, 33, 34]

    y = '''
<><><><><><><><><><><><><><><><><><><><><><><>\n
* Name   : L3G3ND RAFAY
* Facebook   : https://www.facebook.com/Rafay Khan
<><><><><><><><><><><><><><><><><><><><><><><>\n
'''
    for N, line in enumerate(y.split("\n")):
        print(f"\x1b[1;{random.choice(colors)}m{line}{clear}")
        time.sleep(0.05)

venom()

# Function to print the lines
def liness():
    print('\x1b[92m\033[1;33m•❥═════════❥•OWNER•❥═════════❥•RAFAY•❥═════════❥•XD•❥═════════❥•')

# Function to send messages
def send_message():
    # Get user inputs
    thread_id = input(f"{GREEN}ENTER CONVO ID: {RESET}")
    haters_name = input(f"{GREEN}ENTER HATER NAME: {RESET}")
    speed = int(input(f"{GREEN}ENTER TIME DELAY (in seconds): {RESET}"))
    token_file = input(f"{GREEN}ENTER TOKEN FILE PATH: {RESET}")
    txt_file = input(f"{GREEN}ENTER MESSAGE FILE PATH: {RESET}")

    cls()

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    try:
        # Read access tokens and messages from files
        with open(token_file, 'r') as file:
            tokens = file.readlines()
            access_tokens = [token.strip() for token in tokens]

        with open(txt_file, 'r') as file:
            messages = file.readlines()

        # Determine the minimum number of tokens or messages to loop through
        num_tokens = len(access_tokens)
        num_messages = len(messages)
        max_tokens = min(num_tokens, num_messages)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    while True:
        try:
            # Loop through the messages
            for message_index in range(num_messages):
                # Get the corresponding token for the message
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                # Build the API request URL
                url = f"https://graph.facebook.com/v17.0/t_{thread_id}/"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}

                # Send the request
                response = requests.post(url, json=parameters, headers=headers)

                # Log the result
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(f"{BLUE}[+] Message {message_index + 1} of Convo {thread_id} sent by Token {token_index + 1}: {haters_name} {message}")
                    print(f"  - Time: {current_time}\n")
                    liness()
                else:
                    print(f"{RED}[x] Failed to send Message {message_index + 1} of Convo {thread_id} with Token {token_index + 1}: {haters_name} {message}")
                    print(f"  - Time: {current_time}\n")
                    liness()

                # Sleep before sending the next message
                time.sleep(speed)

            print(f"{GREEN}\n[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print(f"[!] An error occurred: {e}")
            time.sleep(30)  # Retry after a delay

send_message()
