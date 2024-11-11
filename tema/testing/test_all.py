from . import test_client
from . import test_movie

class AssembleTests:
    @staticmethod
    def testAll():
       testClient = test_client.TestClient()
       testClient.run_all_tests()
       testClient = test_client.TestClientValidator()
       testClient.run_all_tests()
       testMovie = test_movie.TestMovie()
       testMovie.run_all_tests()
       testMovie = test_movie.TestMovieValidator()
       testMovie.run_all_tests()
