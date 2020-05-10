from game.config import config as CONFIG
import pygame
from game.objects.control_panel import ControlPanel
from game.objects.tile_grid import TileGrid


class GameRenderer:
    WIDTH = CONFIG['screen']['width']
    HEIGHT = CONFIG['screen']['height']
    TILE_MARGIN = CONFIG['styles']['tilemap_margin']
    GAME_AREA_WIDTH = WIDTH-TILE_MARGIN['left']-TILE_MARGIN['right']
    GAME_AREA_HEIGHT = HEIGHT-TILE_MARGIN['left']-TILE_MARGIN['right']

    def __init__(self, mouse):
        self.mouse = mouse
        self.objects = []
        self.surf = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.control_panel = ControlPanel(self.surf, self.mouse)
        self.grid = TileGrid(self.surf, self.mouse)

    def draw(self, screen):

        self.surf.fill([255, 255, 255])
        self.grid.draw()
        self.control_panel.draw()

        screen.blit(self.surf, (0, 0))
