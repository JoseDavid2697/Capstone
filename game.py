import pygame
from pygame.locals import *
import os
import pickle
import requests
from dotenv import load_dotenv

load_dotenv()



pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

font_score = pygame.font.SysFont('Bauhaus 93', 30)

#define game variables
tile_size = 50
main_menu = True
level = 1
jump_counter = 0
game_over = 0
score = 0
score_silver = 0
background = 'img/sky.png'
last_level = False
player_img = 'kirb'
white = (255, 255, 255)
requested = False

#load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load(background)
start_img = pygame.image.load('img/start_btn.png')
exit_img = pygame.image.load('img/exit_btn.png')
post_img = pygame.image.load('img/post_btn.png')
success_img = pygame.image.load('img/success_btn.png')
ed_img = pygame.image.load('img/ed_btn.png')
juan_img = pygame.image.load('img/juan_btn.png')
ana_img = pygame.image.load('img/ana_btn.png')
ethan_img = pygame.image.load('img/ethan_btn.png')
vicky_img = pygame.image.load('img/vicky_btn.png')
camilo_img = pygame.image.load('img/camilo_btn.png')
victor_img = pygame.image.load('img/victor_btn.png')
johan_img = pygame.image.load('img/johan_btn.png')
kirb_img = pygame.image.load('img/kirb_btn.png')

def set_level():
	global bg_img
	global background
	global last_level
	data = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]

	background = 'img/astrix.png'
	bg_img = pygame.image.load(background)
	last_level = True
	return data


def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

def draw_text_silver(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

#function to reset level
def reset_level(level):
	player.reset(100, screen_height - 130)
	exit_group.empty()
	silver_group.empty()
	coin_group.empty()
	if level == 3:
		coin_group.empty()
		silver_group.empty()
		world_data = world_data = set_level()
		world = World(world_data)
	else:
		pickle_in = open(f'level{level}_data', 'rb')
		world_data = pickle.load(pickle_in)
		world = World(world_data)

	if level == 3:
		score = 0
		score_silver = 0

	return world


class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
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
		screen.blit(self.image, self.rect)

		return action

class Player():
	def __init__(self, x, y, img):
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		self.player_img = img
		for num in range(1, 5):
			img_right = pygame.image.load(f'img/{self.player_img}{num}.png')
			img_right = pygame.transform.scale(img_right, (40, 80))
			img_left = pygame.transform.flip(img_right, True, False)
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		self.image = self.images_right[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0

	def update(self, game_over):
		global requested
		global jump_counter
		dx = 0
		dy = 0
		walk_cooldown = 5

		if game_over == 0:
			#get keypresses
			key = pygame.key.get_pressed()
			if jump_counter < 2:
			#if True:	
				if key[pygame.K_SPACE] and self.jumped == False:
					self.vel_y = -15
					self.jumped = True
					jump_counter += 1
				if key[pygame.K_SPACE] == False:
					self.jumped = False
			if key[pygame.K_LEFT]:
				dx -= 5
				self.counter += 1
				self.direction = -1
			if key[pygame.K_RIGHT]:
				dx += 5
				self.counter += 1
				self.direction = 1
			if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
				self.counter = 0
				self.index = 0
				if self.direction == 1:
					self.image = self.images_right[self.index]
				if self.direction == -1:
					self.image = self.images_left[self.index]


			#handle animation
			if self.counter > walk_cooldown:
				self.counter = 0	
				self.index += 1
				if self.index >= len(self.images_right):
					self.index = 0
				if self.direction == 1:
					self.image = self.images_right[self.index]
				if self.direction == -1:
					self.image = self.images_left[self.index]


			#add gravity
			self.vel_y += 1
			#if self.vel_y > 10:
			#	self.vel_y = 10
			dy += self.vel_y

			#check for collision
			for tile in world.tile_list:
				#check for collision in x direction
				if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
					dx = 0
				#check for collision in y direction
				if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
					#check if below the ground i.e. jumping
					if self.vel_y < 0:
						dy = tile[1].bottom - self.rect.top
						self.vel_y = 0
					#check if above the ground i.e. falling
					elif self.vel_y >= 0:
						dy = tile[1].top - self.rect.bottom
						self.vel_y = 0
						jump_counter = 0
					

			#check collision with exit
			if pygame.sprite.spritecollide(self, exit_group, False):
				game_over = 1

			#check collision with furnace
			if pygame.sprite.spritecollide(self, furnace_group, False):
				if post_button.draw() and requested == False:
					#Make post 
					IP = os.getenv('IP')
					#url = 'http://localhost:8080/'
					url = IP
					myobj = {'owner': player_img.capitalize(),
	       					 'gold': score, 
		                     'silver': score_silver
							}
					x = requests.post(url, json = myobj)
					if x.status_code == 200:
						post_button.image = success_img
						requested = True
			
			

			#update player coordinates
			self.rect.x += dx
			self.rect.y += dy

		if self.rect.bottom > screen_height:
			self.rect.bottom = screen_height
			dy = 0

		#draw player onto screen
		screen.blit(self.image, self.rect)

		return game_over
	
	
	def reset(self, x, y):
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		for num in range(1, 5):
			img_right = pygame.image.load(f'img/{self.player_img}{num}.png')
			img_right = pygame.transform.scale(img_right, (40, 80))
			img_left = pygame.transform.flip(img_right, True, False)
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		self.image = self.images_right[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0




class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		dirt_img = pygame.image.load('img/dirt.png')
		grass_img = pygame.image.load('img/grass.png')

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 7:
					coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
					coin_group.add(coin)
				if tile == 9:
					silver = Silver(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
					silver_group.add(silver)
				if tile == 8:
					exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
					exit_group.add(exit)
				if tile == 10:
					furnace = Furnace(col_count * tile_size, row_count * tile_size)
					furnace_group.add(furnace)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])


class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/coin.png')
		self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

class Silver(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/silver.png')
		self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

class Exit(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/exit.png')
		self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Furnace(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/furnace.png')
		self.image = pygame.transform.scale(img, (int(tile_size * 4), int(tile_size * 4)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

#player = Player(100, screen_height - 130, player_img)

exit_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
silver_group = pygame.sprite.Group()
furnace_group = pygame.sprite.Group()

#create buttons
#start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2 + 50, exit_img)
post_button = Button(screen_width // 2 - 150, screen_height // 2, post_img)
success_button = Button(screen_width // 2 - 150, screen_height // 2, success_img)
ed_button = Button(screen_width // 2 - 350, screen_height // 100 + 700, ed_img)
juan_button = Button(screen_width // 2 - 250, screen_height // 100 + 700, juan_img)
ana_button = Button(screen_width // 2 - 150, screen_height // 100 + 700, ana_img)
ethan_button = Button(screen_width // 2 - 50, screen_height // 100 + 700, ethan_img)
vicky_button = Button(screen_width // 2 - 350, screen_height // 100 + 600, vicky_img)
camilo_button = Button(screen_width // 2 - 350, screen_height // 2, camilo_img)
johan_button = Button(screen_width // 2 - 250, screen_height // 2, johan_img)
victor_button = Button(screen_width // 2 - 150, screen_height // 2, victor_img)
kirb_button = Button(screen_width // 2 - 50, screen_height // 2 , kirb_img)
#load in level data and create world
pickle_in = open(f'level{level}_data', 'rb')
world_data = pickle.load(pickle_in)
world = World(world_data)

run = True
while run:
	clock.tick(fps)

	if last_level == False:
		screen.blit(bg_img, (0, 0))
		screen.blit(sun_img, (100, 100))
	else: 
		screen.blit(bg_img, (0, 0))


	if main_menu == True:
		if exit_button.draw():
			run = False
		#if start_button.draw():
			#main_menu = False
		if ed_button.draw():
			main_menu = False
			player_img = 'ed'
		if juan_button.draw():
			main_menu = False
			player_img = 'juan'
		if ana_button.draw():
			main_menu = False
			player.player_img = 'ana'
		if ethan_button.draw():
			main_menu = False
			player.player_img = 'ethan'
		if vicky_button.draw():
			main_menu = False
			player.player_img = 'vicky'
		if victor_button.draw():
			main_menu = False
			player.player_img = 'victor'
		if camilo_button.draw():
			main_menu = False
			player.player_img = 'camilo'
		if johan_button.draw():
			main_menu = False
			player.player_img = 'johan'
		if kirb_button.draw():
			main_menu = False
			player_img = 'kirb'	
		player = Player(100, screen_height - 130, player_img)
	else:
		world.draw()

		if pygame.sprite.spritecollide(player, coin_group, True):
			score += 1
		if pygame.sprite.spritecollide(player, silver_group, True):
			score_silver += 1

		draw_text('Gold: ' + str(score), font_score, white, tile_size - 10, 10)
		draw_text('Silver: ' + str(score_silver), font_score, white, tile_size + 120, 10)

		exit_group.draw(screen)
		coin_group.draw(screen)
		silver_group.draw(screen)
		furnace_group.draw(screen)
		game_over = player.update(game_over)

		#if player has completed the level
		if game_over == 1:
			#reset game and go to the next level
			level += 1
			world_data = []
			world = reset_level(level)
			game_over = 0


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()