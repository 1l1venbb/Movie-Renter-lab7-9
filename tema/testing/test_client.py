from domain.Client import Client, ClientValidator


class TestClient:


    def run_all_tests(self):
        """
        Runs all test for Client
        """
        self.test_getID()
        self.test_getFirstName()
        self.test_getLastName()
        self.test_getCNP()
        self.test_setID()
        self.test_setFirstName()
        self.test_setLastName()
        self.test_setCNP()

    def test_getID(self):
        """
        Test function for getID()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890123')
        assert client.getID() == 1

    def test_getFirstName(self):
        """
        Test function for getFirstName()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890')
        assert client.getFirstName() == "Ion"

    def test_getLastName(self):
        """
        Test function for getLastName()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890')
        assert client.getLastName() == "Popescu"

    def test_getCNP(self):
        """
        Test function for getCNP()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890')
        assert client.getCNP() == "1234567890"

    def test_setID(self):
        """
        Test function for setID()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890')
        client.setID(2)
        assert client.getID() == 2

    def test_setFirstName(self):
        """
        Test function for setFirstName()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890')
        client.setFirstName("Iulian")
        assert client.getFirstName() == "Iulian"

    def test_setLastName(self):
        """
        Test function for setLastName()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890')
        client.setLastName("Pop")
        assert client.getLastName() == "Pop"

    def test_setCNP(self):
        """
        Test function for setCNP()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890')
        client.setCNP('1234567890123')
        assert client.getCNP() == '1234567890123'

class TestClientValidator:

    def run_all_tests(self):
        """
        Runs all test for ClientValidator
        """
        self.test_validateClient()

    def test_validateClient(self):

        client = Client(1, "Ion" , "Popescu", '1234567890123')
        validator = ClientValidator()
        try:
            validator.validateClient(client)
            assert True
        except ValueError:
            assert False

        client = Client(1, "Ion" , "Popescu", '123456789012')
        try:
            validator.validateClient(client)
            assert False
        except ValueError:
            assert True

        client = Client(1, "Ion" , "Popescu", '123456789012a')
        try:
            validator.validateClient(client)
            assert False
        except ValueError:
            assert True

        client = Client(1, "Ion" , "Popescu", '')
        try:
            validator.validateClient(client)
            assert False
        except ValueError:
            assert True

        client = Client(1 , " ", "Popescu", '1234567890123')

        try:
            validator.validateClient(client)
            assert False
        except ValueError:
            assert True