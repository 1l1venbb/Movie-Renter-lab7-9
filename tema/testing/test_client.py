from domain.Client import Client, ClientValidator

class TestClient:
    @staticmethod
    def test_getID():
        """
        Test function for getID()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890123')
        assert client.getID() == 1

    @staticmethod
    def test_getFirstName():
        """
        Test function for getFirstName()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890')
        assert client.getFirstName() == "Ion"

    @staticmethod
    def test_getLastName():
        """
        Test function for getLastName()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890')
        assert client.getLastName() == "Popescu"

    @staticmethod
    def test_getCNP():
        """
        Test function for getCNP()
        """
        client = Client(1, "Ion" , "Popescu", '1234567890')
        assert client.getCNP() == "1234567890"