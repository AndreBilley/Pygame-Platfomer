from logging import getLoggerClass
import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

# Define game variables
tile_size = 40

# Load images
bg_img = pygame.image.load('Nea_game_files/glacial_mountains.png')
grnd_img = pygame.image.load('Nea_game_files/ground.png')
bg_img = pygame.transform.scale(bg_img, (800,800))

############-Draw Grid-###############
def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size)) # Horziontal lines
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height)) # Vertical lines

class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        # char = pygame.image.load('Nea_game_files/Sprites/adventurer-idle-0.png')
        for num in range (0, 5):
            char_right = pygame.image.load(f'Nea_game_files/Sprites/adventurer-run-{num}.png')
            char_right = self.image = pygame.transform.scale(char_right, (40,50))
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

        
    def update(self):
        dx,dy = 0,0
        walk_cooldown = 3
        
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
            self.counter +=1
            self.direction = -1
            dx -= 5

        
        ###### -Jump- ######
        if (key[pygame.K_SPACE] or key[pygame.K_UP] or key[pygame.K_w]) and self.jumped == False:
            self.jumped = True
            self.vel_y = -15

        if (key[pygame.K_SPACE] or key[pygame.K_UP] or key[pygame.K_w]) == False:
            self.jumped = False

        ###### -Collisions- ######
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
          
        #### -Gravity- ####
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
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
           
           
        dy += self.vel_y
        
        
        self.rect.x += dx
        self.rect.y += dy
        

        
        screen.blit(self.image, self.rect) 
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)
        
               
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
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255,255,255), tile[1], 2)


world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


world = World(world_data)
player = Player(40, screen_height - 120)


run = True
while run:

    clock.tick(fps)
    
    screen.blit(bg_img, (0,0))
    # screen.blit(grnd_img, (100,100))

    world.draw()
    player.update()

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()