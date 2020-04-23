from game.config import config as CONFIG
import pygame
from game.game_renderer import GameRenderer


class GameManager:
    SCREEN_WIDTH = CONFIG['screen']['width']
    SCREEN_HEIGHT = CONFIG['screen']['height']

    def __init__(self):
        screen = pygame.display.set_mode([self.SCREEN_WIDTH,
                                         self.SCREEN_HEIGHT])
        self.screen = screen
        self.scene = 1
        self.button_clicked = False
        self.game = GameRenderer()

    def update(self):
        if self.scene == 1:
            self.game.draw(self.screen)

    def process(self):
        if self.button_clicked:
            self.scene = 1

    def start(self):
        pygame.init()
        pygame.font.init()

        self.screen.fill([255, 255, 255])

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.button_clicked = True

            self.update()
            self.process()
            pygame.display.flip()

        pygame.quit()
