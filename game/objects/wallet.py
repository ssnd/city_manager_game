from game import ConfigHandler, config as CONFIG
import logging

logger = logging.getLogger('game')


class Wallet(object):
    def __init__(self, game_save):
        self.game_save = game_save
        self.setup_game_saver()
        tile_config = ConfigHandler.open_config(CONFIG['tilemap_config'])
        self.tile_info = tile_config['tiles']

    @property
    def money(self):
        return self.game_save['money']

    def setup_game_saver(self):
        if self.game_save['money'] == {}:
            self.game_save['money'] = CONFIG['initial_money_available']

    def spend(self, amount):
        logger.info(f"Spending {amount} money.")
        self.game_save['money'] -= amount

    def add(self, amount):
        logger.info(f"Adding {amount} money to the wallet.")
        self.game_save['money'] += amount

    def get_income(self, tile_name):
        if 'income' in self.tile_info[tile_name].keys():
            return self.tile_info[tile_name]['income']
        return 0

    def get_price(self, tile_name):
        if 'price' in self.tile_info[tile_name].keys():
            return self.tile_info[tile_name]['price']
        return 0