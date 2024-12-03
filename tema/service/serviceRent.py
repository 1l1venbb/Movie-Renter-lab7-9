from domain import Rent
from utils.randomRent import RandomRent


class ServiceRent:

    def __init__(self, repoRents, validatorRent, movieRepo, clientRepo):
        self.movieRepo = movieRepo
        self.repoRents = repoRents
        self.validatorRent = validatorRent
        self.clientRepo = clientRepo

    def addRentService(self, ID, IDClient, IDMovie, day, month, year):
        """
        Service for adding rents
        :param ID: ID of the rent
        :param IDClient: ID of the client renting
        :param IDMovie: ID of the movie rented
        :param day: day of rent
        :param month: month of rent
        :param year: year of rent
        """
        try:
            rent = Rent.Rent(ID, IDClient, IDMovie, day, month, year, 0, 0, 0, False)
            self.validatorRent.validateRent(rent, self.clientRepo.getAll(), self.movieRepo.getAll())
            self.repoRents.addRent(rent)

            movie = self.movieRepo.getMovie(IDMovie)
            movie.wasRented()
            self.movieRepo.writeToFile()

            client = self.clientRepo.getClient(IDClient)
            client.rented()
            self.clientRepo.writeToFile()

        except ValueError as ve:
            raise ValueError(ve)

    def addReturnService(self, ID, day, month, year):
        """
        Service for adding returns
        :param ID: ID of the rent
        :param day: day of return
        :param month: month of return
        :param year: year of return
        """
        rent = self.repoRents.getRent(ID)
        try:
            self.validatorRent.validateReturnDate(day, month, year, rent)
            rent.setReturnDate(day, month, year)
            self.repoRents.modifyRent(rent)

            movieID = self.repoRents.getRent(ID).getMovieID()
            movie = self.movieRepo.getMovie(movieID)
            movie.wasReturned()
            self.movieRepo.writeToFile()

            clientID = self.repoRents.getRent(ID).getClientID()
            client = self.clientRepo.getClient(clientID)
            client.returned()
            self.clientRepo.writeToFile()

        except ValueError as ve:
            raise ValueError(ve)

    def getAllRentsService(self):
        """
        :return: The full list of rents
        """
        return self.repoRents.getAll()

    def deleteRentService(self, ID):
        """
        Service for deleting a rent
        :param ID: ID of the rent to be deleted
        """
        self.repoRents.deleteRent(ID)

    def getRentService(self, ID):
        """
        Service for getting a rent
        :param ID: ID of the rent
        :return: the rent object
        """
        return self.repoRents.getRent(ID)

    def modifyRentService(self, ID, newID, IDClient, IDMovie, day, month, year, returnDay, returnMonth, returnYear, clientList, movieList):
        """
        Service for modifying a rent
        :param ID: ID of rent object to be modified
        :param newID: new rent ID
        :param IDClient: new client ID
        :param IDMovie: new movie ID
        :param day: new day of rent
        :param month: new month of rent
        :param year: new year of rent
        :param returnDay: new return day
        :param returnMonth: new return month
        :param returnYear: new return year
        :param clientList: list of clients
        :param movieList: list of movies
        """
        try:
            newID = int(newID) if newID != "" else self.repoRents.getRent(ID).getID()
            IDClient = int(IDClient) if IDClient != "" else self.repoRents.getRent(ID).getClientID()
            IDMovie = int(IDMovie) if IDMovie != "" else self.repoRents.getRent(ID).getMovieID()
            day = int(day) if day != "" else self.repoRents.getRent(ID).getRentDay()
            month = int(month) if month != "" else self.repoRents.getRent(ID).getRentMonth()
            year = int(year) if year != "" else self.repoRents.getRent(ID).getRentYear()
            returnDay = int(returnDay) if returnDay != "" else self.repoRents.getRent(ID).getReturnDay()
            returnMonth = int(returnMonth) if returnMonth != "" else self.repoRents.getRent(ID).getReturnMonth()
            returnYear = int(returnYear) if returnYear != "" else self.repoRents.getRent(ID).getReturnYear()
        except ValueError:
            raise ValueError("All ID, day, month, and year values must be integers or empty strings.")

        rent = Rent.Rent(newID, IDClient, IDMovie, day, month, year, returnDay, returnMonth, returnYear, False)

        try:
            self.validatorRent.validateRent(rent, clientList, movieList)
        except ValueError as ve:
            raise ValueError(ve)
        if returnDay != 0 or returnMonth != 0 or returnYear != 0:
            try:
                self.validatorRent.validateReturnDate(returnDay, returnMonth, returnYear, rent)
            except ValueError as ve:
                raise ValueError(ve)

        self.repoRents.modifyRent(rent, ID)


    def searchRentByClientID(self, ID):
        """
        Searches rents by client ID
        :param ID: Client's ID who rented movies
        :return: list of rents
        """
        lst = [rent for rent in self.repoRents.getAll() if rent.getClientID() == ID]
        if len(lst) == 0:
            raise ValueError("This client never rented a movie before")
        else:
            return lst

    def searchRentByMovieID(self, ID):
        """
        Searches rents by movie ID
        :param ID: Movie's ID that was rented
        :return: list of rents
        """
        lst = [rent for rent in self.repoRents.getAll() if rent.getMovieID() == ID]
        if len(lst) == 0:
            raise ValueError("This movie was never rented")
        else:
            return lst

    def generateRentService(self):
        """
        Generates a random rent and adds it to the repository
        """

        randomRent = RandomRent(self.clientRepo, self.movieRepo)
        ID = 0
        while True:
            try:
                ID = randomRent.generateRandomID()
                self.repoRents.isIDUnique(ID)
                break
            except ValueError:
                continue

        r = randomRent.generateRandomRent(ID)
        self.addRentService(r["id"], r["clientID"], r["movieID"], r["rentDay"], r["rentMonth"], r["rentYear"])