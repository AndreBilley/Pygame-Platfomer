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
max_levels = 1
emeralds = 0
start_screen = True
paused = False
# Sprite configuration
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
emerald_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
# GUI configuration
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
UI_font = pygame.font.SysFont('Bauhaus 93 ', 30)
font = pygame.font.SysFont('Bauhaus 93', 70)