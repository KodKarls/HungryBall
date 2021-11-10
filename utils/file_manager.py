from datetime import date

class FileManager:
    """Klasa przeznaczona do zapisywania danych w pliku."""

    def __init__(self):
        """Inicjalizacja danych."""
        self.filename = 'best_score.txt'
        self.filename_path = 'data/' + self.filename

        self.data = {}

    def save_data(self, score):
        """Zapisanie danych o największym wyniku w pliku."""
        if self._check_data(score):
            # Pobranie aktualnej daty i czasu.
            date_now = date.today().strftime("%d-%m-%Y")

            # Przygotowanie danych do zapisu.
            self.data['Najlepszy wynik'] = str(score)
            self.data['Data'] = date_now

            with open(self.filename_path, 'w') as file_object:
                for key, value in self.data.items():
                    file_object.write(key + ': ' + value + '\n')

    def _check_data(self, score):
        """Sprawdzenie aktualnych danych w pliku."""
        contents = ''
        try:
            with open(self.filename_path, 'r') as file_object:
                contents = file_object.read()
        except FileNotFoundError:
            return True

        # Przygotowanie danych do zapisu.
        words = contents.split()
        try:
            self.data['Najlepszy wynik'] = words[2]
        except IndexError:
            return True

        # Konwersja punktacji na liczbę.
        best_score = int(self.data['Najlepszy wynik'])
        current_score = int(score)

        # Sprawdzenie czy ustanowiono nowy rekord.
        if current_score > best_score:
            return True

        return False
