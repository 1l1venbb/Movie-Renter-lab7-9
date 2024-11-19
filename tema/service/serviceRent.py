from domain import Rent


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
            rent = Rent.Rent(ID, IDClient, IDMovie, day, month, year)
            self.validatorRent.validateRent(rent, self.clientRepo.getAll(), self.movieRepo.getAll())
            self.repoRents.addRent(rent)
            movieID = self.repoRents.getRent(ID).getMovieID()
            movie = self.movieRepo.getMovie(movieID)
            movie.wasRented()
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
        except ValueError:
            raise ValueError("Return date cannot be in the past.")

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
        rent1 = self.repoRents.getRent(ID)
        try:
            newID = int(newID) if newID != "" else None
            IDClient = int(IDClient) if IDClient != "" else None
            IDMovie = int(IDMovie) if IDMovie != "" else None
            day = int(day) if day != "" else None
            month = int(month) if month != "" else None
            year = int(year) if year != "" else None
            returnDay = int(returnDay) if returnDay != "" else None
            returnMonth = int(returnMonth) if returnMonth != "" else None
            returnYear = int(returnYear) if returnYear != "" else None
        except ValueError:
            raise ValueError("All ID, day, month, and year values must be integers or empty strings.")

        rent = Rent.Rent(newID if newID is not None else self.repoRents.getRent(ID).getID(),
                    IDClient if IDClient is not None else self.repoRents.getRent(ID).getClientID(),
                    IDMovie if IDMovie is not None else self.repoRents.getRent(ID).getMovieID(),
                    day if day is not None else self.repoRents.getRent(ID).getRentDay(),
                    month if month is not None else self.repoRents.getRent(ID).getRentMonth(),
                    year if year is not None else self.repoRents.getRent(ID).getRentYear())

        self.validatorRent.validateRent(rent, clientList, movieList)
        self.repoRents.modifyRent(rent)

        if returnDay is not None or returnMonth is not None or returnYear is not None:
            try:

                rent.setReturnDate(
                returnDay if returnDay is not None else rent1.getReturnDay(),
                returnMonth if returnMonth is not None else rent1.getReturnMonth(),
                returnYear if returnYear is not None else rent1.getReturnYear())

                self.validatorRent.validateReturnDate(rent.getReturnDay(),rent.getReturnMonth(),rent.getReturnYear(), rent)
                self.repoRents.getRent(ID).setReturnDate(rent.getReturnDay(), rent.getReturnMonth(), rent.getReturnYear())
            except ValueError:
                raise ValueError("Return date cannot be in the past.")

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
