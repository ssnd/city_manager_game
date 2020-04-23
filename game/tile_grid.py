from game.config import config as CONFIG
import pygame
from game.builders.block_builder import BlockBuilder
from game.block_director import BlockDirector


class TileGrid:
    WIDTH = CONFIG['screen']['width']
    HEIGHT = CONFIG['screen']['height']
    TILE_COUNT_X = CONFIG['tile']['tile_count_x']
    TILE_COUNT_Y = CONFIG['tile']['tile_count_y']
    TILE_MARGIN = CONFIG['styles']['tilemap_margin']

    def __init__(self, surface):
        self.surface = surface

    def draw(self):
        GAME_AREA_WIDTH = self.WIDTH-self.TILE_MARGIN*2
        GAME_AREA_HEIGHT = self.HEIGHT-self.TILE_MARGIN*2

        pygame.draw.rect(self.surface, (0, 255, 0),
                         (self.TILE_MARGIN,
                          self.TILE_MARGIN,
                          GAME_AREA_WIDTH,
                          GAME_AREA_WIDTH))

        tile_width = GAME_AREA_WIDTH / self.TILE_COUNT_X
        tile_height = GAME_AREA_HEIGHT / self.TILE_COUNT_Y

        builder = BlockBuilder(self.surface, tile_width, tile_height)
        tile_director = BlockDirector(builder)

        for x in range(self.TILE_COUNT_X):
            for y in range(self.TILE_COUNT_Y):

                x_coord = self.TILE_MARGIN + x*(tile_width)
                y_coord = self.TILE_MARGIN + y*(tile_height)

                # this has to be replaced by some smart map handling
                if (x == 5 and y == 0) or (x == 2 and y == 4):
                    tile_director.create_clay_tile(x_coord, y_coord)
                else:
                    tile_director.create_grass_tile(x_coord, y_coord)
