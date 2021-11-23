class Settings:
    """A class designed to store all game settings."""

    def __init__(self):
        """Necessary attributes initialization.."""
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.title = 'Hungry Ball'
        self.bg_color = (230, 230, 230)

        # Game settings.
        self.target_fps = 60

        # Font settings.
        self.font_name = 'Courier'
        self.font_point_size = 48
        self.font_button_size = 40

        # Entities settings.
        self.dot_radius = 10
        self.black_dot_color = (0, 0, 0)
        self.red_dot_color = (255, 0, 0)

        # Points awarded for eating a black dot .
        self.dot_point = 1

        # Scale variables settings.
        self.level_increase = 1
        self.black_dots_eaten_increase = 1
        self.red_dots_amount_scale = 2
        self.player_speed_scale = 1.05

        self._init_dynamic_settings()

    def _init_dynamic_settings(self):
        """Initializing settings that change during the game."""
        self.red_dots_amount = 2
        self.player_speed = 3.0

    def increase_red_dots_amount(self, level):
        """Changing the settings for the number of red dots."""
        if level % 10 == 0:
            self.red_dots_amount_scale += 2
            self.red_dots_amount += level * 0.5
            return
        self.red_dots_amount += self.red_dots_amount_scale

    def increase_player_speed(self, level):
        """Changing player speed settings."""
        if level % 10 == 0:
            self.player_speed *= self.player_speed_scale
