from domain import Rent
from testing.test_all import AssembleTests
from service import serviceClient, serviceRent
from service import serviceMovie
import domain.Client as Client
import domain.Movie as Movie
from repository.rentList import RentList
import repository.movieList as movieList
import repository.clientList as clientList
import repository.repoMemory as repoMemory
import ui.terminal as terminal


print("Loading...")
AssembleTests.testAll()
print("Loaded!")

clientValidator = Client.ClientValidator()
clientRepo = clientList.ClientList()
clientMemory = repoMemory.FileRepoClients("clients.txt")
clientService = serviceClient.ServiceClient(clientMemory, clientValidator)

movieValidator = Movie.MovieValidator()
movieRepo = movieList.MovieList()
movieMemory = repoMemory.FileRepoMovies("movies.txt")
movieService = serviceMovie.ServiceMovie(movieMemory, movieValidator)

rentValidator = Rent.RentValidator()
rentRepo = RentList()
rentMemory = repoMemory.FileRepoRents("rents.txt")
rentService = serviceRent.ServiceRent(rentMemory, rentValidator, movieMemory, clientMemory)

UI = terminal.Terminal(clientService, movieService, rentService)

UI.run()
