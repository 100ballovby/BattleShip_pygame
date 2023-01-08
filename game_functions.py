import sys
import pygame as pg
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, obj, config, screen, bullets_list):
    if event.key == pg.K_RIGHT:
        obj.moving_right = True  # разрешаем кораблю двигаться вправо
    elif event.key == pg.K_LEFT:
        obj.moving_left = True
    elif event.key == pg.K_SPACE:
        fire(config, screen, obj, bullets_list)
    elif event.key == pg.K_ESCAPE:  # если нажата кнопка ESCAPE
        sys.exit()  # закрыть окно игры



def check_keyup_events(event, obj):
    if event.key == pg.K_RIGHT:
        obj.moving_right = False  # запрещаем движение
    elif event.key == pg.K_LEFT:
        obj.moving_left = False


def check_events(obj, config, screen, bullets_list):
    for event in pg.event.get():  # обрабатываю события
        if event.type == pg.QUIT:  # если нажали на крестик
            sys.exit()  # закрыть окно
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, obj, config, screen, bullets_list)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, obj)


def update_screen(settings, screen, obj, group, enemy):
    screen.fill(settings.bg_color)
    for bullet in group.sprites():
        bullet.draw_bullet()
    obj.blit()
    enemy.blit()
    pg.display.flip()  # отображение последнего прорисованного кадра


def update_bullets(bullets_list):
    bullets_list.update()

    # удаляем пули, которые улетели за игровую зону
    for bullet in bullets_list:
        if bullet.rect.bottom <= 0:  # координата нижней части пули меньше нуля
            bullets_list.remove(bullet)


def fire(config, screen, obj, bullets_list):
    if len(bullets_list) < config.bullets_limit:  # если количество выстрелов меньше позволенного лимита
        new_bullet = Bullet(config, screen, obj)  # создать пулю
        bullets_list.add(new_bullet)  # добавить ее в группу


def create_fleet(config, screen, enemies):
    alien = Alien(screen)
    alien_width = alien.rect.width
    avail_space_x = config.screen_width - (2 * alien_width)
    num_of_aliens = avail_space_x / (2 * alien_width)
    enemies.add(alien)
