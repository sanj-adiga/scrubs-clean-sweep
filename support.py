from os import walk
import pygame

#scrub = pygame.transform.scale(pygame.image.load("BlueScrubWithoutBG.png"), (94, 90))
def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surface = pygame.transform.scale(pygame.image.load(full_path), (94,90)).convert_alpha()
            surface_list.append(image_surface)

    return surface_list
