import unittest
from domain.Rent import RentValidator, Rent
from domain.Client import Client
from domain.Movie import Movie


class TestRent(unittest.TestCase):

    def test_getID(self):
        """
        Test function for getID()
        """
        rent = Rent(2, 1, 1, 12, 10, 2024, 0, 0, 0, False)
        self.assertEqual(rent.getID(), 2)

    def test_getClientID(self):
        """
        Test function for getClientID()
        """
        rent = Rent(1, 2, 1, 12, 10, 2024, 0, 0, 0, False)
        self.assertEqual(rent.getClientID(), 2)

    def test_getMovieID(self):
        """
        Test function for getMovieID()
        """
        rent = Rent(1, 1, 2, 12, 10, 2024, 0, 0, 0, False)
        self.assertEqual(rent.getMovieID(), 2)

    def test_getRentDate(self):
        """
        Test function for getRentDate()
        """
        rent = Rent(1, 1, 1, 12, 10, 2024, 0, 0, 0, False)
        self.assertEqual(rent.getRentDay(), 12)
        self.assertEqual(rent.getRentMonth(), 10)
        self.assertEqual(rent.getRentYear(), 2024)

    def test_getReturnDate(self):
        """
        Test function for getReturnDate()
        """
        rent = Rent(1, 1, 1, 12, 10, 2024, 0, 0, 0, False)
        rent.setReturnDate(13, 11, 2024)
        self.assertEqual(rent.getReturnDay(), 13)
        self.assertEqual(rent.getReturnMonth(), 11)
        self.assertEqual(rent.getReturnYear(), 2024)

    def test_setID(self):
        """
        Test function for setID()
        """
        rent = Rent(2, 1, 1, 12, 10, 2024, 0, 0, 0, False)
        rent.setID(3)
        self.assertEqual(rent.getID(), 3)

    def test_setClientID(self):
        """
        Test function for setClientID()
        """

        rent = Rent(1, 2, 1, 12, 10, 2024, 0, 0, 0, False)
        rent.setClientID(3)
        self.assertEqual(rent.getClientID(), 3)

    def test_setMovieID(self):
        """
        Test function for setMovieID()
        """
        rent = Rent(1, 1, 2, 12, 10, 2024, 0, 0, 0, False)
        rent.setMovieID(3)
        self.assertEqual(rent.getMovieID(), 3)

    def test_setRentDate(self):
        """
        Test function for setRentDate()
        """
        rent = Rent(1, 1, 1, 12, 10, 2024, 0, 0, 0, False)
        rent.setRentDate(13, 11, 2024)
        self.assertEqual(rent.getRentDay(), 13)
        self.assertEqual(rent.getRentMonth(), 11)
        self.assertEqual(rent.getRentYear(), 2024)

    def test_setReturnDate(self):
        """
        Test function for setReturnDate()
        """
        rent = Rent(2, 1, 1, 12, 10, 2024, 0, 0, 0, False)
        rent.setReturnDate(13, 11, 2024)
        self.assertEqual(rent.getReturnDay(), 13)
        self.assertEqual(rent.getReturnMonth(), 11)
        self.assertEqual(rent.getReturnYear(), 2024)


class TestRentValidator(unittest.TestCase):

    def test_validateRent(self):
        """
        Test function for validateRent()
        """
        client = Client(1, "Ion", "Popescu", 1231231230321, 0, False)
        movie = Movie(1, "Mos Craciun", "Xmas Movie", "Adventure", 1997, 0, False)
        rent = Rent(2, 1, 1, 12, 10, 2024, 0, 0, 0, False)
        clients = [client]
        movies = [movie]

        validator = RentValidator()
        try:
            validator.validateRent(rent, clients, movies)
            result = True
        except ValueError:
            result = False
        self.assertTrue(result)

        rent.setClientID(2)
        try:
            validator.validateRent(rent, clients, movies)
            result = False
        except ValueError:
            self.assertTrue(result)

        rent.setClientID(1)
        rent.setMovieID(2)

        try:
            validator.validateRent(rent, clients, movies)
            result = False
        except ValueError:
            self.assertTrue(result)

        rent = Rent(1, 1, 1, 12, 10, 2023, 0, 0, 0, False)
        try:
            validator.validateRent(rent, clients, movies)
            result = False
        except ValueError:
            self.assertTrue(result)


        rent = Rent(1, 1, 1, 12, 13, 2024, 0, 0, 0, False)
        try:
            validator.validateRent(rent, clients, movies)
            result = False
        except ValueError:
            self.assertTrue(result)


        rent = Rent(1, 1, 1, 32, 10, 2023, 0, 0, 0, False)
        try:
            validator.validateRent(rent, clients, movies)
            result = False
        except ValueError:
            self.assertTrue(result)

    def test_validateReturnDate(self):
        """
        Test function for validateReturnDate()
        """
        rent = Rent(2, 1, 1, 12, 10, 2024, 0, 0, 0, False)
        validator = RentValidator()

        try:
            validator.validateReturnDate(13, 11, 2024, rent)
            result = True
        except ValueError:
            result = False
        self.assertTrue(result)

        try:
            validator.validateReturnDate(12, 11, 2026, rent)
            result = False
        except ValueError:
            result = True
        self.assertTrue(result)

        rent.setReturnDate(13, 11, 2024)
        try:
            validator.validateReturnDate(rent.getReturnDay(), rent.getReturnMonth(), rent.getReturnYear(), rent)
            result = True
        except ValueError:
            result = False
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
