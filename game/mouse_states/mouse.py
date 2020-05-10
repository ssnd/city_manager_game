from abc import ABC
import logging
import pygame

logger = logging.getLogger('game')


class Mouse(ABC):
    _state = None
    _selectedBlock = None

    def __init__(self, state) -> None:
        self.transition_to(state)
        self.last_press = False
        self.click_info = None

    def handleClick(self):
        pygame.event.get()
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        if pressed1 == 0 and self.last_press == 1:
            self.click_info = pos

        self.last_press = pressed1

    def transition_to(self, state):
        logger.debug(f"Mouse: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def select_block(self, tile):
        self._selectedBlock = tile
        self._state.select_block(tile)

    def block_built(self):
        self._state.block_built()

    @property
    def selectedBlock(self):
        return self._selectedBlock

    @selectedBlock.setter
    def selectedBlock(self, value):
        self._selectedBlock = value


