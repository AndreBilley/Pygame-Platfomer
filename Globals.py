import pygame
pygame.init()
# Screen configuration
screen_width = 800
screen_height = 800
tile_size = 40
screen = pygame.display.set_mode((screen_width, screen_height))
# Level configuration
game_cond = 0
level = 1
max_levels = 3
emeralds = 0
start_screen = True
paused = False
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
emerald_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
# GUI configuration
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255,255,0)
text_font = "Nea_game_files/Map/PressStart2P.ttf"
UI_font = "Nea_game_files/Map/Roboto.ttf"
UI_font_size = 25
font_size = 70
text_font = pygame.font.Font(text_font, font_size)
UI_font = pygame.font.Font(UI_font, UI_font_size)