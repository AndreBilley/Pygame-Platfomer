from logging import getLoggerClass
import pygame
from Globals import *

class Player():
    def __init__(self, x, y, world):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range (0, 5):
            char_right = pygame.image.load(f'Nea_game_files/Sprites/adventurer-run-{num}.png')
            char_right = self.image = pygame.transform.scale(char_right, (35,50))
            char_left = pygame.transform.flip(char_right, True, False)
            self.images_right.append(char_right)
            self.images_left.append(char_left)
        self.image = self.images_right[self.index] 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.world = world

        
    def update(self, game_over):
        dx,dy = 0,0
        walk_cooldown = 4
  
        if game_over == 0:        
    ################## -Controls- ##################
            key = pygame.key.get_pressed()
            
            
            ###### -Forward- ######
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                self.counter +=1
                self.direction = 1
                dx += 5
                
            if (key[pygame.K_RIGHT] or key[pygame.K_d]) == False and (key[pygame.K_LEFT] or key[pygame.K_a]) == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]  
                if self.direction == -1:
                    self.image = self.images_left[self.index]
            
            ###### -Backward- ######
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.counter += 1
                self.direction = -1
                dx -= 5

            
            ###### -Jump- ######
            if (key[pygame.K_SPACE] or key[pygame.K_UP] or key[pygame.K_w]) and self.jumped == False:
                self.jumped = True
                self.vel_y = -15


            if (key[pygame.K_SPACE] or key[pygame.K_UP] or key[pygame.K_w]) == False:
                self.jumped = False


            
            #### -Gravity- ####
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y
            #~~~~~~~~~~~~~~~~~#    
            
            ###### -Animations- ######
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]  
                if self.direction == -1:
                    self.image = self.images_left[self.index]
            
            ###### -Collisions- ######
            # Check for collisions in the x-direction
            for tile in self.world.tile_list:
                # Check if the character's rectangle collides with the current tile
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    # If there is a collision, set dx to zero to stop the character from moving in the x-direction
                    dx = 0

            # Check for collisions in the y-direction
            for tile in self.world.tile_list:
                # Check if the character's rectangle collides with the current tile
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # If there is a collision and the character is moving upwards (vel_y is negative), adjust dy and stop the upward movement
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # If there is a collision and the character is moving downwards or is stationary (vel_y is non-negative), adjust dy and stop the downward movement
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        
                        
            # Check for collision with enemies
            if pygame.sprite.spritecollide(self, enemy_group, False):
                game_over = -1
            # Check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
            
            self.rect.x += dx
            self.rect.y += dy
        

        
        screen.blit(self.image, self.rect) 
        # pygame.draw.rect(screen, (255,255,255), self.rect, 2,)