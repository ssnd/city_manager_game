from game.config import config as CONFIG
import pygame
from collections import deque
from game.builders.block_builder import BlockBuilder
from game.builders.block_director import BlockDirector
import logging


logger = logging.getLogger('game')

class TileGrid:
    WIDTH = CONFIG['screen']['width']
    HEIGHT = CONFIG['screen']['height']
    TILE_COUNT_X = CONFIG['tile']['tile_count_x']
    TILE_COUNT_Y = CONFIG['tile']['tile_count_y']
    TILE_MARGIN = CONFIG['styles']['tilemap_margin']
    GAME_AREA_WIDTH = WIDTH-TILE_MARGIN['left']-TILE_MARGIN['right']
    GAME_AREA_HEIGHT = HEIGHT-TILE_MARGIN['top']-TILE_MARGIN['bottom']
    TILE_WIDTH = CONFIG['tilemap']['width'] / TILE_COUNT_X
    TILE_HEIGHT = CONFIG['tilemap']['height'] / TILE_COUNT_Y

    def __init__(self, surface, mouse):
        self.surface = surface
        self.mouse = mouse
        self.elements = []
        self.mouse_movements = deque([], maxlen=10)
        self.last_press = False
        self.rect = None
        self.blocks = {}
        self.subsurface = None

    def handle_click(self):
        if self.mouse.click_info and self.rect.collidepoint(self.mouse.click_info):
            self.build_block(self.mouse.selectedBlock)
            self.mouse.click_info = None

    def build_block(self, new_block_type):
        x = int((self.mouse.click_info[0] - self.rect.x)/self.TILE_WIDTH)
        y = int((self.mouse.click_info[1] - self.rect.y)/self.TILE_HEIGHT)

        new_tile = {
            "name": new_block_type,
        }

        self.blocks[(x,y)] = new_tile

        logger.debug("Building new tile: {}".format(new_block_type))

    def draw(self):
        self.subsurface = pygame.Surface((CONFIG['tilemap']['width'],
                                          CONFIG['tilemap']['height']
                                        ))
        self.subsurface.fill((255, 255, 255))

        builder = BlockBuilder(self.subsurface,
                               self.mouse,
                               self.TILE_WIDTH,
                               self.TILE_HEIGHT)

        tile_director = BlockDirector(builder)

        for x in range(self.TILE_COUNT_X):
            for y in range(self.TILE_COUNT_Y):
                x_coord = x * self.TILE_WIDTH
                y_coord = y * self.TILE_HEIGHT
                coords = (x_coord, y_coord)

                if (x, y) in self.blocks.keys():
                    new_block = self.blocks[(x, y)]
                    name = new_block['name']
                    tile_director.create_tile(name, coords)

                else:
                    new_block = {
                        "name": "cobblestone"
                    }
                    self.blocks[(x,y)] = new_block
                    tile_director.create_tile(new_block['name'], coords)

        self.rect = self.surface.blit(self.subsurface, (110, 10))

        self.handle_click()
