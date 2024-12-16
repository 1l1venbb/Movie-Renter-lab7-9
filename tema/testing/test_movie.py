import unittest
from domain.Movie import Movie, MovieValidator
from repository.movieList import MovieList
from service.serviceMovie import ServiceMovie


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

    def test_getCopiesRented(self):
        """
        Test function for getCopiesRented()
        """
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        self.assertEqual(movie.getCopiesRented(), 0)

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

    def test_len(self):
        """
        Test function for len()
        """
        lst = MovieList()

        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        self.assertEqual(len(lst), 1)
        movie = Movie(2, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        self.assertEqual(len(lst), 2)

    def test_getMovie(self):
        """
        Test function for getmovie()
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        self.assertEqual(lst.getMovie(1), movie)
        self.assertEqual(lst.getMovie(2), None)

    def test_isIDUnique(self):
        """
        Test function for isIDUnique()
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        movie = Movie(2, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        result=True
        try:
            lst.isIDUnique(1)
            result = False
        except ValueError:
            self.assertTrue(result)

    def test_isEmpty(self):
        """
        Test function for isEmpty()
        """
        lst = MovieList()
        self.assertTrue(lst.isEmpty())

        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        self.assertFalse(lst.isEmpty())

    def test_addMovie(self):
        """
        Test function for addMovie()
        """
        lst = MovieList()
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        self.assertEqual(lst.getAll(), [movie])
        movie = Movie(1, "The Cat in Motion", "First movie ever", "Action", 1878, 0, False)

        result = True
        try:
            lst.addMovie(movie)
            result = False
        except ValueError:
            self.assertTrue(result)

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
        result = True
        try:
            lst.deleteMovie(1)
            result = False
        except ValueError:
            self.assertTrue(result)

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


class TestMovieService(unittest.TestCase):

    def test_addMovie(self):
        """
        Test function for addMovie()
        """
        movieValidator = MovieValidator()
        movieRepo = MovieList()
        service = ServiceMovie(movieRepo, movieValidator)

        service.addMovieService(1, "The Horse in Motion", "First movie ever made", "Action", 1887)
        movie = movieRepo.getMovie(1)
        self.assertEqual(movieRepo.getAll(), [movie])

    def test_getAllMoviesService(self):
        movieValidator = MovieValidator()
        movieRepo = MovieList()
        service = ServiceMovie(movieRepo, movieValidator)

        movie1 = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        movieRepo.addMovie(movie1)
        movie2 = Movie(2, "The Cat in Motion", "First movie ever", "Action", 1878, 0, False)
        movieRepo.addMovie(movie2)

        self.assertEqual(service.getAllMoviesService(), [movie1, movie2])

    def test_deleteMovieService(self):
        """
        Test function for deleteMovieService()
        """
        lst = MovieList()
        service = ServiceMovie(lst, MovieValidator())
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        service.deleteMovieService(1)
        self.assertEqual(lst.getAll(), [])

    def test_getMovieService(self):
        """
        Test function for getMovieService()
        """
        lst = MovieList()
        service = ServiceMovie(lst, MovieValidator())
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        self.assertEqual(service.getMovieService(1), movie)

    def test_modifyMovieService(self):
        """
        Test function for modifyMovieService()
        """
        lst = MovieList()
        service = ServiceMovie(lst, MovieValidator())
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        result = True

        try:
            service.modifyMovieService(1, "The Cat in Motion", "First movie ever made", "Action", 1887)
        except ValueError:
            result = False
        self.assertTrue(result)

        try:
            service.modifyMovieService(1, "", "First movie ever made", "Action", 1887)
        except ValueError:
            result = False
        self.assertTrue(result)

        try:
            service.modifyMovieService(1, "The Cat in Motion", "", "Action", 1887)
        except ValueError:
            result = False
        self.assertTrue(result)

        try:
            service.modifyMovieService(1, "The Cat in Motion", "First movie ever made", "", 1887)
        except ValueError:
            result = False
        self.assertTrue(result)

        try:
            service.modifyMovieService(1, "The Cat in Motion", "First movie ever made", "Action", 1887)
        except ValueError:
            result = False
        self.assertTrue(result)

        try:
            service.modifyMovieService(1, "The Cat in Motion", "First movie ever made", "Action", "")
        except ValueError:
            result = False
        self.assertTrue(result)


    def test_searchByTitle(self):
        """
        Test function for searchByTitle()
        """
        lst = MovieList()
        service = ServiceMovie(lst, MovieValidator())
        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)
        result = True

        self.assertEqual(service.searchByTitle("The Horse in Motion"), [movie])
        try:
            service.searchByTitle("asdasdsa")
            result = False
        except ValueError:
            self.assertTrue(result)

    def test_searchByGenre(self):
        """
        Test function for searchByGenre()
        """
        lst = MovieList()
        service = ServiceMovie(lst, MovieValidator())
        result = True

        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)


        self.assertEqual(service.searchByGenre("Action"), [movie])
        try:
            service.searchByGenre("asdasdsa")
            result = False
        except ValueError:
            self.assertTrue(result)

    def test_searchByReleaseYear(self):
        """
        Test function for searchByReleaseYear()
        """
        lst = MovieList()
        service = ServiceMovie(lst, MovieValidator())
        result = True

        movie = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 0, False)
        lst.addMovie(movie)

        self.assertEqual(service.searchByReleaseYear(1878), [movie])
        try:
            service.searchByReleaseYear("asdasdsa")
            result = False
        except ValueError:
            self.assertTrue(result)

    def test_generateMovieService(self):
        """
        Test function for generateMovieService()
        """
        lst = MovieList()
        service = ServiceMovie(lst, MovieValidator())

        service.generateMovieService()
        self.assertEqual((len(lst.getAll())), 1)
        self.assertTrue(isinstance(lst.getAll()[0], Movie))

    def test_showLeastRentedMoviesService(self):
        """
        Test function for showLeastRentedMoviesService()
        """
        lst = MovieList()
        service = ServiceMovie(lst, MovieValidator())
        movie1 = Movie(1, "The Horse in Motion", "First movie ever", "Action", 1878, 2, False)
        lst.addMovie(movie1)
        movie2 = Movie(2, "The Cat in Motion", "First movie ever", "Action", 1878, 1, False)
        lst.addMovie(movie2)
        movie3 = Movie(3, "The Horse in Motion", "First movie ever", "Comedy", 1878, 0, False)
        lst.addMovie(movie3)
        self.assertEqual(service.showLeastRentedMoviesService(), [movie3, movie2, movie1])

if __name__ == '__main__':
    unittest.main()
