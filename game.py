#! ./venv/bin/python3
from game.game_manager import GameManager
import logging


if __name__ == "__main__":
    logger = logging.getLogger('game')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s:%(message)s')

    ch.setFormatter(formatter)

    logger.addHandler(ch)
    logger.info('Starting the application...')

    gm = GameManager()
    gm.start()
