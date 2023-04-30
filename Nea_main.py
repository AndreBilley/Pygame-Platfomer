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
mountains_img = pygame.image.load('Nea_game_files/Map/mountains.png')
mountains_img = pygame.transform.scale(mountains_img, (screen_width, screen_height))
greenforest_img = pygame.image.load('Nea_game_files/Map/greenforest.png')
greenforest_img = pygame.transform.scale(greenforest_img, (screen_width, screen_height))
bg_img = mountains_img
ground_img = pygame.image.load('Nea_game_files/Map/ground.png')
ground_img = pygame.transform.scale(ground_img, (screen_width, 150))
restart_img = pygame.image.load('Nea_game_files/Buttons/Restart_BTN.png')
start_img = pygame.image.load('Nea_game_files/Buttons/Start_BTN.png')
exit_img = pygame.image.load('Nea_game_files/Buttons/Exit_BTN.png')
quit_img = pygame.image.load('Nea_game_files/Buttons/Quit_BTN.png')
title_img = pygame.image.load('Nea_game_files/Map/Title_IMG.png')
paused_img = pygame.image.load('Nea_game_files/Map/Paused_Text.png')
resume_img = pygame.image.load('Nea_game_files/Buttons/Resume_BTN.png')
pause_img = pygame.image.load('Nea_game_files/Buttons/Pause_BTN.png')
pause_img = pygame.transform.scale(pause_img, (36,42.5))
emerald_img = pygame.image.load('Nea_game_files/Map/emerald.png')
emerald_img = pygame.transform.scale(emerald_img, (tile_size / 1.5 , tile_size / 1.5))

# Load level from file
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
# else:
#     print(f"Error: level{level}_data file not found")
    
    
# Class instances
world = World(world_data)
player = Player(40, screen_height - 120, world)
restart_button = Button(screen_width/2 - 350, screen_height/2, restart_img)
start_button = Button(screen_width/2 - 350, screen_height/2, start_img)
exit_button = Button(screen_width/2 + 98, screen_height/2, exit_img)
quit_button = Button(screen_width/2 + 98, screen_height/2, quit_img)
resume_button = Button(screen_width/2 - 350, screen_height/2, resume_img)
pause_button = Button(screen_width - 35, 5, pause_img)

# Level reset function
def reset_level(level, world):
    player.reset(40, screen_height - 120, world)
    enemy_group.empty()
    lava_group.empty()
    exit_group.empty()
    emerald_group.empty()
    gold_exit_group.empty()
    powerup_group.empty()
    player.stat_boost = False
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
        world = World(world_data)        
        return world

# Start screen
def main_menu():
    global start_screen
    global run
    screen.blit(title_img, (screen_width/2-261.5, 40))
    screen.blit(ground_img, (0, 650))
    if start_button.draw():
        start_screen = False
    if exit_button.draw():
        run = False       

# Pause menu
def pause_menu():
    global game_cond
    global paused
    global run
    paused = True
    screen.blit(paused_img, (screen_width/2-261.5, 40))
    if resume_button.draw():
        game_cond = 0
        paused = False
    if quit_button.draw():
        run = False
              
# Draw text           
def draw_text(text, size, text_col, x, y):
    global text_font
    global UI_font
    if size == 'text':
        img = text_font.render(text, True, text_col)
        screen.blit(img, (x, y))
    elif size == 'UI':
        img = UI_font.render(text, True, text_col)
        screen.blit(img, (x, y)) 
     
# Update score
def update_score():
    global emeralds
    screen.blit(emerald_img, (screen_width - 137, 7))
    # Check for collision with emerald
    if pygame.sprite.spritecollide(player, emerald_group, True):
        emeralds += 1
    if player.stat_boost:
        if pygame.sprite.spritecollide(player, enemy_group, True):
            emeralds += 2
    draw_text('X ' + str(emeralds), 'UI', green, screen_width - 110, 4)
    
def level_info():
    # Declaring global variables
    global location
    global level
    global current_location
    if level % 4 == 0 and level != 0: # Every 4th level (Every 3 levels)
        current_location = (level // 4) % len(location) # Current location will increase on every 4th level
    # Displaying text on window
    draw_text(f'Level {level}', 'UI', green, screen_width/2 - 30, 5)
    draw_text(f'Location: {location[current_location]}', 'UI', blue, screen_width/2 - 160, 45)
    
    


# Run functions
run = True
while run:

    clock.tick(fps)
    
    if level > 3:
        bg_img = greenforest_img
    
    screen.blit(bg_img, (0,0))
    
    # Start screen functionality
    if start_screen:
        main_menu()

    else:
        world.draw()
        # Game is running
        if game_cond == 0:
            enemy_group.update()
            update_score()
            level_info()
            
        # Pause menu functionality
        if paused:
            pause_menu()
        if pause_button.draw():
            paused = True
            game_cond = 2
        
        # If player has died
        if game_cond < 0:
            draw_text('YOU LOSE', 'text', red, (screen_width / 2) - 270, screen_height / 2 - 200)
            if restart_button.draw():
                world_data = []
                world = reset_level(level, world)
                game_cond = 0
                emeralds = 0
                player.stat_boost = False
            if quit_button.draw():
                run = False
        
        # If player has completed level
        if game_cond == 1 or game_cond == 3:
            # regular exit
            if game_cond == 1:
                level += 1
            # gold exit
            if game_cond == 3:
                level += 2
            if level <= max_levels:
                # reset level
                world_data = []
                world = reset_level(level, world)
                player.stat_boost = False
                game_cond = 0

            else: # If player has completed last level/game
                draw_text('YOU WIN!', 'text', green, (screen_width / 2) - 270, screen_height / 2 - 200)
                # restart game
                if restart_button.draw():
                    level = 1
                    # reset level
                    world_data = []
                    bg_img = mountains_img
                    world = reset_level(level, world)
                    game_cond = 0
                    emeralds = 0
                if exit_button.draw():
                    run = False
            
        enemy_group.draw(screen)
        lava_group.draw(screen)
        emerald_group.draw(screen)
        exit_group.draw(screen)
        gold_exit_group.draw(screen)
        pause_button.draw()
        powerup_group.draw(screen)
        game_cond = player.update(game_cond, world)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()