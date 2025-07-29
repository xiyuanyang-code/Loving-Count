import json
import os
import sys
import random

sys.path.append(os.getcwd())

from src.logging_config import setup_logging_config
from src.secret import show_secret
from typing import List, Dict

logger = setup_logging_config()

# ---- utils functions


def search_block(target_name, data_blocks: List[Dict]):
    for data_block in data_blocks:
        if data_block["name"] == target_name:
            return data_block

    logger.warning("Error, invalid user name")


# ---- utils functions end


class RecordBot:
    def __init__(self, data_path="./data/data.json", egg=0):
        self.data_path = data_path
        self.egg = egg
        self.load_json()

    def load_json(self):
        with open(self.data_path, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def show_score(self, name=None):
        name = str(name) if name is not None else None
        if name is None:
            # default mode, show all the number
            show_data = self.data
        elif name == "1" or name == "yanyan":
            show_data = search_block("yanyan", self.data)
        elif name == "0" or name == "xiaoyuan":
            show_data = search_block("xiaoyuan", self.data)
        else:
            logger.warning("WARNING, invalid user name")
            show_data = self.data

        output_string = json.dumps(
            show_data, ensure_ascii=False, sort_keys=True, indent=4
        )
        print(output_string)
        return output_string

    def add_score(self, user, number):
        match str(user):
            case "yanyan" | "1":
                self._add_score("yanyan", number)
            case "xiaoyuan" | "0":
                self._add_score("xiaoyuan", number)
            case _:
                print("error")
        # save back to json
        with open(self.data_path, "w") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False, sort_keys=True)
        # update self.data
        self.load_json()

        # add random module
        rand_number = random.randint(1, 100) % 2
        if rand_number == 1:
            self.show_egg()

    def _add_score(self, user, number):
        block = search_block(user, self.data)
        if block is not None and isinstance(block.get("score", None), int):
            block["score"] += number
        else:
            logger.warning(f"User {user} not found or score type error.")

    def show_egg(self):
        if self.egg == 520:
            show_secret()


if __name__ == "__main__":
    test = RecordBot(egg=520)
    # print(test.show_score())
    # test.add_score(user="xiaoyuan", number=2)
    test.add_score(1, 100)
    # print(test.show_score())
