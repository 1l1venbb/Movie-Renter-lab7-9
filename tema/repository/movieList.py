class MovieList:
    def __init__(self):
        self.movies = []

    def isEmpty(self):
        """
        Checks if the list is empty
        :return: True if list is empty (bool)
        """
        if len(self.movies) == 0:
            return True
        return False

    def getNewID(self):
        """
        Generates a new client ID.
        :return: The new client ID (int)
        """
        if self.isEmpty():
            return 0
        return self.movies[-1].id + 1

    def addMovie(self, client):
        """
        Adds a client to the list of clients
        :param client: Client object
        """
        client.setID(self.getNewID())
        self.movies.append(client)

    def removeClient(self, clientToDelete):
        """
        Removes a client from the list of clients
        :param clientToDelete: Client object that will be deleted
        :raises: Exception if the client does not exist
        """
        deleted = False

        for client in self.movies:
            if client.getID() == clientToDelete.getID():
                self.movies.pop(client)
                deleted = True

        if not deleted:
            raise Exception("Movie does not exist")

    def getAll(self):
        """
        Returns all movies in the list
        :return: list
        """

        return [x for x in self.movies]