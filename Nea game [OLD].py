import pygame
import sys
from sys import exit
from random import randint

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#yo

# sky_surf = pygame.image.load("mountain/background_glacial_mountains.png").convert_alpha()
sky_surf = pygame.image.load("./Nea_game_files/sky.png").convert_alpha()
mount_surf = pygame.image.load(
    "./Nea_game_files/glacial_mountains.png").convert_alpha()

cloud_surf = pygame.image.load(
    "./Nea_game_files/clouds_mg_2.png").convert_alpha()
ground_surf = pygame.image.load("./Nea_game_files/ground.png").convert_alpha()
# char_surf = pygame.image.load(r"adventurer-idle-00.png")

x = 150
y = 100
width = 40
height = 60
vel = 5


sky_surf = pygame.transform.scale(sky_surf, (800, 400))
mount_surf = pygame.transform.scale(mount_surf, (800, 400))
cloud_surf = pygame.transform.scale(cloud_surf, (800, 400))
# char_surf = pygame.transform.scale(char_surf, (150, 100))

screen.blit(sky_surf, (0, 0))
screen.blit(cloud_surf, (0, -160))
screen.blit(mount_surf, (0, 0))
screen.blit(ground_surf, (0, 400))
# screen.blit(char_surf, (0, 300))

class Player():
    def __init__(self, x, y):
        char = pygame.image.load('./Nea_game_files/adventurer-idle-00.png')
        self.image = pygame.transform.scale(char, (150, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.vel_y = 0
        # self.jumped = False

    def update(self):
        dx = 0
        dy = 0
        # Get key presses
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 1
        if key[pygame.K_RIGHT]:
            dx += 1

        # Update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0
            
        
        
        
        
        # Draw character on
        screen.blit(self.image, self.rect)
    




player = Player(0,screen_height - 300)


run = True
while run:
    player.update()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

























# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit(); sys.exit()
#             main = False

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT or event.key == ord('a'):
#                 print('left')
#             if event.key == pygame.K_RIGHT or event.key == ord('d'):
#                 print('right')
#             if event.key == pygame.K_UP or event.key == ord('w'):
#                 print('jump')

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == ord('a'):
#                 print('left stop')
#             if event.key == pygame.K_RIGHT or event.key == ord('d'):
#                 print('right stop')
#             if event.key == ord('q'):
#                 pygame.quit()
#                 sys.exit()
#                 main = False    
