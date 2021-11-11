import pygame

class Player():
    """Klasa przeznaczona do zarządzania graczem."""

    def __init__(self, hb_game):
        """Inicjalizacja składników gracza."""
        self.screen = hb_game.screen
        self.screen_rect = hb_game.screen.get_rect()
        self.settings = hb_game.settings

        # Wczytanie obrazu piłki, reprezentującej gracza i pobranie jej położenia.
        self.image = pygame.image.load('res/images/black_ball.png')
        self.rect = self.image.get_rect()

        # Gracz pojawia się na środku ekranu.
        self.rect.center = self.screen_rect.center

        # Położenie poziome i pionowe gracza jest przechowywane w
        # postaci liczby zmiennoprzecinkowej.
        self.x_pos = float(self.rect.x)
        self.y_pos = float(self.rect.y)

        # Opcje wskazujące na poruszanie się gracza.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def reset_position(self):
        """Przywrócenie gracza na środek ekranu."""
        self.rect.center = self.screen_rect.center
        self.x_pos = float(self.rect.x)
        self.y_pos = float(self.rect.y)

    def update(self, delta_time):
        """Uaktualnienie położenia gracza na podstawie opcji wskazującej
        na jego ruch."""
        # Uaktualnienie wartości współrzędnej X i Y gracza.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x_pos += self.settings.player_speed * delta_time
        if self.moving_left and self.rect.left > 0:
            self.x_pos -= self.settings.player_speed * delta_time
        if self.moving_up and self.rect.top > 0:
            self.y_pos -= self.settings.player_speed * delta_time
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y_pos += self.settings.player_speed * delta_time

        # Uaktualninie obiektu rect na podstawie wartości self.x_pos i self.y_pos.
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

    def blitme(self):
        """Wyświetlenie gracza w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)
