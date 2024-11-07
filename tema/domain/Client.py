class Client:

    ID: int = -1
    firstName: str = ""
    lastName: str = ""
    cnp: str = ""

    def __init__(self, ID, firstName, lastName, cnp):
        """
        Constructor for Client class
        :param ID: Unique client ID (int)
        :param firstName: Client's first name (string)
        :param lastName: Client's last name (string)
        :param cnp: Client's CNP (int)
        """
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.cnp = cnp

    def getClientID(self):
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

    def getCnp(self):
        """
        :return: Client's CNP (int)
        """
        return self.cnp

    def setID(self, ID):
        """
        :param ID: Unique client ID (int)
        """
        self.ID = ID

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

    def setCnp(self, cnp):
        """
        Sets the Client's CNP (int)
        :param cnp: client's CNP (int)
        """
        self.cnp = cnp


class ClientValidator:

    @staticmethod
    def validateClient(client):
        if client.getFirstName() == "":
            raise ValueError("First Name cannot be empty")

        if client.getLastName() == "":
            raise ValueError("Last Name cannot be empty")

        if len(client.getCnp()) != 13:
            raise ValueError("CNP cannot be empty")

        try:
            int(client.getCNP())
        except TypeError:
            raise ValueError("CNP is invalid")