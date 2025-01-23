import pygame


class Grit(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("imgs/Gritty.png"), (90, 90))
        self.rect = self.image.get_rect(center=pos)
        self.alpha_val = 255
        self.rect.width = 90
        self.rect.height = 90
        self.direction = pygame.math.Vector2(0, 0)
        self.speed_x = 1
        self.speed_y = 2

    def move(self, player_x, player_y):
        # scrub is on the left
        if self.rect.x > player_x:

            self.direction.x = -1
            self.rect.x += self.direction.x

    def update(self, player_x, player_y):
        self.move(player_x, player_y)
        self.image.set_alpha(self.alpha_val)

    def update_alpha(self):
        self.alpha_val -= 10.2
