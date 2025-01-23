import pygame
import time
from boss_battle_settings import *
from platform_boss_battle import Level
import mainMenu

screen = pygame.display.set_mode((w, h))

game_over_bg_img = pygame.transform.scale(pygame.image.load('imgs/game_over_bg.png'), (w, h))
game_over_bg_rect = game_over_bg_img.get_rect()

game_win_bg_img = pygame.transform.scale(pygame.image.load('imgs/WinGame.png'), (w, h))
game_win_bg_rect = game_win_bg_img.get_rect()

try_again_img = pygame.transform.scale(pygame.image.load('imgs/game_over_try_again.png').convert_alpha(), (300, 70))
try_again_rect = try_again_img.get_rect(center=(300, 500))

quit_img = pygame.transform.scale(pygame.image.load('imgs/game_over_quit.png').convert_alpha(), (300, 70))
quit_rect = quit_img.get_rect(center=(700, 500))


def render_loss():
    screen.blit(game_over_bg_img, game_over_bg_rect)
    screen.blit(try_again_img, try_again_rect)
    screen.blit(quit_img, quit_rect)
    pygame.display.update()

def render_win():
    screen.blit(game_win_bg_img, game_win_bg_rect)
    screen.blit(quit_img, quit_rect)
    pygame.display.update()

global running
running = True
global running2
running2 = True
global running3
running3 = True

def run():
    # setting up pygame
    pygame.init()

    pygame.mixer.music.load("music/finalbattle.mp3")
    pygame.mixer.music.play(10)
    mainMenu.set_volume()

    clock = pygame.time.Clock()
    level = Level(level_map, screen)

    blue = (81, 144, 245)
    bg_img = pygame.transform.scale(pygame.image.load('imgs/cleanosphereical.png'), (1000, 600))
    bg_rect = bg_img.get_rect()

    global running
    global running2
    global running3
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(bg_img, bg_rect)

        level.run()
        if level.check_quit():
            running2 = False
            running = False

        if level.check_game_over():
            running = False
            running2 = True
            game_over()

        if level.check_win():
            running = False
            game_win()

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

        render_loss()
        time.sleep(0.02)

def game_win():
    pygame.init()

    global running
    global running3
    while running3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                running3 = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if quit_rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()

            pos = pygame.mouse.get_pos()
            if quit_rect.collidepoint(pos):
                quit_img.set_alpha(100)
            else:
                quit_img.set_alpha(255)

        render_win()
        time.sleep(0.02)
