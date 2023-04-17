import pygame
screen_width = 800
screen_height = 800
level = 1
max_levels = 3
tile_size = 40
game_cond = 0
start_screen = True
screen = pygame.display.set_mode((screen_width, screen_height))
enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()