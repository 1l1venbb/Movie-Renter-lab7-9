from domain import Movie

class ServiceMovie:

    def __init__(self, repoMovie, validatorMovie):
        self.repoMovie = repoMovie
        self.validatorMovie = validatorMovie

    def addClientService(self, ID, title, description, genre, releaseYear):
        movie = Movie.Movie(ID, title, description, genre, releaseYear)
        self.validatorMovie.validateMovie(movie)
        self.repoMovie.addMovie(movie)

