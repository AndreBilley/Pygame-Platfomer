from logging import getLoggerClass
import pygame
from pygame.locals import *
from Player_Class import *
from Globals import *
from World_Class import *
import pickle
from os import path

# Window setup
pygame.init()
pygame.display.set_caption('Emerald Run')

# FPS control
clock = pygame.time.Clock()
fps = 60

# Load images
bg_img = pygame.image.load('Nea_game_files/Map/glacial_mountains.png')
bg_img = pygame.transform.scale(bg_img, (800,800))
restart_img = pygame.image.load('Nea_game_files/Buttons/Restart_BTN.png')
restart_img = pygame.transform.scale(restart_img, (168,60.7))
start_img = pygame.image.load('Nea_game_files/Buttons/Start_BTN.png')
exit_img = pygame.image.load('Nea_game_files/Buttons/Exit_BTN.png')
title_img = pygame.image.load('Nea_game_files/Map/Title_IMG.png')

# Load level from file
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
    
    
# Class instances
world = World(world_data)
player = Player(40, screen_height - 120, world)
restart_button = Button(screen_width/2 - 50, screen_height/2 + 100, restart_img)
start_button = Button(screen_width/2 - 350, screen_height/2, start_img)
exit_button = Button(screen_width/2 + 98, screen_height/2, exit_img)

#Level reset function
def reset_level(level, world):
    player.reset(40, screen_height - 120, world)
    enemy_group.empty()
    lava_group.empty()
    exit_group.empty()
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
    world = World(world_data)        

    return world


# Run funtions
run = True
while run:

    clock.tick(fps)
    
    screen.blit(bg_img, (0,0))
    
    if start_screen:
        screen.blit(title_img, (screen_width/2-261.5,20))
        if start_button.draw():
            start_screen = False
        if exit_button.draw():
            run = False
    else:
        world.draw()
        
        if game_over == 0:
            enemy_group.update()
        
        elif game_over < 0 and restart_button.draw():
            player.reset(40, screen_height - 120, world)
            game_over = 0
        
        if game_over == 1:
            level += 1
            if level <= max_levels:
                # reset level
                world_data = []
                world = reset_level(level, world)
                game_over = 0
            else:
                # restart game
                pass
            
        enemy_group.draw(screen)
        lava_group.draw(screen)
        exit_group.draw(screen)
        game_over = player.update(game_over)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()