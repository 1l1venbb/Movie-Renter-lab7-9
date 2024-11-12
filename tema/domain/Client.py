from repository import clientList

class Client:

    def __init__(self, ID, firstName, lastName, cnp):
        """
        Constructor for Client class
        :param firstName: Client's first name (string)
        :param lastName: Client's last name (string)
        :param cnp: Client's CNP (int)
        """
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.cnp = cnp

    def __str__(self):
        return (f"Client:\n"
                f"  ID: {self.ID}\n"
                f"  First Name: {self.firstName}\n"
                f"  Last Name: {self.lastName}\n"
                f"  CNP: {self.cnp}")


    def getID(self):
        """
        :return: Client ID (int)
        """
        return self.ID

    def getFirstName(self):
        """
        :return: Client's first name (string)
        """
        return self.firstName

    def getLastName(self):
        """
        :return: Client's last name (string)
        """
        return self.lastName

    def getCNP(self):
        """
        :return: Client's CNP (int)
        """
        return self.cnp

    def setFirstName(self, firstName):
        """
        Sets the client's first name.
        :param firstName: Client's first name (string)
        """
        self.firstName = firstName

    def setLastName(self, lastName):
        """
        Sets the clients last name.
        :param lastName: Client's last name (string)
        """
        self.lastName = lastName

    def setCNP(self, cnp):
        """
        Sets the Client's CNP (int)
        :param cnp: client's CNP (int)
        """
        self.cnp = cnp

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