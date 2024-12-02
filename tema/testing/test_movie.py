from domain.Movie import Movie, MovieValidator
from repository.movieList import MovieList

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
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        assert movie.getID() == 1

    def test_getTitle(self):
        """
        Test function for getTitle()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        assert movie.getTitle() == "The Horse in Motion"

    def test_getDescription(self):
        """
        Test function for getDescription()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        assert movie.getDescription() == "First movie ever"

    def test_getGenre(self):
        """
        Test function for getGenre()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        assert movie.getGenre() == "Action"

    def test_getReleaseYear(self):
        """
        Test function for getReleaseYear()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        assert movie.getReleaseYear() == 1878

    def test_setID(self):
        """
        Test function for setID()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        movie.setID(2)
        assert movie.getID() == 2

    def test_setTitle(self):
        """
        Test function for setTitle()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        movie.setTitle("The Horse in Motion 2")
        assert movie.getTitle() == "The Horse in Motion 2"

    def test_setDescription(self):
        """
        Test function for setDescription()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        movie.setDescription("Second movie ever")
        assert movie.getDescription() == "Second movie ever"

    def test_setGenre(self):
        """
        Test function for setGenre()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        movie.setGenre("Comedy")
        assert movie.getGenre() == "Comedy"

    def test_setReleaseYear(self):
        """
        Test function for setReleaseYear()
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        movie.setReleaseYear(1900)
        assert movie.getReleaseYear() == 1900

    def test_RentFunctions(self):
        """
        Test function for Renting functions
        """
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)

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
        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        validator = MovieValidator()
        try:
            validator.validateMovie(movie)
            assert True
        except ValueError:
            assert False

        movie = Movie(1 , "  ", "First movie ever", "Action", 1878, 0)
        try:
            validator.validateMovie(movie)
            assert False
        except ValueError:
            assert True

        movie = Movie(1 , "The Horse in Motion", "  ", "Action", 1878, 0)
        try:
            validator.validateMovie(movie)
            assert False
        except ValueError:
            assert True

        movie = Movie(1 , "The Horse in Motion", "First movie ever", "  ", 1878, 0)
        try:
            validator.validateMovie(movie)
            assert False
        except ValueError:
            assert True

        movie = Movie(1 , "The Horse in Motion" , "First movie ever", "Action", 1877, 0)
        try:
            validator.validateMovie(movie)
            assert False
        except ValueError:
            assert True

class TestRepoMovie:

    def run_all_tests(self):
        """
        Runs all tests for RepoMovie
        """
        self.test_isEmpty()
        self.test_getMovie()
        self.test_addMovie()
        self.test_deleteMovie()
        self.test_getAll()
        self.test_modifyMovie()

    def test_isEmpty(self):
        """
        Test function for isEmpty()
        """
        lst = MovieList()
        assert lst.isEmpty() == True

        movie = Movie(1 , "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        lst.addMovie(movie)
        assert lst.isEmpty() == False

    def test_getMovie(self):
        """
        Test function for getMovie()
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        lst.addMovie(movie)
        assert lst.getMovie(1) == movie

    def test_addMovie(self):
        """
        Test function for addMovie()
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        lst.addMovie(movie)
        assert lst.getAll() == [movie]


    def test_deleteMovie(self):
        """
        Test function for deleteMovie()
        :return:
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        lst.addMovie(movie)
        assert lst.isEmpty() == False
        lst.deleteMovie(1)
        assert lst.isEmpty() == True

    def test_getAll(self):
        """
        Test function for getAll()
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        lst.addMovie(movie)
        movie1 = Movie(2, "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        lst.addMovie(movie1)
        assert lst.getAll() == [movie, movie1]

    def test_modifyMovie(self):
        """
        Test function for modifyMovie()
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0)
        lst.addMovie(movie)
        movie1 = Movie(1, "The Horse in the House", "First movie ever", "Action", 18, 0)
        lst.modifyMovie(movie1)
        movie = lst.getMovie(1)
        assert movie.getTitle() == movie1.getTitle()
        assert movie.getReleaseYear() == movie1.getReleaseYear()