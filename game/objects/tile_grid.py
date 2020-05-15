from game import config as CONFIG
import pygame
from collections import deque
from game.builders.block_builder import BlockBuilder
from game.builders.block_director import BlockDirector
# from deepcopy import copy
import logging

from game.checkers.CheckTiles import CheckTiles

logger = logging.getLogger('game')


WIDTH = CONFIG['screen']['width']
HEIGHT = CONFIG['screen']['height']
TILE_COUNT_X = CONFIG['tile']['tile_count_x']
TILE_COUNT_Y = CONFIG['tile']['tile_count_y']
TILE_WIDTH = CONFIG['tilemap']['width'] / TILE_COUNT_X
TILE_HEIGHT = CONFIG['tilemap']['height'] / TILE_COUNT_Y


class TileGrid:

    def __init__(self, surface, mouse, wallet, game_save):
        self.game_save = game_save
        self.wallet = wallet
        self.surface = surface
        self.mouse = mouse
        self.rect = None
        self.blocks = game_save['created_blocks']

    def handle_click(self):
        if self.mouse.click_info and self.rect.collidepoint(self.mouse.click_info):
            new_block = self.mouse.selectedBlock.copy()
            self.build_block(new_block)
            self.mouse.click_info = None

    def build_block(self, new_block):

        if new_block == {}:
            logger.info("You haven't selected a block")
            return

        x = int((self.mouse.click_info[0] - self.rect.x)/TILE_WIDTH)
        y = int((self.mouse.click_info[1] - self.rect.y)/TILE_HEIGHT)

        new_block['ticks_created'] = pygame.time.get_ticks()
        if (self.wallet.money - self.wallet.get_price(new_block['name'])) < 0:
            logger.info("You don't have enough money to buy that.")
            return

        self.blocks[(x, y)] = new_block


        self.game_save['created_blocks'] = self.blocks
        self.wallet.spend(self.wallet.get_price(new_block['name']))
        logger.debug("Building new tile: {}".format(new_block))

    def draw(self):
        subsurface = pygame.Surface((CONFIG['tilemap']['width'],
                                          CONFIG['tilemap']['height']
                                        ))
        subsurface.fill((255, 255, 255))

        builder = BlockBuilder(subsurface,
                               self.mouse,
                               TILE_WIDTH,
                               TILE_HEIGHT,
                               wallet=self.wallet)

        tile_director = BlockDirector(builder)
        tile_checker = CheckTiles(self.blocks)

        for x in range(TILE_COUNT_X):
            for y in range(TILE_COUNT_Y):
                x_coord = x * TILE_WIDTH
                y_coord = y * TILE_HEIGHT
                coords = (x_coord, y_coord)

                if (x, y) in self.blocks.keys():
                    # tile_checker.check(x,y)
                    new_block = self.blocks[(x, y)]
                    name, type, time = new_block['name'], new_block['type'], new_block['ticks_created']
                    self.blocks[(x,y)] = tile_director.create_tile(name, type, coords, time)
                    # print(self.blocks[(x,y)]['ticks_created'])
                else:
                    new_block = {
                        "name": "cobblestone",
                        "type" : "main",
                        "ticks_created" : pygame.time.get_ticks()
                    }
                    self.blocks[(x,y)] = new_block
                    name, type, time = new_block.values()
                    tile_director.create_tile(name, type, coords, time)

        self.rect = self.surface.blit(subsurface, (110, 10))

        self.handle_click()
