import unittest
from domain.Client import Client, ClientValidator
from repository.clientList import ClientList
from service.serviceClient import ServiceClient


class TestClient(unittest.TestCase):

    def test_getID(self):
        """
        Test function for getID()
        """
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        self.assertEqual(client.getID(), 1)

    def test_getFirstName(self):
        """
        Test function for getFirstName()
        """
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        self.assertEqual(client.getFirstName(), "Ion")

    def test_getLastName(self):
        """
        Test function for getLastName()
        """
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        self.assertEqual(client.getLastName(), "Popescu")

    def test_getCNP(self):
        """
        Test function for getCNP()
        """
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        self.assertEqual(client.getCNP(), "1234567890")

    def test_getCopiesRented(self):
        """
        Test function for getCopiesRented()
        """
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        self.assertEqual(client.getCopiesRented(), 0)

    def test_rented(self):
        """
        Test function for rented()
        """
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        client.rented()
        self.assertEqual(client.getCopiesRented(), 1)

    def test_returned(self):
        """
        Test function for returned()
        """
        client = Client(1, "Ion", "Popescu", '1234567890', 1, False)
        client.returned()
        self.assertEqual(client.getCopiesRented(), 0)

    def test_setFirstName(self):
        """
        Test function for setFirstName()
        """
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        client.setFirstName("Iulian")
        self.assertEqual(client.getFirstName(), "Iulian")

    def test_setLastName(self):
        """
        Test function for setLastName()
        """
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        client.setLastName("Pop")
        self.assertEqual(client.getLastName(), "Pop")

    def test_setCNP(self):
        """
        Test function for setCNP()
        """
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        client.setCNP('1234567890123')
        self.assertEqual(client.getCNP(), '1234567890123')


class TestClientValidator(unittest.TestCase):

    def test_validateClient(self):
        """
        Test function for validateClient()
        """
        validator = ClientValidator()

        # Valid client
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        try:
            validator.validateClient(client)
            result = True
        except ValueError:
            result = False
        self.assertTrue(result)

        # Invalid clients
        invalid_clients = [
            Client(1, "Ion", "Popescu", '123456789012', 0, False),
            Client(1, "Ion", "Popescu", '123456789012a', 0, False),
            Client(1, "Ion", "Popescu", '', 0, False),
            Client(1, " ", "Popescu", '1234567890123', 0, False)
        ]

        for client in invalid_clients:
            with self.assertRaises(ValueError):
                validator.validateClient(client)


class TestRepoClient(unittest.TestCase):

    def test_len(self):
        """
        Test function for len()
        """
        lst = ClientList()

        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        self.assertEqual(len(lst), 1)
        client = Client(2, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        self.assertEqual(len(lst), 2)

    def test_isEmpty(self):
        """
        Test function for isEmpty()
        """
        lst = ClientList()
        self.assertTrue(lst.isEmpty())

        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        self.assertFalse(lst.isEmpty())

    def test_getClient(self):
        """
        Test function for getClient()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        self.assertEqual(lst.getClient(1), client)

    def test_addClient(self):
        """
        Test function for addClient()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        lst.addClient(client)
        self.assertEqual(lst.getAll(), [client])
        result = True
        try:
            lst.addClient(client)
            result = False
        except ValueError:
            self.assertTrue(result)

    def test_deleteClient(self):
        """
        Test function for deleteClient()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        lst.addClient(client)
        lst.deleteClient(1)
        self.assertTrue(lst.isEmpty())


        result = True
        try:
            lst.deleteClient(1)
            result = False
        except ValueError:
            self.assertTrue(result)

    def test_getAll(self):
        """
        Test function for getAll()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        lst.addClient(client)
        client1 = Client(2, "Ion", "Popescu", '1234567890', 0, False)
        lst.addClient(client1)
        self.assertEqual(lst.getAll(), [client, client1])

    def test_modifyClient(self):
        """
        Test function for modifyClient()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890', 0, False)
        lst.addClient(client)
        client1 = Client(1, "Ion", "Pope", '1234567890123', 0, False)
        lst.modifyClient(client1)
        self.assertEqual(client.getCNP(), client1.getCNP())
        self.assertEqual(client.getLastName(), client1.getLastName())

    def test_isIDUnique(self):
        """
        Test function for isIDUnique()
        """
        result = True
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)

        try:
            lst.isIDUnique(1)
            result = False
        except ValueError:
            self.assertTrue(result)

        try:
            lst.isIDUnique(2)
            result = True
        except ValueError:
            result = False
        self.assertTrue(result)

    def test_isCNPUnique(self):
        """
        Test function for isCNPUnique()
        """
        result = True
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        try:
            lst.isCNPUnique("1234567890123")
            result = False
        except ValueError:
            self.assertTrue(result)

        try:
            lst.isCNPUnique("1231231230123")
            result = True
        except ValueError:
            result = False
        self.assertTrue(result)


class TestClientService(unittest.TestCase):

    def test_addClientService(self):
        """
        Test function for addClientService()
        """
        clientValidator = ClientValidator()
        clientRepo = ClientList()
        service = ServiceClient(clientRepo, clientValidator)

        service.addClientService(1, "Ion", "Popescu", '1234567890123')
        client = clientRepo.getClient(1)
        self.assertEqual(clientRepo.getAll(), [client])

    def test_getAllClientService(self):
        """
        Test function for getAllClientService()
        """
        clientValidator = ClientValidator()
        clientRepo = ClientList()
        service = ServiceClient(clientRepo, clientValidator)
        client = Client(1, "Ion", "Popescu", '1234567890321', 0, False)
        client1 = Client(2, "Ion", "Popescu", '1234567890123', 0, False)

        service.addClientService(1, "Ion", "Popescu", '1234567890321')
        service.addClientService(2, "Ion", "Popescu", '1234567890123')

        self.assertEqual(service.getAllClientsService(), [client, client1])

    def test_deleteClientService(self):
        """
        Test function for deleteClientService()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        service = ServiceClient(lst, ClientValidator())
        result = True

        try:
            service.deleteClientService(2)
            result = False
        except ValueError:
            self.assertTrue(result)

        service.deleteClientService(1)
        self.assertTrue(lst.isEmpty())

    def test_getClientService(self):
        """
        Test function for getClientService()
        :return:
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        service = ServiceClient(lst, ClientValidator())

        self.assertIsNone(service.getClientService(2))
        self.assertEqual(service.getClientService(1), client)

    def test_modifyClientService(self):
        """
        Test function for modifyClientService()
        """

        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        service = ServiceClient(lst, ClientValidator())
        result = True

        try:
            service.modifyClientService(1, "Nea", "Caisa", "2131231230123")
        except ValueError:
            result = False
        self.assertTrue(result)

        try:
            service.modifyClientService(1, "", "Caisa", "2131231230123")
        except ValueError:
            result = False
        self.assertTrue(result)

        try:
            service.modifyClientService(1, "Nea", "", "2131231230123")
        except ValueError:
            result = False
        self.assertTrue(result)

        try:
            service.modifyClientService(1, "Nea", "Caisa", "")
        except ValueError:
            result = False
        self.assertTrue(result)

    def test_searchClientByFirstName(self):
        """
        Test function for searchClientByFirstName()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        service = ServiceClient(lst, ClientValidator())
        result = True
        self.assertEqual(service.searchClientByFirstName("Ion"), [client])
        try:
            service.searchClientByFirstName("Nea")
            result = False
        except ValueError:
            self.assertTrue(result)

    def test_searchClientByLastName(self):
        """
        Test function for searchClientByLastName()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        service = ServiceClient(lst, ClientValidator())
        result = True
        self.assertEqual(service.searchClientByLastName("Popescu"), [client])
        try:
            service.searchClientByLastName("Nea")
            result = False
        except ValueError:
            self.assertTrue(result)

    def test_searchClientByCNP(self):
        """
        Test function for searchClientByCNP()
        """
        lst = ClientList()
        client = Client(1, "Ion", "Popescu", '1234567890123', 0, False)
        lst.addClient(client)
        service = ServiceClient(lst, ClientValidator())
        result = True
        self.assertEqual(service.searchClientByCNP("1234567890123"), client)
        try:
            service.searchClientByCNP("1231231230123")
            result = False
        except ValueError:
            self.assertTrue(result)

    def test_generateClientService(self):
        """
        Test function for generateClientService()
        """
        lst = ClientList()
        service = ServiceClient(lst, ClientValidator())

        service.generateClientService()
        self.assertEqual(len(lst.getAll()), 1)
        self.assertTrue(isinstance(lst.getAll()[0], Client))

    def test_sortRentingClientsService(self):
        """
        Test function for sortRentingClientsService()
        """
        lst = ClientList()
        client1 = Client(1, "Don", "Popescu", '1234567890123', 0, False)
        lst.addClient(client1)
        client2 = Client(2, "Nea", "Popescu", '1234567890124', 3, False)
        lst.addClient(client2)
        client3 = Client(3, "Ion", "Caisa", '1234567890125', 2, False)
        lst.addClient(client3)
        client4 = Client(4, "Caisa", "Popescu", '1234567890153', 6, False)
        lst.addClient(client4)
        client5 = Client(5, "Jon", "Nea", '1234567890128', 23, False)
        lst.addClient(client5)
        service = ServiceClient(lst, ClientValidator())

        lst = service.sortRentingClientsService()
        self.assertEqual(lst, [client4, client3, client5, client2])


    def test_sortClientsByRentsService(self):
        """
        Test function for sortClientsByRentsService()
        """
        lst = ClientList()
        client1 = Client(1, "Don", "Popescu", '1234567890123', 0, False)
        lst.addClient(client1)
        client2 = Client(2, "Nea", "Popescu", '1234567890124', 3, False)
        lst.addClient(client2)
        client3 = Client(3, "Ion", "Caisa", '1234567890125', 2, False)
        lst.addClient(client3)
        client4 = Client(4, "Caisa", "Popescu", '1234567890153', 6, False)
        lst.addClient(client4)
        client5 = Client(5, "Jon", "Nea", '1234567890128', 23, False)
        lst.addClient(client5)
        service = ServiceClient(lst, ClientValidator())

        lst = service.sortClientsByRentsService()

        self.assertEqual(lst, [client5, client4, client2, client3, client1])

    def test_top30pClientsService(self):
        """
        Test function for top30pClientsService()
        """
        lst = ClientList()
        client1 = Client(1, "Don", "Popescu", '1234567890123', 0, False)
        lst.addClient(client1)
        client2 = Client(2, "Nea", "Popescu", '1234567890124', 3, False)
        lst.addClient(client2)
        client3 = Client(3, "Ion", "Caisa", '1234567890125', 2, False)
        lst.addClient(client3)
        client4 = Client(4, "Caisa", "Popescu", '1234567890153', 6, False)
        lst.addClient(client4)
        client5 = Client(5, "Jon", "Nea", '1234567890128', 23, False)
        lst.addClient(client5)
        service = ServiceClient(lst, ClientValidator())

        lst = service.top30pClientsService()
        self.assertEqual(lst, [client5])

if __name__ == '__main__':
    unittest.main()
