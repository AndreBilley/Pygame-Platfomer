from logging import getLoggerClass
import pygame
from Globals import *

class World():
    def __init__(self, data):
        self.tile_list = []

        grass_img = pygame.image.load('Nea_game_files/Map/grass.png')
        gravel_img = pygame.image.load('Nea_game_files/Map/gravel.png')
        emerald_forest_sign = pygame.image.load('Nea_game_files/Map/EmeraldForest_sign.png')

        row_count = 0
        for row in data: # Each individual row
            col_count = 0
            for tile in row: # Each individual tile
                if tile == 1:
                    img = pygame.transform.scale(gravel_img, (tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                
                if tile == 3:
                    enemy = Enemy(col_count * tile_size + 6.5, row_count * tile_size + 13)
                    enemy_group.add(enemy)
                    
                if tile == 4:
                    lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size/2))
                    lava_group.add(lava)
                    
                if tile == 5:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size/2))
                    exit_group.add(exit)
                    
                if tile == 6:
                    img = pygame.transform.scale(emerald_forest_sign, (tile_size*1.5,tile_size*1.5))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size - 20
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    
                if tile == 7:
                    emerald = Emerald(col_count * tile_size + (tile_size / 2), row_count * tile_size + (tile_size / 2))
                    emerald_group.add(emerald)                
    
                col_count += 1
            row_count += 1
                

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            # pygame.draw.rect(screen, (255,255,255), tile[1], 2)
     
     
class Entity(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        entity_img = pygame.image.load(image_path)
        self.image = pygame.transform.scale(entity_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__('Nea_game_files/Sprites/enemy_01.png', x, y, 27, 27)
        self.enemy_direction = 1
        self.enemy_counter = 0

    def update(self):
        self.rect.x += self.enemy_direction
        self.enemy_counter += 1
        if self.enemy_counter > 40:
            self.enemy_direction *= -1
            self.enemy_counter *= -1

class Lava(Entity):
    def __init__(self, x, y):
        super().__init__('Nea_game_files/Map/lava.png', x, y, tile_size, tile_size / 2)

class Emerald(Entity):
    def __init__(self, x, y):
        super().__init__('Nea_game_files/Map/emerald.png', x, y, tile_size / 1.5 , tile_size / 1.5)
        self.rect.center = (x, y)

class Exit(Entity):
    def __init__(self, x, y):
        super().__init__('Nea_game_files/Map/exit.png', x, y, tile_size, tile_size * 1.5)
        
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        
    def draw(self):
        action = False
        
        # Get mouse position
        pos = pygame.mouse.get_pos()
        
        # Check mouse collision and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        # Draw button
        screen.blit(self.image, self.rect)
        # Icons
        score_icon = Emerald(tile_size / 2, tile_size / 2)
        emerald_group.add(score_icon)
                
        return action
