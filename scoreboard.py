import pygame.font as pgf

class Scoreboard:
    def __init__(self, config, screen, stat):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = config
        self.stat = stat

        self.text_color = (50, 50, 50)
        self.font = pgf.SysFont('Arial', int(config.screen_width * 0.03))

        self.transform_score()  # сразу при инициализации вызываем метод подготовки вывода очков
        self.transform_high_score()  # вызываем метод подготовки рекорда

    def transform_score(self):
        rounded_score = int(round(self.stat.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - int(self.settings.screen_width * 0.03)
        self.score_rect.top = int(self.settings.screen_width * 0.01)


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)


    def transform_high_score(self):
        high_score = int(round(self.stat.high_score, -1))
        high_score_str = "{:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                 self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top



