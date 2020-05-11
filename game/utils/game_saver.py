import pickle
import os
import logging
import time

logger = logging.getLogger('game')


class GameSaver:
    def __init__(self, saved_game_file):
        self.saved_game_file = saved_game_file
        self.game_state = None

    def __setitem__(self, key, value):
        self.game_state[key] = value

    def __getitem__(self, key):
        if key in self.game_state.keys():
            return self.game_state[key]

        return {}

    def save_game(self):
        logger.info("Saving the game and exitting")
        with open(self.saved_game_file, "wb") as f:
            pickle.dump(self.game_state, f)

    def create_saved_game(self, fpath: str):
        new_saved_game_obj = {
            "time_created": time.ctime()
        }

        with open(fpath, 'wb') as f:
            pickle.dump(new_saved_game_obj, f)

        self.game_state = new_saved_game_obj


    def load_game(self):
        exists: bool = os.path.isfile(self.saved_game_file)

        if exists:
            logger.info(f"Opening the saved game file")
            with open(self.saved_game_file, "rb") as f:
                self.game_state = pickle.load(f)
        else:
            logger.info(f"Saved game file doesn't exist. Creating a new one.")
            self.create_saved_game(self.saved_game_file)


        return self
