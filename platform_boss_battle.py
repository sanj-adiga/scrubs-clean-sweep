import time

import pygame, mainMenu

import Game_Objects
from level_3_settings import *
from level_3_tiles import Tile
from playerScrub import Player
from laser import Bubble
from Grit import Grit


class Level:
    def __init__(self, level_data, surface):
        # setting up level display
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.collision_no = 0
        self.grit_hit = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.exit_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.laser_group = pygame.sprite.Group()
        self.grit = pygame.sprite.Group()

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
                    grit_sprite = Grit((x, y))
                    self.grit.add(grit_sprite)

        self.world_height = len(layout) * tile_size

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
        shooter = pygame.sprite.groupcollide(self.laser_group, self.grit, True, False)
        if shooter:
            self.laser_group.remove()
            self.grit_hit += 1
            for sprite in self.grit:
                sprite.update_alpha()

    def enemy_collision(self):
        grit_player = pygame.sprite.groupcollide(self.grit, self.player, True, True)
        if grit_player:
            self.player.remove()
            self.collision_no += 1

    def check_quit(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            return True

    def check_game_over(self):
        if self.collision_no >= 1:
            return True

    def check_win(self):
        if self.grit_hit == 25:
            for sprite in self.grit:
                sprite.kill()

            return True

    def run(self):
        # tiles
        self.tiles.update(self.world_shift_x, self.world_shift_y)
        self.tiles.draw(self.display_surface)
        self.exit_tiles.update(self.world_shift_x, self.world_shift_y)
        self.exit_tiles.draw(self.display_surface)
        # player
        self.player.sprite.update_boss()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        # laser
        self.laser_group.update()
        self.laser_group.draw(self.display_surface)
        # enemy
        self.grit.update(self.player.sprite.rect.x, self.player.sprite.rect.y)
        self.grit.draw(self.display_surface)
        self.laser_collision()
        self.enemy_collision()


