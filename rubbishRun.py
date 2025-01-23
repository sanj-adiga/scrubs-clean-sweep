import pygame, random


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, img_path, screen_rect):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (75, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.rand_xd = random.choice([-1, 1])
        self.rand_yd = random.choice([-1, 1])
        self.speed = 5

        self.screen_rect = screen_rect

    def update(self):
        self.rect = self.rect.move(self.rand_xd * self.speed, self.rand_yd * self.speed)

        if not self.screen_rect.contains(self.rect):
            if self.rect.left < self.screen_rect.left or self.rect.right > self.screen_rect.right:
                self.rand_xd *= -1
            if self.rect.top < self.screen_rect.top or self.rect.bottom > self.screen_rect.bottom:
                self.rand_yd *= -1


class PinkFlower(GameObject):
    def __init__(self, screen_rect):
        rand_x = random.randint(100, screen_rect.width - 100)
        rand_y = random.randint(100, screen_rect.height - 100)
        super().__init__(rand_x, rand_y, "imgs/pinkflower.png", screen_rect)
        self.speed = 5


class BlueFlower(GameObject):
    def __init__(self, screen_rect):
        rand_x = random.randint(100, screen_rect.width - 100)
        rand_y = random.randint(100, screen_rect.height - 100)
        super().__init__(rand_x, rand_y, "imgs/blueflower.png", screen_rect)
        self.speed = 6


class Trash(GameObject):
    def __init__(self, screen_rect):
        rand_x = random.randint(100, screen_rect.width - 100)
        rand_y = random.randint(100, screen_rect.height - 100)
        super().__init__(rand_x, rand_y, 'imgs/trash.png', screen_rect)
        self.speed = 5


class Cans(GameObject):
    def __init__(self, screen_rect):
        rand_x = random.randint(100, screen_rect.width - 100)
        rand_y = random.randint(100, screen_rect.height - 100)
        super().__init__(rand_x, rand_y, 'imgs/cans.png', screen_rect)
        self.speed = 6
