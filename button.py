import pygame.font as pgf
import pygame as pg

class Button:
    def __init__(self, config, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # размеры и цвет кнопки
        self.width, self.height = config.screen_width * 0.1, config.screen_height * 0.1
        self.button_color = (66, 194, 245)
        self.text_color = (255, 255, 255)
        self.font = pgf.SysFont('Arial', int(self.width * 0.2))

        # построим объект прямоугольник вокруг кнопки
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # вызовем метод, который будет отображать текст на кнопку
        self.write_text(msg)

    def write_text(self, msg):
        """Метод помещает текст на кнопку и выравнивает по центру"""
        self.msg_view = self.font.render(msg, False, self.text_color, self.button_color)
        self.msg_rect = self.msg_view.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)  # выводим на экран прямоугольник
        self.screen.blit(self.msg_view, self.msg_rect)  # помещаем на прямоугольник текст
