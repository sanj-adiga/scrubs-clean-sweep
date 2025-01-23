import pygame
#import platform_Level_1
import random



class Dirt_Demon_1(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("imgs/DirtDemon1_WithoutBG.png"), (90, 90))
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed_x = random.randrange(1, 2) + random.random() + random.random()
        self.speed_y = .5 + random.random()

    def move(self, player_x, player_y):
        # scrub is on the left
        if self.rect.x > player_x:

            self.direction.x = -1
            self.rect.x += self.direction.x * self.speed_x
        # scrub is on the right
        elif self.rect.x < player_x:

            self.direction.x = 1
            self.rect.x += self.direction.x * self.speed_x

        if self.rect.y < player_y:
            self.direction.y = 1
            self.rect.y += self.direction.y * self.speed_y
        if self.rect.y > player_y:
            self.direction.y = -1
            self.rect.y += self.direction.y * self.speed_y

    def update(self, player_x, player_y):
        self.move(player_x, player_y)


class dirt_demon_2(pygame.sprite.Sprite):
    def __init__(self, pos, tiles):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("imgs/DirtDemon2_WithoutBG.png"), (90, 90))
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed_x = 1
        self.speed_y = 0
        self.tiles = tiles
        self.direction.x = -1

    def move(self):
        for sprite in self.tiles:
            if sprite.rect.colliderect(self.rect):
                self.direction = self.direction * -1

        self.rect.x += self.direction.x * self.speed_x

    def update(self):
        self.move()


class mrClean(pygame.sprite.Sprite):
    def __init__(self, pos, tiles):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("imgs/mrClean.png"), (106, 196))
        self.rect = self.image.get_rect(center=pos)
        self.rect.width = 10
        self.rect.height = 10
        self.direction = pygame.math.Vector2(0, 0)
        self.speed_x = random.randrange(1, 2) + random.random() + random.random()
        self.speed_y = .5 + random.random()
        self.tiles = tiles

    def move(self):
        self.rect.colliderect(self)


    def update(self):
        self.rect.y += self.speed_y
        # Check for collisions with other sprites
        for sprite in self.tiles:
            if sprite != self and pygame.sprite.collide_rect(self, sprite):
                self.speed_y *= -1

    def update(self,player_x, player_y):
        self.move(player_x,player_y)
