import pygame
from pygame.locals import *

from game.builders.block_builder import BlockBuilder
from game.builders.block_director import BlockDirector
from game import config as CONFIG
from game.utils.config_handler import ConfigHandler
from game.utils.sprite_handler import SpriteHandler
import logging

from game.utils.text_box import TextBox

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
            logger.debug("Selected tile: {}".format(self.tile_name))
            logger.debug(f"income: {self.wallet.get_income(self.tile_name)}")
            self.mouse.select_block(self.tile_name)
            self.mouse.click_info = None

    def draw_tile(self, name, coords):
        self.rect = self.tile_director.create_cpanel_tile(name, (coords[0]+10, coords[1]+5))
        self.tile_name = name
        self.handle_click()
        self.surface.blit(self.button, (0, 0))


class ResetButton(object):
    def __init__(self, subsurf, mouse, grid):
        self.subsurface = subsurf
        self.mouse = mouse
        self.grid = grid
        self.color = (255, 0,0)
        self.surface = pygame.Surface((70, 300))
        self.surface.fill((255, 255, 255))
        self.text = TextBox(self.surface, align="center")
        self.text.text_color = (255, 255, 255)
        self.rect = None
        self.text.background_color = self.color

    def handle_click(self):
        if self.mouse.click_info and self.rect.collidepoint(self.mouse.click_info):
            logger.info("Resetting the grid")
            self.grid.reset_grid()

        self.mouse.click_info = None

    def draw(self):

        pygame.draw.rect(self.surface, self.color, (0, 0, 150, 30))
        self.text.set_margin_top(5)
        self.text.draw("RESET")
        self.rect = self.subsurface.blit(self.surface, (10, 565))
        self.handle_click()

class ControlPanel:
    def __init__(self, surface, mouse, wallet, grid):
        self.surface = surface
        self.grid = grid
        # TODO: get the data from the config file
        self.subsurface = pygame.Surface((100, 621))
        self.mouse = mouse
        self.reset_button = ResetButton(self.subsurface, self.mouse, self.grid)
        self.wallet = wallet
        self.last_press = 0

    def setup_subsurface(self):
        self.subsurface.fill((255, 255, 255))

    def draw(self):
        self.setup_subsurface()

        # TODO: add gamearea+tilemap margins config handling
        styles = CONFIG['styles']
        gamearea_margins = styles['game_area_margin']
        top = gamearea_margins['top']

        config = ConfigHandler.open_config(CONFIG['tilemap_config'])
        tiles = config['tiles']

        button = TileButton(self.subsurface, self.mouse, self.wallet)

        for i, tile in enumerate(tiles):
            coords = (0, 50*i)
            button.draw_tile(tile, coords)

        t = TextBox(self.subsurface, font_size=12)

        for i,tile in enumerate(tiles):
            t.position = (51, 15+i*50)
            t.draw("income: {}".format(self.wallet.get_income(tile)))
            t.position = (51, 30+i*50)
            t.draw("price: {}".format(self.wallet.get_income(tile)))

        self.reset_button.draw()

        t1 = TextBox(self.subsurface, font_size=20)
        t1.position = (10, 600)
        t1.draw("Money: {}".format(self.wallet.money))


        self.surface.blit(self.subsurface, (0, 30))

        # self.surface.blit()


