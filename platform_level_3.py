import pygame, mainMenu

import Game_Objects
from level_3_settings import *
from level_3_tiles import Tile
from playerScrub import Player
from laser import Laser
from DirtDemon import dirt_demon_2, Dirt_Demon_1
import random

class Level:
    def __init__(self, level_data, surface):
        # setting up level display
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.collision_no = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.exit_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.laser_group = pygame.sprite.Group()
        self.dirt_demons = pygame.sprite.Group()
        self.heart_group = pygame.sprite.Group()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):

                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size,1)
                    self.tiles.add(tile)
                if cell == 'D':
                    tile = Tile((x, y), tile_size, 3)
                    self.tiles.add(tile)

                if cell == 'E':
                    tile = Tile((x, y), tile_size, 4)
                    self.exit_tiles.add(tile)

                if cell =='P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Player((x, y), self.tiles, self.laser_group, self.exit_tiles)
                    self.player.add(player_sprite)

                if cell == '1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    dirtDemon_sprite = Dirt_Demon_1((x, y))
                    self.dirt_demons.add(dirtDemon_sprite)

        self.world_height = len(layout) * tile_size

        while len(self.heart_group) < self.player.sprite.get_health():
            self.heart_group.add(Game_Objects.Heart((len(self.heart_group) + 1)))

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if mainMenu.get_scrub_class() == 'default':
            player.speed = 8
        elif mainMenu.get_scrub_class() == 'tank':
            player.speed = 3
        elif mainMenu.get_scrub_class() == 'acrobat':
            player.speed = 15

    def scroll_y(self):
        player = self.player.sprite
        dirt_demon = self.dirt_demons.sprites()
        player_y = player.rect.centery
        direction_y = player.direction.y
        lasers = self.laser_group.sprites()

        if player_y < h / 6 and direction_y < 0:
            self.world_shift_y = 8
            for laser in lasers:
                laser.speed_y = 8
                laser.direction.y = 1

            for dd in dirt_demon:
                if dd.direction.y < 0:
                    dd.speed_y = -8
                    dd.direction.y = -1

        elif player_y > (h - h / 4) and direction_y > 0: # world is going down
            self.world_shift_y = -8
            for laser in lasers:

                laser.direction.y = -1
                laser.speed_y = 8

            for dd in dirt_demon:
                if dd.direction.y > 0:
                    dd.speed_y = -8
                    dd.direction.y = -1
        else:
            self.world_shift_y = 0
            player.speed = 8
            for laser in lasers:
                laser.direction.y = 0

            for dd in dirt_demon:
                dd.speed_y = .5 + random.random()
                dd.direction.y = 0

        if player.rect.top < 0:
            player.rect.top = 0
        elif player.rect.bottom > self.world_height:
            player.rect.bottom = self.world_height

        player.rect.y += self.world_shift_y

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0

                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def laser_collision(self):
        shooter = pygame.sprite.groupcollide(self.laser_group, self.dirt_demons, True, True)
        if shooter:
            self.laser_group.remove()
            self.dirt_demons.remove()

    def enemy_collision(self):
        player = self.player.sprite

        for sprite in self.dirt_demons:
            if sprite.rect.colliderect(player.rect):
                self.collision_no += 1
        # for sprite in self.dirt_demons_2:
        #     if sprite.rect.colliderect(player.rect):
        #         self.collision_no += 1

    def dirt_demon_collision(self):
        shooter = pygame.sprite.groupcollide(self.dirt_demons, self.player, True, True)
        if shooter:
            # health bar down one, remove life
            self.player.remove()

    def check_quit(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            return True
        if self.player.sprite.is_level_done:
            return True

    def check_game_over(self):
        dmg = self.player.sprite.get_damage()
        if dmg == self.player.sprite.get_health():
            return True

    def run(self):
        # tiles
        self.tiles.update(self.world_shift_x, self.world_shift_y)
        self.tiles.draw(self.display_surface)
        self.exit_tiles.update(self.world_shift_x, self.world_shift_y)
        self.exit_tiles.draw(self.display_surface)
        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.enemy_collision()
        self.player.draw(self.display_surface)
        # laser
        self.laser_group.update()
        self.laser_group.draw(self.display_surface)
        # enemy
        self.dirt_demons.update(self.player.sprite.rect.x, self.player.sprite.rect.y)
        self.dirt_demons.draw(self.display_surface)
        self.laser_collision()
        # self.scroll_x()
        self.scroll_y()
        self.scroll_x()

        self.heart_group.draw(self.display_surface)
        heart_sprites = self.heart_group.sprites()

        if self.collision_no == 50:
            self.player.sprite.take_damage()

        # TODO: damage is weird in level 3 !oh no!
            dmg = self.player.sprite.get_damage()
            if dmg <= self.player.sprite.get_health():
                heart = heart_sprites[self.player.sprite.get_health() - dmg]
                heart.kill()
                self.heart_group.draw(self.display_surface)

                self.collision_no = 0
