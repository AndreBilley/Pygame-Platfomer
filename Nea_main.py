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
# else:
#     print(f"Error: level{level}_data file not found")
    
    
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
    # else:
    #     print(f"Error: Level{level}_data file not found")
    #     return None


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
        # Game is running
        if game_cond == 0:
            enemy_group.update()
        
        # If player has died
        elif game_cond < 0 and restart_button.draw():
            world_data = []
            world = reset_level(level, world)
            game_cond = 0
        
        # If player has completed level
        if game_cond == 1:
            level += 1
            if level <= max_levels:
                # reset level
                world_data = []
                world = reset_level(level, world)
                game_cond = 0

            else: # If player has completed last level/game
                # restart game
                if restart_button.draw():
                    level = 1
                # reset level
                world_data = []
                world = reset_level(level, world)
                game_cond = 0
            
        enemy_group.draw(screen)
        lava_group.draw(screen)
        exit_group.draw(screen)
        game_cond = player.update(game_cond, world)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()