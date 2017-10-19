class OutputToText:

    @classmethod
    def write(cls, text, file_location='temp_text.txt'):
        """ This takes a list of text and overwrites the current
        file location with the aformentioned text."""
        with open(file_location, "w") as file:
            file.write(text)

    @classmethod
    def get(cls, file_location='temp_text.txt'):
        """ This gets all the text from the file_location and
        returns the text data."""
        try:
            with open(file_location) as file:
                return(file.read())
        except FileNotFoundError:
            return False
