import pygame
from pygame.sprite import Sprite

class Dot(Sprite):
    """Klasa przeznaczona do zarządzania kropkami pojawiającymi
    się w grze."""

    def __init__(self, hb_game, color):
        """Inicjalizacja składników kropki."""
        super().__init__()
        self.screen = hb_game.screen
        self.settings = hb_game.settings
        self.color = color
        self.image = pygame.Surface(
            (self.settings.dot_radius * 2, self.settings.dot_radius * 2))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (700, 700)

        # Położenie kropki jest zdefiniowane za pomocą wartości zmiennoprzecinkowej.
        self.x_pos = float(self.rect.x)
        self.y_pos = float(self.rect.y)

    def draw(self):
        """Wyświetlenie kropki na ekranie."""
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.settings.dot_radius)
        