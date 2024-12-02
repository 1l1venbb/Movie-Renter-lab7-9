from domain.Eraseable import Erase

class Client(Erase):

    def __init__(self, ID, firstName, lastName, cnp, copiesRented):
        """
        Constructor for Client class
        :param firstName: Client's first name (string)
        :param lastName: Client's last name (string)
        :param cnp: Client's CNP (int)
        """
        super().__init__()
        self.attr = {"id" : ID, "firstName" : firstName, "lastName" : lastName, "cnp" : cnp, "copiesRented" : copiesRented}

    def __str__(self):
        return (f"Client:\n"
                f"  ID: {self.attr["id"]}\n"
                f"  First Name: {self.attr["firstName"]}\n"
                f"  Last Name: {self.attr["lastName"]}\n"
                f"  CNP: {self.attr["cnp"]}\n"
                f"  Copies Rented: {self.attr["copiesRented"]}")

    def __eq__(self, other):
        if isinstance(other, Client):
            return (self.attr["id"] == other.attr["id"] and
                    self.attr["firstName"] == other.attr["firstName"] and
                    self.attr["lastName"] == other.attr["lastName"] and
                    self.attr["cnp"] == other.attr["cnp"])
        return False

    def getID(self):
        """
        :return: Client ID (int)
        """
        return self.attr["id"]

    def getFirstName(self):
        """
        :return: Client's first name (string)
        """
        return self.attr["firstName"]

    def getLastName(self):
        """
        :return: Client's last name (string)
        """
        return self.attr["lastName"]

    def getCNP(self):
        """
        :return: Client's CNP (int)
        """
        return self.attr["cnp"]

    def getCopiesRented(self):
        """
        :return: The number of movie copies rented
        """
        return self.attr["copiesRented"]

    def setFirstName(self, firstName):
        """
        Sets the client's first name.
        :param firstName: Client's first name (string)
        """
        self.attr["firstName"] = firstName

    def setLastName(self, lastName):
        """
        Sets the clients last name.
        :param lastName: Client's last name (string)
        """
        self.attr["lastName"] = lastName

    def setCNP(self, cnp):
        """
        Sets the Client's CNP (int)
        :param cnp: client's CNP (int)
        """
        self.attr["cnp"] = cnp

    def rented(self):
        """
        Counts the copies currently rented by a client.
        """
        self.attr["copiesRented"] += 1

    def returned(self):
        """
        Counts the copies currently rented by a client.
        """
        self.attr["copiesRented"] -= 1

class ClientValidator:

    def validateClient(self, client):
        """
        Checks if a client is valid.
        :param client: Client object to validate
        :raise: ValueError if object is invalid
        """
        errors = ""

        if client.getFirstName().strip() == "":
            errors+= "First Name cannot be empty"

        if client.getLastName().strip() == "":
            errors+="Last Name cannot be empty"

        if len(client.getCNP()) != 13:
            errors+= "CNP cannot be empty or is too short or too long"

        try:
            int(client.getCNP())
        except TypeError:
            errors+= "CNP is invalid"

        if errors != "":
            raise ValueError(errors)