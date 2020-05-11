from game import config as CONFIG
import pygame
from collections import deque
from game.builders.block_builder import BlockBuilder
from game.builders.block_director import BlockDirector
# from deepcopy import copy
import logging


logger = logging.getLogger('game')


WIDTH = CONFIG['screen']['width']
HEIGHT = CONFIG['screen']['height']
TILE_COUNT_X = CONFIG['tile']['tile_count_x']
TILE_COUNT_Y = CONFIG['tile']['tile_count_y']
TILE_WIDTH = CONFIG['tilemap']['width'] / TILE_COUNT_X
TILE_HEIGHT = CONFIG['tilemap']['height'] / TILE_COUNT_Y


class TileGrid:

    def __init__(self, surface, mouse, game_save):
        self.game_save = game_save
        self.surface = surface
        self.mouse = mouse
        self.rect = None
        self.blocks = game_save['created_blocks']

    def handle_click(self):
        if self.mouse.click_info and self.rect.collidepoint(self.mouse.click_info):
            self.build_block(self.mouse.selectedBlock.copy())
            self.mouse.click_info = None

    def build_block(self, new_block):
        x = int((self.mouse.click_info[0] - self.rect.x)/TILE_WIDTH)
        y = int((self.mouse.click_info[1] - self.rect.y)/TILE_HEIGHT)

        self.blocks[(x, y)] = new_block

        self.game_save['created_blocks'] = self.blocks

        logger.debug("Building new tile: {}".format(new_block))

    def draw(self):
        subsurface = pygame.Surface((CONFIG['tilemap']['width'],
                                          CONFIG['tilemap']['height']
                                        ))
        subsurface.fill((255, 255, 255))

        builder = BlockBuilder(subsurface,
                               self.mouse,
                               TILE_WIDTH,
                               TILE_HEIGHT)

        tile_director = BlockDirector(builder)

        for x in range(TILE_COUNT_X):
            for y in range(TILE_COUNT_Y):
                x_coord = x * TILE_WIDTH
                y_coord = y * TILE_HEIGHT
                coords = (x_coord, y_coord)

                if (x, y) in self.blocks.keys():
                    if x>0 and y>0 and x<15 and y<15:
                        if self.blocks[(x, y+1)] == self.blocks[(x, y)] == self.blocks[(x+1, y)] \
                                and self.blocks[(x,y)]['name'] == 'sidewalk':

                            self.blocks[(x, y)] = {
                                'name': 'sidewalk',
                                'type': "corner_tl"
                            }
                            self.blocks[(x, y+1)] = {
                                'name': 'sidewalk',
                                'type': "left"
                            }
                            self.blocks[(x+1, y)] = {
                                'name': 'sidewalk',
                                'type': "up"
                            }

                    new_block = self.blocks[(x, y)]
                    name, type = new_block['name'], new_block['type']
                    tile_director.create_tile(name, type, coords)

                else:
                    new_block = {
                        "name": "cobblestone",
                        "type" : "main"
                    }
                    self.blocks[(x,y)] = new_block
                    name, type = new_block.values()
                    tile_director.create_tile(name, type, coords)

        self.rect = self.surface.blit(subsurface, (110, 10))

        self.handle_click()
