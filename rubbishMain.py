import pygame, time, random

import mainMenu
import rubbishRun

def run_minigame():
    pygame.init()

    pygame.mixer.music.load("music/cleanup.mp3")
    pygame.mixer.music.play(10)
    mainMenu.set_volume()

    # Initialize the game
    bg_img = pygame.transform.scale(pygame.image.load('imgs/grass.png'), (1000, 600))
    bg_rect = bg_img.get_rect()

    try_again_img = pygame.transform.scale(pygame.image.load("imgs/try_again_btn.png").convert_alpha(), (150, 50))
    try_again_rect = try_again_img.get_rect(center=(900, 550))

    screen = pygame.display.set_mode((1000, 600))
    screen_rect = screen.get_rect()

    no_of_pink_flowers = 10
    pink_flower_group = pygame.sprite.Group()
    for i in range(no_of_pink_flowers):
        pink_flower_group.add(rubbishRun.PinkFlower(screen_rect))

    no_of_blue_flowers = 10
    blue_flower_group = pygame.sprite.Group()
    for i in range(no_of_blue_flowers):
        blue_flower_group.add(rubbishRun.BlueFlower(screen_rect))

    no_of_trash = 20
    trash_group = pygame.sprite.Group()
    for i in range(no_of_trash):
        trash_group.add(rubbishRun.Trash(screen_rect))

    no_of_cans = 20
    cans_group = pygame.sprite.Group()
    for i in range(no_of_cans):
        cans_group.add(rubbishRun.Cans(screen_rect))

    remaining = 40
    lives = 3

    def render():
        screen.blit(bg_img, bg_rect)
        pink_flower_group.update()
        pink_flower_group.draw(screen)

        blue_flower_group.update()
        blue_flower_group.draw(screen)

        trash_group.update()
        trash_group.draw(screen)

        cans_group.update()
        cans_group.draw(screen)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Remaining: {remaining}", True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)
        screen.blit(score_text, score_rect)

        lives_text = font.render(f"Lives Remaining: {lives}", True, (255, 255, 255))
        live_rect = lives_text.get_rect()
        live_rect.topright = (980, 10)
        screen.blit(lives_text, live_rect)

        if len(trash_group) == 0 and len(cans_group) == 0 or len(pink_flower_group) + len(blue_flower_group) <= 17:
            if remaining == 0:
                result_text = font.render("You Win!", True, (255, 255, 255))
            else:
                result_text = font.render("You Lose!", True, (255, 255, 255))
                screen.blit(try_again_img, try_again_rect)
                pygame.display.update()
            result_rect = result_text.get_rect()
            result_rect.center = screen_rect.center
            screen.blit(result_text, result_rect)

        pygame.display.flip()

    render()
    running = True
    # gameloop
    while running:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for sprite in pink_flower_group.sprites():
                    if sprite.rect.collidepoint(event.pos):
                        pink_flower_group.remove(sprite)
                        pink_flower_group.update()
                        pink_flower_group.draw(screen)
                        lives -= 1
                for sprite in blue_flower_group.sprites():
                    if sprite.rect.collidepoint(event.pos):
                        blue_flower_group.remove(sprite)
                        blue_flower_group.update()
                        blue_flower_group.draw(screen)
                        lives -= 1
                for sprite in trash_group.sprites():
                    if sprite.rect.collidepoint(event.pos):
                        trash_group.remove(sprite)
                        trash_group.update()
                        trash_group.draw(screen)
                        remaining -= 1
                for sprite in cans_group.sprites():
                    if sprite.rect.collidepoint(event.pos):
                        cans_group.remove(sprite)
                        cans_group.update()
                        cans_group.draw(screen)
                        remaining -= 1
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if try_again_rect.collidepoint(pos):
                    running = False
                    run_minigame()

            if (len(pink_flower_group) + len(blue_flower_group)) <= 17:
                render()
                screen.blit(try_again_img, try_again_rect)
                pygame.display.update()
            if bool(trash_group) == False and bool(cans_group) == False:
                render()
                time.sleep(2)
                running = False

        render()
        time.sleep(0.05)
