class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry."""
        # Ustawienia ekranu.
        self.screen_width = 800
        self.screen_height = 600
        self.title = 'Głodna piłka'
        self.bg_color = (230, 230, 230)

        # Ustawienia gry.
        self.target_fps = 60

        # Ustawienia czcionki.
        self.font_name = 'Courier'
        self.font_point_size = 48
        self.font_button_size = 40

        # Ustawienia dotyczące kropek zjadanych przez gracza.
        self.dot_radius = 10
        self.black_dot_color = (0, 0, 0)
        self.red_dot_color = (255, 0, 0)

        # Punkty przyznawane za zjedzenie czarnej kropki.
        self.dot_point = 1

        # Ustawienie dotyczące wzrostu poziomu trudności gry.
        self.level_increase = 1

        # Ustawienie dotyczące zmiany ilości zjadanych czarnych kropek.
        self.black_dots_eaten_increase = 1

        # Ustawienie dotyczące ilości czerwonych kropek.
        self.red_dots_amount_scale = 2

        # Ustawienia dotyczące szybkości gracza.
        self.player_speed_scale = 1.05

        self._init_dynamic_settings()

    def _init_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry."""
        self.red_dots_amount = 2
        self.player_speed = 3.0

    def increase_red_dots_amount(self, level):
        """Zmiana ustawień dotyczących ilości czerwonych kropek."""
        if level % 10 == 0:
            self.red_dots_amount_scale += 2
            self.red_dots_amount += level * 0.5
            return
        self.red_dots_amount += self.red_dots_amount_scale

    def increase_player_speed(self, level):
        """Zmiana ustawień dotyczących szybkości gracza."""
        if level % 10 == 0:
            self.player_speed *= self.player_speed_scale
