import pygame
import sys
from platformSettings import *
from platformLevel import Level

# setting up pygame
pygame.init()
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)


