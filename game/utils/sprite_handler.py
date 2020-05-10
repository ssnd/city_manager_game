import pygame
import yaml
from game.utils.config_handler import ConfigHandler
import logging

logger = logging.getLogger('game')

class SpriteHandler:

    def __init__(self, config_file):
        self.config = ConfigHandler.open_config(config_file)
        self.image = self.open_image()
        self.sprite_tile_height = self.config['tile_height']
        self.sprite_tile_width = self.config['tile_width']

    def open_image(self):
        image_path = self.config['path']
        image = pygame.image.load(image_path).convert()
        return image

    def get_tile_coords(self, name):
        return self.config['tiles'][name]

    def get_tile_by_name(self, name):
        coords_list = self.get_tile_coords(name)

        tile_coords = [self.get_tile_subsurface(*coords)
                       for coords in coords_list]

        # tile_coords.reverse()
        return tile_coords

    def get_tile_subsurface(self, x, y):
        selected_rect = (x*self.sprite_tile_width, y*self.sprite_tile_height,
                         self.sprite_tile_width, self.sprite_tile_height)

        subsurface = self.image.subsurface(selected_rect)

        return subsurface

    @staticmethod
    def scale_tile_subsurface(subsurface, size: tuple):
        return pygame.transform.scale(subsurface, size)
