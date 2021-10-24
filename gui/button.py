import pygame.font

class Button():
    """Klasa reprezentująca pojedynczy przycisk w grze."""

    def __init__(self, hb_game, width, height, pos_y, msg):
        """Inicjalizacja atrybutów przycisku."""
        self.screen = hb_game.screen
        self.screen_rect = self.screen.get_rect()

        # Zdefiniowanie wymiarów, pozycji i właściwości przycisku.
        self.width, self.height = width, height
        self.pos_y = pos_y
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Utworzenie prostokąta przycisku i ustawienie jego odpowiedniej pozycji.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 120 - self.pos_y

        # Komunikat wyświetlany przez przycisk trzeba przygotować tylko jednokrotnie.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Umieszczenie komunikatu w wygenerowanym obrazie i wyśrodkowanie
        tekstu na przycisku."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Wyświetlenie przycisku w jego aktualnym położeniu."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
