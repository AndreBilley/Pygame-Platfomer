from logging import getLoggerClass
import pygame
from Globals import *

class Player():
    def __init__(self, x, y, world):
        self.reset(x, y, world)

        
    def update(self, game_cond, world):
        global level
        global platform
        dx,dy = 0,0
        col_thresh = 22
        walk_cooldown = 4
  
        if game_cond == 0:        
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
            if pygame.sprite.spritecollide(self, powerup_group, True):
                self.stat_boost = True
            if (key[pygame.K_SPACE] or key[pygame.K_UP] or key[pygame.K_w]) and self.jumped == False and self.in_air == False:
                jump_fx.play() # Play jump sound
                self.jumped = True
                self.in_air = True
                if self.stat_boost:
                    self.vel_y = -22
                else:
                    self.vel_y = -15


            if (key[pygame.K_SPACE] or key[pygame.K_UP] or key[pygame.K_w]) == False:
                self.jumped = False


            
            #### -Gravity- ####
            self.vel_y += 1
            if self.stat_boost:
                if self.vel_y > 20:
                    self.vel_y = 20
            else:
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
            for tile in world.tile_list:
                # Check if the character's rectangle collides with the current tile
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    # If there is a collision, set dx to zero to stop the character from moving in the x-direction
                    dx = 0

            # Check for collisions in the y-direction
            for tile in world.tile_list:
                # Check if the character's rectangle collides with the current tile
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # If there is a collision and the character is jumping (vel_y is negative), adjust dy and stop the upward movement
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # If there is a collision and the character is moving downwards or is stationary (vel_y is non-negative), adjust dy and stop the downward movement
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False
                        

            # Check for collision with enemies
            if pygame.sprite.spritecollide(self, enemy_group, False):
                game_cond = -2
                game_over_fx.play()
            # Check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_cond = -1
                game_over_fx.play()
            # Check for collision with exit
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_cond = 1
            # Check for collision with gold exit
            if pygame.sprite.spritecollide(self, gold_exit_group, False):
                game_cond = 3
                
                
            # Check for collision with platforms
            for platform in platform_group:
                # Collision in the x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # Collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # Check if below platform
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    # Check if above platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        dy = 0
                    # Move sideways with platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
           
            # Update player coodinates
            self.rect.x += dx
            self.rect.y += dy
        
        elif game_cond == -1: # If touching lava, character's soul will ascend
            self.image = self.dead
            if self.rect.y > -40:
                self.rect.y -= 5
        
        elif game_cond == -2: # If touching enemy, character's soul will descend
            self.image = self.dead
            if self.rect.y < 800:
                self.rect.y += 5

        
        screen.blit(self.image, self.rect) 
        
        return game_cond
    
    def reset(self, x, y, world):
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
        self.dead = pygame.image.load('Nea_game_files/Sprites/death_img.png')
        self.dead = pygame.transform.scale(self.dead, (40,40))
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
        self.in_air = False
        self.stat_boost = False