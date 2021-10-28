import pygame.font

class Scoreboard():
    """Klasa przeznaczona do przedstawiania informacji o punktacji."""

    def __init__(self, hb_game):
        """Inicjalizacja atrybutów dotyczących punktacji."""

        self.screen = hb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = hb_game.settings
        self.stats = hb_game.stats

        # Ustawienia czcionki dla informacji dotyczących punktacji.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(self.settings.font_name, self.settings.font_point_size)

        # Przygotowanie początkowych obrazów z punktacją.
        self.prep_score()

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
            self.text_color, self.settings.bg_color)

        # Wyświetlenie punktacji w środkowej-górnej części ekranu.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midtop = self.screen_rect.midtop
        self.score_rect.top = 20

    def show_score(self):
        """Wyświetlenie punktacji na ekranie."""
        self.screen.blit(self.score_image, self.score_rect)
