from domain import Client

class ServiceClient:

    def __init__(self, repoClient, validatorClient):
        self.repoClient = repoClient
        self.validatorClient = validatorClient

    def addClientService(self, ID, firstName, lastName, cnp):
        client = Client.Client(ID, firstName, lastName, cnp)
        self.validatorClient.validateClient(client)
        self.repoClient.addClient(client)

    def getAllClientsService(self):
        return self.repoClient.getAll()

    def deleteClientService(self, ID):
        self.repoClient.deleteClient(ID)

    def getClientService(self, ID):
        return self.repoClient.getClient(ID)

    def modifyClientService(self, ID, firstName, lastName, cnp):
        client = Client.Client(ID, firstName, lastName, cnp)
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