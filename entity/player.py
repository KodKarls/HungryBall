import pygame

class Player():
    """Klasa przeznaczona do zarządzania piłką, sterowaną przez
    gracza."""

    def __init__(self, hb_game):
        """Inicjalizacja piłki i jej położenia początkowego."""
        self.screen = hb_game.screen
        self.screen_rect = hb_game.screen.get_rect()
        self.settings = hb_game.settings

        # Wczytanie obrazu piłki i pobranie jej położenia.
        self.image = pygame.image.load('res/images/black_ball.png')
        self.rect = self.image.get_rect()

        # Każda nowa piłka pojawia się na środku ekranu.
        self.rect.center = self.screen_rect.center

        # Położenie poziome i pionowe piłki jest przechowywane w
        # postaci liczby zmiennoprzecinkowej.
        self.x_pos = float(self.rect.x)
        self.y_pos = float(self.rect.y)

        # Opcje wskazujące na poruszanie się piłki.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Uaktualnienie położenia piłki na podstawie opcji wskazującej
        na jej ruch."""
        # Uaktualnienie wartości współrzędnej X piłki, a nie jej prostokąta.
        if self.moving_right:
            self.x_pos += self.settings.ball_speed_x
        if self.moving_left:
            self.x_pos -= self.settings.ball_speed_x
        if self.moving_up:
            self.y_pos -= self.settings.ball_speed_y
        if self.moving_down:
            self.y_pos += self.settings.ball_speed_y

        # Uaktualninie obiektu rect na podstawie wartości self.x_pos i self.y_pos.
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

    def blitme(self):
        """Wyświetlenie piłki w jej aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)
