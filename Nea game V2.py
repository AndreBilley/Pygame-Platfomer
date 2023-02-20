from logging import getLoggerClass
import pygame
from pygame.locals import *

pygame.init()

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
# grnd_img = pygame.transform.scale(grnd_img, (800,400))

############-Draw Grid-###############
def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size)) # Horziontal lines
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height)) # Vertical lines

class Player():
    def __init__(self, x, y):
        char = pygame.image.load('Nea_game_files/adventurer.png')
        self.image = pygame.transform.scale(char, (100,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        dx,dy = 0,0
        
        ########### -Controls- ###########
        key = pygame.key.get_pressed()
        
        if key[pygame.K_LEFT]:
            dx -= 5
            print("Left Key Pressed")
            print("x position " + str(self.rect.x))
            print("y position " + str(self.rect.y))
            
        if key[pygame.K_RIGHT]:
            dx += 5
            print("Right Key Pressed")
            print("x position " + str(self.rect.x))
            print("y position " + str(self.rect.y))
            
        
        self.rect.x += dx
        self.rect.y += dy
        
        screen.blit(self.image, self.rect) 
        
               
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