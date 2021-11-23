import pygame.font


class Button:
    """A class representing the button."""

    def __init__(self, hb_game, width, height, pos_y, msg):
        """Necessary attributes initialization."""
        self.screen = hb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = hb_game.settings

        # Defining the dimensions, positions, and properties of the button.
        self.width, self.height = width, height
        self.pos_y = pos_y
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(self.settings.font_name, self.settings.font_button_size)

        # Create the button rectangle and set its appropriate position.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 120 - self.pos_y

        # One-time preparation of the message displayed by the button.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Placing a message in the generated image and centering the text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Display the button on the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
