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
        self.scoreboard = hb_game.score_board

        # Nadanie kropce koloru i zdefiniowanie powierzchni.
        self.color = color
        self.image = pygame.Surface(
            (self.settings.dot_radius * 2, self.settings.dot_radius * 2))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Obszar, który wyznacza granicę wokół obiektu, w której nie mogą pojawiać się kropki.
        self.safe_area_size = 25

    def rand_black_dot_position(self, red_dots):
        """Losowanie nowej pozycji dla czarnej kropki."""
        while True:
            pos_x = random.randint(0, self.settings.screen_width)
            pos_y = random.randint(0, self.settings.screen_height)

            if self._check_random_dot_player_position(pos_x, pos_y):
                continue
            elif self._check_random_red_dots_positon(pos_x, pos_y, red_dots):
                continue
            elif self._check_random_scoreboard_position(pos_x, pos_y):
                continue
            else:
                break

        # Ustawienie odpowiedniego środka dla rysowanej kropki.
        self.rect.center = (pos_x, pos_y)

    def rand_red_dot_position(self):
        """Losowanie nowej pozycji dla czerwonej kropki."""
        while True:
            pos_x = random.randint(0, self.settings.screen_width)
            pos_y = random.randint(0, self.settings.screen_height)

            if self._check_random_dot_player_position(pos_x, pos_y):
                continue
            elif self._check_random_scoreboard_position(pos_x, pos_y):
                continue
            else:
                break

        # Ustawienie odpowiedniego środka dla rysowanej kropki.
        self.rect.center = (pos_x, pos_y)

    def _check_random_dot_player_position(self, rand_x, rand_y):
        """Sprawdzenie czy losowana pozycja nie jest zbyt blisko gracza."""
        return (rand_x > self.player.rect.left - self.safe_area_size and
                rand_x < self.player.rect.right + self.safe_area_size and
                rand_y > self.player.rect.top - self.safe_area_size and
                rand_y < self.player.rect.bottom + self.safe_area_size)

    def _check_random_red_dots_positon(self, rand_x, rand_y, red_dots):
        """Sprawdzenie czy losowana pozycja nie jest zbyt blisko czerwonych kropek."""
        for red_dot in red_dots.sprites():
            if (rand_x > red_dot.rect.left - self.safe_area_size and
                rand_x < red_dot.rect.right + self.safe_area_size and
                rand_y > red_dot.rect.top - self.safe_area_size and
                rand_y < red_dot.rect.bottom + self.safe_area_size):
                return True

        return False

    def _check_random_scoreboard_position(self, rand_x, rand_y):
        """Sprawdzenie czy losowana pozycja nie jest zbyt blisko tablicy z wyświetlanym wynikiem."""
        return (rand_x > self.scoreboard.score_rect.left - self.safe_area_size and
                rand_x < self.scoreboard.score_rect.right + self.safe_area_size and
                rand_y > self.scoreboard.score_rect.top - self.safe_area_size and
                rand_y < self.scoreboard.score_rect.bottom + self.safe_area_size)

    def draw(self):
        """Wyświetlenie kropki na ekranie."""
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.settings.dot_radius)
        