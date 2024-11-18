from domain import Rent
from repository import rentList
from testing.test_all import AssembleTests
from service import serviceClient, serviceRent
from service import serviceMovie
import domain.Client as Client
import domain.Movie as Movie
import repository.movieList as movieList
import repository.clientList as clientList
import ui.terminal as terminal


print("Loading...")
AssembleTests.testAll()
print("Loaded!")

clientValidator = Client.ClientValidator()
clientRepo = clientList.ClientList()
clientService = serviceClient.ServiceClient(clientRepo, clientValidator)

movieValidator = Movie.MovieValidator()
movieRepo = movieList.MovieList()
movieService = serviceMovie.ServiceMovie(movieRepo, movieValidator)

rentValidator = Rent.RentValidator()
rentRepo = rentList.RentList()
rentService = serviceRent.ServiceRent(rentRepo, rentValidator)

UI = terminal.Terminal(clientService, movieService, rentService)


UI.run()