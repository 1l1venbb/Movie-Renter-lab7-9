class MovieList:
    def __init__(self):
        self.movies = []

    def __len__(self):
        """
        Returns the number of clients.
        """
        return len(self.movies)

    def isEmpty(self):
        """
        Checks if the list is empty
        :return: True if list is empty (bool)
        """
        if len(self.movies) == 0:
            return True
        return False

    def getMovie(self, ID):
        """
        Returns a movie with the given ID
        :param ID: ID of the movie
        :return: The movie or None
        """
        for movie in self.movies:
            if movie.getID() == ID:
                return movie
        return None

    def getNewID(self):
        """
        Generates a new movie ID.
        :return: The new movie ID (int)
        """
        if self.isEmpty():
            return 0
        return self.movies[-1].id + 1

    def addMovie(self, movie):
        """
        Adds a movie to the list of movies
        :param movie: Movie object
        """
        if movie.getID() in self.movies:
            raise Exception("Client ID already exists")
        else:
            #client.setID(self.getNewID())
            self.movies.append(movie)

    def deleteMovie(self, ID):
        """
        Deletes a movie from the list of movies
        :param ID: ID of the movie to delete
        :raises: Exception if the movie does not exist
        """
        movie = self.getMovie(ID)
        if movie is not None:
                self.movies.remove(movie)

        else:
            raise Exception("Movie does not exist")

    def getAll(self):
        """
        Returns all movies in the list
        :return: list
        """

        return [x for x in self.movies]

    def modifyMovie(self, movie):
        """
        Modifies a movie in the list of movies
        :param movie: Movie object
        """
        actualMovie = self.getMovie(movie.getID())
        actualMovie.setTitle(movie.getTitle())
        actualMovie.setDescription(movie.getDescription())
        actualMovie.setGenre(movie.getGenre())
        actualMovie.setReleaseYear(movie.getReleaseYear())

