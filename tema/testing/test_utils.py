import unittest
from utils.randomClient import RandomClient
from domain import Client, Movie, Rent


class TestRandomClient(unittest.TestCase):

    def test_generateRandomID(self):
        """
        Test function for generateRandomID()
        """
        random_client = RandomClient()
        generated_id = random_client.generateRandomID()
        self.assertGreaterEqual(len(str(generated_id)), 1)
        self.assertLessEqual(len(str(generated_id)), 7)

    def test_generateRandomCNP(self):
        """
        Test function for generateRandomCNP()
        """
        random_client = RandomClient()
        generated_cnp = random_client.generateRandomCNP()
        self.assertEqual(len(generated_cnp), 13)

        try:
            int(generated_cnp)
            is_integer = True
        except ValueError:
            is_integer = False

        self.assertTrue(is_integer)

    def test_isErased(self):
        """
        Test function for isErased()
        """
        client = Client.Client(1, "Ion", "Popescu", "1231231230123", 0, False)
        self.assertFalse(client.isErased())
        client.delete()
        self.assertTrue(client.isErased())

        movie = Movie.Movie(1, "The Horse", "idk", "action", 1997, 0, False)
        self.assertFalse(movie.isErased())
        movie.delete()
        self.assertTrue(movie.isErased())

        rent = Rent.Rent(1, 2, 3, 10, 11, 2024, 0, 0, 0, False)
        self.assertFalse(rent.isErased())
        rent.delete()
        self.assertTrue(rent.isErased())

if __name__ == '__main__':
    unittest.main()
