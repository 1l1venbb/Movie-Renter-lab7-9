import unittest
from domain.Movie import Movie, MovieValidator
from repository.movieList import MovieList


class TestMovie(unittest.TestCase):

    def test_getID(self):
        """
        Test function for getID()
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        self.assertEqual(movie.getID(), 1)

    def test_getTitle(self):
        """
        Test function for getTitle()
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        self.assertEqual(movie.getTitle(), "The Horse in Motion")

    def test_getDescription(self):
        """
        Test function for getDescription()
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        self.assertEqual(movie.getDescription(), "First movie ever")

    def test_getGenre(self):
        """
        Test function for getGenre()
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        self.assertEqual(movie.getGenre(), "Action")

    def test_getReleaseYear(self):
        """
        Test function for getReleaseYear()
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        self.assertEqual(movie.getReleaseYear(), 1878)

    def test_setID(self):
        """
        Test function for setID()
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        movie.setID(2)
        self.assertEqual(movie.getID(), 2)

    def test_setTitle(self):
        """
        Test function for setTitle()
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        movie.setTitle("The Horse in Motion 2")
        self.assertEqual(movie.getTitle(), "The Horse in Motion 2")

    def test_setDescription(self):
        """
        Test function for setDescription()
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        movie.setDescription("Second movie ever")
        self.assertEqual(movie.getDescription(), "Second movie ever")

    def test_setGenre(self):
        """
        Test function for setGenre()
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        movie.setGenre("Comedy")
        self.assertEqual(movie.getGenre(), "Comedy")

    def test_setReleaseYear(self):
        """
        Test function for setReleaseYear()
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        movie.setReleaseYear(1900)
        self.assertEqual(movie.getReleaseYear(), 1900)

    def test_RentFunctions(self):
        """
        Test function for Renting functions
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)

        movie.wasRented()
        movie.wasRented()
        self.assertEqual(movie.getCopiesRented(), 2)

        movie.wasReturned()
        self.assertEqual(movie.getCopiesRented(), 1)


class TestMovieValidator(unittest.TestCase):

    def test_validateMovie(self):
        """
        Test function for validateMovie()
        """
        validator = MovieValidator()

        # Valid movie
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        try:
            validator.validateMovie(movie)
            result = True
        except ValueError:
            result = False
        self.assertTrue(result)

        # Invalid movies
        invalid_movies = [
            Movie(1, "  ", "First movie ever", "Action", 1878, 0, False),
            Movie(1, "The Horse in Motion", "  ", "Action", 1878, 0, False),
            Movie(1, "The Horse in Motion", "First movie ever", "  ", 1878, 0, False),
            Movie(1, "The Horse in Motion", "First movie ever", "Action", 1877, 0, False)
        ]

        for movie in invalid_movies:
            with self.assertRaises(ValueError):
                validator.validateMovie(movie)


class TestRepoMovie(unittest.TestCase):

    def test_isEmpty(self):
        """
        Test function for isEmpty()
        """
        lst = MovieList()
        self.assertTrue(lst.isEmpty())

        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        self.assertFalse(lst.isEmpty())

    def test_getMovie(self):
        """
        Test function for getMovie()
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        self.assertEqual(lst.getMovie(1), movie)

    def test_addMovie(self):
        """
        Test function for addMovie()
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        self.assertEqual(lst.getAll(), [movie])

    def test_deleteMovie(self):
        """
        Test function for deleteMovie()
        :return:
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        self.assertFalse(lst.isEmpty())
        lst.deleteMovie(1)
        self.assertTrue(lst.isEmpty())

    def test_getAll(self):
        """
        Test function for getAll()
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        movie1 = Movie(2, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie1)
        self.assertEqual(lst.getAll(), [movie, movie1])

    def test_modifyMovie(self):
        """
        Test function for modifyMovie()
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        movie1 = Movie(1, "The Horse in the House", "First movie ever", "Action", 18, 0, False)
        lst.modifyMovie(movie1)
        modified_movie = lst.getMovie(1)
        self.assertEqual(modified_movie.getTitle(), movie1.getTitle())
        self.assertEqual(modified_movie.getReleaseYear(), movie1.getReleaseYear())


if __name__ == '__main__':
    unittest.main()
