import pygame
from level_2_settings import *


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.direction = 1  # Start moving downwards


    def update(self):
        self.rect.move_ip(0, self.direction * self.speed)

        # Change direction if the enemy reaches the top or bottom of the screen
        if self.rect.bottom >= h or self.rect.top <= 0:
            self.direction *= -1


    def draw(self, surface):
        surface.blit(self.image, self.rect)
