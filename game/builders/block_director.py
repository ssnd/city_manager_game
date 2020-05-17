import logging

from game.objects.tile import Tile

logger = logging.getLogger('game')

class BlockDirector:
    def __init__(self, builder):
        self._builder = builder

    def create_tile(self, name: str, type: str, coords: tuple, time):
        self._builder.set_tile_name(name)
        self._builder.set_tile_type(type)
        self._builder.set_tile_subsurf()
        self._builder.set_coords(coords)
        self._builder.render()
        return  {
            "name" : name,
            "type" : type,
            "ticks_created" : 0,
        }

    def create_cpanel_tile(self, name, coords) -> Tile:
        self._builder.set_tile_name(name)
        self._builder.set_tile_type("main")
        self._builder.set_tile_subsurf()
        self._builder.set_surface_size((40, 40))
        self._builder.set_coords(coords)
        return self._builder.render()






