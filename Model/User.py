from Model.Movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __str__(self):
        movies = ""
        for m in self.movies:
            movies = "\n" + str(m)
        return self.name + " " + movies

    def __repr__(self):
        return f"<User {self.name}>"

    def addMovie(self, name, genre):
        movie = Movie(name, genre)
        self.movies.append(movie)

    def deleteMovie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def markWatched(self, num):
        self.movies[num-1].watched = True

    def watchedMovies(self):
        return list(filter(lambda movie: movie.watched, self.movies))