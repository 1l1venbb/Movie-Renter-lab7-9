class Terminal:

    def __init__(self, ClientService, MovieService, RentService):
        self.ClientService = ClientService
        self.MovieService = MovieService
        self.RentService = RentService
        self.commands ={

            "add_client":self.uiAddClient,
            "add_movie":self.uiAddMovie,
            "add_rent":self.uiAddRent,
            "add_return":self.uiAddReturn,

            "print_clients":self.uiPrintClients,
            "print_movies":self.uiPrintMovies,
            "print_rents":self.uiPrintRents,

            "delete_client":self.uiDeleteClient,
            "delete_movie":self.uiDeleteMovie,
            "delete_rent":self.uiDeleteRent,

            "modify_client":self.uiModifyClient,
            "modify_movie":self.uiModifyMovie,
            "modify_rent":self.uiModifyRent,

            "search_client_by_first_name":self.uiSearchClientByFirstName,
            "search_client_by_last_name":self.uiSearchClientByLastName,
            "search_client_by_cnp":self.uiSearchClientByCNP,
            "search_movie_by_title":self.uiSearchMovieByTitle,
            "search_movie_by_genre":self.uiSearchMovieByGenre,
            "search_movie_by_release_year":self.uiSearchMovieByReleaseYear,
            "search_rent_by_client_id":self.uiSearchRentByClientID,
            "search_rent_by_movie_id":self.uiSearchRentByMovieID,

            "generate_clients":self.uiGenerateClients


        }

    def uiAddClient(self):
        """
        UI function for adding a client.
        """
        while True:
            try:
                ID = int(input("Enter client ID:"))
                break
            except ValueError:
                print("Invalid ID")

        firstName = input("Enter the clients first name:")
        lastName = input("Enter the clients last name:")
        cnp = input("Enter the clients CNP:")
        try:
            self.ClientService.addClientService(ID, firstName, lastName, cnp)
        except Exception as e:
            print(e)

    def uiAddMovie(self):
        """
        UI function for adding a movie.
        """
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
        try:
            self.MovieService.addMovieService(ID, title, description, genre, releaseYear)
        except Exception as e:
            print(e)

    def uiAddRent(self):
        """
        UI function for adding a rent.
        """
        while True:
            try:
                ID = int(input("Enter rent ID:"))
                break
            except ValueError:
                print("Invalid ID")

        while True:
            try:
                clientID = int(input("Enter client ID:"))
                break
            except ValueError:
                print("Invalid ID")

        while True:
            try:
                movieID = int(input("Enter movie ID:"))
                break
            except ValueError:
                print("Invalid ID")

        while True:
            try:
                day = int(input("Enter day of rent:"))
                month = int(input("Enter month of rent:"))
                year = int(input("Enter year of rent:"))
                break
            except ValueError:
                print("Invalid date")

        try:
            self.RentService.addRentService(ID, clientID, movieID, day, month, year)
        except Exception as e:
            print(e)

    def uiAddReturn(self):
        """
        Marks a rented movie as returned
        :return:
        """

        try:
            ID = int(input("Enter rent ID to return:"))
            if self.RentService.getRentService(ID) is None:
                print("Rent ID not found")
                return

        except ValueError:
            print("Invalid ID")
            return

        while True:
            try:
                day = int(input("Enter day of return:"))
                month = int(input("Enter month of return:"))
                year = int(input("Enter year of return:"))
                break
            except ValueError:
                print("Invalid date")

        try:
            self.RentService.addReturnService(ID, day, month, year)
        except Exception as e:
            print(e)



    def uiPrintClients(self):
        """
        UI function for printing clients
        """
        clients = self.ClientService.getAllClientsService()

        if len(clients) == 0:
            print("There are no clients")

        for client in clients:
            print(client)

    def uiPrintMovies(self):
        """
        UI function for printing movies
        """
        movies = self.MovieService.getAllMoviesService()

        if len(movies) == 0:
            print("There are no movies")

        for movie in movies:
            print(movie)

    def uiPrintRents(self):
        """
        UI function for printing rents
        """

        rents = self.RentService.getAllRentsService()
        if len(rents) == 0:
            print("There are no rents")

        for rent in rents:
            print(rent)

    def uiDeleteClient(self):
        """
        UI function for deleting a client
        """
        while True:
            try:
                ID = int(input("Enter client ID to delete:"))
                break
            except ValueError:
                print("Invalid ID")

        try:
            self.ClientService.deleteClientService(ID)
        except Exception as e:
            print(e)

    def uiDeleteMovie(self):
        """
        UI function for deleting a movie
        """
        while True:
            try:
                ID = int(input("Enter movie ID to delete:"))
                break
            except ValueError:
                print("Invalid ID")
        try:
            self.MovieService.deleteMovieService(ID)
        except Exception as e:
            print(e)

    def uiDeleteRent(self):
        """
        UI function for deleting a rent
        """
        while True:
            try:
                ID = int(input("Enter rent ID to delete:"))
                break
            except ValueError:
                print("Invalid ID")

        try:
            self.RentService.deleteRentService(ID)
        except Exception as e:
            print(e)

    def uiModifyClient(self):
        """
        UI function for modifying a clients ID, first name, last name and CNP
        """
        try:
            ID = int(input("Enter client ID to modify:"))
            if not self.ClientService.getClientService(ID):
                print("Client ID not found, please try again.")

        except ValueError:
            print("Invalid ID")
            return
        firstName = input("Enter the new first name (leave empty to keep current):")
        lastName = input("Enter the new last name (leave empty to keep current):")
        cnp = input("Enter the new CNP (leave empty to keep current):")

        self.ClientService.modifyClientService(ID, firstName, lastName, cnp)

    def uiModifyMovie(self):
        """
        UI function for modifying a movie ID, title, description, genre and release year
        """

        try:
            ID = int(input("Enter movie ID to modify:"))
            if not self.MovieService.getMovieService(ID):
                print("Movie ID not found, please try again.")
                return
        except ValueError:
            print("Invalid ID")
            return


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

    def uiModifyRent(self):
        """
        UI function for modifying a rent's id, client id, movie id, rent date, return date
        """
        try:
            ID = int(input("Enter rent ID to modify:"))
            if self.RentService.getRentService(ID) is None:
                print("Rent ID not found, please try again.")
                return

        except ValueError:
            print("Invalid ID")
            return


        newID = input("Enter new ID(leave empty to keep current):")
        clientID = input("Enter new client ID(leave empty to keep current):")
        movieID = input("Enter new movie ID(leave empty to keep current):")
        rentDay = input("Enter new rent day(leave empty to keep current):")
        rentMonth = input("Enter new rent month(leave empty to keep current):")
        rentYear = input("Enter new rent year(leave empty to keep current):")
        returnDay = input("Enter new return day(leave empty to keep current):")
        returnMonth = input("Enter new return month(leave empty to keep current):")
        returnYear = input("Enter new return year(leave empty to keep current):")

        self.RentService.modifyRentService(ID, newID, clientID, movieID, rentDay, rentMonth, rentYear, returnDay, returnMonth, returnYear, self.ClientService.getAllClientsService(), self.MovieService.getAllMoviesService())

    def uiSearchClientByFirstName(self):
        """
        UI function for searching a client by first name
        """
        clients = []
        while True:
            firstName = input("Enter the first name to search for:")
            if firstName != "":
                break
            else:
                print("First name can't be empty.")
        try:
            clients = self.ClientService.searchClientByFirstName(firstName)
        except ValueError:
            print("There are no clients with the first name " + firstName.strip() + ".")

        for client in clients:
            print(client)

    def uiSearchClientByLastName(self):
        """
        UI function for searching a client by last name
        """
        clients = []
        while True:
            lastName = input("Enter the last name to search for:")
            if lastName != "":
                break
            else:
                print("last name can't be empty.")
        try:
            clients = self.ClientService.searchClientByLastName(lastName)
        except ValueError:
            print("There are no clients with the last name " + lastName.strip() + ".")

        for client in clients:
            print(client)

    def uiSearchClientByCNP(self):
        """
        UI function for searching a client by CNP
        """
        while True:
            cnp = input("Enter the CNP to search for:")
            if cnp != "" and len(cnp)== 13:
                break
            else:
                print("CNP is invalid.")

        client = self.ClientService.searchClientByCNP(cnp.strip())

        if client is None:
            print("There are no clients with the CNP " + cnp.strip() + ".")
        else :
            print(client)

    def uiSearchMovieByTitle(self):
        """
        UI function for searching a movie by title
        """
        movies = []
        while True:
            title = input("Enter the first name to search for:")
            if title != "":
                break
            else:
                print("First name can't be empty.")

        try:
            movies = self.MovieService.searchByTitle(title)
        except ValueError:
            print("There are no movies with the title " + title.strip() + ".")

        for movie in movies:
            print(movie)

    def uiSearchMovieByGenre(self):
        """
        UI function for searching a movie by genre
        """
        movies = []
        while True:
            genre = input("Enter the genre to search for:")
            if genre != "":
                break
            else:
                print("Genre can't be empty.")

        try:
            movies = self.MovieService.searchByGenre(genre)
        except ValueError:
            print("There are no movies with the genre " + genre.strip() + ".")

        for movie in movies:
            print(movie)

    def uiSearchMovieByReleaseYear(self):
        """
        UI function for searching a movie by release year
        """
        movies = []
        year = 0
        while True:
            try:
                year = int(input("Enter the release year to search for:"))
            except ValueError:
                print("Year has to be a number between 1878 and 2024")
            if year >= 1878 or year <= 2024:
                break
            else:
                print("Release year invalid.")

        try:
            movies = self.MovieService.searchByReleaseYear(year)
        except ValueError:
            print("There are no movies released in the year " + str(year) + ".")

        for movie in movies:
            print(movie)

    def uiSearchRentByClientID(self):
        """
        UI function for searching a rent by client ID
        """

        rents = []
        while True:
            try:
                clientID = int(input("Enter the client ID to search for:"))
                break
            except ValueError:
                print("Invalid ID")

        try:
            rents = self.RentService.searchRentByClientID(clientID)
        except ValueError as ve:
            print(ve)

        for rent in rents:
            print(rent)

    def uiSearchRentByMovieID(self):
        """
        UI function for searching a rent by movie ID
        """
        rents = []
        while True:
            try:
                movieID = int(input("Enter the client ID to search for:"))
                break
            except ValueError:
                print("Invalid ID")

        try:
            rents = self.RentService.searchRentByMovieID(movieID)
        except ValueError as ve:
            print(ve)

        for rent in rents:
            print(rent)

    def uiGenerateClients(self):
        """
        UI function for generating clients
        """
        while True:
            try:
                count = int(input("Enter the number of clients you want to generate:"))
                break
            except ValueError:
                print("Invalid number of clients.")

        for i in range(count):
            self.ClientService.generateClientService()


    def run(self):
        """
        Reads commands and runs them
        """
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