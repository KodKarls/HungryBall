class GameStats:
    """A class designed to the monitoring of statistical data in the game."""

    def __init__(self, hb_game):
        """Necessary attributes initialization."""
        self.settings = hb_game.settings

        # Start the game inactive state.
        self.game_active = False

        # Points.
        self.score = 0

        # The number of black dots currently eaten.
        self.number_black_dots_eaten = 0

        # The current level of the game.
        self.level = 1
