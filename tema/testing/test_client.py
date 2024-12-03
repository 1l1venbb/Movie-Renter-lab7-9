from domain.Client import Client, ClientValidator
from repository.clientList import ClientList
from service.serviceClient import ServiceClient


class TestClient:


    def run_all_tests(self):
        """
        Runs all test for Client
        """
        self.test_getID()
        self.test_getFirstName()
        self.test_getLastName()
        self.test_getCNP()
        self.test_setFirstName()
        self.test_setLastName()
        self.test_setCNP()

    def test_getID(self):
        """
        Test function for getID()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890123', 0, False)
        assert client.getID() == 1

    def test_getFirstName(self):
        """
        Test function for getFirstName()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890', 0, False)
        assert client.getFirstName() == "Ion"

    def test_getLastName(self):
        """
        Test function for getLastName()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890', 0, False)
        assert client.getLastName() == "Popescu"

    def test_getCNP(self):
        """
        Test function for getCNP()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890', 0, False)
        assert client.getCNP() == "1234567890"

    def test_setFirstName(self):
        """
        Test function for setFirstName()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890', 0, False)
        client.setFirstName("Iulian")
        assert client.getFirstName() == "Iulian"

    def test_setLastName(self):
        """
        Test function for setLastName()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890', 0, False)
        client.setLastName("Pop")
        assert client.getLastName() == "Pop"

    def test_setCNP(self):
        """
        Test function for setCNP()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890', 0, False)
        client.setCNP('1234567890123')
        assert client.getCNP() == '1234567890123'

class TestClientValidator:

    def run_all_tests(self):
        """
        Runs all test for ClientValidator
        """
        self.test_validateClient()

    def test_validateClient(self):

        client = Client(1, "Ion" , "Popescu", '1234567890123', 0, False)
        validator = ClientValidator()
        try:
            validator.validateClient(client)
            assert True
        except ValueError:
            assert False

        client = Client(1, "Ion" , "Popescu", '123456789012', 0, False)
        try:
            validator.validateClient(client)
            assert False
        except ValueError:
            assert True

        client = Client(1, "Ion" , "Popescu", '123456789012a', 0, False)
        try:
            validator.validateClient(client)
            assert False
        except ValueError:
            assert True

        client = Client(1, "Ion" , "Popescu", '', 0, False)
        try:
            validator.validateClient(client)
            assert False
        except ValueError:
            assert True

        client = Client(1 , " ", "Popescu", '1234567890123', 0, False)

        try:
            validator.validateClient(client)
            assert False
        except ValueError:
            assert True

class TestRepoClient:

    def run_all_tests(self):
        """
        Runs all test for RepoClient
        """
        self.test_isEmpty()
        self.test_getClient()
        self.test_addClient()
        self.test_deleteClient()
        self.test_getAll()
        self.test_modifyClient()

    def test_isEmpty(self):
        """
        Test function for isEmpty()
        """
        lst = ClientList()
        assert lst.isEmpty() == True

        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        assert lst.isEmpty() == False

    def test_getClient(self):
        """
        Test function for getClient()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        assert lst.getClient(1) == client

    def test_addClient(self):
        """
        Test function for addClient()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        lst.addClient(client)
        assert lst.getAll() == [client]

    def test_deleteClient(self):
        """
        Test function for deleteClient()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        lst.addClient(client)
        lst.deleteClient(1)
        assert lst.isEmpty() == True

    def test_getAll(self):
        """
        Test function for getAll()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        lst.addClient(client)
        client1 = Client(2, "Ion", "Popescu", '1234567890', 0, False)
        lst.addClient(client1)
        assert lst.getAll() == [client, client1]

    def test_modifyClient(self):
        """
        Test function for modifyClient()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        lst.addClient(client)
        client1 = Client(1, "Ion", "Pope", '1234567890123', 0, False)
        lst.modifyClient(client1)
        assert client.getCNP() == client1.getCNP()
        assert client.getLastName() == client1.getLastName()

class TestClientService:

    def run_all_tests(self):
        """
        Runs all test for ClientService
        """
        self.test_addClientService()
        self.getAllClientService()

    def test_addClientService(self):
        """
        Test function for addClientService()
        """
        clientValidator = ClientValidator()
        clientRepo = ClientList()
        service = ServiceClient(clientRepo, clientValidator)

        service.addClientService(1, "Ion" , "Popescu" , '1234567890123')
        client = clientRepo.getClient(1)
        assert clientRepo.getAll() == [client]

    def getAllClientService(self):
        """
        Test function for getAllClientService()
        """
        clientValidator = ClientValidator()
        clientRepo = ClientList()
        service = ServiceClient(clientRepo, clientValidator)
        client = Client(1, "Ion" , "Popescu", '1234567890321', 0, False)
        client1 = Client(2, "Ion", "Popescu", '1234567890123', 0, False)

        service.addClientService(1, "Ion" , "Popescu", '1234567890321')
        service.addClientService(2, "Ion", "Popescu", '1234567890123')

        assert service.getAllClientsService() == [client, client1]