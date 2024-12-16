from domain import Client
from utils.randomClient import RandomClient
from utils.Sorts import Sorts as Sorts

class ServiceClient:

    def __init__(self, repoClient, validatorClient):
        """
        Constructor for ServiceClient
        :param repoClient: Object of type ClientRepository
        :param validatorClient: Object of type ClientValidator
        """
        self.repoClient = repoClient
        self.validatorClient = validatorClient

    def addClientService(self, ID, firstName, lastName, cnp):
        """
        Service for adding a client
        :param ID: new ID (int)
        :param firstName: First name of the client (str)
        :param lastName: Last name of the client (str)
        :param cnp: CNP of the client (str len()=13)
        """
        client = Client.Client(ID, firstName, lastName, cnp, 0, False)
        self.validatorClient.validateClient(client)
        self.repoClient.addClient(client)

    def getAllClientsService(self):
        """
        Service for getting all clients
        """
        return self.repoClient.getAll()

    def deleteClientService(self, ID):
        """
        Service for deleting a client
        :param ID: ID of the client to be deleted (int)
        """
        self.repoClient.deleteClient(ID)

    def getClientService(self, ID):
        """"
        Service for getting a client
        :param ID: ID of the client to be returned (int)
        :return: Client object
        """
        return self.repoClient.getClient(ID)

    def modifyClientService(self, ID, firstName, lastName, cnp):
        """
        Service for modifying a client
        :param ID: ID (int)
        :param firstName: New first name(str)
        :param lastName: New last name(str)
        :param cnp: New cnp(int)
        """
        client = Client.Client(ID, firstName, lastName, cnp, 0, False)
        if client is not None:
            if firstName != "":
                client.setFirstName(firstName)
            else:
                client.setFirstName(self.repoClient.getClient(ID).getFirstName())

            if lastName != "":
                client.setLastName(lastName)
            else:
                client.setLastName(self.repoClient.getClient(ID).getLastName())
            if cnp != "":
                client.setCNP(cnp)
            else:
                client.setCNP(self.repoClient.getClient(ID).getCNP())
            self.validatorClient.validateClient(client)
            self.repoClient.modifyClient(client)

    def searchClientByFirstName(self, firstName):
        """
        Searches clients by their first name
        :param firstName: First name to search for
        :return: list of all clients with the first name firstName
        :raises: ValueError if no client with the given first name exists
        """
        lst = [client for client in self.repoClient.getAll() if client.getFirstName() == firstName]
        if len(lst) == 0:
            raise ValueError
        else:
            return lst

    def searchClientByLastName(self, lastName):
        """
        Searches clients by their last name
        :param lastName: Last name to search for
        :return: list of all clients with the last name lastName
        :raises: ValueError if no client with the given last name exists
        """
        lst = [client for client in self.repoClient.getAll() if client.getLastName() == lastName]
        if len(lst) == 0:
            raise ValueError
        else:
            return lst

    def searchClientByCNP(self, cnp):
        """
        Searches a client by their CNP
        :param cnp: CNP t osearch for
        :return: Client if found or None
        """
        for client in self.repoClient.getAll():
            if client.getCNP() == cnp:
                return client

        return None

    def generateClientService(self):
        """
        Generates a random client and adds it to the repository
        :return:
        """
        randomClient = RandomClient()

        ID = 0
        cnp = ""

        while True:
            try:
                ID = randomClient.generateRandomID()
                self.repoClient.isIDUnique(ID)
                break
            except ValueError:
                continue
        while True:
            try:
                cnp = randomClient.generateRandomCNP()
                self.repoClient.isCNPUnique(cnp)
                break
            except ValueError:
                continue

        r = randomClient.generateRandomClient(ID, cnp)
        self.addClientService(r["id"], r["firstName"], r["lastName"], r["cnp"])

    def sortRentingClientsService(self):
        """
        Service for sorting clients by first name that are currently renting movies
        :return: list
        """

        lst = []
        for client in self.repoClient.getAll():
            if client.getCopiesRented() > 0:
                lst.append(client)

        sort = Sorts()

        #lst.sort(key=lambda x: x.getFirstName(), reverse=False)
        sort.insertionSort(lst, key = lambda x: x.getFirstName())

        return lst

    def sortClientsByRentsService(self):
        """
        Service for sorting clients by number of current rents
        """
        lst = []
        for client in self.repoClient.getAll():
            lst.append(client)
        sort = Sorts()
        #lst.sort(key=lambda x: x.getCopiesRented(), reverse=True)
        sort.combSort(lst, key = lambda x: x.getCopiesRented(), reverse = True)
        return lst

    def top30pClientsService(self):
        """
        Service for calculating top 30% clients
        """

        lst = []
        for client in self.repoClient.getAll():
            lst.append(client)

        #lst.sort(key=lambda x: x.getCopiesRented(), reverse=True)
        sort = Sorts()
        sort.combSort(lst, key = lambda x: x.getCopiesRented(), reverse = True)
        length = int(len(lst) * 0.3)

        return lst[:length]
