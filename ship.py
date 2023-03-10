import pygame as pg


class Ship:
    """Класс корабля"""

    def __init__(self, screen, config):
        self.screen = screen
        self.image = pg.image.load('images/spaceship.png')

        self.settings = config

        DEFAULT_IMAGE_SIZE = (128, 128)
        self.image = pg.transform.scale(self.image, DEFAULT_IMAGE_SIZE)

        self.rect = self.image.get_rect()  # создает колижн-модель
        self.screen_rect = screen.get_rect()
        #self.image.fill((255, 0, 0))

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def blit(self):
        """Рисует корабль на экране"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Обновляет позицию корабля с учетом флаговой переменной"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.settings.ship_speed_factor

    def center_ship(self):
        """Размещает корабль в центре экрана"""
        self.rect.centerx = self.screen_rect.centerx

