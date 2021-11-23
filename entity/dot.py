import random

import pygame
from pygame.sprite import Sprite


class Dot(Sprite):
    """A class designed to manage dots that appear in the game."""

    def __init__(self, hb_game, player, color):
        """Necessary attributes initialization."""
        Sprite.__init__(self)
        self.screen = hb_game.screen
        self.settings = hb_game.settings
        self.player = player
        self.scoreboard = hb_game.scoreboard

        # Initialize color and surface for dot.
        self.color = color
        self.image = pygame.Surface(
            (self.settings.dot_radius * 2, self.settings.dot_radius * 2))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # The area that marks the boundary around an object where dots cannot appear.
        self.safe_area_size = 25

    def rand_black_dot_position(self, red_dots):
        """Draw by lot a new position for the black dot."""
        while True:
            pos_x = random.randint(0, self.settings.screen_width)
            pos_y = random.randint(0, self.settings.screen_height)

            if self._check_random_dot_player_position(pos_x, pos_y):
                continue
            elif self._check_random_red_dots_position(pos_x, pos_y, red_dots):
                continue
            elif self._check_random_scoreboard_position(pos_x, pos_y):
                continue
            else:
                break

        # Setting the appropriate center for the drawn dot.
        self.rect.center = (pos_x, pos_y)

    def rand_red_dot_position(self):
        """Draw by lot a new position for the red dot."""
        while True:
            pos_x = random.randint(0, self.settings.screen_width)
            pos_y = random.randint(0, self.settings.screen_height)

            if self._check_random_dot_player_position(pos_x, pos_y):
                continue
            elif self._check_random_scoreboard_position(pos_x, pos_y):
                continue
            else:
                break

        # Setting the appropriate center for the drawn dot.
        self.rect.center = (pos_x, pos_y)

    def _check_random_dot_player_position(self, rand_x, rand_y):
        """Checking if the randomly selected position is not too close to the player."""
        return (self.player.rect.left - self.safe_area_size < rand_x < self.player.rect.right + self.safe_area_size and
                self.player.rect.top - self.safe_area_size < rand_y < self.player.rect.bottom + self.safe_area_size)

    def _check_random_red_dots_position(self, rand_x, rand_y, red_dots):
        """Checking if the randomly selected position is not too close to red dots."""
        for red_dot in red_dots.sprites():
            if (red_dot.rect.left - self.safe_area_size < rand_x < red_dot.rect.right + self.safe_area_size and
                    red_dot.rect.top - self.safe_area_size < rand_y < red_dot.rect.bottom + self.safe_area_size):
                return True

        return False

    def _check_random_scoreboard_position(self, rand_x, rand_y):
        """Checking if the randomly selected position is not too close to the scoreboard."""
        return (self.scoreboard.score_rect.left - self.safe_area_size < rand_x < self.scoreboard.score_rect.right +
                self.safe_area_size and self.scoreboard.score_rect.top - self.safe_area_size < rand_y <
                self.scoreboard.score_rect.bottom + self.safe_area_size)

    def draw(self):
        """Display a dot on the screen."""
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.settings.dot_radius)
