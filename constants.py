import pygame
import os

WIDTH = 1280
HEIGHT = 720
ASSETS_LOCATION = ".\\assets"
AUDIO_ASSETS = ".\\audio"
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BG = pygame.image.load(os.path.join(ASSETS_LOCATION, "bg_black.png"))
RED_SPACE_SHIP = pygame.image.load(os.path.join(ASSETS_LOCATION, "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join(ASSETS_LOCATION, "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join(ASSETS_LOCATION, "pixel_ship_blue_small.png"))
RED_LASER = pygame.image.load(os.path.join(ASSETS_LOCATION, "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join(ASSETS_LOCATION, "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join(ASSETS_LOCATION, "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join(ASSETS_LOCATION, "pixel_laser_yellow.png"))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join(ASSETS_LOCATION, "pixel_ship_yellow.png"))
