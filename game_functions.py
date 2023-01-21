import sys
from time import sleep
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
    enemy.draw(screen)
    pg.display.flip()  # отображение последнего прорисованного кадра


def update_bullets(bullets_list, enemies, config, screen, obj):
    bullets_list.update()

    collisions = pg.sprite.groupcollide(bullets_list, enemies, True, True)
    # при обнаружении столкновения пули с пришельцем, удалить пулю
    if len(enemies) == 0:
        # уничтожим существующие пули и добавим новых врагов
        bullets_list.empty()
        create_fleet(config, screen, enemies, obj)

    # удаляем пули, которые улетели за игровую зону
    for bullet in bullets_list:
        if bullet.rect.bottom <= 0:  # координата нижней части пули меньше нуля
            bullets_list.remove(bullet)


def fire(config, screen, obj, bullets_list):
    if len(bullets_list) < config.bullets_limit:  # если количество выстрелов меньше позволенного лимита
        new_bullet = Bullet(config, screen, obj)  # создать пулю
        bullets_list.add(new_bullet)  # добавить ее в группу


def get_num_of_enemies(config, enemy_width):
    avail_space_x = config.screen_width - (2 * enemy_width)  # считаем количество пришельцев в ряду
    num_of_aliens = avail_space_x // (2 * enemy_width)
    return num_of_aliens


def get_num_of_rows(config, obj_height, enemy_height):
    avail_space_y = config.screen_height - (3 * enemy_height) - obj_height
    num_of_rows = avail_space_y // (2 * enemy_height)
    return num_of_rows


def create_enemy(screen, enemies, enemy_number, row_number):
    """Создаем врага и размещаем его на экране"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * enemy_number
    alien.rect.x = alien.x  # совмещаем хитбокс пришельца с картинкой пришельца
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    enemies.add(alien)


def create_fleet(config, screen, enemies, obj):
    alien = Alien(screen)
    num_of_aliens = get_num_of_enemies(config, alien.rect.width)
    num_of_rows = get_num_of_rows(config, obj.rect.height, alien.rect.height)

    for row_n in range(num_of_rows):
        for alien_n in range(num_of_aliens):
            create_enemy(screen, enemies, alien_n, row_n)


def check_fleet_edges(enemies):
    """Реагирует на столкновение врага с краем экрана"""
    for enemy in enemies.sprites():
        if enemy.check_edges():
            change_fleet_direction(enemies)
            break

def change_fleet_direction(enemies):
    """Опускает весь флот на одну линейку вниз """
    for enemy in enemies.sprites():
        enemy.rect.y += enemy.drop_speed
        enemy.direction *= -1

def update_enemies(config, stat, screen, obj, enemies, bullets_list):
    """Обновляет позицию всех врагов на экране"""
    check_fleet_edges(enemies)
    enemies.update()

    # проверка коллизий "враг-игрок"
    if pg.sprite.spritecollideany(obj, enemies):
        ship_hit(config, stat, screen, obj, enemies, bullets_list)


def ship_hit(config, stat, screen, obj, enemies, bullets_list):
    # уменьшаем количество доступных кораблей
    stat.ships_left -= 1

    enemies.empty()
    bullets_list.empty()

    create_fleet(config, screen, enemies, obj)
    obj.center_ship()

    sleep(0.5)
