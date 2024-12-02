from domain.Movie import Movie
from .clientList import ClientList
from.movieList import MovieList
from domain.Client import Client
from .rentList import RentList
from domain.Rent import Rent

class FileRepoClients(ClientList):
    def __init__(self, file_name):
        """
        Constructor for FileRepoClients
        :param file_name: Name of the file that saves clients
        """
        super().__init__()
        self.file_name = file_name

        try:
            f = open(self.file_name, 'x')
        except FileExistsError:
            pass

        self.readFromFile()

    def __len__(self):
        """
        Returns the number of clients from memory.
        :return: int
        """
        self.readFromFile()
        return ClientList.__len__(self)

    def readFromFile(self):
        """
        Reads all clients from memory and makes a list of them.
        """
        with open(self.file_name, 'r') as f:
            self.clients.clear()
            lines = f.readlines()
            for line in lines:
                if line != '':
                    parts = line.split(',')
                    ID = int(parts[0].strip())
                    firstName = parts[1].strip()
                    lastName = parts[2].strip()
                    cnp = parts[3].strip()
                    copiesRented = int(parts[4].strip())
                    client = Client(ID, firstName, lastName, cnp, copiesRented)
                    self.clients.append(client)

    def writeToFile(self):
        """
        Writes to memory the current list of clients.
        """
        with open(self.file_name, 'w') as f:
            for client in self.clients:
                f.write(f"{str(client.getID())},{client.getFirstName()},{client.getLastName()},{client.getCNP()},{str(client.getCopiesRented())} \n")

    def addClient(self, client):
        """
        Adds a client to memory.
        :param client: Client object
        """
        self.readFromFile()
        ClientList.addClient(self, client)
        self.writeToFile()

    def getAll(self):
        """
        Returns all clients from memory.
        :return: list
        """
        self.readFromFile()
        return ClientList.getAll(self)

    def getClient(self, ID):
        """
        Searches a client by his ID
        :param ID: ID of the client (int)
        :return: Client object
        """
        self.readFromFile()
        return ClientList.getClient(self, ID)

    def modifyClient(self, client):
        self.readFromFile()
        ClientList.modifyClient(self, client)
        self.writeToFile()

class FileRepoMovies(MovieList):

    def __init__(self, file_name):
        """
        Constructor for FileRepoMovies
        :param file_name: Name of the file that saves movies
        """
        super().__init__()
        self.file_name = file_name
        try:
            f = open(self.file_name, 'x')
        except FileExistsError:
            pass

        self.readFromFile()

    def __len__(self):
        """
        Returns the number of movies from memory
        :return: list
        """
        self.readFromFile()
        return MovieList.__len__(self)

    def readFromFile(self):
        """
        Reads all movies from memory and makes a list of them.
        """
        with open(self.file_name, 'r') as f:
            self.movies.clear()
            lines = f.readlines()
            for line in lines:
                if line != '':
                    parts = line.split(',')
                    ID = int(parts[0].strip())
                    title = parts[1].strip()
                    description = parts[2].strip()
                    genre = parts[3].strip()
                    releaseYear = int(parts[4].strip())
                    copiesRented = int(parts[5].strip())
                    movie = Movie(ID, title, description, genre, releaseYear, copiesRented)
                    self.movies.append(movie)

    def writeToFile(self):
        """
        Writes to memory the current list of movies.
        """
        with open(self.file_name, 'w') as f:
            for movie in self.movies:
                f.write(f"{str(movie.getID())},{movie.getTitle()},{movie.getDescription()},{movie.getGenre()},{movie.getReleaseYear()},{movie.getCopiesRented()} \n")

    def addMovie(self, movie):
        """
        Add a movie to memory.
        :param movie: Movie object
        """
        self.readFromFile()
        MovieList.addMovie(self, movie)
        self.writeToFile()

    def getAll(self):
        """
        Returns all movies from memory.
        :return: list
        """

        self.readFromFile()
        return MovieList.getAll(self)

    def getMovie(self, ID):
        """
        Searches a movie by his ID
        :param ID: ID of the movie (int)
        :return: Movie Object
        """
        self.readFromFile()
        return MovieList.getMovie(self, ID)

    def modifyMovie(self, movie):
        self.readFromFile()
        MovieList.modifyMovie(self, movie)
        self.writeToFile()

class FileRepoRents(RentList):

    def __init__(self, file_name):
        """
        Constructor for FileRepoRents
        :param file_name: Name of the file that saves rents
        """
        super().__init__()
        self.file_name = file_name
        try:
            f = open(self.file_name, 'x')
        except FileExistsError:
            pass

        self.readFromFile()

    def __len__(self):
        """
        Returns the number of rents from memory
        :return: int
        """
        self.readFromFile()
        return RentList.__len__(self)

    def readFromFile(self):
        """
        Reads all rents from memory and makes a list of them.
        """
        with open(self.file_name, 'r') as f:
            self.rents.clear()
            lines = f.readlines()
            for line in lines:
                if line != '':
                    parts = line.split(',')
                    ID = int(parts[0].strip())
                    clientID = int(parts[1].strip())
                    movieID = int(parts[2].strip())
                    rentDay = int(parts[3].strip())
                    rentMonth = int(parts[4].strip())
                    rentYear = int(parts[5].strip())
                    returnDay = int(parts[6].strip())
                    returnMonth = int(parts[7].strip())
                    returnYear = int(parts[8].strip())
                    rent = Rent(ID, clientID, movieID, rentDay, rentMonth, rentYear, returnDay, returnMonth, returnYear)
                    self.rents.append(rent)

    def writeToFile(self):
        """
        Writes to memory the current list of rents.
        """
        with open(self.file_name, 'w') as f:
            for rent in self.rents:
                f.write(f"{str(rent.getID())},{str(rent.getClientID())},{str(rent.getMovieID())},{str(rent.getRentDay())},{str(rent.getRentMonth())},{str(rent.getRentYear())},{str(rent.getReturnDay())},{str(rent.getReturnMonth())},{str(rent.getReturnYear())} \n")

    def addRent(self, rent):
        """
        Add a rent to memory.
        :param rent: Rent object
        """
        self.readFromFile()
        RentList.addRent(self, rent)
        self.writeToFile()

    def getAll(self):
        """
        Returns all rents from memory.
        """
        self.readFromFile()
        return RentList.getAll(self)

    def getRent(self, ID):
        """
        Searches a rent by his ID
        :param ID: ID of the rent (int)
        :return: Rent object
        """
        self.readFromFile()
        return RentList.getRent(self, ID)

    def modifyRent(self, rent, ID):
        self.readFromFile()
        RentList.modifyRent(self, rent, ID)
        self.writeToFile()