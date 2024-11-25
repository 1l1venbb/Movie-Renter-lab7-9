from domain.Movie import Movie
from .clientList import ClientList
from.movieList import MovieList
from domain.Client import Client


class FileRepoClients(ClientList):
    def __init__(self, file_name):
        """
        Constructor for FileRepoClients
        :param file_name: Name of the file that saves clients
        """
        super().__init__()
        self.file_name = file_name

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
                    ID = int(parts[0])
                    firstName = parts[1]
                    lastName = parts[2]
                    cnp = parts[3]
                    client = Client(ID, firstName, lastName, cnp)
                    self.clients.append(client)

    def writeToFile(self):
        """
        Writes to memory the current list of clients.
        """
        with open(self.file_name, 'w') as f:
            for client in self.clients:
                f.write(f"{str(client.getID())},{client.getFirstName()},{client.getLastName()},{client.getCNP()} \n")

    def addClientInMemory(self, client):
        """
        Adds a client to memory.
        :param client: Client object
        """
        self.readFromFile()
        ClientList.addClient(self, client)
        self.writeToFile()

    def getAllInMemory(self):
        """
        Returns all clients from memory.
        :return: list
        """
        self.readFromFile()
        return ClientList.getAll(self)

    def searchClient(self, ID):
        """
        Searches a client by his ID
        :param ID: ID of the client (int)
        :return: Client object
        """
        self.readFromFile()
        return ClientList.getClient(self, ID)

class FileRepoMovies(MovieList):

    def __init__(self, file_name):
        """
        Constructor for FileRepoMovies
        :param file_name: Name of the file that saves movies
        """
        super().__init__()
        self.file_name = file_name

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
                    ID = int(parts[0])
                    title = parts[1]
                    description = parts[2]
                    genre = parts[3]
                    releaseYear = int(parts[4])
                    copiesRented = int(parts[5])
                    movie = Movie(ID, title, description, genre, releaseYear, copiesRented)
                    self.movies.append(movie)

    def writeToFile(self):
        """
        Writes to memory the current list of movies.
        """
        with open(self.file_name, 'w') as f:
            for movie in self.movies:
                f.write(f"{str(movie.getID())},{movie.getTitle()},{movie.getDescription()},{movie.getGenre()},{movie.getReleaseYear()},{movie.getCopiesRented()} \n")

    def addMovieInMemory(self, movie):
        """
        Add a movie to memory.
        :param movie: Movie object
        """
        self.readFromFile()
        MovieList.addMovie(self, movie)
        self.writeToFile()

    def getAllInMemory(self):
        """
        Returns all movies from memory.
        :return: list
        """

        self.readFromFile()
        return MovieList.getAll(self)

    def searchMovie(self, ID):
        """
        Searches a movie by his ID
        :param ID: ID of the movie (int)
        :return: Movie Object
        """
        self.readFromFile()
        return MovieList.getMovie(self, ID)

