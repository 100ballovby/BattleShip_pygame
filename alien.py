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


    def blit(self):
        """Рисует врага на экране"""
        self.screen.blit(self.image, self.rect)

