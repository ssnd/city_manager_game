from abc import ABC
import logging
import pygame

logger = logging.getLogger('game')


class Mouse(ABC):
    _state = None
    _selectedBlock = {}

    def __init__(self, state) -> None:
        self.transition_to(state)
        self.last_press = False
        self.click_info = None

    def handleClick(self):
        pygame.event.get()
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        
        # logger.debug(f"{pressed1, pressed2, pressed3}")
        if pressed1 == 0 and self.last_press == 1:
            self.click_info = pos

        self.last_press = pressed1

    def transition_to(self, state):
        logger.debug(f"Mouse: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def select_block(self, tile):
        self._selectedBlock['name'] = tile
        self._selectedBlock['type'] = "main"
        self._state.select_block(self.selectedBlock)

    def block_built(self):
        self._state.block_built()

    @property
    def selectedBlock(self):
        return self._selectedBlock

    @selectedBlock.setter
    def selectedBlock(self, value):
        self._selectedBlock = value


