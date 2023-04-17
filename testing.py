import pygame


pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

# Load images
bg_img = pygame.image.load('Nea_game_files/Map/greenforest.png')
bg_img = pygame.transform.scale(bg_img, (800,800))

run = True
while run:

    screen.blit(bg_img, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()