import pygame, mainMenu

import Game_Objects
from level_2_tiles import Tile
from level_2_settings import *
from playerScrub import Player
from DirtDemon import Dirt_Demon_1, dirt_demon_2


class Level:
    def __init__(self, level_data, surface):
        # setting up level display
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.collision_no = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.exit_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.dirt_demons = pygame.sprite.Group()
        self.laser_group = pygame.sprite.Group()
        self.heart_group = pygame.sprite.Group()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):

                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size,1)
                    self.tiles.add(tile)
                if cell == 'D':
                    tile = Tile((x, y), tile_size, 2)
                    self.tiles.add(tile)
                if cell == 'G':
                    tile = Tile((x, y), tile_size, 3)
                    self.tiles.add(tile)
                if cell == 'P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Player((x, y), self.tiles,self.laser_group,self.exit_tiles)
                    self.player.add(player_sprite)
                if cell == 'C': # Mr Clean tile
                    tile = Tile((x, y), tile_size, 4)
                    self.exit_tiles.add(tile)
                if cell == 'E':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    dirtDemon_sprite = dirt_demon_2((x, y), self.tiles)
                    self.dirt_demons.add(dirtDemon_sprite)
                if cell == 'R':
                    tile = Tile((x,y), tile_size, 5)
                    self.tiles.add(tile)
                if cell == 'L':
                    tile = Tile((x,y,), tile_size, 6)
                    self.tiles.add(tile)
                if cell == 'M':
                    tile = Tile((x, y), tile_size, 7)
                    self.tiles.add(tile)

        while len(self.heart_group) < self.player.sprite.get_health():
            self.heart_group.add(Game_Objects.Heart((len(self.heart_group) + 1)))

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        dirt_demon = self.dirt_demons.sprites()
        lasers = self.laser_group.sprites()

        if mainMenu.get_scrub_class() == 'default':
            if player_x < w/6 and direction_x < 0:
                self.world_shift = 8
                player.speed = 0
                for dd in dirt_demon:
                    dd.speed_x = -7 * dd.direction.x * -1

                for laser in lasers:
                    if laser.direction.x > 0:
                     laser.speed = -9 * laser.direction.x * -1

                    else:
                        laser.speed = -5 * laser.direction.x * -1


            elif player_x > (w - w/4) and direction_x > 0:
                self.world_shift = -8
                player.speed = 0

                for dd in dirt_demon:
                    dd.speed_x = 9 * dd.direction.x * -1

                for laser in lasers:
                    if laser.direction.x < 0:
                        laser.speed = 9 * laser.direction.x * -1
                    else:
                        laser.speed = 3 * laser.direction.x * -1
            else:
                self.world_shift = 0
                player.speed = 8
                for dd in dirt_demon:
                    dd.speed_x = 1

                for laser in lasers:
                    laser.speed = 3

        elif mainMenu.get_scrub_class() == 'tank':
            if player_x < w / 6 and direction_x < 0:
                self.world_shift = 5
                player.speed = 0
                for dd in dirt_demon:
                    dd.speed_x = -4 * dd.direction.x * -1
                for laser in lasers:
                    if laser.direction.x > 0:
                     laser.speed = -9 * laser.direction.x * -1

                    else:
                        laser.speed = -5 * laser.direction.x * -1

            elif player_x > (w - w / 4) and direction_x > 0:
                self.world_shift = -5
                player.speed = 0
                for dd in dirt_demon:
                    dd.speed_x = 6 * dd.direction.x * -1

                for laser in lasers:
                    if laser.direction.x < 0:
                        laser.speed = 9 * laser.direction.x * -1
                    else:
                        laser.speed = 3 * laser.direction.x * -1
            else:
                self.world_shift = 0
                player.speed = 5
                for dd in dirt_demon:
                    dd.speed_x = 1
                for laser in lasers:
                    laser.speed = 3
        elif mainMenu.get_scrub_class() == 'acrobat':
            if player_x < w / 6 and direction_x < 0:
                self.world_shift = 15
                player.speed = 0
                for dd in dirt_demon:
                    dd.speed_x = -14 * dd.direction.x * -1

                for laser in lasers:
                    if laser.direction.x > 0:
                     laser.speed = -9 * laser.direction.x * -1

                    else:
                        laser.speed = -5 * laser.direction.x * -1
            elif player_x > (w - w / 4) and direction_x > 0:
                self.world_shift = -15
                player.speed = 0
                for dd in dirt_demon:
                    dd.speed_x = 16 * dd.direction.x * -1
                for laser in lasers:
                    if laser.direction.x < 0:
                        laser.speed = 9 * laser.direction.x * -1
                    else:
                        laser.speed = 3 * laser.direction.x * -1
            else:
                self.world_shift = 0
                player.speed = 15
                for dd in dirt_demon:
                    dd.speed_x = 1
                for laser in lasers:
                    laser.speed = 3

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

    def check_quit(self):
        player = self.player.sprite

        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            return True
        if player.is_level_done:
            return True



    def check_game_over(self):
        dmg = self.player.sprite.get_damage()
        if dmg == self.player.sprite.get_health():
            return True
        if self.player.sprite.rect.y > 1000:
            return True
    def run(self):
        #tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        #player
        self.player.update()
        self.laser_group.update()
        self.laser_group.draw(self.display_surface)
        self.dirt_demons.update()
        self.dirt_demons.draw(self.display_surface)
        self.laser_collision()
        self.exit_tiles.update(self.world_shift)
        self.exit_tiles.draw(self.display_surface)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.enemy_collision()
        self.player.draw(self.display_surface)
        self.scroll_x()

        self.heart_group.draw(self.display_surface)
        heart_sprites = self.heart_group.sprites()

        if self.collision_no == 50:
            self.player.sprite.take_damage()

            dmg = self.player.sprite.get_damage()
            if dmg <= self.player.sprite.get_health():
                heart = heart_sprites[self.player.sprite.get_health() - dmg]
                heart.kill()
                self.heart_group.draw(self.display_surface)

                self.collision_no = 0
