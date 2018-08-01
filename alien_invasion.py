import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(ai_settings, screen)

    # set the color of background
    bg_color = ai_settings.bg_color

    # 创建一个用于存储子弹的编组,一个外星人编组
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    # alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the game's main loop
    while True:

        # monitor the keyboard events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

        #  redraw the screen at every iteration
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()