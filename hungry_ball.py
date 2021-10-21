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

        self.player = Player(self)
        self.friend_dot = Dot(self, self.player, self.settings.black_dot_color)
        self.red_dots = pygame.sprite.Group()

        self._create_red_dots()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
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
        """Utworzenie pojedynczej czerwonej kropki."""
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
        if self._check_player_friend_dot_collision():
            self.friend_dot.rand_new_position()

        # Reakcja na kolizję gracza z czerwoną kropką.
        if self._check_player_red_dot_collision():
            # Tutaj będzie zakończenie gry.
            pass

    def _check_player_friend_dot_collision(self):
        """Sprawdzenie kolizji gracza z czarną (przyjazną) kropką."""
        return self.player.rect.collidepoint(
                self.friend_dot.rect.centerx, self.friend_dot.rect.centery)

    def _check_player_red_dot_collision(self):
        """Sprawdzenie kolizji gracza z czerwonymi kropkami."""
        return pygame.sprite.spritecollideany(self.player, self.red_dots)

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.settings.bg_color)
        self.friend_dot.draw()
        for red_dot in self.red_dots.sprites():
            red_dot.draw()
        self.player.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    hungry_ball = HungryBall()
    hungry_ball.run_game()
