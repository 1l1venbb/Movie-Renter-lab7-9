class Terminal:

    def __init__(self, ClientService, MovieService):
        self.ClientService = ClientService
        self.MovieService = MovieService
        self.commands ={

            "add_client":self.uiAddClient,
            "add_movie":self.uiAddMovie,
            "print_clients":self.uiPrintClients,
            "print_movies":self.uiPrintMovies,
            "delete_client":self.uiDeleteClient,
            "delete_movie":self.uiDeleteMovie,
            "modify_client":self.uiModifyClient,
            "modify_movie":self.uiModifyMovie

        }

    def uiAddClient(self):
        while True:
            try:
                ID = int(input("Enter client ID:"))
                break
            except ValueError:
                print("Invalid ID")

        firstName = input("Enter the clients first name:")
        lastName = input("Enter the clients last name:")
        cnp = input("Enter the clients CNP:")

        self.ClientService.addClientService(ID, firstName, lastName, cnp)

    def uiAddMovie(self):
        while True:
            try:
                ID = int(input("Enter movie ID:"))
                break
            except ValueError:
                print("Invalid ID")
        title = input("Enter the movie title:")
        description = input("Enter the movie description:")
        genre = input("Enter the movie genre:")
        while True:
            try:
                releaseYear = int(input("Enter movie release year:"))
                break
            except ValueError:
                print("Year has to be a number between 1878 and 2024")

        self.MovieService.addMovieService(ID, title, description, genre, releaseYear)

    def uiPrintClients(self):
        clients = self.ClientService.getAllClientsService()

        if len(clients) == 0:
            print("There are no clients")

        for client in clients:
            print(client)

    def uiPrintMovies(self):
        movies = self.MovieService.getAllMoviesService()

        if len(movies) == 0:
            print("There are no movies")

        for movie in movies:
            print(movie)

    def uiDeleteClient(self):
        while True:
            try:
                ID = int(input("Enter client ID to delete:"))
                break
            except ValueError:
                print("Invalid ID")

        self.ClientService.deleteClientService(ID)

    def uiDeleteMovie(self):
        while True:
            try:
                ID = int(input("Enter movie ID to delete:"))
                break
            except ValueError:
                print("Invalid ID")

        self.MovieService.deleteMovieService(ID)

    def uiModifyClient(self):
        while True:
            try:
                ID = int(input("Enter client ID to modify:"))
                if self.ClientService.getClientService(ID):
                    break
                else:
                    print("Client ID not found, please try again.")
            except ValueError:
                print("Invalid ID")

        firstName = input("Enter the new first name (leave empty to keep current):")
        lastName = input("Enter the new last name (leave empty to keep current):")
        cnp = input("Enter the new CNP (leave empty to keep current):")

        self.ClientService.modifyClientService(ID, firstName, lastName, cnp)

    def uiModifyMovie(self):
        while True:
            try:
                ID = int(input("Enter movie ID to modify:"))
                if self.MovieService.getMovieService(ID) is None:
                    print("Movie ID not found, please try again.")
                else:
                    break
            except ValueError:
                print("Invalid ID")

        title = input("Enter the new title (leave empty to keep current):")
        description = input("Enter the new description (leave empty to keep current):")
        genre = input("Enter the new genre (leave empty to keep current):")
        while True:
            try:
                releaseYear = int(input("Enter the new release year (leave empty to keep current):"))
                break
            except ValueError:
                print("Invalid year, please try again.")

        self.MovieService.modifyMovieService(ID, title, description, genre, releaseYear)

    def run(self):
        while True:
            command = input(">>>")
            command = command.lower()
            command = command.strip()

            if command == "":
                continue

            if command == "exit":
                exit()

            if command in self.commands:
                try:
                    self.commands[command]()
                except ValueError as ve:
                    print(ve)
            else:
                print("Invalid command")