from game import config as CONFIG
from game.objects.wallet import Wallet
import pygame
from game.objects.control_panel import ControlPanel
from game.objects.tile_grid import TileGrid
import logging
from game.utils.scheduled_events_handler import ScheduledEventsHandler

logger = logging.getLogger('game')
WIDTH = CONFIG['screen']['width']
HEIGHT = CONFIG['screen']['height']


class GameRenderer:
    def __init__(self, mouse, game_save):
        self.mouse = mouse
        self.surface = pygame.Surface((WIDTH, HEIGHT))
        self.wallet = Wallet(game_save)
        self.setup_scheduled_events()

        self.grid = TileGrid(self.surface, self.mouse, self.wallet, game_save)
        self.control_panel = ControlPanel(self.surface, self.mouse, self.wallet, self.grid)
        self.scheduled_events_handler = ScheduledEventsHandler(self.wallet, self.grid)

    def setup_scheduled_events(self):
        pygame.time.set_timer(pygame.USEREVENT+1, CONFIG['income_period'])

    def draw(self, screen):
        self.surface.fill([255, 255, 255])
        self.grid.draw()
        self.scheduled_events_handler.handle_events()
        self.control_panel.draw()
        pygame.time.Clock().tick(100)
        screen.blit(self.surface, (0, 0))
