from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.movie import Movie
from domainmodel.user import User


class WatchList:

    def __init__(self, user: User, watchlist_name: str):
        if type(user) is not User:
            raise Exception("Sorry, that is an invalid User")
        else:
            self.__watchlist_owner = user
        if type(watchlist_name) is not str or watchlist_name == "":
            self.__watchlist_name = "New Watchlist"
        else:
            self.__watchlist_name = watchlist_name.strip()
        self.__watchlist = list()

    @property
    def watchlist(self):
        return self.__watchlist

    @property
    def watchlist_owner(self):
        return self.__watchlist_owner

    @property
    def watchlist_name(self):
        return self.__watchlist_name

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__watchlist):
            result = self.__watchlist[self.__index]
            self.__index += 1
            return result
        else:
            raise StopIteration

    def add_movie(self, movie):
        if not isinstance(movie, Movie):
            raise Exception("Only Movies can be added to the watchlist")
        elif movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self, movie):
        if not isinstance(movie, Movie):
            raise Exception("Only Movies can be removed from the watchlist")
        elif movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if not isinstance(index, int):
            return None
        elif index < 0 or index > (len(self.__watchlist) - 1):
            return None
        else:
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) == 0:
            return None
        else:
            return self.__watchlist[0]

    def clear_watchlist(self):
        self.__watchlist.clear()

    def share_watchlist(self, user):
        if not isinstance(user, User):
            raise Exception("A valid User is required")
        else:
            new_watchlist = WatchList(user,"")
            for movie in self.__watchlist:
                new_watchlist.add_movie(movie)
            return new_watchlist

    def sort_watchlist_by_title(self):
        def get_movie_title(movie):
            return movie.title
        return sorted(self.__watchlist, key = get_movie_title)

    def sort_watchlist_by_year(self):
        def get_movie_year(movie):
            return movie.release_year
        return sorted(self.__watchlist, key = get_movie_year)

    def sort_watchlist_by_runtime(self):
        def get_movie_runtime(movie):
            return movie.runtime_minutes
        return sorted(self.__watchlist, key = get_movie_runtime)

    def change_watchlist_name(self, new_name):
        if isinstance(new_name, str) or new_name != "":
            self.__watchlist_name = new_name

    def get_recommendations(self, filename):
        if not isinstance(filename, str):
            raise Exception("Invalid filename")
        elif len(self.__watchlist) == 0:
            raise Exception("Sorry, there are no recommendations for now")
        else:
            new_watchlist = WatchList(self.watchlist_owner,"Movie Recommendations")
            movie_file_reader = MovieFileCSVReader(filename)
            movie_file_reader.read_csv_file()
            for new_movie in movie_file_reader.dataset_of_movies:
                for current_movie in self.__watchlist:
                    if sorted(new_movie.genres) == sorted(current_movie.genres):
                        new_watchlist.add_movie(new_movie)
            return new_watchlist



