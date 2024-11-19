import random

first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Anne"]
last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis", "Clark"]

class RandomClient:

    def __init__(self):
        self.first_names = first_names
        self.last_names = last_names

    def generateRandomID(self):
        ID = random.randint(0, 1000000)
        return ID

    def generateRandomCNP(self):
        cnp = random.randint(1000000000000, 9999999999999)
        return str(cnp)

    def generateRandomClient(self, ID, CNP):
        firstName = random.choice(self.first_names)
        lastName = random.choice(self.last_names)

        client = {
            "id": ID,
            "firstName": firstName,
            "lastName": lastName,
            "cnp": CNP
        }

        return client
