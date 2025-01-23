import pygame, time

pygame.init()


def run_title():

    black = (0, 0, 0)
    w = 1000
    h = 600
    canvas = pygame.Surface((w, h))
    screen = pygame.display.set_mode((w, h))

    title_img = pygame.transform.scale(pygame.image.load('imgs/BG_landscape.png').convert_alpha(), (w, h))
    title_rect = title_img.get_rect()
    # alpha value max is actually 255 but if we set it high there will be a delay before the image starts to fade
    alpha = 400
    # TODO: change value to 50 for testing
    running = True

    def render():
        canvas.fill(black)
        canvas.blit(title_img, title_rect)
        screen.blit(canvas, (0, 0, 0, 0))
        pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        title_img.set_alpha(alpha)

        render()
        alpha -= 2
        title_img.set_alpha(alpha)
        time.sleep(.02)

        if alpha < -10:
            running = False
