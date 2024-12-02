import random
from utils.otherValidations import Validations
class RandomRent:

    def __init__(self, clientRepository, movieRepository):
        self.validations = Validations()
        self.clientRepository = clientRepository
        self.movieRepository = movieRepository

    def generateRandomID(self):
        """
        Generates a random ID.
        :return: ID (int)
        """
        ID = random.randint(0, 1000000)
        return ID

    def getRandomClientID(self):
        """
        Gets a random client ID.
        :return: the ID.
        """
        clients = self.clientRepository.getAll()
        c = self.clientRepository.getAll()
        rc = random.choice(c)
        return rc.getID()

    def getRandomMovieID(self):
        """
        Gets a random movie ID.
        :return: the ID.
        """
        movies = self.movieRepository.getAll()
        rm = random.choice(movies)
        return rm.getID()

    def generateRandomRent(self, ID):
        """
        Generates a random rent.
        :param ID: random valid ID
        :return: dictionary with rent data
        """
        clientID = self.getRandomClientID()
        movieID = self.getRandomMovieID()
        rentDay = 0
        rentMonth = 0
        rentYear = 0

        while True:
            try:
                rentDay = random.randint(1, 31)
                rentMonth = random.randint(1, 12)
                rentYear = random.randint(2024, 2025)
                self.validations.validateRentDate(rentDay, rentMonth, rentYear)
                break
            except ValueError as e:
                continue

        rent = {
            "id": ID,
            "clientID": clientID,
            "movieID": movieID,
            "rentDay": rentDay,
            "rentMonth": rentMonth,
            "rentYear": rentYear
        }
        return rent
