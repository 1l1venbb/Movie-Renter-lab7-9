from domain.Client import Client

class ClientList:
    def __init__(self):
        """
        Constructs a list of clients
        """
        self.clients = []

    def isEmpty(self):
        """
        Checks if the list is empty
        :return: True if list is empty (bool)
        """
        if len(self.clients) == 0:
            return True
        return False

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
        client.setID(self.getNewID())
        self.clients.append(client)

    def removeClient(self, clientToDelete):
        """
        Removes a client from the list of clients
        :param clientToDelete: Client object that will be deleted
        :raises: Exception if the client does not exist
        """
        deleted = False

        for client in self.clients:
            if client.getID() == clientToDelete.getID():
                self.clients.pop(client)
                deleted = True

        if not deleted:
            raise Exception()