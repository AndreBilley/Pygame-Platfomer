import pygame
pygame.init()

# Screen configuration
screen_width = 800
screen_height = 800
tile_size = 40
screen = pygame.display.set_mode((screen_width, screen_height))

# Level configuration
game_cond = 0
level = 5
location = ['Glacial Mountains', 'Emerald Forest', 'Withered Willows', 'Infernal Caverns']
current_location = 0
max_levels = 9
emeralds = 0
start_screen = True
paused = False
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
emerald_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
gold_exit_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()

# GUI configuration
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255,215,0)
text_font = "Nea_game_files/Map/PressStart2P.ttf"
text_font_size = 70
text_font = pygame.font.Font(text_font, text_font_size)
UI_font = pygame.font.SysFont('Bauhaus 93', 30)

# Load sounds
title_music = pygame.mixer.Sound('Nea_game_files/Sounds/Title_Theme.wav')
title_music.set_volume(0.25)
glacial_music = pygame.mixer.Sound('Nea_game_files/Sounds/Glacial_music.wav')
glacial_music.set_volume(0.5)
e_forest_music = pygame.mixer.Sound('Nea_game_files/Sounds/e_forest_music.wav')
e_forest_music.set_volume(0.5)
w_willows_music = pygame.mixer.Sound('Nea_game_files/Sounds/w_willows_music.wav')
w_willows_music.set_volume(0.5)
endgame_music = pygame.mixer.Sound('Nea_game_files/Sounds/endgame_music.wav')
endgame_music.set_volume(0.5)
final_level_music = pygame.mixer.Sound('Nea_game_files/Sounds/final_level_music.wav')
final_level_music.set_volume(0.5)
emerald_fx = pygame.mixer.Sound('Nea_game_files/Sounds/emerald.wav')
emerald_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('Nea_game_files/Sounds/jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('Nea_game_files/Sounds/game_over.wav')
game_over_fx.set_volume(0.5)