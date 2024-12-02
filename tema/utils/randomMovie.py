import random

titles = ["The Horse in Motion" , "Iron Man", "Star Wars", "1917", "Batman", "Morbius"]
descriptions = ["The first movie ever made", "The coolest movie ever made", "The funniest movie ever made", "The saddest movie ever made"]
genres = ["Action", "Adventure", "Romance", "Comedy", "Sci-fi"]
releaseYears = [1878, 2022, 2010, 1998, 1975, 2008, 2019]

class RandomMovie:

    def __init__(self):
        """
        Constructor method for RandomMovie class
        """
        self.titles = titles
        self.descriptions = descriptions
        self.genres = genres
        self.releaseYears = releaseYears

    def generateRandomID(self):
        """
        Generates a random ID.
        :return: ID (int)
        """
        ID = random.randint(0, 1000000)
        return ID

    def generateRandomTitle(self):
        """
        Generates a random title.
        :return: title (str)
        """
        title = random.choice(self.titles)
        return title

    def generateRandomDescription(self):
        """
        Generates a random description.
        :return: description (str)
        """
        description = random.choice(self.descriptions)
        return description

    def generateRandomGenre(self):
        """
        Generates a random genre.
        :return: genre (str)
        """
        genre = random.choice(self.genres)
        return genre

    def generateRandomReleaseYear(self):
        """
        Generates a random release year.
        :return: int
        """
        releaseYear = random.choice(self.releaseYears)
        return releaseYear

    def generateRandomMovie(self, ID):
        """
        Generates a random movie.
        :return:
        """

        title = self.generateRandomTitle()
        description = self.generateRandomDescription()
        genre = self.generateRandomGenre()
        releaseYear = self.generateRandomReleaseYear()

        movie = {
            "id": ID,
            "title": title,
            "description": description,
            "genre": genre,
            "releaseYear": releaseYear
        }

        return movie