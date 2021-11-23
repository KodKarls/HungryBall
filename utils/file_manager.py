from datetime import date


class FileManager:
    """A class designed to save data into the file."""

    def __init__(self):
        """Necessary attributes initialization."""
        self.filename = 'best_score.txt'
        self.filename_path = 'data/' + self.filename

        self.data = {}

    def save_data(self, score):
        """Saving the data with the highest score into the file."""
        if self._check_data(score):
            # Get the current date and time.
            date_now = date.today().strftime("%d-%m-%Y")

            # Preparation of data for saving.
            self.data['best_score'] = str(score)
            self.data['date'] = date_now

            with open(self.filename_path, 'w') as file_object:
                for key, value in self.data.items():
                    file_object.write(key + ': ' + value + '\n')

    def _check_data(self, score):
        """Checking the current data in the file."""
        try:
            with open(self.filename_path, 'r') as file_object:
                contents = file_object.read()
        except FileNotFoundError:
            return True

        # Preparation of data for saving.
        words = contents.split()
        try:
            self.data['best_score'] = words[1]
        except IndexError:
            return True

        # Convert a score to a number.
        best_score = int(self.data['best_score'])
        current_score = int(score)

        # Checking if a new record has been set.
        if current_score > best_score:
            return True

        return False
