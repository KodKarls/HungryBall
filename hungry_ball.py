import sys

import pygame

from utils.settings import Settings
from utils.game_stats import GameStats
from utils.scoreboard import Scoreboard
from utils.collision_system import CollisionSystem
from utils.file_manager import FileManager
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

        # Utworzenie obiektu clock, który zapewnia niezależność działania gry
        # od wydajności sprzętu na którym jest ona uruchamiana oraz obiektu
        # do przechowywania obecnej ilości czasu, który upłynął.
        self.clock = pygame.time.Clock()
        self.delta_time = 0.0

        # Utworzenie obiektu przeznaczonego do przechowywania danych statystycznych
        # gry oraz utworzenie obiektu klasy Scoreboard.
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        # Utworzenie gracza.
        self.player = Player(self)

        # Utworzenie obiektu systemu kolizji.
        self.collision_system = CollisionSystem(self)

        # Utworzenie kropki czarnej i pustej grupy kropek czerwonych.
        self.black_dot = Dot(self, self.player, self.settings.black_dot_color)
        self.red_dots = pygame.sprite.Group()

        # Utworzenie odpowiedniej liczby kropek czerwonych.
        self._create_red_dots()

        # Wylosowanie początkowej pozycji kropki czarnej.
        self.black_dot.rand_black_dot_position(self.red_dots)

        # Utworzenie przycisków "Graj" i "Wyjście".
        self.play_button = Button(self, 200, 50, 160, "Graj")
        self.exit_button = Button(self, 200, 50, 80, "Wyjście")

        # Utworzenie obiketu do zapisu danych w pliku.
        self.file_manager = FileManager()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            # Liczenie delta time.
            self.delta_time = self.clock.tick(60) * .001 * self.settings.target_fps

            self._check_events()

            # Sprawdzenie stanu gry.
            if self.stats.game_active:
                self.player.update(self.delta_time)
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
        red_dot.rand_red_dot_position()
        self.red_dots.add(red_dot)

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_exit_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.player.moving_down = True

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisza."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player.moving_left = False
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.player.moving_down = False

    def _check_play_button(self, mouse_pos):
        """Sprawdzenie czy przycisk "Graj" został kliknięty przez użytkownika."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.game_active = True
            self._reset_game()

            # Ukrycie kursora myszy.
            pygame.mouse.set_visible(False)

    def _check_exit_button(self, mouse_pos):
        """Sprawdzenie czy przycisk "Wyjście" został kliknięty przez użytkownika."""
        button_clicked = self.exit_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Wyjście z gry.
            sys.exit(0)

    def _update_dots(self):
        """Uaktualnie pozycji kropek."""
        # Reakcja na kolizję gracza z czarną kropką.
        if self.collision_system.check_player_black_dot_collision(self.black_dot):
            self.stats.score += self.settings.dot_point
            self.stats.number_black_dots_eaten += self.settings.black_dots_eaten_increase
            self.stats.level += self.settings.level_increase
            self.scoreboard.prep_score()
            self.red_dots.empty()
            self.settings.increase_red_dots_amount()
            self.settings.increase_player_speed()
            self._create_red_dots()
            self.black_dot.rand_black_dot_position(self.red_dots)

        # Reakcja na kolizję gracza z czerwoną kropką.
        if self.collision_system.check_player_red_dots_collision(self.red_dots):
            self.file_manager.save_data(self.stats.score)
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        # Wypełnienie ekranu kolorem tła.
        self.screen.fill(self.settings.bg_color)

        # Wyświetlenie punktacji.
        self.scoreboard.show_score()

        # Uaktualnienie obrazów kropek.
        self.black_dot.draw()
        for red_dot in self.red_dots.sprites():
            red_dot.draw()

        # Uaktualnienie obrazu gracza.
        self.player.blitme()

        # Wyświetlenie przycisku tylko wtedy, gdy gra jest nieaktywna.
        if not self.stats.game_active:
            self.play_button.draw()
            self.exit_button.draw()

        # Odświeżenie ekranu pygame.
        pygame.display.flip()

    def _reset_game(self):
        """Zresetowanie gry po zjedzeniu dowolnej czerwonej kropki."""
        self.player.reset_position()
        self.red_dots.empty()
        self.settings.red_dots_amount = 2
        self.stats.score = 0
        self.scoreboard.prep_score()
        self._create_red_dots()
        self.black_dot.rand_black_dot_position(self.red_dots)

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    hungry_ball = HungryBall()
    hungry_ball.run_game()
