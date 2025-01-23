import time

import pygame
import sys

from level_1_settings import *
from platform_Level_1 import Level
from level_1_tiles import Tile
import mainMenu

screen = pygame.display.set_mode((w, h))

bg_img = pygame.transform.scale(pygame.image.load('imgs/game_over_bg.png'), (w, h))
bg_rect = bg_img.get_rect()

try_again_img = pygame.transform.scale(pygame.image.load('imgs/game_over_try_again.png').convert_alpha(), (300, 70))
try_again_rect = try_again_img.get_rect(center=(300, 500))

quit_img = pygame.transform.scale(pygame.image.load('imgs/game_over_quit.png').convert_alpha(), (300, 70))
quit_rect = quit_img.get_rect(center=(700, 500))

global running
running = True
global running2
running2 = True

def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(try_again_img, try_again_rect)
    screen.blit(quit_img, quit_rect)
    pygame.display.update()


def run():
    # setting up pygame
    pygame.init()

    pygame.mixer.music.load("music/GameplayExtra.mp3")
    pygame.mixer.music.play(10)
    mainMenu.set_volume()

    clock = pygame.time.Clock()
    level = Level(level_map, screen)

    brown = (31, 25, 23)

    global running
    global running2
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(brown)

        level.run()
        if level.check_quit():
            running2 = False
            running = False

        if level.check_game_over():
            running = False
            running2 = True
            game_over()

        pygame.display.update()
        clock.tick(60)

def game_over():
    pygame.init()

    global running
    global running2
    while running2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                running2 = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if try_again_rect.collidepoint(pos):
                    running2 = False
                    running = True
                    run()
                elif quit_rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()

            pos = pygame.mouse.get_pos()
            if try_again_rect.collidepoint(pos):
                try_again_img.set_alpha(100)
            else:
                try_again_img.set_alpha(255)

            if quit_rect.collidepoint(pos):
                quit_img.set_alpha(100)
            else:
                quit_img.set_alpha(255)

        render()
        time.sleep(0.02)
