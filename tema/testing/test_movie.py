from domain.Movie import Movie, MovieValidator

class TestMovie:

    def run_all_tests(self):
        """
        Runs all test for Movie
        """
        self.test_getID()
        self.test_getTitle()
        self.test_getDescription()
        self.test_getGenre()
        self.test_getReleaseYear()
        self.test_setID()
        self.test_setTitle()
        self.test_setDescription()
        self.test_setGenre()
        self.test_setReleaseYear()
        self.test_RentFunctions()

    def test_getID(self):
        """
        Test function for getID()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)
        assert movie.getID() == 1

    def test_getTitle(self):
        """
        Test function for getTitle()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)
        assert movie.getTitle() == "The Horse in Motion"

    def test_getDescription(self):
        """
        Test function for getDescription()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)
        assert movie.getDescription() == "First movie ever"

    def test_getGenre(self):
        """
        Test function for getGenre()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)
        assert movie.getGenre() == "Action"

    def test_getReleaseYear(self):
        """
        Test function for getReleaseYear()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)
        assert movie.getReleaseYear() == 1878

    def test_setID(self):
        """
        Test function for setID()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)
        movie.setID(2)
        assert movie.getID() == 2

    def test_setTitle(self):
        """
        Test function for setTitle()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)
        movie.setTitle("The Horse in Motion 2")
        assert movie.getTitle() == "The Horse in Motion 2"

    def test_setDescription(self):
        """
        Test function for setDescription()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)
        movie.setDescription("Second movie ever")
        assert movie.getDescription() == "Second movie ever"

    def test_setGenre(self):
        """
        Test function for setGenre()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)
        movie.setGenre("Comedy")
        assert movie.getGenre() == "Comedy"

    def test_setReleaseYear(self):
        """
        Test function for setReleaseYear()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)
        movie.setReleaseYear(1900)
        assert movie.getReleaseYear() == 1900

    def test_RentFunctions(self):
        """
        Test function for Renting functions
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)

        movie.wasRented()
        movie.wasRented()
        assert movie.getCopiesRented() == 2

        movie.wasReturned()
        assert movie.getCopiesRented() == 1

class TestMovieValidator:

    def run_all_tests(self):
        """
        Runs all test for MovieValidator
        """
        self.test_validateMovie()

    def test_validateMovie(self):
        """
        Test function for validateMovie()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878)
        try:
            MovieValidator.validateMovie(movie)
            assert True
        except ValueError:
            assert False

        movie = Movie(1 , "  ", "First movie ever", "Action", 1878)
        try:
            MovieValidator.validateMovie(movie)
            assert False
        except ValueError:
            assert True

        movie = Movie(1 , "The Horse in Motion", "  ", "Action", 1878)
        try:
            MovieValidator.validateMovie(movie)
            assert False
        except ValueError:
            assert True

        movie = Movie(1 , "The Horse in Motion", "First movie ever", "  ", 1878)
        try:
            MovieValidator.validateMovie(movie)
            assert False
        except ValueError:
            assert True

        movie = Movie(1 , "The Horse in Motion" , "First movie ever", "Action", 1877)
        try:
            MovieValidator.validateMovie(movie)
            assert False
        except ValueError:
            assert True