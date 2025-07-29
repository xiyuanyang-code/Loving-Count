import argparse
import os
import sys

sys.path.append(os.getcwd())

from src.logging_config import setup_logging_config
from src.record import RecordBot

logger = setup_logging_config()


def parse_argument():
    """
    Parse command-line arguments.

    Returns:
        str: The command string entered by the user.
    """
    parser = argparse.ArgumentParser(description="Loving Count Command Line Tool")
    parser.add_argument("command", help="Command and arguments, e.g. 'add yanyan 10'")
    args = parser.parse_args()
    command: str = args.command
    logger.info(f"Parsed command: {command}")
    return command.strip()


def main():
    """
    Main entry point for the Loving Count CLI.

    Handles command parsing, error handling, and dispatches commands to RecordBot.
    """
    try:
        _command = parse_argument()
        seed = 0
        command = None
        user = None
        number = None

        parts = _command.split()
        logger.debug(f"Command parts: {parts}")

        if len(parts) == 1:
            command = parts[0]
            logger.info(f"Received single command: {command}")
        elif len(parts) == 3:
            command, user, number = parts
            try:
                number = int(number)
            except ValueError as e:
                logger.error(f"Invalid number argument: {number}. Error: {e}")
                print("Error: Number must be an integer.")
                return
            logger.info(f"Received command: {command}, user: {user}, number: {number}")
        elif len(parts) == 2:
            command, egg = parts
            try:
                seed = int(egg)
            except ValueError as e:
                logger.error(f"Invalid egg argument: {egg}. Error: {e}")
                print("Error: Egg must be an integer.")
                return
            logger.info(f"Received command: {command}, egg: {seed}")
        else:
            logger.error("Invalid request format.")
            print("Invalid request format.")
            return

        record_bot = RecordBot(egg=seed)
        if command == "ls":
            logger.info("Executing 'ls' command to show scores.")
            record_bot.show_score()
        elif command == "add":
            if user is None or number is None:
                logger.error("Missing user or number for 'add' command.")
                print("Error: 'add' command requires user and number.")
                return
            logger.info(f"Executing 'add' command for user: {user}, number: {number}")
            record_bot.add_score(user, number)
        elif command == "egg":
            logger.info("Executing 'egg' command to show secret egg.")
            record_bot.show_egg()
        else:
            logger.warning(f"WARNING: invalid command type '{command}'")
            print(f"Invalid command: {command}")
    except Exception as e:
        logger.error(f"Unhandled exception in main: {e}", exc_info=True)
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    """
    Run the Loving Count CLI tool.
    """
    main()
