import pygame

pygame.init()


def run_ddts_instructions():
    pygame.mixer.music.load("music/instruction.mp3")
    pygame.mixer.music.play(10)

    w = 1000
    h = 600
    canvas = pygame.Surface((w, h))
    screen = pygame.display.set_mode((w, h))
    black = (0, 0, 0)
    white = (255, 255, 255)

    start_img = pygame.transform.scale(pygame.image.load("imgs/playbutton.png").convert_alpha(), (300, 100))
    start_rect = start_img.get_rect(bottomright=(970, 590))

    ddts_img = pygame.transform.scale(pygame.image.load("imgs/ddtsInstructions.png").convert_alpha(), (w, h))
    ddts_rect = ddts_img.get_rect()

    alpha = -50
    bg_alpha = -50

    def render():
        if alpha < 170:
            canvas.fill(black)
        elif alpha > 170:
            canvas.fill(white)
        canvas.blit(ddts_img, ddts_rect)
        canvas.blit(start_img, start_rect)
        screen.blit(canvas, (0, 0, 0, 0))
        pygame.display.update()

    def handle_alpha():
        ddts_img.set_alpha(bg_alpha)
        start_img.set_alpha(alpha)

    srt_counter = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(pos):
                    running = False

            pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(pos):
                start_img = pygame.transform.scale(start_img, (310, 110))
                start_rect = start_img.get_rect(bottomright=(970, 590))
                srt_counter += 1

            else:
                start_img = pygame.transform.scale(start_img, (300, 100))
                start_rect = start_img.get_rect(bottomright=(970, 590))
                # fixes the issue of the image warping after many mouse overs/scales
                if srt_counter > 20:
                    start_img = pygame.transform.scale(pygame.image.load("imgs/playbutton.png").convert_alpha(),
                                                       (300, 100))

        handle_alpha()

        if alpha < 255:
            alpha += 5
        if bg_alpha < 200:
            bg_alpha += 5
        render()


import pygame

pygame.init()


def run_ss_instructions():
    pygame.mixer.music.load("music/instruction.mp3")
    pygame.mixer.music.play(10)

    w = 1000
    h = 600
    canvas = pygame.Surface((w, h))
    screen = pygame.display.set_mode((w, h))
    black = (0, 0, 0)
    white = (255, 255, 255)

    start_img = pygame.transform.scale(pygame.image.load("imgs/playbutton.png").convert_alpha(), (300, 100))
    start_rect = start_img.get_rect(bottomright=(970, 590))

    ss_img = pygame.transform.scale(pygame.image.load("imgs/ssinstructions.png").convert_alpha(), (w, h))
    ss_rect = ss_img.get_rect()

    alpha = -50
    bg_alpha = -50

    def render():
        if alpha < 170:
            canvas.fill(black)
        elif alpha > 170:
            canvas.fill(white)
        canvas.blit(ss_img, ss_rect)
        canvas.blit(start_img, start_rect)
        screen.blit(canvas, (0, 0, 0, 0))
        pygame.display.update()

    def handle_alpha():
        ss_img.set_alpha(bg_alpha)
        start_img.set_alpha(alpha)

    srt_counter = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(pos):
                    running = False

            pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(pos):
                start_img = pygame.transform.scale(start_img, (310, 110))
                start_rect = start_img.get_rect(bottomright=(970, 590))
                srt_counter += 1

            else:
                start_img = pygame.transform.scale(start_img, (300, 100))
                start_rect = start_img.get_rect(bottomright=(970, 590))
                # fixes the issue of the image warping after many mouse overs/scales
                if srt_counter > 20:
                    start_img = pygame.transform.scale(pygame.image.load("imgs/playbutton.png").convert_alpha(),
                                                       (300, 100))

        handle_alpha()

        if alpha < 255:
            alpha += 5
        if bg_alpha < 200:
            bg_alpha += 5
        render()


import pygame
from pygame import font

pygame.init()


def run_rr_instructions():
    pygame.mixer.init()
    pygame.mixer.music.load("music/instruction.mp3")
    pygame.mixer.music.play(10)

    w = 1000
    h = 600
    canvas = pygame.Surface((w, h))
    screen = pygame.display.set_mode((w, h))
    black = (0, 0, 0)
    white = (255, 255, 255)

    start_img = pygame.transform.scale(pygame.image.load("imgs/playbutton.png").convert_alpha(), (300, 100))
    start_rect = start_img.get_rect(bottomright=(970, 590))

    rr_img = pygame.transform.scale(pygame.image.load("imgs/rrinstructions.png").convert_alpha(), (w, h))
    rr_rect = rr_img.get_rect()

    alpha = -50
    bg_alpha = -50

    def render():
        if alpha < 170:
            canvas.fill(black)
        elif alpha > 170:
            canvas.fill(white)
        canvas.blit(rr_img, rr_rect)
        canvas.blit(start_img, start_rect)
        screen.blit(canvas, (0, 0, 0, 0))
        pygame.display.update()

    def handle_alpha():
        rr_img.set_alpha(bg_alpha)
        start_img.set_alpha(alpha)

    srt_counter = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(pos):
                    running = False

            pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(pos):
                start_img = pygame.transform.scale(start_img, (310, 110))
                start_rect = start_img.get_rect(bottomright=(970, 590))
                srt_counter += 1

            else:
                start_img = pygame.transform.scale(start_img, (300, 100))
                start_rect = start_img.get_rect(bottomright=(970, 590))
                # fixes the issue of the image warping after many mouse overs/scales
                if srt_counter > 20:
                    start_img = pygame.transform.scale(pygame.image.load("imgs/playbutton.png").convert_alpha(),
                                                       (300, 100))

        handle_alpha()

        if alpha < 255:
            alpha += 5
        if bg_alpha < 200:
            bg_alpha += 5
        render()


import pygame
from pygame import font

pygame.init()


def run_level_instructions():
    pygame.mixer.music.load("music/instruction.mp3")
    pygame.mixer.music.play(10)

    w = 1000
    h = 600
    canvas = pygame.Surface((w, h))
    screen = pygame.display.set_mode((w, h))
    black = (0, 0, 0)
    white = (255, 255, 255)

    start_img = pygame.transform.scale(pygame.image.load("imgs/startbutt.png").convert_alpha(), (300, 100))
    start_rect = start_img.get_rect(bottomright=(970, 590))

    rr_img = pygame.transform.scale(pygame.image.load("imgs/gameinstrooc.png").convert_alpha(), (w, h))
    rr_rect = rr_img.get_rect()

    alpha = -50
    bg_alpha = -50

    def render():
        if alpha < 170:
            canvas.fill(black)
        elif alpha > 170:
            canvas.fill(white)
        canvas.blit(rr_img, rr_rect)
        canvas.blit(start_img, start_rect)
        screen.blit(canvas, (0, 0, 0, 0))
        pygame.display.update()

    def handle_alpha():
        rr_img.set_alpha(bg_alpha)
        start_img.set_alpha(alpha)

    srt_counter = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(pos):
                    running = False

            pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(pos):
                start_img = pygame.transform.scale(start_img, (310, 110))
                start_rect = start_img.get_rect(bottomright=(970, 590))
                srt_counter += 1

            else:
                start_img = pygame.transform.scale(start_img, (300, 100))
                start_rect = start_img.get_rect(bottomright=(970, 590))
                # fixes the issue of the image warping after many mouse overs/scales
                if srt_counter > 20:
                    start_img = pygame.transform.scale(pygame.image.load("imgs/startbutt.png").convert_alpha(),
                                                       (300, 100))

        handle_alpha()

        if alpha < 255:
            alpha += 5
        if bg_alpha < 200:
            bg_alpha += 5
        render()


import pygame
from pygame import font

pygame.init()


def run_boss_instructions():

    pygame.mixer.init()
    pygame.mixer.music.load("music/instruction.mp3")
    pygame.mixer.music.play(10)

    w = 1000
    h = 600
    canvas = pygame.Surface((w, h))
    screen = pygame.display.set_mode((w, h))
    black = (0, 0, 0)
    white = (255, 255, 255)

    start_img = pygame.transform.scale(pygame.image.load("imgs/startbutt.png").convert_alpha(), (300, 100))
    start_rect = start_img.get_rect(bottomright=(970, 590))

    rr_img = pygame.transform.scale(pygame.image.load("imgs/finalbossinstructions.png").convert_alpha(), (w, h))
    rr_rect = rr_img.get_rect()

    alpha = -50
    bg_alpha = -50

    def render():
        if alpha < 170:
            canvas.fill(black)
        elif alpha > 170:
            canvas.fill(white)
        canvas.blit(rr_img, rr_rect)
        canvas.blit(start_img, start_rect)
        screen.blit(canvas, (0, 0, 0, 0))
        pygame.display.update()

    def handle_alpha():
        rr_img.set_alpha(bg_alpha)
        start_img.set_alpha(alpha)

    srt_counter = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(pos):
                    running = False

            pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(pos):
                start_img = pygame.transform.scale(start_img, (310, 110))
                start_rect = start_img.get_rect(bottomright=(970, 590))
                srt_counter += 1

            else:
                start_img = pygame.transform.scale(start_img, (300, 100))
                start_rect = start_img.get_rect(bottomright=(970, 590))
                # fixes the issue of the image warping after many mouse overs/scales
                if srt_counter > 20:
                    start_img = pygame.transform.scale(pygame.image.load("imgs/startbutt.png").convert_alpha(),
                                                       (300, 100))

        handle_alpha()

        if alpha < 255:
            alpha += 5
        if bg_alpha < 200:
            bg_alpha += 5
        render()
