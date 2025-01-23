import pygame

stone_block = pygame.image.load("stone_tile.png")
stone_block = pygame.transform.scale(stone_block, (30, 30))
dirt_block = pygame.image.load("dirt_tile.png")
dirt_block = pygame.transform.scale(dirt_block, (30, 30))
ground_block = pygame.image.load("ground_tile.png")
ground_block = pygame.transform.scale(ground_block, (30, 30))
# 1 for stone, 2 for dirt, 3 for cave block
mr_clean = pygame.image.load("imgs/mrClean.png")
mr_clean = pygame.transform.scale(mr_clean, (106, 196))
l_ground = pygame.image.load("groundLeft.png")
l_ground = pygame.transform.scale(l_ground, (30, 30))
r_ground = pygame.image.load("groundRight.png")
r_ground = pygame.transform.scale(r_ground, (30, 30))
mushroom = pygame.image.load("mushroom.png")
mushroom = pygame.transform.scale(mushroom, (30, 30))



class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, block_num):
        super().__init__()
        if block_num == 1:
            self.image = stone_block
        elif block_num == 2:
            self.image = dirt_block
        elif block_num == 3:
            self.image = ground_block
        elif block_num == 4:
            self.image = mr_clean
        elif block_num == 5:
            self.image = l_ground
        elif block_num == 6:
            self.image = r_ground
        elif block_num == 7:
            self.image = mushroom

        self.rect = self.image.get_rect(center=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

        