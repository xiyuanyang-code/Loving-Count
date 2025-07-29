import json
import os
import sys
import random

sys.path.append(os.getcwd())

from src.logging_config import setup_logging_config
from src.secret import show_secret
from typing import List, Dict, Optional, Any

logger = setup_logging_config()


def search_block(
    target_name: str, data_blocks: List[Dict[str, Any]]
) -> Optional[Dict[str, Any]]:
    """
    Search for a user block by name in the data blocks.

    Args:
        target_name (str): The name of the user to search for.
        data_blocks (List[Dict]): The list of user data blocks.

    Returns:
        Optional[Dict]: The user data block if found, else None.
    """
    for data_block in data_blocks:
        if data_block.get("name") == target_name:
            return data_block
    logger.warning(
        f"Error: Invalid user name '{target_name}' not found in data blocks."
    )
    return None


class RecordBot:
    """
    RecordBot handles user score management and secret egg feature.

    Attributes:
        data_path (str): Path to the JSON data file.
        egg (int): Secret egg trigger value.
        data (List[Dict]): Loaded user data.
    """

    def __init__(self, data_path: str = "./data/data.json", egg: int = 0):
        """
        Initialize RecordBot and load user data.

        Args:
            data_path (str): Path to the JSON data file.
            egg (int): Secret egg trigger value.
        """
        self.data_path = data_path
        self.egg = egg
        self.data = []
        self.load_json()

    def load_json(self) -> None:
        """
        Load user data from the JSON file.
        """
        try:
            with open(self.data_path, "r", encoding="utf-8") as file:
                self.data = json.load(file)
            logger.info(f"Loaded data from {self.data_path}")
        except FileNotFoundError:
            logger.error(f"Data file not found: {self.data_path}")
            self.data = []
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}")
            self.data = []
        except Exception as e:
            logger.error(f"Unexpected error loading JSON: {e}")
            self.data = []

    def show_score(self, name: Optional[str] = None) -> str:
        """
        Show the score for all users or a specific user.

        Args:
            name (Optional[str]): The user name or ID to show score for.

        Returns:
            str: JSON string of the score data.
        """
        name = str(name) if name is not None else None
        try:
            if name is None:
                show_data = self.data
            elif name == "1" or name == "yanyan":
                show_data = search_block("yanyan", self.data)
            elif name == "0" or name == "xiaoyuan":
                show_data = search_block("xiaoyuan", self.data)
            else:
                logger.warning(f"WARNING: Invalid user name '{name}'")
                show_data = self.data

            output_string = json.dumps(
                show_data, ensure_ascii=False, sort_keys=True, indent=4
            )
            print(output_string)
            logger.info(f"Displayed score for '{name if name else 'all'}'")
            return output_string
        except Exception as e:
            logger.error(f"Error showing score: {e}")
            return "{}"

    def add_score(self, user: Any, number: int) -> None:
        """
        Add score to a user and save the data.

        Args:
            user (Any): The user name or ID.
            number (int): The score to add.
        """
        try:
            match str(user):
                case "yanyan" | "1":
                    self._add_score("yanyan", number)
                case "xiaoyuan" | "0":
                    self._add_score("xiaoyuan", number)
                case _:
                    logger.error(f"Error: Invalid user '{user}'")
                    print("error")
                    return

            with open(self.data_path, "w", encoding="utf-8") as file:
                json.dump(self.data, file, indent=4, ensure_ascii=False, sort_keys=True)
            logger.info(f"Score updated for user '{user}' by {number}")
            self.load_json()
            # see the updated data
            self.show_score()

            rand_number = random.randint(1, 100) % 2
            logger.debug(f"Random number for egg: {rand_number}")
            if rand_number == 1:
                self.show_egg()
        except Exception as e:
            logger.error(f"Error adding score: {e}")

    def _add_score(self, user: str, number: int) -> None:
        """
        Internal method to add score to a user block.

        Args:
            user (str): The user name.
            number (int): The score to add.
        """
        block = search_block(user, self.data)
        if block is not None and isinstance(block.get("score", None), int):
            block["score"] += number
            logger.info(f"Added {number} to '{user}', new score: {block['score']}")
        else:
            logger.warning(f"User '{user}' not found or score type error.")

    def show_egg(self) -> None:
        """
        Show the secret egg if the condition is met.
        """
        if self.egg == 520:
            logger.info("Egg triggered! Showing secret.")
            show_secret()
        else:
            logger.debug("Egg not triggered.")


if __name__ == "__main__":
    test = RecordBot(egg=520)
    try:
        test.add_score(1, 100)
    except Exception as e:
        logger.error(f"Error in main: {e}")
