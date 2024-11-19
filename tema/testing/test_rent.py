from domain.Rent import RentValidator, Rent
from domain.Client import Client
from domain.Movie import Movie
class TestRent:

    def run_all_tests(self):
        """
        Runs all tests.
        """
        pass
        self.test_getID()
        self.test_getClientID()
        self.test_getMovieID()
        self.test_getRentDate()
        self.test_getReturnDate()
        self.test_setID()
        self.test_setClientID()
        self.test_setMovieID()
        self.test_setRentDate()
        self.test_setReturnDate()

    def test_getID(self):
        """
        Test function for getID()
        """
        rent = Rent(2, 1, 1, 12,10, 2024)
        assert rent.getID() == 2

    def test_getClientID(self):
        """
        Test function for getClientID()
        """
        rent = Rent(1, 2, 1, 12, 10, 2024)
        assert rent.getClientID() == 2

    def test_getMovieID(self):
        """
        Test function for getMovieID()
        """
        rent = Rent(1, 1, 2, 12, 10, 2024)
        assert rent.getMovieID() == 2

    def test_getRentDate(self):
        """
        Test function for getRentDate()
        """
        rent = Rent(1, 1, 1, 12, 10, 2024)
        assert rent.getRentDay() == 12
        assert rent.getRentMonth() == 10
        assert rent.getRentYear() == 2024

    def test_getReturnDate(self):
        """
        Test function for getReturnDate()
        """
        rent = Rent(1, 1, 1, 12, 10, 2024)
        rent.setReturnDate(13, 11, 2024)
        assert rent.getReturnDay() == 13
        assert rent.getReturnMonth() == 11
        assert rent.getReturnYear() == 2024

    def test_setID(self):
        """
        Test function for setID()
        """
        rent = Rent(2, 1, 1, 12, 10, 2024)
        rent.setID(3)
        assert rent.getID() == 3

    def test_setClientID(self):
        """
        Test function for setClientID()
        """

        rent = Rent(1, 2, 1, 12, 10, 2024)
        rent.setClientID(3)
        assert rent.getClientID() == 3

    def test_setMovieID(self):
        """
        Test function for setMovieID()
        """
        rent = Rent(1, 1, 2, 12, 10, 2024)
        rent.setMovieID(3)
        assert rent.getMovieID() == 3

    def test_setRentDate(self):
        """
        Test function for setRentDate()
        """
        rent = Rent(1, 1, 1, 12, 10, 2024)
        rent.setRentDate(13, 11, 2024)
        assert rent.getRentDay() == 13
        assert rent.getRentMonth() == 11
        assert rent.getRentYear() == 2024

    def test_setReturnDate(self):
        """
        Test function for setReturnDate()
        """
        rent = Rent(2, 1, 1, 12, 10, 2024)
        rent.setReturnDate(13, 11, 2024)
        assert rent.getReturnDay() == 13
        assert rent.getReturnMonth() == 11
        assert rent.getReturnYear() == 2024

class TestRentValidator:
    def run_all_tests(self):
        """
        Runs all tests
        """
        self.test_validateRent()

    def test_validateRent(self):
        """
        Test function for validateRent()
        """
        client = Client(1 , "Ion", "Popescu" , 1231231230321)
        movie = Movie(1 , "Mos Craciun", "Xmas Movie", "Adventure", 1997)
        rent = Rent(2, 1, 1, 12, 10, 2024)
        clients = []
        movies = []
        clients.append(client)
        movies.append(movie)

        validator = RentValidator()
        try:
            validator.validateRent(rent, clients, movies)
            assert True
        except ValueError:
            assert False

    def test_validateReturnDate(self):
        """
        Test function for validateReturnDate()
        """
        rent = Rent(2, 1, 1, 12, 10, 2024)
        validator = RentValidator()
        try:
            validator.validateReturnDate(13, 11, 2024, rent)
            assert True
        except ValueError:
            assert False

        try:
            validator.validateReturnDate(12, 11, 2026, rent)
            assert False
        except ValueError:
            assert True


        rent.setReturnDate(13, 11, 2024)
        try:
            validator.validateReturnDate(rent.getReturnDay(), rent.getReturnMonth(), rent.getReturnYear(), rent)
            assert True
        except ValueError:
            assert False