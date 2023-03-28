from logging import getLoggerClass
import pygame
from pygame.locals import *
from Player_Class import *
from Globals import *
from World_Class import *

# Window setup
pygame.init()
pygame.display.set_caption('Platformer')

# FPS control
clock = pygame.time.Clock()
fps = 60

# Load images
bg_img = pygame.image.load('Nea_game_files/glacial_mountains.png')
grnd_img = pygame.image.load('Nea_game_files/ground.png')
bg_img = pygame.transform.scale(bg_img, (800,800))


# Class instances
world = World(world_data)
player = Player(40, screen_height - 120, world)

# Run funtions
run = True
while run:

    clock.tick(fps)
    
    screen.blit(bg_img, (0,0))

    world.draw()
    game_over = player.update(game_over)
    enemy_group.update()
    enemy_group.draw(screen)
    lava_group.draw(screen)
    
    print(game_over)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()