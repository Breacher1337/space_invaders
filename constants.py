import pygame
import os

# Main
WIDTH = 1280
HEIGHT = 720
ASSETS_LOCATION = ".\\assets"
SHIPS_LOCATION = ".\\assets\\ships"
LASERS_LOCATION = ".\\assets\\lasers"
AUDIO_ASSETS = ".\\audio"
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.image.load(os.path.join(ASSETS_LOCATION, "background-black.png"))

def load_laser_image(filename):
	return pygame.image.load(os.path.join(LASERS_LOCATION, filename))

def load_ship_image(filename):
	return pygame.image.load(os.path.join(SHIPS_LOCATION, filename))

def load_audio(filename):
	return os.path.join(AUDIO_ASSETS, filename)

# Ships
YELLOW_SPACE_SHIP = load_ship_image("pixel_ship_dark_red.png")
RED_SPACE_SHIP = load_ship_image("pixel_ship_red_small.png")
GREEN_SPACE_SHIP = load_ship_image("pixel_ship_green_small.png")
BLUE_SPACE_SHIP = load_ship_image("pixel_ship_blue_small.png")

# Lasers
YELLOW_LASER = load_laser_image("pixel_laser_yellow.png")
GREEN_LASER = load_laser_image("pixel_laser_green_enemy.png")
RED_LASER = load_laser_image("pixel_laser_red_enemy.png")
BLUE_LASER = load_laser_image("pixel_laser_blue_enemy.png")

RANGE_SLIDER_RANGE = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)