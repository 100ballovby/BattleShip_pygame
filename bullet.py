import pygame as pg
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс управления снарядами, которыми стреляет корабль"""
    def __init__(self, config, screen, obj):
        super(Bullet, self).__init__()  # наследую все методы класса-родителя
        self.screen = screen
        self.rect = pg.Rect(0, 0, config.bullet_width,
                            config.bullet_height)
        self.rect.centerx = obj.rect.centerx
        self.rect.top = obj.rect.top

        self.y = float(self.rect.y)

        self.color = config.bullet_color

    def update(self):
        """Перемещаем пулю по экрану"""
        self.y -= 10
        self.rect.y = self.y

    def draw_bullet(self):
        """Выводим пулю на экран"""
        pg.draw.rect(self.screen, self.color, self.rect)

