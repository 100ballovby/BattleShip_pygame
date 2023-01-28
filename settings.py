class Config:
    """Класс для хранения настроек игры"""

    def __init__(self, resolution: tuple, bg_color: tuple):
        self.screen_width = resolution[0]
        self.screen_height = resolution[1]
        self.bg_color = bg_color

        self.ship_limit = 3 # всего игроку доступно 3 корабля
        self.ship_speed_factor = 5

        self.enemy_speed_factor = 5

        # параметры пули
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_limit = 3

        self.speed_scale = 1.1
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Настройки, которые будут изменяться в процессе игры"""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 3
        self.enemy_speed_factor = 5

        self.fleet_direction = 1


    def increase_speed(self):
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.enemy_speed_factor *= self.speed_scale

