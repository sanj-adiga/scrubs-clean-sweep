import pygame, time

global scrub_colour
scrub_colour = 'Blue'
global scrub_class
scrub_class = 'default'
global audio_volume
audio_volume = 50

pygame.init()


def set_volume():
    pygame.mixer.music.set_volume(audio_volume / 100)


def run_menu():
    w = 1000
    h = 600
    canvas = pygame.Surface((w, h))
    screen = pygame.display.set_mode((w, h))
    black = (0, 0, 0)
    white = (255, 255, 255)

    start_img = pygame.transform.scale(pygame.image.load("imgs/blueSrt.png").convert_alpha(), (300, 100))
    start_rect = start_img.get_rect(center=(w / 2, h / 2))

    audio_img = pygame.transform.scale(pygame.image.load("imgs/audio_btn.png").convert_alpha(), (100, 100))
    audio_rect = audio_img.get_rect(center=(900, 550))

    cc_img = pygame.transform.scale(pygame.image.load('imgs/BlueScrubWithoutBG.png').convert_alpha(), (130, 100))
    cc_rect = cc_img.get_rect(center=(100, 550))

    bg_img = pygame.transform.scale(pygame.image.load("imgs/cityBackground.jpg").convert_alpha(), (w, h))
    bg_rect = bg_img.get_rect()

    audio_label_img = pygame.transform.scale(pygame.image.load('imgs/audioBtn.png').convert_alpha(), (150, 30))
    audio_label_rect = audio_label_img.get_rect(center=(900, 475))

    cc_label_img = pygame.transform.scale(pygame.image.load('imgs/characterCustomizationBtn.png').convert_alpha(), (150, 30))
    cc_label_rect = cc_label_img.get_rect(center=(100, 475))

    alpha = -50
    bg_alpha = -50

    def render():
        if alpha < 170:
            canvas.fill(black)
        elif alpha > 170:
            canvas.fill(white)
        canvas.blit(bg_img, bg_rect)
        canvas.blit(start_img, start_rect)
        canvas.blit(audio_img, audio_rect)
        canvas.blit(cc_img, cc_rect)
        canvas.blit(audio_label_img, audio_label_rect)
        canvas.blit(cc_label_img, cc_label_rect)
        screen.blit(canvas, (0, 0, 0, 0))
        pygame.display.update()

    def handle_alpha():
        bg_img.set_alpha(bg_alpha)
        start_img.set_alpha(alpha)
        audio_img.set_alpha(alpha)
        cc_img.set_alpha(alpha)
        audio_label_img.set_alpha(alpha)
        cc_label_img.set_alpha(alpha)

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
                if audio_rect.collidepoint(pos):
                    audio()
                if cc_rect.collidepoint(pos):
                    character_customization()

            pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(pos):
                start_img = pygame.transform.scale(start_img, (310, 110))
                start_rect = start_img.get_rect(center=(w / 2, h / 2))
                srt_counter += 1
            else:
                start_img = pygame.transform.scale(start_img, (300, 100))
                start_rect = start_img.get_rect(center=(w / 2, h / 2))
                # fixes the issue of the image warping after many mouse overs/scales
                if srt_counter > 1:
                    start_img = pygame.transform.scale(pygame.image.load("imgs/blueSrt.png").convert_alpha(), (300, 100))
                    audio_img = pygame.transform.scale(pygame.image.load("imgs/audio_btn.png").convert_alpha(), (100, 100))
                    cc_img = pygame.transform.scale(pygame.image.load('imgs/BlueScrubWithoutBG.png').convert_alpha(), (130, 100))
            if audio_rect.collidepoint(pos):
                audio_img = pygame.transform.scale(audio_img, (110, 110))
                audio_rect = audio_img.get_rect(center=(900, 550))
                srt_counter += 1
            else:
                audio_img = pygame.transform.scale(audio_img, (100, 100))
                audio_rect = audio_img.get_rect(center=(900, 550))
                if srt_counter > 1:
                    start_img = pygame.transform.scale(pygame.image.load("imgs/blueSrt.png").convert_alpha(), (300, 100))
                    audio_img = pygame.transform.scale(pygame.image.load("imgs/audio_btn.png").convert_alpha(), (100, 100))
                    cc_img = pygame.transform.scale(pygame.image.load('imgs/BlueScrubWithoutBG.png').convert_alpha(), (130, 100))
            if cc_rect.collidepoint(pos):
                cc_img = pygame.transform.scale(cc_img, (140, 110))
                cc_rect = cc_img.get_rect(center=(100, 550))
                srt_counter += 1
            else:
                cc_img = pygame.transform.scale(cc_img, (130, 100))
                cc_rect = cc_img.get_rect(center=(100, 550))
                if srt_counter > 1:
                    start_img = pygame.transform.scale(pygame.image.load("imgs/blueSrt.png").convert_alpha(), (300, 100))
                    audio_img = pygame.transform.scale(pygame.image.load("imgs/audio_btn.png").convert_alpha(), (100, 100))
                    cc_img = pygame.transform.scale(pygame.image.load('imgs/BlueScrubWithoutBG.png').convert_alpha(), (130, 100))

        handle_alpha()

        if alpha < 255:
            alpha += 5
        if bg_alpha < 200:
            bg_alpha += 5
        render()
        time.sleep(.02)


# audio settings
def audio():
    w = 1000
    h = 600
    canvas = pygame.Surface((w, h))
    screen = pygame.display.set_mode((w, h))
    black = (0, 0, 0)

    global audio_volume

    bg_img = pygame.transform.scale(pygame.image.load("imgs/cityBackground.jpg").convert_alpha(), (w, h))
    bg_rect = bg_img.get_rect()

    volume_img = pygame.transform.scale(pygame.image.load("imgs/volume_button.png").convert_alpha(), (250, 75))
    volume_rect = volume_img.get_rect(center=(w / 2, 250))

    slider = pygame.Surface((600, 30))
    slider.fill(pygame.Color('dodgerblue2'))
    slider_button = pygame.Surface((30, 30))
    slider_button.fill((255, 255, 255))
    slider_button_rect = slider_button.get_rect(center=(audio_volume * 6, 15))

    font = pygame.font.Font(None, 40)

    back_img = pygame.transform.scale(pygame.image.load("imgs/backbtn.png").convert_alpha(), (200, 75))
    back_rect = back_img.get_rect(center=(900, 550))

    screen.fill(black)

    def render():
        canvas.blit(bg_img, bg_rect)
        canvas.blit(volume_img, volume_rect)
        canvas.blit(back_img, back_rect)
        slider.blit(slider_button, slider_button_rect)
        canvas.blit(slider, (200, 285))
        current_vol = (slider_button_rect.centerx - 13) // 5.7
        if current_vol < 0:
            current_vol = 0
        elif current_vol > 100:
            current_vol = 100
        timer_text = font.render(f'{current_vol}%', True, (255, 255, 255))
        canvas.blit(timer_text, (w / 2 - 30, 330))
        screen.blit(canvas, (0, 0, 0, 0))
        pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if back_rect.collidepoint(pos):
                    running = False

            pos = pygame.mouse.get_pos()

            if (200 <= pos[0] <= 800) and (285 <= pos[1] <= 315):
                slider.fill(pygame.Color('lightskyblue3'))
                if pygame.mouse.get_pressed()[0]:
                    audio_volume = (pos[0] - 200) // 6
                    slider_button_rect = slider_button.get_rect(center=(pos[0] - 200, 15))
            else:
                slider.fill(pygame.Color('dodgerblue2'))

            if back_rect.collidepoint(pos):
                back_img.set_alpha(100)
            else:
                back_img.set_alpha(255)

        bg_img.set_alpha(100)

        render()

        pygame.display.update()

        time.sleep(.02)


# character customization
def character_customization():
    w = 1000
    h = 600
    canvas = pygame.Surface((w, h))
    screen = pygame.display.set_mode((w, h))
    black = (0, 0, 0)

    global scrub_colour
    global scrub_class

    bg_img = pygame.transform.scale(pygame.image.load("imgs/cityBackground.jpg").convert_alpha(), (w, h))
    bg_rect = bg_img.get_rect()

    colour_img = pygame.transform.scale(pygame.image.load("imgs/colour_choose.png").convert_alpha(), (300, 100))
    colour_rect = colour_img.get_rect(center=(300, 75))

    blue_img = pygame.transform.scale(pygame.image.load("imgs/colour_blue.png").convert_alpha(), (150, 50))
    blue_rect = blue_img.get_rect(center=(200, 175))

    green_img = pygame.transform.scale(pygame.image.load("imgs/colour_green.png").convert_alpha(), (150, 50))
    green_rect = green_img.get_rect(center=(400, 175))

    purple_img = pygame.transform.scale(pygame.image.load("imgs/colour_purple.png").convert_alpha(), (150, 50))
    purple_rect = purple_img.get_rect(center=(200, 250))

    yellow_img = pygame.transform.scale(pygame.image.load("imgs/colour_yellow.png").convert_alpha(), (150, 50))
    yellow_rect = yellow_img.get_rect(center=(400, 250))

    class_img = pygame.transform.scale(pygame.image.load("imgs/class_choose.png").convert_alpha(), (300, 50))
    class_rect = class_img.get_rect(center=(300, 375))

    default_img = pygame.transform.scale(pygame.image.load("imgs/class_default.png").convert_alpha(), (150, 50))
    default_rect = default_img.get_rect(center=(200, 450))

    tank_img = pygame.transform.scale(pygame.image.load("imgs/class_tank.png").convert_alpha(), (150, 50))
    tank_rect = tank_img.get_rect(center=(400, 450))

    acrobat_img = pygame.transform.scale(pygame.image.load("imgs/class_acrobat.png").convert_alpha(), (150, 50))
    acrobat_rect = acrobat_img.get_rect(center=(300, 525))

    scrub_img = pygame.transform.scale(pygame.image.load("imgs/BlueScrubWithoutBG.png").convert_alpha(), (400, 300))
    scrub_rect = scrub_img.get_rect(center=(750, 250))

    text_img = pygame.transform.scale(pygame.image.load("imgs/default_text.png").convert_alpha(), (400, 75))
    text_rect = text_img.get_rect(center=(750, 450))

    back_img = pygame.transform.scale(pygame.image.load("imgs/backbtn.png").convert_alpha(), (200, 75))
    back_rect = back_img.get_rect(center=(900, 550))

    if scrub_colour == 'Blue':
        blue_img.set_alpha(100)
        scrub_img = pygame.transform.scale(pygame.image.load("imgs/BlueScrubWithoutBG.png").convert_alpha(), (400, 300))
        scrub_rect = scrub_img.get_rect(center=(750, 250))
    elif scrub_colour == 'Green':
        green_img.set_alpha(100)
        scrub_img = pygame.transform.scale(pygame.image.load("imgs/scrub_green.png"), (400, 300))
        scrub_rect = scrub_img.get_rect(center=(750, 250))
    elif scrub_colour == 'Purple':
        purple_img.set_alpha(100)
        scrub_img = pygame.transform.scale(pygame.image.load("imgs/scrub_purple.png"), (400, 300))
        scrub_rect = scrub_img.get_rect(center=(750, 250))
    elif scrub_colour == 'Yellow':
        yellow_img.set_alpha(100)
        scrub_img = pygame.transform.scale(pygame.image.load("imgs/scrub_yellow.png"), (400, 300))
        scrub_rect = scrub_img.get_rect(center=(750, 250))

    if scrub_class == 'default':
        default_img.set_alpha(100)
        text_img = pygame.transform.scale(pygame.image.load("imgs/default_text.png"), (400, 75))
        text_rect = text_img.get_rect(center=(750, 450))
    elif scrub_class == 'tank':
        tank_img.set_alpha(100)
        text_img = pygame.transform.scale(pygame.image.load("imgs/tank_text.png"), (400, 75))
        text_rect = text_img.get_rect(center=(750, 450))
    elif scrub_class == 'acrobat':
        acrobat_img.set_alpha(100)
        text_img = pygame.transform.scale(pygame.image.load("imgs/acrobat_text.png"), (400, 75))
        text_rect = text_img.get_rect(center=(750, 450))

    screen.fill(black)

    def render():
        canvas.blit(bg_img, bg_rect)
        canvas.blit(colour_img, colour_rect)
        canvas.blit(blue_img, blue_rect)
        canvas.blit(green_img, green_rect)
        canvas.blit(purple_img, purple_rect)
        canvas.blit(yellow_img, yellow_rect)
        canvas.blit(class_img, class_rect)
        canvas.blit(default_img, default_rect)
        canvas.blit(tank_img, tank_rect)
        canvas.blit(acrobat_img, acrobat_rect)
        canvas.blit(back_img, back_rect)
        canvas.blit(scrub_img, scrub_rect)
        canvas.blit(text_img, text_rect)
        screen.blit(canvas, (0, 0, 0, 0))
        pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if back_rect.collidepoint(pos):
                    running = False

                # setting character customizations
                if blue_rect.collidepoint(pos):
                    blue_img.set_alpha(100)
                    green_img.set_alpha(255)
                    purple_img.set_alpha(255)
                    yellow_img.set_alpha(255)
                    scrub_img = pygame.transform.scale(pygame.image.load("imgs/BlueScrubWithoutBG.png"), (400, 300))
                    scrub_rect = scrub_img.get_rect(center=(750, 250))
                    scrub_colour = 'Blue'
                elif green_rect.collidepoint(pos):
                    blue_img.set_alpha(255)
                    green_img.set_alpha(100)
                    purple_img.set_alpha(255)
                    yellow_img.set_alpha(255)
                    scrub_img = pygame.transform.scale(pygame.image.load("imgs/scrub_green.png"), (400, 300))
                    scrub_rect = scrub_img.get_rect(center=(750, 250))
                    scrub_colour = 'Green'
                elif purple_rect.collidepoint(pos):
                    blue_img.set_alpha(255)
                    green_img.set_alpha(255)
                    purple_img.set_alpha(100)
                    yellow_img.set_alpha(255)
                    scrub_img = pygame.transform.scale(pygame.image.load("imgs/scrub_purple.png"), (400, 300))
                    scrub_rect = scrub_img.get_rect(center=(750, 250))
                    scrub_colour = 'Purple'
                elif yellow_rect.collidepoint(pos):
                    blue_img.set_alpha(255)
                    green_img.set_alpha(255)
                    purple_img.set_alpha(255)
                    yellow_img.set_alpha(100)
                    scrub_img = pygame.transform.scale(pygame.image.load("imgs/scrub_yellow.png"), (400, 300))
                    scrub_rect = scrub_img.get_rect(center=(750, 250))
                    scrub_colour = 'Yellow'

                if default_rect.collidepoint(pos):
                    default_img.set_alpha(100)
                    tank_img.set_alpha(255)
                    acrobat_img.set_alpha(255)
                    text_img = pygame.transform.scale(pygame.image.load("imgs/default_text.png"), (400, 75))
                    text_rect = text_img.get_rect(center=(750, 450))
                    scrub_class = 'default'
                elif tank_rect.collidepoint(pos):
                    default_img.set_alpha(255)
                    tank_img.set_alpha(100)
                    acrobat_img.set_alpha(255)
                    text_img = pygame.transform.scale(pygame.image.load("imgs/tank_text.png"), (400, 75))
                    text_rect = text_img.get_rect(center=(750, 450))
                    scrub_class = 'tank'
                elif acrobat_rect.collidepoint(pos):
                    default_img.set_alpha(255)
                    tank_img.set_alpha(255)
                    acrobat_img.set_alpha(100)
                    text_img = pygame.transform.scale(pygame.image.load("imgs/acrobat_text.png"), (400, 75))
                    text_rect = text_img.get_rect(center=(750, 450))
                    scrub_class = 'acrobat'

            pos = pygame.mouse.get_pos()
            if back_rect.collidepoint(pos):
                back_img.set_alpha(100)
            else:
                back_img.set_alpha(255)

        bg_img.set_alpha(100)

        render()
        time.sleep(.02)


def get_scrub_color():
    return scrub_colour


def get_scrub_class():
    return scrub_class
