import pygame

laser_group = pygame.sprite.Group()

class Laser(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("imgs/bubblelasers.png").convert_alpha(), (175, 50))
        self.rect = self.image.get_rect(center=position)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3
        self.speed_y = 0

    def update(self):
        self.rect.move_ip(self.direction.x * self.speed, 0)
        self.rect.move_ip(0, self.direction.y * self.speed_y)
        if self.rect.right < 0:
            laser_group.remove(self)

class Bubble(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('imgs/bubble.png').convert_alpha(), (25, 25))
        self.rect = self.image.get_rect(center=position)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3

    def update(self):
        self.rect.move_ip(self.direction.x * self.speed, 0)
        if self.rect.right < 0:
            laser_group.remove(self)

