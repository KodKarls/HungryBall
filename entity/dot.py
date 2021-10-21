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

        # Nadanie kropce koloru i zdefiniowanie powierzchni.
        self.color = color
        self.image = pygame.Surface(
            (self.settings.dot_radius * 2, self.settings.dot_radius * 2))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Obszar, który wyznacza granicę wokół gracza, w której nie mogą pojawiać się kropki.
        self.player_area_size = 25

        # Losowanie pozycji początkowej kropki.
        self.rand_new_position()

    def rand_new_position(self):
        """Losowanie nowej pozycji dla kropki."""
        while True:
            pos_x = random.randint(0, self.settings.screen_width)
            pos_y = random.randint(0, self.settings.screen_height)

            if self._check_random_dot_player_position(pos_x, pos_y):
                continue
            else:
                break

        # Ustawienie odpowiedniego środka dla rysowanej kropki.
        self.rect.center = (pos_x, pos_y)

    def _check_random_dot_player_position(self, rand_x, rand_y):
        """Sprawdzenie czy losowana pozycja nie jest zbyt blisko gracza."""
        return (rand_x > self.player.rect.left - self.player_area_size and
                rand_x < self.player.rect.right + self.player_area_size and
                rand_y > self.player.rect.top - self.player_area_size and
                rand_y < self.player.rect.bottom + self.player_area_size)

    def draw(self):
        """Wyświetlenie kropki na ekranie."""
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.settings.dot_radius)
        