import pygame as pg


class Alien:
    """Класс врага"""

    def __init__(self, screen):
        self.screen = screen
        self.image = pg.image.load('images/ufo.png')

        DEFAULT_IMAGE_SIZE = (128, 128)
        self.image = pg.transform.scale(self.image, DEFAULT_IMAGE_SIZE)

        self.rect = self.image.get_rect()  # создает колижн-модель
        self.screen_rect = screen.get_rect()

        self.rect.x = 200 or self.screen_rect.width
        self.rect.y = 200 or self.screen_rect.height


    def blit(self):
        """Рисует врага на экране"""
        self.screen.blit(self.image, self.rect)

