from domainmodel.movie import Movie

class WatchList:

    def __init__(self):
        self.__watchlist = list()

    @property
    def watchlist(self):
        return self.__watchlist

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