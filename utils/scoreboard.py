import pygame.font


class Scoreboard:
    """A class designed to provide information on scoring."""

    def __init__(self, hb_game):
        """Necessary attributes initialization."""

        self.screen = hb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = hb_game.settings
        self.stats = hb_game.stats

        # Font settings.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(self.settings.font_name, self.settings.font_point_size)

        # Preparing initial scoring images.
        self.score_image = ''
        self.score_rect = 0
        self.prep_score()

    def prep_score(self):
        """Convert the scoring to a generated image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Setting image position in the top center of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midtop = self.screen_rect.midtop
        self.score_rect.top = 20

    def show_score(self):
        """Display the score on the screen.."""
        self.screen.blit(self.score_image, self.score_rect)
