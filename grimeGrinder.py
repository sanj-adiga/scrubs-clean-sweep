import pygame, random, mainMenu

pygame.init()

def run_minigame():

    pygame.mixer.music.load("music/oldtownfart.mp3")
    pygame.mixer.music.play(10, 29)
    mainMenu.set_volume()
    # screen initialization
    w = 1000
    h = 600
    screen = pygame.display.set_mode((w, h))
    canvas = pygame.Surface((w, h))

    bg_img = pygame.transform.scale(pygame.image.load('imgs/jimmyroom.png'), (1000, 600))
    bg_rect = bg_img.get_rect()

    # game clock
    clock = pygame.time.Clock()

    # loading images
    grime_img_1 = pygame.transform.scale(pygame.image.load("imgs/grime1.png").convert_alpha(), (400, 400))
    grime_img_1_rect = grime_img_1.get_rect(center=(100, random.randint(300, h - 200)))
    grime_img_2 = pygame.transform.scale(pygame.image.load("imgs/grime2.png").convert_alpha(), (400, 400))
    grime_img_2_rect = grime_img_2.get_rect(center=(300, random.randint(200, h - 200)))
    grime_img_3 = pygame.transform.scale(pygame.image.load("imgs/grime3.png").convert_alpha(), (300, 300))
    grime_img_3_rect = grime_img_3.get_rect(center=(500, random.randint(200, h - 200)))
    grime_img_4 = pygame.transform.scale(pygame.image.load("imgs/grime4.png").convert_alpha(), (300, 300))
    grime_img_4_rect = grime_img_4.get_rect(center=(700, random.randint(200, h - 200)))
    grime_img_5 = pygame.transform.scale(pygame.image.load("imgs/grime5.png").convert_alpha(), (300, 300))
    grime_img_5_rect = grime_img_5.get_rect(center=(900, random.randint(200, h - 200)))
    mop_img = pygame.transform.scale(pygame.image.load("imgs/mopping.png").convert_alpha(), (80, 100))

    try_again_img = pygame.transform.scale(pygame.image.load("imgs/try_again_btn.png").convert_alpha(), (150, 50))
    try_again_rect = try_again_img.get_rect(center=(w - 100, h - 50))

    # mop properties
    mop_x = w - 50
    mop_y = 50
    mop_speed = 5
    mop_img_rect = mop_img.get_rect(center=(mop_x, mop_y))
    grime_list = [grime_img_1, grime_img_2, grime_img_3, grime_img_4, grime_img_5]

    font = pygame.font.Font(None, 36)

    start_time = pygame.time.get_ticks() // 1000

    def render():
        screen.blit(bg_img, bg_rect)
        screen.blit(grime_img_1, grime_img_1_rect)
        screen.blit(grime_img_2, grime_img_2_rect)
        screen.blit(grime_img_3, grime_img_3_rect)
        screen.blit(grime_img_4, grime_img_4_rect)
        screen.blit(grime_img_5, grime_img_5_rect)
        time = 15 - (pygame.time.get_ticks() // 1000 - start_time)
        if time < 0:
            time = 0
        timer_text = font.render(f'Time Remaining: {time}', True, (0, 0, 0))
        screen.blit(timer_text, (10, 10))
        screen.blit(mop_img, mop_img_rect)
        pygame.display.update()

    # game loop
    running = True
    failed = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if try_again_rect.collidepoint(pos):
                    running = False
                    run_minigame()

        # player functions
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and mop_img_rect.left > 0:
            mop_img_rect.move_ip(-mop_speed, 0)
        if key[pygame.K_RIGHT] and mop_img_rect.right < w:
            mop_img_rect.move_ip(mop_speed, 0)
        if key[pygame.K_UP] and mop_img_rect.top > 0:
            mop_img_rect.move_ip(0, -mop_speed)
        if key[pygame.K_DOWN] and mop_img_rect.bottom < h:
            mop_img_rect.move_ip(0, mop_speed)

        # cleaning logic
        if mop_img_rect.colliderect(grime_img_1_rect):
            grime_img_1.set_alpha(grime_img_1.get_alpha() - 1)
        if mop_img_rect.colliderect(grime_img_2_rect):
            grime_img_2.set_alpha(grime_img_2.get_alpha() - 1)
        if mop_img_rect.colliderect(grime_img_3_rect):
            grime_img_3.set_alpha(grime_img_3.get_alpha() - 1)
        if mop_img_rect.colliderect(grime_img_4_rect):
            grime_img_4.set_alpha(grime_img_4.get_alpha() - 1)
        if mop_img_rect.colliderect(grime_img_5_rect):
            grime_img_5.set_alpha(grime_img_5.get_alpha() - 1)

        render()
        if failed:
            screen.blit(font.render("You Missed A Spot, Idiot...", True, (0, 0, 0)), (w // 2 - 150, 50))
            screen.blit(try_again_img, try_again_rect)
            pygame.display.update()

        # game over
        img_faded = True
        for grime_img in grime_list:
            if grime_img.get_alpha() != 0:
                img_faded = False

        if img_faded:
            screen.blit(font.render("You Win!", True, (0, 0, 0)), (w // 2 - 50, 50))
            pygame.display.update()
            pygame.time.delay(4000)
            running = False

        elif (16 - (pygame.time.get_ticks() // 1000 - start_time)) == 0:
            screen.blit(font.render("You Missed A Spot, Idiot...", True, (0, 0, 0)), (w // 2 - 150, 50))
            screen.blit(try_again_img, try_again_rect)
            pygame.display.update()
            failed = True
            
        pygame.display.update()

        clock.tick(60)


