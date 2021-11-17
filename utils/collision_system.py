import math

import pygame


class CollisionSystem:
    """Klasa przeznaczona do obsługi systemu kolizji."""

    def __init__(self, hb_game):
        """Inicjalizacja atrybutów dotyczących systemu kolizji."""
        self.player = hb_game.player
        self.settings = hb_game.settings

        # Obliczenie długości boku kwadratu znajdującego się w ćwiartce koła.
        self.diagonal_square = round(self.settings.dot_radius / math.sqrt(2), 0)

        # Słownik przechowujący wszystkie punkty koła, które są wymagane do sprawdzenia kolizji.
        self.player_collide_points = {}

    def check_player_black_dot_collision(self, black_dot):
        """Sprawdzenie kolizji gracza z czarną kropką."""
        # Sprawdzamy dotknięcie gracza i dowolnej czarnej kropki.
        if self._check_player_black_dot_touch(black_dot):
            # Dodajemy wszystkie aktualne punkty kolizji gracza do słownika.
            self._update_player_collide_points()

            for _, values in self.player_collide_points.items():
                # Sprawdzamy odległość między punktami kolizji, a środkiem czarnej kropki.
                distance = math.sqrt(
                    (values[0] - black_dot.rect.centerx)**2 +
                    (values[1] - black_dot.rect.centery)**2)
                if distance <= self.settings.dot_radius:
                    return True

        return False

    def check_player_red_dots_collision(self, red_dots):
        """Sprawdzenie kolizji gracza z czerwoną kropką."""
        # Sprawdzamy dotknięcie gracza i dowolnej czerwonej kropki.
        red_dot = pygame.sprite.spritecollideany(self.player, red_dots)

        if red_dot is None:
            return False

        # Dodajemy wszystkie aktualne punkty kolizji gracza do słownika.
        self._update_player_collide_points()

        for _, values in self.player_collide_points.items():
            points = list(values)
            # Sprawdzamy odległość między punktami kolizji, a środkiem czerwonej kropki.
            distance = math.sqrt(
                (points[0] - red_dot.rect.centerx)**2 + (points[1] - red_dot.rect.centery)**2)
            if distance <= self.settings.dot_radius:
                return True

        return False

    def _update_player_collide_points(self):
        """Aktualizacja punktów kolizji gracza."""
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
        """Sprawdzenie czy gracz dotknął czarną kropką."""
        return self.player.rect.collidepoint(black_dot.rect.centerx, black_dot.rect.centery)
