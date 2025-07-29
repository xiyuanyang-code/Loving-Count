import argparse
import os
import sys

sys.path.append(os.getcwd())

from src.logging_config import setup_logging_config
from src.record import RecordBot

logger = setup_logging_config()


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Command")
    args = parser.parse_args()
    command: str = args.command
    return command.strip()


def main():
    _command = parse_argument()
    seed = 0
    match _command.split():
        case [command]:
            print(f"getting command: {command}")
        case [command, user, number]:
            number = int(number)
            print(
                f"Getting command: {"adding" if number > 0 else "cutting"} score {number} to user: {user}"
            )
        case [command, egg]:
            seed = egg
        case _:
            "Invalid request"
    record_bot = RecordBot(egg=seed)
    if command == "ls":
        record_bot.show_score()
    elif command == "add":
        record_bot.add_score(user, number)
    elif command == "egg":
        record_bot.show_egg()
    else:
        logger.warning("WARNING: invalid command type")


if __name__ == "__main__":
    main()
