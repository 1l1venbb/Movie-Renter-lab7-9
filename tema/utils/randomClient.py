import random

first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Anne"]
last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis", "Clark"]

class RandomClient:

    def __init__(self):
        self.first_names = first_names
        self.last_names = last_names

    def generateRandomID(self):
        """
        Generates a random ID.
        :return: ID (int)
        """
        ID = random.randint(0, 1000000)
        return ID

    def generateRandomCNP(self):
        """
        Generates a random CNP.
        :return: CNP (str)
        """
        cnp = random.randint(1000000000000, 9999999999999)
        return str(cnp)

    def generateRandomClient(self, ID, CNP):
        """
        Generates a random client.
        :param ID: random valid ID
        :param CNP: random valid CNP
        :return: dictionary with client data
        """
        firstName = random.choice(self.first_names)
        lastName = random.choice(self.last_names)

        client = {
            "id": ID,
            "firstName": firstName,
            "lastName": lastName,
            "cnp": CNP
        }

        return client
