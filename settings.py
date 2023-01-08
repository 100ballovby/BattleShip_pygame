class Config:
    """Класс для хранения настроек игры"""

    def __init__(self, resolution: tuple, bg_color: tuple):
        self.screen_width = resolution[0]
        self.screen_height = resolution[1]
        self.bg_color = bg_color

        # параметры пули
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

