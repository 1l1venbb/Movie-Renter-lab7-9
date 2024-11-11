class Terminal:

    def __init__(self, ClientService, MovieService):
        self.ClientService = ClientService
        self.MovieService = MovieService
        self.commands ={

            "add_client":self.uiAddClient,
            "add_movie":self.uiAddMovie,
            "print_clients":self.uiPrintClients,
            "print_movies":self.uiPrintMovies

        }

    def uiAddClient(self, ID, firstName, lastName, cnp):

        pass