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
bg_img = pygame.image.load('Nea_game_files/Map/glacial_mountains.png')
bg_img = pygame.transform.scale(bg_img, (800,800))
restart_img = pygame.image.load('Nea_game_files/Buttons/Restart_BTN.png')
restart_img = pygame.transform.scale(restart_img, (168,60.7))


# Class instances
world = World(world_data)
player = Player(40, screen_height - 120, world)
# Buttons
restart_button = Button(screen_width //2 - 50, screen_height //2 + 100, restart_img )

# Run funtions
run = True
while run:

    clock.tick(fps)
    
    screen.blit(bg_img, (0,0))

    world.draw()
    
    if game_over == 0:
        enemy_group.update()
    
    else:
        if restart_button.draw():
            player.reset(40, screen_height - 120, world)
            game_over = 0
            print("Reset")
        
    
    enemy_group.draw(screen)
    lava_group.draw(screen)
    game_over = player.update(game_over)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()