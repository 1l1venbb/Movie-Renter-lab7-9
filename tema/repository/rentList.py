class RentList:

    def __init__(self):
        """
        Constructs a list of rents
        """
        self.rents = []

    def isEmpty(self):
        """
        Checks if the list is empty
        """

        if len(self.rents) == 0:
            return True
        return False

    def getRent(self, ID):
        """
        Returns a rent with the given ID
        :param ID: ID of the rent
        :return: The rent or None
        """

        for rent in self.rents:
            if rent.getID() == ID:
                return rent
        return None

    def addRent(self, rent):
        """
        Adds a rent to the list of rents
        :param rent: Rent object
        :raises: Exception if the rent ID already exists
        """
        if self.getRent(rent.getID()) is not None:
            raise Exception("Rent ID already exists")
        else:
            self.rents.append(rent)

    def deleteRent(self, ID):
        """
        Removes a rent from the list of rents
        :param: ID of the rent to delete
        :raises: Exception if the rent does not exist
        """
        if self.getRent(ID) is not None:
            self.rents.remove(self.getRent(ID))
        else:
            raise Exception("Rent does not exist")

    def getAll(self):
        """
        Returns all rents in the list
        :return: list
        """
        return [x for x in self.rents]

    def modifyRent(self, rent):
        """
        Modifies a rent in the list of rents
        :param rent: Rent object
        """

        actualRent = self.getRent(rent.getID())
        actualRent.setClientID(rent.getClientID())
        actualRent.setMovieID(rent.getMovieID())
        actualRent.setRentDate(rent.getRentDay(), rent.getRentMonth(), rent.getRentYear())
        actualRent.setReturnDate(rent.getReturnDay(), rent.getReturnMonth(), rent.getReturnYear())