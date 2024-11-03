import random
import pygame

from constants import AUDIO_ASSETS


from settings import get_sfx_volume, get_music_volume, sound_files 

# sound_files = {
#     "button_click1": pygame.mixer.Sound(os.path.join(AUDIO_ASSETS, "button_click1.wav")),
#     "button_click2": pygame.mixer.Sound(os.path.join(AUDIO_ASSETS, "button_click2.wav")),
#     "button_click3": pygame.mixer.Sound(os.path.join(AUDIO_ASSETS, "button_click3.wav")),
#     "defeat": pygame.mixer.Sound(os.path.join(AUDIO_ASSETS, "defeat.wav")),
#     "audio_on_click": pygame.mixer.Sound(os.path.join(AUDIO_ASSETS, "audio_on_click.wav")),
# }

def sound_onclick():
	num = random.randint(1, 3)
	sound_files["button_click" + str(num)].play()

def sound_laser():
	sound_files["audio_on_click"].play()
     
def sound_defeat():
	sound_files["defeat"].play()
     
def menu_music():
	pygame.mixer.music.load(AUDIO_ASSETS + "\\menu_music.mp3")

	pygame.mixer.music.set_volume(get_music_volume())
	pygame.mixer.music.play(-1)
      
def game_music():
	pygame.mixer.music.load(AUDIO_ASSETS + "\\game_music.mp3")

	pygame.mixer.music.set_volume(get_music_volume())
	pygame.mixer.music.play(-1)