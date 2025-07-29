import base64
import time
import sys
import random


# Define ANSI color codes
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


SECRET_WORDS = ["姐姐我喜欢你", "嫣嫣我爱你"]


def show_secret():
    # select one message secretly!
    secret_message_index = random.randint(0, len(SECRET_WORDS) - 1)
    secret_message = SECRET_WORDS[secret_message_index]
    encoded_message = base64.b64encode(secret_message.encode("utf-8")).decode("utf-8")

    print(f"{Colors.CYAN}Initiating secure transmission protocol...{Colors.RESET}")
    time.sleep(1)
    print(f"{Colors.CYAN}...{Colors.RESET}")
    time.sleep(1)
    print(f"{Colors.CYAN}Encoding message for privacy...{Colors.RESET}")
    time.sleep(1)

    print(f"\n{Colors.YELLOW}{Colors.BOLD}Encrypted Transmission:{Colors.RESET}")
    for char in encoded_message:
        sys.stdout.write(
            f"{Colors.YELLOW}{char}{Colors.RESET}"
        )  # Encoded message in yellow
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")
    time.sleep(2)

    print(f"{Colors.BLUE}Decryption sequence initiated...{Colors.RESET}")
    time.sleep(1)
    print(f"{Colors.BLUE}...{Colors.RESET}")
    time.sleep(1)
    print(f"{Colors.GREEN}Message authentication successful!{Colors.RESET}")
    time.sleep(1)

    decoded_message = base64.b64decode(encoded_message.encode("utf-8")).decode("utf-8")

    print(f"\n{Colors.MAGENTA}{Colors.BOLD}-- Decrypted Message --{Colors.RESET}")
    for char in decoded_message:
        sys.stdout.write(f"{Colors.RED}{char}{Colors.RESET}")  # Decoded message in red
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")
    time.sleep(1)

    print(f"{Colors.GREEN}Transmission complete. ❤️{Colors.RESET}")


if __name__ == "__main__":
    show_secret()
