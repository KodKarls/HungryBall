import sys

import pygame

from settings import Settings

class HungryBall:
    """Ogólna klasa przeznaczona do zarządzania zasobami
    i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.title)

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Odświeżenie ekranu w trakcie każdej iteracji pętli.
            self.screen.fill(self.settings.bg_color)

            # Wyświetlenie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    hungry_ball = HungryBall()
    hungry_ball.run_game()
