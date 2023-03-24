from logging import getLoggerClass
import pygame
from Globals import *

class World():
    def __init__(self, data):
        self.tile_list = []

        grass_img = pygame.image.load('Nea_game_files/grass.png')
        gravel_img = pygame.image.load('Nea_game_files/gravel.png')

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
                    blob = Enemy(col_count * tile_size + 6.5, row_count * tile_size + 13)
                    blob_group.add(blob)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            # pygame.draw.rect(screen, (255,255,255), tile[1], 2)
     
     
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Nea_game_files/Sprites/enemy_01.png')
        self.image = pygame.transform.scale(self.image, (27,27))
        self.rect = self.image.get_rect()
        self.rect.x  = x
        self.rect.y  = y
        self.move_direction = 1
        self.move_counter = 0
        
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter > 40:
            self.move_direction *= -1
            self.move_counter *= -1
            

blob_group = pygame.sprite.Group()
