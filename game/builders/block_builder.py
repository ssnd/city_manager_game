from game.builders.abstract_builder import Builder
from game.objects.tile import Tile
from game.utils.sprite_handler import SpriteHandler
import pygame
from game.config import config as CONFIG


class BlockBuilder(Builder):

    def __init__(self, surface, tile_width, tile_height):
        self.surface = surface
        # self.set_coords(None, None)
        self.set_size(tile_width, tile_height)
        self.sprite_handler = SpriteHandler(CONFIG['tilemap_config'])
        self.subsurface = None

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def set_size(self, tile_width, tile_height):
        self.tile_width = tile_width
        self.tile_height = tile_height

    def set_color(self, color):
        self.color = color

    def set_tile(self, tile_name):
        tile_surf = self.sprite_handler.get_tile_by_name(tile_name)
        self.subsurface = tile_surf

    def render(self) -> Tile:
        TILE_WIDTH = int(CONFIG['screen']['width'] /
                         CONFIG['tile']['tile_count_x'])

        TILE_HEIGHT = int(CONFIG['screen']['height'] /
                          CONFIG['tile']['tile_count_y'])

        self.subsurface = pygame.transform.scale(self.subsurface,
                                                 (TILE_WIDTH, TILE_HEIGHT))

        tile = Tile(self.x, self.y, self.tile_width, self.tile_height)
        self.surface.blit(self.subsurface, tile)

        # pygame.draw.rect(self.surface, self.color, tile)

        return tile
