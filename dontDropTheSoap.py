import time

import pygame, random, mainMenu

def run_minigame():
    pygame.mixer.music.load("music/coconutmall.mp3")
    pygame.mixer.music.play(10)
    mainMenu.set_volume()
    # screen initialization from windowTemplate
    w = 1000
    h = 600
    screen = pygame.display.set_mode((w, h))
    canvas = pygame.Surface((w, h))
    black = (0, 0, 0)
    bg_img = pygame.transform.scale(pygame.image.load('imgs/ddtsbackground.png'), (1000, 600))
    bg_rect = bg_img.get_rect()


    # game clock
    clock = pygame.time.Clock()

    # load soap image and catcher image
    soap_image = pygame.transform.scale(pygame.image.load("imgs/soap.png").convert_alpha(), (100, 100))
    catcher_image = pygame.transform.scale(pygame.image.load("imgs/player.png").convert_alpha(), (250, 250))

    try_again_img = pygame.transform.scale(pygame.image.load("imgs/try_again_btn.png").convert_alpha(), (150, 50))
    try_again_rect = try_again_img.get_rect(center=(w - 100, h - 50))

    # catcher properties
    catcher_x = w // 2
    catcher_y = h - 100
    catcher_speed = 8
    catcher_rect = catcher_image.get_rect(center=(catcher_x, catcher_y))

    # soap properties
    soap_width = 100
    soap_height = 100
    soap_speed = 7
    soap_list = []

    # Set up game variables
    score = 0
    font = pygame.font.Font(None, 36)

    def render():
        screen.blit(bg_img, bg_rect)
        screen.blit(catcher_image, catcher_rect)
        for soap_rect in soap_list:
            screen.blit(soap_image, soap_rect)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        pygame.display.update()

    # game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if try_again_rect.collidepoint(pos):
                    running = False
                    run_minigame()

        # player move
        key = pygame.key.get_pressed()

        # if left key is pressed and catcher is not at the left border
        if key[pygame.K_LEFT] and catcher_rect.left > 0:
            catcher_rect.move_ip(-catcher_speed, 0)

        # if right key is pressed and catcher is not at the right border
        if key[pygame.K_RIGHT] and catcher_rect.right < w:
            catcher_rect.move_ip(catcher_speed, 0)

        # spawn soap if no other soap on the screen
        if len(soap_list) < 1:
            soap_x = random.randint(0, w - soap_width)
            soap_y = -soap_height
            soap_rect = pygame.Rect(soap_x, soap_y, soap_width, soap_height)
            soap_list.append(soap_rect)

        for soap_rect in soap_list:
            soap_rect.move_ip(0, soap_speed)

        # soap collision with catcher
        for soap_rect in soap_list:
            if soap_rect.colliderect(catcher_rect):
                soap_list.remove(soap_rect)
                score += 1

        render()

        # game over requirements
        if score >= 15:
            pygame.mixer.music.load("music/youwin.mp3")
            pygame.mixer.music.play(1)
            screen.blit(font.render("You Win!", True, (0, 0, 0)), (w // 2 - 50, h // 2))
            pygame.display.update()
            pygame.time.delay(3000)
            running = False

        elif any(soap_rect.bottom >= h for soap_rect in soap_list):
            screen.blit(font.render("Game Over, You Lose.", True, (0, 0, 0)), (w // 2, h // 2 - 50))
            screen.blit(font.render("Way to make everything worse.", True, (0, 0, 0)), (w // 2, h // 2))
            screen.blit(try_again_img, try_again_rect)
            pygame.display.update()

        pygame.display.update()

        clock.tick(60)
