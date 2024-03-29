import itertools
from game.builders.abstract_builder import Builder
from game.objects.tile import Tile
from game.utils.sprite_handler import SpriteHandler
from game import config as CONFIG
import pygame
import logging

logger = logging.getLogger('game')


class BlockBuilder(Builder):

    def __init__(self, surface, mouse, tile_width, tile_height, wallet=None):
        self.surface = surface
        self.wallet = wallet
        self.mouse = mouse
        self.tile_width = int(tile_width)
        self.tile_height = int(tile_height)
        # self.set_size(tile_width, tile_height)
        self.sprite_handler = SpriteHandler(CONFIG['tilemap_config'])
        self.tile_subsurfaces = None
        self.subsurface = None
        self.subsurface_size = None
        self.tile = {}
        self.color = None
        self.tile_coords = None
        self.x, self.y = None, None
        self.tile_name = None
        self.time = 0

    def set_time(self, time):
        self.time = time

    def set_coords(self, coords: tuple):
        self.x, self.y = coords

    def set_color(self, color):
        self.color = color

    def set_size(self, size):
        self.tile_width, self.tile_height = size

    def set_tile_subsurf(self):
        tile_surf = self.sprite_handler.get_tile_by_name(self.tile['name'], self.tile['type'])
        self.tile_subsurfaces = tile_surf

    def set_surface_size(self, size):
        self.subsurface_size = size

    def set_tile_type(self, tile_type):
        self.tile['type'] = tile_type

    def set_tile_name(self, tile_name):
        self.tile['name'] = tile_name

    def render(self) -> None:
        tile_coords = self.sprite_handler.get_tile_coords(self.tile['name'], self.tile['type'])
        width_in_tiles = len(set(map(lambda q: q[0], tile_coords)))
        height_in_tiles = len(set(map(lambda q: q[1], tile_coords)))
        self.subsurface = pygame.Surface((self.tile_width*width_in_tiles,
                                          self.tile_height*height_in_tiles))

        for x, y in itertools.product(range(width_in_tiles),
                                      range(height_in_tiles)):

            self.tile_subsurfaces[2 * x + y] = pygame.transform.scale(
                self.tile_subsurfaces[2 * x + y],
                (self.tile_width, self.tile_height)
            )

            tile = Tile(self.tile_width * x,
                            self.tile_height * y,
                            self.tile_width,
                            self.tile_height)

            self.subsurface.blit(self.tile_subsurfaces[2 * x + y], tile)

        if self.subsurface_size is not None:
            self.subsurface = self.sprite_handler.scale_tile_subsurface(self.subsurface, (40, 40))
            return self.surface.blit(self.subsurface, (self.x, self.y))

        return self.surface.blit(self.subsurface,
                                 (self.x-(width_in_tiles-1)*self.tile_width,
                                  self.y-(height_in_tiles-1)*self.tile_height))
