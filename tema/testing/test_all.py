from . import test_client, test_rent
from . import test_movie
from . import test_utils

class AssembleTests:
    @staticmethod
    def testAll():
       testClient = test_client.TestClient()
       testClient.run_all_tests()
       testClient = test_client.TestClientValidator()
       testClient.run_all_tests()
       testClient = test_client.TestRepoClient()
       testClient.run_all_tests()
       testClient = test_client.TestClientService()
       testClient.run_all_tests()

       testMovie = test_movie.TestMovie()
       testMovie.run_all_tests()
       testMovie = test_movie.TestMovieValidator()
       testMovie.run_all_tests()
       testMovie = test_movie.TestRepoMovie()
       testMovie.run_all_tests()

       testRent = test_rent.TestRent()
       testRent.run_all_tests()
       testRentValidator = test_rent.TestRentValidator()
       testRentValidator.run_all_tests()

       testUtils = test_utils.TestRandomClient()
       testUtils.run_all_tests()