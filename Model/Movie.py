class Movie:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.watched = False

    def __str__(self):
        return self.name + " " + self.genre + " " + str(self.watched)

    def __repr__(self):
        return f"{self.name}"