import sys

import pygame

from utils.settings import Settings
from utils.game_stats import GameStats
from utils.scoreboard import Scoreboard
from gui.button import Button
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

        # Utworzenie obiektu przeznaczonego do przechowywania danych statystycznych
        # gry oraz utworzenie obiektu klasy Scoreboard.
        self.stats = GameStats(self)
        self.score_board = Scoreboard(self)

        # Utworzenie gracza.
        self.player = Player(self)

        # Utworzenie kropki czarnej i pustej grupy kropek czerwonych.
        self.black_dot = Dot(self, self.player, self.settings.black_dot_color)
        self.red_dots = pygame.sprite.Group()

        # Utworzenie odpowiedniej liczby kropek czerwonych.
        self._create_red_dots()

        # Utworzenie przycisku "Graj".
        self.play_button = Button(self, "Graj")

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()

            # Sprawdzenie stanu gry.
            if self.stats.game_active:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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

    def _check_play_button(self, mouse_pos):
        """Sprawdzenie czy przycisk "Graj" został kliknięty przez użytkownika."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.game_active = True
            self._reset_game()

            # Ukrycie kursora myszy.
            pygame.mouse.set_visible(False)

    def _update_dots(self):
        """Uaktualnie pozycji kropek."""
        # Reakcja na kolizję gracza z czarną kropką.
        if self._check_player_black_dot_collision():
            self.stats.score += self.settings.dot_point
            self.score_board.prep_score()
            self.black_dot.rand_new_position()
            self.red_dots.empty()
            self.settings.increase_red_dots_amount()
            self._create_red_dots()

        # Reakcja na kolizję gracza z czerwoną kropką.
        if self._check_player_red_dots_collision():
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

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

        # Wyświetlenie punktacji.
        self.score_board.show_score()

        # Wyświetlenie przycisku tylko wtedy, gdy gra jest nieaktywna.
        if not self.stats.game_active:
            self.play_button.draw()

        # Odświeżenie ekranu pygame.
        pygame.display.flip()

    def _reset_game(self):
        """Zresetowanie gry po zjedzeniu dowolnej czerwonej kropki."""
        self.player.reset_position()
        self.red_dots.empty()
        self.settings.red_dots_amount = 2
        self.stats.score = 0
        self.score_board.prep_score()
        self._create_red_dots()
        self.black_dot.rand_new_position()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    hungry_ball = HungryBall()
    hungry_ball.run_game()
