import pygame

from platformSettings import *
from platformTiles import Tile


class Level:
    def __init__(self, level_data, surface):
        # setting up level display
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    print(y)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(0)
        self.tiles.draw(self.display_surface)

