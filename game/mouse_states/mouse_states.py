from game.mouse_states.abstract_state import State


class FreeMoving(State):
    def select_block(self, tile) -> None:
        self.context.transition_to(BuildBlocks())


class BuildBlocks(State):
    def block_built(self):
        self.context.selectedBlock = None
        self._context.transition_to(FreeMoving())