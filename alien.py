import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс врага"""

    def __init__(self, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pg.image.load('images/ufo.png')

        DEFAULT_IMAGE_SIZE = (64, 64)  # TODO: добавить относительное определение размера
        self.image = pg.transform.scale(self.image, DEFAULT_IMAGE_SIZE)

        self.rect = self.image.get_rect()  # создает колижн-модель

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)  # сохранение точной позиции пришельца

        # настройка direction отвечает за направление движения флота. 1 - право, -1 лево
        self.direction = 1
        self.speed = 5  # скорость перемещения влево-вправо
        self.drop_speed = 5  # скорость перемещения вниз


    def blit(self):
        """Рисует врага на экране"""
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        """Проверяем, коснулся ли корабль врага края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Перемещает пришельцев вправо"""
        self.x += (self.speed * self.direction)
        self.rect.x = self.x



