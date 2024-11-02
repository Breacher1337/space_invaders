import pygame
import pygame_menu
from constants import WIDTH, HEIGHT, WIN, BG, RED_SPACE_SHIP, RED_LASER, BLUE_SPACE_SHIP, BLUE_LASER, GREEN_SPACE_SHIP, GREEN_LASER
import os
from constants import SHIPS_LOCATION, LASERS_LOCATION

ships_data = {
	"Elaijah": {
		"health": 150,
		"ship_img": "pixel_ship_navy_blue.png",
		"laser_img": "pixel_laser_blue.png",
		"lives": 5,
		"player_vel": 10,
		"laser_vel": 4,
		"fire_rate": 15,
	},
	"Amber": { #support
		"health": 50,
		"ship_img": "pixel_ship_light_pink.png",
		"laser_img": "pixel_laser_pink.png",
		"lives": 15,
		"player_vel": 3,
		"laser_vel": 4,
		"fire_rate": 60,
	},
	"Christian" : { #tank
		"health": 200,
		"ship_img": "pixel_ship_dark_red.png",
		"laser_img": "pixel_laser_red.png",
		"lives": 5,
		"player_vel": 5,
		"laser_vel": 4,
		"fire_rate": 30,

	},
	"Carl": { #dps
		"health": 100,
		"ship_img": "pixel_ship_purple.png",
		"laser_img": "pixel_laser_purple.png",
		"lives": 5,
		"player_vel": 4,
		"laser_vel": 2,
		"fire_rate": 5,
	},
	"Antonio": { #glasscannon
		"health": 30,
		"ship_img": "pixel_ship_orange.png",
		"laser_img": "pixel_laser_orange.png",
		"lives": 5,
		"player_vel": 15,
		"laser_vel": 8,
		"fire_rate": 15,
	}
}

class Laser:
	def __init__(self, x, y, img):
		self.x = x
		self.y = y
		self.img = img
		self.mask = pygame.mask.from_surface(self.img)

	def draw(self, window):
		window.blit(self.img, (self.x, self.y))

	def move(self, vel):
		self.y += vel

	def off_screen(self, height):
		return not(self.y <= height and self.y >= 0)

	def collision(self, obj):
		return collide(self, obj)

class Ship:
	def __init__(self, x, y, health=100, fire_rate=60) -> None:
		self.x = x
		self.y = y
		self.health = health 
		self.ship_img = None
		self.laser_img = None
		self.lasers = []
		self.cool_down_counter = 0
		self.fire_rate = fire_rate # the higher the number, the slower the fire rate
		self.ammo = 10
		self.max_ammo = self.ammo

	def draw(self, window):
		window.blit(self.ship_img, (self.x, self.y))
		for laser in self.lasers:
			laser.draw(window)

	def move_lasers(self, vel, obj):
		self.cooldown()
		for laser in self.lasers:
			laser.move(vel)
			if laser.off_screen(HEIGHT):
				self.lasers.remove(laser)
			elif laser.collision(obj):
				obj.health -= 10
				self.lasers.remove(laser)

	def cooldown(self):
		if self.cool_down_counter >= self.fire_rate:
			self.cool_down_counter = 0
		elif self.cool_down_counter > 0:
			self.cool_down_counter += 1

	def shoot(self):  
		if self.cool_down_counter == 0 and self.ammo > 0:
			laser = Laser(self.x, self.y, self.laser_img)
			self.lasers.append(laser)
			self.cool_down_counter = 1
			self.ammo -= 1

	def get_width(self):
		return self.ship_img.get_width()

	def get_height(self):
		return self.ship_img.get_height()

class Player(Ship):
	def __init__(self, x, y, health, ship_img, laser_img, fire_rate=60, **kwargs):
		super().__init__(x, y, health, fire_rate=fire_rate)
		self.ship_img = pygame.image.load(os.path.join(SHIPS_LOCATION, ship_img))
		self.laser_img = pygame.image.load(os.path.join(LASERS_LOCATION, laser_img))
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health

	def move_lasers(self, vel, objs):
		self.cooldown()
		for laser in self.lasers:
			laser.move(vel)
			if laser.off_screen(HEIGHT):
				self.lasers.remove(laser)
			else: 
				for obj in objs:
					if laser.collision(obj):
						objs.remove(obj)
						if laser in self.lasers:                        
							self.lasers.remove(laser)

	def draw(self, window):
		super().draw(window)
		self.healthbar(window)
		self.ammobar(window)

	def healthbar(self, window):
		pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
		pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

	def ammobar(self, window):
		pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 20, self.ship_img.get_width(), 10))
		pygame.draw.rect(window, (0,0,255), (self.x, self.y + self.ship_img.get_height() + 20, self.ship_img.get_width() * (self.ammo/self.max_ammo), 10))

class Enemy(Ship):
	COLOR_MAP = {
		"red": (RED_SPACE_SHIP, RED_LASER),
		"green": (GREEN_SPACE_SHIP, GREEN_LASER),
		"blue": (BLUE_SPACE_SHIP, BLUE_LASER)
				}
	def __init__(self, x, y, color, health=100):
		super().__init__(x, y, health)
		self.ship_img, self.laser_img = self.COLOR_MAP[color]
		self.mask = pygame.mask.from_surface(self.ship_img)

	def move(self, vel):
		self.y += vel

	def shoot(self):
		if self.cool_down_counter == 0:
			laser = Laser(self.x-20, self.y, self.laser_img)

			self.lasers.append(laser)
			self.cool_down_counter = 1

def collide(obj1, obj2):
	offset_x = obj2.x - obj1.x
	offset_y = obj2.y - obj1.y

	return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def select_ship(ship_name, selected_ship_ref):
	print(f"Selected ship: {ship_name}")
	selected_ship_ref[0] = ship_name
	return ship_name

def character_select(screen):
	menu = pygame_menu.Menu("Select Your Ship", WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_DARK)

	selected_ship_name = [None]

	for ship_name in ships_data.keys():
		menu.add.button(ship_name, lambda s=ship_name: select_ship(s, selected_ship_name))
		
	menu.add.button("Confirm", lambda: menu.disable())		
	menu.mainloop(screen)

	return selected_ship_name[0]