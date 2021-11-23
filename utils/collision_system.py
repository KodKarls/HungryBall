import math

import pygame


class CollisionSystem:
    """A class designed to manage the collision system."""

    def __init__(self, hb_game):
        """Necessary attributes initialization."""
        self.player = hb_game.player
        self.settings = hb_game.settings

        # Calculation of the diagonal of a square in a quarter of a circle.
        self.diagonal_square = round(self.settings.dot_radius / math.sqrt(2), 0)

        # A dictionary that stores all circle collision points.
        self.player_collide_points = {}

    def check_player_black_dot_collision(self, black_dot):
        """A player collision check with a black dot."""
        # Checking if the player touches the black dot.
        if self._check_player_black_dot_touch(black_dot):
            # Adding all the player's current collision points to the dictionary.
            self._update_player_collide_points()

            for _, values in self.player_collide_points.items():
                # Check the distance between the collision points and the center of the black dot.
                distance = math.sqrt(
                    (values[0] - black_dot.rect.centerx)**2 +
                    (values[1] - black_dot.rect.centery)**2)
                if distance <= self.settings.dot_radius:
                    return True

        return False

    def check_player_red_dots_collision(self, red_dots):
        """A player collision check with a red dot."""
        # Checking if the player touches any red dot.
        red_dot = pygame.sprite.spritecollideany(self.player, red_dots)

        if red_dot is None:
            return False

        # Adding all the player's current collision points to the dictionary.
        self._update_player_collide_points()

        for _, values in self.player_collide_points.items():
            # Check the distance between the collision points and the center of the red dot.
            distance = math.sqrt(
                (values[0] - red_dot.rect.centerx)**2 + (values[1] - red_dot.rect.centery)**2)
            if distance <= self.settings.dot_radius:
                return True

        return False

    def _update_player_collide_points(self):
        """Updating player's collision points."""
        self.player_collide_points[0] = [
            self.player.rect.centerx + self.settings.dot_radius, self.player.rect.centery]
        self.player_collide_points[1] = [
            self.player.rect.centerx, self.player.rect.centery + self.settings.dot_radius]
        self.player_collide_points[2] = [
            self.player.rect.centerx - self.settings.dot_radius, self.player.rect.centery]
        self.player_collide_points[3] = [
            self.player.rect.centerx, self.player.rect.centery - self.settings.dot_radius]

        self.player_collide_points[4] = [
            self.player.rect.centerx + self.diagonal_square,
            self.player.rect.centery + self.diagonal_square]
        self.player_collide_points[5] = [
            self.player.rect.centerx - self.diagonal_square,
            self.player.rect.centery + self.diagonal_square]
        self.player_collide_points[6] = [
            self.player.rect.centerx - self.diagonal_square,
            self.player.rect.centery - self.diagonal_square]
        self.player_collide_points[7] = [
            self.player.rect.centerx + self.diagonal_square,
            self.player.rect.centery - self.diagonal_square]

    def _check_player_black_dot_touch(self, black_dot):
        """Checking if the player has touched the black dot (use default pygame collision system)."""
        return self.player.rect.collidepoint(black_dot.rect.centerx, black_dot.rect.centery)
