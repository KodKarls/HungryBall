class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry."""
        # Ustawienia ekranu.
        self.screen_width = 800
        self.screen_height = 600
        self.title = 'Głodna piłka'
        self.bg_color = (230, 230, 230)
