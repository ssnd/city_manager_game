import pygame

# from game.objects.control_panel import logger
from game.utils.text_box import TextBox
import logging

logger= logging.getLogger('game')


class ResetButton(object):
    def __init__(self, subsurf, mouse, grid):
        self.subsurface = subsurf
        self.mouse = mouse
        self.grid = grid
        self.color = (255, 0,0)
        self.surface = pygame.Surface((70, 300))
        self.surface.fill((255, 255, 255))
        self.text = TextBox(self.surface, align="center")
        self.text.text_color = (255, 255, 255)
        self.rect = None
        self.text.background_color = self.color

    def handle_click(self):
        if self.mouse.click_info and self.rect.collidepoint(self.mouse.click_info):
            logger.info("Resetting the grid")
            self.grid.reset_grid()

        self.mouse.click_info = None

    def draw(self):

        pygame.draw.rect(self.surface, self.color, (0, 0, 150, 30))
        self.text.set_margin_top(5)
        self.text.draw("RESET")
        self.rect = self.subsurface.blit(self.surface, (10, 565))
        self.handle_click()