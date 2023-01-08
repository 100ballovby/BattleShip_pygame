import sys
import pygame as pg
from bullet import Bullet


def check_keydown_events(event, obj, config, screen, group):
    if event.key == pg.K_RIGHT:
        obj.moving_right = True  # разрешаем кораблю двигаться вправо
    elif event.key == pg.K_LEFT:
        obj.moving_left = True
    elif event.key == pg.K_SPACE:
        new_bullet = Bullet(config, screen, obj)
        group.add(new_bullet)


def check_keyup_events(event, obj):
    if event.key == pg.K_RIGHT:
        obj.moving_right = False  # запрещаем движение
    elif event.key == pg.K_LEFT:
        obj.moving_left = False


def check_events(obj, config, screen, group):
    for event in pg.event.get():  # обрабатываю события
        if event.type == pg.QUIT:  # если нажали на крестик
            sys.exit()  # закрыть окно
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, obj, config, screen, group)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, obj)


def update_screen(settings, screen, obj, group):
    screen.fill(settings.bg_color)
    for bullet in group.sprites():
        bullet.draw_bullet()
    obj.blit()
    pg.display.flip()  # отображение последнего прорисованного кадра
