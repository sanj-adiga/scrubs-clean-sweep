import pygame

block = pygame.image.load("imgs/greyChiseledBlock.png")
block = pygame.transform.scale(block,(30,30))
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = block

        self.rect = self.image.get_rect(center=pos)

    def update(self, x_shift):
        self.rect.x += x_shift