import sys

import pygame

from settings import Settings
from entity.player import Player
from entity.dot import Dot

class HungryBall:
    """Ogólna klasa przeznaczona do zarządzania zasobami
    i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(self.settings.title)

        # Utworzenie gracza.
        self.player = Player(self)

        # Utworzenie kropki czarnej i pustej grupy kropek czerwonych.
        self.black_dot = Dot(self, self.player, self.settings.black_dot_color)
        self.red_dots = pygame.sprite.Group()

        # Utworzenie odpowiedniej liczby kropek czerwonych.
        self._create_red_dots()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            # Sprawdzenie stanu gry.
            if self.settings.game_active:
                self._check_events()
                self.player.update()
                self._update_dots()

            self._update_screen()

    def _create_red_dots(self):
        """Utworzenie odpowiedniej liczby czerwonych kropek."""
        number = self.settings.red_dots_amount
        while number > 0:
            self._create_red_dot()
            number -= 1

    def _create_red_dot(self):
        """Utworzenie pojedynczej czerwonej kropki i dodanie jej do grupy."""
        red_dot = Dot(self, self.player, self.settings.red_dot_color)
        self.red_dots.add(red_dot)

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False

    def _update_dots(self):
        """Uaktualnie pozycji kropek."""
        # Reakcja na kolizję gracza z czarną kropką.
        if self._check_player_black_dot_collision():
            self.black_dot.rand_new_position()
            self.red_dots.empty()
            self.settings.increase_red_dots_amount()
            self._create_red_dots()

        # Reakcja na kolizję gracza z czerwoną kropką.
        if self._check_player_red_dots_collision():
            self._reset_game()

    def _check_player_black_dot_collision(self):
        """Sprawdzenie kolizji gracza z czarną kropką."""
        return self.player.rect.collidepoint(
                self.black_dot.rect.centerx, self.black_dot.rect.centery)

    def _check_player_red_dots_collision(self):
        """Sprawdzenie kolizji gracza z czerwonymi kropkami."""
        return pygame.sprite.spritecollideany(self.player, self.red_dots)

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        # Wypełnienie ekranu kolorem tła.
        self.screen.fill(self.settings.bg_color)

        # Uaktualnienie obrazów kropek.
        self.black_dot.draw()
        for red_dot in self.red_dots.sprites():
            red_dot.draw()

        # Uaktualnienie obrazu gracza.
        self.player.blitme()

        # Odświeżenie ekranu pygame.
        pygame.display.flip()

    def _reset_game(self):
        """Zresetowanie gry po zjedzeniu dowolnej czerwonej kropki."""
        self.player.reset_position()
        self.red_dots.empty()
        self.settings.red_dots_amount = 2
        self._create_red_dots()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    hungry_ball = HungryBall()
    hungry_ball.run_game()
