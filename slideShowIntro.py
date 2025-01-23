import pygame, mainMenu

pygame.init()

def run_slideshow():
    pygame.mixer.music.load("music/badjazz.mp3")
    pygame.mixer.music.play(5, 2)
    mainMenu.set_volume()
    w = 1000
    h = 600
    canvas = pygame.Surface((w, h))
    screen = pygame.display.set_mode((w, h))
    black = (0, 0, 0)

    slide1 = pygame.transform.scale(pygame.image.load("imgs/Scrub_Slide1.png").convert_alpha(), (w, h))
    slide1_rect = slide1.get_rect()

    slide2 = pygame.transform.scale(pygame.image.load("imgs/Scrub_Slide2.png").convert_alpha(), (w, h))
    slide2_rect = slide2.get_rect()

    slide3 = pygame.transform.scale(pygame.image.load("imgs/Scrub_Slide3.png").convert_alpha(), (w, h))
    slide3_rect = slide3.get_rect()

    slide4 = pygame.transform.scale(pygame.image.load("imgs/Scrub_Slide4.png").convert_alpha(), (w, h))
    slide4_rect = slide4.get_rect()

    slide5 = pygame.transform.scale(pygame.image.load("imgs/Scrub_Slide5.png").convert_alpha(), (w, h))
    slide5_rect = slide5.get_rect()

    slide6 = pygame.transform.scale(pygame.image.load("imgs/Scrub_slide6.png").convert_alpha(), (w, h))
    slide6_rect = slide6.get_rect()

    slide7 = pygame.transform.scale(pygame.image.load("imgs/Scrub_Slide7.png").convert_alpha(), (w, h))
    slide7_rect = slide7.get_rect()

    current_slide = slide1
    current_slide_rect = slide1_rect

    space_font = pygame.font.Font(None, 24)
    space_text = space_font.render("Click Space to Continue...", True, (0, 0, 0))
    counter = 1

    def render():
        canvas.fill(black)
        canvas.blit(current_slide, current_slide_rect)
        canvas.blit(space_text, (10, 575))
        screen.blit(canvas, (0, 0, 0, 0))
        pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    counter += 1
                    if counter == 2:
                        current_slide = slide2
                        current_slide_rect = slide2_rect
                    if counter == 3:
                        current_slide = slide3
                        current_slide_rect = slide3_rect
                    if counter == 4:
                        pygame.mixer.music.load("music/suspense.mp3")
                        pygame.mixer.music.play(5, 2)
                        current_slide = slide4
                        current_slide_rect = slide4_rect
                    if counter == 5:
                        current_slide = slide5
                        current_slide_rect = slide5_rect
                    if counter == 6:
                        pygame.mixer.music.load("music/drevil.mp3")
                        pygame.mixer.music.play(5, 2)
                        current_slide = slide6
                        current_slide_rect = slide6_rect
                    if counter == 7:
                        current_slide = slide7
                        current_slide_rect = slide7_rect
                    if counter == 8:
                        running = False

        render()
