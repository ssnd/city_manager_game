import logging

from game.objects.tile import Tile

logger = logging.getLogger('game')

class BlockDirector:
    def __init__(self, builder):
        self._builder = builder

    def create_tile(self, name: str, type: str, coords: tuple) -> None:
        self._builder.set_tile_name(name)
        self._builder.set_tile_type(type)
        self._builder.set_tile_subsurf()
        self._builder.set_coords(coords)
        return self._builder.render()

    def create_cpanel_tile(self, name, coords) -> Tile:
        self._builder.set_tile_name(name)
        self._builder.set_tile_type("main")
        # self._builder.set_size((20, 20))
        self._builder.set_tile_subsurf()
        self._builder.set_surface_size((40, 40))
        self._builder.set_coords(coords)
        return self._builder.render()






