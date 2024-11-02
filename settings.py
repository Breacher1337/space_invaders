# settings.py
import pygame_menu
import pygame
import json
import os

from constants import RANGE_SLIDER_RANGE, WIDTH, HEIGHT, AUDIO_ASSETS

pygame.mixer.init()

with open("settings.json", "r") as f:
    settings = json.load(f)

MUSIC_VOLUME = settings["music_volume"]
SFX_VOLUME = settings["sfx_volume"]

sound_files = {
    "button_click1": pygame.mixer.Sound(os.path.join(AUDIO_ASSETS, "button_click1.wav")),
    "button_click2": pygame.mixer.Sound(os.path.join(AUDIO_ASSETS, "button_click2.wav")),
    "button_click3": pygame.mixer.Sound(os.path.join(AUDIO_ASSETS, "button_click3.wav")),
    "defeat": pygame.mixer.Sound(os.path.join(AUDIO_ASSETS, "defeat.wav")),
    "audio_on_click": pygame.mixer.Sound(os.path.join(AUDIO_ASSETS, "audio_on_click.wav")),
}

for sound in sound_files.values():
    sound.set_volume(SFX_VOLUME)

def add_range_slider(menu, label, initial_value, values, increment=1, onchange=None, **kwargs):

    if "range_text_value_enabled" not in kwargs:
        kwargs['range_text_value_enabled'] = False
 
    if "slider_text_value_enabled" not in kwargs:
        kwargs["slider_text_value_enabled"] = False

    return menu.add.range_slider(label, initial_value, values, increment=increment, onchange=onchange, **kwargs)

def set_music_volume(volume):
    global MUSIC_VOLUME
    MUSIC_VOLUME = volume
    pygame.mixer.music.set_volume(MUSIC_VOLUME)
    print(f"Music Volume set to: {MUSIC_VOLUME * 100}%")

def get_music_volume():
    return MUSIC_VOLUME

def set_sfx_volume(volume):
    global SFX_VOLUME
    SFX_VOLUME = volume
    
    for sound in sound_files.values():
        sound.set_volume(SFX_VOLUME)
    print(f"SFX Volume set to: {SFX_VOLUME * 100}%")

def get_sfx_volume():
    return SFX_VOLUME

def settings_menu(screen, return_callback):
    menu = pygame_menu.Menu("Settings", WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_DARK)
    add_range_slider(menu, "Music", MUSIC_VOLUME, RANGE_SLIDER_RANGE, onchange=set_music_volume)
    add_range_slider(menu, "Sound", MUSIC_VOLUME, RANGE_SLIDER_RANGE, onchange=set_sfx_volume)
    
    menu.add.button("Return", lambda: (save_settings(), return_callback()))

    menu.mainloop(screen)

def save_settings():
    with open("settings.json", "w") as f:
        json.dump({"music_volume": MUSIC_VOLUME, "sfx_volume": SFX_VOLUME}, f)    