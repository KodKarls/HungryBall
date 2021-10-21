import random

import pygame
from pygame.sprite import Sprite

class Dot(Sprite):
    """Klasa przeznaczona do zarządzania kropkami pojawiającymi
    się w grze."""

    def __init__(self, hb_game, player, color):
        """Inicjalizacja składników kropki."""
        super().__init__()

        self.screen = hb_game.screen
        self.settings = hb_game.settings
        self.player = player

        self.color = color
        self.image = pygame.Surface(
            (self.settings.dot_radius * 2, self.settings.dot_radius * 2))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Losowanie pozycji początkowej kulki.
        self._rand_new_position()

    def _rand_new_position(self):
        """Losowanie nowej pozycji dla kropki."""
        while True:
            pos_x = random.randint(0, self.settings.screen_width)
            pos_y = random.randint(0, self.settings.screen_height)

            if (pos_x > self.player.rect.left - 25 and pos_x < self.player.rect.right + 10 and
                pos_y > self.player.rect.top - 10 and pos_y < self.player.rect.bottom + 10):
                continue
            else:
                break

        self.rect.center =(pos_x, pos_y)

    def draw(self):
        """Wyświetlenie kropki na ekranie."""
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.settings.dot_radius)
        