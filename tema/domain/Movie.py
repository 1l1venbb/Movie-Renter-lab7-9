class Movie:

    def __init__(self, ID, title, description, genre, releaseYear):
        """
        Constructor for Movie class
        :param ID: ID of movie (int)
        :param title: Title of movie (string)
        :param description: Description of movie (string)
        :param genre: Genre of movie (string)
        :param releaseYear: The year of release of the movie (int)
        """

        self.ID = ID
        self.title = title
        self.description = description
        self.genre = genre
        self.releaseYear = releaseYear
        self.copiesRented = 0

    def getID(self):
        """
        :return: ID of movie (int)
        """
        return self.ID

    def getTitle(self):
        """
        :return: Title of movie (string)
        """
        return self.title

    def getDescription(self):
        """
        :return: Description of movie (string)
        """
        return self.description

    def getGenre(self):
        """
        :return: Genre of movie (string)
        """
        return self.genre

    def getReleaseYear(self):
        """
        :return: Release of movie (int)
        """
        return self.releaseYear

    def setID(self, ID):
        """
        Sets the ID of the movie
        :param ID: ID of movie (int)
        """
        self.ID = ID

    def setTitle(self, title):
        """
        Sets the title of the movie
        :param title: Title of movie (string)
        """
        self.title = title

    def setDescription(self, description):
        """
        Sets the description of the movie
        :param description: Description of movie (string)
        """
        self.description = description

    def setGenre(self, genre):
        """
        Sets the genre of the movie
        :param genre: Genre of movie (string)
        """
        self.genre = genre

    def setReleaseYear(self, releaseYear):
        """
        Sets the year of release of the movie
        :param releaseYear: Year of release of the movie (int)
        """
        self.releaseYear = releaseYear

    def wasRented(self):
        """
        Adds one copy to the count of copies rented
        """
        self.copiesRented += 1

    def wasReturned(self):
        """
        Subtracts one copy from the count of copies rented
        """
        self.copiesRented -= 1

    def getCopiesRented(self):
        """
        :return: The number of copies rented at the current moment(int)
        """
        return self.copiesRented

class MovieValidator:
    @staticmethod
    def validateMovie(movie):
        """
        Checks if a Movie object is valid
        :param movie: Movie object to validate
        :raise: ValueError if object is invalid
        """
        if movie.getTitle().strip() == "":
            raise ValueError("Title cannot be empty")

        if movie.getDescription().strip() == "":
            raise ValueError("Description cannot be empty")

        if movie.getGenre().strip() == "":
            raise ValueError("Genre cannot be empty")

        if movie.getReleaseYear() >= 2025 or movie.getReleaseYear() < 1878:
            raise ValueError("Invalid year")