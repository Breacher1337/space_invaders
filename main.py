import pygame
import pygame_menu
import random
import settings
from constants import WIDTH, HEIGHT, WIN, BG, AUDIO_ASSETS
from ships import Player, Enemy, collide, ships_data, character_select, ships_data
from audio import sound_onclick, sound_laser, sound_defeat, menu_music, game_music

import pygame_menu.font

pygame.font.init()
pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Space Shooter")

def main(player, player_stats):
    game_music()

    run = True
    FPS = 60
    level = 0
    lives = player_stats["lives"]
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 2
    enemy_vel = 0.5

    player_vel = player_stats["player_vel"]
    player_laser_vel = player_stats["laser_vel"]
    laser_vel = 4
    
    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG, (0,0))

        lives_label =  main_font.render(f"Lives: {lives}", 1, (255, 0, 0))
        level_label =  main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)
        
        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

            lost_label = lost_font.render("You lost!", 1, (255,0,0))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        if len(enemies) == 0:
            level += 1
            wave_length += random.randint(1, 3)

            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500,-100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x + player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel

        if keys[pygame.K_UP] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-player_laser_vel, enemies)

def start_game(selected_ship_name):
    if selected_ship_name:
        player_stats = ships_data[selected_ship_name]
        sound_onclick()
        print(f"Selected ship: {selected_ship_name}")
        print(player_stats)
        
        player = Player(600, 540, health=player_stats["health"], ship_img=player_stats["ship_img"], laser_img=player_stats["laser_img"], fire_rate=player_stats["fire_rate"],
                        ammo=player_stats["ammo"], reload_speed=player_stats["reload_speed"])

        main(player=player, player_stats=player_stats)
    else: 
        print("No ship selected!") 

def open_settings():

    sound_onclick()
    settings.settings_menu(WIN, main_menu)

def exit_game():
    pygame.quit()
    quit()

def open_character_select():
    sound_onclick()

    settings.save_settings()

    selected_ship_name = character_select(WIN)
    start_game(selected_ship_name)

def main_menu():
    menu = pygame_menu.Menu("Space Invaders: Pyth-ers", WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_DARK)
    menu.add.label("Welcome to Space Invaders: Pyth-ers!")

    pygame.mixer.music.stop()

    menu_music()

    menu.add.button("Start", open_character_select)
    menu.add.button("Settings", open_settings)
    menu.add.button("Exit", exit_game)

    menu.mainloop(WIN)
    pygame.quit()

main_menu()

        