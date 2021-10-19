import sys

import pygame

class HungryBall:
    """Ogólna klasa przeznaczona do zarządzania zasobami
    i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Głodna piłka")

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Wyświetlenie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    hungry_ball = HungryBall()
    hungry_ball.run_game()
