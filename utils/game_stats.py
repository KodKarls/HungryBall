class GameStats:
    """Monitorowanie danych statystycznych w grze "Głodna piłka"."""

    def __init__(self, hb_game):
        """Inicjalizacja danych statystycznych."""
        self.settings = hb_game.settings

        # Uruchomienie gry "Głodna piłka" w stanie aktywnym.
        self.game_active = False

        # Punktacja.
        self.score = 0

        # Liczba aktualnie zjedzonych czarnych kropek.
        self.number_black_dots_eaten = 0

        # Aktualny poziom gry.
        self.level = 1
