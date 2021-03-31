import pygame

from game import config as CONFIG
from game.objects.reset_button import ResetButton
from game.objects.tile_button import TileButton
from game.utils.config_handler import ConfigHandler
import logging

from game.utils.text_box import TextBox

logger = logging.getLogger('game')


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
            t.draw(f"income: {self.wallet.get_income(tile)}")
            t.position = (51, 30+i*50)
            t.draw(f"price: {self.wallet.get_price(tile)}")

        self.reset_button.draw()

        t1 = TextBox(self.subsurface, font_size=20)
        t1.position = (10, 600)
        t1.draw(f"Money: {self.wallet.money}")

        self.surface.blit(self.subsurface, (0, 0))



