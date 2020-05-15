import logging

from game.utils.Coord import Coord

logger = logging.getLogger("game")


class CheckTiles:
    def __init__(self, blocks):
        self.blocks = blocks

    @staticmethod
    def create_block(name, type):
        return  {
                    'name': name,
                    'type': type
                }

    def block_name(self, x,y):
        return self.blocks[(x,y)]['name']
    def block_type(self, x,y):
        return self.blocks[(x,y)]['type']

    def check(self, *coords):
        # first, run the checks on non-corner tiles
        x, y = list(coords)
        x, y = Coord(x), Coord(y)

        self.check_corner_tiles(x, y)

    def check_corner_tiles(self, *coords):
        x, y = list(coords)
        b = self.blocks
        block_name = self.block_name
        block_type = self.block_type

        if x.between(0, 15) and y.between(0, 15):

            # if (b[(x,y-1)] == b[(x,y)] and block_name(x,y) == 'sidewalk'):
            #     b[(x, y)] = self.create_block('sidewalk', "left")
            #     b[(x, y-1)] = self.create_block('sidewalk', "left")
            #
            if (b[(x+1,y)] == b[(x,y)] and block_name(x,y) == 'sidewalk') and\
                block_name(x,y+1) != 'sidewalk':

                b[(x, y)] = self.create_block('sidewalk', block_type(x,y))
                b[(x+1, y)] = self.create_block('sidewalk', block_type(x,y))

            if (b[(x, y)] == b[(x + 1, y)] == b[(x, y + 1)]) \
                    and \
                    b[(x+1,y+1)]['name'] != 'sidewalk' \
                    and \
                    b[(x, y)]['name'] == 'sidewalk':
                # logger.debug(f"here")
                b[(x, y)] = self.create_block('sidewalk', 'corner_tl')
                b[(x, y + 1)] = self.create_block('sidewalk', 'left')
                b[(x + 1, y)] = self.create_block('sidewalk', 'up')

            if (b[(x, y)] == b[(x - 1, y)] == b[(x, y - 1)]) \
                    and \
                    block_name(x-1,y-1) != 'sidewalk' \
                    and \
                    block_name(x,y) == 'sidewalk':

                b[(x, y)] = self.create_block('sidewalk', 'corner_br')
                b[(x, y-1)] = self.create_block('sidewalk', 'right')
                b[(x-1, y)] = self.create_block('sidewalk', 'down')

            if (b[(x, y)] == b[(x + 1, y)] == b[(x, y - 1)]) \
                    and \
                    block_name(x-1,y-1) != 'sidewalk' \
                    and \
                    block_name(x,y) == 'sidewalk':

                b[(x, y)] = self.create_block('sidewalk', 'corner_bl')
                b[(x+1, y)] = self.create_block('sidewalk', 'down')
                b[(x, y-1)] = self.create_block('sidewalk', 'left')
            if (b[(x, y)] == b[(x - 1, y)] == b[(x, y + 1)]) \
                    and \
                    block_name(x-1,y-1) != 'sidewalk' \
                    and \
                    block_name(x,y) == 'sidewalk':

                b[(x, y)] = self.create_block('sidewalk', 'corner_tr')
                b[(x-1, y)] = self.create_block('sidewalk', 'up')
                b[(x, y+1)] = self.create_block('sidewalk', 'right')


            # if (b[(x, y)] == b[(x + 1, y)] == b[(x, y - 1)]) \
