import pygame as pg
from pygame.sprite import Group  # группа пуль, к которым можно применять методы
import game_functions as gf
from settings import Config
from ship import Ship
from alien import Alien
from game_stat import GameStat
from button import Button


def run():
    pg.init()  # инициализация PyGame
    pg.font.init()  # инициализация работы со шрифтами
    game_config = Config((1200, 800), (230, 230, 230))  # создаю экземпляр класса настроек
    screen = pg.display.set_mode((game_config.screen_width,
                                 game_config.screen_height))  # окно игры и размер
    ship = Ship(screen, game_config)
    bullets = Group()  # группируем объекты-пули
    aliens = Group()
    stat = GameStat(game_config)
    play_btn = Button(game_config, screen, "Start")
    # создадим вражеский флот
    gf.create_fleet(game_config, screen, aliens, ship)

    # цвет фона игры
    pg.display.set_caption('Battle Ship!')  # название игры в окошке
    while True:
        gf.check_events(ship, game_config, screen, bullets, stat, play_btn, aliens)  # трекаем события в игре

        if stat.game_active:  # если игра в активном состоянии
            ship.update()
            gf.update_bullets(bullets, aliens, game_config, screen, ship)
            gf.update_enemies(game_config, stat, screen, ship, aliens, bullets)
        gf.update_screen(game_config, screen, ship, bullets, aliens, play_btn, stat)  # обновление экрана игры



run()



