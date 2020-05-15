from game import config as CONFIG
import pygame
from game.mouse_states.mouse import Mouse
from game.mouse_states.mouse_states import FreeMoving
from game.game_renderer import GameRenderer
from game.utils.game_saver import GameSaver


SCREEN_WIDTH = CONFIG['screen']['width']
SCREEN_HEIGHT = CONFIG['screen']['height']
SAVED_GAME = CONFIG['game_save_file']


class GameManager:
    def __init__(self):
        screen = pygame.display.set_mode([SCREEN_WIDTH,
                                         SCREEN_HEIGHT])
        self.screen = screen
        self.scene = 1
        self.game_save = GameSaver(SAVED_GAME).load_game()
        self.button_clicked = False
        self.mouse = Mouse(FreeMoving())
        self.game = None

    def update(self):
        self.mouse.handleClick()
        if self.scene == 1:
            self.game.draw(self.screen)

    def process(self):
        if self.button_clicked:
            self.scene = 1

    def start(self):
        pygame.init()
        pygame.font.init()
        self.game = GameRenderer(self.mouse,
                                 game_save=self.game_save)

        self.screen.fill([255, 255, 255])



        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or \
                   (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    self.game_save.save_game()
                    running = False


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.button_clicked = True

            self.update()
            self.process()
            pygame.display.flip()

        pygame.quit()
