from testing.test_all import AssembleTests
from service import serviceClient
from service import serviceMovie
import domain.Client as Client
import domain.Movie as Movie
import repository.movieList as movieList
import repository.clientList as clientList
import ui.terminal as terminal


AssembleTests.testAll()
clientValidator = Client.ClientValidator()
clientRepo = clientList.ClientList()
movieValidator = Movie.MovieValidator()
movieRepo = movieList.MovieList()
clientService = serviceClient.ServiceClient(clientRepo, clientValidator)
movieService = serviceMovie.ServiceMovie(movieRepo, movieValidator)

UI = terminal.Terminal(clientService, movieService)


UI.run()