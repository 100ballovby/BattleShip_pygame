class GameStat:
    def __init__(self, game_settings):
        self.settings = game_settings
        self.reset_stat()
        self.game_active = False # игра запускается в не активном состоянии
        self.score = 0

        with open("high_score.txt", "r") as file:
            hs = int(file.read())
        self.high_score = hs  # рекорд всегда берем из файла

    def reset_stat(self):
        self.ships_left = self.settings.ship_limit


