import sys
import time

import pygame

import level_1_main


class Heart(pygame.sprite.Sprite):
    def __init__(self, no):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("designBlocks/Tiles/tile_0044.png"), (40, 40))
        self.rect = self.image.get_rect(center=(no * 40, 30))
