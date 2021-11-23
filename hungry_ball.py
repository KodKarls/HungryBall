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
    """A class designed to resource management and the way the game works."""

    def __init__(self):
        """Necessary attributes initialization."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(self.settings.title)

        # Creating clock object and delta time variable.
        self.clock = pygame.time.Clock()
        self.delta_time = 0.0

        # Creating statistic and scoreboard object.
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        # Creating the player.
        self.player = Player(self)

        # Creating collision system object.
        self.collision_system = CollisionSystem(self)

        # Creating the black dot and group of red dots.
        self.black_dot = Dot(self, self.player, self.settings.black_dot_color)
        self.red_dots = pygame.sprite.Group()

        self._create_red_dots()
        self.black_dot.rand_black_dot_position(self.red_dots)

        # Creating play and exit button.
        self.play_button = Button(self, 200, 50, 160, "Graj")
        self.exit_button = Button(self, 200, 50, 80, "Wyjście")

        # Creating the file manager.
        self.file_manager = FileManager()

    def run_game(self):
        """Game loop."""
        while True:
            self.delta_time = self.clock.tick(60) * .001 * self.settings.target_fps

            self._check_events()

            if self.stats.game_active:
                self.player.update(self.delta_time)
                self._update_dots()

            self._update_screen()

    def _create_red_dots(self):
        """Creating the correct number of red dots."""
        number = self.settings.red_dots_amount
        while number > 0:
            self._create_red_dot()
            number -= 1

    def _create_red_dot(self):
        """Creating a single red dot and adding it to the group."""
        red_dot = Dot(self, self.player, self.settings.red_dot_color)
        red_dot.rand_red_dot_position()
        self.red_dots.add(red_dot)

    def _check_events(self):
        """Reaction to mouse and keyboard events."""
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
        """Reaction to push the key."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.player.moving_down = True

    def _check_keyup_events(self, event):
        """Reaction to release the key."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player.moving_left = False
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.player.moving_down = False

    def _check_play_button(self, mouse_pos):
        """Checking if the play button has been clicked."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.game_active = True
            self._reset_game()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_exit_button(self, mouse_pos):
        """Checking if the exit button has been clicked."""
        button_clicked = self.exit_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            sys.exit(0)

    def _update_dots(self):
        """Update dots."""
        # Reaction for player's and black dot collision.
        if self.collision_system.check_player_black_dot_collision(self.black_dot):
            self.stats.score += self.settings.dot_point
            self.stats.number_black_dots_eaten += self.settings.black_dots_eaten_increase
            self.stats.level += self.settings.level_increase
            self.scoreboard.prep_score()
            self.red_dots.empty()
            self.settings.increase_red_dots_amount(self.stats.level)
            self.settings.increase_player_speed(self.stats.level)
            self._create_red_dots()
            self.black_dot.rand_black_dot_position(self.red_dots)

        # Reaction for player's and red dot collision.
        if self.collision_system.check_player_red_dots_collision(self.red_dots):
            self.file_manager.save_data(self.stats.score)
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Updating the images on the screen and going to a new screen."""
        # Fill the screen with the background color.
        self.screen.fill(self.settings.bg_color)

        # Display scoring.
        self.scoreboard.show_score()

        # Display dots.
        self.black_dot.draw()
        for red_dot in self.red_dots.sprites():
            red_dot.draw()

        # Display the player.
        self.player.draw()

        # Display buttons only if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw()
            self.exit_button.draw()

        # Update the full display Surface to the screen.
        pygame.display.flip()

    def _reset_game(self):
        """Reset the game after the player died ."""
        self.player.reset_position()
        self.red_dots.empty()
        self.settings.red_dots_amount = 2
        self.settings.red_dots_amount_scale = 2
        self.stats.score = 0
        self.scoreboard.prep_score()
        self._create_red_dots()
        self.black_dot.rand_black_dot_position(self.red_dots)


if __name__ == '__main__':
    hungry_ball = HungryBall()
    hungry_ball.run_game()
