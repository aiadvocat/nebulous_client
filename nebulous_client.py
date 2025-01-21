import requests
import argparse
import time
import sys
import os
from typing import Optional

# Add ANSI escape codes for formatting
RED_ITALIC = "\033[3;31m"  # Red and italic
RED = "\033[31m"  # Red
PINK = "\033[95m"  # Pink
GREEN = "\033[32m"  # Green
RESET = "\033[0m"  # Reset formatting

WELCOME_ART = r"""
 _   _ _____ ____  _   _ _     ___  _   _ ____  
| \ | | ____| __ )| | | | |   / _ \| | | / ___| 
|  \| |  _| |  _ \| | | | |  | | | | | | \___ \ 
| |\  | |___| |_) | |_| | |__| |_| | |_| |___) |
|_| \_|_____|____/ \___/|_____\___/ \___/|____/ 
"""

class NebulousClient:
    def __init__(self, api_key: str, api_url: str = "https://nebulous.dev.straiker.ai/api/chat"):
        self.api_url = api_url
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json"
        }

    def send_message(self, message: str) -> Optional[str]:
        try:
            payload = {
                "message": message,
                "apiKey": self.api_key
            }
            response = requests.post(self.api_url, json=payload, headers=self.headers)
            response.raise_for_status()
            
            response_data = response.json()
            message = response_data.get('message', '')
            annotation = response_data.get('message_annotation', '')
            
            if annotation:
                return f"{message}\n{RED_ITALIC}{annotation}{RESET}"
            return message
            
        except requests.exceptions.RequestException as e:
            print(f"Error sending message: {e}", file=sys.stderr)
            return None

def process_file_input(client: NebulousClient, filename: str, delay: float):
    try:
        with open(filename, 'r') as file:
            for line in file:
                prompt = line.strip()
                if prompt:  # Skip empty lines
                    print(f"\nPrompt: {prompt}")
                    response = client.send_message(prompt)
                    if response:
                        print(f"Response: {response}")
                    time.sleep(delay)  # Wait between requests
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
    except Exception as e:
        print(f"Error processing file: {e}", file=sys.stderr)

def interactive_mode(client: NebulousClient):
    print(WELCOME_ART)
    print(f"{RED}The Secure AI Challenge{RESET}")
    print(f"\n{PINK}Nebulous{RESET} Interactive Mode (Press Ctrl+C to exit)")
    try:
        while True:
            prompt = input(f"\n{GREEN}You{RESET}: ").strip()
            if prompt:
                response = client.send_message(prompt)
                if response:
                    print(f"{PINK}Nebulous{RESET}: {response}")
    except KeyboardInterrupt:
        print("\nExiting...")

def main():
    parser = argparse.ArgumentParser(description="Nebulous CLI Client")
    parser.add_argument("-f", "--file", help="Input file containing prompts (one per line)")
    parser.add_argument("-d", "--delay", type=float, default=1.0,
                        help="Delay between prompts in seconds when reading from file (default: 1.0)")
    parser.add_argument("-k", "--api-key", help="API key for the chatbot service")
    
    args = parser.parse_args()

    # Get API key from command line argument or environment variable
    api_key = args.api_key or os.environ.get("NEBULOUS_API_KEY")
    if not api_key:
        print("Error: API key must be provided either through --api-key argument or NEBULOUS_API_KEY environment variable",
              file=sys.stderr)
        sys.exit(1)

    client = NebulousClient(api_key=api_key)

    if args.file:
        process_file_input(client, args.file, args.delay)
    else:
        interactive_mode(client)

if __name__ == "__main__":
    main() 