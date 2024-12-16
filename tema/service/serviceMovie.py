from domain import Movie
from utils.Sorts import Sorts
from utils.randomMovie import RandomMovie


class ServiceMovie:

    def __init__(self, repoMovie, validatorMovie):
        """
        Constructor for ServiceMovie
        :param repoMovie: Object of type MovieRepository
        :param validatorMovie: Object of type MovieValidator
        """
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
        movie = Movie.Movie(ID, title, description, genre, releaseYear, 0, False)
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
        """
        Service for getting a movie
        :param ID: (int)
        :return: Movie object
        """
        return self.repoMovie.getMovie(ID)

    def modifyMovieService(self, ID, title, description, genre, releaseYear):
        """
        Service for modifying a movie
        :param ID: ID of the movie (int)
        :param title: New Title(str)
        :param description: New description(str)
        :param genre: New genre(str)
        :param releaseYear: New release year(int between 1878 and 2024)
        """
        movie = Movie.Movie(ID, title, description, genre, releaseYear, 0, False)
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

    def searchByTitle(self, title):
        """
        Searches movies by their title
        :param title: title to search
        :return: list of movies with the title title
        """
        lst = [movie for movie in self.repoMovie.getAll() if movie.getTitle() == title]
        if len(lst) == 0:
            raise ValueError
        else:
            return lst

    def searchByGenre(self, genre):
        """
        Searches movies by their genre
        :param genre: genre to search
        :return: list of movies with the genre genre
        """
        lst = [movie for movie in self.repoMovie.getAll() if movie.getGenre() == genre]
        if len(lst) == 0:
            raise ValueError
        else:
            return lst

    def searchByReleaseYear(self, year):
        """
        Searches movies by their release year
        :param year: release year to search
        :return: list of movies with the release year year
        """
        lst = [movie for movie in self.repoMovie.getAll() if movie.getReleaseYear() == year]
        if len(lst) == 0:
            raise ValueError
        else:
            return lst

    def generateMovieService(self):
        """
        Generates a random movie and adds it to the repository
        """

        randomMovie = RandomMovie()

        ID = 0

        while True:
            try:
                ID = randomMovie.generateRandomID()
                self.repoMovie.isIDUnique(ID)
                break
            except ValueError:
                continue

        m = randomMovie.generateRandomMovie(ID)
        self.addMovieService(m["id"], m["title"], m["description"], m["genre"], m["releaseYear"])

    def showMostRentedMoviesService(self):
        """
        Service for showing the most rented movies
        """
        lst = []
        for movie in self.repoMovie.getAll():
            lst.append(movie)
        sort = Sorts()
        #lst.sort(key = lambda x: x.getCopiesRented(), reverse=True)
        sort.insertionSort(lst, lambda x: x.getCopiesRented(), reverse=True)
        return [lst[0], lst[1], lst[2]]

    def showLeastRentedMoviesService(self):
        """
        Service for showing the least rented movies
        """
        lst = []
        for movie in self.repoMovie.getAll():
            lst.append(movie)

        sort = Sorts()
        #lst.sort(key=lambda x: x.getCopiesRented(), reverse=False)
        sort.insertionSort(lst, lambda x: x.getCopiesRented(), reverse=False)
        return [lst[0], lst[1], lst[2]]