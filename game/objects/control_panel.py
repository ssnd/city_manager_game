import pygame
from pygame.locals import *

from game.builders.block_builder import BlockBuilder
from game.builders.block_director import BlockDirector
from game import config as CONFIG
from game.utils.config_handler import ConfigHandler
from game.utils.sprite_handler import SpriteHandler
import logging

logger = logging.getLogger('game')


class TileButton:
    def __init__(self, surface, mouse):
        self.surface = surface
        self.button = pygame.Surface((100, 600))
        self.mouse = mouse
        self.rect = None
        self.tile_name = None
        self.last_press = 0
        self.sprite_handler = SpriteHandler(CONFIG['tilemap_config'])
        builder = BlockBuilder(self.button, self.mouse, 40, 40)
        self.tile_director = BlockDirector(builder)
        self.button.fill((255, 255, 255))

    def handle_click(self):
        if self.mouse.click_info and self.rect.collidepoint(self.mouse.click_info):
            logger.debug("Selected tile: {}".format(self.tile_name))
            self.mouse.select_block(self.tile_name)
            self.mouse.click_info = None

    def draw_tile(self, name, coords):
        self.rect = self.tile_director.create_cpanel_tile(name, (coords[0]+10, coords[1]+5))
        self.tile_name = name

        self.handle_click()
        self.surface.blit(self.button, (0, 0))

class ControlPanel:
    def __init__(self, surface, mouse):
        self.surface = surface
        # TODO: get the data from the config file
        self.subsurface = pygame.Surface((100, 621))
        self.mouse = mouse
        self.last_press = 0

    def setup_subsurface(self):
        self.subsurface.fill((0, 0, 0))

    def draw(self):
        self.setup_subsurface()

        # TODO: add gamearea+tilemap margins config handling
        styles = CONFIG['styles']
        gamearea_margins = styles['game_area_margin']
        top = gamearea_margins['top']

        config = ConfigHandler.open_config(CONFIG['tilemap_config'])
        tiles = config['tiles']

        button = TileButton(self.subsurface, self.mouse)

        for i, tile in enumerate(tiles):
            coords = (50*(i%2), 50*int(i/2))
            button.draw_tile(tile, coords)

        self.surface.blit(self.subsurface, (0, 10))


