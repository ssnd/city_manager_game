import pygame

from game import config as CONFIG
from game.builders.block_builder import BlockBuilder
from game.builders.block_director import BlockDirector
# from game.objects.control_panel import logger
import logging
# from game import logger
from game.utils.sprite_handler import SpriteHandler
logger = logging.getLogger('game')

class TileButton:
    def __init__(self, surface, mouse, wallet):
        self.surface = surface
        self.button = pygame.Surface((100, 600))
        self.mouse = mouse
        self.wallet = wallet
        self.rect = None
        self.tile_name = None
        self.last_press = 0
        self.sprite_handler = SpriteHandler(CONFIG['tilemap_config'])
        builder = BlockBuilder(self.button, self.mouse, 40, 40)
        self.tile_director = BlockDirector(builder)
        self.button.fill((255, 255, 255))

    def handle_click(self):
        if self.mouse.click_info and self.rect.collidepoint(self.mouse.click_info):
            logger.info(f"Selected tile: {self.tile_name}")
            logger.info(f"Income: {self.wallet.get_income(self.tile_name)}, "
                         f"Price: {self.wallet.get_price(self.tile_name)}")
            self.mouse.select_block(self.tile_name)
            self.mouse.click_info = None

    def draw_tile(self, name, coords):
        self.rect = self.tile_director.create_cpanel_tile(name, (coords[0]+10, coords[1]+5))
        self.tile_name = name
        self.handle_click()
        self.surface.blit(self.button, (0, 0))