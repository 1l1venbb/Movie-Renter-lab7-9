from calendar import monthrange
from domain.Eraseable import Erase


class Rent(Erase):

    def __init__(self, ID, clientID, movieID, day, month, year, rday, rmonth, ryear, isDeleted):
        """
        Constructor for Rent class
        :param ID: ID of a renting (int)
        :param clientID: ID of the client that rented
        :param movieID: ID of the movie that was rented
        :param day: Day of renting
        :param month: Month of renting
        :param year: Year of renting
        """
        super().__init__(isDeleted)
        self.ID = ID
        self.clientID = clientID
        self.movieID = movieID
        self.rentDate = {"day" : day, "month" : month, "year" : year}
        self.returnDate = {"day" : rday, "month" : rmonth, "year" : ryear}

    def __str__(self):
        rent_info = (f"Rent:\n"
                     f"  ID: {self.ID}\n"
                     f"  Client ID: {self.clientID}\n"
                     f"  Movie ID: {self.movieID}\n"
                     f"  Rent Date: {self.rentDate}\n")

        if self.returnDate == {"day": 0, "month": 0, "year": 0}:
            return rent_info + "  Return Date: Not yet returned"
        else:
            return rent_info + f"  Return Date: {self.returnDate}"

    def getID(self):
        """
        :return: Rent ID (int)
        """
        return self.ID

    def getClientID(self):
        """
        :return: The client's ID
        """
        return self.clientID

    def getMovieID(self):
        """
        :return: The movie's ID
        """
        return self.movieID

    def getRentDay(self):
        """
        :return: Day of the renting (int)
        """
        return self.rentDate["day"]

    def getRentMonth(self):
        """
        :return: Month of the renting (int)
        """
        return self.rentDate["month"]

    def getRentYear(self):
        """
        :return: Year of the renting (int)
        """
        return self.rentDate["year"]

    def getReturnDay(self):
        """
        :return: Date of the return (int)
        """
        return self.returnDate["day"]
    
    def getReturnMonth(self):
        """
        :return: Month of the return (int)
        """
        return self.returnDate["month"]

    def getReturnYear(self):
        """
        :return: Year of the return (int)
        """
        return self.returnDate["year"]

    def setReturnDate(self, day, month, year):
        """
        Sets the return date
        :param day: the day of return (int)
        :param month: the month of return (int)
        :param year: the year of return (int)
        """
        self.returnDate = {"day" : day, "month" : month, "year" : year}

    def setID(self, ID):
        """
        Sets the rent's ID
        """
        self.ID = ID

    def setClientID(self, clientID):
        """
        Sets the client's ID
        :param clientID: Client ID to be set
        """
        self.clientID = clientID

    def setMovieID(self, movieID):
        """
        Sets the movie's ID
        :param movieID: Movie ID to be set
        """
        self.movieID = movieID

    def setRentDate(self, day, month, year):
        """
        Sets the rent date
        :param day: day of renting (int)
        :param month: month of renting (int)
        :param year: year of renting (int)
        """
        self.rentDate = {"day" : day, "month" : month, "year" : year}

class RentValidator:

    def validateRent(self, rent, clientList, movieList):
        """
        Checks if a rent is valid
        :param rent: Rent object to validate
        :param clientList: Object from clients repository
        :param movieList: Object from movies repository
        :raise: ValueError if object is invalid
        """
        if not any(client.getID() == rent.getClientID() for client in clientList):
            raise ValueError("Invalid client ID")

        if not any(movie.getID() == rent.getMovieID() for movie in movieList):
            raise ValueError("Invalid movie ID")

        day = rent.getRentDay()
        month = rent.getRentMonth()
        year = rent.getRentYear()

        errors = ""

        if year < 2024 or year > 2025:
            errors+= "Invalid year"
        if month < 1 or month > 12:
            errors+= "Invalid month"
        if day < 1 or day > monthrange(year, month)[1]:
            errors+= "Invalid day"

        if errors != "":
            raise ValueError(errors)

    def validateReturnDate(self, day, month, year, rent):
        """
        Checks if return date is valid
        :param day: day of return (int)
        :param month: month of return (int)
        :param year: year of return (int)
        :param rent: Rent object to validate
        :raises: ValueError if return date is invalid
        """
        errors = ""

        day1 = rent.getRentDay()
        month1 = rent.getRentMonth()
        year1 = rent.getRentYear()

        rent_date = (year1, month1, day1)
        return_date = (year, month, day)

        if return_date < rent_date:
            errors += "Return date cannot be before the rent date. "

        if year < 2024 or year > 2025:
            errors += "Invalid year"
        if month < 1 or month > 12:
            errors += "Invalid month"
        if day < 1 or day > monthrange(year, month)[1]:
            errors += "Invalid day"

        if errors != "":
            raise ValueError(errors)
