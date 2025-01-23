import pygame
import mainMenu
import time
from support import import_folder
from laser import Laser, Bubble


# As of right now scrub can fit in a 2 block wide gap and is 2 blocks high

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, tiles, laser_group, exit_tiles):
        super().__init__()
        self.get_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15

        self.image = self.animations['move'][self.frame_index]
        self.tiles = tiles
        self.exit_tiles = exit_tiles
        self.rect = self.image.get_rect(topleft=pos)
        self.rect.width = 80
        self.rect.height = 80
        # movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = .8
        self.jump_speed = -16
        self.status = 'idle'
        self.damage = 0
        self.color = mainMenu.get_scrub_color()
        self.get_character_customization()
        # laser
        self.laser_group = laser_group
        self.laser_cooldown = 0
        self.clock = pygame.time.Clock()
        self.is_level_done = False
        self.mouse_down = False

    def get_character_customization(self):
        if mainMenu.get_scrub_class() == 'default':
            self.speed = 8
            self.jump_speed = -16
            self.health = 3
        elif mainMenu.get_scrub_class() == 'tank':
            self.speed = 3
            self.jump_speed = -16
            self.health = 5
        elif mainMenu.get_scrub_class() == 'acrobat':
            self.speed = 15
            self.jump_speed = -16
            self.health = 1

    def get_character_assets(self):
        character_path = './' + mainMenu.get_scrub_color() + 'ScrubPics/'
        self.animations = {'idle': [], 'move': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'move'
            else:
                self.status = 'idle'

    def animate(self):
        animation = self.animations[self.status]
        # loop over frame_index

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

        if keys[pygame.K_2] and self.laser_cooldown <= 0:
            self.fire_laser_right()
            self.laser_cooldown = 1500
        if self.laser_cooldown > 0:
            self.laser_cooldown -= self.clock.tick()

        if keys[pygame.K_1] and self.laser_cooldown <= 0:
            self.fire_laser_left()
            self.laser_cooldown = 1500
        if self.laser_cooldown > 0:
            self.laser_cooldown -= self.clock.tick()
            self.laser_cooldown -= self.clock.tick()

    def get_input_boss(self):
        if pygame.mouse.get_pressed()[0] and self.laser_cooldown <= 0 and not self.mouse_down:
            self.fire_bubble()
            self.laser_cooldown = 10
            self.mouse_down = True

        if self.laser_cooldown > 0:
            self.laser_cooldown -= self.clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = False
                self.laser_cooldown = 0

    def level_done(self):
        level_over = False
        for sprite in self.exit_tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                level_over = True

        if level_over:
            self.is_level_done = True

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        on_ground = False
        self.rect.y += 1
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                on_ground = True
        self.rect.y -= 1
        if on_ground:
            self.direction.y = self.jump_speed

    def fire_laser_right(self):
        laser_pos = (self.rect.right, self.rect.centery)
        laser = Laser(laser_pos)
        laser.direction.x = 1
        self.laser_group.add(laser)

    def fire_laser_left(self):
        laser_pos = (self.rect.left, self.rect.centery)
        laser = Laser(laser_pos)
        laser.direction.x = -1
        self.laser_group.add(laser)


    def fire_bubble(self):
        laser_pos = (self.rect.right, self.rect.centery)
        laser = Bubble(laser_pos)
        laser.direction.x = 1
        self.laser_group.add(laser)

    def update(self):

        self.get_input()
        self.get_status()
        self.animate()
        self.level_done()

    def update_boss(self):

        self.get_input_boss()
        self.level_done()

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def take_damage(self):
        self.damage += 1
