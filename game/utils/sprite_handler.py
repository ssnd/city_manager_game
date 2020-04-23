import pygame
import yaml


class SpriteHandler:

    def __init__(self, config_file):
        self.config = self.open_config(config_file)
        self.image = self.open_image()
        self.sprite_tile_height = self.config['tile_height']
        self.sprite_tile_width = self.config['tile_width']

    def open_config(self, path):
        with open(path) as f:
            config = yaml.safe_load(f)

        return config

    def open_image(self):
        image_path = self.config['path']
        image = pygame.image.load(image_path).convert()
        return image

    def get_tile_by_name(self, name):
        coords = self.config['tiles'][name]
        return self.get_tile_subsurface(*coords)

    def get_tile_subsurface(self, x, y):
        selected_rect = (x*self.sprite_tile_width, y*self.sprite_tile_height,
                         self.sprite_tile_width,   self.sprite_tile_height)

        subsurface = self.image.subsurface(selected_rect)

        return subsurface
