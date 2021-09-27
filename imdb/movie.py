
class Movie:
    def __init__(self, title, year, genre, director):
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director

    def __str__(self):
        return self.title

    def has_genre(self, g):
        lower_genre = self.genre.lower()
        return g in lower_genre




