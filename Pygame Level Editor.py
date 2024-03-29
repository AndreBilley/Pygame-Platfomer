import pygame
import pickle
from os import path


pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
tile_size = 40
cols = 20
margin = 100
screen_width = tile_size * cols
screen_height = (tile_size * cols) + margin

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level Editor')


#load images
bg_img = pygame.image.load('Nea_game_files/Map/mountains.png')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height - margin))
gravel_img = pygame.image.load('Nea_game_files/Map/gravel.png')
grass_img = pygame.image.load('Nea_game_files/Map/grass.png')
enemy_img = pygame.image.load('Nea_game_files/Sprites/enemy_01.png')
lava_img = pygame.image.load('Nea_game_files/Map/lava.png')
emerald_img = pygame.image.load('Nea_game_files/Map/Emerald.png')
exit_img = pygame.image.load('Nea_game_files/Map/exit.png')
gold_exit_img = pygame.image.load('Nea_game_files/Map/exit2.png')
save_img = pygame.image.load('Nea_game_files/Buttons/Save_BTN.png')
save_img = pygame.transform.scale(save_img, (168,60.7))
load_img = pygame.image.load('Nea_game_files/Buttons/Load_BTN.png')
load_img = pygame.transform.scale(load_img, (168,60.7))
emerald_forest_sign = pygame.image.load('Nea_game_files/Map/EmeraldForest_sign.png')
powerup_img = pygame.image.load('Nea_game_files/Map/powerup.png')
platform_x = pygame.image.load('Nea_game_files/Map/platform_x.png')
platform_y = pygame.image.load('Nea_game_files/Map/platform_y.png')

#define game variables
clicked = False
level = 1

#define colours
white = (255, 255, 255)
green = (144, 201, 120)
black = (0,0,0)

font = pygame.font.SysFont('Futura', 24)

#create empty tile list
world_data = []
for row in range(20):
	r = [0] * 20
	world_data.append(r)

#create boundary
for tile in range(0, 20):
	world_data[19][tile] = 2
	world_data[0][tile] = 1
	world_data[tile][0] = 1
	world_data[tile][19] = 1

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

def draw_grid():
	for c in range(21):
		#vertical lines
		pygame.draw.line(screen, white, (c * tile_size, 0), (c * tile_size, screen_height - margin))
		#horizontal lines
		pygame.draw.line(screen, white, (0, c * tile_size), (screen_width, c * tile_size))


def draw_world():
	for row in range(20):
		for col in range(20):
			if world_data[row][col] > 0:
				if world_data[row][col] == 1:
					#dirt blocks
					img = pygame.transform.scale(gravel_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 2:
					#grass blocks
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 3:
					#enemy blocks
					img = pygame.transform.scale(enemy_img, (tile_size, int(tile_size * 0.75)))
					screen.blit(img, (col * tile_size, row * tile_size + (tile_size * 0.25)))
				if world_data[row][col] == 4:
					#lava
					img = pygame.transform.scale(lava_img, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size + (tile_size // 2)))
				if world_data[row][col] == 5:
					#exit
					img = pygame.transform.scale(exit_img, (tile_size, int(tile_size * 1.5)))
					screen.blit(img, (col * tile_size, row * tile_size - (tile_size // 2)))
				if world_data[row][col] == 6:
					#sign
					img = pygame.transform.scale(emerald_forest_sign, (tile_size * 1.5, tile_size * 1.5))
					screen.blit(img, (col * tile_size, row * tile_size - 20))     
				if world_data[row][col] == 7:
					#emerald
					img = pygame.transform.scale(emerald_img, (tile_size // 2, tile_size // 2))
					screen.blit(img, (col * tile_size + (tile_size // 4), row * tile_size + (tile_size // 4)))
				if world_data[row][col] == 8:
					#gold exit
					img = pygame.transform.scale(gold_exit_img, (tile_size, int(tile_size * 1.5)))
					screen.blit(img, (col * tile_size, row * tile_size - (tile_size // 2)))
				if world_data[row][col] == 9:
					#powerup
					img = pygame.transform.scale(powerup_img, (tile_size // 2, tile_size // 2))
					screen.blit(img, (col * tile_size + (tile_size // 4), row * tile_size + (tile_size // 4)))
				if world_data[row][col] == 10:
					#horizontally moving platform
					img = pygame.transform.scale(platform_x, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 11:
					#vertically moving platform
					img = pygame.transform.scale(platform_y, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size))

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return action

#create load and save buttons
save_button = Button(screen_width // 2 - 210, screen_height - 80, save_img)
load_button = Button(screen_width // 2, screen_height - 80, load_img)

#main game loop
run = True
while run:

	clock.tick(fps)

	#draw background
	screen.fill(green)
	screen.blit(bg_img, (0, 0))
	# screen.blit(sun_img, (tile_size * 2, tile_size * 2))

	#load and save level
	if save_button.draw():
		#save level data
		pickle_out = open(f'level{level}_data','wb')
		pickle.dump(world_data, pickle_out)
		pickle_out.close()
	if load_button.draw():
		#load in level data
		if path.exists(f'level{level}_data'):
			pickle_in = open(f'level{level}_data', 'rb')
			world_data = pickle.load(pickle_in)


	#show the grid and draw the level tiles
	draw_grid()
	draw_world()


	#text showing current level
	draw_text(f'Level: {level}', font, black, tile_size - 20, screen_height - 40)
	draw_text('Press UP or DOWN to change level', font, black, tile_size - 20, screen_height - 20)

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
		#mouseclicks to change tiles
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
			pos = pygame.mouse.get_pos()
			x = pos[0] // tile_size
			y = pos[1] // tile_size
			#check that the coordinates are within the tile area
			if x < 20 and y < 20:
				#update tile value
				if pygame.mouse.get_pressed()[0] == 1:
					world_data[y][x] += 1
					if world_data[y][x] > 11:
						world_data[y][x] = 0
				elif pygame.mouse.get_pressed()[2] == 1:
					world_data[y][x] -= 1
					if world_data[y][x] < 0:
						world_data[y][x] = 11
		if event.type == pygame.MOUSEBUTTONUP:
			clicked = False
		#up and down key presses to change level number
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				level += 1
			elif event.key == pygame.K_DOWN and level > 1:
				level -= 1

	#update game display window
	pygame.display.update()

pygame.quit()