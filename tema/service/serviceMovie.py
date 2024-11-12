from domain import Movie

class ServiceMovie:

    def __init__(self, repoMovie, validatorMovie):
        self.repoMovie = repoMovie
        self.validatorMovie = validatorMovie

    def addMovieService(self, ID, title, description, genre, releaseYear):
        """
        Service for adding a movie
        :param ID: ID of the movie
        :param title: Title of the movie
        :param description: Description of the movie
        :param genre: Genre of the movie
        :param releaseYear: Release year of the movie
        """
        movie = Movie.Movie(ID, title, description, genre, releaseYear)
        self.validatorMovie.validateMovie(movie)
        self.repoMovie.addMovie(movie)

    def getAllMoviesService(self):
        """
        Service for getting all movies
        :return: List of all movies
        """
        return self.repoMovie.getAll()

    def deleteMovieService(self, ID):
        """
        Service for deleting a movie
        :param ID: ID of the movie to delete
        """
        self.repoMovie.deleteMovie(ID)

    def getMovieService(self, ID):
        return self.repoMovie.getMovie(ID)

    def modifyMovieService(self, ID, title, description, genre, releaseYear):
        movie = Movie.Movie(ID, title, description, genre, releaseYear)
        if movie is not None:
            if title != "":
                movie.setTitle(title)
            else:
                movie.setTitle(self.repoMovie.getMovie(ID).getTitle())

            if description != "":
                movie.setDescription(description)
            else:
                movie.setDescription(self.repoMovie.getMovie(ID).getDescription())

            if genre != "":
                movie.setGenre(genre)
            else:
                movie.setGenre(self.repoMovie.getMovie(ID).getGenre())

            if releaseYear != "":
                movie.setReleaseYear(releaseYear)
            else:
                movie.setReleaseYear(self.repoMovie.getMovie(ID).getReleaseYear())

            self.validatorMovie.validateMovie(movie)
            self.repoMovie.modifyMovie(movie)