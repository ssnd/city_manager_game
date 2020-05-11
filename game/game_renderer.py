from game import config as CONFIG
import pygame
from game.objects.control_panel import ControlPanel
from game.objects.tile_grid import TileGrid
from game.utils.game_saver import GameSaver

WIDTH = CONFIG['screen']['width']
HEIGHT = CONFIG['screen']['height']


class GameRenderer:
    def __init__(self, mouse, game_save):
        self.mouse = mouse
        self.surface = pygame.Surface((WIDTH, HEIGHT))
        self.control_panel = ControlPanel(self.surface, self.mouse)
        self.grid = TileGrid(self.surface, self.mouse, game_save)

    def draw(self, screen):
        self.surface.fill([255, 255, 255])
        self.grid.draw()
        self.control_panel.draw()

        screen.blit(self.surface, (0, 0))
