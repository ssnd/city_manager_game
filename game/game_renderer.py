from game.config import config as CONFIG
import pygame
from game.tile_grid import TileGrid


class GameRenderer():
    WIDTH = CONFIG['screen']['width']
    HEIGHT = CONFIG['screen']['height']
    TILE_MARGIN = CONFIG['styles']['tilemap_margin']

    def __init__(self):
        self.GAME_AREA_WIDTH = self.WIDTH-self.TILE_MARGIN*2
        self.GAME_AREA_HEIGHT = self.HEIGHT-self.TILE_MARGIN*2

    def draw(self, screen):
        surf = pygame.Surface((self.WIDTH, self.HEIGHT))
        surf.fill([255, 255, 255])

        grid = TileGrid(surf)
        grid.draw()

        screen.blit(surf, (0, 0))
