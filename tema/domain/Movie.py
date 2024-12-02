from domain.Eraseable import Erase

class Movie(Erase):

    def __init__(self, ID, title, description, genre, releaseYear, copiesRented):
        """
        Constructor for Movie class
        :param ID: ID of movie (int)
        :param title: Title of movie (string)
        :param description: Description of movie (string)
        :param genre: Genre of movie (string)
        :param releaseYear: The year of release of the movie (int)
        """

        super().__init__()

        self.ID = ID
        self.title = title
        self.description = description
        self.genre = genre
        self.releaseYear = releaseYear
        self.copiesRented = copiesRented

    def __str__(self):
        return (f"Movie:\n"
                f"  ID: {self.ID}\n"
                f"  Title: {self.title}\n"
                f"  Description: {self.description}\n"
                f"  Genre: {self.genre}\n"
                f"  Release Year: {self.releaseYear}\n"
                f"  Copies Rented: {self.copiesRented}")

    def __eq__(self, other):
        if isinstance(other, Movie):
            return (self.ID == other.ID and
                    self.title == other.title and
                    self.description == other.description and
                    self.genre == other.genre and
                    self.releaseYear == other.releaseYear)
        return False

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

    def validateMovie(self ,movie):
        """
        Checks if a Movie object is valid
        :param movie: Movie object to validate
        :raise: ValueError if object is invalid
        """
        errors = ""
        if movie.getTitle().strip() == "":
            errors+= "Title cannot be empty"

        if movie.getDescription().strip() == "":
            errors+= "Description cannot be empty"

        if movie.getGenre().strip() == "":
            errors+= "Genre cannot be empty"

        if movie.getReleaseYear() >= 2025 or movie.getReleaseYear() < 1878:
            errors+= "Invalid year"

        if errors != "":
            raise ValueError(errors)