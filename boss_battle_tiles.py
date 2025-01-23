import pygame

stone_block = pygame.image.load("imgs/plaintile.png")
dirt_block = pygame.image.load("imgs/plaintile.png")
dirt_block = pygame.transform.scale(dirt_block, (30, 30))
stone_block = pygame.transform.scale(stone_block, (30, 30))
cave_block = pygame.image.load("imgs/plaintile.png")
cave_block = pygame.transform.scale(cave_block, (30, 30))
door_block = pygame.image.load('imgs/soap.png')
door_block = pygame.transform.scale(door_block, (40,90))



# 1 for stone, 2 for dirt, 3 for cave block

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, block_num):
        super().__init__()
        if block_num == 1:
            self.image = stone_block
        elif block_num == 2:
            self.image = dirt_block
        elif block_num == 3:
            self.image= cave_block
        elif block_num == 4:
            self.image = door_block
        el

        self.rect = self.image.get_rect(center=pos)

    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift
