from game import ConfigHandler, config as CONFIG
import logging

logger = logging.getLogger('game')

class Wallet(object):
    def __init__(self, game_save):
        self.money = 100
        tile_config = ConfigHandler.open_config(CONFIG['tilemap_config'])
        self.tile_info = tile_config['tiles']

    def spend(self, amount):
        logger.debug(f"Spending {amount} money.")
        self.money -= amount

    def add(self, amount):
        logger.debug(f"Adding {amount} money to the wallet.")
        self.money+=amount

    def get_income(self, tile_name):
        if 'income' in self.tile_info[tile_name].keys():
            return self.tile_info[tile_name]['income']
        return 0

    def get_price(self, tile_name):
        if 'price' in self.tile_info[tile_name].keys():
            return self.tile_info[tile_name]['price']
        return 0