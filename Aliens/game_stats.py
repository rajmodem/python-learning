class GameStats:
    """Track statistics for alien invasion"""

    def __init__(self,ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        #start Alien Invasion in an active state
        self.game_active = True

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.settings.ship_limit

        