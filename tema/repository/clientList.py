class ClientList:
    def __init__(self):
        """
        Constructs a list of clients
        """
        self.clients = []

    def __len__(self):
        """
        Returns the number of clients.
        """
        return len(self.clients)

    def isEmpty(self):
        """
        Checks if the list is empty
        :return: True if list is empty (bool)
        """
        if len(self.clients) == 0:
            return True
        return False

    def isIDUnique(self, ID):
        """
        Checks if ID is unique
        :param ID:ID to be checked
        :return: True if ID is unique (bool)
        :raises: ValueError if ID already exists
        """

        for client in self.clients:
            if client.getID() == ID:
                raise ValueError("ID already exists")
        return True

    def isCNPUnique(self, CNP):
        """
        Checks if CNP is unique
        :param CNP: CNP to be checked
        :return: True if CNP is unique (bool)
        :raises: ValueError if CNP already exists
        """
        for client in self.clients:
            if client.getCNP() == CNP:
                raise ValueError("CNP already exists")
        return True

    def getClient(self, ID):
        """"
        Returns a client with the given ID
        :param ID: ID of the client
        """
        for client in self.clients:
            if client.getID() == ID:
                return client
        return None

    def getNewID(self):
        """
        Generates a new client ID.
        :return: The new client ID (int)
        """

        if self.isEmpty():
            return 0
        return self.clients[-1].id + 1



    def addClient(self, client):
        """
        Adds a client to the list of clients
        :param client: Client object
        """
        if self.getClient(client.getID()) is not None:
            raise Exception("Client ID already exists")
        else:
            #client.setID(self.getNewID())
            self.clients.append(client)

    def deleteClient(self, ID):
        """
        Removes a client from the list of clients
        :param ID: ID of the client to delete
        :raises: Exception if the client does not exist
        """

        client = self.getClient(ID)
        if client is not None:
            self.clients.remove(client)

        else:
            raise Exception("Client does not exist")

    def getAll(self):
        """
        Returns all clients in the list
        :return: list
        """

        return [x for x in self.clients]

    def modifyClient(self, client):
        """
        Modifies a client in the list of clients
        :param client: Client object
        """
        actualClient = self.getClient(client.getID())
        actualClient.setFirstName(client.getFirstName())
        actualClient.setLastName(client.getLastName())
        actualClient.setCNP(client.getCNP())