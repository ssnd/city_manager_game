from abc import ABC

from game.mouse_states.mouse import Mouse


class State(ABC):
    _context = None

    @property
    def context(self) -> Mouse:
        return self._context

    @context.setter
    def context(self, context: Mouse) -> None:
        self._context = context

    def select_block(self, tile) -> None:
        pass

    def block_built(self):
        pass