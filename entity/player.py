import pygame


class Player:
    """A class designed to manage the player."""

    def __init__(self, hb_game):
        """Necessary attributes initialization."""
        self.screen = hb_game.screen
        self.screen_rect = hb_game.screen.get_rect()
        self.settings = hb_game.settings

        # Loading the image of the ball representing the player and get its position.
        self.image = pygame.image.load('res/images/black_ball.png')
        self.rect = self.image.get_rect()

        # Set the player on screen center.
        self.rect.center = self.screen_rect.center

        # The player's horizontal and vertical position is stored as a floating-point number.
        self.x_pos = float(self.rect.x)
        self.y_pos = float(self.rect.y)

        # Options that indicate player movement.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def reset_position(self):
        """Return the player to the center of the screen."""
        self.rect.center = self.screen_rect.center
        self.x_pos = float(self.rect.x)
        self.y_pos = float(self.rect.y)

    def update(self, delta_time):
        """Update the player's position based on the options indicating his movement."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x_pos += self.settings.player_speed * delta_time
        if self.moving_left and self.rect.left > 0:
            self.x_pos -= self.settings.player_speed * delta_time
        if self.moving_up and self.rect.top > 0:
            self.y_pos -= self.settings.player_speed * delta_time
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y_pos += self.settings.player_speed * delta_time

        # Updating rect object based on self.x_pos and self.y_pos.
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

    def draw(self):
        """Display the player on the screen."""
        self.screen.blit(self.image, self.rect)
