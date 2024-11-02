import random
import pygame

from constants import AUDIO_ASSETS


from settings import get_sfx_volume, get_music_volume, sound_files
def sound_onclick():
	random.choice([sound_files["button_click1"], sound_files["button_click2"], sound_files["button_click3"]]).play()
    
def sound_laser():
    pygame.mixer.Sound.play(pygame.mixer.Sound(AUDIO_ASSETS + "\\laser" + random.choice(["1", "2", "3"]) + ".wav"))
     
def sound_defeat():
	pygame.mixer.Sound.play(pygame.mixer.Sound(AUDIO_ASSETS + "\\defeat" + random.choice(["1", "2", "3"]) + ".wav"))
     
def menu_music():
	pygame.mixer.music.load(AUDIO_ASSETS + "\\menu_music.mp3")

	pygame.mixer.music.set_volume(get_music_volume())
	pygame.mixer.music.play(-1)
      
def game_music():
	pygame.mixer.music.load(AUDIO_ASSETS + "\\game_music.mp3")

	pygame.mixer.music.set_volume(get_music_volume())
	pygame.mixer.music.play(-1)