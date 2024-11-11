from domain import Client

class ServiceClient:

    def __init__(self, repoClient, validatorClient):
        self.repoClient = repoClient
        self.validatorClient = validatorClient

    def addClientService(self, ID, firstName, lastName, cnp):
        client = Client.Client(ID, firstName, lastName, cnp)
        self.validatorClient.validateClient(client)
        self.repoClient.addClient(client)

    