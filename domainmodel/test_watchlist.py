from domainmodel.movie import Movie
from domainmodel.watchlist import WatchList


def test_iter():
    w = WatchList()
    w.add_movie(Movie("Moana", 2016))
    w.add_movie(Movie("Ice Age", 2002))
    w.add_movie(Movie("Guardians of the Galaxy", 2012))
    iterable = iter(w)
    assert(next(iterable) == Movie("Moana", 2016)) == True