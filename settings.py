# settings.py
import pygame_menu
import pygame

MUSIC_VOLUME = 0.3 
SFX_VOLUME = 0.3 
RANGE_SLIDER_RANGE = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)

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

    pygame.mixer.music.set_volume(SFX_VOLUME)

    print(f"SFX Volume set to: {SFX_VOLUME * 100}%")

def get_sfx_volume():
    return SFX_VOLUME

def settings_menu(screen, return_callback):
    menu = pygame_menu.Menu("Settings", 600, 400, theme=pygame_menu.themes.THEME_DARK)

    add_range_slider(menu, "Music", MUSIC_VOLUME, RANGE_SLIDER_RANGE, onchange=set_music_volume)

    add_range_slider(menu, "Sound", MUSIC_VOLUME, RANGE_SLIDER_RANGE, onchange=set_music_volume)



    menu.add.button("Return", return_callback)

    menu.mainloop(screen)
