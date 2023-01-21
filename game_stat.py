class GameStat:
    def __init__(self, game_settings):
        self.settings = game_settings
        self.reset_stat()

    def reset_stat(self):
        self.ships_left = self.settings.ship_limit


