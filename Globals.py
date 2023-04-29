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
location = ['Glacial Mountains', 'Emerald Forest', 'Withered Willows']
current_location = 0
max_levels = 4
emeralds = 0
start_screen = True
paused = False
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
emerald_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
gold_exit_group = pygame.sprite.Group()
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