
class BlockDirector:
    def __init__(self, builder):
        self._builder = builder

    def create_grass_tile(self, x_coord, y_coord):
        self._builder.set_tile('grass')
        self._builder.set_color((50, 205, 50))
        self._builder.set_coords(x_coord, y_coord)
        self._builder.render()

    def create_clay_tile(self, x_coord, y_coord):
        self._builder.set_tile('clay')
        self._builder.set_coords(x_coord, y_coord)
        self._builder.set_color((134, 69, 0))
        self._builder.render()
